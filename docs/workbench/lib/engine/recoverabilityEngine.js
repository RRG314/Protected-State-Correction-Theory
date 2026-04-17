import {
  EPS,
  clamp,
  identity,
  cloneMatrix,
  dot,
  norm,
  addVec,
  subVec,
  scaleVec,
  addMat,
  scaleMat,
  transpose,
  matVec,
  matMul,
  frobeniusNorm,
  matrixRank,
  rowSpaceResidual,
  recoverableRowIndices,
  minimalRowAugmentation,
  formatVector,
  nullSpace,
  rref,
} from './core/linearAlgebra.js';
import { LINEAR_TEMPLATE_LIBRARY } from '../domain/templates.js';
import { analyzeBoundaryProjectionLimit, analyzeBoundedHodgeCompatible } from './physicsEngine.js';

function flattenValue(value) {
  if (Array.isArray(value) && Array.isArray(value[0])) {
    return value.flat();
  }
  return value.slice();
}

function rmsMetric(a, b) {
  const flatA = flattenValue(a);
  const flatB = flattenValue(b);
  return norm(subVec(flatA, flatB)) / Math.sqrt(Math.max(flatA.length, 1));
}

function scalarGap(a, b) {
  return Math.abs(a[0] - b[0]);
}

function collapseFromSamples(observations, protectedValues, deltas, obsMetric = rmsMetric, protMetric = rmsMetric) {
  return deltas.map((delta) => {
    let maxGap = 0;
    for (let i = 0; i < observations.length; i += 1) {
      for (let j = i + 1; j < observations.length; j += 1) {
        if (obsMetric(observations[i], observations[j]) <= delta + 1e-9) {
          maxGap = Math.max(maxGap, protMetric(protectedValues[i], protectedValues[j]));
        }
      }
    }
    return maxGap;
  });
}

function collapseAtDeltaFromSamples(observations, protectedValues, delta, obsMetric = rmsMetric, protMetric = rmsMetric) {
  let maxGap = 0;
  for (let i = 0; i < observations.length; i += 1) {
    for (let j = i + 1; j < observations.length; j += 1) {
      if (obsMetric(observations[i], observations[j]) <= delta + 1e-9) {
        maxGap = Math.max(maxGap, protMetric(protectedValues[i], protectedValues[j]));
      }
    }
  }
  return maxGap;
}

function fiberCollisionGap(observations, protectedValues, obsMetric = rmsMetric, protMetric = rmsMetric) {
  let maxGap = 0;
  for (let i = 0; i < observations.length; i += 1) {
    for (let j = i + 1; j < observations.length; j += 1) {
      if (obsMetric(observations[i], observations[j]) <= 1e-9) {
        maxGap = Math.max(maxGap, protMetric(protectedValues[i], protectedValues[j]));
      }
    }
  }
  return maxGap;
}

function qubitBloch(theta, phi) {
  return [
    Math.sin(theta) * Math.cos(phi),
    Math.sin(theta) * Math.sin(phi),
    Math.cos(theta),
  ];
}

function qubitRecord(theta) {
  const p0 = Math.cos(theta / 2) ** 2;
  return [p0, 1 - p0];
}

function qubitPhaseCollisionFormula(phaseWindowDeg) {
  const window = Math.abs((phaseWindowDeg * Math.PI) / 180);
  return 2 * Math.sin(Math.min(window, Math.PI / 2));
}

function analyzeQubitRecoverability(config) {
  const phaseWindowDeg = Number(config.qubitPhaseWindowDeg);
  const phaseWindow = (phaseWindowDeg * Math.PI) / 180;
  const protectedMode = config.qubitProtected;
  const thetaGrid = Array.from({ length: 17 }, (_, index) => 0.1 + (index * (Math.PI - 0.2)) / 16);
  const phaseGrid = phaseWindowDeg === 0 ? [0] : Array.from({ length: 13 }, (_, index) => -phaseWindow + (2 * phaseWindow * index) / 12);
  const observations = [];
  const protectedValues = [];
  const recoveryErrors = [];
  for (const theta of thetaGrid) {
    for (const phi of phaseGrid) {
      observations.push(qubitRecord(theta));
      if (protectedMode === 'bloch_vector') {
        const protectedValue = qubitBloch(theta, phi);
        protectedValues.push(protectedValue);
        recoveryErrors.push(rmsMetric(protectedValue, qubitBloch(theta, 0)));
      } else {
        const protectedValue = [Math.cos(theta)];
        protectedValues.push(protectedValue);
        recoveryErrors.push(0);
      }
    }
  }
  const deltas = Array.from({ length: 40 }, (_, index) => index / 39);
  const collapse = collapseFromSamples(
    observations,
    protectedValues,
    deltas,
    rmsMetric,
    protectedMode === 'bloch_vector' ? rmsMetric : scalarGap
  );
  const kappa0 = fiberCollisionGap(
    observations,
    protectedValues,
    rmsMetric,
    protectedMode === 'bloch_vector' ? rmsMetric : scalarGap
  );
  const boundaryWindows = [0, 15, 30, 60, 90, 135, 180];
  const boundaryValues = protectedMode === 'bloch_vector'
    ? boundaryWindows.map((window) => qubitPhaseCollisionFormula(window))
    : boundaryWindows.map(() => 0);
  const selectedDelta = clamp(Number(config.qubitDelta), 0, 1);
  const selectedKappa = collapseAtDeltaFromSamples(
    observations,
    protectedValues,
    selectedDelta,
    rmsMetric,
    protectedMode === 'bloch_vector' ? rmsMetric : scalarGap
  );
  return {
    systemLabel: 'Qubit fixed-basis record',
    protectedLabel: protectedMode === 'bloch_vector' ? 'full Bloch vector' : 'z coordinate only',
    observationLabel: 'fixed-basis measurement probabilities',
    classification:
      protectedMode === 'bloch_vector'
        ? phaseWindowDeg === 0
          ? 'Exact on the meridian family'
          : 'Impossible for full-state recovery'
        : 'Exact for the weaker protected variable',
    exact: kappa0 < 1e-8,
    asymptotic: false,
    impossible: kappa0 > 1e-8,
    deltas,
    collapse,
    selectedDelta,
    selectedKappa,
    kappa0,
    meanRecoveryError: recoveryErrors.reduce((sum, value) => sum + value, 0) / recoveryErrors.length,
    maxRecoveryError: Math.max(...recoveryErrors),
    phaseWindowDeg,
    boundaryWindows,
    boundaryValues,
  };
}

function curl2d(Ux, Uy, h) {
  const dUy = centralDiffX(Uy, h);
  const dUx = centralDiffY(Ux, h);
  return dUy.map((row, i) => row.map((value, j) => value - dUx[i][j]));
}

function lowPassField(field, cutoff) {
  const n = field.length;
  const fieldHat = dft2(field);
  const filteredHat = Array.from({ length: n }, () => Array.from({ length: n }, () => complex(0, 0)));
  for (let kx = 0; kx < n; kx += 1) {
    for (let ky = 0; ky < n; ky += 1) {
      if (Math.abs(fftFrequency(kx, n)) <= cutoff && Math.abs(fftFrequency(ky, n)) <= cutoff) {
        filteredHat[kx][ky] = fieldHat[kx][ky];
      }
    }
  }
  return idft2(filteredHat);
}

function velocityFromVorticity(field, h) {
  const psi = solvePoissonPeriodic(field, h);
  return {
    Ux: centralDiffY(psi, h).map((row) => row.map((value) => -value)),
    Uy: centralDiffX(psi, h),
  };
}

const PERIODIC_MODE_CUTOFFS = [1, 2, 3, 4];

function periodicProtectedFamily() {
  const coeffs = [-1, 0, 1];
  const family = [];
  for (const c1 of coeffs) {
    for (const c2 of coeffs) {
      for (const c3 of coeffs) {
        for (const c4 of coeffs) {
          family.push({ coefficients: [c1, c2, c3, c4] });
        }
      }
    }
  }
  return family;
}

function periodicProtectedVector(coefficients, protectedVariable) {
  switch (protectedVariable) {
    case 'mode_1_coefficient':
      return [coefficients[0]];
    case 'modes_1_2_coefficients':
      return [coefficients[0], coefficients[1]];
    case 'low_mode_sum':
      return [coefficients[0] + coefficients[1]];
    case 'bandlimited_contrast':
      return [coefficients[1] - coefficients[2]];
    case 'full_weighted_sum':
      return [coefficients[0] - 0.5 * coefficients[1] + 0.75 * coefficients[2] + 0.25 * coefficients[3]];
    case 'full_modal_coefficients':
    default:
      return coefficients.slice();
  }
}

function periodicProtectedThreshold(protectedVariable) {
  switch (protectedVariable) {
    case 'mode_1_coefficient':
      return 1;
    case 'modes_1_2_coefficients':
      return 2;
    case 'low_mode_sum':
      return 2;
    case 'bandlimited_contrast':
      return 3;
    case 'full_weighted_sum':
      return 4;
    case 'full_modal_coefficients':
    default:
      return 4;
  }
}

function periodicProtectedLabel(protectedVariable) {
  switch (protectedVariable) {
    case 'mode_1_coefficient':
      return 'leading modal coefficient';
    case 'modes_1_2_coefficients':
      return 'first two modal coefficients';
    case 'low_mode_sum':
      return 'low-mode weighted sum';
    case 'bandlimited_contrast':
      return 'band-limited contrast functional';
    case 'full_weighted_sum':
      return 'full weighted modal sum';
    case 'full_modal_coefficients':
    default:
      return 'full four-mode coefficient vector';
  }
}

function periodicObservationVector(coefficients, observation, cutoff) {
  if (observation === 'divergence_only') {
    return [0];
  }
  if (observation === 'full_vorticity') {
    return coefficients.slice();
  }
  return coefficients.map((value, index) => (PERIODIC_MODE_CUTOFFS[index] <= cutoff ? value : 0));
}

function periodicEstimatedProtected(coefficients, observation, cutoff, protectedVariable) {
  const estimatedCoefficients =
    observation === 'divergence_only'
      ? Array.from({ length: PERIODIC_MODE_CUTOFFS.length }, () => 0)
      : observation === 'full_vorticity'
        ? coefficients.slice()
        : coefficients.map((value, index) => (PERIODIC_MODE_CUTOFFS[index] <= cutoff ? value : 0));
  return periodicProtectedVector(estimatedCoefficients, protectedVariable);
}

const periodicRecoverabilityCache = new Map();

function periodicObservationResult(observation, protectedVariable, family, cutoff = 1) {
  const cacheKey = `${observation}:${protectedVariable}:${cutoff}`;
  if (periodicRecoverabilityCache.has(cacheKey)) {
    return periodicRecoverabilityCache.get(cacheKey);
  }
  const deltas = Array.from({ length: 40 }, (_, index) => (index * 3) / 39);
  const observations = [];
  const protectedValues = [];
  const errors = [];
  for (const state of family) {
    const protectedValue = periodicProtectedVector(state.coefficients, protectedVariable);
    const observed = periodicObservationVector(state.coefficients, observation, cutoff);
    const estimate = periodicEstimatedProtected(state.coefficients, observation, cutoff, protectedVariable);
    observations.push(observed);
    protectedValues.push(protectedValue);
    errors.push(rmsMetric(estimate, protectedValue));
  }
  const metric = periodicProtectedVector([0, 0, 0, 0], protectedVariable).length === 1 ? scalarGap : rmsMetric;
  const collapse = collapseFromSamples(observations, protectedValues, deltas, rmsMetric, metric);
  const kappa0 = fiberCollisionGap(observations, protectedValues, rmsMetric, metric);
  const result = {
    deltas,
    collapse,
    kappa0,
    observations,
    protectedValues,
    protectedMetric: metric,
    meanRecoveryError: errors.reduce((sum, value) => sum + value, 0) / errors.length,
    maxRecoveryError: Math.max(...errors),
  };
  periodicRecoverabilityCache.set(cacheKey, result);
  return result;
}

function analyzePeriodicRecoverability(config) {
  const observation = config.periodicObservation;
  const protectedVariable = config.periodicProtected;
  const cutoff = Number(config.periodicCutoff ?? 1);
  const family = periodicProtectedFamily();
  const current = periodicObservationResult(observation, protectedVariable, family, cutoff);
  const selectedDelta = clamp(Number(config.periodicDelta), 0, 3);
  const selectedKappa = collapseAtDeltaFromSamples(
    current.observations,
    current.protectedValues,
    selectedDelta,
    rmsMetric,
    current.protectedMetric
  );
  const thresholdCutoffs = [0, 1, 2, 3, 4];
  const thresholdRows = thresholdCutoffs.map((value) => ({
    cutoff: value,
    result: periodicObservationResult('cutoff_vorticity', protectedVariable, family, value),
  }));
  const threshold = periodicProtectedThreshold(protectedVariable);
  const exact =
    observation === 'full_vorticity' ||
    (observation === 'cutoff_vorticity' && cutoff >= threshold && current.kappa0 < 1e-8);
  const impossible = observation === 'divergence_only' || (observation === 'cutoff_vorticity' && cutoff < threshold);
  const classification =
    observation === 'full_vorticity'
      ? 'Exact on the finite modal family'
      : observation === 'divergence_only'
        ? 'Impossible for nontrivial recovery'
        : cutoff >= threshold
          ? 'Exact once the protected modal support is retained'
          : 'Impossible below the protected-support cutoff';
  return {
    systemLabel: 'Finite periodic incompressible modal family',
    protectedLabel: periodicProtectedLabel(protectedVariable),
    observationLabel: observation === 'cutoff_vorticity' ? `cutoff vorticity coordinates (cutoff ${cutoff})` : observation.replaceAll('_', ' '),
    classification,
    exact,
    asymptotic: false,
    impossible,
    deltas: current.deltas,
    collapse: current.collapse,
    selectedDelta,
    selectedKappa,
    kappa0: current.kappa0,
    meanRecoveryError: current.meanRecoveryError,
    maxRecoveryError: current.maxRecoveryError,
    currentCutoff: cutoff,
    predictedMinCutoff: threshold,
    thresholdCutoffs,
    thresholdKappa0: thresholdRows.map((item) => item.result.kappa0),
    thresholdErrors: thresholdRows.map((item) => item.result.meanRecoveryError),
  };
}

function ltiRecordMatrix(a, b, epsilon, horizon) {
  return Array.from({ length: horizon }, (_, t) => [a ** t, epsilon * (b ** t)]);
}

function matVec2(matrix, vector) {
  return matrix.map((row) => dot(row, vector));
}

function observerGain(a, b, epsilon, p1 = 0.2, p2 = 0.3) {
  const s = p1 + p2;
  const p = p1 * p2;
  const det = epsilon * (a - b);
  if (Math.abs(det) < 1e-9) return null;
  const mat = [
    [1, epsilon],
    [b, a * epsilon],
  ];
  const rhs = [a + b - s, a * b - p];
  const inv = inverse2(mat);
  if (!inv) return null;
  return matVec(inv, rhs);
}

function inverse2(matrix) {
  if (matrix.length !== 2 || matrix[0].length !== 2) return null;
  const [[a, b], [c, d]] = matrix;
  const det = a * d - b * c;
  if (Math.abs(det) < 1e-9) return null;
  return [
    [d / det, -b / det],
    [-c / det, a / det],
  ];
}

function controlContinuousCollisionGap(epsilon, horizon) {
  if (horizon >= 2 && Math.abs(epsilon) > 1e-9) {
    return 0;
  }
  return 2;
}

function analyzeTwoStateControlRecoverability(config) {
  const a = 0.95;
  const b = 0.65;
  const epsilon = Number(config.controlEpsilon);
  const horizon = Number(config.controlHorizon);
  const recordMatrix = ltiRecordMatrix(a, b, epsilon, horizon);
  const deltas = Array.from({ length: 40 }, (_, index) => (index * 2.5) / 39);
  const states = [];
  const observations = [];
  const protectedValues = [];
  const errors = [];
  const coeffs = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1];
  const exact = horizon >= 2 && Math.abs(epsilon * (a - b)) > 1e-9;
  for (const x1 of coeffs) {
    for (const x2 of coeffs) {
      const state = [x1, x2];
      states.push(state);
      const record = matVec2(recordMatrix, state);
      const protectedValue = [x2];
      observations.push(record);
      protectedValues.push(protectedValue);
      let estimate = [0];
      if (exact) {
        estimate = [(a * record[0] - record[1]) / (epsilon * (a - b))];
      }
      errors.push(Math.abs(estimate[0] - x2));
    }
  }
  const collapse = collapseFromSamples(observations, protectedValues, deltas, rmsMetric, scalarGap);
  const kappa0 = controlContinuousCollisionGap(epsilon, horizon);
  const selectedDelta = clamp(Number(config.controlDelta), 0, 2.5);
  const selectedKappa = collapseAtDeltaFromSamples(observations, protectedValues, selectedDelta, rmsMetric, scalarGap);
  const historyThreshold = [1, 2, 3].map((value) => ({
    horizon: value,
    kappa0: controlContinuousCollisionGap(epsilon, value),
  }));
  let observerErrorHistory = [];
  let spectralRadius = null;
  const gain = observerGain(a, b, epsilon);
  if (gain) {
    let x = [1.2, -0.8];
    let xhat = [-0.4, 0.5];
    observerErrorHistory = [Math.abs(xhat[1] - x[1])];
    const closedLoop = [
      [a - gain[0], -gain[0] * epsilon],
      [-gain[1], b - gain[1] * epsilon],
    ];
    spectralRadius = maxEigenRadius2(closedLoop);
    for (let step = 0; step < 18; step += 1) {
      const y = x[0] + epsilon * x[1];
      const yhat = xhat[0] + epsilon * xhat[1];
      x = [a * x[0], b * x[1]];
      xhat = [a * xhat[0] + gain[0] * (y - yhat), b * xhat[1] + gain[1] * (y - yhat)];
      observerErrorHistory.push(Math.abs(xhat[1] - x[1]));
    }
  }
  return {
    systemLabel: 'Two-state functional observability model',
    protectedLabel: 'second state coordinate x₂',
    observationLabel: `${horizon}-step scalar output history`,
    classification:
      Math.abs(epsilon) < 1e-9
        ? 'Impossible'
        : exact
          ? 'Exact from finite history'
          : 'Finite exact recovery fails; asymptotic observer remains available',
    exact,
    asymptotic: Boolean(gain),
    impossible: Math.abs(epsilon) < 1e-9,
    deltas,
    collapse,
    selectedDelta,
    selectedKappa,
    kappa0,
    meanRecoveryError: errors.reduce((sum, value) => sum + value, 0) / errors.length,
    maxRecoveryError: Math.max(...errors),
    observerErrorHistory,
    spectralRadius,
    historyThreshold,
  };
}

export function diagonalRecordMatrix(eigenvalues, sensorWeights, horizon) {
  return Array.from({ length: horizon }, (_, t) =>
    sensorWeights.map((weight, index) => weight * (eigenvalues[index] ** t))
  );
}

function activeSensorCount(sensorWeights) {
  return sensorWeights.filter((value) => Math.abs(value) > 1e-9).length;
}

export function solveLeastSquares(matrix, rhs) {
  const mt = transpose(matrix);
  const gram = matMul(mt, matrix);
  const inv = invertMatrix(gram);
  if (!inv) return null;
  return matVec(matMul(inv, mt), rhs);
}

function diagonalProtectedWeights(eigenvalues, sensorWeights, functionalName) {
  switch (functionalName) {
    case 'sensor_sum':
      return sensorWeights.slice();
    case 'first_moment':
      return sensorWeights.map((weight, index) => weight * eigenvalues[index]);
    case 'second_moment':
      return sensorWeights.map((weight, index) => weight * (eigenvalues[index] ** 2));
    case 'protected_coordinate':
    default:
      return [0, 0, 1];
  }
}

function diagonalFunctionalLabel(functionalName) {
  switch (functionalName) {
    case 'sensor_sum':
      return 'sensor-weighted state sum';
    case 'first_moment':
      return 'first sensor moment functional';
    case 'second_moment':
      return 'second sensor moment functional';
    case 'protected_coordinate':
    default:
      return 'third state coordinate x₃';
  }
}

function diagonalRecoveryWeights(eigenvalues, sensorWeights, protectedIndex, horizon) {
  const active = sensorWeights
    .map((value, index) => ({ value, index }))
    .filter((entry) => Math.abs(entry.value) > 1e-9);
  if (!active.some((entry) => entry.index === protectedIndex)) {
    return null;
  }
  if (horizon < active.length) {
    return null;
  }
  const vandermonde = active.map((entry) =>
    Array.from({ length: active.length }, (_, power) => eigenvalues[entry.index] ** power)
  );
  const targets = active.map((entry) => (entry.index === protectedIndex ? 1 / entry.value : 0));
  const inverse = invertMatrix(vandermonde);
  if (!inverse) return null;
  const leading = matVec(inverse, targets);
  return [...leading, ...Array.from({ length: horizon - leading.length }, () => 0)];
}

function diagonalFunctionalRecoveryWeights(eigenvalues, sensorWeights, protectedWeights, horizon) {
  const active = sensorWeights
    .map((value, index) => ({ value, index }))
    .filter((entry) => Math.abs(entry.value) > 1e-9);
  const inactiveProtected = protectedWeights.some(
    (value, index) => Math.abs(value) > 1e-9 && !active.some((entry) => entry.index === index)
  );
  if (inactiveProtected || !active.length) {
    return null;
  }
  const vandermonde = active.map((entry) =>
    Array.from({ length: horizon }, (_, power) => eigenvalues[entry.index] ** power)
  );
  const targets = active.map((entry) => protectedWeights[entry.index] / entry.value);
  const coeffs = solveLeastSquares(vandermonde, targets);
  if (!coeffs) return null;
  const residual = norm(subVec(matVec(vandermonde, coeffs), targets));
  return residual < 1e-8 ? coeffs : null;
}

function invertMatrix(matrix) {
  const n = matrix.length;
  const augmented = matrix.map((row, i) => [...row, ...identity(n)[i]]);
  const { matrix: reduced, pivots } = rref(augmented);
  if (pivots.length < n) return null;
  return reduced.map((row) => row.slice(n));
}

function analyzeDiagonalControlComplexity(config) {
  const eigenvalues = [0.95, 0.8, 0.65];
  const profiles = {
    three_active: [1.0, 0.4, 0.2],
    two_active: [1.0, 0.0, 0.2],
    protected_hidden: [1.0, 0.4, 0.0],
  };
  const profileKey = config.controlProfile;
  const sensorWeights = profiles[profileKey];
  const functionalName = config.controlFunctional ?? 'protected_coordinate';
  const protectedWeights = diagonalProtectedWeights(eigenvalues, sensorWeights, functionalName);
  const horizon = Number(config.controlHorizon);
  const recordMatrix = diagonalRecordMatrix(eigenvalues, sensorWeights, horizon);
  const deltas = Array.from({ length: 40 }, (_, index) => (index * 2) / 39);
  const coeffs = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1];
  const observations = [];
  const protectedValues = [];
  const errors = [];
  const activeCount = activeSensorCount(sensorWeights);
  let predictedMinHorizon = null;
  for (let value = 1; value <= 4; value += 1) {
    if (diagonalFunctionalRecoveryWeights(eigenvalues, sensorWeights, protectedWeights, value)) {
      predictedMinHorizon = value;
      break;
    }
  }
  const exact = predictedMinHorizon !== null && horizon >= predictedMinHorizon;
  const weights = diagonalFunctionalRecoveryWeights(eigenvalues, sensorWeights, protectedWeights, horizon);
  for (const x1 of coeffs) {
    for (const x2 of coeffs) {
      for (const x3 of coeffs) {
        const state = [x1, x2, x3];
        const record = matVec2(recordMatrix, state);
        const protectedValue = [dot(protectedWeights, state)];
        observations.push(record);
        protectedValues.push(protectedValue);
        const estimate = weights ? [dot(weights, record)] : [0];
        errors.push(Math.abs(estimate[0] - protectedValue[0]));
      }
    }
  }
  const collapse = collapseFromSamples(observations, protectedValues, deltas, rmsMetric, scalarGap);
  const kappa0 = exact ? 0 : 2;
  const selectedDelta = clamp(Number(config.controlDelta), 0, 2);
  const selectedKappa = collapseAtDeltaFromSamples(observations, protectedValues, selectedDelta, rmsMetric, scalarGap);
  const historyThreshold = [1, 2, 3, 4].map((value) => ({
    horizon: value,
    kappa0: diagonalFunctionalRecoveryWeights(eigenvalues, sensorWeights, protectedWeights, value) ? 0 : 2,
  }));
  return {
    systemLabel: 'Three-state diagonal scalar-output family',
    protectedLabel: diagonalFunctionalLabel(functionalName),
    observationLabel: `${horizon}-step history (${profileKey.replaceAll('_', ' ')})`,
    classification:
      predictedMinHorizon === null
        ? 'Impossible because the protected functional does not lie in the finite-history row space'
        : exact
          ? `Exact once the record horizon reaches ${predictedMinHorizon}`
          : `Impossible below the minimal horizon ${predictedMinHorizon}`,
    exact,
    asymptotic: false,
    impossible: predictedMinHorizon === null || !exact,
    deltas,
    collapse,
    selectedDelta,
    selectedKappa,
    kappa0,
    meanRecoveryError: errors.reduce((sum, value) => sum + value, 0) / errors.length,
    maxRecoveryError: Math.max(...errors),
    observerErrorHistory: [],
    spectralRadius: null,
    historyThreshold,
    predictedMinHorizon,
    activeSensorCount: activeCount,
    controlModeLabel: 'minimal-history threshold model',
    functionalName,
  };
}

function analyzeControlRecoverability(config) {
  if (config.controlMode === 'diagonal_threshold') {
    return analyzeDiagonalControlComplexity(config);
  }
  const base = analyzeTwoStateControlRecoverability(config);
  return {
    ...base,
    controlModeLabel: 'two-state observer model',
    predictedMinHorizon: Math.abs(config.controlEpsilon) < 1e-9 ? null : 2,
    activeSensorCount: Math.abs(config.controlEpsilon) < 1e-9 ? 1 : 2,
  };
}


function linearTemplateFamily() {
  const coeffs = [-1, -0.5, 0, 0.5, 1];
  const family = [];
  for (const x1 of coeffs) {
    for (const x2 of coeffs) {
      for (const x3 of coeffs) {
        family.push([x1, x2, x3]);
      }
    }
  }
  return family;
}

function linearTemplateActiveCandidates(config) {
  const template = LINEAR_TEMPLATE_LIBRARY[config.linearTemplate] ?? LINEAR_TEMPLATE_LIBRARY.sensor_basis;
  return template.candidates.filter((candidate) => config.linearMeasurements?.[candidate.id]);
}

function linearRowRecoverableWeights(observationRows, protectedRow) {
  if (!observationRows.length) return null;
  const coeffs = solveLeastSquares(transpose(observationRows), protectedRow);
  if (!coeffs) return null;
  const reconstructed = Array(observationRows[0].length).fill(0);
  observationRows.forEach((row, index) => {
    for (let j = 0; j < row.length; j += 1) {
      reconstructed[j] += coeffs[index] * row[j];
    }
  });
  return norm(subVec(reconstructed, protectedRow)) < 1e-8 ? coeffs : null;
}

function linearTemplateProtectedValue(state, rows) {
  return rows.map((row) => dot(row, state));
}

function analyzeLinearTemplateRecoverability(config) {
  const template = LINEAR_TEMPLATE_LIBRARY[config.linearTemplate] ?? LINEAR_TEMPLATE_LIBRARY.sensor_basis;
  const family = linearTemplateFamily();
  const active = linearTemplateActiveCandidates(config);
  const activeRows = active.map((candidate) => candidate.row);
  const remainingCandidates = template.candidates.filter((candidate) => !config.linearMeasurements?.[candidate.id]);
  const protectedOption = template.protectedOptions[config.linearProtected] ?? template.protectedOptions.x3;
  const protectedRows = protectedOption.rows.map((row) => row.slice());
  const { residuals, recoverable, unrecoverable } = recoverableRowIndices(activeRows, protectedRows);
  const exact = unrecoverable.length === 0;
  const rankObservation = activeRows.length ? matrixRank(activeRows) : 0;
  const rankProtected = matrixRank(protectedRows);
  const unrestrictedMinimalAdded = Math.max(0, matrixRank([...activeRows, ...protectedRows]) - matrixRank(activeRows.length ? activeRows : [zeros(3)]));
  const augmentation = minimalRowAugmentation(activeRows, protectedRows, remainingCandidates.map((candidate) => candidate.row));
  const nullBasis = nullSpace(activeRows.length ? activeRows : [zeros(3)]);
  let witness = null;
  let witnessGap = 0;
  for (const vector of nullBasis) {
    const scaled = scaleVec(vector, 1 / Math.max(...vector.map((value) => Math.abs(value)), 1));
    const gap = norm(linearTemplateProtectedValue(scaled, protectedRows));
    if (gap > witnessGap + 1e-9) {
      witness = scaled;
      witnessGap = gap;
    }
  }

  const deltas = Array.from({ length: 40 }, (_, index) => (index * 2.5) / 39);
  const observations = [];
  const protectedValues = [];
  const errors = [];
  const rowMetric = protectedRows.length === 1 ? scalarGap : rmsMetric;
  let recoveryMatrix = null;
  let stabilitySlopeUpper = null;
  if (exact) {
    recoveryMatrix = protectedRows.map((row) => {
      const weights = linearRowRecoverableWeights(activeRows, row);
      return weights ?? Array.from({ length: activeRows.length }, () => 0);
    });
    stabilitySlopeUpper = frobeniusNorm(recoveryMatrix);
  }
  for (const state of family) {
    const observation = activeRows.map((row) => dot(row, state));
    const protectedValue = linearTemplateProtectedValue(state, protectedRows);
    observations.push(observation);
    protectedValues.push(protectedValue);
    let estimate = Array.from({ length: protectedRows.length }, () => 0);
    if (exact && recoveryMatrix) {
      estimate = recoveryMatrix.map((weights) => dot(weights, observation));
    }
    errors.push(rowMetric(estimate, protectedValue));
  }

  const collapse = collapseFromSamples(observations, protectedValues, deltas, rmsMetric, rowMetric);
  const kappa0 = fiberCollisionGap(observations, protectedValues, rmsMetric, rowMetric);
  const selectedDelta = clamp(Number(config.linearDelta ?? 1), 0, 2.5);
  const selectedKappa = collapseAtDeltaFromSamples(observations, protectedValues, selectedDelta, rmsMetric, rowMetric);
  const recoverableOptions = Object.entries(template.protectedOptions)
    .map(([key, value]) => ({
      key,
      label: value.label,
      exact: recoverableRowIndices(activeRows, value.rows).unrecoverable.length === 0,
    }))
    .filter((item) => item.exact);

  return {
    systemLabel: template.label,
    protectedLabel: protectedOption.label,
    observationLabel: active.length ? active.map((candidate) => candidate.label).join(', ') : 'no measurements selected',
    classification: exact
      ? 'Exact under the current static record'
      : augmentation.minimalAdded !== null
        ? `Impossible now; exact after ${augmentation.minimalAdded} added measurement${augmentation.minimalAdded === 1 ? '' : 's'}`
        : unrestrictedMinimalAdded > 0
          ? 'Impossible under the current candidate record family'
          : 'Impossible under the current static record',
    exact,
    asymptotic: false,
    impossible: !exact,
    deltas,
    collapse,
    selectedDelta,
    selectedKappa,
    kappa0,
    meanRecoveryError: errors.reduce((sum, value) => sum + value, 0) / errors.length,
    maxRecoveryError: Math.max(...errors),
    rankObservation,
    rankProtected,
    activeMeasurementLabels: active.map((candidate) => candidate.label),
    remainingMeasurementLabels: remainingCandidates.map((candidate) => candidate.label),
    recoverableProtectedRows: recoverable,
    unrecoverableProtectedRows: unrecoverable,
    rowResiduals: residuals,
    weakerProtectedOptions: recoverableOptions.map((item) => item.label),
    weakerProtectedChoices: recoverableOptions,
    unrestrictedMinimalAddedMeasurements: unrestrictedMinimalAdded,
    minimalAddedMeasurements: augmentation.minimalAdded,
    stabilitySlopeUpper,
    selectedStabilityUpperBound: stabilitySlopeUpper === null ? null : stabilitySlopeUpper * selectedDelta,
    candidateExactSets: augmentation.exactSets.map((combo) => combo.map((index) => remainingCandidates[index].label)),
    candidateExactIds: augmentation.exactSets.map((combo) => combo.map((index) => remainingCandidates[index].id)),
    nullspaceWitness: witness,
    nullspaceWitnessGap: witnessGap,
    templateProtectedOptions: Object.values(template.protectedOptions).map((item) => item.label),
  };
}

function maxEigenRadius2(matrix) {
  const [[a, b], [c, d]] = matrix;
  const trace = a + d;
  const det = a * d - b * c;
  const disc = Math.max(trace * trace - 4 * det, 0);
  const sqrtDisc = Math.sqrt(disc);
  const lam1 = (trace + sqrtDisc) / 2;
  const lam2 = (trace - sqrtDisc) / 2;
  return Math.max(Math.abs(lam1), Math.abs(lam2));
}

function analyzeAnalyticRecoverability(config) {
  const epsilon = Math.abs(Number(config.analyticEpsilon));
  const deltas = Array.from({ length: 40 }, (_, index) => index / 39);
  const collapse = deltas.map((delta) => (epsilon < 1e-9 ? 2 : Math.min(2, delta / epsilon)));
  const noiseLowerBounds = collapse.map((value) => 0.5 * value);
  const selectedDelta = clamp(Number(config.analyticDelta), 0, 1);
  const selectedKappa = epsilon < 1e-9 ? 2 : Math.min(2, selectedDelta / epsilon);
  const selectedLowerBound = 0.5 * selectedKappa;
  return {
    systemLabel: 'Analytic benchmark Mε(u,v) = (u, εv)',
    protectedLabel: 'protected scalar v',
    observationLabel: 'coarse two-coordinate record',
    classification: epsilon < 1e-9 ? 'Impossible' : 'Exact with explicit stability loss',
    exact: epsilon >= 1e-9,
    asymptotic: false,
    impossible: epsilon < 1e-9,
    deltas,
    collapse,
    noiseLowerBounds,
    selectedDelta,
    selectedKappa,
    selectedLowerBound,
    kappa0: epsilon < 1e-9 ? 2 : 0,
    meanRecoveryError: 0,
    maxRecoveryError: 0,
    epsilon,
    amplification: epsilon < 1e-9 ? Infinity : 1 / epsilon,
  };
}

function analyzeBoundaryRecoverability(config) {
  const architecture = config.boundaryArchitecture ?? 'periodic_transplant';
  const protectedTarget = config.boundaryProtected ?? 'bounded_velocity_class';
  const gridSize = Math.max(Number(config.boundaryGridSize ?? 17), 9);
  const transplant = analyzeBoundaryProjectionLimit({ gridSize, poissonIterations: 320 });
  const compatible = analyzeBoundedHodgeCompatible({ gridSize: Math.max(gridSize, 17) });
  const selectedDelta = clamp(Number(config.boundaryDelta ?? 0.2), 0, 1);
  const deltas = Array.from({ length: 40 }, (_, index) => index / 39);
  const strongTarget = protectedTarget === 'bounded_velocity_class';
  const exact = architecture === 'boundary_compatible_hodge' || (!strongTarget && architecture === 'periodic_transplant');
  const impossible = architecture === 'periodic_transplant' && strongTarget;
  const kappa0 = exact ? 0 : transplant.projectedBoundaryNormalRms;
  const collapse = deltas.map(() => kappa0);
  const weakerTargets = strongTarget ? ['bulk divergence certificate only'] : [];
  return {
    systemLabel: 'Bounded-domain projection architecture benchmark',
    protectedLabel: strongTarget ? 'bounded velocity class with boundary compatibility' : 'bulk divergence certificate only',
    observationLabel: architecture === 'boundary_compatible_hodge' ? 'boundary-compatible finite-mode Hodge projector' : 'periodic projector transplanted to a bounded domain',
    classification:
      architecture === 'boundary_compatible_hodge'
        ? 'Exact on the restricted boundary-compatible finite-mode family'
        : strongTarget
          ? 'Impossible for the strong bounded target under the transplanted architecture'
          : 'Exact only for the weaker divergence certificate',
    exact,
    asymptotic: false,
    impossible,
    deltas,
    collapse,
    selectedDelta,
    selectedKappa: kappa0,
    kappa0,
    meanRecoveryError:
      architecture === 'boundary_compatible_hodge'
        ? compatible.recoveryError
        : strongTarget
          ? transplant.projectedBoundaryNormalRms
          : transplant.afterNorm,
    maxRecoveryError:
      architecture === 'boundary_compatible_hodge'
        ? compatible.recoveryError
        : strongTarget
          ? transplant.projectedBoundaryNormalRms
          : transplant.afterNorm,
    boundaryArchitecture: architecture,
    boundaryProtectedTarget: protectedTarget,
    weakerBoundaryTargets: weakerTargets,
    boundaryArchitectureSeries: [
      { x: 0, y: strongTarget ? transplant.projectedBoundaryNormalRms : transplant.afterNorm, label: 'transplant' },
      { x: 1, y: strongTarget ? compatible.recoveryError : compatible.recoveredDivNorm, label: 'compatible' },
    ],
    transplantBeforeDiv: transplant.beforeNorm,
    transplantAfterDiv: transplant.afterNorm,
    transplantBoundaryMismatch: transplant.projectedBoundaryNormalRms,
    transplantPhysicalBoundaryNormalRms: transplant.physicalBoundaryNormalRms,
    compatibleProtectedDivNorm: compatible.protectedDivNorm,
    compatibleRecoveredDivNorm: compatible.recoveredDivNorm,
    compatibleBoundaryMismatch: compatible.recoveredBoundaryNormalRms,
    compatibleProtectedBoundaryNormalRms: compatible.protectedBoundaryNormalRms,
    compatibleRecoveryError: compatible.recoveryError,
    compatibleOrthogonalityResidual: compatible.orthogonalityResidual,
    compatibleIdempotenceError: compatible.idempotenceError,
    compatibleProjectorConstructionAgreement: compatible.projectorConstructionAgreement,
  };
}

function recoverabilityStatusLabel(result) {
  if (result.exact) return 'Exact';
  if (result.asymptotic) return 'Asymptotic';
  if (result.impossible) return 'Impossible';
  return 'Approximate';
}

function cloneValue(value) {
  return JSON.parse(JSON.stringify(value));
}

export function mergeRecoverabilityConfig(config, patch) {
  const next = cloneValue(config);
  for (const [key, value] of Object.entries(patch ?? {})) {
    if (value && typeof value === 'object' && !Array.isArray(value) && typeof next[key] === 'object' && next[key] !== null && !Array.isArray(next[key])) {
      next[key] = { ...next[key], ...value };
    } else {
      next[key] = value;
    }
  }
  return next;
}

function periodicProtectedOptions() {
  return [
    { key: 'mode_1_coefficient', label: 'leading modal coefficient', threshold: 1 },
    { key: 'modes_1_2_coefficients', label: 'first two modal coefficients', threshold: 2 },
    { key: 'low_mode_sum', label: 'low-mode weighted sum', threshold: 2 },
    { key: 'bandlimited_contrast', label: 'band-limited contrast functional', threshold: 3 },
    { key: 'full_weighted_sum', label: 'full weighted modal sum', threshold: 4 },
    { key: 'full_modal_coefficients', label: 'full four-mode coefficient vector', threshold: 4 },
  ];
}

function controlFunctionalOptions() {
  return [
    { key: 'sensor_sum', label: 'sensor-weighted state sum' },
    { key: 'first_moment', label: 'first sensor moment functional' },
    { key: 'second_moment', label: 'second sensor moment functional' },
    { key: 'protected_coordinate', label: 'third coordinate x₃' },
  ];
}

function periodicWeakerSuggestions(cutoff) {
  return periodicProtectedOptions().filter((option) => cutoff >= option.threshold).map((option) => option.label);
}

function guidanceForRecoverability(result, config) {
  switch (config.system) {
    case 'analytic': {
      if (result.exact) {
        return {
          architecture: 'Static exact recovery with noise-budget control',
          blocker: 'No structural blocker is present, but the record becomes poorly conditioned as ε shrinks.',
          missing: result.amplification > 6 ? 'Increase ε or reduce tolerated record noise before treating the setup as robust.' : 'Current record is sufficient for exact recovery on the chosen family.',
          nextSteps: [
            `Keep ε away from zero; the current amplification factor is ${Number.isFinite(result.amplification) ? result.amplification.toFixed(2) : '∞'}.`,
            'Use κ(η)/2 to decide whether the current noise budget is acceptable.',
            'If robustness matters more than exactness, redesign the record before changing the protected variable.',
          ],
          weaker: [],
          noGo: null,
        };
      }
      return {
        architecture: 'No static recovery under the current record',
        blocker: 'The record collapses the protected scalar completely when ε = 0.',
        missing: 'Any nonzero coupling to the protected coordinate would restore exact recoverability on this family.',
        nextSteps: [
          'Add direct sensitivity to the protected coordinate.',
          'Do not switch to an observer here; the issue is missing information, not missing time dynamics.',
        ],
        weaker: [],
        noGo: 'Fiber collision at κ(0) > 0',
      };
    }
    case 'qubit': {
      if (result.exact) {
        return {
          architecture: 'Static exact recovery on the restricted family',
          blocker: 'None on the current protected variable and phase family.',
          missing: 'The fixed-basis record is already sufficient for the chosen weaker protected variable.',
          nextSteps: [
            'Keep the protected target weak if you want to stay with a fixed-basis record.',
            'If you need the full Bloch vector, add another measurement basis rather than over-interpreting the current record.',
          ],
          weaker: result.protectedLabel === 'z coordinate only' ? [] : ['z coordinate only'],
          noGo: result.exact ? null : 'Fixed-basis phase-loss no-go',
        };
      }
      return {
        architecture: 'Richer measurement family required',
        blocker: 'Phase freedom creates fiber collisions under the fixed-basis record.',
        missing: 'Add at least one complementary measurement basis or restrict the admissible state family to a meridian.',
        nextSteps: [
          'Add X/Y-sensitive observables if you need the full Bloch vector.',
          'If the record must stay fixed-basis, weaken the protected variable to the z coordinate.',
        ],
        weaker: ['z coordinate only'],
        noGo: 'Fixed-basis phase-loss no-go',
      };
    }
    case 'periodic': {
      if (result.exact) {
        return {
          architecture: 'Static exact recovery from projection-compatible periodic records',
          blocker: 'No structural blocker on the current finite modal family.',
          missing: 'Current retained modal support is sufficient.',
          nextSteps: [
            'If you enlarge the protected variable, recheck the protected-support cutoff.',
            'If you move to bounded domains, do not reuse this verdict without a boundary-compatible projector.',
          ],
          weaker: periodicWeakerSuggestions(result.currentCutoff).filter((label) => label !== result.protectedLabel),
          noGo: null,
        };
      }
      if (config.periodicObservation === 'divergence_only') {
        return {
          architecture: 'Switch to a richer record family',
          blocker: 'Divergence-only data leave nontrivial incompressible states indistinguishable.',
          missing: 'Add vorticity or another record that separates the protected modal content.',
          nextSteps: [
            'Move from divergence-only data to cutoff or full vorticity.',
            'If bandwidth is limited, lower the protected target to a variable with smaller modal support.',
          ],
          weaker: periodicWeakerSuggestions(0),
          noGo: 'Divergence-only no-go',
        };
      }
      return {
        architecture: 'Increase retained record complexity',
        blocker: 'The retained cutoff misses part of the protected modal support.',
        missing: `Raise the cutoff from ${result.currentCutoff} to at least ${result.predictedMinCutoff}.`,
        nextSteps: [
          `Increase the cutoff to ${result.predictedMinCutoff} for exact recovery of the current protected variable.`,
          'If that cost is too high, weaken the protected variable to one supported on the retained modes.',
        ],
        weaker: periodicWeakerSuggestions(result.currentCutoff).filter((label) => label !== result.protectedLabel),
        noGo: 'Protected-support cutoff law',
      };
    }
    case 'control': {
      if (result.exact) {
        return {
          architecture: 'Static finite-history recovery',
          blocker: 'No exactness blocker remains at the current horizon.',
          missing: 'Current history length is sufficient for the chosen protected variable.',
          nextSteps: [
            'Keep the current horizon if you only need static recovery from batched records.',
            'Switch to an observer only if you need online estimation rather than finite-history reconstruction.',
          ],
          weaker: [],
          noGo: null,
        };
      }
      if (result.asymptotic) {
        return {
          architecture: 'Observer / asymptotic recovery',
          blocker: 'Finite-history exact recovery fails at the current horizon even though the dynamic record remains informative.',
          missing: `Either extend the horizon to ${result.predictedMinHorizon ?? 2} or switch to observer-style recovery.`,
          nextSteps: [
            `Increase the finite history to ${result.predictedMinHorizon ?? 2} for exact static recovery.`,
            'If latency matters more than exact one-shot reconstruction, use an observer and monitor spectral radius.',
          ],
          weaker: [],
          noGo: 'Finite-history insufficiency with observer-side asymptotic rescue',
        };
      }
      return {
        architecture: 'Increase horizon or weaken the protected functional',
        blocker: result.predictedMinHorizon === null
          ? 'The current sensor profile never spans the chosen protected functional.'
          : 'The finite history is too short to interpolate the protected functional.',
        missing: result.predictedMinHorizon === null
          ? 'Change the sensor profile or choose a weaker protected functional generated by the sensed moments.'
          : `Increase the horizon to at least ${result.predictedMinHorizon}.`,
        nextSteps: result.predictedMinHorizon === null
          ? ['Switch to sensor_sum or first_moment if those fit the real task better.', 'Otherwise add a sensor that directly touches the hidden protected direction.']
          : [`Extend the history to ${result.predictedMinHorizon}.`, 'If that is not possible, weaken the protected target to one of the lower-moment functionals.'],
        weaker: result.controlModeLabel === 'minimal-history threshold model' ? ['sensor-weighted state sum', 'first sensor moment functional'] : [],
        noGo: result.predictedMinHorizon === null ? 'Hidden protected-direction no-go' : 'Minimal-history threshold law',
      };
    }
    case 'linear': {
      return {
        architecture: result.exact ? 'Static linear recovery' : 'Augment the record or weaken the protected variable',
        blocker: result.exact
          ? 'No structural blocker remains on the current protected rows; exactness comes from row-space alignment, not from rank alone.'
          : result.nullspaceWitness
            ? `A nullspace witness still changes the protected variable by ${result.nullspaceWitnessGap.toFixed(2)} while leaving the record fixed.`
            : 'The current record row space does not contain every protected row.',
        missing: result.exact
          ? 'Current measurement rows span the protected target, so the exact branch also has a computable linear stability envelope.'
          : result.minimalAddedMeasurements === null
            ? `No exact fix exists inside the current candidate measurement library. The theorem-backed unrestricted minimum is ${result.unrestrictedMinimalAddedMeasurements}.`
            : `Add ${result.minimalAddedMeasurements} measurement${result.minimalAddedMeasurements === 1 ? '' : 's'} from the candidate library.`,
        nextSteps: result.exact
          ? [
              `At the selected δ, the current computable upper bound on protected-variable ambiguity is ${result.selectedStabilityUpperBound?.toExponential(2) ?? '0.00e+0'}.`,
              'Export this scenario as a reusable exact-recovery template.',
              'If robustness matters, enlarge the admissible family and retest.'
            ]
          : [
              result.candidateExactSets.length
                ? `Try one of the minimal fixes: ${result.candidateExactSets.map((set) => set.join(' + ')).join(' or ')}.`
                : 'Rethink the measurement library; the current candidates cannot support exact recovery.',
              result.weakerProtectedOptions.length
                ? `If the full target is too expensive, a weaker recoverable target already exists: ${result.weakerProtectedOptions.join(', ')}.`
                : 'There is no weaker recoverable option in the current protected menu.',
            ],
        weaker: result.weakerProtectedOptions.filter((label) => label !== result.protectedLabel),
        noGo: result.exact ? null : 'Restricted-linear row-space insufficiency',
      };
    }
    case 'boundary': {
      if (result.exact) {
        return {
          architecture: result.boundaryArchitecture === 'boundary_compatible_hodge'
            ? 'Boundary-compatible exact projector'
            : 'Keep the weak divergence-only target',
          blocker: 'No structural blocker remains for the current target on the chosen bounded-domain architecture.',
          missing: result.boundaryArchitecture === 'boundary_compatible_hodge'
            ? 'The current boundary-compatible finite-mode projector respects both divergence and the bounded protected class.'
            : 'The current transplanted architecture is only acceptable because the protected target has been weakened to a bulk divergence certificate.',
          nextSteps: [
            result.boundaryArchitecture === 'boundary_compatible_hodge'
              ? 'Keep the boundary-compatible basis if you want an honest exact bounded-domain statement.'
              : 'Only keep this weaker target if a divergence certificate is all the application really needs.',
            'If you enlarge the bounded family, rerun the compatibility checks rather than assuming the same projector still fits.',
          ],
          weaker: result.weakerBoundaryTargets ?? [],
          noGo: null,
        };
      }
      return {
        architecture: 'Switch to a boundary-compatible bounded-domain architecture',
        blocker: 'The periodic projector removes divergence but leaves the bounded protected class because the projected field picks up the wrong boundary-normal trace.',
        missing: 'Use the restricted boundary-compatible finite-mode Hodge family for exact recovery, or weaken the target to a bulk divergence certificate.',
        nextSteps: [
          'Switch from the periodic transplant to the boundary-compatible Hodge projector on the restricted finite-mode family.',
          'If the application only needs bulk incompressibility and not the full bounded protected class, weaken the target to a divergence certificate.',
        ],
        weaker: result.weakerBoundaryTargets ?? ['bulk divergence certificate only'],
        noGo: 'Bounded-domain projector transplant failure',
      };
    }
    default:
      return {
        architecture: 'Use the current branch classification',
        blocker: 'No additional guidance available.',
        missing: 'Inspect κ(0), the threshold plots, and the no-go layer.',
        nextSteps: ['Use the theory links and outside literature cards to refine the model.'],
        weaker: [],
        noGo: null,
      };
  }
}

function theoremStatusForRecoverability(result, config) {
  switch (config.system) {
    case 'analytic':
      return result.exact ? 'Explicit analytic exactness / stability toy model' : 'Analytic impossibility witness on the degenerate record';
    case 'qubit':
      return result.exact ? 'Family-specific weaker-target split' : 'Family-specific phase-loss no-go with standard measurement enrichment outside the current theorem spine';
    case 'periodic':
      return config.periodicObservation === 'divergence_only'
        ? 'Theorem-backed no-go plus family-specific periodic support thresholds'
        : 'Family-specific periodic threshold result with repeated falsification';
    case 'control':
      return result.controlModeLabel === 'minimal-history threshold model'
        ? 'Family-specific finite-history threshold law with interpolation checks'
        : 'Mixed exact / asymptotic control benchmark';
    case 'linear':
      return 'Restricted-linear theorem-backed design and augmentation spine';
    case 'boundary':
      return result.boundaryArchitecture === 'boundary_compatible_hodge'
        ? 'Restricted exact bounded-domain Hodge theorem on the finite-mode family'
        : 'Theorem-backed bounded-domain transplant failure with restricted exact repair path';
    default:
      return 'Recoverability branch diagnostic';
  }
}

function scopeLabelForRecoverability(result, config) {
  switch (config.system) {
    case 'analytic':
      return result.exact ? 'exact / analytic toy family / theorem-linked' : 'impossible / analytic toy witness';
    case 'qubit':
      return result.exact ? 'exact / weaker-target only / family-restricted' : 'impossible / family-specific phase-loss no-go';
    case 'periodic':
      if (config.periodicObservation === 'divergence_only') {
        return result.exact ? 'exact / weaker-target only / family-restricted' : 'impossible / theorem-backed divergence-only no-go';
      }
      return result.exact ? 'exact / family-specific threshold result' : 'impossible / family-specific threshold failure';
    case 'control':
      if (result.asymptotic) {
        return 'asymptotic / benchmark-backed / family-restricted';
      }
      return result.exact ? 'exact / family-specific threshold result' : 'impossible / family-specific threshold failure';
    case 'linear':
      return result.exact ? 'exact / theorem-backed / restricted linear family' : 'impossible / theorem-backed / restricted linear family';
    case 'boundary':
      if (result.exact && result.boundaryArchitecture === 'boundary_compatible_hodge') {
        return 'exact / theorem-backed / restricted bounded-domain family';
      }
      if (result.exact) {
        return 'exact / weaker-target only / family-restricted bounded-domain fallback';
      }
      return 'impossible / theorem-backed bounded-domain counterexample';
    default:
      return 'branch-classified result';
  }
}

function identifiabilityStatusForRecoverability(result, config, guidance) {
  if (result.exact) {
    return 'exactly identifiable target on the declared family';
  }
  if (result.asymptotic) {
    return 'not exactly identifiable from the current finite record, but asymptotically recoverable under the continuing observer architecture';
  }
  if (guidance.weaker?.length) {
    return 'selected target is not identifiable on the current record, but a weaker/coarsened target is identifiable';
  }
  if (config.system === 'boundary' && config.boundaryProtected === 'bounded_velocity_class') {
    return 'strong bounded target is non-identifiable under the current architecture';
  }
  return 'target is non-identifiable on the current family and record';
}

function falsePositiveWarningsForRecoverability(result, config) {
  const warnings = [];
  switch (config.system) {
    case 'analytic':
      warnings.push('Family-restriction warning: this verdict is only certified on the current analytic toy family, not on arbitrary enlarged observation models.');
      break;
    case 'qubit':
      if (result.exact) {
        warnings.push('Target-strength warning: only the phase-insensitive z target is exact here; phase-sensitive Bloch targets remain mixed on the same measurement fibers.');
      } else {
        warnings.push('Family-restriction warning: this no-go is on the fixed-basis phase-window family, not on every enriched qubit measurement architecture.');
      }
      break;
    case 'periodic':
      warnings.push('Family-restriction warning: periodic exactness and threshold numbers here are certified only on the supported finite modal benchmark.');
      if (result.exact && config.periodicObservation !== 'divergence_only') {
        warnings.push('Discretization/refinement warning: enlarging the modal family or the protected support can destroy exactness even when the current cutoff looks sufficient on the present truncation.');
      }
      if (config.periodicObservation === 'divergence_only') {
        warnings.push('Target-strength warning: divergence-only success certifies only the weak divergence target, not full field recovery.');
      }
      break;
    case 'control':
      warnings.push('Family-restriction warning: the current control verdict is tied to the supported diagonal/history or observer benchmark, not a universal observability law.');
      if (result.asymptotic) {
        warnings.push('Regime warning: this architecture is asymptotic, not exact, on the current record.');
      }
      if (result.weakerRecoverableTargets?.length) {
        warnings.push('Target-strength warning: weaker protected functionals may already be exact even though the selected stronger target fails at the current horizon.');
      }
      break;
    case 'linear':
      warnings.push('Family-restriction warning: the current verdict is certified only on the declared restricted linear family.');
      warnings.push('Anti-classifier warning: same rank, same sensor count, or the same candidate-library budget can still produce the opposite exactness verdict on a different sensor geometry.');
      if (result.exact) {
        warnings.push('Family-enlargement warning: enlarging the admissible family can reintroduce hidden target-changing fiber directions and invalidate this exact decoder.');
      }
      warnings.push('Model-mismatch warning: a decoder exact on one restricted family can drift on a nearby structurally different family even when the true family remains exactly recoverable.');
      if (!result.exact && result.weakerProtectedOptions?.length) {
        warnings.push('Target-strength warning: some weaker protected targets are already exact even though the currently selected stronger target fails.');
      }
      break;
    case 'boundary':
      warnings.push('Family-restriction warning: bounded-domain claims here apply only on the restricted compatible family and tested architecture.');
      if (result.exact && result.boundaryArchitecture !== 'boundary_compatible_hodge') {
        warnings.push('Target-strength warning: this success is only for the weakened divergence certificate, not for the strong bounded protected class.');
      }
      if (!result.exact) {
        warnings.push('Wrong-architecture warning: reducing divergence alone is not enough when boundary trace remains fiber-mixed.');
      }
      break;
    default:
      break;
  }
  return Array.from(new Set(warnings));
}

function recommendationsForRecoverability(result, config) {
  switch (config.system) {
    case 'analytic': {
      if (result.exact) {
        return [
          {
            id: 'keep-analytic',
            title: 'Keep current record',
            actionKind: 'keep',
            theoremStatus: theoremStatusForRecoverability(result, config),
            rationale: 'The current analytic record already separates the protected scalar on the chosen family; only robustness tuning remains.',
            minimal: true,
            expectedRegime: 'exact',
            patch: {},
            availableInStudio: true,
          },
        ];
      }
      return [
        {
          id: 'add-coupling',
          title: 'Add nonzero protected-coordinate coupling',
          actionKind: 'add_measurement',
          theoremStatus: 'Analytic exactness criterion on the toy family',
          rationale: 'Any nonzero coupling to the protected coordinate restores exact recoverability on this analytic family.',
          minimal: true,
          expectedRegime: 'exact',
          patch: { analyticEpsilon: 0.1 },
          availableInStudio: true,
        },
      ];
    }
    case 'qubit': {
      if (result.exact) {
        return [
          {
            id: 'keep-qubit',
            title: 'Keep current protected target',
            actionKind: 'keep',
            theoremStatus: theoremStatusForRecoverability(result, config),
            rationale: 'The fixed-basis record already preserves the selected weaker target exactly on the current phase family.',
            minimal: true,
            expectedRegime: 'exact',
            patch: {},
            availableInStudio: true,
          },
        ];
      }
      return [
        {
          id: 'weaken-to-z',
          title: 'Weaken target to z coordinate only',
          actionKind: 'weaken_target',
          theoremStatus: 'Family-specific weaker-target split',
          rationale: 'The fixed-basis record keeps the phase-insensitive z coordinate exact even when the full Bloch vector collapses.',
          minimal: true,
          expectedRegime: 'exact',
          patch: { qubitProtected: 'z_coordinate' },
          availableInStudio: true,
        },
        {
          id: 'add-basis',
          title: 'Add a complementary basis',
          actionKind: 'switch_architecture',
          theoremStatus: 'Standard physics guidance outside the current theorem spine',
          rationale: 'Adding a complementary basis is the conventional way to recover phase-sensitive information, but this richer architecture is not yet proven in the repo.',
          minimal: false,
          expectedRegime: 'likely exact on the enlarged measurement family',
          patch: null,
          availableInStudio: false,
        },
      ];
    }
    case 'periodic': {
      if (result.exact) {
        return [
          {
            id: 'keep-periodic',
            title: 'Keep current periodic record',
            actionKind: 'keep',
            theoremStatus: theoremStatusForRecoverability(result, config),
            rationale: 'The current record already retains the full protected modal support for the chosen target.',
            minimal: true,
            expectedRegime: 'exact',
            patch: {},
            availableInStudio: true,
          },
        ];
      }
      const recommendations = [];
      if (config.periodicObservation === 'divergence_only') {
        recommendations.push({
          id: 'switch-to-cutoff-record',
          title: `Switch to cutoff-vorticity record at cutoff ${result.predictedMinCutoff}`,
          actionKind: 'switch_record',
          theoremStatus: 'Theorem-backed divergence-only no-go plus family-specific threshold law',
          rationale: 'The divergence-only record is structurally insufficient; a cutoff-vorticity record is the smallest supported exact architecture on this lane.',
          minimal: false,
          expectedRegime: 'exact',
          patch: { periodicObservation: 'cutoff_vorticity', periodicCutoff: result.predictedMinCutoff },
          availableInStudio: true,
        });
      } else {
        recommendations.push({
          id: 'raise-periodic-cutoff',
          title: `Raise cutoff to ${result.predictedMinCutoff}`,
          actionKind: 'add_mode',
          theoremStatus: theoremStatusForRecoverability(result, config),
          rationale: 'The current retained support misses part of the protected target; exact recovery begins at the first cutoff containing the whole protected support.',
          minimal: true,
          expectedRegime: 'exact',
          patch: { periodicCutoff: result.predictedMinCutoff },
          availableInStudio: true,
        });
      }
      const weaker = periodicProtectedOptions()
        .filter((option) => option.threshold <= (config.periodicObservation === 'divergence_only' ? 0 : result.currentCutoff))
        .filter((option) => option.label !== result.protectedLabel)
        .map((option) => ({
          id: `weaken-periodic-${option.key}`,
          title: `Weaken target to ${option.label}`,
          actionKind: 'weaken_target',
          theoremStatus: 'Family-specific periodic support threshold result',
          rationale: 'This weaker target already lives on the currently visible modal support.',
          minimal: false,
          expectedRegime: 'exact',
          patch: { periodicProtected: option.key },
          availableInStudio: true,
        }));
      return [...recommendations, ...weaker];
    }
    case 'control': {
      if (result.exact) {
        return [
          {
            id: 'keep-control',
            title: 'Keep current control architecture',
            actionKind: 'keep',
            theoremStatus: theoremStatusForRecoverability(result, config),
            rationale: 'The current finite-history or observer architecture already supports the chosen protected variable.',
            minimal: true,
            expectedRegime: result.asymptotic ? 'asymptotic' : 'exact',
            patch: {},
            availableInStudio: true,
          },
        ];
      }
      const recommendations = [];
      if (result.predictedMinHorizon !== null && Number(config.controlHorizon) < result.predictedMinHorizon) {
        recommendations.push({
          id: 'increase-control-horizon',
          title: `Increase horizon to ${result.predictedMinHorizon}`,
          actionKind: 'add_history',
          theoremStatus: theoremStatusForRecoverability(result, config),
          rationale: 'The current history is too short; exact recovery begins at the first horizon that interpolates the protected functional.',
          minimal: true,
          expectedRegime: 'exact',
          patch: { controlHorizon: result.predictedMinHorizon },
          availableInStudio: true,
        });
      }
      if (result.controlModeLabel === 'two-state observer model' && result.asymptotic) {
        recommendations.push({
          id: 'keep-observer-architecture',
          title: 'Switch to observer-style recovery',
          actionKind: 'switch_architecture',
          theoremStatus: 'Empirical/theorem-linked asymptotic control benchmark',
          rationale: 'Single-shot exact recovery fails at the current horizon, but the ongoing record still supports asymptotic observer convergence.',
          minimal: false,
          expectedRegime: 'asymptotic',
          patch: {},
          availableInStudio: true,
        });
      }
      const weaker = controlFunctionalOptions()
        .filter((option) => option.key !== config.controlFunctional)
        .filter((option) => guidanceForRecoverability(result, config).weaker.includes(option.label))
        .map((option) => ({
          id: `weaken-control-${option.key}`,
          title: `Weaken target to ${option.label}`,
          actionKind: 'weaken_target',
          theoremStatus: 'Family-specific control-side weaker-target split',
          rationale: 'The current record already spans this lower-complexity protected functional.',
          minimal: false,
          expectedRegime: 'exact',
          patch: { controlFunctional: option.key },
          availableInStudio: true,
        }));
      return [...recommendations, ...weaker];
    }
    case 'linear': {
      if (result.exact) {
        return [
          {
            id: 'keep-linear',
            title: 'Keep current measurement set',
            actionKind: 'keep',
            theoremStatus: theoremStatusForRecoverability(result, config),
            rationale: 'The current measurement rows already span the protected rows on the restricted family.',
            minimal: true,
            expectedRegime: 'exact',
            patch: {},
            availableInStudio: true,
          },
        ];
      }
      const recommendations = [];
      if (result.candidateExactIds.length) {
        const firstPatch = { ...(config.linearMeasurements ?? {}) };
        result.candidateExactIds[0].forEach((id) => {
          firstPatch[id] = true;
        });
        recommendations.push({
          id: 'add-linear-measurements',
          title: `Add ${result.candidateExactIds[0].join(' + ')}`,
          actionKind: 'add_measurement',
          theoremStatus: theoremStatusForRecoverability(result, config),
          rationale: 'This is the smallest candidate-library augmentation that removes the protected-variable-changing nullspace witness.',
          minimal: true,
          expectedRegime: 'exact',
          patch: { linearMeasurements: firstPatch },
          availableInStudio: true,
        });
      }
      result.weakerProtectedChoices
        .filter((choice) => choice.label !== result.protectedLabel)
        .forEach((choice) => {
          recommendations.push({
            id: `weaken-linear-${choice.key}`,
            title: `Weaken target to ${choice.label}`,
            actionKind: 'weaken_target',
            theoremStatus: 'Restricted-linear weaker-target split',
            rationale: 'The current record already spans this weaker protected target exactly.',
            minimal: false,
            expectedRegime: 'exact',
            patch: { linearProtected: choice.key },
            availableInStudio: true,
          });
        });
      return recommendations;
    }
    case 'boundary': {
      if (result.exact) {
        return [
          {
            id: 'keep-boundary',
            title: result.boundaryArchitecture === 'boundary_compatible_hodge'
              ? 'Keep the boundary-compatible projector'
              : 'Keep the weaker divergence-only target',
            actionKind: 'keep',
            theoremStatus: theoremStatusForRecoverability(result, config),
            rationale: result.boundaryArchitecture === 'boundary_compatible_hodge'
              ? 'The current bounded-domain architecture is already aligned with the restricted exact theorem-backed family.'
              : 'The current architecture only works because the target has been weakened to something the transplanted projector actually certifies.',
            minimal: true,
            expectedRegime: 'exact',
            patch: {},
            availableInStudio: true,
          },
        ];
      }
      return [
        {
          id: 'switch-boundary-architecture',
          title: 'Switch to the boundary-compatible Hodge family',
          actionKind: 'switch_architecture',
          theoremStatus: theoremStatusForRecoverability(result, config),
          rationale: 'The wrong architecture is the blocker here; the restricted bounded-domain Hodge projector restores exact recovery on the compatible finite-mode family.',
          minimal: true,
          expectedRegime: 'exact',
          patch: { boundaryArchitecture: 'boundary_compatible_hodge' },
          availableInStudio: true,
        },
        {
          id: 'weaken-boundary-target',
          title: 'Weaken target to bulk divergence certificate only',
          actionKind: 'weaken_target',
          theoremStatus: 'Weaker-target fallback using the existing transplanted computation',
          rationale: 'If the application only needs a divergence certificate, the transplanted architecture can still support that weaker target even though it fails the strong bounded protected class.',
          minimal: false,
          expectedRegime: 'exact',
          patch: { boundaryProtected: 'divergence_certificate' },
          availableInStudio: true,
        },
      ];
    }
    default:
      return [];
  }
}

function fiberSummaryForRecoverability(result, config) {
  switch (config.system) {
    case 'analytic':
      return result.exact
        ? 'The protected scalar is constant on every current record fiber of the analytic family.'
        : 'The current record fibers still mix states with different protected scalar values.';
    case 'qubit':
      return result.exact
        ? 'The fixed-basis record fibers collapse only states with the same z-coordinate target.'
        : 'The fixed-basis record fibers still contain states with different phase-sensitive Bloch targets.';
    case 'periodic':
      if (config.periodicObservation === 'divergence_only') {
        return result.exact
          ? 'The remaining record fibers already preserve the chosen weak divergence certificate.'
          : 'Divergence-only fibers still contain distinct incompressible states and therefore mix the stronger target.';
      }
      return result.exact
        ? 'The retained cutoff record now refines the modal fibers enough that the chosen protected target is constant on them.'
        : 'The retained cutoff fibers still mix states that differ on hidden protected modes.';
    case 'control':
      if (result.exact) {
        return 'The current finite-history record fibers are fine enough to separate the chosen protected functional exactly.';
      }
      if (result.asymptotic) {
        return 'Static fibers at the current horizon still mix target values, but the continuing observer record separates them asymptotically over time.';
      }
      return 'The current finite-history fibers still mix the protected functional, so exact recovery needs either horizon refinement or a weaker target.';
    case 'linear':
      return result.exact
        ? 'On the restricted linear family, every record fiber lies inside a target-constant fiber because the protected rows lie in the observation row space.'
        : 'A nontrivial restricted-linear record fiber still contains directions that change the protected target.';
    case 'boundary':
      return result.exact
        ? (result.boundaryArchitecture === 'boundary_compatible_hodge'
            ? 'The boundary-compatible architecture refines the bounded-domain fibers so both divergence and boundary trace stay target-constant on the restricted family.'
            : 'The target was weakened until it became constant on the coarse divergence-only fibers.')
        : 'The transplanted projector collapses divergence but leaves fibers that still mix different bounded protected states through boundary-trace mismatch.';
    default:
      return 'Recoverability depends on whether the protected target is constant on the active record fibers.';
  }
}

function decisionPostureForRecoverability(result, config, chosenRecommendation, falsePositiveWarnings) {
  const fragileWarning = falsePositiveWarnings.find((item) =>
    item.startsWith('Family-enlargement')
      || item.startsWith('Model-mismatch')
      || item.startsWith('Discretization/refinement')
  );
  if (fragileWarning && result.exact) {
    return {
      label: 'Continue exact only on the current supported family',
      action: 'continue_with_fragility_caution',
      rationale: `${fragileWarning} Keep the current exact result local to the declared family instead of promoting it as a robust inverse-recovery law.`,
      theoremStatus: theoremStatusForRecoverability(result, config),
    };
  }
  if (chosenRecommendation) {
    switch (chosenRecommendation.actionKind) {
      case 'keep':
        return {
          label: 'Continue exact recovery attempt',
          action: 'continue_exact',
          rationale: chosenRecommendation.rationale,
          theoremStatus: chosenRecommendation.theoremStatus,
        };
      case 'weaken_target':
        return {
          label: 'Switch to a weaker target',
          action: 'switch_target',
          rationale: chosenRecommendation.rationale,
          theoremStatus: chosenRecommendation.theoremStatus,
        };
      case 'add_measurement':
      case 'add_history':
      case 'add_mode':
        return {
          label: 'Augment the record',
          action: 'augment',
          rationale: chosenRecommendation.rationale,
          theoremStatus: chosenRecommendation.theoremStatus,
        };
      case 'switch_architecture':
      case 'switch_record':
        return {
          label: 'Change architecture',
          action: 'change_architecture',
          rationale: chosenRecommendation.rationale,
          theoremStatus: chosenRecommendation.theoremStatus,
        };
      default:
        break;
    }
  }
  if (result.asymptotic) {
    return {
      label: 'Change architecture toward asymptotic recovery',
      action: 'change_architecture',
      rationale: 'The current exact pursuit fails, but the supported continuing-time architecture still converges asymptotically.',
      theoremStatus: theoremStatusForRecoverability(result, config),
    };
  }
  if (result.impossible) {
    return {
      label: 'Stop exact recovery attempt as impossible',
      action: 'stop_exact',
      rationale: 'The current target remains fiber-mixed on the declared family and record, so continuing an exact-recovery claim is structurally futile.',
      theoremStatus: theoremStatusForRecoverability(result, config),
    };
  }
  return {
    label: 'Continue with caution',
    action: 'continue_cautiously',
    rationale: 'The current result is neither exact nor ruled out strongly enough to force a sharper decision on this surface.',
    theoremStatus: theoremStatusForRecoverability(result, config),
  };
}

function decorateRecoverabilityGuidance(result, config, depth = 0) {
  const guidance = guidanceForRecoverability(result, config);
  const status = recoverabilityStatusLabel(result);
  const recommendations = recommendationsForRecoverability(result, config);
  const fiberSummary = fiberSummaryForRecoverability(result, config);
  const falsePositiveWarnings = falsePositiveWarningsForRecoverability(result, config);
  const resultScopeLabel = scopeLabelForRecoverability(result, config);
  const identifiabilityStatus = identifiabilityStatusForRecoverability(result, config, guidance);
  let chosenRecommendation = null;
  let comparison = null;
  if (depth === 0) {
    chosenRecommendation = recommendations.find((item) => item.availableInStudio && item.actionKind !== 'keep') ?? recommendations[0] ?? null;
    if (chosenRecommendation && chosenRecommendation.patch && chosenRecommendation.actionKind !== 'keep') {
      const nextAnalysis = analyzeRecoverability(mergeRecoverabilityConfig(config, chosenRecommendation.patch), depth + 1);
      const keyMetricName = config.system === 'boundary' ? 'boundary mismatch' : 'κ(0)';
      const keyMetricBefore = config.system === 'boundary' ? result.transplantBoundaryMismatch : result.kappa0;
      const keyMetricAfter = config.system === 'boundary'
        ? (nextAnalysis.boundaryArchitecture === 'boundary_compatible_hodge' ? nextAnalysis.compatibleRecoveryError : nextAnalysis.kappa0)
        : nextAnalysis.kappa0;
      comparison = {
        beforeRegime: status.toLowerCase(),
        afterRegime: nextAnalysis.status.toLowerCase(),
        regimeChanged: status !== nextAnalysis.status,
        keyMetricName,
        keyMetricBefore,
        keyMetricAfter,
        exactAfter: nextAnalysis.exact,
        asymptoticAfter: nextAnalysis.asymptotic,
        impossibleAfter: nextAnalysis.impossible,
        narrative:
          chosenRecommendation.actionKind === 'weaken_target'
            ? 'Weakening the target coarsens the protected variable until it becomes constant on the existing record fibers.'
            : chosenRecommendation.actionKind === 'switch_architecture'
              ? 'The proposed architecture change replaces the current fiber geometry with one that is compatible with the protected target.'
              : 'The proposed augmentation refines the record fibers by adding the missing structure identified in the current failure analysis.',
      };
    }
  }
  const decisionPosture = decisionPostureForRecoverability(result, config, chosenRecommendation, falsePositiveWarnings);
  return {
    ...result,
    status,
    guidance,
    theoremStatus: theoremStatusForRecoverability(result, config),
    resultScopeLabel,
    identifiabilityStatus,
    fiberSummary,
    falsePositiveWarnings,
    familyRestrictionWarning: falsePositiveWarnings.find((item) => item.startsWith('Family-restriction')) ?? null,
    targetStrengthWarning: falsePositiveWarnings.find((item) => item.startsWith('Target-strength')) ?? null,
    modelMismatchWarning: falsePositiveWarnings.find((item) => item.startsWith('Model-mismatch')) ?? null,
    discretizationWarning: falsePositiveWarnings.find((item) => item.startsWith('Discretization/refinement')) ?? null,
    missingStructure: guidance.missing,
    structuralBlocker: guidance.blocker,
    recommendedArchitecture: guidance.architecture,
    weakerRecoverableTargets: guidance.weaker,
    decisionPosture,
    failureModes: Array.from(new Set(guidance.noGo ? [guidance.noGo, guidance.blocker, ...falsePositiveWarnings] : [guidance.blocker, ...falsePositiveWarnings])),
    recommendations,
    chosenRecommendation,
    comparison,
    workflow: [
      { label: 'Define protected variable', status: result.protectedLabel ? 'done' : 'pending', detail: result.protectedLabel },
      { label: 'Check record sufficiency', status: result.exact ? 'done' : result.impossible ? 'blocked' : 'in-progress', detail: result.observationLabel },
      { label: 'Choose architecture', status: guidance.architecture ? 'done' : 'pending', detail: guidance.architecture },
      { label: 'Take next step', status: guidance.nextSteps?.length ? 'ready' : 'pending', detail: guidance.nextSteps?.[0] ?? 'No next step generated' },
    ],
  };
}

function analyzeRecoverabilityCore(config) {
  let result;
  switch (config.system) {
    case 'linear':
      result = analyzeLinearTemplateRecoverability(config);
      break;
    case 'qubit':
      result = analyzeQubitRecoverability(config);
      break;
    case 'periodic':
      result = analyzePeriodicRecoverability(config);
      break;
    case 'control':
      result = analyzeControlRecoverability(config);
      break;
    case 'boundary':
      result = analyzeBoundaryRecoverability(config);
      break;
    case 'analytic':
    default:
      result = analyzeAnalyticRecoverability(config);
      break;
  }
  return result;
}

export function analyzeRecoverability(config, depth = 0) {
  return decorateRecoverabilityGuidance(analyzeRecoverabilityCore(config), config, depth);
}

export function analyzeStructuralDiscovery(config) {
  return analyzeRecoverability(config, 0);
}
