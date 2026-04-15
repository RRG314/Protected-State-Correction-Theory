import test from 'node:test';
import assert from 'node:assert/strict';
import {
  DISCOVERY_MIXER_DEMOS,
  analyzeDiscoveryMixer,
  applyDiscoveryMixerRecommendation,
} from '../../docs/workbench/lib/discoveryMixer.js';
import {
  DEFAULT_STATE,
  exportScenarioCsv,
  exportScenarioReport,
  sanitizeState,
} from '../../docs/workbench/lib/state.js';

test('structured linear mixer recommends a structured fix and becomes exact after application', () => {
  const config = {
    ...DEFAULT_STATE.labs.mixer,
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
  const report = analyzeDiscoveryMixer(config);
  assert.equal(report.mode, 'structured');
  assert.equal(report.family, 'linear');
  assert.equal(report.impossible, true);
  assert.equal(report.chosenRecommendation?.patch?.mode, 'structured');
  assert.equal(report.chosenRecommendation?.patch?.family, 'linear');
  const repaired = analyzeDiscoveryMixer(applyDiscoveryMixerRecommendation(config, report.chosenRecommendation));
  assert.equal(repaired.mode, 'structured');
  assert.equal(repaired.exact, true);
});

test('structured control mixer keeps the repair inside structured mode', () => {
  const config = {
    ...DEFAULT_STATE.labs.mixer,
    mode: 'structured',
    family: 'control',
    structuredControlProfile: 'three_active',
    structuredControlFunctional: 'second_moment',
    structuredControlHorizon: 2,
  };
  const report = analyzeDiscoveryMixer(config);
  assert.equal(report.mode, 'structured');
  assert.equal(report.impossible, true);
  assert.equal(report.chosenRecommendation?.patch?.mode, 'structured');
  assert.equal(report.chosenRecommendation?.patch?.family, 'control');
  const repaired = analyzeDiscoveryMixer(applyDiscoveryMixerRecommendation(config, report.chosenRecommendation));
  assert.equal(repaired.mode, 'structured');
  assert.equal(repaired.exact, true);
});

test('custom nonlinear mixer input is rejected clearly', () => {
  const report = analyzeDiscoveryMixer({
    ...DEFAULT_STATE.labs.mixer,
    mode: 'custom',
    customFamily: 'linear',
    customLinearDimension: 3,
    customLinearObservationText: 'x1\nx2',
    customLinearProtectedText: 'sin(x3)',
    customLinearCandidateText: 'x3',
  });
  assert.equal(report.unsupported, true);
  assert.match(report.diagnostics[0].detail, /nonlinear|unsupported/i);
});

test('demo mode resolves to supported periodic and random demos reproducibly', () => {
  const demo = analyzeDiscoveryMixer({
    ...DEFAULT_STATE.labs.mixer,
    mode: 'demo',
    demoKey: 'periodic_builder',
  });
  assert.equal(demo.family, 'periodic');
  assert.equal(demo.impossible, true);
  assert.ok(DISCOVERY_MIXER_DEMOS.periodic_builder);

  const randomA = analyzeDiscoveryMixer({
    ...DEFAULT_STATE.labs.mixer,
    mode: 'random',
    randomFamily: 'linear',
    randomSeed: 37,
    randomTrials: 16,
    randomObjective: 'failure',
  });
  const randomB = analyzeDiscoveryMixer({
    ...DEFAULT_STATE.labs.mixer,
    mode: 'random',
    randomFamily: 'linear',
    randomSeed: 37,
    randomTrials: 16,
    randomObjective: 'failure',
  });
  assert.deepEqual(randomA.generatedConfig, randomB.generatedConfig);
  assert.equal(randomA.regime, randomB.regime);
});

test('mixer report and csv exports include typed-object and export-row data', () => {
  const state = sanitizeState({
    ...DEFAULT_STATE,
    activeLab: 'mixer',
    labs: {
      ...DEFAULT_STATE.labs,
      mixer: {
        ...DEFAULT_STATE.labs.mixer,
        mode: 'structured',
        family: 'boundary',
        structuredBoundaryArchitecture: 'periodic_transplant',
        structuredBoundaryProtected: 'bounded_velocity_class',
      },
    },
  });
  const analysis = analyzeDiscoveryMixer(state.labs.mixer);
  const report = exportScenarioReport(state, analysis);
  const csv = exportScenarioCsv(state, analysis);
  assert.match(report, /Typed Objects/i);
  assert.match(report, /boundary-compatible Hodge/i);
  assert.match(csv, /boundaryMismatch|family/);
});
