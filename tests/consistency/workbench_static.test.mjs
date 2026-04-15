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
  analyzeRecoverability,
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
    frame: 3,
    poissonIterations: 320,
    dt: 0.05,
    ch: 1,
    cp: 1,
  });
  assert.ok(result.afterExactNorm < result.beforeNorm);
  assert.ok(result.afterGlmNorm < result.beforeNorm);
  assert.ok(result.afterExactNorm < result.afterGlmNorm);
  assert.equal(result.selectedFrame, 3);
  assert.equal(result.selectedGlmNorm, result.glmHistory[3]);
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
    frame: 65,
  });
  assert.equal(result.finiteTimeExactRecoveryPossible, false);
  assert.ok(result.exactRecoveryResidual > 0.05);
  assert.equal(result.selectedFrame, 65);
  assert.ok(result.selectedTime > 0.4 && result.selectedTime < 0.6);
  assert.equal(result.selectedState.length, 3);
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

test('recoverability lab keeps the analytic exact-versus-impossible threshold visible', () => {
  const exact = analyzeRecoverability({
    system: 'analytic',
    analyticEpsilon: 0.25,
    analyticDelta: 0.25,
  });
  const impossible = analyzeRecoverability({
    system: 'analytic',
    analyticEpsilon: 0,
    analyticDelta: 0.25,
  });
  assert.equal(exact.exact, true);
  assert.ok(exact.kappa0 < 1e-9);
  assert.ok(Math.abs(exact.selectedLowerBound - 0.5128205128205128) < 1e-9);
  assert.equal(impossible.impossible, true);
  assert.ok(impossible.kappa0 > 1.9);
});

test('recoverability lab captures qubit phase-loss and weaker-variable recovery', () => {
  const bloch = analyzeRecoverability({
    system: 'qubit',
    qubitProtected: 'bloch_vector',
    qubitPhaseWindowDeg: 30,
    qubitDelta: 0.2,
  });
  const zOnly = analyzeRecoverability({
    system: 'qubit',
    qubitProtected: 'z_coordinate',
    qubitPhaseWindowDeg: 30,
    qubitDelta: 0.2,
  });
  assert.equal(bloch.impossible, true);
  assert.ok(bloch.kappa0 > 0.2);
  assert.equal(zOnly.exact, true);
  assert.ok(zOnly.kappa0 < 1e-8);
});

test('recoverability lab keeps periodic exact, approximate, and no-go branches separate', () => {
  const full = analyzeRecoverability({
    system: 'periodic',
    periodicProtected: 'full_modal_coefficients',
    periodicObservation: 'full_vorticity',
    periodicDelta: 2,
  });
  const cutoffOne = analyzeRecoverability({
    system: 'periodic',
    periodicProtected: 'full_modal_coefficients',
    periodicObservation: 'cutoff_vorticity',
    periodicCutoff: 1,
    periodicDelta: 2,
  });
  const cutoffThree = analyzeRecoverability({
    system: 'periodic',
    periodicProtected: 'full_modal_coefficients',
    periodicObservation: 'cutoff_vorticity',
    periodicCutoff: 3,
    periodicDelta: 2,
  });
  const cutoffFour = analyzeRecoverability({
    system: 'periodic',
    periodicProtected: 'full_modal_coefficients',
    periodicObservation: 'cutoff_vorticity',
    periodicCutoff: 4,
    periodicDelta: 2,
  });
  const lowMode = analyzeRecoverability({
    system: 'periodic',
    periodicProtected: 'mode_1_coefficient',
    periodicObservation: 'cutoff_vorticity',
    periodicCutoff: 1,
    periodicDelta: 2,
  });
  const lowModeSum = analyzeRecoverability({
    system: 'periodic',
    periodicProtected: 'low_mode_sum',
    periodicObservation: 'cutoff_vorticity',
    periodicCutoff: 2,
    periodicDelta: 2,
  });
  const bandlimitedContrast = analyzeRecoverability({
    system: 'periodic',
    periodicProtected: 'bandlimited_contrast',
    periodicObservation: 'cutoff_vorticity',
    periodicCutoff: 3,
    periodicDelta: 2,
  });
  const divergence = analyzeRecoverability({
    system: 'periodic',
    periodicProtected: 'full_modal_coefficients',
    periodicObservation: 'divergence_only',
    periodicDelta: 2,
  });
  assert.equal(full.exact, true);
  assert.ok(full.meanRecoveryError < 1e-6);
  assert.equal(cutoffOne.exact, false);
  assert.equal(cutoffOne.impossible, true);
  assert.equal(cutoffThree.exact, false);
  assert.equal(cutoffFour.exact, true);
  assert.equal(lowMode.exact, true);
  assert.equal(lowModeSum.exact, true);
  assert.equal(bandlimitedContrast.exact, true);
  assert.ok(cutoffOne.meanRecoveryError > full.meanRecoveryError);
  assert.ok(cutoffOne.kappa0 > 0.1);
  assert.ok(cutoffFour.kappa0 < 1e-8);
  assert.equal(lowMode.predictedMinCutoff, 1);
  assert.equal(lowModeSum.predictedMinCutoff, 2);
  assert.equal(bandlimitedContrast.predictedMinCutoff, 3);
  assert.equal(divergence.impossible, true);
  assert.ok(divergence.kappa0 > cutoffOne.kappa0);
});

test('recoverability lab keeps finite-history and observer asymptotics distinct', () => {
  const oneStep = analyzeRecoverability({
    system: 'control',
    controlEpsilon: 0.2,
    controlHorizon: 1,
    controlDelta: 0.5,
  });
  const twoStep = analyzeRecoverability({
    system: 'control',
    controlEpsilon: 0.2,
    controlHorizon: 2,
    controlDelta: 0.5,
  });
  assert.equal(oneStep.exact, false);
  assert.equal(oneStep.asymptotic, true);
  assert.ok(Math.abs(oneStep.kappa0 - 2) < 1e-9);
  assert.equal(twoStep.exact, true);
  assert.ok(twoStep.kappa0 < 1e-9);
  assert.ok(twoStep.meanRecoveryError < 1e-8);
  assert.ok(twoStep.observerErrorHistory.at(-1) < twoStep.observerErrorHistory[0]);
});

test('recoverability lab captures the three-state minimal-history threshold', () => {
  const oneStep = analyzeRecoverability({
    system: 'control',
    controlMode: 'diagonal_threshold',
    controlProfile: 'three_active',
    controlFunctional: 'protected_coordinate',
    controlHorizon: 1,
    controlDelta: 0.5,
  });
  const twoActive = analyzeRecoverability({
    system: 'control',
    controlMode: 'diagonal_threshold',
    controlProfile: 'two_active',
    controlFunctional: 'protected_coordinate',
    controlHorizon: 2,
    controlDelta: 0.5,
  });
  const threeActive = analyzeRecoverability({
    system: 'control',
    controlMode: 'diagonal_threshold',
    controlProfile: 'three_active',
    controlFunctional: 'protected_coordinate',
    controlHorizon: 3,
    controlDelta: 0.5,
  });
  const hidden = analyzeRecoverability({
    system: 'control',
    controlMode: 'diagonal_threshold',
    controlProfile: 'protected_hidden',
    controlFunctional: 'protected_coordinate',
    controlHorizon: 4,
    controlDelta: 0.5,
  });
  const momentOne = analyzeRecoverability({
    system: 'control',
    controlMode: 'diagonal_threshold',
    controlProfile: 'three_active',
    controlFunctional: 'first_moment',
    controlHorizon: 2,
    controlDelta: 0.5,
  });
  const momentTwo = analyzeRecoverability({
    system: 'control',
    controlMode: 'diagonal_threshold',
    controlProfile: 'three_active',
    controlFunctional: 'second_moment',
    controlHorizon: 3,
    controlDelta: 0.5,
  });
  const sensorSum = analyzeRecoverability({
    system: 'control',
    controlMode: 'diagonal_threshold',
    controlProfile: 'three_active',
    controlFunctional: 'sensor_sum',
    controlHorizon: 1,
    controlDelta: 0.5,
  });
  assert.equal(oneStep.exact, false);
  assert.equal(oneStep.predictedMinHorizon, 3);
  assert.equal(twoActive.exact, true);
  assert.equal(twoActive.predictedMinHorizon, 2);
  assert.ok(twoActive.meanRecoveryError < 1e-8);
  assert.equal(threeActive.exact, true);
  assert.ok(threeActive.kappa0 < 1e-8);
  assert.equal(momentOne.exact, true);
  assert.equal(momentOne.predictedMinHorizon, 2);
  assert.equal(momentTwo.exact, true);
  assert.equal(momentTwo.predictedMinHorizon, 3);
  assert.equal(sensorSum.exact, true);
  assert.equal(sensorSum.predictedMinHorizon, 1);
  assert.equal(hidden.exact, false);
  assert.equal(hidden.impossible, true);
  assert.equal(hidden.predictedMinHorizon, null);
});
