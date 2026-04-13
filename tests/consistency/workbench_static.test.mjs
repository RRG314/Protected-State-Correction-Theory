import test from 'node:test';
import assert from 'node:assert/strict';
import {
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

test('state share encoding round-trips', () => {
  const encoded = encodeShareState(DEFAULT_STATE);
  const decoded = decodeShareState(`#state=${encoded}`);
  assert.deepEqual(decoded, sanitizeState(DEFAULT_STATE));
});
