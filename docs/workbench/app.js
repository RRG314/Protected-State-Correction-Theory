import {
  analyzeContinuousGenerator,
  analyzeExactProjection,
  analyzeMhdProjection,
  analyzeNoGo,
  analyzeQecSector,
  clamp,
  formatMatrix,
  formatVector,
} from './lib/compute.js';
import {
  DEFAULT_STATE,
  STORAGE_KEY,
  cloneState,
  decodeShareState,
  encodeShareState,
  exportScenarioPayload,
  sanitizeState,
} from './lib/state.js';

const LAB_META = {
  exact: {
    label: 'Exact Projection Lab',
    short: 'Orthogonal exact recovery and overlap failure.',
    status: 'PROVED / NO-GO',
    plain:
      'This module shows the cleanest exact branch of OCP. When the disturbance is truly orthogonal to the protected direction, projection recovers the protected component exactly. As soon as overlap is introduced, the same projector leaks disturbance into the recovered result.',
    technical:
      'Implements the finite-dimensional projector model H = S ⊕ D with recovery R = P_S. The overlap slider moves the example outside the admissible OCP hypotheses and turns the module into a counterexample illustrating OCP-T1 versus OCP-N1.',
    use: 'Use this to see the exact theorem and its failure mode in the smallest possible setting.',
    avoid: 'Do not treat a non-orthogonal case as an exact OCP system. The module shows why that would overclaim.',
    refs: [
      { title: 'Central theorem', href: '../theorem-candidates/central-theorem.md', note: 'OCP-T1 exact protected-subspace recovery' },
      { title: 'No-go results', href: '../impossibility-results/no-go-results.md', note: 'OCP-N1 overlap / indistinguishability' },
      { title: 'Operator constructions', href: '../operators/operator-constructions.md', note: 'Projector and complementary disturbance operator' },
    ],
  },
  qec: {
    label: 'QEC Sector Lab',
    short: '3-qubit bit-flip code in exact sector language.',
    status: 'PROVED / CONDITIONAL ANCHOR',
    plain:
      'This module treats QEC as the exact sector branch of OCP. The code space is the protected object, each bit-flip sector is a disturbance sector, and recovery works because the sectors stay distinguishable and can be mapped back without damaging the logical state.',
    technical:
      'Implements the 3-qubit bit-flip sector model using orthogonal sector bases and a sector-conditioned recovery operator. The exact statement is branch-specific: OCP is interpreting standard QEC structure, not replacing it.',
    use: 'Use this to see the strongest exact anchor system beyond the simple projector case.',
    avoid: 'Do not read this as a new QEC theorem. The novelty is the finished OCP framing, not the underlying code theory.',
    refs: [
      { title: 'QEC in OCP language', href: '../qec/qec-in-ocp.md', note: 'Protected space, sectors, and recovery map' },
      { title: 'Sector recovery theorem', href: '../theorem-candidates/sector-recovery-theorems.md', note: 'Exact orthogonal sector recovery and sector-overlap no-go' },
      { title: 'QEC foundations', href: '../qec/qec-foundations.md', note: 'Knill-Laflamme anchor and syndrome structure' },
    ],
  },
  mhd: {
    label: 'MHD Projection Lab',
    short: 'Exact periodic projection versus GLM damping.',
    status: 'PROVED / CONDITIONAL',
    plain:
      'This module contrasts the exact and asymptotic continuous branches. Exact projection removes the divergence-producing component in one shot for the periodic model, while GLM reduces it gradually instead of annihilating it exactly.',
    technical:
      'Builds a periodic discrete field of the form B = B_phys + grad(phi), then compares a numerical Helmholtz-style projection with a GLM-style damping update. The exact branch is projection-based; the GLM branch is asymptotic and should not be promoted as exact.',
    use: 'Use this when you want the clearest continuous-system difference between exact and asymptotic correction.',
    avoid: 'Do not read the GLM side as an exact projector or assume the periodic result automatically extends to boundary-sensitive domains.',
    refs: [
      { title: 'Divergence cleaning in OCP', href: '../mhd/divergence-cleaning-in-ocp.md', note: 'Exact Leray / Helmholtz anchor' },
      { title: 'GLM and asymptotic correction', href: '../mhd/glm-and-asymptotic-correction.md', note: 'Asymptotic branch and limitation notes' },
      { title: 'Exact vs asymptotic', href: '../formalism/exact-vs-asymptotic.md', note: 'Why the split matters' },
    ],
  },
  continuous: {
    label: 'Continuous Generator Lab',
    short: 'Invariant-split flows, spectral damping, and mixing failure.',
    status: 'PROVED / NO-GO',
    plain:
      'This module shows the strongest asymptotic theorem spine in the repo. Some generators preserve the protected coordinates and damp the disturbance coordinates. Others look stable overall but fail because they mix disturbance back into the protected part.',
    technical:
      'Computes the kernel-based protected space, an orthogonal disturbance complement, an RK4 flow path, the mixing norm ||P_S K P_D||, and the finite-time exact-recovery residual. This is where the repo now draws a hard line between asymptotic correction and exact one-shot recovery.',
    use: 'Use this to test whether a linear correction generator actually qualifies as an OCP correction flow.',
    avoid: 'Do not treat every dissipative matrix as an OCP flow. Protected-state preservation is a separate condition from decay.',
    refs: [
      { title: 'Generator theorems', href: '../theorem-candidates/generator-theorems.md', note: 'OCP-T3 and the PSD corollary' },
      { title: 'Advanced no-go results', href: '../impossibility-results/advanced-no-go-results.md', note: 'Finite-time exact recovery failure and stronger boundaries' },
      { title: 'Worked linear example', href: '../control/worked-linear-example.md', note: 'Clean invariant-split control picture' },
    ],
  },
  nogo: {
    label: 'No-Go Explorer',
    short: 'Failure modes the theory can actually rule out.',
    status: 'PROVED BOUNDARY LAYER',
    plain:
      'The negative-results layer is part of the theory, not an appendix. These examples show when exact recovery is impossible, when sector detection collapses, when correction image is too small, and when smooth flows cannot do exact one-shot recovery.',
    technical:
      'Each preset is wired to a specific theorem or theorem-grade obstruction in the repo. The point is to make failure structural and inspectable rather than rhetorical.',
    use: 'Use this to understand what the framework excludes and why those exclusions matter.',
    avoid: 'Do not hide these cases or treat them as edge trivia. The no-go layer is one of the strongest outputs of the repository.',
    refs: [
      { title: 'No-go results', href: '../impossibility-results/no-go-results.md', note: 'Core impossibility spine' },
      { title: 'Advanced no-go results', href: '../impossibility-results/advanced-no-go-results.md', note: 'Stronger flow and sector boundaries' },
      { title: 'Dead ends and do not promote', href: '../open-questions/dead-ends-and-do-not-promote.md', note: 'Explicit negative curation' },
    ],
  },
};

const CONTINUOUS_PRESETS = {
  invariant: {
    matrix: [
      [0, 0, 0],
      [0, 1, 1],
      [0, 0, 1.5],
    ],
    x0: [2, -1, 0.5],
  },
  psd: {
    matrix: [
      [0, 0, 0],
      [0, 0.75, 0],
      [0, 0, 2],
    ],
    x0: [3, -4, 1],
  },
  mixing: {
    matrix: [
      [0, 1],
      [0, 1],
    ],
    x0: [0, 1],
  },
};

let state = initialState();
let latestAnalysis = analyzeActiveLab();
let savedScenarios = loadSavedScenarios();

function initialState() {
  const fromHash = decodeShareState(window.location.hash);
  return fromHash ?? cloneState(DEFAULT_STATE);
}

function loadSavedScenarios() {
  try {
    return JSON.parse(window.localStorage.getItem(STORAGE_KEY) ?? '{}');
  } catch {
    return {};
  }
}

function saveScenariosStore() {
  window.localStorage.setItem(STORAGE_KEY, JSON.stringify(savedScenarios));
}

function analyzeActiveLab() {
  switch (state.activeLab) {
    case 'exact':
      return analyzeExactProjection(state.labs.exact);
    case 'qec':
      return analyzeQecSector(state.labs.qec);
    case 'mhd':
      return analyzeMhdProjection(state.labs.mhd);
    case 'continuous':
      return analyzeContinuousGenerator(state.labs.continuous);
    case 'nogo':
    default:
      return analyzeNoGo(state.labs.nogo);
  }
}

function syncHash() {
  const encoded = encodeShareState(state);
  window.history.replaceState(null, '', `#state=${encoded}`);
}

function applyContinuousPreset(name) {
  const preset = CONTINUOUS_PRESETS[name];
  if (!preset) return;
  state.labs.continuous.preset = name;
  state.labs.continuous.matrix = preset.matrix.map((row) => row.slice());
  state.labs.continuous.x0 = preset.x0.slice();
}

function render() {
  latestAnalysis = analyzeActiveLab();
  syncHash();
  const app = document.getElementById('app');
  const meta = LAB_META[state.activeLab];
  app.innerHTML = `
    <div class="site-shell">
      <header class="masthead">
        <div class="masthead-inner">
          <div>
            <span class="kicker">Protected-State Correction</span>
            <h1>OCP Workbench</h1>
            <p class="deck">A static scientific workbench for exact projection, exact sector recovery, continuous asymptotic correction, and theorem-grade failure modes. Every module is tied to a proved result, a conditional branch, or a no-go statement in the repository.</p>
          </div>
          <div class="toolbar">
            <button id="mode-toggle">${state.mode === 'plain' ? 'Switch to Technical Mode' : 'Switch to Plain-Language Mode'}</button>
            <select id="saved-scenarios">
              <option value="">Saved scenarios</option>
              ${Object.keys(savedScenarios).sort().map((key) => `<option value="${key}">${key}</option>`).join('')}
            </select>
            <button id="load-scenario">Load</button>
            <button id="save-scenario">Save</button>
            <button id="share-link">Copy Share Link</button>
            <button id="export-json">Export JSON</button>
            <button id="export-figure" class="primary">Export Figure</button>
          </div>
        </div>
      </header>
      <main class="workspace">
        <aside class="rail">
          <div class="context-block">
            <h3>Modules</h3>
            <p>${state.mode === 'plain' ? 'Each lab isolates one operator pattern or one failure pattern, so the theory stays inspectable instead of drifting into analogy.' : 'The workbench mirrors the repo architecture: exact branch, sector branch, continuous/asymptotic branch, and explicit no-go layer.'}</p>
          </div>
          <nav class="lab-nav">
            ${Object.entries(LAB_META).map(([key, entry]) => `
              <button class="${key === state.activeLab ? 'active' : ''}" data-lab="${key}">
                <strong>${entry.label}</strong>
                <span>${entry.short}</span>
              </button>
            `).join('')}
          </nav>
          <div class="callout ${meta.status.includes('NO-GO') ? 'warn' : 'good'}">
            <div class="status-pill">${meta.status}</div>
            <p>${state.mode === 'plain' ? meta.use : meta.avoid}</p>
          </div>
        </aside>
        <section class="canvas-panel">
          <div class="panel-head">
            <div class="status-pill">${meta.status}</div>
            <h2>${meta.label}</h2>
            <p>${state.mode === 'plain' ? meta.plain : meta.technical}</p>
          </div>
          <div class="lab-layout">
            <div class="config-pane">${renderConfigPane()}</div>
            <div class="visual-pane">
              <div class="visual-stage">${renderVisualStage()}</div>
              <div class="metric-strip">${renderMetrics()}</div>
            </div>
          </div>
        </section>
        <aside class="context-panel">
          <div class="context-block">
            <h3>Interpretation</h3>
            <p>${state.mode === 'plain' ? meta.plain : meta.technical}</p>
          </div>
          <div class="context-block">
            <h4>When To Use This</h4>
            <p>${meta.use}</p>
          </div>
          <div class="context-block">
            <h4>When Not To Use This</h4>
            <p>${meta.avoid}</p>
          </div>
          <div class="context-block">
            <h4>Theory And Proof Map</h4>
            <div class="ref-list">
              ${meta.refs.map((ref) => `<a href="${ref.href}"><strong>${ref.title}</strong><small>${ref.note}</small></a>`).join('')}
            </div>
          </div>
          <div class="context-block">
            <h4>Current Output</h4>
            ${renderNarrativeSummary()}
          </div>
        </aside>
      </main>
    </div>
  `;

  attachEvents();
  hydrateCanvases();
}

function renderConfigPane() {
  switch (state.activeLab) {
    case 'exact':
      return `
        ${rangeField('protectedMagnitude', 'Protected magnitude', state.labs.exact.protectedMagnitude, 0.2, 2.5, 0.05)}
        ${rangeField('disturbanceMagnitude', 'Disturbance magnitude', state.labs.exact.disturbanceMagnitude, 0, 2.5, 0.05)}
        ${rangeField('angleDeg', 'Disturbance angle (degrees)', state.labs.exact.angleDeg, 15, 90, 1)}
        <div class="callout ${latestAnalysis.admissible ? 'good' : 'warn'}">
          <strong>${latestAnalysis.admissible ? 'Exact theorem applies.' : 'This is a deliberate no-go case.'}</strong>
          <p>${latestAnalysis.admissible ? 'Protected and disturbance directions are orthogonal, so exact projector recovery is justified.' : 'The disturbance now leaks into the protected direction, so the projector no longer returns the original protected component exactly.'}</p>
        </div>
      `;
    case 'qec':
      return `
        ${rangeField('alpha', 'Logical coefficient α', state.labs.qec.alpha, -2, 2, 0.1)}
        ${rangeField('beta', 'Logical coefficient β', state.labs.qec.beta, -2, 2, 0.1)}
        <div class="field">
          <label for="qec-errorIndex">Selected error sector</label>
          <select id="qec-errorIndex" data-path="labs.qec.errorIndex">
            <option value="0" ${state.labs.qec.errorIndex === 0 ? 'selected' : ''}>I</option>
            <option value="1" ${state.labs.qec.errorIndex === 1 ? 'selected' : ''}>X₁</option>
            <option value="2" ${state.labs.qec.errorIndex === 2 ? 'selected' : ''}>X₂</option>
            <option value="3" ${state.labs.qec.errorIndex === 3 ? 'selected' : ''}>X₃</option>
          </select>
        </div>
        <div class="callout good">
          <strong>Exact sector recovery in action.</strong>
          <p>The disturbed logical state lives in one orthogonal sector and the selected recovery maps it back to the code space without changing the logical coefficients.</p>
        </div>
      `;
    case 'mhd':
      return `
        ${rangeField('contamination', 'Gradient contamination strength', state.labs.mhd.contamination, 0.02, 0.6, 0.01)}
        ${rangeField('glmSteps', 'GLM steps', state.labs.mhd.glmSteps, 1, 20, 1)}
        ${rangeField('poissonIterations', 'Projection iterations', state.labs.mhd.poissonIterations, 80, 500, 20)}
        ${rangeField('dt', 'GLM timestep', state.labs.mhd.dt, 0.01, 0.1, 0.01)}
        <div class="callout ${latestAnalysis.afterExactNorm < latestAnalysis.afterGlmNorm ? 'good' : 'warn'}">
          <strong>Exact versus asymptotic branch check.</strong>
          <p>Exact projection should drive the divergence much closer to zero than a short GLM run. If that stops being true, the example is no longer representing the repo’s strongest exact/asymptotic split clearly enough.</p>
        </div>
      `;
    case 'continuous':
      return `
        <div class="field">
          <label for="continuous-preset">Preset generator</label>
          <select id="continuous-preset">
            <option value="invariant" ${state.labs.continuous.preset === 'invariant' ? 'selected' : ''}>Invariant split</option>
            <option value="psd" ${state.labs.continuous.preset === 'psd' ? 'selected' : ''}>Self-adjoint PSD</option>
            <option value="mixing" ${state.labs.continuous.preset === 'mixing' ? 'selected' : ''}>Mixing failure</option>
          </select>
        </div>
        <div class="field">
          <label for="continuous-matrix">Generator K</label>
          <textarea id="continuous-matrix">${state.labs.continuous.matrix.map((row) => row.join(', ')).join('\n')}</textarea>
        </div>
        <div class="field">
          <label for="continuous-x0">Initial state x₀</label>
          <input id="continuous-x0" value="${state.labs.continuous.x0.join(', ')}" />
        </div>
        ${rangeField('time', 'Simulation time', state.labs.continuous.time, 0.25, 4, 0.05)}
        ${rangeField('steps', 'RK4 steps', state.labs.continuous.steps, 80, 500, 20)}
        <div class="callout ${latestAnalysis.mixingNorm < 1e-8 ? 'good' : 'warn'}">
          <strong>${latestAnalysis.mixingNorm < 1e-8 ? 'Protected coordinates are preserved.' : 'Mixing failure detected.'}</strong>
          <p>${latestAnalysis.mixingNorm < 1e-8 ? 'This generator respects the protected/disturbance split and belongs to the asymptotic correction branch.' : 'This generator may damp disturbance overall, but it also injects disturbance into the protected coordinates, so it fails the OCP criterion.'}</p>
        </div>
      `;
    case 'nogo':
    default:
      return `
        <div class="field">
          <label for="nogo-example">Failure mode</label>
          <select id="nogo-example" data-path="labs.nogo.example">
            <option value="finite-time" ${state.labs.nogo.example === 'finite-time' ? 'selected' : ''}>Finite-time flow no-go</option>
            <option value="overlap" ${state.labs.nogo.example === 'overlap' ? 'selected' : ''}>Overlap / indistinguishability</option>
            <option value="sector-overlap" ${state.labs.nogo.example === 'sector-overlap' ? 'selected' : ''}>Sector overlap</option>
            <option value="mixing" ${state.labs.nogo.example === 'mixing' ? 'selected' : ''}>Mixing failure</option>
            <option value="rank" ${state.labs.nogo.example === 'rank' ? 'selected' : ''}>Insufficient correction image</option>
          </select>
        </div>
        <div class="callout warn">
          <strong>Negative results are part of the finished theory.</strong>
          <p>This module exists to keep the repo honest. Each example corresponds to a claim the theory can actually reject, not just a vague warning.</p>
        </div>
      `;
  }
}

function rangeField(key, label, value, min, max, step) {
  return `
    <div class="field">
      <label for="${state.activeLab}-${key}">${label}</label>
      <div class="range-row">
        <input id="${state.activeLab}-${key}" type="range" min="${min}" max="${max}" step="${step}" value="${value}" data-path="labs.${state.activeLab}.${key}" />
        <output>${Number(value).toFixed(step >= 1 ? 0 : 2)}</output>
      </div>
    </div>
  `;
}

function renderVisualStage() {
  switch (state.activeLab) {
    case 'exact':
      return renderExactStage();
    case 'qec':
      return renderQecStage();
    case 'mhd':
      return renderMhdStage();
    case 'continuous':
      return renderContinuousStage();
    case 'nogo':
    default:
      return renderNoGoStage();
  }
}

function renderExactStage() {
  const a = latestAnalysis;
  return `
    <div class="visual-grid double">
      <div class="figure" data-exportable="true">
        <h4>2D decomposition</h4>
        ${vectorPlotSvg(a)}
        <small>Blue = protected component, amber = disturbance, dark = ambient state, red = recovered state.</small>
      </div>
      <div class="figure">
        <h4>Algebraic check</h4>
        <div class="value-grid">
          <div><small>Ambient state</small><code>${formatVector(a.x)}</code></div>
          <div><small>Recovered state</small><code>${formatVector(a.recovered)}</code></div>
          <div><small>Protected part</small><code>${formatVector(a.s)}</code></div>
          <div><small>Disturbance part</small><code>${formatVector(a.d)}</code></div>
        </div>
      </div>
    </div>
  `;
}

function renderQecStage() {
  const a = latestAnalysis;
  return `
    <div class="visual-grid double">
      <div class="figure" data-exportable="true">
        <h4>Amplitude comparison</h4>
        ${barChartSvg([
          { label: 'Logical', values: a.logical },
          { label: `Disturbed (${a.selectedLabel})`, values: a.disturbed },
          { label: 'Recovered', values: a.recovered },
        ])}
        <small>The recovery should return the logical amplitudes exactly for the selected single-bit-flip sector.</small>
      </div>
      <div class="figure">
        <h4>Sector overlap matrix</h4>
        <div id="qec-overlap-table"></div>
        <small>Orthogonal sectors are what make exact sector-conditioned recovery possible here.</small>
      </div>
    </div>
  `;
}

function renderMhdStage() {
  return `
    <div class="visual-grid triple">
      <div class="figure"><h4>Before projection</h4><canvas id="heat-before" width="240" height="240" data-exportable="true"></canvas><small>Divergence field before correction.</small></div>
      <div class="figure"><h4>After exact projection</h4><canvas id="heat-exact" width="240" height="240"></canvas><small>Exact periodic projection branch.</small></div>
      <div class="figure"><h4>After GLM steps</h4><canvas id="heat-glm" width="240" height="240"></canvas><small>Asymptotic reduction after the selected number of GLM steps.</small></div>
    </div>
    <div class="visual-grid double" style="margin-top:1rem;">
      <div class="figure" data-exportable="true">
        <h4>GLM divergence history</h4>
        ${lineChartSvg(latestAnalysis.glmHistory.map((value, index) => ({ x: index, y: value })), 'Step', 'L2 divergence')}
        <small>GLM reduces the constraint violation, but the exact projector removes it much more sharply.</small>
      </div>
      <div class="figure">
        <h4>Norm comparison</h4>
        <div class="value-grid">
          <div><small>Before</small><code>${latestAnalysis.beforeNorm.toExponential(3)}</code></div>
          <div><small>After exact projection</small><code>${latestAnalysis.afterExactNorm.toExponential(3)}</code></div>
          <div><small>After GLM</small><code>${latestAnalysis.afterGlmNorm.toExponential(3)}</code></div>
          <div><small>Exact improvement factor</small><code>${formatFactor(latestAnalysis.exactImprovementFactor)}</code></div>
        </div>
      </div>
    </div>
  `;
}

function renderContinuousStage() {
  const a = latestAnalysis;
  return `
    <div class="visual-grid double">
      <div class="figure" data-exportable="true">
        <h4>Disturbance norm over time</h4>
        ${lineChartSvg(a.disturbanceNorms.map((value, index) => ({ x: index, y: value })), 'Step', '||P_D x||')}
        <small>Decay alone is not enough. The protected component must also stay fixed.</small>
      </div>
      <div class="figure">
        <h4>Kernel / split diagnostics</h4>
        <div class="value-grid">
          <div><small>ker(K) basis</small><code>${a.kernelBasis.length ? a.kernelBasis.map((row) => formatVector(row)).join('\n') : '[]'}</code></div>
          <div><small>Disturbance complement</small><code>${a.disturbanceBasis.length ? a.disturbanceBasis.map((row) => formatVector(row)).join('\n') : '[]'}</code></div>
          <div><small>Final state</small><code>${formatVector(a.xt)}</code></div>
          <div><small>Mixing norm</small><code>${a.mixingNorm.toExponential(3)}</code></div>
        </div>
      </div>
    </div>
  `;
}

function renderNoGoStage() {
  const a = latestAnalysis;
  return `
    <div class="figure" data-exportable="true">
      <h4>${a.title}</h4>
      <p>${a.summary}</p>
      <div class="value-grid">
        ${Object.entries(a.details).map(([key, value]) => `<div><small>${key}</small><code>${typeof value === 'object' ? JSON.stringify(value, null, 2) : String(value)}</code></div>`).join('')}
      </div>
    </div>
  `;
}

function renderMetrics() {
  switch (state.activeLab) {
    case 'exact':
      return [
        metric('Basis overlap', latestAnalysis.overlap.toFixed(3), latestAnalysis.admissible ? 'good' : 'bad'),
        metric('Recovery error', latestAnalysis.exactError.toExponential(2), latestAnalysis.exactError < 1e-8 ? 'good' : 'bad'),
        metric('Mode', latestAnalysis.admissible ? 'Exact branch' : 'No-go case'),
      ].join('');
    case 'qec':
      return [
        metric('Selected sector', latestAnalysis.selectedLabel),
        metric('Recovery error', latestAnalysis.recoveryError.toExponential(2), latestAnalysis.recoveryError < 1e-9 ? 'good' : 'bad'),
        metric('Max off-sector overlap', Math.max(...latestAnalysis.sectorOverlap.flat().filter((value) => value < 1)).toExponential(2), 'good'),
      ].join('');
    case 'mhd':
      return [
        metric('Before', latestAnalysis.beforeNorm.toExponential(2)),
        metric('After exact', latestAnalysis.afterExactNorm.toExponential(2), 'good'),
        metric('After GLM', latestAnalysis.afterGlmNorm.toExponential(2), latestAnalysis.afterGlmNorm < latestAnalysis.beforeNorm ? 'good' : 'bad'),
        metric('Exact vs GLM', latestAnalysis.afterExactNorm < latestAnalysis.afterGlmNorm ? 'Exact stronger' : 'Check example', latestAnalysis.afterExactNorm < latestAnalysis.afterGlmNorm ? 'good' : 'bad'),
      ].join('');
    case 'continuous':
      return [
        metric('Protected drift', latestAnalysis.protectedDrift.toExponential(2), latestAnalysis.protectedDrift < 1e-4 ? 'good' : 'bad'),
        metric('Mixing norm', latestAnalysis.mixingNorm.toExponential(2), latestAnalysis.mixingNorm < 1e-6 ? 'good' : 'bad'),
        metric('Finite-time exact recovery', latestAnalysis.finiteTimeExactRecoveryPossible ? 'Apparent yes' : 'No', latestAnalysis.finiteTimeExactRecoveryPossible ? 'bad' : 'good'),
      ].join('');
    case 'nogo':
    default:
      return [
        metric('Status', latestAnalysis.status, 'bad'),
        metric('Scope', 'Structural boundary'),
      ].join('');
  }
}

function renderNarrativeSummary() {
  switch (state.activeLab) {
    case 'exact':
      return `<p>${latestAnalysis.admissible ? 'The protected and disturbance directions are orthogonal, so projection returns the protected component exactly.' : 'The disturbance direction overlaps the protected direction, so the same projection now carries contamination into the recovered state.'}</p>`;
    case 'qec':
      return `<p>The selected sector ${latestAnalysis.selectedLabel} is recovered with error ${latestAnalysis.recoveryError.toExponential(2)}. In this branch, exactness comes from sector distinguishability rather than one global projector on physical Hilbert space.</p>`;
    case 'mhd':
      return `<p>Projection drops the divergence norm from ${latestAnalysis.beforeNorm.toExponential(2)} to ${latestAnalysis.afterExactNorm.toExponential(2)}, while GLM reaches ${latestAnalysis.afterGlmNorm.toExponential(2)} after ${state.labs.mhd.glmSteps} steps. This is the exact versus asymptotic split in numerical form.</p>`;
    case 'continuous':
      return `<p>The generator produces protected drift ${latestAnalysis.protectedDrift.toExponential(2)} and mixing norm ${latestAnalysis.mixingNorm.toExponential(2)}. Finite-time exact recovery remains ${latestAnalysis.finiteTimeExactRecoveryPossible ? 'apparently possible' : 'ruled out'} for this smooth flow model.</p>`;
    case 'nogo':
    default:
      return `<p>${latestAnalysis.summary}</p>`;
  }
}

function formatFactor(value) {
  return value >= 1e4 ? `${value.toExponential(2)}×` : `${value.toFixed(1)}×`;
}

function metric(label, value, tone = '') {
  return `<div class="metric ${tone}"><strong>${value}</strong><span>${label}</span></div>`;
}

function attachEvents() {
  document.querySelectorAll('[data-lab]').forEach((button) => {
    button.addEventListener('click', () => {
      state.activeLab = button.dataset.lab;
      render();
    });
  });

  document.getElementById('mode-toggle').addEventListener('click', () => {
    state.mode = state.mode === 'plain' ? 'technical' : 'plain';
    render();
  });

  document.querySelectorAll('[data-path]').forEach((input) => {
    const eventName = input.tagName === 'SELECT' ? 'change' : 'input';
    input.addEventListener(eventName, () => updateStatePath(input.dataset.path, input.value));
  });

  const matrixInput = document.getElementById('continuous-matrix');
  if (matrixInput) {
    matrixInput.addEventListener('change', () => {
      state.labs.continuous.matrix = parseMatrix(matrixInput.value);
      render();
    });
  }

  const x0Input = document.getElementById('continuous-x0');
  if (x0Input) {
    x0Input.addEventListener('change', () => {
      state.labs.continuous.x0 = parseVector(x0Input.value);
      render();
    });
  }

  const preset = document.getElementById('continuous-preset');
  if (preset) {
    preset.addEventListener('change', () => {
      applyContinuousPreset(preset.value);
      render();
    });
  }

  document.getElementById('save-scenario').addEventListener('click', saveScenario);
  document.getElementById('load-scenario').addEventListener('click', loadScenarioFromSelect);
  document.getElementById('share-link').addEventListener('click', copyShareLink);
  document.getElementById('export-json').addEventListener('click', exportJson);
  document.getElementById('export-figure').addEventListener('click', exportFigure);
}

function updateStatePath(path, rawValue) {
  const parts = path.split('.');
  let target = state;
  for (let i = 0; i < parts.length - 1; i += 1) target = target[parts[i]];
  const key = parts[parts.length - 1];
  target[key] = Number.isNaN(Number(rawValue)) || rawValue === '' ? rawValue : Number(rawValue);
  state = sanitizeState(state);
  render();
}

function saveScenario() {
  const name = window.prompt('Save current scenario as:', `${LAB_META[state.activeLab].label} ${new Date().toLocaleString()}`);
  if (!name) return;
  savedScenarios[name] = cloneState(state);
  saveScenariosStore();
  render();
}

function loadScenarioFromSelect() {
  const select = document.getElementById('saved-scenarios');
  if (!select.value || !savedScenarios[select.value]) return;
  state = sanitizeState(savedScenarios[select.value]);
  render();
}

async function copyShareLink() {
  const url = `${window.location.origin}${window.location.pathname}#state=${encodeShareState(state)}`;
  try {
    await navigator.clipboard.writeText(url);
  } catch {
    window.prompt('Copy this share link:', url);
  }
}

function exportJson() {
  const payload = exportScenarioPayload(state, latestAnalysis);
  downloadText(`ocp-${state.activeLab}-scenario.json`, JSON.stringify(payload, null, 2), 'application/json');
}

function exportFigure() {
  const exportable = document.querySelector('[data-exportable="true"] canvas, [data-exportable="true"] svg') || document.querySelector('canvas, svg');
  if (!exportable) return;
  if (exportable.tagName.toLowerCase() === 'canvas') {
    const link = document.createElement('a');
    link.download = `ocp-${state.activeLab}-figure.png`;
    link.href = exportable.toDataURL('image/png');
    link.click();
    return;
  }
  const serializer = new XMLSerializer();
  const source = serializer.serializeToString(exportable);
  const blob = new Blob([source], { type: 'image/svg+xml;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.download = `ocp-${state.activeLab}-figure.svg`;
  link.href = url;
  link.click();
  URL.revokeObjectURL(url);
}

function downloadText(filename, text, mime) {
  const blob = new Blob([text], { type: mime });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.download = filename;
  link.href = url;
  link.click();
  URL.revokeObjectURL(url);
}

function parseMatrix(text) {
  return text
    .trim()
    .split(/\n+/)
    .map((row) => row.split(',').map((value) => Number(value.trim())));
}

function parseVector(text) {
  return text.split(',').map((value) => Number(value.trim()));
}

function hydrateCanvases() {
  if (state.activeLab === 'mhd') {
    drawHeatmap('heat-before', latestAnalysis.beforeDiv);
    drawHeatmap('heat-exact', latestAnalysis.afterExactDiv);
    drawHeatmap('heat-glm', latestAnalysis.afterGlmDiv);
  }
  if (state.activeLab === 'qec') {
    const mount = document.getElementById('qec-overlap-table');
    if (mount) mount.innerHTML = matrixTable(latestAnalysis.sectorOverlap, latestAnalysis.sectorLabels);
  }
}

function vectorPlotSvg(analysis) {
  const size = 360;
  const half = size / 2;
  const scale = 90;
  const toPoint = (vector) => [half + vector[0] * scale, half - vector[1] * scale];
  const makeArrow = (vector, color, width) => {
    const [x2, y2] = toPoint(vector);
    return `<line x1="${half}" y1="${half}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="${width}" stroke-linecap="round" marker-end="url(#arrow-${color.replace('#', '')})" />`;
  };
  return `
    <svg viewBox="0 0 ${size} ${size}" aria-label="Exact projection plot">
      <defs>
        ${['#1f4b99', '#9c5b2a', '#1c1d21', '#a63229'].map((color) => `
          <marker id="arrow-${color.replace('#', '')}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="${color}" />
          </marker>
        `).join('')}
      </defs>
      <rect width="${size}" height="${size}" rx="18" fill="rgba(255,255,255,0.65)" />
      <line x1="0" y1="${half}" x2="${size}" y2="${half}" stroke="rgba(28,29,33,0.15)" />
      <line x1="${half}" y1="0" x2="${half}" y2="${size}" stroke="rgba(28,29,33,0.15)" />
      ${makeArrow(analysis.s, '#1f4b99', 4)}
      ${makeArrow(analysis.d, '#9c5b2a', 4)}
      ${makeArrow(analysis.x, '#1c1d21', 4)}
      ${makeArrow(analysis.recovered, '#a63229', 3)}
      <text x="16" y="28" fill="#5d625e" font-size="13">Overlap = ${analysis.overlap.toFixed(3)}</text>
      <text x="16" y="46" fill="#5d625e" font-size="13">Recovery error = ${analysis.exactError.toExponential(2)}</text>
    </svg>
  `;
}

function barChartSvg(series) {
  const width = 540;
  const height = 260;
  const innerH = 180;
  const maxAbs = Math.max(...series.flatMap((entry) => entry.values.map((value) => Math.abs(value)))) || 1;
  const barWidth = 14;
  const gap = 8;
  const groupGap = 24;
  const colors = ['#1f4b99', '#9c5b2a', '#356c4a'];
  let x = 36;
  const bars = [];
  const labels = [];
  series.forEach((entry, groupIndex) => {
    entry.values.forEach((value, index) => {
      const scaled = (Math.abs(value) / maxAbs) * innerH;
      const y = value >= 0 ? 200 - scaled : 200;
      bars.push(`<rect x="${x}" y="${y}" width="${barWidth}" height="${scaled}" fill="${colors[groupIndex % colors.length]}" rx="4" />`);
      labels.push(`<text x="${x + barWidth / 2}" y="222" text-anchor="middle" font-size="11" fill="#5d625e">${index}</text>`);
      x += barWidth + gap;
    });
    labels.push(`<text x="${x - (entry.values.length * (barWidth + gap)) / 2 - 4}" y="244" text-anchor="middle" font-size="12" fill="#1c1d21">${entry.label}</text>`);
    x += groupGap;
  });
  return `
    <svg viewBox="0 0 ${width} ${height}" aria-label="QEC amplitude comparison">
      <rect width="${width}" height="${height}" rx="18" fill="rgba(255,255,255,0.65)" />
      <line x1="20" y1="200" x2="${width - 16}" y2="200" stroke="rgba(28,29,33,0.2)" />
      ${bars.join('')}
      ${labels.join('')}
    </svg>
  `;
}

function lineChartSvg(points, xLabel, yLabel) {
  const width = 540;
  const height = 260;
  const left = 48;
  const right = 18;
  const top = 18;
  const bottom = 42;
  const xs = points.map((point) => point.x);
  const ys = points.map((point) => point.y);
  const xMin = Math.min(...xs);
  const xMax = Math.max(...xs);
  const yMin = Math.min(...ys);
  const yMax = Math.max(...ys);
  const xScale = (value) => left + ((value - xMin) / Math.max(xMax - xMin, 1e-9)) * (width - left - right);
  const yScale = (value) => height - bottom - ((value - yMin) / Math.max(yMax - yMin, 1e-9)) * (height - top - bottom);
  const path = points.map((point, index) => `${index === 0 ? 'M' : 'L'} ${xScale(point.x)} ${yScale(point.y)}`).join(' ');
  return `
    <svg viewBox="0 0 ${width} ${height}" aria-label="Line chart">
      <rect width="${width}" height="${height}" rx="18" fill="rgba(255,255,255,0.65)" />
      <line x1="${left}" y1="${height - bottom}" x2="${width - right}" y2="${height - bottom}" stroke="rgba(28,29,33,0.18)" />
      <line x1="${left}" y1="${top}" x2="${left}" y2="${height - bottom}" stroke="rgba(28,29,33,0.18)" />
      <path d="${path}" fill="none" stroke="#9c5b2a" stroke-width="3" stroke-linecap="round" />
      <text x="${width / 2}" y="${height - 10}" text-anchor="middle" font-size="12" fill="#5d625e">${xLabel}</text>
      <text x="16" y="${height / 2}" transform="rotate(-90 16 ${height / 2})" text-anchor="middle" font-size="12" fill="#5d625e">${yLabel}</text>
    </svg>
  `;
}

function drawHeatmap(id, field) {
  const canvas = document.getElementById(id);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const rows = field.length;
  const cols = field[0].length;
  const flat = field.flat();
  const maxAbs = Math.max(...flat.map((value) => Math.abs(value))) || 1;
  const cellW = canvas.width / cols;
  const cellH = canvas.height / rows;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = 0; i < rows; i += 1) {
    for (let j = 0; j < cols; j += 1) {
      const value = clamp(field[i][j] / maxAbs, -1, 1);
      const red = value > 0 ? 190 + Math.round(55 * value) : 34 + Math.round(90 * (1 + value));
      const blue = value < 0 ? 190 + Math.round(55 * -value) : 45 + Math.round(70 * (1 - value));
      const green = 120 + Math.round(40 * (1 - Math.abs(value)));
      ctx.fillStyle = `rgb(${red}, ${green}, ${blue})`;
      ctx.fillRect(j * cellW, i * cellH, cellW + 0.5, cellH + 0.5);
    }
  }
}

function matrixTable(matrix, labels) {
  return `
    <table style="width:100%; border-collapse:collapse; font-size:0.92rem;">
      <thead>
        <tr><th></th>${labels.map((label) => `<th style="padding:0.35rem; text-align:right; color:#5d625e;">${label}</th>`).join('')}</tr>
      </thead>
      <tbody>
        ${matrix.map((row, i) => `<tr><th style="padding:0.35rem; text-align:left; color:#5d625e;">${labels[i]}</th>${row.map((value) => `<td style="padding:0.35rem; text-align:right;">${value.toFixed(3)}</td>`).join('')}</tr>`).join('')}
      </tbody>
    </table>
  `;
}

render();
window.addEventListener('hashchange', () => {
  const decoded = decodeShareState(window.location.hash);
  if (decoded) {
    state = decoded;
    render();
  }
});
