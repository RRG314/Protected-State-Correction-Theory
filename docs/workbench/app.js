import {
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
  DEFAULT_STATE,
  STORAGE_KEY,
  cloneState,
  decodeShareState,
  encodeShareState,
  exportScenarioPayload,
  sanitizeState,
} from './lib/state.js';

const LAB_META = {
  recoverability: {
    label: 'Recoverability / Correction Studio',
    short: 'Decide what is recoverable, what is blocked, and what to add next.',
    branch: 'Constrained-observation branch',
    fit: 'Exact / approximate / asymptotic / impossible classification',
    status: 'ACTIVE RESEARCH BRANCH',
    lane: 'Observation and reconstruction',
    protected: 'Chosen protected variable p(x)',
    disturbance: 'Unseen ambiguity inside the observation fibers',
    correction: 'Recovery map R after constrained observation M',
    plain:
      'This studio turns the recoverability branch into a decision tool. It asks what you want to preserve, what record you actually have, whether recovery is exact, approximate, asymptotic, or impossible, and what you should change next.',
    technical:
      'Implements the constrained-observation recoverability branch as a design studio. The module computes finite-sample collapse curves κ(δ), fiber-collision boundaries, restricted-linear sufficiency diagnostics, minimal augmentation suggestions, and system-specific recovery behavior for analytic, quantum, periodic-flow, control-observer, and reusable linear-template examples.',
    use: 'Use this when you want to decide whether a record is sufficient, what weaker variable is still recoverable, what extra measurements would fix the problem, and which recovery architecture fits best.',
    avoid: 'Do not treat loss of recoverability as a metaphysical statement. This branch is about operator-level information access and reconstruction limits.',
    refs: [
      { title: 'Branch overview', href: '../theory/advanced-directions/constrained-observation-recoverability.md', note: 'Design scope and falsification target' },
      { title: 'Formalism', href: '../theory/advanced-directions/constrained-observation-formalism.md', note: 'Definitions, propositions, and theorem candidates' },
      { title: 'Results report', href: '../theory/advanced-directions/constrained-observation-results-report.md', note: 'Experiments, outputs, and assessment' },
      { title: 'Studio workflow', href: '../app/recoverability-correction-studio.md', note: 'User-facing design path' },
    ],
    literature: [
      { title: 'Jenčová-Petz on quantum sufficiency', href: 'https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-263/issue-1/Sufficiency-in-quantum-statistical-inference/cmp/1143668799.full', note: 'Quantum recoverability anchor' },
      { title: 'Functional observability and subspace reconstruction', href: 'https://doi.org/10.1103/PhysRevResearch.4.043195', note: 'Control-side protected-functional anchor' },
      { title: 'Chorin projection-method foundation', href: 'https://doi.org/10.1090/S0025-5718-1968-0242392-2', note: 'Periodic constrained reconstruction anchor' },
    ],
  },
  exact: {
    label: 'Exact Projection Lab',
    short: 'Orthogonal exact recovery and overlap failure.',
    branch: 'Exact branch',
    fit: 'Exact fit',
    status: 'PROVED / NO-GO',
    lane: 'Finite-dimensional anchor',
    protected: 'Protected subspace S',
    disturbance: 'Orthogonal disturbance direction D',
    correction: 'Orthogonal projector P_S',
    plain:
      'This is the smallest exact correction model in the repo. When the disturbance is truly orthogonal to the protected direction, projection recovers the protected component exactly. When overlap is introduced, the same operator becomes a clean counterexample.',
    technical:
      'Implements the finite-dimensional direct-sum model H = S ⊕ D with recovery R = P_S. The angle control lets the example move outside the admissible OCP hypotheses and turns the module into a witness for OCP-T1 versus OCP-N1.',
    use: 'Use this to understand the clean exact theorem and the sharp overlap failure in the simplest possible setting.',
    avoid: 'Do not treat non-orthogonal cases as exact protected-state correction systems.',
    refs: [
      { title: 'Central theorem', href: '../theorem-candidates/central-theorem.md', note: 'Exact projector recovery' },
      { title: 'No-go spine', href: '../impossibility-results/no-go-results.md', note: 'Overlap / indistinguishability no-go' },
      { title: 'Operator spine', href: '../finalization/operator-spine-final.md', note: 'Projector-based correction language' },
    ],
    literature: [
      { title: 'Chorin projection-method anchor', href: 'https://doi.org/10.1090/S0025-5718-1968-0242392-2', note: 'Classical exact projection in PDE settings' },
    ],
  },
  qec: {
    label: 'QEC Sector Lab',
    short: '3-qubit bit-flip code in exact sector language.',
    branch: 'Exact sector branch',
    fit: 'Exact fit / standard-anchor reinterpretation',
    status: 'PROVED / CONDITIONAL ANCHOR',
    lane: 'Quantum information anchor',
    protected: 'Code space / logical state',
    disturbance: 'Correctable syndrome sectors',
    correction: 'Sector projectors and recovery family',
    plain:
      'This module treats QEC as the exact sector branch. The code space is what must be preserved, each bit-flip sector is a disturbance sector, and recovery works because the sectors stay distinguishable and can be mapped back without changing the logical information.',
    technical:
      'Implements the 3-qubit bit-flip sector model using orthogonal sector bases and a sector-conditioned recovery operator. The exact statement here is branch-specific: the repo is re-framing standard QEC structure, not replacing it.',
    use: 'Use this when you want the strongest exact anchor beyond the simple projector model.',
    avoid: 'Do not read this as a new QEC theorem. The value here is the protected-state correction framing.',
    refs: [
      { title: 'QEC in protected-state language', href: '../qec/qec-in-ocp.md', note: 'Protected space, sectors, and recovery' },
      { title: 'Sector recovery theorem', href: '../theorem-candidates/sector-recovery-theorems.md', note: 'Exact orthogonal sector recovery' },
      { title: 'QEC foundations', href: '../qec/qec-foundations.md', note: 'Knill-Laflamme and syndrome structure' },
    ],
    literature: [
      { title: 'Knill-Laflamme foundation', href: 'https://arxiv.org/abs/quant-ph/9604034', note: 'Foundational exact correction anchor' },
      { title: 'Continuous-QEC bridge', href: 'https://doi.org/10.1103/PhysRevA.65.042301', note: 'Useful next-step literature' },
    ],
  },
  mhd: {
    label: 'MHD Projection Lab',
    short: 'Exact periodic projection versus GLM damping.',
    branch: 'Exact and asymptotic comparison',
    fit: 'Exact fit + asymptotic comparator',
    status: 'PROVED / CONDITIONAL',
    lane: 'Fluid / MHD physics',
    protected: 'Divergence-free field component',
    disturbance: 'Gradient contamination / divergence error',
    correction: 'Helmholtz/Leray projector versus GLM cleaning',
    plain:
      'This module is the clearest continuous-system split in the repo. Exact projection removes the divergence-producing component in one shot for the periodic model, while GLM only reduces it gradually.',
    technical:
      'Builds a periodic field B = B_phys + grad(phi), applies the exact discrete Helmholtz-style projector, and compares it to a short GLM evolution. The exact branch is projection-based; the GLM branch is asymptotic and should not be promoted as exact.',
    use: 'Use this when you want the cleanest continuous exact-versus-asymptotic comparison.',
    avoid: 'Do not read the GLM side as an exact projector or assume the periodic result automatically extends to bounded domains.',
    refs: [
      { title: 'Divergence cleaning in protected-state language', href: '../mhd/divergence-cleaning-in-ocp.md', note: 'Exact Leray / Helmholtz anchor' },
      { title: 'GLM and asymptotic correction', href: '../mhd/glm-and-asymptotic-correction.md', note: 'Asymptotic branch and limits' },
      { title: 'Exact vs asymptotic split', href: '../formalism/exact-vs-asymptotic.md', note: 'Why the distinction matters' },
    ],
    literature: [
      { title: 'Dedner et al. on hyperbolic divergence cleaning', href: 'https://doi.org/10.1006/jcph.2001.6961', note: 'Asymptotic cleaning anchor' },
      { title: 'Evans-Hawley constrained transport', href: 'https://www.sciencedirect.com/science/article/pii/0021999188901209', note: 'Constraint-preserving MHD direction' },
    ],
  },
  cfd: {
    label: 'CFD Projection Lab',
    short: 'Periodic incompressible projection and bounded-domain limits.',
    branch: 'CFD extension',
    fit: 'Exact fit on the periodic branch / conditional bounded-domain extension',
    status: 'KEPT CFD EXTENSION / NO-GO LIMIT',
    lane: 'Incompressible CFD',
    protected: 'Divergence-free velocity field',
    disturbance: 'Non-solenoidal velocity contamination',
    correction: 'Pressure projection / Helmholtz-Hodge projector',
    plain:
      'This module is the narrow CFD lane that genuinely fits the theory. On the periodic branch, projection recovers the divergence-free velocity exactly. On bounded domains, the same idea becomes conditional because boundary data are part of the protected object and naive projector reuse can fail.',
    technical:
      'Computes a periodic velocity decomposition u = u_df + grad(phi), applies the exact projector, and then compares that exact branch to a bounded-domain counterexample and a divergence-only no-go witness. The point is to separate real projector fits from boundary-insensitive overreach.',
    use: 'Use this to understand where incompressible projection methods genuinely fit the protected-state correction framework and where the fit becomes conditional or fails.',
    avoid: 'Do not read this as a theorem about all CFD solvers. It is a narrow statement about projection-compatible incompressible correction architectures.',
    refs: [
      { title: 'Incompressible projection in protected-state language', href: '../cfd/incompressible-projection.md', note: 'Main CFD entry point' },
      { title: 'Bounded versus periodic projection', href: '../cfd/bounded-vs-periodic-projection.md', note: 'Boundary-sensitive scope control' },
      { title: 'CFD projection results', href: '../theorem-candidates/cfd-projection-results.md', note: 'Corollary and no-go layer' },
    ],
    literature: [
      { title: 'Chorin projection-method foundation', href: 'https://doi.org/10.1090/S0025-5718-1968-0242392-2', note: 'Classical incompressible projection anchor' },
      { title: 'Brown-Cortez-Minion on accurate projection methods', href: 'https://www.sciencedirect.com/science/article/pii/S0021999101967154', note: 'Boundary and pressure-correction context' },
      { title: 'Guermond-Minev-Shen overview', href: 'https://doi.org/10.1016/j.cma.2005.10.010', note: 'Broader projection-method literature' },
    ],
  },
  gauge: {
    label: 'Gauge Projection Lab',
    short: 'Transverse projection for Maxwell / Coulomb-gauge structure.',
    branch: 'Exact physics extension',
    fit: 'Exact fit on projection-compatible domains',
    status: 'KEPT PHYSICS EXTENSION',
    lane: 'Maxwell / gauge physics',
    protected: 'Transverse field or vector-potential component',
    disturbance: 'Longitudinal / pure-gradient component',
    correction: 'Transverse projector P_perp',
    plain:
      'This module shows the strongest additional physics bridge kept in the repo. It uses the same exact projector logic as the MHD periodic branch, but interprets the protected object as the transverse piece of a Maxwell-side field or vector potential.',
    technical:
      'Computationally this reuses the projection-compatible exact branch. The physics content is the Coulomb-gauge or transverse projection interpretation. It is a real operator-level fit, but not a new theorem beyond the existing exact projection spine.',
    use: 'Use this to see where the theory really reaches into additional physics without forcing a new universal claim.',
    avoid: 'Do not sell this as a new Maxwell theorem. It is a principled physics extension of the exact projector branch.',
    refs: [
      { title: 'Maxwell / Coulomb-gauge note', href: '../physics/maxwell-coulomb-gauge.md', note: 'Fit verdict and scope' },
      { title: 'Physics system matrix', href: '../physics/physics-system-matrix.md', note: 'Where this bridge sits' },
      { title: 'Kept vs rejected physics bridges', href: '../physics/kept-vs-rejected-physics-bridges.md', note: 'Why this one survives' },
    ],
    literature: [
      { title: 'Constraint-preserving Maxwell FEM', href: 'https://doi.org/10.1016/j.jcp.2019.109340', note: 'Operator-level Maxwell direction' },
      { title: 'Maxwell-case constraint remedy', href: 'https://arxiv.org/abs/gr-qc/0404036', note: 'Constraint-preserving evolution context' },
    ],
  },
  continuous: {
    label: 'Continuous Generator Lab',
    short: 'Invariant-split flows, spectral damping, and mixing failure.',
    branch: 'Asymptotic generator branch',
    fit: 'Asymptotic fit',
    status: 'PROVED / NO-GO',
    lane: 'Generator classification',
    protected: 'ker(K) or invariant protected coordinates',
    disturbance: 'Stable disturbance subspace',
    correction: 'Damping or invariant-split generator K',
    plain:
      'This module shows the strongest asymptotic theorem spine in the repo. Some generators preserve the protected coordinates and damp the disturbance coordinates. Others look stable overall but fail because they mix disturbance back into the protected part.',
    technical:
      'Computes the kernel-based protected space, an orthogonal disturbance complement, an RK4 flow path, the mixing norm ||P_S K P_D||, and the finite-time exact-recovery residual. This is where the theory draws the hard line between asymptotic correction and exact one-shot recovery.',
    use: 'Use this to test whether a linear correction generator actually qualifies as a protected-state correction flow.',
    avoid: 'Do not treat every dissipative matrix as a valid correction flow. Decay alone is not enough.',
    refs: [
      { title: 'Generator theorems', href: '../theorem-candidates/generator-theorems.md', note: 'Invariant-split and PSD results' },
      { title: 'Advanced no-go results', href: '../impossibility-results/advanced-no-go-results.md', note: 'Finite-time exact-recovery boundary' },
      { title: 'Worked linear example', href: '../control/worked-linear-example.md', note: 'Clean invariant-split control picture' },
    ],
    literature: [
      { title: 'Constraint damping in Z4 / harmonic gauge', href: 'https://arxiv.org/abs/gr-qc/0504114', note: 'Strong asymptotic physics lane' },
      { title: 'Continuous QEC / feedback', href: 'https://doi.org/10.1103/PhysRevA.65.042301', note: 'Potential future bridge' },
    ],
  },
  nogo: {
    label: 'No-Go Explorer',
    short: 'Failure modes the theory can actually rule out.',
    branch: 'No-go boundary layer',
    fit: 'Structural rejection layer',
    status: 'PROVED BOUNDARY LAYER',
    lane: 'Failure diagnostics',
    protected: 'Whatever the candidate architecture claims to preserve',
    disturbance: 'Ambiguous, overlapping, or unreachable disturbance families',
    correction: 'Counterexample, obstruction, or impossibility witness',
    plain:
      'The negative-results layer is part of the theory, not an appendix. These examples show when exact recovery is impossible, when sector detection collapses, when correction image is too small, and when smooth flows cannot do exact one-shot recovery.',
    technical:
      'Each preset is wired to a specific theorem, counterexample, or theorem-grade obstruction in the repository. The point is to make failure structural and inspectable rather than rhetorical.',
    use: 'Use this to understand what the framework excludes and why those exclusions matter.',
    avoid: 'Do not hide these cases. The no-go layer is one of the strongest outputs of the repo.',
    refs: [
      { title: 'No-go spine', href: '../finalization/no-go-spine-final.md', note: 'Finalized impossibility layer' },
      { title: 'Advanced no-go results', href: '../impossibility-results/advanced-no-go-results.md', note: 'Sharper flow and sector boundaries' },
      { title: 'Kept vs rejected physics bridges', href: '../physics/kept-vs-rejected-physics-bridges.md', note: 'Physics-side demotions and rejections' },
    ],
    literature: [
      { title: 'Constraint-preserving vs damped systems', href: 'https://doi.org/10.1088/1361-6382/ac88af', note: 'Useful scope-control anchor' },
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

const LAB_DEFAULTS = cloneState(DEFAULT_STATE.labs);

let state = initialState();
let latestAnalysis = analyzeActiveLab();
let savedScenarios = loadSavedScenarios();
let playbackTimer = null;
let playbackLab = null;

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
    case 'recoverability':
      return analyzeRecoverability(state.labs.recoverability);
    case 'exact':
      return analyzeExactProjection(state.labs.exact);
    case 'qec':
      return analyzeQecSector(state.labs.qec);
    case 'mhd':
      return analyzeMhdProjection(state.labs.mhd);
    case 'cfd':
      return analyzeCfdProjection(state.labs.cfd);
    case 'gauge':
      return analyzeGaugeProjection(state.labs.gauge);
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
  state.labs.continuous.frame = state.labs.continuous.steps;
}

function render() {
  normalizeInteractiveState();
  latestAnalysis = analyzeActiveLab();
  syncHash();
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
            <p class="deck">A static scientific workbench for exact projection, sector recovery, continuous asymptotic correction, and theorem-grade failure modes. The workbench uses the Orthogonal Correction Principle as the core internal principle name, but keeps the public-facing structure theory-first and proof-linked.</p>
            <div class="hero-meta-row">
              <span class="fit-pill">${meta.branch}</span>
              <span class="status-pill">${meta.status}</span>
              <span class="fit-pill subtle">Physics lane: ${meta.lane}</span>
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

      <section class="module-section">
        <div class="section-heading">
          <h2>Choose a theorem-linked module</h2>
          <p>Each module is kept only if it corresponds to a proved result, a conditional but citable branch, or a sharp rejected bridge.</p>
        </div>
        <div class="module-grid">
          ${renderModuleCards()}
        </div>
      </section>

      <section class="summary-section">
        <div class="summary-grid">
          ${renderSummaryCards(meta)}
        </div>
      </section>

      <main class="workspace">
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
  const parts = path.split('.');
  let target = state;
  for (let i = 0; i < parts.length - 1; i += 1) target = target[parts[i]];
  target[parts[parts.length - 1]] = value;
  state = sanitizeState(state);
  normalizeInteractiveState();
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
  state.labs[state.activeLab] = cloneState(LAB_DEFAULTS[state.activeLab]);
  render();
}

function resetAllLabs() {
  stopPlayback();
  const mode = state.mode;
  const activeLab = state.activeLab;
  state = cloneState(DEFAULT_STATE);
  state.mode = mode;
  state.activeLab = activeLab;
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

function renderConfigPane() {
  switch (state.activeLab) {
    case 'recoverability':
      return `
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
        <div class="callout ${latestAnalysis.impossible ? 'warn' : (latestAnalysis.exact || latestAnalysis.asymptotic) ? 'good' : ''}">
          <strong>${latestAnalysis.status}: ${latestAnalysis.classification}</strong>
          <p>${latestAnalysis.guidance.blocker} ${latestAnalysis.guidance.missing}</p>
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
    case 'recoverability':
      return renderRecoverabilityStage();
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

function renderRecoverabilityStage() {
  const a = latestAnalysis;
  const guidedMode = state.labs.recoverability.studioMode !== 'diagnostic';
  const guidanceTone = a.impossible ? 'warn' : (a.exact || a.asymptotic) ? 'good' : '';
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
            <div><small>Interpretation</small><code>${a.guidance.missing}</code></div>
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
            <div><small>Weaker recoverable target</small><code>${a.guidance.weaker.length ? a.guidance.weaker.join('\n') : 'none needed'}</code></div>
            <div><small>Missing structure</small><code>${a.guidance.missing}</code></div>
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
            <div><small>Weaker recoverable targets</small><code>${a.guidance.weaker.length ? a.guidance.weaker.join('\n') : 'none below current cutoff'}</code></div>
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
            <div><small>Minimal added measurements</small><code>${a.minimalAddedMeasurements === null ? 'none available' : a.minimalAddedMeasurements}</code></div>
            <div><small>Witness gap</small><code>${a.nullspaceWitnessGap.toExponential(3)}</code></div>
            <div><small>Unrecoverable protected rows</small><code>${a.unrecoverableProtectedRows.length}</code></div>
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
          <div><small>Divergence-only witness 1</small><code>${latestAnalysis.divergenceOnlyWitness.firstStateDivergenceRms.toExponential(3)}</code></div>
          <div><small>Divergence-only witness separation</small><code>${latestAnalysis.divergenceOnlyWitness.stateSeparationRms.toExponential(3)}</code></div>
        </div>
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
    case 'recoverability':
      return `<p>${latestAnalysis.classification}. The current system is ${latestAnalysis.systemLabel}, the protected variable is ${latestAnalysis.protectedLabel}, and the chosen record map is ${latestAnalysis.observationLabel}. At the selected tolerance δ = ${latestAnalysis.selectedDelta.toFixed(2)}, the collapse value is ${latestAnalysis.selectedKappa.toExponential(2)} and the zero-noise lower bound from κ(0) is ${(0.5 * latestAnalysis.kappa0).toExponential(2)}. Recommended architecture: ${latestAnalysis.guidance.architecture}. ${latestAnalysis.guidance.missing}${state.labs.recoverability.system === 'analytic' ? ` Under adversarial record noise of the same size, the current lower bound on worst-case protected-variable error is ${latestAnalysis.selectedLowerBound.toExponential(2)}.` : ''}${state.labs.recoverability.system === 'periodic' ? ` The current cutoff is ${latestAnalysis.currentCutoff}, and the predicted minimum cutoff for the chosen protected functional is ${latestAnalysis.predictedMinCutoff}; in this lane the threshold is set by the largest protected visible cutoff, not by raw support size.` : ''}${state.labs.recoverability.system === 'control' ? ` The current horizon is ${state.labs.recoverability.controlHorizon}.${state.labs.recoverability.controlMode === 'diagonal_threshold' ? ` In the diagonal threshold model, the predicted minimum exact-history length is ${latestAnalysis.predictedMinHorizon === null ? 'none because the protected functional is not generated by the sensed moment family' : latestAnalysis.predictedMinHorizon}, and the threshold is governed by interpolation complexity on the active sensor spectrum rather than by support count alone.` : ' In the two-state observer model, the first exact finite-history threshold stays at horizon 2 when ε is nonzero.'}` : ''}${state.labs.recoverability.system === 'linear' ? ` The current static record uses ${latestAnalysis.activeMeasurementLabels.length} measurement rows and ${latestAnalysis.minimalAddedMeasurements === null ? 'no exact fix exists inside the current candidate library.' : `the smallest exact fix needs ${latestAnalysis.minimalAddedMeasurements} added measurement${latestAnalysis.minimalAddedMeasurements === 1 ? '' : 's'}.`}` : ''} This studio is meant to tell you what can be recovered, what is blocked, and what to change next.</p>`;
    case 'exact':
      return `<p>${latestAnalysis.admissible ? 'The disturbance is orthogonal, so projection returns the protected component exactly.' : 'The disturbance overlaps the protected direction, so exact recovery fails in the way the theorem spine predicts.'}</p>`;
    case 'qec':
      return `<p>The selected sector ${latestAnalysis.selectedLabel} is recovered with error ${latestAnalysis.recoveryError.toExponential(2)}. In this branch, exactness comes from sector distinguishability rather than one global projector on the entire physical Hilbert space.</p>`;
    case 'mhd':
      return `<p>Projection drops the divergence norm from ${latestAnalysis.beforeNorm.toExponential(2)} to ${latestAnalysis.afterExactNorm.toExponential(2)}. At the currently selected GLM frame ${latestAnalysis.selectedFrame}, the asymptotic branch sits at ${latestAnalysis.selectedGlmNorm.toExponential(2)} and only reaches ${latestAnalysis.afterGlmNorm.toExponential(2)} at the final frame. This is the exact-versus-asymptotic split in numerical form.</p>`;
    case 'cfd':
      return `<p>The periodic incompressible projection drops the divergence norm from ${latestAnalysis.periodicBeforeNorm.toExponential(2)} to ${latestAnalysis.periodicAfterNorm.toExponential(2)} with recovery error ${latestAnalysis.periodicRecoveryError.toExponential(2)}. The bounded-domain transplant still leaves a boundary-normal mismatch of ${latestAnalysis.boundedProjectedBoundaryNormalRms.toExponential(2)}, so the honest CFD fit remains narrow and boundary-sensitive.</p>`;
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
  downloadText(`protected-state-correction-${state.activeLab}-scenario.json`, JSON.stringify(payload, null, 2), 'application/json');
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
    drawHeatmap('heat-before', latestAnalysis.beforeDiv);
    drawHeatmap('heat-exact', latestAnalysis.afterExactDiv);
    drawHeatmap('heat-glm', latestAnalysis.selectedGlmDiv);
  }
  if (state.activeLab === 'cfd') {
    drawHeatmap('cfd-periodic-before', latestAnalysis.periodicBeforeDiv);
    drawHeatmap('cfd-periodic-after', latestAnalysis.periodicAfterDiv);
    drawHeatmap('cfd-bounded-before', latestAnalysis.boundedBeforeDiv);
    drawHeatmap('cfd-bounded-after', latestAnalysis.boundedAfterDiv);
  }
  if (state.activeLab === 'gauge') {
    drawHeatmap('gauge-before', latestAnalysis.beforeDiv);
    drawHeatmap('gauge-exact', latestAnalysis.afterExactDiv);
    drawHeatmap('gauge-glm', latestAnalysis.selectedGlmDiv);
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
        ${['#1f4b99', '#9c5b2a', '#1c1d21', '#a63229']
          .map(
            (color) => `
          <marker id="arrow-${color.replace('#', '')}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="${color}" />
          </marker>
        `
          )
          .join('')}
      </defs>
      <rect width="${size}" height="${size}" rx="18" fill="rgba(255,255,255,0.78)" />
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
      <rect width="${width}" height="${height}" rx="18" fill="rgba(255,255,255,0.78)" />
      <line x1="20" y1="200" x2="${width - 16}" y2="200" stroke="rgba(28,29,33,0.2)" />
      ${bars.join('')}
      ${labels.join('')}
    </svg>
  `;
}

function lineChartSvg(points, xLabel, yLabel, markerX = null) {
  const finitePoints = points
    .map((point) => ({ x: Number(point.x), y: Number(point.y) }))
    .filter((point) => Number.isFinite(point.x) && Number.isFinite(point.y));
  const width = 540;
  const height = 260;
  const left = 48;
  const right = 18;
  const top = 18;
  const bottom = 42;
  if (!finitePoints.length) {
    return `
      <svg viewBox="0 0 ${width} ${height}" aria-label="Line chart unavailable">
        <rect width="${width}" height="${height}" rx="18" fill="rgba(255,255,255,0.78)" />
        <text x="${width / 2}" y="${height / 2 - 6}" text-anchor="middle" font-size="14" fill="#5d625e">No finite chart data</text>
        <text x="${width / 2}" y="${height / 2 + 18}" text-anchor="middle" font-size="12" fill="#8a8f8b">${xLabel} / ${yLabel}</text>
      </svg>
    `;
  }
  const xs = finitePoints.map((point) => point.x);
  const ys = finitePoints.map((point) => point.y);
  const xMin = Math.min(...xs);
  const xMax = Math.max(...xs);
  const yMin = Math.min(...ys);
  const yMax = Math.max(...ys);
  const xScale = (value) => left + ((value - xMin) / Math.max(xMax - xMin, 1e-9)) * (width - left - right);
  const yScale = (value) => height - bottom - ((value - yMin) / Math.max(yMax - yMin, 1e-9)) * (height - top - bottom);
  const path = finitePoints.map((point, index) => `${index === 0 ? 'M' : 'L'} ${xScale(point.x)} ${yScale(point.y)}`).join(' ');
  const marker = markerX === null
    ? ''
    : (() => {
        const numericMarker = Number(markerX);
        if (!Number.isFinite(numericMarker)) {
          return '';
        }
        const chosen = finitePoints.reduce((best, point) =>
          Math.abs(point.x - numericMarker) < Math.abs(best.x - numericMarker) ? point : best
        );
        const x = xScale(chosen.x);
        const y = yScale(chosen.y);
        return `
          <line x1="${x}" y1="${top}" x2="${x}" y2="${height - bottom}" stroke="rgba(28,29,33,0.18)" stroke-dasharray="5 5" />
          <circle cx="${x}" cy="${y}" r="5" fill="#1c1d21" stroke="#fffdf8" stroke-width="2" />
        `;
      })();
  return `
    <svg viewBox="0 0 ${width} ${height}" aria-label="Line chart">
      <rect width="${width}" height="${height}" rx="18" fill="rgba(255,255,255,0.78)" />
      <line x1="${left}" y1="${height - bottom}" x2="${width - right}" y2="${height - bottom}" stroke="rgba(28,29,33,0.18)" />
      <line x1="${left}" y1="${top}" x2="${left}" y2="${height - bottom}" stroke="rgba(28,29,33,0.18)" />
      <path d="${path}" fill="none" stroke="#9c5b2a" stroke-width="3" stroke-linecap="round" />
      ${marker}
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
    <table class="matrix-table">
      <thead>
        <tr><th></th>${labels.map((label) => `<th>${label}</th>`).join('')}</tr>
      </thead>
      <tbody>
        ${matrix
          .map(
            (row, i) =>
              `<tr><th>${labels[i]}</th>${row.map((value) => `<td>${value.toFixed(3)}</td>`).join('')}</tr>`
          )
          .join('')}
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
