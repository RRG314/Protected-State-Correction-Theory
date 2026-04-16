import {
  analyzeBenchmarkConsole,
  analyzeCfdProjection,
  analyzeBoundaryProjectionLimit,
  analyzeContinuousGenerator,
  analyzeExactProjection,
  analyzeGaugeProjection,
  analyzeMhdProjection,
  analyzeNoGo,
  analyzeQecSector,
  analyzeRecoverability,
  LINEAR_TEMPLATE_LIBRARY,
  clamp,
  formatVector,
} from './lib/compute.js';
import {
  DISCOVERY_MIXER_DEMOS,
  DISCOVERY_MIXER_LIBRARY,
  analyzeDiscoveryMixer,
} from './lib/discoveryMixer.js';
import {
  DEFAULT_STATE,
  cloneState,
  exportScenarioCsv,
  exportScenarioPayload,
  exportScenarioReport,
} from './lib/state.js';
import {
  LAB_META,
  CONTINUOUS_PRESETS,
  STRUCTURAL_DISCOVERY_PRESETS,
  QUICKSTARTS,
} from './lib/domain/workbenchCatalog.js';
import { createWorkbenchStore } from './lib/app/scenarioStore.js';
import {
  barChartSvg,
  drawHeatmap,
  lineChartSvg,
  matrixTable,
  vectorPlotSvg,
} from './lib/ui/charts.js';

const LAB_DEFAULTS = cloneState(DEFAULT_STATE.labs);

const store = createWorkbenchStore(window);
let { state, latestAnalysis, savedScenarios } = store.snapshot();
let playbackTimer = null;
let playbackLab = null;

function syncViewState() {
  ({ state, latestAnalysis, savedScenarios } = store.snapshot());
}

function applyContinuousPreset(name) {
  const preset = CONTINUOUS_PRESETS[name];
  if (!preset) return;
  store.patchLab('continuous', {
    preset: name,
    matrix: preset.matrix.map((row) => row.slice()),
    x0: preset.x0.slice(),
    frame: state.labs.continuous.steps,
  });
  syncViewState();
}

function applyStructuralPreset(name) {
  const preset = STRUCTURAL_DISCOVERY_PRESETS[name];
  if (!preset) return;
  store.setState({
    ...state,
    activeLab: 'recoverability',
    labs: {
      ...state.labs,
      recoverability: {
        ...cloneState(DEFAULT_STATE.labs.recoverability),
        ...cloneState(preset.patch),
      },
    },
  });
  syncViewState();
  render();
}

function applyQuickStart(id) {
  const quickStart = QUICKSTARTS.find((item) => item.id === id);
  if (!quickStart) return;
  if (quickStart.action.type === 'preset') {
    applyStructuralPreset(quickStart.action.preset);
    return;
  }
  if (quickStart.action.type === 'lab') {
    store.setActiveLab(quickStart.action.lab);
    syncViewState();
    render();
  }
}

function applyStructuralRecommendation(index) {
  const recommendation = latestAnalysis?.recommendations?.[Number(index)];
  if (!recommendation || !recommendation.availableInStudio || !recommendation.patch) return;
  store.setState({
    ...state,
    activeLab: 'recoverability',
    labs: {
      ...state.labs,
      recoverability: {
        ...cloneState(state.labs.recoverability),
        ...cloneState(recommendation.patch),
        linearMeasurements: recommendation.patch.linearMeasurements
          ? { ...cloneState(state.labs.recoverability.linearMeasurements), ...cloneState(recommendation.patch.linearMeasurements) }
          : cloneState(state.labs.recoverability.linearMeasurements),
      },
    },
  });
  syncViewState();
  render();
}

function applyMixerDemo(key) {
  const demo = DISCOVERY_MIXER_DEMOS[key];
  if (!demo) return;
  store.setState({
    ...state,
    activeLab: 'mixer',
    labs: {
      ...state.labs,
      mixer: {
        ...cloneState(DEFAULT_STATE.labs.mixer),
        mode: demo.mode,
        family: demo.family,
        ...cloneState(demo.patch),
      },
    },
  });
  syncViewState();
  render();
}

function applyMixerRecommendation(index) {
  const recommendation = latestAnalysis?.recommendations?.[Number(index)];
  if (!recommendation || !recommendation.availableInStudio || !recommendation.patch) return;
  store.setState({
    ...state,
    activeLab: 'mixer',
    labs: {
      ...state.labs,
      mixer: {
        ...cloneState(state.labs.mixer),
        ...cloneState(recommendation.patch),
      },
    },
  });
  syncViewState();
  render();
}

function render() {
  normalizeInteractiveState();
  store.setState(state);
  syncViewState();
  if (playbackTimer && playbackLab !== state.activeLab) {
    stopPlayback();
  }
  const app = document.getElementById('app');
  const meta = LAB_META[state.activeLab];
  app.innerHTML = `
    <div class="site-shell">
      <header class="hero">
        <div class="hero-grid">
          <div class="hero-copy">
            <span class="kicker">Protected-State Correction Theory</span>
            <h1>Protected-State Correction Workbench</h1>
            <p class="deck">A theorem-linked structural-discovery, recoverability, and composition workbench for exact projection, asymptotic redesign, threshold diagnosis, minimal augmentation, bounded-domain architecture checks, and typed system assembly. The interface is organized as a real workspace: choose the branch, configure the family, inspect the evidence, and compare the fix before you trust it.</p>
            <div class="hero-meta-row">
              <span class="fit-pill">${meta.branch}</span>
              <span class="status-pill">${meta.status}</span>
              <span class="fit-pill subtle">Current lane: ${meta.lane}</span>
            </div>
          </div>
          <div class="hero-actions card-surface">
            <div class="action-group">
              <span class="action-label">Mode</span>
              <button id="mode-toggle" class="ghost-button">${state.mode === 'plain' ? 'Switch to Technical Mode' : 'Switch to Plain-Language Mode'}</button>
            </div>
            <div class="action-group">
              <span class="action-label">Scenarios</span>
              <div class="action-row">
                <select id="saved-scenarios">
                  <option value="">Saved scenarios</option>
                  ${Object.keys(savedScenarios).sort().map((key) => `<option value="${key}">${key}</option>`).join('')}
                </select>
                <button id="load-scenario">Load</button>
                <button id="save-scenario">Save</button>
              </div>
            </div>
            <div class="action-group">
              <span class="action-label">Export</span>
              <div class="action-row compact">
                <button id="share-link">Copy Share Link</button>
                <button id="export-json">Export JSON</button>
                <button id="export-csv">Export CSV</button>
                <button id="export-report">Export Report</button>
                <button id="export-figure" class="primary">Export Figure</button>
              </div>
            </div>
            <div class="action-group">
              <span class="action-label">Reset</span>
              <div class="action-row compact">
                <button id="reset-current">Reset Current Lab</button>
                <button id="reset-all">Reset All Labs</button>
              </div>
            </div>
          </div>
        </div>
      </header>

      <main class="workspace-shell">
        <aside class="navigator-rail card-surface">
          <div class="nav-section">
            <div class="pane-heading compact">
              <h3>Start Here</h3>
              <p>Pick the question you actually have first, then drop into the right branch surface.</p>
            </div>
            <div class="quickstart-stack">
              ${renderQuickStarts()}
            </div>
          </div>
          <div class="nav-section">
            <div class="pane-heading compact">
              <h3>Module Navigator</h3>
              <p>Every lab here is either theorem-backed, family-validated, or an explicit no-go / benchmark layer.</p>
            </div>
            <div class="module-stack">
              ${renderModuleCards()}
            </div>
          </div>
        </aside>

        <section class="workspace-column">
          <section class="summary-section">
            <div class="summary-grid">
              ${renderSummaryCards(meta)}
            </div>
          </section>

        <section class="lab-shell card-surface">
          <div class="lab-header">
            <div>
              <span class="fit-pill">${meta.fit}</span>
              <h2>${meta.label}</h2>
              <p>${state.mode === 'plain' ? meta.plain : meta.technical}</p>
            </div>
          </div>
          <div class="lab-body">
            <aside class="config-pane">
              <div class="pane-heading">
                <h3>Configuration</h3>
                <p>Adjust the example and inspect how the operator or no-go behaves.</p>
              </div>
              ${renderConfigPane()}
            </aside>
            <section class="results-pane">
              ${renderStageToolbar()}
              <div class="results-stage">
                ${renderVisualStage()}
              </div>
              <div class="metric-grid">
                ${renderMetrics()}
              </div>
            </section>
          </div>
        </section>
        </section>

        <aside class="context-rail">
          ${renderContextCards(meta)}
        </aside>
      </main>
    </div>
  `;

  attachEvents();
  hydrateCanvases();
}

function normalizeInteractiveState() {
  normalizePlaybackFrame('mhd');
  normalizePlaybackFrame('gauge');
  normalizePlaybackFrame('continuous');
}

function normalizePlaybackFrame(lab) {
  if (lab === 'mhd' || lab === 'gauge') {
    const current = state.labs[lab];
    current.frame = clamp(Number(current.frame ?? current.glmSteps), 0, Number(current.glmSteps));
    return;
  }
  if (lab === 'continuous') {
    const current = state.labs.continuous;
    current.frame = clamp(Number(current.frame ?? current.steps), 0, Number(current.steps));
  }
}

function getPlaybackConfig(lab = state.activeLab) {
  if (lab === 'mhd') {
    const cfg = state.labs.mhd;
    return {
      lab,
      path: 'labs.mhd.frame',
      min: 0,
      max: Number(cfg.glmSteps),
      value: Number(cfg.frame),
      intervalMs: 280,
      title: 'GLM time history',
      description: 'Scrub the asymptotic cleaner frame by frame. The exact projector remains fixed so you can compare one-shot removal against gradual reduction.',
      currentText: `Frame ${Number(cfg.frame)} of ${Number(cfg.glmSteps)}`,
    };
  }
  if (lab === 'gauge') {
    const cfg = state.labs.gauge;
    return {
      lab,
      path: 'labs.gauge.frame',
      min: 0,
      max: Number(cfg.glmSteps),
      value: Number(cfg.frame),
      intervalMs: 280,
      title: 'Damped cleanup history',
      description: 'Scrub the damping branch over time and compare it against the exact transverse projector.',
      currentText: `Frame ${Number(cfg.frame)} of ${Number(cfg.glmSteps)}`,
    };
  }
  if (lab === 'continuous') {
    const cfg = state.labs.continuous;
    return {
      lab,
      path: 'labs.continuous.frame',
      min: 0,
      max: Number(cfg.steps),
      value: Number(cfg.frame),
      intervalMs: 140,
      title: 'Generator flow history',
      description: 'Step through the continuous correction flow to inspect drift, damping, and mixing over time rather than only at the endpoint.',
      currentText: `Step ${Number(cfg.frame)} of ${Number(cfg.steps)}`,
    };
  }
  return null;
}

function isPlaybackActive() {
  return Boolean(playbackTimer && playbackLab === state.activeLab);
}

function stopPlayback() {
  if (playbackTimer) {
    window.clearInterval(playbackTimer);
    playbackTimer = null;
    playbackLab = null;
  }
}

function setStatePath(path, value) {
  store.setStatePath(path, value);
  syncViewState();
}

function stepPlayback(delta) {
  const playback = getPlaybackConfig();
  if (!playback) return;
  const next = clamp(playback.value + delta, playback.min, playback.max);
  setStatePath(playback.path, next);
  if (next >= playback.max && delta > 0) {
    stopPlayback();
  }
  render();
}

function togglePlayback() {
  const playback = getPlaybackConfig();
  if (!playback) return;
  if (isPlaybackActive()) {
    stopPlayback();
    render();
    return;
  }
  if (playback.value >= playback.max) {
    setStatePath(playback.path, 0);
  }
  playbackLab = state.activeLab;
  playbackTimer = window.setInterval(() => {
    const current = getPlaybackConfig(playbackLab);
    if (!current) {
      stopPlayback();
      return;
    }
    const next = current.value + 1;
    if (next > current.max) {
      stopPlayback();
      render();
      return;
    }
    setStatePath(current.path, next);
    render();
  }, playback.intervalMs);
  render();
}

function resetCurrentLab() {
  stopPlayback();
  store.resetCurrentLab();
  syncViewState();
  render();
}

function resetAllLabs() {
  stopPlayback();
  store.resetAllLabs();
  syncViewState();
  render();
}

function resetPlaybackView() {
  const playback = getPlaybackConfig();
  if (!playback) return;
  stopPlayback();
  setStatePath(playback.path, 0);
  render();
}

function renderModuleCards() {
  return Object.entries(LAB_META)
    .map(
      ([key, entry]) => `
        <button class="module-card ${key === state.activeLab ? 'active' : ''}" data-lab="${key}">
          <span class="module-kicker">${entry.branch}</span>
          <strong>${entry.label}</strong>
          <p>${entry.short}</p>
          <div class="module-meta">
            <span>${entry.fit}</span>
            <span>${entry.lane}</span>
          </div>
        </button>
      `
    )
    .join('');
}

function renderQuickStarts() {
  return QUICKSTARTS.map(
    (item) => `
      <button class="quickstart-card card-surface" data-quickstart="${item.id}">
        <span class="module-kicker">guided path</span>
        <strong>${item.title}</strong>
        <p>${item.body}</p>
      </button>
    `
  ).join('');
}

function renderSummaryCards(meta) {
  return [
    summaryCard('Protected object', meta.protected),
    summaryCard('Disturbance family', meta.disturbance),
    summaryCard('Correction architecture', meta.correction),
    summaryCard('Public reading', meta.fit),
  ].join('');
}

function renderStageToolbar() {
  const playback = getPlaybackConfig();
  if (!playback) {
    return `
      <div class="stage-toolbar card-surface passive">
        <div class="toolbar-copy">
          <span class="action-label">Interaction</span>
          <strong>Static theorem witness</strong>
          <p>This module updates immediately when its inputs change, but it does not have a time-history branch to scrub through.</p>
        </div>
        <div class="toolbar-actions">
          <button id="reset-current-view">Reset Current Lab</button>
        </div>
      </div>
    `;
  }
  return `
    <div class="stage-toolbar card-surface">
      <div class="toolbar-copy">
        <span class="action-label">Time and History</span>
        <strong>${playback.title}</strong>
        <p>${playback.description}</p>
      </div>
      <div class="timeline-block">
        <div class="timeline-topline">
          <span>${playback.currentText}</span>
          <span>${isPlaybackActive() ? 'Playing' : 'Paused'}</span>
        </div>
        <input
          class="timeline-slider"
          type="range"
          min="${playback.min}"
          max="${playback.max}"
          step="1"
          value="${playback.value}"
          data-path="${playback.path}"
        />
        <div class="timeline-actions">
          <button data-playback-step="-1">Step Back</button>
          <button id="playback-toggle" class="primary">${isPlaybackActive() ? 'Pause' : 'Play'}</button>
          <button data-playback-step="1">Step Forward</button>
          <button id="reset-playback-view">Reset View</button>
        </div>
      </div>
    </div>
  `;
}

function renderContextCards(meta) {
  return `
    <div class="context-card card-surface">
      <h3>Fit verdict</h3>
      <p>${meta.fit}</p>
      <ul>
        <li><strong>Branch:</strong> ${meta.branch}</li>
        <li><strong>Status:</strong> ${meta.status}</li>
        <li><strong>Lane:</strong> ${meta.lane}</li>
      </ul>
    </div>
    <div class="context-card card-surface">
      <h3>Interpretation</h3>
      <p>${state.mode === 'plain' ? meta.plain : meta.technical}</p>
    </div>
    <div class="context-card card-surface">
      <h3>When to use this</h3>
      <p>${meta.use}</p>
      <h4>When not to use it</h4>
      <p>${meta.avoid}</p>
    </div>
    <div class="context-card card-surface">
      <h3>Theory links</h3>
      <div class="ref-list">
        ${meta.refs.map((ref) => `<a href="${ref.href}"><strong>${ref.title}</strong><small>${ref.note}</small></a>`).join('')}
      </div>
    </div>
    <div class="context-card card-surface">
      <h3>Outside research</h3>
      <div class="ref-list">
        ${meta.literature.map((ref) => `<a href="${ref.href}" target="_blank" rel="noreferrer"><strong>${ref.title}</strong><small>${ref.note}</small></a>`).join('')}
      </div>
    </div>
    <div class="context-card card-surface">
      <h3>Current output</h3>
      ${renderNarrativeSummary()}
    </div>
  `;
}

function summaryCard(label, value) {
  return `<article class="summary-card card-surface"><span>${label}</span><strong>${value}</strong></article>`;
}

function checkboxField(id, label, path, checked, note = '') {
  return `
    <label class="toggle-card" for="${id}">
      <input id="${id}" type="checkbox" data-path="${path}" ${checked ? 'checked' : ''} />
      <span>
        <strong>${label}</strong>
        ${note ? `<small>${note}</small>` : ''}
      </span>
    </label>
  `;
}

function renderRecoverabilityLinearControls() {
  const template = LINEAR_TEMPLATE_LIBRARY[state.labs.recoverability.linearTemplate] ?? LINEAR_TEMPLATE_LIBRARY.sensor_basis;
  const activeCount = Object.values(state.labs.recoverability.linearMeasurements ?? {}).filter(Boolean).length;
  return `
    <div class="field">
      <label for="recoverability-linear-template">Reusable template</label>
      <select id="recoverability-linear-template" data-path="labs.recoverability.linearTemplate">
        ${Object.entries(LINEAR_TEMPLATE_LIBRARY)
          .map(
            ([key, value]) =>
              `<option value="${key}" ${state.labs.recoverability.linearTemplate === key ? 'selected' : ''}>${value.label}</option>`
          )
          .join('')}
      </select>
    </div>
    <div class="field">
      <label for="recoverability-linear-protected">Protected variable</label>
      <select id="recoverability-linear-protected" data-path="labs.recoverability.linearProtected">
        ${Object.entries(template.protectedOptions)
          .map(
            ([key, value]) =>
              `<option value="${key}" ${state.labs.recoverability.linearProtected === key ? 'selected' : ''}>${value.label}</option>`
          )
          .join('')}
      </select>
    </div>
    ${rangeField('linearDelta', 'Selected δ', state.labs.recoverability.linearDelta, 0, 2.5, 0.05)}
    <div class="field">
      <label>Candidate measurements</label>
      <div class="toggle-stack">
        ${template.candidates
          .map((candidate) =>
            checkboxField(
              `recoverability-${candidate.id}`,
              candidate.label,
              `labs.recoverability.linearMeasurements.${candidate.id}`,
              Boolean(state.labs.recoverability.linearMeasurements?.[candidate.id]),
              'Toggle this row into the static record library.'
            )
          )
          .join('')}
      </div>
      <small class="field-note">${activeCount} active measurement${activeCount === 1 ? '' : 's'}. Exact recovery requires the protected row space to lie inside the active record row space.</small>
    </div>
  `;
}

function renderMixerLinearMeasurementToggles() {
  const template = LINEAR_TEMPLATE_LIBRARY.sensor_basis;
  return `
    <div class="field">
      <label>Active observation rows</label>
      <div class="toggle-stack">
        ${template.candidates
          .map((candidate) =>
            checkboxField(
              `mixer-${candidate.id}`,
              candidate.label,
              `labs.mixer.structuredLinearMeasurements.${candidate.id}`,
              Boolean(state.labs.mixer.structuredLinearMeasurements?.[candidate.id]),
              'Toggle this record row into the current structured composition.'
            )
          )
          .join('')}
      </div>
    </div>
  `;
}

function renderMixerConfigPane() {
  const mixer = state.labs.mixer;
  return `
    <div class="field">
      <label>Discovery Mixer demos</label>
      <div class="action-row wrap-row">
        ${Object.entries(DISCOVERY_MIXER_DEMOS)
          .map(([key, demo]) => `<button type="button" class="ghost-button" data-mixer-demo="${key}">${demo.label}</button>`)
          .join('')}
      </div>
      <small class="field-note">Each demo starts from a supported composition and either finds a structural failure or validates a real repair path.</small>
    </div>
    <div class="field">
      <label for="mixer-mode">Mixer mode</label>
      <select id="mixer-mode" data-path="labs.mixer.mode">
        <option value="structured" ${mixer.mode === 'structured' ? 'selected' : ''}>structured mixer</option>
        <option value="custom" ${mixer.mode === 'custom' ? 'selected' : ''}>controlled custom input</option>
        <option value="random" ${mixer.mode === 'random' ? 'selected' : ''}>random exploration</option>
        <option value="demo" ${mixer.mode === 'demo' ? 'selected' : ''}>demo mode</option>
      </select>
    </div>
    ${mixer.mode === 'demo' ? `
      <div class="field">
        <label for="mixer-demo-key">Demo scenario</label>
        <select id="mixer-demo-key" data-path="labs.mixer.demoKey">
          ${Object.entries(DISCOVERY_MIXER_DEMOS).map(([key, demo]) => `<option value="${key}" ${mixer.demoKey === key ? 'selected' : ''}>${demo.label}</option>`).join('')}
        </select>
      </div>
    ` : ''}
    ${mixer.mode === 'structured' ? `
      <div class="field">
        <label for="mixer-family">Structured family</label>
        <select id="mixer-family" data-path="labs.mixer.family">
          ${Object.entries(DISCOVERY_MIXER_LIBRARY.structuredFamilies).map(([key, meta]) => `<option value="${key}" ${mixer.family === key ? 'selected' : ''}>${meta.label}</option>`).join('')}
        </select>
        <small class="field-note">${DISCOVERY_MIXER_LIBRARY.structuredFamilies[mixer.family]?.note ?? ''}</small>
      </div>
      ${mixer.family === 'linear' ? `
        <div class="field">
          <label for="mixer-structured-linear-protected">Protected target</label>
          <select id="mixer-structured-linear-protected" data-path="labs.mixer.structuredLinearProtected">
            ${Object.entries(LINEAR_TEMPLATE_LIBRARY.sensor_basis.protectedOptions).map(([key, option]) => `<option value="${key}" ${mixer.structuredLinearProtected === key ? 'selected' : ''}>${option.label}</option>`).join('')}
          </select>
        </div>
        ${renderMixerLinearMeasurementToggles()}
      ` : ''}
      ${mixer.family === 'periodic' ? `
        <div class="field">
          <label for="mixer-structured-periodic-protected">Protected target</label>
          <select id="mixer-structured-periodic-protected" data-path="labs.mixer.structuredPeriodicProtected">
            <option value="mode_1_coefficient" ${mixer.structuredPeriodicProtected === 'mode_1_coefficient' ? 'selected' : ''}>leading modal coefficient</option>
            <option value="modes_1_2_coefficients" ${mixer.structuredPeriodicProtected === 'modes_1_2_coefficients' ? 'selected' : ''}>first two modal coefficients</option>
            <option value="low_mode_sum" ${mixer.structuredPeriodicProtected === 'low_mode_sum' ? 'selected' : ''}>low-mode weighted sum</option>
            <option value="bandlimited_contrast" ${mixer.structuredPeriodicProtected === 'bandlimited_contrast' ? 'selected' : ''}>band-limited contrast functional</option>
            <option value="full_weighted_sum" ${mixer.structuredPeriodicProtected === 'full_weighted_sum' ? 'selected' : ''}>full weighted modal sum</option>
            <option value="full_modal_coefficients" ${mixer.structuredPeriodicProtected === 'full_modal_coefficients' ? 'selected' : ''}>full four-mode coefficient vector</option>
          </select>
        </div>
        <div class="field">
          <label for="mixer-structured-periodic-observation">Observation map</label>
          <select id="mixer-structured-periodic-observation" data-path="labs.mixer.structuredPeriodicObservation">
            <option value="full_vorticity" ${mixer.structuredPeriodicObservation === 'full_vorticity' ? 'selected' : ''}>full vorticity</option>
            <option value="cutoff_vorticity" ${mixer.structuredPeriodicObservation === 'cutoff_vorticity' ? 'selected' : ''}>spectral cutoff vorticity</option>
            <option value="divergence_only" ${mixer.structuredPeriodicObservation === 'divergence_only' ? 'selected' : ''}>divergence only</option>
          </select>
        </div>
        ${rangeField('structuredPeriodicCutoff', 'Retained cutoff', mixer.structuredPeriodicCutoff, 1, 4, 1, 'labs.mixer')}
      ` : ''}
      ${mixer.family === 'control' ? `
        <div class="field">
          <label for="mixer-structured-control-profile">Sensor profile</label>
          <select id="mixer-structured-control-profile" data-path="labs.mixer.structuredControlProfile">
            <option value="three_active" ${mixer.structuredControlProfile === 'three_active' ? 'selected' : ''}>three active sensors</option>
            <option value="two_active" ${mixer.structuredControlProfile === 'two_active' ? 'selected' : ''}>two active sensors</option>
            <option value="protected_hidden" ${mixer.structuredControlProfile === 'protected_hidden' ? 'selected' : ''}>protected direction hidden</option>
          </select>
        </div>
        <div class="field">
          <label for="mixer-structured-control-functional">Protected target</label>
          <select id="mixer-structured-control-functional" data-path="labs.mixer.structuredControlFunctional">
            <option value="sensor_sum" ${mixer.structuredControlFunctional === 'sensor_sum' ? 'selected' : ''}>sensor sum</option>
            <option value="first_moment" ${mixer.structuredControlFunctional === 'first_moment' ? 'selected' : ''}>first moment</option>
            <option value="second_moment" ${mixer.structuredControlFunctional === 'second_moment' ? 'selected' : ''}>second moment</option>
            <option value="protected_coordinate" ${mixer.structuredControlFunctional === 'protected_coordinate' ? 'selected' : ''}>protected coordinate</option>
          </select>
        </div>
        ${rangeField('structuredControlHorizon', 'History horizon', mixer.structuredControlHorizon, 1, 4, 1, 'labs.mixer')}
      ` : ''}
      ${mixer.family === 'boundary' ? `
        <div class="field">
          <label for="mixer-structured-boundary-architecture">Architecture</label>
          <select id="mixer-structured-boundary-architecture" data-path="labs.mixer.structuredBoundaryArchitecture">
            <option value="periodic_transplant" ${mixer.structuredBoundaryArchitecture === 'periodic_transplant' ? 'selected' : ''}>periodic projector transplant</option>
            <option value="boundary_compatible_hodge" ${mixer.structuredBoundaryArchitecture === 'boundary_compatible_hodge' ? 'selected' : ''}>boundary-compatible Hodge projector</option>
          </select>
        </div>
        <div class="field">
          <label for="mixer-structured-boundary-protected">Protected target</label>
          <select id="mixer-structured-boundary-protected" data-path="labs.mixer.structuredBoundaryProtected">
            <option value="bounded_velocity_class" ${mixer.structuredBoundaryProtected === 'bounded_velocity_class' ? 'selected' : ''}>bounded velocity class</option>
            <option value="divergence_certificate" ${mixer.structuredBoundaryProtected === 'divergence_certificate' ? 'selected' : ''}>divergence certificate</option>
          </select>
        </div>
        ${rangeField('structuredBoundaryGridSize', 'Benchmark grid size', mixer.structuredBoundaryGridSize, 9, 25, 2, 'labs.mixer')}
      ` : ''}
      ${rangeField('structuredDelta', 'Selected δ', mixer.structuredDelta, 0, 2.5, 0.05, 'labs.mixer')}
    ` : ''}
    ${mixer.mode === 'custom' ? `
      <div class="field">
        <label for="mixer-custom-family">Custom family</label>
        <select id="mixer-custom-family" data-path="labs.mixer.customFamily">
          ${Object.entries(DISCOVERY_MIXER_LIBRARY.customFamilies).map(([key, note]) => `<option value="${key}" ${mixer.customFamily === key ? 'selected' : ''}>${key}</option>`).join('')}
        </select>
        <small class="field-note">${DISCOVERY_MIXER_LIBRARY.customFamilies[mixer.customFamily]}</small>
      </div>
      ${mixer.customFamily === 'linear' ? `
        ${rangeField('customLinearDimension', 'State dimension', mixer.customLinearDimension, 2, 6, 1, 'labs.mixer')}
        <div class="field">
          <label for="mixer-custom-linear-observation">Observation rows</label>
          <textarea id="mixer-custom-linear-observation" data-path="labs.mixer.customLinearObservationText" rows="5">${mixer.customLinearObservationText}</textarea>
          <small class="field-note">Use numeric rows or linear expressions in x1..xn. One row per line.</small>
        </div>
        <div class="field">
          <label for="mixer-custom-linear-protected">Protected rows / functional</label>
          <textarea id="mixer-custom-linear-protected" data-path="labs.mixer.customLinearProtectedText" rows="3">${mixer.customLinearProtectedText}</textarea>
        </div>
        <div class="field">
          <label for="mixer-custom-linear-candidates">Candidate augmentation rows</label>
          <textarea id="mixer-custom-linear-candidates" data-path="labs.mixer.customLinearCandidateText" rows="4">${mixer.customLinearCandidateText}</textarea>
        </div>
      ` : ''}
      ${mixer.customFamily === 'periodic' ? `
        <div class="field">
          <label for="mixer-custom-periodic-functional">Protected modal functional</label>
          <textarea id="mixer-custom-periodic-functional" data-path="labs.mixer.customPeriodicFunctionalText" rows="3">${mixer.customPeriodicFunctionalText}</textarea>
          <small class="field-note">Supported variables: a1..a4. Only linear functionals are accepted.</small>
        </div>
        <div class="field">
          <label for="mixer-custom-periodic-observation">Observation map</label>
          <select id="mixer-custom-periodic-observation" data-path="labs.mixer.customPeriodicObservation">
            <option value="full_vorticity" ${mixer.customPeriodicObservation === 'full_vorticity' ? 'selected' : ''}>full vorticity</option>
            <option value="cutoff_vorticity" ${mixer.customPeriodicObservation === 'cutoff_vorticity' ? 'selected' : ''}>spectral cutoff vorticity</option>
            <option value="divergence_only" ${mixer.customPeriodicObservation === 'divergence_only' ? 'selected' : ''}>divergence only</option>
          </select>
        </div>
        ${rangeField('customPeriodicCutoff', 'Retained cutoff', mixer.customPeriodicCutoff, 1, 4, 1, 'labs.mixer')}
      ` : ''}
      ${mixer.customFamily === 'control' ? `
        <div class="field">
          <label for="mixer-custom-control-profile">Sensor profile</label>
          <textarea id="mixer-custom-control-profile" data-path="labs.mixer.customControlSensorProfileText" rows="2">${mixer.customControlSensorProfileText}</textarea>
          <small class="field-note">Comma-separated sensor weights on the diagonal benchmark family.</small>
        </div>
        <div class="field">
          <label for="mixer-custom-control-target">Protected target</label>
          <textarea id="mixer-custom-control-target" data-path="labs.mixer.customControlTargetText" rows="2">${mixer.customControlTargetText}</textarea>
          <small class="field-note">Supported forms: moment(k), xi, or a linear functional in x1..xn.</small>
        </div>
        ${rangeField('customControlHorizon', 'History horizon', mixer.customControlHorizon, 1, 4, 1, 'labs.mixer')}
      ` : ''}
      ${rangeField('customDelta', 'Selected δ', mixer.customDelta, 0, 2.5, 0.05, 'labs.mixer')}
    ` : ''}
    ${mixer.mode === 'random' ? `
      <div class="field">
        <label for="mixer-random-family">Random family</label>
        <select id="mixer-random-family" data-path="labs.mixer.randomFamily">
          ${Object.entries(DISCOVERY_MIXER_LIBRARY.randomFamilies).map(([key, note]) => `<option value="${key}" ${mixer.randomFamily === key ? 'selected' : ''}>${key}</option>`).join('')}
        </select>
        <small class="field-note">${DISCOVERY_MIXER_LIBRARY.randomFamilies[mixer.randomFamily]}</small>
      </div>
      ${rangeField('randomSeed', 'Seed', mixer.randomSeed, 1, 999, 1, 'labs.mixer')}
      ${rangeField('randomTrials', 'Search budget', mixer.randomTrials, 1, 64, 1, 'labs.mixer')}
      <div class="field">
        <label for="mixer-random-objective">Search objective</label>
        <select id="mixer-random-objective" data-path="labs.mixer.randomObjective">
          <option value="failure" ${mixer.randomObjective === 'failure' ? 'selected' : ''}>find a failing case with a repair</option>
          <option value="any" ${mixer.randomObjective === 'any' ? 'selected' : ''}>accept the first supported case</option>
        </select>
      </div>
    ` : ''}
  `;
}

function renderConfigPane() {
  switch (state.activeLab) {
    case 'mixer':
      return renderMixerConfigPane();
    case 'recoverability':
      return `
        <div class="field">
          <label>Validated demo scenarios</label>
          <div class="action-row wrap-row">
            ${Object.entries(STRUCTURAL_DISCOVERY_PRESETS)
              .map(([key, preset]) => `<button type="button" class="ghost-button" data-structural-demo="${key}">${preset.label}</button>`)
              .join('')}
          </div>
          <small class="field-note">Each preset starts from a real failing setup the studio can diagnose and repair inside the current theorem-backed or family-specific lanes.</small>
        </div>
        <div class="field">
          <label for="recoverability-studio-mode">Studio mode</label>
          <select id="recoverability-studio-mode" data-path="labs.recoverability.studioMode">
            <option value="guided" ${state.labs.recoverability.studioMode === 'guided' ? 'selected' : ''}>guided diagnosis</option>
            <option value="diagnostic" ${state.labs.recoverability.studioMode === 'diagnostic' ? 'selected' : ''}>raw diagnostics</option>
          </select>
        </div>
        <div class="field">
          <label for="recoverability-system">System family</label>
          <select id="recoverability-system" data-path="labs.recoverability.system">
            <option value="analytic" ${state.labs.recoverability.system === 'analytic' ? 'selected' : ''}>analytic benchmark</option>
            <option value="qubit" ${state.labs.recoverability.system === 'qubit' ? 'selected' : ''}>qubit fixed-basis record</option>
            <option value="periodic" ${state.labs.recoverability.system === 'periodic' ? 'selected' : ''}>periodic incompressible flow</option>
            <option value="control" ${state.labs.recoverability.system === 'control' ? 'selected' : ''}>functional observability model</option>
            <option value="linear" ${state.labs.recoverability.system === 'linear' ? 'selected' : ''}>reusable linear design template</option>
            <option value="boundary" ${state.labs.recoverability.system === 'boundary' ? 'selected' : ''}>bounded-domain architecture check</option>
          </select>
        </div>
        ${state.labs.recoverability.system === 'analytic' ? `
          ${rangeField('analyticEpsilon', 'Degeneracy parameter ε', state.labs.recoverability.analyticEpsilon, 0, 0.8, 0.01)}
          ${rangeField('analyticDelta', 'Selected δ', state.labs.recoverability.analyticDelta, 0, 1, 0.01)}
        ` : ''}
        ${state.labs.recoverability.system === 'qubit' ? `
          <div class="field">
            <label for="recoverability-qubit-protected">Protected variable</label>
            <select id="recoverability-qubit-protected" data-path="labs.recoverability.qubitProtected">
              <option value="bloch_vector" ${state.labs.recoverability.qubitProtected === 'bloch_vector' ? 'selected' : ''}>full Bloch vector</option>
              <option value="z_coordinate" ${state.labs.recoverability.qubitProtected === 'z_coordinate' ? 'selected' : ''}>z coordinate only</option>
            </select>
          </div>
          ${rangeField('qubitPhaseWindowDeg', 'Allowed phase window (degrees)', state.labs.recoverability.qubitPhaseWindowDeg, 0, 180, 5)}
          ${rangeField('qubitDelta', 'Selected δ', state.labs.recoverability.qubitDelta, 0, 1, 0.01)}
        ` : ''}
        ${state.labs.recoverability.system === 'periodic' ? `
          <div class="field">
            <label for="recoverability-periodic-observation">Observation map</label>
            <select id="recoverability-periodic-observation" data-path="labs.recoverability.periodicObservation">
              <option value="full_vorticity" ${state.labs.recoverability.periodicObservation === 'full_vorticity' ? 'selected' : ''}>full vorticity</option>
              <option value="cutoff_vorticity" ${state.labs.recoverability.periodicObservation === 'cutoff_vorticity' ? 'selected' : ''}>spectral cutoff vorticity</option>
              <option value="divergence_only" ${state.labs.recoverability.periodicObservation === 'divergence_only' ? 'selected' : ''}>divergence only</option>
            </select>
          </div>
          <div class="field">
            <label for="recoverability-periodic-protected">Protected variable</label>
            <select id="recoverability-periodic-protected" data-path="labs.recoverability.periodicProtected">
              <option value="mode_1_coefficient" ${state.labs.recoverability.periodicProtected === 'mode_1_coefficient' ? 'selected' : ''}>leading modal coefficient</option>
              <option value="modes_1_2_coefficients" ${state.labs.recoverability.periodicProtected === 'modes_1_2_coefficients' ? 'selected' : ''}>first two modal coefficients</option>
              <option value="low_mode_sum" ${state.labs.recoverability.periodicProtected === 'low_mode_sum' ? 'selected' : ''}>low-mode weighted sum</option>
              <option value="bandlimited_contrast" ${state.labs.recoverability.periodicProtected === 'bandlimited_contrast' ? 'selected' : ''}>band-limited contrast functional</option>
              <option value="full_weighted_sum" ${state.labs.recoverability.periodicProtected === 'full_weighted_sum' ? 'selected' : ''}>full weighted modal sum</option>
              <option value="full_modal_coefficients" ${state.labs.recoverability.periodicProtected === 'full_modal_coefficients' ? 'selected' : ''}>full four-mode coefficient vector</option>
            </select>
          </div>
          ${state.labs.recoverability.periodicObservation === 'cutoff_vorticity' ? rangeField('periodicCutoff', 'Retained Fourier cutoff', state.labs.recoverability.periodicCutoff, 0, 4, 1) : ''}
          ${rangeField('periodicDelta', 'Selected δ', state.labs.recoverability.periodicDelta, 0, 3, 0.05)}
        ` : ''}
        ${state.labs.recoverability.system === 'control' ? `
          <div class="field">
            <label for="recoverability-control-mode">Control family</label>
            <select id="recoverability-control-mode" data-path="labs.recoverability.controlMode">
              <option value="two_state_observer" ${state.labs.recoverability.controlMode === 'two_state_observer' ? 'selected' : ''}>two-state observer model</option>
              <option value="diagonal_threshold" ${state.labs.recoverability.controlMode === 'diagonal_threshold' ? 'selected' : ''}>three-state minimal-history model</option>
            </select>
          </div>
          ${state.labs.recoverability.controlMode === 'diagonal_threshold' ? `
            <div class="field">
              <label for="recoverability-control-profile">Sensor profile</label>
              <select id="recoverability-control-profile" data-path="labs.recoverability.controlProfile">
                <option value="three_active" ${state.labs.recoverability.controlProfile === 'three_active' ? 'selected' : ''}>three active coordinates</option>
                <option value="two_active" ${state.labs.recoverability.controlProfile === 'two_active' ? 'selected' : ''}>two active coordinates</option>
                <option value="protected_hidden" ${state.labs.recoverability.controlProfile === 'protected_hidden' ? 'selected' : ''}>protected coordinate hidden</option>
              </select>
            </div>
            <div class="field">
              <label for="recoverability-control-functional">Protected functional</label>
              <select id="recoverability-control-functional" data-path="labs.recoverability.controlFunctional">
                <option value="protected_coordinate" ${state.labs.recoverability.controlFunctional === 'protected_coordinate' ? 'selected' : ''}>third coordinate x₃</option>
                <option value="sensor_sum" ${state.labs.recoverability.controlFunctional === 'sensor_sum' ? 'selected' : ''}>sensor-weighted state sum</option>
                <option value="first_moment" ${state.labs.recoverability.controlFunctional === 'first_moment' ? 'selected' : ''}>first sensor moment</option>
                <option value="second_moment" ${state.labs.recoverability.controlFunctional === 'second_moment' ? 'selected' : ''}>second sensor moment</option>
              </select>
            </div>
          ` : ''}
          ${state.labs.recoverability.controlMode === 'two_state_observer' ? rangeField('controlEpsilon', 'Output coupling ε', state.labs.recoverability.controlEpsilon, 0, 0.8, 0.01) : ''}
          ${rangeField('controlHorizon', 'Finite record horizon', state.labs.recoverability.controlHorizon, 1, state.labs.recoverability.controlMode === 'diagonal_threshold' ? 4 : 3, 1)}
          ${rangeField('controlDelta', 'Selected δ', state.labs.recoverability.controlDelta, 0, state.labs.recoverability.controlMode === 'diagonal_threshold' ? 2 : 2.5, 0.05)}
        ` : ''}
        ${state.labs.recoverability.system === 'linear' ? renderRecoverabilityLinearControls() : ''}
        ${state.labs.recoverability.system === 'boundary' ? `
          <div class="field">
            <label for="recoverability-boundary-architecture">Architecture</label>
            <select id="recoverability-boundary-architecture" data-path="labs.recoverability.boundaryArchitecture">
              <option value="periodic_transplant" ${state.labs.recoverability.boundaryArchitecture === 'periodic_transplant' ? 'selected' : ''}>periodic projector transplant</option>
              <option value="boundary_compatible_hodge" ${state.labs.recoverability.boundaryArchitecture === 'boundary_compatible_hodge' ? 'selected' : ''}>boundary-compatible finite-mode Hodge projector</option>
            </select>
          </div>
          <div class="field">
            <label for="recoverability-boundary-protected">Protected target</label>
            <select id="recoverability-boundary-protected" data-path="labs.recoverability.boundaryProtected">
              <option value="bounded_velocity_class" ${state.labs.recoverability.boundaryProtected === 'bounded_velocity_class' ? 'selected' : ''}>full bounded protected class</option>
              <option value="divergence_certificate" ${state.labs.recoverability.boundaryProtected === 'divergence_certificate' ? 'selected' : ''}>bulk divergence certificate only</option>
            </select>
          </div>
          ${rangeField('boundaryGridSize', 'Grid size', state.labs.recoverability.boundaryGridSize, 13, 25, 2)}
          ${rangeField('boundaryDelta', 'Selected δ', state.labs.recoverability.boundaryDelta, 0, 1, 0.02)}
        ` : ''}
        <div class="callout ${latestAnalysis.impossible ? 'warn' : (latestAnalysis.exact || latestAnalysis.asymptotic) ? 'good' : ''}">
          <strong>${latestAnalysis.status}: ${latestAnalysis.classification}</strong>
          <p>${latestAnalysis.structuralBlocker} ${latestAnalysis.missingStructure}</p>
        </div>
      `;
    case 'exact':
      return `
        ${rangeField('protectedMagnitude', 'Protected magnitude', state.labs.exact.protectedMagnitude, 0.2, 2.5, 0.05)}
        ${rangeField('disturbanceMagnitude', 'Disturbance magnitude', state.labs.exact.disturbanceMagnitude, 0, 2.5, 0.05)}
        ${rangeField('angleDeg', 'Disturbance angle (degrees)', state.labs.exact.angleDeg, 15, 90, 1)}
        <div class="callout ${latestAnalysis.admissible ? 'good' : 'warn'}">
          <strong>${latestAnalysis.admissible ? 'Exact theorem applies.' : 'No-go witness active.'}</strong>
          <p>${latestAnalysis.admissible ? 'Protected and disturbance directions are orthogonal, so exact projector recovery is justified.' : 'The disturbance now overlaps the protected direction, so the same projector leaks contamination into the recovered state.'}</p>
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
          <strong>Exact sector recovery.</strong>
          <p>The disturbed logical state stays inside one orthogonal sector and the selected recovery maps it back to the code space without changing the logical coefficients.</p>
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
          <p>Exact projection should drive divergence much closer to zero than a short GLM run. If that stops being true, the example is no longer representing the repo’s strongest exact-versus-asymptotic split cleanly enough.</p>
        </div>
      `;
    case 'cfd':
      return `
        ${rangeField('contamination', 'Velocity contamination strength', state.labs.cfd.contamination, 0.02, 0.6, 0.01)}
        ${rangeField('periodicGridSize', 'Periodic grid size', state.labs.cfd.periodicGridSize, 10, 24, 2)}
        ${rangeField('boundedGridSize', 'Bounded grid size', state.labs.cfd.boundedGridSize, 12, 28, 2)}
        ${rangeField('poissonIterations', 'Reference projection iterations', state.labs.cfd.poissonIterations, 80, 500, 20)}
        <div class="callout ${latestAnalysis.boundedTransplantFails ? 'warn' : 'good'}">
          <strong>${latestAnalysis.boundedTransplantFails ? 'Boundary-sensitive limit detected.' : 'Recheck bounded example.'}</strong>
          <p>The periodic branch should remain exact, but the bounded-domain transplant should keep its boundary-normal mismatch. That split is what makes the CFD extension honest instead of overly broad.</p>
        </div>
      `;
    case 'gauge':
      return `
        ${rangeField('contamination', 'Longitudinal contamination strength', state.labs.gauge.contamination, 0.02, 0.6, 0.01)}
        ${rangeField('glmSteps', 'Damping steps', state.labs.gauge.glmSteps, 1, 20, 1)}
        ${rangeField('poissonIterations', 'Projection iterations', state.labs.gauge.poissonIterations, 80, 500, 20)}
        ${rangeField('dt', 'Damping timestep', state.labs.gauge.dt, 0.01, 0.1, 0.01)}
        <div class="callout good">
          <strong>Exact physics extension.</strong>
          <p>This module keeps the same exact projector logic as the periodic branch but changes the interpretation: the protected object is now the transverse component, and the disturbance is the longitudinal gauge piece.</p>
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
          <p>${latestAnalysis.mixingNorm < 1e-8 ? 'This generator respects the protected/disturbance split and belongs to the asymptotic correction branch.' : 'This generator may damp disturbance overall, but it also injects disturbance into the protected coordinates, so it fails the protected-state correction criterion.'}</p>
        </div>
      `;
    case 'benchmark':
      return `
        <div class="field">
          <label for="benchmark-suite">Console focus</label>
          <select id="benchmark-suite" data-path="labs.benchmark.suite">
            <option value="all" ${state.labs.benchmark.suite === 'all' ? 'selected' : ''}>all results</option>
            <option value="demos" ${state.labs.benchmark.suite === 'demos' ? 'selected' : ''}>demo repairs only</option>
            <option value="modules" ${state.labs.benchmark.suite === 'modules' ? 'selected' : ''}>module health only</option>
          </select>
        </div>
        <div class="field">
          <label for="benchmark-demo">Selected demo</label>
          <select id="benchmark-demo" data-path="labs.benchmark.selectedDemo">
            ${latestAnalysis.demoRows.map((row) => `<option value="${row.demo}" ${state.labs.benchmark.selectedDemo === row.demo ? 'selected' : ''}>${row.label}</option>`).join('')}
          </select>
        </div>
        <div class="callout good">
          <strong>Validation-facing console.</strong>
          <p>This surface gathers the built-in repair demos, module health checks, and reproducibility exports in one place so the workbench is auditable instead of purely visual.</p>
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
            <option value="divergence-only" ${state.labs.nogo.example === 'divergence-only' ? 'selected' : ''}>Divergence-only bounded recovery</option>
            <option value="boundary" ${state.labs.nogo.example === 'boundary' ? 'selected' : ''}>Bounded-domain projector transplant</option>
          </select>
        </div>
        <div class="callout warn">
          <strong>Negative results are part of the theory.</strong>
          <p>This explorer keeps the repo honest. Each example corresponds to a theorem, a counterexample, or an explicit rejection decision.</p>
        </div>
      `;
  }
}

function rangeField(key, label, value, min, max, step, labOverride = state.activeLab) {
  return `
    <div class="field">
      <label for="${labOverride}-${key}">${label}</label>
      <div class="range-row">
        <input id="${labOverride}-${key}" type="range" min="${min}" max="${max}" step="${step}" value="${value}" data-path="labs.${labOverride}.${key}" />
        <output>${Number(value).toFixed(step >= 1 ? 0 : 2)}</output>
      </div>
    </div>
  `;
}

function formatDisplayValue(value) {
  if (typeof value === 'number') {
    if (!Number.isFinite(value)) return String(value);
    if (Math.abs(value) >= 1000 || (Math.abs(value) > 0 && Math.abs(value) < 1e-2)) {
      return value.toExponential(3);
    }
    return value.toFixed(3);
  }
  if (typeof value === 'boolean') return value ? 'yes' : 'no';
  if (typeof value === 'string') return value;
  return JSON.stringify(value, null, 2);
}

function renderVisualStage() {
  switch (state.activeLab) {
    case 'mixer':
      return renderMixerStage();
    case 'recoverability':
      return renderRecoverabilityStage();
    case 'benchmark':
      return renderBenchmarkStage();
    case 'exact':
      return renderExactStage();
    case 'qec':
      return renderQecStage();
    case 'mhd':
      return renderMhdStage();
    case 'cfd':
      return renderCfdStage();
    case 'gauge':
      return renderGaugeStage();
    case 'continuous':
      return renderContinuousStage();
    case 'nogo':
    default:
      return renderNoGoStage();
  }
}

function resolveActiveMixerConfig() {
  const config = cloneState(state.labs.mixer);
  if ((config.mode ?? 'structured') !== 'demo') return config;
  const demo = DISCOVERY_MIXER_DEMOS[config.demoKey ?? 'periodic_builder'];
  if (!demo) return config;
  return {
    ...config,
    ...cloneState(demo.patch),
    mode: demo.mode,
    family: demo.family,
  };
}

function mixerSeverityClass(severity) {
  if (severity === 'success') return 'success';
  if (severity === 'warning') return 'warning';
  if (severity === 'error') return 'error';
  return 'info';
}

function mixerMetricFigure(analysis) {
  if (analysis.unsupported) {
    return `
      <div class="callout warn">
        <strong>Unsupported composition</strong>
        <p>The current mixer state could not be reduced to one of the supported typed families, so no structural threshold or recoverability chart is promoted here.</p>
      </div>
    `;
  }
  const resolved = resolveActiveMixerConfig();
  if (analysis.family === 'periodic') {
    const cutoffKey = resolved.mode === 'custom' ? 'customPeriodicCutoff' : 'structuredPeriodicCutoff';
    const points = Array.from({ length: 4 }, (_, index) => {
      const cutoff = index + 1;
      const report = analyzeDiscoveryMixer({ ...resolved, [cutoffKey]: cutoff });
      return { x: cutoff, y: report.rawDetails?.kappa0 ?? 0 };
    });
    return `
      ${lineChartSvg(points, 'retained cutoff', 'κ(0)', resolved[cutoffKey])}
      <small>Periodic threshold scan: the zero-noise collision gap collapses only when the retained cutoff contains the protected modal support.</small>
    `;
  }
  if (analysis.family === 'control') {
    const horizonKey = resolved.mode === 'custom' ? 'customControlHorizon' : 'structuredControlHorizon';
    const points = Array.from({ length: 4 }, (_, index) => {
      const horizon = index + 1;
      const report = analyzeDiscoveryMixer({ ...resolved, [horizonKey]: horizon });
      return { x: horizon, y: report.rawDetails?.collisionGap ?? 0 };
    });
    return `
      ${lineChartSvg(points, 'history horizon', 'collision gap', resolved[horizonKey])}
      <small>Diagonal/history threshold scan: exact finite-history recovery begins at the first horizon where the protected functional is generated by the sensed history rows.</small>
    `;
  }
  if (analysis.family === 'linear' && Array.isArray(analysis.rawDetails?.rowResiduals) && analysis.rawDetails.rowResiduals.length) {
    const rawPoints = analysis.rawDetails.rowResiduals.map((value, index) => ({ x: index + 1, y: value }));
    const points = rawPoints.length === 1 ? [...rawPoints, { x: 2, y: rawPoints[0].y }] : rawPoints;
    return `
      ${lineChartSvg(points, 'protected row index', 'row-space residual', rawPoints[0].x)}
      <small>Restricted-linear residual profile: any nonzero protected-row residual witnesses a structural exactness failure on the current admissible family.</small>
    `;
  }
  if (analysis.comparison) {
    const points = [
      { x: 1, y: analysis.comparison.keyMetricBefore },
      { x: 2, y: analysis.comparison.keyMetricAfter },
    ];
    return `
      ${lineChartSvg(points, 'configuration (1 = before, 2 = after)', analysis.comparison.keyMetricName, 2)}
      <small>Before/after evidence uses the same branch metric before the recommended structural change and after it is applied.</small>
    `;
  }
  return `
    <div class="callout ${analysis.exact ? 'good' : analysis.impossible ? 'warn' : ''}">
      <strong>No dedicated threshold chart for this case</strong>
      <p>The current supported evidence is textual and algebraic rather than a family sweep. Use the raw details and theorem links below for the precise diagnostic trail.</p>
    </div>
  `;
}

function renderMixerStage() {
  const a = latestAnalysis;
  const summaryTone = a.unsupported ? 'warn' : a.impossible ? 'warn' : a.exact ? 'good' : '';
  const objectCards = a.objects?.length
    ? a.objects
        .map(
          (item) => `
            <article class="object-card">
              <div class="recommendation-header">
                <span class="recommendation-kind">${item.objectType.replaceAll('_', ' ')}</span>
                <span class="recommendation-regime">${item.supportStatus}</span>
              </div>
              <strong>${item.label}</strong>
              <div class="object-meta">
                <span><strong>family:</strong> ${item.family}</span>
                <span><strong>map:</strong> ${item.domain} → ${item.codomain}</span>
                <span><strong>basis:</strong> ${item.basis}</span>
                <span><strong>dimension:</strong> ${item.dimension}</span>
              </div>
              <ul class="detail-list">
                ${item.compatibilityRequirements.map((entry) => `<li>${entry}</li>`).join('')}
              </ul>
            </article>
          `
        )
        .join('')
    : '<div class="callout warn"><strong>No typed objects emitted</strong><p>This happens only when the input never reduced into a supported typed family.</p></div>';
  const diagnosticCards = a.diagnostics?.length
    ? a.diagnostics
        .map(
          (item) => `
            <article class="diagnostic-card ${mixerSeverityClass(item.severity)}">
              <div class="recommendation-header">
                <span class="recommendation-kind">${item.severity}</span>
                <span class="recommendation-regime">${item.theoremStatus}</span>
              </div>
              <strong>${item.title}</strong>
              <p>${item.detail}</p>
              <small class="diagnostic-code">${item.code}</small>
            </article>
          `
        )
        .join('')
    : '<div class="callout"><strong>No diagnostics returned</strong><p>The current case did not emit additional diagnostic rows.</p></div>';
  const recommendationCards = a.recommendations?.length
    ? a.recommendations
        .map((item, index) => {
          const expectedLabel = item.expectedRegime
            ?? (item.actionKind === 'weaken_target'
              ? 'alternative target'
              : item.actionKind === 'reformulate'
                ? 'unsupported'
                : item.availableInStudio
                  ? 'testable fix'
                  : 'advisory');
          const tone = item.expectedRegime === 'exact' || item.availableInStudio
            ? 'good'
            : item.expectedRegime === 'unsupported'
              ? 'neutral'
              : '';
          return `
            <article class="recommendation-card card-surface ${tone}">
              <div class="recommendation-header">
                <span class="recommendation-kind">${item.actionKind.replaceAll('_', ' ')}</span>
                <span class="recommendation-regime">${expectedLabel}</span>
              </div>
              <strong>${item.title}</strong>
              <p>${item.rationale}</p>
              <div class="recommendation-meta">
                <span>${item.theoremStatus}</span>
                <span>${item.minimal ? 'minimal change' : 'larger redesign'}</span>
                <span>${item.availableInStudio ? 'testable in mixer' : 'advisory only'}</span>
              </div>
              <div class="action-row">
                ${item.availableInStudio && item.patch ? `<button class="primary" data-apply-mixer-recommendation="${index}">Apply and compare</button>` : ''}
                ${item.cost !== undefined && item.cost !== null ? `<button class="ghost-button" disabled>cost: ${item.cost} ${item.costUnit ?? ''}</button>` : ''}
              </div>
            </article>
          `;
        })
        .join('')
    : '<div class="callout"><strong>No fix candidate was promoted</strong><p>The current case either already works, is unsupported, or only supports a documentation-level redesign rather than an in-studio patch.</p></div>';
  const comparisonPanel = a.comparison
    ? `
      <div class="before-after-grid">
        <article class="before-after-card before">
          <small>Before</small>
          <strong>${a.comparison.beforeRegime}</strong>
          <code>${a.comparison.keyMetricName}: ${formatDisplayValue(a.comparison.keyMetricBefore)}</code>
        </article>
        <article class="before-after-card after">
          <small>After</small>
          <strong>${a.comparison.afterRegime}</strong>
          <code>${a.comparison.keyMetricName}: ${formatDisplayValue(a.comparison.keyMetricAfter)}</code>
        </article>
      </div>
      <p class="studio-note">${a.comparison.narrative}</p>
    `
    : `
      <div class="callout ${summaryTone}">
        <strong>No before/after patch is currently attached</strong>
        <p>${a.missingStructure}</p>
      </div>
    `;
  const detailEntries = Object.entries(a.rawDetails ?? {});
  const rawDetails = detailEntries.length
    ? detailEntries
        .map(
          ([key, value]) => `
            <article class="detail-card">
              <small>${key}</small>
              <code>${typeof value === 'object' ? JSON.stringify(value, null, 2) : formatDisplayValue(value)}</code>
            </article>
          `
        )
        .join('')
    : '<div class="callout"><strong>No raw details emitted</strong><p>This case did not return an additional raw detail bundle.</p></div>';
  const theoremLinks = (a.theoremLinks ?? [])
    .map((href) => `<a href="${href}"><strong>${href.split('/').at(-1)}</strong><small>${href}</small></a>`)
    .join('');
  const generatedConfig = a.generatedConfig
    ? `
      <div class="callout">
        <strong>Generated case</strong>
        <p>This seeded exploration produced a reproducible supported configuration.</p>
        <code>${JSON.stringify(a.generatedConfig, null, 2)}</code>
      </div>
    `
    : '';
  return `
    <div class="figure-grid double">
      <div class="figure" data-exportable="true">
        <h4>Structural verdict and threshold evidence</h4>
        ${mixerMetricFigure(a)}
      </div>
      <div class="figure">
        <h4>Composition summary</h4>
        <div class="callout ${summaryTone}">
          <strong>${a.status}</strong>
          <p>${a.rootCause}</p>
        </div>
        <div class="action-row top-gap">
          <span class="fit-pill">${a.familyLabel}</span>
          <span class="fit-pill subtle">${a.theoremStatus}</span>
          <span class="fit-pill subtle">${a.architectureLabel}</span>
        </div>
        <ul class="guidance-list">
          <li><strong>Protected target:</strong> ${a.protectedLabel}</li>
          <li><strong>Record / architecture:</strong> ${a.observationLabel}</li>
          <li><strong>Missing structure:</strong> ${a.missingStructure}</li>
          <li><strong>Recoverable weaker target:</strong> ${a.targetSplitSummary}</li>
          <li><strong>Supported scope:</strong> ${a.supportScope}</li>
        </ul>
        ${generatedConfig}
      </div>
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure">
        <h4>Typed composition inventory</h4>
        <div class="object-grid">
          ${objectCards}
        </div>
      </div>
      <div class="figure">
        <h4>Compatibility and failure diagnostics</h4>
        <div class="diagnostic-list">
          ${diagnosticCards}
        </div>
      </div>
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure">
        <h4>Structural discovery and redesign</h4>
        <div class="recommendation-grid">
          ${recommendationCards}
        </div>
      </div>
      <div class="figure">
        <h4>Before / after evidence</h4>
        ${comparisonPanel}
      </div>
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure">
        <h4>Supported calculations and provenance</h4>
        <ul class="guidance-list">
          ${(a.supportedCalculations ?? []).map((entry) => `<li>${entry}</li>`).join('')}
        </ul>
        <div class="ref-list top-gap">
          ${theoremLinks || '<span class="studio-note">No theorem or note links were attached to this case.</span>'}
        </div>
      </div>
      <div class="figure">
        <h4>Deep detail</h4>
        <div class="detail-grid">
          ${rawDetails}
        </div>
      </div>
    </div>
  `;
}

function renderRecoverabilityStage() {
  const a = latestAnalysis;
  const guidedMode = state.labs.recoverability.studioMode !== 'diagnostic';
  const guidanceTone = a.impossible ? 'warn' : (a.exact || a.asymptotic) ? 'good' : '';
  const recommendationCards = `
    <div class="recommendation-grid">
      ${a.recommendations
        .map(
          (item, index) => `
            <article class="recommendation-card card-surface ${item.actionKind === 'keep' ? 'neutral' : item.expectedRegime === 'exact' ? 'good' : ''}">
              <div class="recommendation-header">
                <span class="recommendation-kind">${item.actionKind.replaceAll('_', ' ')}</span>
                <span class="recommendation-regime">${item.expectedRegime}</span>
              </div>
              <strong>${item.title}</strong>
              <p>${item.rationale}</p>
              <div class="recommendation-meta">
                <span>${item.theoremStatus}</span>
                <span>${item.minimal ? 'minimal change' : 'non-minimal change'}</span>
                <span>${item.availableInStudio ? 'testable here' : 'doc-linked only'}</span>
              </div>
              <div class="action-row">
                ${item.availableInStudio && item.patch ? `<button class="primary" data-apply-recommendation="${index}">Apply in studio</button>` : ''}
                ${item.cost !== undefined && item.cost !== null ? `<button class="ghost-button" disabled>Cost: ${item.cost} ${item.costUnit ?? ''}</button>` : ''}
              </div>
            </article>
          `
        )
        .join('')}
    </div>
  `;
  const comparisonPanel = a.comparison
    ? `
      <div class="figure-grid double top-gap">
        <div class="figure" data-exportable="true">
          <h4>Before / after evidence</h4>
          <div class="before-after-grid">
            <div class="before-after-card before">
              <small>Before</small>
              <strong>${a.comparison.beforeRegime}</strong>
              <code>${a.comparison.keyMetricName}: ${Number(a.comparison.keyMetricBefore).toExponential(3)}</code>
            </div>
            <div class="before-after-card after">
              <small>After</small>
              <strong>${a.comparison.afterRegime}</strong>
              <code>${a.comparison.keyMetricName}: ${Number(a.comparison.keyMetricAfter).toExponential(3)}</code>
            </div>
          </div>
          <small>${a.comparison.narrative}</small>
        </div>
        <div class="figure">
          <h4>Discovery provenance</h4>
          <div class="value-grid">
            <div><small>Theorem / evidence status</small><code>${a.theoremStatus}</code></div>
            <div><small>Missing structure</small><code>${a.missingStructure}</code></div>
            <div><small>Primary blocker</small><code>${a.structuralBlocker}</code></div>
            <div><small>Chosen fix</small><code>${a.chosenRecommendation ? a.chosenRecommendation.title : 'none'}</code></div>
          </div>
        </div>
      </div>
    `
    : '';
  const secondaryFigure = (() => {
    if (state.labs.recoverability.system === 'qubit') {
      return `
        <div class="figure">
          <h4>Fiber-collision boundary</h4>
          ${lineChartSvg(
            a.boundaryWindows.map((value, index) => ({ x: value, y: a.boundaryValues[index] })),
            'phase window (degrees)',
            'κ(0)',
            a.phaseWindowDeg
          )}
          <small>The full Bloch-vector protected variable fails as soon as the phase window opens, while the z-only protected variable stays recoverable.</small>
        </div>
      `;
    }
    if (state.labs.recoverability.system === 'periodic') {
      return `
        <div class="figure">
          <h4>Modal cutoff threshold</h4>
          ${lineChartSvg(
            a.thresholdCutoffs.map((value, index) => ({ x: value, y: a.thresholdKappa0[index] })),
            'cutoff',
            'κ(0)',
            a.currentCutoff
          )}
          <small>On this finite modal family, exact recovery turns on exactly when the cutoff retains every mode that the chosen protected functional depends on.</small>
        </div>
      `;
    }
    if (state.labs.recoverability.system === 'control') {
      return `
        <div class="figure">
          <h4>History-length threshold</h4>
          ${lineChartSvg(
            a.historyThreshold.map((item) => ({ x: item.horizon, y: item.kappa0 })),
            'horizon',
            'κ(0)',
            Number(state.labs.recoverability.controlHorizon)
          )}
          <small>${state.labs.recoverability.controlMode === 'diagonal_threshold' ? 'This diagonal family now exposes a stronger functional law: exact recovery starts once the finite history is rich enough to interpolate the chosen protected functional from the active sensor moments.' : 'For the two-state observer model, one-step output history is not enough, while two steps already separate the protected coordinate whenever ε is nonzero.'}</small>
        </div>
      `;
    }
    if (state.labs.recoverability.system === 'linear') {
      return `
        <div class="figure">
          <h4>Protected-row residuals</h4>
          ${barChartSvg([{ label: 'Residuals', values: a.rowResiduals }])}
          <small>Residual 0 means that the protected row already lies in the active record row space. Positive residual means the current record still loses protected information.</small>
        </div>
      `;
    }
    if (state.labs.recoverability.system === 'boundary') {
      return `
        <div class="figure">
          <h4>Architecture threshold</h4>
          ${lineChartSvg(
            a.boundaryArchitectureSeries.map((item) => ({ x: item.x, y: item.y })),
            'architecture step',
            a.boundaryProtectedTarget === 'bounded_velocity_class' ? 'strong-target obstruction' : 'bulk divergence residual',
            a.boundaryArchitecture === 'boundary_compatible_hodge' ? 1 : 0
          )}
          <small>The bounded-domain issue is architectural: the periodic transplant can reduce divergence without preserving the strong bounded protected class, while the boundary-compatible finite-mode family restores exactness on its restricted admissible set.</small>
        </div>
      `;
    }
    return `
      <div class="figure">
        <h4>Noise lower bound</h4>
        ${lineChartSvg(
          a.deltas.map((value, index) => ({ x: value, y: a.noiseLowerBounds[index] })),
          'noise radius η',
          'worst-case error lower bound',
          a.selectedDelta
        )}
        <small>Any estimator must incur worst-case protected-variable error at least κ(η)/2 once the record can be perturbed by η.</small>
      </div>
    `;
  })();

  const tertiaryFigure = (() => {
    if (state.labs.recoverability.system === 'control' && state.labs.recoverability.controlMode === 'two_state_observer') {
      return `
        <div class="figure top-gap">
          <h4>Observer convergence</h4>
          ${
            a.observerErrorHistory.length
              ? lineChartSvg(
                  a.observerErrorHistory.map((value, index) => ({ x: index, y: value })),
                  'step',
                  '|protected-variable error|'
                )
              : '<p class="empty-state">No asymptotic observer is available when ε = 0.</p>'
          }
          <small>Single-shot recovery can fail even when an observer still converges asymptotically from the ongoing record.</small>
        </div>
      `;
    }
    if (state.labs.recoverability.system === 'linear') {
      return `
        <div class="figure top-gap">
          <h4>Minimal fixes and weaker targets</h4>
          <div class="value-grid">
            <div><small>Active measurements</small><code>${a.activeMeasurementLabels.length ? a.activeMeasurementLabels.join('\n') : 'none'}</code></div>
            <div><small>Minimal exact fixes</small><code>${a.candidateExactSets.length ? a.candidateExactSets.map((set) => set.join(' + ')).join('\n') : 'no exact fix in current candidate library'}</code></div>
            <div><small>Weaker recoverable targets</small><code>${a.weakerProtectedOptions.length ? a.weakerProtectedOptions.join('\n') : 'none'}</code></div>
            <div><small>Nullspace witness</small><code>${a.nullspaceWitness ? formatVector(a.nullspaceWitness) : 'none'}</code></div>
          </div>
        </div>
      `;
    }
    return '';
  })();

  const systemDiagnostics = (() => {
    if (state.labs.recoverability.system === 'analytic') {
      return `
        <div class="figure">
          <h4>Conditioning and robustness</h4>
          <div class="value-grid">
            <div><small>Degeneracy ε</small><code>${a.epsilon.toFixed(3)}</code></div>
            <div><small>Amplification</small><code>${Number.isFinite(a.amplification) ? a.amplification.toFixed(3) : '∞'}</code></div>
            <div><small>Selected lower bound</small><code>${a.selectedLowerBound.toExponential(3)}</code></div>
            <div><small>Interpretation</small><code>${a.missingStructure}</code></div>
          </div>
        </div>
      `;
    }
    if (state.labs.recoverability.system === 'qubit') {
      return `
        <div class="figure">
          <h4>Measurement sufficiency</h4>
          <div class="value-grid">
            <div><small>Phase window</small><code>${a.phaseWindowDeg.toFixed(0)}°</code></div>
            <div><small>Protected target</small><code>${a.protectedLabel}</code></div>
            <div><small>Weaker recoverable target</small><code>${a.weakerRecoverableTargets.length ? a.weakerRecoverableTargets.join('\n') : 'none needed'}</code></div>
            <div><small>Missing structure</small><code>${a.missingStructure}</code></div>
          </div>
        </div>
      `;
    }
    if (state.labs.recoverability.system === 'periodic') {
      return `
        <div class="figure">
          <h4>Record-complexity diagnostics</h4>
          <div class="value-grid">
            <div><small>Current cutoff</small><code>${a.currentCutoff ?? 'n/a'}</code></div>
            <div><small>Predicted minimum cutoff</small><code>${a.predictedMinCutoff ?? 'n/a'}</code></div>
            <div><small>Weaker recoverable targets</small><code>${a.weakerRecoverableTargets.length ? a.weakerRecoverableTargets.join('\n') : 'none below current cutoff'}</code></div>
            <div><small>No-go / threshold</small><code>${a.guidance.noGo ?? 'none'}</code></div>
          </div>
        </div>
      `;
    }
    if (state.labs.recoverability.system === 'control') {
      return `
        <div class="figure">
          <h4>Finite-history diagnostics</h4>
          <div class="value-grid">
            <div><small>Control mode</small><code>${a.controlModeLabel}</code></div>
            <div><small>Current horizon</small><code>${state.labs.recoverability.controlHorizon}</code></div>
            <div><small>Predicted minimum horizon</small><code>${a.predictedMinHorizon === null ? 'none' : a.predictedMinHorizon}</code></div>
            <div><small>Observer spectral radius</small><code>${a.spectralRadius === null ? 'n/a' : a.spectralRadius.toFixed(3)}</code></div>
          </div>
        </div>
      `;
    }
    if (state.labs.recoverability.system === 'linear') {
      return `
        <div class="figure">
          <h4>Linear design diagnosis</h4>
          <div class="value-grid">
            <div><small>Active measurements</small><code>${a.activeMeasurementLabels.length}</code></div>
            <div><small>Record / protected rank</small><code>${a.rankObservation} / ${a.rankProtected}</code></div>
            <div><small>Minimal added measurements</small><code>${a.minimalAddedMeasurements === null ? 'none available' : a.minimalAddedMeasurements}</code></div>
            <div><small>Exact-regime upper bound</small><code>${a.selectedStabilityUpperBound === null ? 'n/a' : a.selectedStabilityUpperBound.toExponential(3)}</code></div>
            <div><small>Witness gap</small><code>${a.nullspaceWitnessGap.toExponential(3)}</code></div>
            <div><small>Unrecoverable protected rows</small><code>${a.unrecoverableProtectedRows.length}</code></div>
          </div>
        </div>
      `;
    }
    if (state.labs.recoverability.system === 'boundary') {
      return `
        <div class="figure">
          <h4>Boundary compatibility diagnostics</h4>
          <div class="value-grid">
            <div><small>Current architecture</small><code>${a.boundaryArchitecture.replaceAll('_', ' ')}</code></div>
            <div><small>Protected target</small><code>${a.protectedLabel}</code></div>
            <div><small>Transplant boundary mismatch</small><code>${a.transplantBoundaryMismatch.toExponential(3)}</code></div>
            <div><small>Compatible recovery error</small><code>${a.compatibleRecoveryError.toExponential(3)}</code></div>
            <div><small>Compatible orthogonality residual</small><code>${a.compatibleOrthogonalityResidual.toExponential(3)}</code></div>
            <div><small>Weaker recoverable target</small><code>${a.weakerRecoverableTargets.length ? a.weakerRecoverableTargets.join('\n') : 'none needed'}</code></div>
          </div>
        </div>
      `;
    }
    return `
      <div class="figure">
        <h4>Branch diagnostics</h4>
        <div class="value-grid">
          <div><small>Selected δ</small><code>${a.selectedDelta.toFixed(3)}</code></div>
          <div><small>Mean recovery error</small><code>${a.meanRecoveryError.toExponential(3)}</code></div>
          <div><small>Worst sampled error</small><code>${a.maxRecoveryError.toExponential(3)}</code></div>
          <div><small>Architecture</small><code>${a.guidance.architecture}</code></div>
        </div>
      </div>
    `;
  })();

  return `
    <div class="figure-grid double">
      <div class="figure" data-exportable="true">
        <h4>Recoverability-collapse curve</h4>
        ${lineChartSvg(a.deltas.map((value, index) => ({ x: value, y: a.collapse[index] })), 'δ', 'κ(δ)', a.selectedDelta)}
        <small>κ(δ) measures how much protected-variable ambiguity remains among states whose records stay within δ.</small>
      </div>
      ${secondaryFigure}
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure">
        <h4>Failure analysis</h4>
        <div class="callout ${guidanceTone}">
          <strong>${a.recommendedArchitecture}</strong>
          <p>${guidedMode ? a.missingStructure : a.structuralBlocker}</p>
        </div>
        <ul class="guidance-list">
          ${a.failureModes.map((mode) => `<li>${mode}</li>`).join('')}
        </ul>
        <p class="studio-note"><strong>Weaker target now recoverable:</strong> ${a.weakerRecoverableTargets.length ? a.weakerRecoverableTargets.join(', ') : 'None currently suggested.'}</p>
      </div>
      <div class="figure">
        <h4>Minimal fixes and redesigns</h4>
        ${recommendationCards}
      </div>
    </div>
    ${comparisonPanel}
    <div class="figure-grid double top-gap">
      <div class="figure">
        <h4>Decision workflow</h4>
        <div class="workflow-list">
          ${a.workflow
            .map(
              (step) => `
                <article class="workflow-step ${step.status}">
                  <span>${step.label}</span>
                  <strong>${step.status.replace('-', ' ')}</strong>
                  <p>${step.detail}</p>
                </article>
              `
            )
            .join('')}
        </div>
      </div>
      <div class="figure">
        <h4>${guidedMode ? 'What should I do next?' : 'Why this verdict was returned'}</h4>
        <div class="callout ${guidanceTone}">
          <strong>${a.guidance.architecture}</strong>
          <p>${guidedMode ? a.guidance.missing : a.guidance.blocker}</p>
        </div>
        <ul class="guidance-list">
          ${a.guidance.nextSteps.map((step) => `<li>${step}</li>`).join('')}
        </ul>
        <p class="studio-note"><strong>Blocking boundary:</strong> ${a.guidance.noGo ?? 'None. The current architecture is admissible on the chosen family.'}</p>
        <p class="studio-note"><strong>Weaker recoverable target:</strong> ${a.guidance.weaker.length ? a.guidance.weaker.join(', ') : 'No weaker alternative is currently suggested.'}</p>
      </div>
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure">
        <h4>Classification and evidence</h4>
        <div class="value-grid">
          <div><small>Status</small><code>${a.status}</code></div>
          <div><small>Branch verdict</small><code>${a.classification}</code></div>
          <div><small>System</small><code>${a.systemLabel}</code></div>
          <div><small>Observation</small><code>${a.observationLabel}</code></div>
          <div><small>Protected variable</small><code>${a.protectedLabel}</code></div>
          <div><small>κ(0)</small><code>${a.kappa0.toExponential(3)}</code></div>
          <div><small>Selected κ(δ)</small><code>${a.selectedKappa.toExponential(3)}</code></div>
          <div><small>Selected δ</small><code>${a.selectedDelta.toFixed(3)}</code></div>
          <div><small>Mean recovery error</small><code>${a.meanRecoveryError.toExponential(3)}</code></div>
          <div><small>Worst sampled error</small><code>${a.maxRecoveryError.toExponential(3)}</code></div>
          <div><small>Exact</small><code>${a.exact ? 'yes' : 'no'}</code></div>
          <div><small>Asymptotic</small><code>${a.asymptotic ? 'yes' : 'no'}</code></div>
          <div><small>Impossible</small><code>${a.impossible ? 'yes' : 'no'}</code></div>
        </div>
      </div>
      ${systemDiagnostics}
    </div>
    ${tertiaryFigure}
  `;
}

function renderBenchmarkStage() {
  const suite = state.labs.benchmark.suite;
  const demoRows = suite === 'modules' ? [] : latestAnalysis.demoRows;
  const moduleRows = suite === 'demos' ? [] : latestAnalysis.moduleRows;
  const selected = latestAnalysis.selectedDemoRow;
  return `
    <div class="figure-grid double">
      <div class="figure" data-exportable="true">
        <h4>Validated demo regime changes</h4>
        ${lineChartSvg(
          latestAnalysis.demoRows.map((row, index) => ({ x: index + 1, y: row.metricBefore })),
          'demo index',
          'before metric'
        )}
        <small>The console keeps the built-in repair stories visible as measurable before/after transitions rather than as static screenshots.</small>
      </div>
      <div class="figure">
        <h4>Console summary</h4>
        <div class="value-grid">
          <div><small>Demos</small><code>${latestAnalysis.summary.demoCount}</code></div>
          <div><small>Regime changes</small><code>${latestAnalysis.summary.regimeChangeCount}</code></div>
          <div><small>Exact after fix</small><code>${latestAnalysis.summary.exactAfterCount}</code></div>
          <div><small>Benchmarked modules</small><code>${latestAnalysis.summary.moduleCount}</code></div>
        </div>
      </div>
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure">
        <h4>Selected demo</h4>
        <div class="value-grid">
          <div><small>Demo</small><code>${selected.label}</code></div>
          <div><small>Family</small><code>${selected.family}</code></div>
          <div><small>Before</small><code>${selected.beforeRegime}</code></div>
          <div><small>After</small><code>${selected.afterRegime}</code></div>
          <div><small>Key metric</small><code>${selected.metricName}</code></div>
          <div><small>Fix</small><code>${selected.fixTitle}</code></div>
          <div><small>Theorem status</small><code>${selected.theoremStatus}</code></div>
        </div>
        <div class="action-row top-gap">
          <button class="primary" data-open-demo="${selected.demo}">Open this demo in the studio</button>
        </div>
      </div>
      <div class="figure">
        <h4>Demo repair table</h4>
        <div class="benchmark-table">
          <table class="matrix-table">
            <thead>
              <tr><th>Demo</th><th>Before</th><th>After</th><th>Fix</th></tr>
            </thead>
            <tbody>
              ${demoRows.map((row) => `<tr><th>${row.label}</th><td>${row.beforeRegime}</td><td>${row.afterRegime}</td><td>${row.fixTitle}</td></tr>`).join('')}
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="figure top-gap">
      <h4>Module health map</h4>
      <div class="benchmark-module-grid">
        ${moduleRows.map((row) => `
          <article class="benchmark-module-card">
            <strong>${row.label}</strong>
            <span>${row.verdict}</span>
            <small>${row.evidence}</small>
          </article>
        `).join('')}
      </div>
    </div>
  `;
}

function renderExactStage() {
  const a = latestAnalysis;
  return `
    <div class="figure-grid double">
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
    <div class="figure-grid double">
      <div class="figure" data-exportable="true">
        <h4>Amplitude comparison</h4>
        ${barChartSvg([
          { label: 'Logical', values: a.logical },
          { label: `Disturbed (${a.selectedLabel})`, values: a.disturbed },
          { label: 'Recovered', values: a.recovered },
        ])}
        <small>The selected recovery should return the logical amplitudes exactly for the chosen bit-flip sector.</small>
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
  const a = latestAnalysis;
  return `
    <div class="figure-grid triple">
      <div class="figure"><h4>Before projection</h4><canvas id="heat-before" width="240" height="240" data-exportable="true"></canvas><small>Divergence field before correction.</small></div>
      <div class="figure"><h4>After exact projection</h4><canvas id="heat-exact" width="240" height="240"></canvas><small>Exact periodic projection branch.</small></div>
      <div class="figure"><h4>GLM frame ${a.selectedFrame}</h4><canvas id="heat-glm" width="240" height="240"></canvas><small>Asymptotic reduction at the selected frame. The final frame remains available in the history chart and summary below.</small></div>
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure" data-exportable="true">
        <h4>GLM divergence history</h4>
        ${lineChartSvg(a.glmHistory.map((value, index) => ({ x: index, y: value })), 'Step', 'L2 divergence', a.selectedFrame)}
        <small>GLM reduces the constraint violation, but the exact projector removes it much more sharply.</small>
      </div>
      <div class="figure">
        <h4>Norm comparison</h4>
        <div class="value-grid">
          <div><small>Before</small><code>${a.beforeNorm.toExponential(3)}</code></div>
          <div><small>After exact projection</small><code>${a.afterExactNorm.toExponential(3)}</code></div>
          <div><small>Selected GLM frame</small><code>${a.selectedGlmNorm.toExponential(3)}</code></div>
          <div><small>Final GLM frame</small><code>${a.afterGlmNorm.toExponential(3)}</code></div>
          <div><small>Exact improvement factor</small><code>${formatFactor(a.exactImprovementFactor)}</code></div>
          <div><small>Current frame</small><code>${a.selectedFrame} / ${state.labs.mhd.glmSteps}</code></div>
        </div>
      </div>
    </div>
  `;
}

function renderGaugeStage() {
  const a = latestAnalysis;
  return `
    <div class="figure-grid triple">
      <div class="figure"><h4>Before transverse projection</h4><canvas id="gauge-before" width="240" height="240" data-exportable="true"></canvas><small>Longitudinal contamination before correction.</small></div>
      <div class="figure"><h4>After exact transverse projection</h4><canvas id="gauge-exact" width="240" height="240"></canvas><small>Exact projection-compatible branch.</small></div>
      <div class="figure"><h4>Damping frame ${a.selectedFrame}</h4><canvas id="gauge-glm" width="240" height="240"></canvas><small>Asymptotic cleanup at the selected frame. This branch is intentionally slower than the exact projection branch.</small></div>
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure" data-exportable="true">
        <h4>Longitudinal-mode history</h4>
        ${lineChartSvg(a.glmHistory.map((value, index) => ({ x: index, y: value })), 'Step', 'Residual longitudinal norm', a.selectedFrame)}
        <small>The exact projector is what gives the clean physics fit here; damping is only a secondary comparator.</small>
      </div>
      <div class="figure">
        <h4>Physics reading</h4>
        <div class="value-grid">
          <div><small>Before</small><code>${a.beforeGaugeNorm.toExponential(3)}</code></div>
          <div><small>After exact projection</small><code>${a.afterExactGaugeNorm.toExponential(3)}</code></div>
          <div><small>Selected damping frame</small><code>${a.selectedGlmNorm.toExponential(3)}</code></div>
          <div><small>Final damping frame</small><code>${a.afterGlmGaugeNorm.toExponential(3)}</code></div>
          <div><small>Interpretation</small><code>Transverse part recovered exactly on the compatible projection branch.</code></div>
          <div><small>Current frame</small><code>${a.selectedFrame} / ${state.labs.gauge.glmSteps}</code></div>
        </div>
      </div>
    </div>
  `;
}

function renderCfdStage() {
  return `
    <div class="figure-grid double">
      <div class="figure"><h4>Periodic branch before projection</h4><canvas id="cfd-periodic-before" width="240" height="240" data-exportable="true"></canvas><small>Divergence of the contaminated velocity field on the periodic branch.</small></div>
      <div class="figure"><h4>Periodic branch after projection</h4><canvas id="cfd-periodic-after" width="240" height="240"></canvas><small>Exact incompressible projection recovers the protected velocity component.</small></div>
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure"><h4>Bounded-domain before transplant</h4><canvas id="cfd-bounded-before" width="240" height="240"></canvas><small>The bounded-domain field carries divergence contamination before the periodic projector is misapplied.</small></div>
      <div class="figure"><h4>Bounded-domain after periodic transplant</h4><canvas id="cfd-bounded-after" width="240" height="240"></canvas><small>Divergence is reduced, but the bounded protected class still fails because the boundary-normal trace is wrong.</small></div>
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure">
        <h4>Periodic exactness check</h4>
        <div class="value-grid">
          <div><small>Before divergence</small><code>${latestAnalysis.periodicBeforeNorm.toExponential(3)}</code></div>
          <div><small>After projection</small><code>${latestAnalysis.periodicAfterNorm.toExponential(3)}</code></div>
          <div><small>Recovery error</small><code>${latestAnalysis.periodicRecoveryError.toExponential(3)}</code></div>
          <div><small>Idempotence error</small><code>${latestAnalysis.periodicIdempotenceError.toExponential(3)}</code></div>
        </div>
      </div>
      <div class="figure">
        <h4>Bounded-domain limitation check</h4>
        <div class="value-grid">
          <div><small>Physical boundary-normal RMS</small><code>${latestAnalysis.boundedPhysicalBoundaryNormalRms.toExponential(3)}</code></div>
          <div><small>Projected boundary-normal RMS</small><code>${latestAnalysis.boundedProjectedBoundaryNormalRms.toExponential(3)}</code></div>
          <div><small>Compatible protected boundary-normal RMS</small><code>${latestAnalysis.boundedCompatibleProtectedBoundaryNormalRms.toExponential(3)}</code></div>
          <div><small>Compatible recovered boundary-normal RMS</small><code>${latestAnalysis.boundedCompatibleRecoveredBoundaryNormalRms.toExponential(3)}</code></div>
          <div><small>Compatible recovery error</small><code>${latestAnalysis.boundedCompatibleRecoveryError.toExponential(3)}</code></div>
          <div><small>Compatible projector agreement</small><code>${latestAnalysis.boundedCompatibleProjectorConstructionAgreement?.toExponential(3) ?? 'n/a'}</code></div>
          <div><small>Divergence-only witness 1</small><code>${latestAnalysis.divergenceOnlyWitness.firstStateDivergenceRms.toExponential(3)}</code></div>
          <div><small>Divergence-only witness separation</small><code>${latestAnalysis.divergenceOnlyWitness.stateSeparationRms.toExponential(3)}</code></div>
        </div>
      </div>
    </div>
    <div class="figure-grid double top-gap">
      <div class="figure">
        <h4>Restricted exact bounded-domain subcase</h4>
        <div class="value-grid">
          <div><small>Protected divergence RMS</small><code>${latestAnalysis.boundedCompatibleProtectedDivNorm.toExponential(3)}</code></div>
          <div><small>Recovered divergence RMS</small><code>${latestAnalysis.boundedCompatibleRecoveredDivNorm.toExponential(3)}</code></div>
          <div><small>Orthogonality residual</small><code>${latestAnalysis.boundedCompatibleOrthogonalityResidual.toExponential(3)}</code></div>
          <div><small>Idempotence error</small><code>${latestAnalysis.boundedCompatibleIdempotenceError.toExponential(3)}</code></div>
        </div>
      </div>
      <div class="figure">
        <h4>Interpretation</h4>
        <p class="studio-note">The CFD lane now shows both sides honestly: the periodic branch is exact, the periodic-transplant bounded branch fails, and the restricted boundary-compatible finite-mode Hodge family gives a real bounded exact subcase instead of a vague rescue claim.</p>
      </div>
    </div>
  `;
}

function renderContinuousStage() {
  const a = latestAnalysis;
  return `
    <div class="figure-grid double">
      <div class="figure" data-exportable="true">
        <h4>Disturbance norm over time</h4>
        ${lineChartSvg(a.disturbanceNorms.map((value, index) => ({ x: index, y: value })), 'Step', '||P_D x||', a.selectedFrame)}
        <small>Decay alone is not enough. The protected component must also stay fixed.</small>
      </div>
      <div class="figure">
        <h4>Selected flow state</h4>
        <div class="value-grid">
          <div><small>ker(K) basis</small><code>${a.kernelBasis.length ? a.kernelBasis.map((row) => formatVector(row)).join('\n') : '[]'}</code></div>
          <div><small>Disturbance complement</small><code>${a.disturbanceBasis.length ? a.disturbanceBasis.map((row) => formatVector(row)).join('\n') : '[]'}</code></div>
          <div><small>Selected time</small><code>${a.selectedTime.toFixed(3)}</code></div>
          <div><small>Selected state</small><code>${formatVector(a.selectedState)}</code></div>
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
        ${Object.entries(a.details)
          .map(
            ([key, value]) =>
              `<div><small>${key}</small><code>${typeof value === 'object' ? JSON.stringify(value, null, 2) : String(value)}</code></div>`
          )
          .join('')}
      </div>
    </div>
  `;
}

function renderMetrics() {
  switch (state.activeLab) {
    case 'mixer':
      return [
        metric('Status', latestAnalysis.status, latestAnalysis.exact ? 'good' : latestAnalysis.impossible || latestAnalysis.unsupported ? 'bad' : ''),
        metric('Family', latestAnalysis.familyLabel ?? latestAnalysis.family),
        metric('Evidence', latestAnalysis.theoremStatus ?? 'mixed'),
        metric('Diagnostics', String(latestAnalysis.diagnostics?.length ?? 0), latestAnalysis.diagnostics?.some((item) => item.severity === 'error') ? 'bad' : 'good'),
        metric('Recommendations', String(latestAnalysis.recommendations?.length ?? 0), latestAnalysis.recommendations?.length ? 'good' : ''),
        ...(latestAnalysis.rawDetails?.collisionGap !== undefined
          ? [metric('Collision gap', Number(latestAnalysis.rawDetails.collisionGap).toExponential(2), Number(latestAnalysis.rawDetails.collisionGap) < 1e-8 ? 'good' : 'bad')]
          : []),
        ...(latestAnalysis.rawDetails?.kappa0 !== undefined
          ? [metric('κ(0)', Number(latestAnalysis.rawDetails.kappa0).toExponential(2), Number(latestAnalysis.rawDetails.kappa0) < 1e-8 ? 'good' : 'bad')]
          : []),
        ...(latestAnalysis.rawDetails?.predictedMinCutoff !== undefined
          ? [metric('Min cutoff', latestAnalysis.rawDetails.predictedMinCutoff < 0 ? 'none' : String(latestAnalysis.rawDetails.predictedMinCutoff), latestAnalysis.exact ? 'good' : '')]
          : []),
        ...(latestAnalysis.rawDetails?.predictedMinHorizon !== undefined
          ? [metric('Min horizon', latestAnalysis.rawDetails.predictedMinHorizon < 0 || latestAnalysis.rawDetails.predictedMinHorizon === null ? 'none' : String(latestAnalysis.rawDetails.predictedMinHorizon), latestAnalysis.exact ? 'good' : '')]
          : []),
      ].join('');
    case 'recoverability':
      return [
        metric('Status', latestAnalysis.status, latestAnalysis.exact || latestAnalysis.asymptotic ? 'good' : latestAnalysis.impossible ? 'bad' : ''),
        metric('κ(0)', latestAnalysis.kappa0.toExponential(2), latestAnalysis.kappa0 < 1e-8 ? 'good' : 'bad'),
        metric('κ(0)/2 bound', (0.5 * latestAnalysis.kappa0).toExponential(2), latestAnalysis.kappa0 < 1e-8 ? 'good' : 'bad'),
        metric('Selected κ(δ)', latestAnalysis.selectedKappa.toExponential(2), latestAnalysis.selectedKappa < 1e-6 ? 'good' : ''),
        metric('Exact', latestAnalysis.exact ? 'yes' : 'no', latestAnalysis.exact ? 'good' : ''),
        metric('Asymptotic', latestAnalysis.asymptotic ? 'yes' : 'no', latestAnalysis.asymptotic ? 'good' : ''),
        ...(state.labs.recoverability.system === 'analytic'
          ? [metric('κ(η)/2 bound', latestAnalysis.selectedLowerBound.toExponential(2), latestAnalysis.selectedLowerBound > 0 ? 'bad' : 'good')]
          : []),
        ...(state.labs.recoverability.system === 'periodic'
          ? [metric('Min cutoff', String(latestAnalysis.predictedMinCutoff ?? 'n/a'), latestAnalysis.exact ? 'good' : '')]
          : []),
        ...(state.labs.recoverability.system === 'control'
          ? [metric('Min horizon', String(latestAnalysis.predictedMinHorizon ?? 'none'), latestAnalysis.exact || latestAnalysis.asymptotic ? 'good' : '')]
          : []),
        ...(state.labs.recoverability.system === 'linear'
          ? [
              metric('Active measurements', String(latestAnalysis.activeMeasurementLabels.length), latestAnalysis.exact ? 'good' : ''),
              metric('Minimal fix size', latestAnalysis.minimalAddedMeasurements === null ? 'none' : String(latestAnalysis.minimalAddedMeasurements), latestAnalysis.minimalAddedMeasurements !== null ? 'good' : 'bad'),
            ]
          : []),
        ...(state.labs.recoverability.system === 'boundary'
          ? [
              metric('Boundary mismatch', latestAnalysis.transplantBoundaryMismatch.toExponential(2), latestAnalysis.boundaryArchitecture === 'boundary_compatible_hodge' ? 'good' : 'bad'),
              metric('Compatible recovery', latestAnalysis.compatibleRecoveryError.toExponential(2), latestAnalysis.compatibleRecoveryError < 1e-6 ? 'good' : ''),
            ]
          : []),
      ].join('');
    case 'benchmark':
      return [
        metric('Demos', String(latestAnalysis.summary.demoCount), 'good'),
        metric('Regime changes', String(latestAnalysis.summary.regimeChangeCount), latestAnalysis.summary.regimeChangeCount === latestAnalysis.summary.demoCount ? 'good' : ''),
        metric('Exact after fix', String(latestAnalysis.summary.exactAfterCount), 'good'),
        metric('Benchmarked modules', String(latestAnalysis.summary.moduleCount), 'good'),
      ].join('');
    case 'exact':
      return [
        metric('Basis overlap', latestAnalysis.overlap.toFixed(3), latestAnalysis.admissible ? 'good' : 'bad'),
        metric('Recovery error', latestAnalysis.exactError.toExponential(2), latestAnalysis.exactError < 1e-8 ? 'good' : 'bad'),
        metric('Branch', latestAnalysis.admissible ? 'Exact theorem' : 'No-go case'),
      ].join('');
    case 'qec':
      return [
        metric('Selected sector', latestAnalysis.selectedLabel),
        metric('Recovery error', latestAnalysis.recoveryError.toExponential(2), latestAnalysis.recoveryError < 1e-9 ? 'good' : 'bad'),
        metric('Off-sector overlap', Math.max(...latestAnalysis.sectorOverlap.flat().filter((value) => value < 1)).toExponential(2), 'good'),
      ].join('');
    case 'mhd':
      return [
        metric('Before', latestAnalysis.beforeNorm.toExponential(2)),
        metric('After exact', latestAnalysis.afterExactNorm.toExponential(2), 'good'),
        metric(`GLM frame ${latestAnalysis.selectedFrame}`, latestAnalysis.selectedGlmNorm.toExponential(2), latestAnalysis.selectedGlmNorm < latestAnalysis.beforeNorm ? 'good' : 'bad'),
        metric('Reading', latestAnalysis.afterExactNorm < latestAnalysis.selectedGlmNorm ? 'Exact branch wins' : 'Recheck example', latestAnalysis.afterExactNorm < latestAnalysis.selectedGlmNorm ? 'good' : 'bad'),
      ].join('');
    case 'cfd':
      return [
        metric('Periodic after projection', latestAnalysis.periodicAfterNorm.toExponential(2), 'good'),
        metric('Periodic recovery error', latestAnalysis.periodicRecoveryError.toExponential(2), latestAnalysis.periodicRecoveryError < 1e-8 ? 'good' : 'bad'),
        metric('Bounded boundary mismatch', latestAnalysis.boundedProjectedBoundaryNormalRms.toExponential(2), latestAnalysis.boundedTransplantFails ? 'bad' : 'good'),
        metric('Verdict', latestAnalysis.boundedTransplantFails ? 'Narrow CFD fit only' : 'Recheck bounded example', latestAnalysis.boundedTransplantFails ? 'good' : 'bad'),
      ].join('');
    case 'gauge':
      return [
        metric('Before', latestAnalysis.beforeGaugeNorm.toExponential(2)),
        metric('After exact', latestAnalysis.afterExactGaugeNorm.toExponential(2), 'good'),
        metric(`Frame ${latestAnalysis.selectedFrame}`, latestAnalysis.selectedGlmNorm.toExponential(2), latestAnalysis.selectedGlmNorm < latestAnalysis.beforeGaugeNorm ? 'good' : 'bad'),
        metric('Verdict', 'Exact physics extension', 'good'),
      ].join('');
    case 'continuous':
      return [
        metric('Selected time', latestAnalysis.selectedTime.toFixed(2)),
        metric('Protected drift', latestAnalysis.protectedDrift.toExponential(2), latestAnalysis.protectedDrift < 1e-4 ? 'good' : 'bad'),
        metric('Mixing norm', latestAnalysis.mixingNorm.toExponential(2), latestAnalysis.mixingNorm < 1e-6 ? 'good' : 'bad'),
        metric('Finite-time exact recovery', latestAnalysis.finiteTimeExactRecoveryPossible ? 'Apparent yes' : 'No', latestAnalysis.finiteTimeExactRecoveryPossible ? 'bad' : 'good'),
      ].join('');
    case 'nogo':
    default:
      return [metric('Status', latestAnalysis.status, 'bad'), metric('Scope', 'Structural boundary')].join('');
  }
}

function renderNarrativeSummary() {
  switch (state.activeLab) {
    case 'mixer':
      return `<p>${latestAnalysis.status}. The mixer reduced the current composition to the ${latestAnalysis.familyLabel ?? latestAnalysis.family} and returned a ${latestAnalysis.theoremStatus ?? 'mixed-evidence'} verdict. Protected target: ${latestAnalysis.protectedLabel}. Current record or architecture: ${latestAnalysis.observationLabel}. Root cause: ${latestAnalysis.rootCause} Missing structure: ${latestAnalysis.missingStructure}${latestAnalysis.comparison ? ` The leading before/after witness is ${latestAnalysis.comparison.keyMetricName}, moving from ${formatDisplayValue(latestAnalysis.comparison.keyMetricBefore)} to ${formatDisplayValue(latestAnalysis.comparison.keyMetricAfter)} when the promoted fix is applied.` : ''}${latestAnalysis.generatedConfig ? ' This view was produced by a seeded constrained search, so the generated case can be replayed exactly.' : ''} This lab is intentionally typed and bounded: unsupported inputs are rejected rather than silently approximated.</p>`;
    case 'recoverability':
      return `<p>${latestAnalysis.classification}. The current system is ${latestAnalysis.systemLabel}, the protected variable is ${latestAnalysis.protectedLabel}, and the chosen record map is ${latestAnalysis.observationLabel}. At the selected tolerance δ = ${latestAnalysis.selectedDelta.toFixed(2)}, the collapse value is ${latestAnalysis.selectedKappa.toExponential(2)} and the zero-noise lower bound from κ(0) is ${(0.5 * latestAnalysis.kappa0).toExponential(2)}. Recommended architecture: ${latestAnalysis.guidance.architecture}. ${latestAnalysis.guidance.missing}${state.labs.recoverability.system === 'analytic' ? ` Under adversarial record noise of the same size, the current lower bound on worst-case protected-variable error is ${latestAnalysis.selectedLowerBound.toExponential(2)}.` : ''}${state.labs.recoverability.system === 'periodic' ? ` The current cutoff is ${latestAnalysis.currentCutoff}, and the predicted minimum cutoff for the chosen protected functional is ${latestAnalysis.predictedMinCutoff}; in this lane the threshold is set by the largest protected visible cutoff, not by raw support size.` : ''}${state.labs.recoverability.system === 'control' ? ` The current horizon is ${state.labs.recoverability.controlHorizon}.${state.labs.recoverability.controlMode === 'diagonal_threshold' ? ` In the diagonal threshold model, the predicted minimum exact-history length is ${latestAnalysis.predictedMinHorizon === null ? 'none because the protected functional is not generated by the sensed moment family' : latestAnalysis.predictedMinHorizon}, and the threshold is governed by interpolation complexity on the active sensor spectrum rather than by support count alone.` : ' In the two-state observer model, the first exact finite-history threshold stays at horizon 2 when ε is nonzero.'}` : ''}${state.labs.recoverability.system === 'linear' ? ` The current static record uses ${latestAnalysis.activeMeasurementLabels.length} measurement rows. The unrestricted theorem-backed minimum added-measurement count is ${latestAnalysis.unrestrictedMinimalAddedMeasurements}.${latestAnalysis.minimalAddedMeasurements === null ? ' No exact fix exists inside the current candidate library.' : ` Inside the current library, the smallest exact fix needs ${latestAnalysis.minimalAddedMeasurements} added measurement${latestAnalysis.minimalAddedMeasurements === 1 ? '' : 's'}.`}` : ''}${state.labs.recoverability.system === 'boundary' ? ` The transplanted periodic projector leaves a bounded-domain boundary mismatch of ${latestAnalysis.transplantBoundaryMismatch.toExponential(2)}, while the restricted boundary-compatible finite-mode Hodge family reaches recovery error ${latestAnalysis.compatibleRecoveryError.toExponential(2)} on its admissible family.` : ''} This studio is meant to tell you what can be recovered, what is blocked, and what to change next.</p>`;
    case 'benchmark':
      return `<p>The console currently tracks ${latestAnalysis.summary.demoCount} validated repair demos and ${latestAnalysis.summary.moduleCount} benchmarked module surfaces. The selected demo is ${latestAnalysis.selectedDemoRow.label}, which moves from ${latestAnalysis.selectedDemoRow.beforeRegime} to ${latestAnalysis.selectedDemoRow.afterRegime} after applying ${latestAnalysis.selectedDemoRow.fixTitle}. Use this surface when you need a reproducible starting point, an exportable evidence snapshot, or a quick sanity check that the workbench is still telling one consistent story.</p>`;
    case 'exact':
      return `<p>${latestAnalysis.admissible ? 'The disturbance is orthogonal, so projection returns the protected component exactly.' : 'The disturbance overlaps the protected direction, so exact recovery fails in the way the theorem spine predicts.'}</p>`;
    case 'qec':
      return `<p>The selected sector ${latestAnalysis.selectedLabel} is recovered with error ${latestAnalysis.recoveryError.toExponential(2)}. In this branch, exactness comes from sector distinguishability rather than one global projector on the entire physical Hilbert space.</p>`;
    case 'mhd':
      return `<p>Projection drops the divergence norm from ${latestAnalysis.beforeNorm.toExponential(2)} to ${latestAnalysis.afterExactNorm.toExponential(2)}. At the currently selected GLM frame ${latestAnalysis.selectedFrame}, the asymptotic branch sits at ${latestAnalysis.selectedGlmNorm.toExponential(2)} and only reaches ${latestAnalysis.afterGlmNorm.toExponential(2)} at the final frame. This is the exact-versus-asymptotic split in numerical form.</p>`;
    case 'cfd':
      return `<p>The periodic incompressible projection drops the divergence norm from ${latestAnalysis.periodicBeforeNorm.toExponential(2)} to ${latestAnalysis.periodicAfterNorm.toExponential(2)} with recovery error ${latestAnalysis.periodicRecoveryError.toExponential(2)}. The bounded-domain transplant still leaves a boundary-normal mismatch of ${latestAnalysis.boundedProjectedBoundaryNormalRms.toExponential(2)}, while the restricted boundary-compatible finite-mode Hodge family reaches recovery error ${latestAnalysis.boundedCompatibleRecoveryError.toExponential(2)}. That is the honest CFD picture: one real exact periodic branch, one real bounded exact subcase, and one sharp bounded failure.</p>`;
    case 'gauge':
      return `<p>The exact transverse projection drops the longitudinal residual from ${latestAnalysis.beforeGaugeNorm.toExponential(2)} to ${latestAnalysis.afterExactGaugeNorm.toExponential(2)}. At the currently selected damping frame ${latestAnalysis.selectedFrame}, the comparator branch sits at ${latestAnalysis.selectedGlmNorm.toExponential(2)}. This bridge is kept because it uses a real operator, not just an analogy.</p>`;
    case 'continuous':
      return `<p>At the selected time ${latestAnalysis.selectedTime.toFixed(2)}, the flow state is ${formatVector(latestAnalysis.selectedState)}. The full generator still produces protected drift ${latestAnalysis.protectedDrift.toExponential(2)} and mixing norm ${latestAnalysis.mixingNorm.toExponential(2)}, so finite-time exact recovery remains ${latestAnalysis.finiteTimeExactRecoveryPossible ? 'apparently possible' : 'ruled out'} for this smooth flow model.</p>`;
    case 'nogo':
    default:
      return `<p>${latestAnalysis.summary}</p>`;
  }
}

function formatFactor(value) {
  return value >= 1e4 ? `${value.toExponential(2)}×` : `${value.toFixed(1)}×`;
}

function metric(label, value, tone = '') {
  return `<article class="metric-card card-surface ${tone}"><strong>${value}</strong><span>${label}</span></article>`;
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
    const eventName = input.tagName === 'SELECT' || input.type === 'checkbox' ? 'change' : 'input';
    input.addEventListener(eventName, () => {
      const value = input.type === 'checkbox' ? input.checked : input.value;
      updateStatePath(input.dataset.path, value);
    });
  });

  document.querySelectorAll('[data-structural-demo]').forEach((button) => {
    button.addEventListener('click', () => applyStructuralPreset(button.dataset.structuralDemo));
  });

  document.querySelectorAll('[data-quickstart]').forEach((button) => {
    button.addEventListener('click', () => applyQuickStart(button.dataset.quickstart));
  });

  document.querySelectorAll('[data-open-demo]').forEach((button) => {
    button.addEventListener('click', () => applyStructuralPreset(button.dataset.openDemo));
  });

  document.querySelectorAll('[data-mixer-demo]').forEach((button) => {
    button.addEventListener('click', () => applyMixerDemo(button.dataset.mixerDemo));
  });

  document.querySelectorAll('[data-apply-recommendation]').forEach((button) => {
    button.addEventListener('click', () => applyStructuralRecommendation(button.dataset.applyRecommendation));
  });

  document.querySelectorAll('[data-apply-mixer-recommendation]').forEach((button) => {
    button.addEventListener('click', () => applyMixerRecommendation(button.dataset.applyMixerRecommendation));
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
  document.getElementById('export-csv').addEventListener('click', exportCsv);
  document.getElementById('export-report').addEventListener('click', exportReport);
  document.getElementById('export-figure').addEventListener('click', exportFigure);
  document.getElementById('reset-current').addEventListener('click', resetCurrentLab);
  document.getElementById('reset-all').addEventListener('click', resetAllLabs);

  const resetCurrentView = document.getElementById('reset-current-view');
  if (resetCurrentView) {
    resetCurrentView.addEventListener('click', resetCurrentLab);
  }

  const playbackToggle = document.getElementById('playback-toggle');
  if (playbackToggle) {
    playbackToggle.addEventListener('click', togglePlayback);
  }

  const resetPlayback = document.getElementById('reset-playback-view');
  if (resetPlayback) {
    resetPlayback.addEventListener('click', resetPlaybackView);
  }

  document.querySelectorAll('[data-playback-step]').forEach((button) => {
    button.addEventListener('click', () => stepPlayback(Number(button.dataset.playbackStep)));
  });
}

function updateStatePath(path, rawValue) {
  const value = typeof rawValue === 'boolean' || Number.isNaN(Number(rawValue)) || rawValue === '' ? rawValue : Number(rawValue);
  setStatePath(path, value);
  render();
}

function saveScenario() {
  const name = window.prompt('Save current scenario as:', `${LAB_META[state.activeLab].label} ${new Date().toLocaleString()}`);
  if (!name) return;
  store.saveScenario(name);
  syncViewState();
  render();
}

function loadScenarioFromSelect() {
  const select = document.getElementById('saved-scenarios');
  if (!select.value || !savedScenarios[select.value]) return;
  store.loadScenario(select.value);
  syncViewState();
  render();
}

async function copyShareLink() {
  const url = `${window.location.origin}${window.location.pathname}#state=${store.getShareState()}`;
  try {
    await navigator.clipboard.writeText(url);
  } catch {
    window.prompt('Copy this share link:', url);
  }
}

function exportJson() {
  const payload = exportScenarioPayload(state, latestAnalysis);
  downloadText(`protected-state-correction-${state.activeLab}-scenario.json`, JSON.stringify(payload, null, 2), 'application/json');
}

function exportCsv() {
  const csv = exportScenarioCsv(state, latestAnalysis);
  if (!csv) {
    window.alert('CSV export is not available for the current module.');
    return;
  }
  downloadText(`protected-state-correction-${state.activeLab}-series.csv`, csv, 'text/csv');
}

function exportReport() {
  const report = exportScenarioReport(state, latestAnalysis);
  downloadText(`protected-state-correction-${state.activeLab}-report.md`, report, 'text/markdown');
}

function exportFigure() {
  const exportable = document.querySelector('[data-exportable="true"] canvas, [data-exportable="true"] svg') || document.querySelector('canvas, svg');
  if (!exportable) return;
  if (exportable.tagName.toLowerCase() === 'canvas') {
    const link = document.createElement('a');
    link.download = `protected-state-correction-${state.activeLab}-figure.png`;
    link.href = exportable.toDataURL('image/png');
    link.click();
    return;
  }
  const serializer = new XMLSerializer();
  const source = serializer.serializeToString(exportable);
  const blob = new Blob([source], { type: 'image/svg+xml;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.download = `protected-state-correction-${state.activeLab}-figure.svg`;
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
    drawHeatmap(document.getElementById('heat-before'), latestAnalysis.beforeDiv);
    drawHeatmap(document.getElementById('heat-exact'), latestAnalysis.afterExactDiv);
    drawHeatmap(document.getElementById('heat-glm'), latestAnalysis.selectedGlmDiv);
  }
  if (state.activeLab === 'cfd') {
    drawHeatmap(document.getElementById('cfd-periodic-before'), latestAnalysis.periodicBeforeDiv);
    drawHeatmap(document.getElementById('cfd-periodic-after'), latestAnalysis.periodicAfterDiv);
    drawHeatmap(document.getElementById('cfd-bounded-before'), latestAnalysis.boundedBeforeDiv);
    drawHeatmap(document.getElementById('cfd-bounded-after'), latestAnalysis.boundedAfterDiv);
  }
  if (state.activeLab === 'gauge') {
    drawHeatmap(document.getElementById('gauge-before'), latestAnalysis.beforeDiv);
    drawHeatmap(document.getElementById('gauge-exact'), latestAnalysis.afterExactDiv);
    drawHeatmap(document.getElementById('gauge-glm'), latestAnalysis.selectedGlmDiv);
  }
  if (state.activeLab === 'qec') {
    const mount = document.getElementById('qec-overlap-table');
    if (mount) mount.innerHTML = matrixTable(latestAnalysis.sectorOverlap, latestAnalysis.sectorLabels);
  }
}

render();
window.addEventListener('hashchange', () => {
  const updated = store.hydrateFromHash(window.location.hash);
  if (updated) {
    syncViewState();
    render();
  }
});
