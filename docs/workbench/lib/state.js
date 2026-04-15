export const DEFAULT_STATE = {
  mode: 'plain',
  activeLab: 'exact',
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
    state: sanitizeState(state),
    analysis,
  };
}
