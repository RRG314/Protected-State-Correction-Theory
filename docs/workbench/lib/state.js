export const DEFAULT_STATE = {
  mode: 'plain',
  activeLab: 'exact',
  labs: {
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
      poissonIterations: 320,
      dt: 0.05,
      ch: 1,
      cp: 1,
    },
    gauge: {
      gridSize: 14,
      contamination: 0.18,
      glmSteps: 8,
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
