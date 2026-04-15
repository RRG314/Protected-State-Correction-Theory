export const DEFAULT_STATE = {
  mode: 'plain',
  activeLab: 'recoverability',
  labs: {
    recoverability: {
      system: 'analytic',
      analyticEpsilon: 0.25,
      analyticDelta: 0.25,
      studioMode: 'guided',
      qubitProtected: 'bloch_vector',
      qubitPhaseWindowDeg: 30,
      qubitDelta: 0.2,
      periodicObservation: 'cutoff_vorticity',
      periodicProtected: 'full_modal_coefficients',
      periodicCutoff: 1,
      periodicDelta: 2.0,
      controlMode: 'two_state_observer',
      controlProfile: 'three_active',
      controlFunctional: 'protected_coordinate',
      controlEpsilon: 0.2,
      controlHorizon: 2,
      controlDelta: 0.5,
      linearTemplate: 'sensor_basis',
      linearProtected: 'x3',
      linearDelta: 1.0,
      boundaryArchitecture: 'periodic_transplant',
      boundaryProtected: 'bounded_velocity_class',
      boundaryGridSize: 17,
      boundaryDelta: 0.2,
      linearMeasurements: {
        measure_x1: true,
        measure_x2_plus_x3: true,
        measure_x2: false,
        measure_x3: false,
        measure_x1_plus_x2: false,
      },
    },
    exact: {
      protectedMagnitude: 1.4,
      disturbanceMagnitude: 0.9,
      angleDeg: 90,
    },
    qec: {
      alpha: 1,
      beta: 1,
      errorIndex: 2,
    },
    mhd: {
      gridSize: 14,
      contamination: 0.22,
      glmSteps: 8,
      frame: 8,
      poissonIterations: 320,
      dt: 0.05,
      ch: 1,
      cp: 1,
    },
    cfd: {
      periodicGridSize: 14,
      boundedGridSize: 18,
      contamination: 0.22,
      poissonIterations: 320,
    },
    gauge: {
      gridSize: 14,
      contamination: 0.18,
      glmSteps: 8,
      frame: 8,
      poissonIterations: 320,
      dt: 0.05,
      ch: 1,
      cp: 1,
    },
    continuous: {
      preset: 'invariant',
      matrix: [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 1.5],
      ],
      x0: [2, -1, 0.5],
      time: 2,
      steps: 280,
      frame: 280,
    },
    nogo: {
      example: 'finite-time',
    },
    benchmark: {
      suite: 'all',
      selectedDemo: 'periodic_modal_repair',
    },
  },
};

export const STORAGE_KEY = 'ocp-workbench-scenarios';

export function cloneState(value) {
  return JSON.parse(JSON.stringify(value));
}

export function sanitizeState(candidate) {
  const safe = cloneState(DEFAULT_STATE);
  if (!candidate || typeof candidate !== 'object') return safe;
  if (candidate.mode === 'technical') safe.mode = 'technical';
  if (typeof candidate.activeLab === 'string' && safe.labs[candidate.activeLab]) {
    safe.activeLab = candidate.activeLab;
  }
  for (const [lab, defaults] of Object.entries(safe.labs)) {
    if (candidate.labs?.[lab] && typeof candidate.labs[lab] === 'object') {
      for (const key of Object.keys(defaults)) {
        if (candidate.labs[lab][key] !== undefined) {
          safe.labs[lab][key] = candidate.labs[lab][key];
        }
      }
    }
  }
  return safe;
}

const encodeBase64 = (text) => {
  if (typeof btoa === 'function') {
    return btoa(unescape(encodeURIComponent(text)));
  }
  return Buffer.from(text, 'utf8').toString('base64');
};

const decodeBase64 = (text) => {
  if (typeof atob === 'function') {
    return decodeURIComponent(escape(atob(text)));
  }
  return Buffer.from(text, 'base64').toString('utf8');
};

export function encodeShareState(state) {
  const payload = JSON.stringify(sanitizeState(state));
  return encodeBase64(payload);
}

export function decodeShareState(hash) {
  try {
    const cleaned = hash.replace(/^#?state=/, '').trim();
    if (!cleaned) return null;
    const json = decodeBase64(cleaned);
    return sanitizeState(JSON.parse(json));
  } catch {
    return null;
  }
}

export function exportScenarioPayload(state, analysis) {
  return {
    exportedAt: new Date().toISOString(),
    workbenchVersion: 'structural-discovery-v2',
    activeLab: sanitizeState(state).activeLab,
    evidenceLevel: scenarioEvidenceLevel(state, analysis),
    state: sanitizeState(state),
    analysis,
  };
}

export function scenarioEvidenceLevel(state, analysis) {
  const activeLab = sanitizeState(state).activeLab;
  if (activeLab === 'recoverability') {
    if (state.labs.recoverability.system === 'linear') return 'theorem-backed restricted-linear result';
    if (state.labs.recoverability.system === 'boundary') {
      return state.labs.recoverability.boundaryArchitecture === 'boundary_compatible_hodge'
        ? 'restricted exact bounded-domain result'
        : 'theorem-linked counterexample and family-specific redesign guidance';
    }
    if (state.labs.recoverability.system === 'analytic') return 'explicit analytic benchmark';
    if (state.labs.recoverability.system === 'qubit') return 'family-specific result with standard external guidance';
    if (state.labs.recoverability.system === 'periodic') return 'family-specific threshold result';
    if (state.labs.recoverability.system === 'control') return 'family-specific threshold and asymptotic benchmark';
  }
  if (activeLab === 'exact' || activeLab === 'qec' || activeLab === 'mhd' || activeLab === 'gauge') {
    return 'theorem-backed or theorem-linked branch example';
  }
  if (activeLab === 'cfd' || activeLab === 'nogo' || activeLab === 'continuous') {
    return 'validated theorem / no-go / empirical branch example';
  }
  if (activeLab === 'benchmark') {
    return 'validated workbench benchmark and regression surface';
  }
  return analysis?.theoremStatus ?? 'workbench output';
}

function formatValue(value) {
  if (typeof value === 'number') {
    if (!Number.isFinite(value)) return String(value);
    if (Math.abs(value) >= 1000 || (Math.abs(value) > 0 && Math.abs(value) < 1e-2)) {
      return value.toExponential(3);
    }
    return value.toFixed(3);
  }
  if (typeof value === 'string') return value;
  if (typeof value === 'boolean') return value ? 'yes' : 'no';
  return JSON.stringify(value, null, 2);
}

function configLines(config) {
  return Object.entries(config)
    .map(([key, value]) => `- \`${key}\`: ${formatValue(value)}`)
    .join('\n');
}

function metricLines(analysis) {
  const pairs = Object.entries(analysis ?? {})
    .filter(([, value]) => ['number', 'string', 'boolean'].includes(typeof value))
    .slice(0, 18);
  return pairs.map(([key, value]) => `- \`${key}\`: ${formatValue(value)}`).join('\n');
}

export function exportScenarioReport(state, analysis) {
  const safeState = sanitizeState(state);
  const activeLab = safeState.activeLab;
  const config = safeState.labs[activeLab];
  const title = `Protected-State Correction Workbench Report — ${activeLab}`;
  const recommendations = Array.isArray(analysis?.recommendations)
    ? analysis.recommendations.map((item) => `- ${item.title}: ${item.rationale}`).join('\n')
    : '';
  const comparison = analysis?.comparison
    ? [
        `- before regime: ${analysis.comparison.beforeRegime}`,
        `- after regime: ${analysis.comparison.afterRegime}`,
        `- key metric: ${analysis.comparison.keyMetricName}`,
        `- before metric: ${formatValue(analysis.comparison.keyMetricBefore)}`,
        `- after metric: ${formatValue(analysis.comparison.keyMetricAfter)}`,
        `- narrative: ${analysis.comparison.narrative}`,
      ].join('\n')
    : '- no before/after comparison available for the current state';
  return [
    `# ${title}`,
    '',
    `- exported at: ${new Date().toISOString()}`,
    `- active lab: ${activeLab}`,
    `- evidence level: ${scenarioEvidenceLevel(state, analysis)}`,
    '',
    '## Summary',
    '',
    activeLab === 'recoverability'
      ? `${analysis?.status ?? 'Unknown'} — ${analysis?.classification ?? 'No classification available.'}`
      : `${analysis?.title ?? analysis?.systemLabel ?? activeLab} — ${analysis?.status ?? analysis?.classification ?? 'Workbench output'}`,
    '',
    '## Configuration',
    '',
    configLines(config),
    '',
    '## Analysis',
    '',
    analysis?.structuralBlocker
      ? `- blocker: ${analysis.structuralBlocker}`
      : analysis?.summary
        ? `- summary: ${analysis.summary}`
        : '- summary: see metrics below',
    analysis?.missingStructure ? `- missing structure: ${analysis.missingStructure}` : null,
    analysis?.recommendedArchitecture ? `- recommended architecture: ${analysis.recommendedArchitecture}` : null,
    analysis?.guidance?.noGo ? `- no-go / boundary: ${analysis.guidance.noGo}` : null,
    '',
    '## Key Metrics',
    '',
    metricLines(analysis),
    '',
    '## Recommendations',
    '',
    recommendations || '- no additional recommendation list for the current lab',
    '',
    '## Before / After',
    '',
    comparison,
    '',
    '## Reproducibility',
    '',
    '- export source: static Protected-State Correction Workbench',
    '- data origin: current in-browser configuration and analysis result',
    '- provenance: use the JSON export for exact state replay and the share link for direct UI reconstruction',
    '',
  ]
    .filter(Boolean)
    .join('\n');
}

export function exportScenarioCsv(state, analysis) {
  const activeLab = sanitizeState(state).activeLab;
  if (activeLab === 'recoverability') {
    const rows = [['series', 'x', 'y']];
    if (Array.isArray(analysis?.deltas) && Array.isArray(analysis?.collapse)) {
      analysis.deltas.forEach((delta, index) => {
        rows.push(['collapse', String(delta), String(analysis.collapse[index])]);
      });
    }
    if (Array.isArray(analysis?.thresholdCutoffs) && Array.isArray(analysis?.thresholdKappa0)) {
      analysis.thresholdCutoffs.forEach((cutoff, index) => {
        rows.push(['threshold_kappa0', String(cutoff), String(analysis.thresholdKappa0[index])]);
      });
    }
    if (Array.isArray(analysis?.historyThreshold)) {
      analysis.historyThreshold.forEach((item) => {
        rows.push(['history_threshold', String(item.horizon), String(item.kappa0)]);
      });
    }
    if (Array.isArray(analysis?.boundaryArchitectureSeries)) {
      analysis.boundaryArchitectureSeries.forEach((item) => {
        rows.push(['boundary_architecture', String(item.x), String(item.y)]);
      });
    }
    return rows.map((row) => row.join(',')).join('\n');
  }
  if (activeLab === 'benchmark' && Array.isArray(analysis?.demoRows)) {
    const header = ['demo', 'family', 'before_regime', 'after_regime', 'metric_name', 'metric_before', 'metric_after', 'fix'];
    const body = analysis.demoRows.map((row) =>
      [row.demo, row.family, row.beforeRegime, row.afterRegime, row.metricName, row.metricBefore, row.metricAfter, row.fixTitle]
        .map((value) => `"${String(value).replaceAll('"', '""')}"`)
        .join(',')
    );
    return [header.join(','), ...body].join('\n');
  }
  return null;
}
