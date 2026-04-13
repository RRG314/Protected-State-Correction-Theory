import test from 'node:test';
import assert from 'node:assert/strict';
import {
  analyzeCfdProjection,
  analyzeContinuousGenerator,
  analyzeExactProjection,
  analyzeGaugeProjection,
  analyzeMhdProjection,
  analyzeNoGo,
  analyzeQecSector,
} from '../../docs/workbench/lib/compute.js';
import { DEFAULT_STATE, decodeShareState, encodeShareState, sanitizeState } from '../../docs/workbench/lib/state.js';

test('exact projection lab is exact when the split is orthogonal', () => {
  const result = analyzeExactProjection({ protectedMagnitude: 1.4, disturbanceMagnitude: 0.9, angleDeg: 90 });
  assert.equal(result.admissible, true);
  assert.ok(result.exactError < 1e-9);
});

test('exact projection lab becomes a no-go example when overlap is introduced', () => {
  const result = analyzeExactProjection({ protectedMagnitude: 1.4, disturbanceMagnitude: 0.9, angleDeg: 50 });
  assert.equal(result.admissible, false);
  assert.ok(result.exactError > 0.2);
});

test('qec sector lab recovers the selected bit-flip sector exactly', () => {
  const result = analyzeQecSector({ alpha: 1, beta: 1, errorIndex: 3 });
  assert.ok(result.recoveryError < 1e-9);
});

test('mhd projection outperforms short GLM run on the periodic example', () => {
  const result = analyzeMhdProjection({
    gridSize: 12,
    contamination: 0.22,
    glmSteps: 8,
    poissonIterations: 320,
    dt: 0.05,
    ch: 1,
    cp: 1,
  });
  assert.ok(result.afterExactNorm < result.beforeNorm);
  assert.ok(result.afterGlmNorm < result.beforeNorm);
  assert.ok(result.afterExactNorm < result.afterGlmNorm);
});

test('gauge projection shares the exact-versus-asymptotic split on the compatible example', () => {
  const result = analyzeGaugeProjection({
    gridSize: 12,
    contamination: 0.22,
    glmSteps: 8,
    poissonIterations: 320,
    dt: 0.05,
    ch: 1,
    cp: 1,
  });
  assert.ok(result.afterExactGaugeNorm < result.beforeGaugeNorm);
  assert.ok(result.afterExactGaugeNorm < result.afterGlmGaugeNorm);
});

test('cfd projection keeps the periodic exact branch and bounded-domain limitation visible', () => {
  const result = analyzeCfdProjection({
    periodicGridSize: 12,
    boundedGridSize: 18,
    contamination: 0.22,
    poissonIterations: 320,
  });
  assert.ok(result.periodicAfterNorm < result.periodicBeforeNorm);
  assert.ok(result.periodicRecoveryError < 1e-8);
  assert.ok(result.boundedProjectedBoundaryNormalRms > 1e-2);
  assert.equal(result.boundedTransplantFails, true);
  assert.ok(result.divergenceOnlyWitness.firstStateDivergenceRms < 1e-10);
  assert.ok(result.divergenceOnlyWitness.stateSeparationRms > 0.1);
});

test('continuous generator lab detects finite-time exact recovery failure', () => {
  const result = analyzeContinuousGenerator({
    matrix: [[0, 0, 0], [0, 1, 1], [0, 0, 1.5]],
    x0: [2, -1, 0.5],
    time: 2,
    steps: 260,
  });
  assert.equal(result.finiteTimeExactRecoveryPossible, false);
  assert.ok(result.exactRecoveryResidual > 0.05);
});

test('no-go explorer surfaces the finite-time flow boundary', () => {
  const result = analyzeNoGo({ example: 'finite-time' });
  assert.equal(result.status, 'PROVED NO-GO');
  assert.equal(result.details.finiteTimeExactRecoveryPossible, false);
});

test('no-go explorer surfaces the bounded-domain projector transplant failure', () => {
  const result = analyzeNoGo({ example: 'boundary' });
  assert.equal(result.status, 'COUNTEREXAMPLE / REJECTED BRIDGE');
  assert.ok(result.details.projectedBoundaryNormalRms > 1e-2);
});

test('no-go explorer surfaces the divergence-only bounded recovery failure', () => {
  const result = analyzeNoGo({ example: 'divergence-only' });
  assert.equal(result.status, 'PROVED NO-GO');
  assert.ok(result.details.firstStateDivergenceRms < 1e-10);
  assert.ok(result.details.stateSeparationRms > 0.1);
});

test('state share encoding round-trips', () => {
  const encoded = encodeShareState(DEFAULT_STATE);
  const decoded = decodeShareState(`#state=${encoded}`);
  assert.deepEqual(decoded, sanitizeState(DEFAULT_STATE));
});
