import fs from 'node:fs/promises';
import { existsSync } from 'node:fs';
import net from 'node:net';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

import { chromium } from 'playwright';

import { analyzeRecoverability, analyzeBenchmarkConsole, analyzeContinuousGenerator, analyzeNoGo } from '../../docs/workbench/lib/compute.js';
import { analyzeDiscoveryMixer } from '../../docs/workbench/lib/discoveryMixer.js';
import { DEFAULT_STATE, cloneState, encodeShareState, sanitizeState } from '../../docs/workbench/lib/state.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..', '..');
const DOCS_DIR = path.join(ROOT, 'docs');
const OUT_DIR = path.join(ROOT, 'data', 'generated', 'validations');
const JSON_PATH = path.join(OUT_DIR, 'browser_tool_qualification.json');

function mergeStatePatch(target, patch) {
  for (const [key, value] of Object.entries(patch ?? {})) {
    if (
      value &&
      typeof value === 'object' &&
      !Array.isArray(value) &&
      target[key] &&
      typeof target[key] === 'object' &&
      !Array.isArray(target[key])
    ) {
      target[key] = { ...target[key], ...value };
    } else {
      target[key] = value;
    }
  }
}

function makeState(lab, patch = {}) {
  const state = cloneState(DEFAULT_STATE);
  state.activeLab = lab;
  state.labs[lab] = cloneState(state.labs[lab]);
  mergeStatePatch(state.labs[lab], patch);
  return sanitizeState(state);
}

function makeUrl(origin, lab, patch = {}) {
  const state = makeState(lab, patch);
  const hash = encodeShareState(state);
  return `${origin}/workbench/index.html#state=${hash}`;
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

async function findFreePort() {
  return new Promise((resolve, reject) => {
    const server = net.createServer();
    server.unref();
    server.on('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      const port = typeof address === 'object' && address ? address.port : null;
      server.close((error) => {
        if (error) reject(error);
        else resolve(port);
      });
    });
  });
}

async function waitForServer(origin, timeoutMs = 15000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    try {
      const response = await fetch(`${origin}/workbench/index.html`);
      if (response.ok) return;
    } catch {
      // keep polling
    }
    await new Promise((resolve) => setTimeout(resolve, 250));
  }
  throw new Error(`Timed out waiting for static server at ${origin}`);
}

async function startStaticServer() {
  const port = await findFreePort();
  const proc = spawn('python3', ['-m', 'http.server', String(port), '--bind', '127.0.0.1'], {
    cwd: DOCS_DIR,
    stdio: 'ignore',
  });
  const origin = `http://127.0.0.1:${port}`;
  await waitForServer(origin);
  return {
    origin,
    proc,
    stop: async () => {
      if (!proc.killed) {
        proc.kill('SIGTERM');
      }
      await new Promise((resolve) => proc.on('exit', resolve));
    },
  };
}

async function getBodyText(page) {
  await page.waitForLoadState('networkidle');
  return (await page.locator('body').innerText()).replace(/\s+/g, ' ').trim();
}

async function exportText(page, buttonSelector) {
  const downloadPromise = page.waitForEvent('download');
  await page.click(buttonSelector);
  const download = await downloadPromise;
  const downloadPath = await download.path();
  assert(downloadPath, `Download path missing for ${buttonSelector}`);
  return fs.readFile(downloadPath, 'utf8');
}

async function clickButtonByText(page, pattern) {
  const result = await page.evaluate((source) => {
    const regex = new RegExp(source, 'i');
    const buttons = Array.from(document.querySelectorAll('button')).map((item) => (item.textContent ?? '').trim()).filter(Boolean);
    const button = Array.from(document.querySelectorAll('button')).find((item) => regex.test(item.textContent ?? ''));
    const heading = document.querySelector('h2')?.textContent ?? null;
    if (!button) return { clicked: false, buttons, heading };
    button.click();
    return { clicked: true, buttons, heading };
  }, pattern);
  assert(result.clicked, `Could not find button matching /${pattern}/i on heading "${result.heading}" with buttons ${JSON.stringify(result.buttons)}`);
}

async function loadScenario(page, origin, lab, patch = {}) {
  const url = makeUrl(origin, lab, patch);
  await page.goto(url);
  await page.waitForLoadState('networkidle');
  return url;
}

async function waitForActiveHeading(page, expectedText) {
  await page.waitForFunction((target) => {
    const heading = document.querySelector('h2');
    return Boolean(heading && heading.textContent && heading.textContent.includes(target));
  }, expectedText);
  const headingText = (await page.locator('h2').first().innerText()).trim();
  assert(headingText.includes(expectedText), `Expected active heading to include "${expectedText}" but saw "${headingText}"`);
}

async function run() {
  await fs.mkdir(OUT_DIR, { recursive: true });
  const server = await startStaticServer();
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ acceptDownloads: true });
  await context.grantPermissions(['clipboard-read', 'clipboard-write'], { origin: server.origin });
  const consoleMessages = [];
  const instrumentPage = (page) => {
    page.on('console', (message) => {
      consoleMessages.push({ type: message.type(), text: message.text() });
    });
    page.on('pageerror', (error) => {
      consoleMessages.push({ type: 'pageerror', text: error.message });
    });
  };
  const page = await context.newPage();
  instrumentPage(page);
  page.setDefaultTimeout(10000);

  const workflows = [];
  const mark = (label) => console.log(`[browser-qualification] ${label}`);

  try {
    // Exact success workflow
    mark('exact success workflow');
    await loadScenario(page, server.origin, 'exact', { protectedMagnitude: 1.4, disturbanceMagnitude: 0.9, angleDeg: 90 });
    await waitForActiveHeading(page, 'Exact Projection Lab');
    let bodyText = await getBodyText(page);
    assert(bodyText.includes('Exact theorem applies'), 'Exact lab did not show the exact theorem callout');
    const exactReport = await exportText(page, '#export-report');
    assert(exactReport.includes('active lab: exact'), 'Exact report export did not preserve the exact lab state');
    workflows.push({
      workflow: 'Exact recovery success workflow',
      status: 'pass',
      notes: 'Exact Projection Lab preserved the orthogonal exact-recovery anchor and exported the same verdict.',
    });

    // Home / guided route to benchmark console
    mark('guided benchmark route');
    await page.goto(`${server.origin}/workbench/index.html`);
    await page.waitForLoadState('networkidle');
    await page.getByRole('button', { name: /Run built-in benchmarks/i }).click();
    await waitForActiveHeading(page, 'Benchmark / Validation Console');
    const benchmarkText = await getBodyText(page);
    const benchmarkExpected = analyzeBenchmarkConsole({ suite: 'all', selectedDemo: 'periodic_modal_repair' });
    const benchmarkCsv = await exportText(page, '#export-csv');
    const benchmarkReport = await exportText(page, '#export-report');
    const benchmarkModuleCards = await page.locator('.benchmark-module-card').count();
    assert(benchmarkText.includes('Periodic modal augmentation'), 'Benchmark console did not show periodic modal demo');
    assert(benchmarkText.includes('Structural Discovery Studio'), 'Benchmark console did not show broadened module-health rows');
    assert(benchmarkModuleCards >= 8, `Benchmark module card count too small: ${benchmarkModuleCards}`);
    assert(benchmarkCsv.includes('boundary_architecture_repair'), 'Benchmark CSV export missing expected demo row');
    assert(benchmarkReport.includes('summary.demoCount'), 'Benchmark report export missing nested summary metrics');
    workflows.push({
      workflow: 'Guided benchmark route and export',
      status: 'pass',
      notes: `Guided entry opened the benchmark console with ${benchmarkExpected.summary.moduleCount} module rows and working CSV/report export.`,
    });

    // Structural discovery boundary failure -> repair -> reload -> share link
    mark('boundary diagnosis and repair workflow');
    const boundaryPatch = {
      system: 'boundary',
      boundaryArchitecture: 'periodic_transplant',
      boundaryProtected: 'bounded_velocity_class',
      boundaryGridSize: 17,
      boundaryDelta: 0.2,
    };
    const boundaryExpected = analyzeRecoverability(boundaryPatch);
    await loadScenario(page, server.origin, 'recoverability', boundaryPatch);
    await waitForActiveHeading(page, 'Structural Discovery Studio');
    bodyText = await getBodyText(page);
    assert(bodyText.includes(boundaryExpected.chosenRecommendation.title), 'Boundary recommendation missing from UI');
    assert(bodyText.includes('Impossible'), 'Boundary scenario did not show impossible status before repair');
    await page.locator('[data-apply-recommendation="0"]').first().click();
    await page.waitForFunction(() => document.body.innerText.includes('Exact on the restricted boundary-compatible finite-mode family'));
    bodyText = await getBodyText(page);
    assert(bodyText.includes('Exact on the restricted boundary-compatible finite-mode family'), 'Boundary repair did not move UI into exact regime');
    const repairedUrl = page.url();
    await page.click('#share-link');
    const sharedLink = await page.evaluate(() => navigator.clipboard.readText());
    assert(sharedLink === repairedUrl, 'Copied share link did not match the live repaired URL');
    const boundaryReport = await exportText(page, '#export-report');
    assert(boundaryReport.includes('boundary-compatible finite-mode Hodge'), 'Boundary report export missing repaired architecture');
    await page.reload();
    await page.waitForLoadState('networkidle');
    bodyText = await getBodyText(page);
    assert(bodyText.includes('Exact on the restricted boundary-compatible finite-mode family'), 'Reload lost the repaired boundary state');
    workflows.push({
      workflow: 'Failing setup → diagnosis → fix → verified success',
      status: 'pass',
      notes: 'Boundary architecture repair moved from impossible to exact, and share-link/reload preserved the repaired result.',
    });

    // Recoverability threshold case
    mark('periodic threshold workflow');
    const periodicPatch = {
      system: 'periodic',
      periodicObservation: 'cutoff_vorticity',
      periodicProtected: 'full_weighted_sum',
      periodicCutoff: 3,
      periodicDelta: 2,
    };
    const periodicExpected = analyzeRecoverability(periodicPatch);
    await loadScenario(page, server.origin, 'recoverability', periodicPatch);
    await waitForActiveHeading(page, 'Structural Discovery Studio');
    bodyText = await getBodyText(page);
    assert(bodyText.includes('Impossible below the protected-support cutoff'), 'Periodic threshold no-go explanation missing');
    assert(bodyText.includes(periodicExpected.chosenRecommendation.title), 'Periodic fix recommendation missing');
    await page.locator('[data-apply-recommendation="0"]').first().click();
    await page.waitForFunction(() => document.body.innerText.includes('Current retained modal support is sufficient.'));
    bodyText = await getBodyText(page);
    assert(bodyText.includes('Current retained modal support is sufficient.'), 'Periodic repair did not show the exact-support explanation');
    workflows.push({
      workflow: 'Threshold failure → cutoff augmentation → verified exact recovery',
      status: 'pass',
      notes: 'Periodic stronger-target threshold failure was diagnosed and repaired in the live studio.',
    });

    // Weaker-versus-stronger salvage workflow
    mark('weaker-versus-stronger salvage workflow');
    const qubitPatch = {
      system: 'qubit',
      qubitProtected: 'bloch_vector',
      qubitPhaseWindowDeg: 30,
      qubitDelta: 0.2,
    };
    await loadScenario(page, server.origin, 'recoverability', qubitPatch);
    await waitForActiveHeading(page, 'Structural Discovery Studio');
    bodyText = await getBodyText(page);
    assert(bodyText.includes('Weaken target to z coordinate only'), 'Qubit weaker-target recommendation missing');
    await page.locator('[data-apply-recommendation="0"]').first().click();
    await page.waitForFunction(() => {
      const text = document.body.innerText;
      return text.includes('z coordinate only') && text.includes('Exact');
    });
    bodyText = await getBodyText(page);
    assert(bodyText.includes('z coordinate only') && bodyText.includes('Exact'), 'Qubit weaker-target salvage did not reach exact recovery');
    workflows.push({
      workflow: 'Stronger target fails / weaker target succeeds',
      status: 'pass',
      notes: 'The qubit workflow correctly weakened the Bloch-vector target to the z coordinate and preserved the exact verdict after the change.',
    });

    // Discovery mixer structured repair
    const mixerStructuredPatch = {
      mode: 'structured',
      family: 'linear',
      structuredLinearProtected: 'x3',
      structuredLinearMeasurements: {
        measure_x1: true,
        measure_x2_plus_x3: true,
        measure_x2: false,
        measure_x3: false,
        measure_x1_plus_x2: false,
      },
    };
    const mixerExpected = analyzeDiscoveryMixer(mixerStructuredPatch);
    const mixerPage = await context.newPage();
    instrumentPage(mixerPage);
    mixerPage.setDefaultTimeout(10000);
    mark('structured mixer workflow');
    await loadScenario(mixerPage, server.origin, 'mixer', mixerStructuredPatch);
    await waitForActiveHeading(mixerPage, 'Discovery Mixer / Structural Composition Lab');
    bodyText = await getBodyText(mixerPage);
    assert(bodyText.includes(mixerExpected.chosenRecommendation.title), 'Mixer recommendation missing');
    assert(bodyText.includes('Impossible'), 'Mixer structured failure did not show impossible status');
    await clickButtonByText(mixerPage, 'Apply and compare');
    await mixerPage.waitForFunction(() => document.body.innerText.includes('Exact'));
    bodyText = await getBodyText(mixerPage);
    assert(bodyText.includes('Exact'), 'Mixer repair did not reach an exact result');
    const mixerJson = await exportText(mixerPage, '#export-json');
    const mixerPayload = JSON.parse(mixerJson);
    assert(mixerPayload.activeLab === 'mixer', 'Mixer JSON export did not preserve active lab');
    assert(mixerPayload.analysis.regime === 'exact', 'Mixer JSON export did not preserve repaired regime');
    workflows.push({
      workflow: 'Structured linear mixer failure → repair → JSON export',
      status: 'pass',
      notes: 'Typed linear mixer case repaired cleanly and exported the repaired exact state.',
    });

    // Unsupported custom mixer input
    mark('unsupported custom mixer workflow');
    const mixerUnsupportedPatch = {
      mode: 'custom',
      customFamily: 'linear',
      customLinearDimension: 3,
      customLinearObservationText: 'x1\nx2',
      customLinearProtectedText: 'sin(x3)',
      customLinearCandidateText: 'x3',
    };
    await loadScenario(mixerPage, server.origin, 'mixer', mixerUnsupportedPatch);
    await waitForActiveHeading(mixerPage, 'Discovery Mixer / Structural Composition Lab');
    bodyText = await getBodyText(mixerPage);
    const unsupportedExpected = analyzeDiscoveryMixer(mixerUnsupportedPatch);
    assert(unsupportedExpected.unsupported, 'Unsupported mixer case was expected to be unsupported');
    assert(bodyText.toLowerCase().includes('unsupported'), 'Mixer did not show unsupported status for nonlinear input');
    assert(await mixerPage.locator('[data-apply-mixer-recommendation]').count() === 0, 'Unsupported mixer case exposed a fake apply recommendation');
    workflows.push({
      workflow: 'Unsupported custom input → honest rejection',
      status: 'pass',
      notes: 'Custom nonlinear protected variable is rejected explicitly and no fake repair is offered.',
    });
    await mixerPage.close();

    // No-go explorer
    mark('no-go explorer workflow');
    const nogoPatch = { example: 'divergence-only' };
    const nogoExpected = analyzeNoGo(nogoPatch);
    await loadScenario(page, server.origin, 'nogo', nogoPatch);
    await waitForActiveHeading(page, 'No-Go Explorer');
    bodyText = await getBodyText(page);
    assert(bodyText.includes(nogoExpected.status), 'No-Go Explorer status did not match the live analysis');
    assert(await page.locator('[data-apply-recommendation]').count() === 0, 'No-Go Explorer exposed a fake repair action');
    workflows.push({
      workflow: 'Impossible setup → no-go explanation → no fake fix suggested',
      status: 'pass',
      notes: 'No-Go Explorer preserved the proved no-go without inventing a redesign path.',
    });

    // Physics example workflow
    mark('physics example workflow');
    const cfdPatch = {
      periodicGridSize: 12,
      boundedGridSize: 18,
      contamination: 0.22,
      poissonIterations: 320,
    };
    await loadScenario(page, server.origin, 'cfd', cfdPatch);
    await waitForActiveHeading(page, 'CFD Projection Lab');
    bodyText = await getBodyText(page);
    assert(bodyText.includes('Boundary-sensitive limit detected') || bodyText.includes('Recheck bounded example'), 'CFD lab did not surface the bounded-domain limit callout');
    assert(bodyText.includes('periodic') || bodyText.includes('Periodic'), 'CFD lab did not show the periodic exact branch context');
    const cfdReport = await exportText(page, '#export-report');
    assert(cfdReport.includes('bounded') && cfdReport.includes('periodic'), 'CFD report export did not preserve both periodic and bounded-domain context');
    workflows.push({
      workflow: 'Physics example workflow',
      status: 'pass',
      notes: 'CFD Projection Lab preserved the periodic exact branch and the bounded-domain limitation in both UI and exported report.',
    });

    // Continuous asymptotic-only workflow
    mark('continuous asymptotic workflow');
    const continuousPatch = {
      matrix: [[0, 0, 0], [0, 1, 1], [0, 0, 1.5]],
      x0: [2, -1, 0.5],
      time: 2,
      steps: 280,
      frame: 280,
    };
    const continuousExpected = analyzeContinuousGenerator(continuousPatch);
    await loadScenario(page, server.origin, 'continuous', continuousPatch);
    await waitForActiveHeading(page, 'Continuous Generator Lab');
    bodyText = await getBodyText(page);
    assert(bodyText.includes('Asymptotic'), 'Continuous lab did not show asymptotic status');
    assert(!continuousExpected.finiteTimeExactRecoveryPossible, 'Continuous benchmark was expected to remain finite-time impossible');
    workflows.push({
      workflow: 'Exact impossible / asymptotic possible workflow',
      status: 'pass',
      notes: 'Continuous generator lab preserved the finite-time exactness no-go and asymptotic-only interpretation.',
    });

    const errors = consoleMessages.filter((message) => message.type === 'error' || message.type === 'pageerror');
    const warnings = consoleMessages.filter((message) => message.type === 'warning');

    const result = {
      executedAt: new Date().toISOString(),
      origin: server.origin,
      workflows,
      console: {
        errorCount: errors.length,
        warningCount: warnings.length,
        errors,
        warnings,
      },
      qualified: workflows.every((item) => item.status === 'pass') && errors.length === 0,
      scope: 'high-risk workbench surfaces and real user workflows',
    };

    await fs.writeFile(JSON_PATH, JSON.stringify(result, null, 2), 'utf8');
    console.log(`wrote ${JSON_PATH}`);
  } finally {
    await browser.close();
    await server.stop();
  }
}

run().catch(async (error) => {
  await fs.mkdir(OUT_DIR, { recursive: true });
  const failure = {
    executedAt: new Date().toISOString(),
    qualified: false,
    error: error.message,
    stack: error.stack,
  };
  await fs.writeFile(JSON_PATH, JSON.stringify(failure, null, 2), 'utf8');
  console.error(error);
  process.exitCode = 1;
});
