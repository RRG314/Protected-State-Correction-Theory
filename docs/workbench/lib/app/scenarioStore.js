import { DEFAULT_STATE, STORAGE_KEY } from '../domain/defaultState.js';
import { cloneState, decodeShareState, encodeShareState, sanitizeState } from './scenarioSerialization.js';
import { analyzeLab } from './analysisDispatcher.js';

export function createWorkbenchStore(windowObject = window) {
  let state = decodeShareState(windowObject.location.hash) ?? cloneState(DEFAULT_STATE);
  let savedScenarios = loadSavedScenarios(windowObject);
  let latestAnalysis = analyzeLab(state.activeLab, state.labs);

  function refreshAnalysis() {
    latestAnalysis = analyzeLab(state.activeLab, state.labs);
    return latestAnalysis;
  }

  function syncHash() {
    const encoded = encodeShareState(state);
    windowObject.history.replaceState(null, '', `#state=${encoded}`);
  }

  function snapshot() {
    return {
      state,
      latestAnalysis,
      savedScenarios,
    };
  }

  function setState(nextState) {
    state = sanitizeState(nextState);
    refreshAnalysis();
    syncHash();
    return snapshot();
  }

  function patchLab(lab, patch) {
    state = sanitizeState({
      ...state,
      labs: {
        ...state.labs,
        [lab]: {
          ...state.labs[lab],
          ...patch,
        },
      },
    });
    refreshAnalysis();
    syncHash();
    return snapshot();
  }

  function setActiveLab(lab) {
    if (!state.labs[lab]) return snapshot();
    state = sanitizeState({ ...state, activeLab: lab });
    refreshAnalysis();
    syncHash();
    return snapshot();
  }

  function setMode(mode) {
    state = sanitizeState({ ...state, mode });
    refreshAnalysis();
    syncHash();
    return snapshot();
  }

  function setStatePath(path, value) {
    const parts = path.split('.');
    const next = cloneState(state);
    let target = next;
    for (let i = 0; i < parts.length - 1; i += 1) target = target[parts[i]];
    target[parts[parts.length - 1]] = value;
    return setState(next);
  }

  function resetCurrentLab() {
    return patchLab(state.activeLab, cloneState(DEFAULT_STATE.labs[state.activeLab]));
  }

  function resetAllLabs() {
    const preservedMode = state.mode;
    const preservedActiveLab = state.activeLab;
    return setState({
      ...cloneState(DEFAULT_STATE),
      mode: preservedMode,
      activeLab: preservedActiveLab,
    });
  }

  function saveScenario(name) {
    savedScenarios = {
      ...savedScenarios,
      [name]: cloneState(state),
    };
    saveScenariosStore(windowObject, savedScenarios);
    return snapshot();
  }

  function loadScenario(name) {
    if (!savedScenarios[name]) return snapshot();
    return setState(savedScenarios[name]);
  }

  function hydrateFromHash(hash) {
    const decoded = decodeShareState(hash);
    if (!decoded) return null;
    return setState(decoded);
  }

  return {
    snapshot,
    setState,
    setActiveLab,
    setMode,
    setStatePath,
    patchLab,
    resetCurrentLab,
    resetAllLabs,
    saveScenario,
    loadScenario,
    hydrateFromHash,
    refreshAnalysis,
    syncHash,
    getShareState: () => encodeShareState(state),
  };
}

function loadSavedScenarios(windowObject) {
  try {
    return JSON.parse(windowObject.localStorage.getItem(STORAGE_KEY) ?? '{}');
  } catch {
    return {};
  }
}

function saveScenariosStore(windowObject, savedScenarios) {
  windowObject.localStorage.setItem(STORAGE_KEY, JSON.stringify(savedScenarios));
}
