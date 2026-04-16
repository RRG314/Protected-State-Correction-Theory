import test from 'node:test';
import assert from 'node:assert/strict';

import { createWorkbenchStore } from '../../docs/workbench/lib/app/scenarioStore.js';
import { DEFAULT_STATE } from '../../docs/workbench/lib/domain/defaultState.js';
import { encodeShareState } from '../../docs/workbench/lib/app/scenarioSerialization.js';

function makeWindow({ hash = '', storage = {} } = {}) {
  const local = new Map(Object.entries(storage));
  return {
    location: {
      hash,
    },
    history: {
      replaceState(_state, _title, url) {
        const [, nextHash = ''] = String(url).split('#');
        this.lastUrl = String(url);
        windowObject.location.hash = nextHash ? `#${nextHash}` : '';
      },
      lastUrl: '',
    },
    localStorage: {
      getItem(key) {
        return local.has(key) ? local.get(key) : null;
      },
      setItem(key, value) {
        local.set(key, value);
      },
    },
  };
}

let windowObject;

test('scenario store hydrates from share-state hash and computes matching analysis', () => {
  const encoded = encodeShareState({
    ...DEFAULT_STATE,
    activeLab: 'recoverability',
    labs: {
      ...DEFAULT_STATE.labs,
      recoverability: {
        ...DEFAULT_STATE.labs.recoverability,
        system: 'linear',
        linearProtected: 'x3',
        linearMeasurements: {
          ...DEFAULT_STATE.labs.recoverability.linearMeasurements,
          measure_x3: false,
        },
      },
    },
  });
  windowObject = makeWindow({ hash: `#state=${encoded}` });
  const store = createWorkbenchStore(windowObject);
  const snapshot = store.snapshot();
  assert.equal(snapshot.state.activeLab, 'recoverability');
  assert.equal(snapshot.state.labs.recoverability.system, 'linear');
  assert.equal(snapshot.latestAnalysis.status, 'Impossible');
  assert.match(snapshot.latestAnalysis.structuralBlocker, /nullspace witness|leaving the record fixed/i);
});

test('scenario store updates nested state paths and keeps share-state in sync', () => {
  windowObject = makeWindow();
  const store = createWorkbenchStore(windowObject);
  store.setActiveLab('recoverability');
  store.setStatePath('labs.recoverability.system', 'periodic');
  store.setStatePath('labs.recoverability.periodicObservation', 'cutoff_vorticity');
  store.setStatePath('labs.recoverability.periodicProtected', 'full_weighted_sum');
  store.setStatePath('labs.recoverability.periodicCutoff', 4);
  const snapshot = store.snapshot();
  assert.equal(snapshot.state.labs.recoverability.periodicCutoff, 4);
  assert.equal(snapshot.latestAnalysis.predictedMinCutoff, 4);
  assert.equal(snapshot.latestAnalysis.exact, true);
  assert.match(windowObject.history.lastUrl, /#state=/);
});

test('scenario store reset and saved scenario flows preserve orchestration boundaries', () => {
  windowObject = makeWindow();
  const store = createWorkbenchStore(windowObject);
  store.setMode('technical');
  store.setActiveLab('mixer');
  store.setStatePath('labs.mixer.mode', 'random');
  store.setStatePath('labs.mixer.randomSeed', 99);
  store.saveScenario('random-search');
  store.resetCurrentLab();
  let snapshot = store.snapshot();
  assert.equal(snapshot.state.activeLab, 'mixer');
  assert.equal(snapshot.state.mode, 'technical');
  assert.equal(snapshot.state.labs.mixer.randomSeed, DEFAULT_STATE.labs.mixer.randomSeed);
  store.loadScenario('random-search');
  snapshot = store.snapshot();
  assert.equal(snapshot.state.labs.mixer.randomSeed, 99);
  assert.equal(snapshot.state.labs.mixer.mode, 'random');
});
