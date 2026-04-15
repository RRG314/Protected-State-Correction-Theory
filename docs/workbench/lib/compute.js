const EPS = 1e-10;

export function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}

export function zeros(length) {
  return Array.from({ length }, () => 0);
}

export function zeros2(rows, cols) {
  return Array.from({ length: rows }, () => Array.from({ length: cols }, () => 0));
}

export function identity(n) {
  return Array.from({ length: n }, (_, i) =>
    Array.from({ length: n }, (_, j) => (i === j ? 1 : 0))
  );
}

export function cloneMatrix(matrix) {
  return matrix.map((row) => row.slice());
}

export function dot(a, b) {
  return a.reduce((sum, value, index) => sum + value * b[index], 0);
}

export function norm(v) {
  return Math.sqrt(dot(v, v));
}

export function addVec(a, b) {
  return a.map((value, index) => value + b[index]);
}

export function subVec(a, b) {
  return a.map((value, index) => value - b[index]);
}

export function scaleVec(v, scalar) {
  return v.map((value) => value * scalar);
}

export function outer(a, b) {
  return a.map((value, row) => b.map((other) => value * other));
}

export function addMat(a, b) {
  return a.map((row, i) => row.map((value, j) => value + b[i][j]));
}

export function subMat(a, b) {
  return a.map((row, i) => row.map((value, j) => value - b[i][j]));
}

export function scaleMat(matrix, scalar) {
  return matrix.map((row) => row.map((value) => value * scalar));
}

export function transpose(matrix) {
  return matrix[0].map((_, j) => matrix.map((row) => row[j]));
}

export function matVec(matrix, vector) {
  return matrix.map((row) => dot(row, vector));
}

export function matMul(a, b) {
  const bt = transpose(b);
  return a.map((row) => bt.map((col) => dot(row, col)));
}

export function frobeniusNorm(matrix) {
  return Math.sqrt(matrix.flat().reduce((sum, value) => sum + value * value, 0));
}

export function gramSchmidt(vectors, tol = EPS) {
  const basis = [];
  for (const vector of vectors) {
    let work = vector.slice();
    for (const q of basis) {
      const coeff = dot(work, q);
      work = subVec(work, scaleVec(q, coeff));
    }
    const nrm = norm(work);
    if (nrm > tol) {
      basis.push(scaleVec(work, 1 / nrm));
    }
  }
  return basis;
}

export function projectorFromBasis(vectors, dimension = null) {
  const q = gramSchmidt(vectors);
  const dim = dimension ?? (q[0] ? q[0].length : vectors[0]?.length ?? 0);
  let projector = zeros2(dim, dim);
  for (const qv of q) {
    projector = addMat(projector, outer(qv, qv));
  }
  return projector;
}

export function maxBasisOverlap(basisA, basisB) {
  const qa = gramSchmidt(basisA);
  const qb = gramSchmidt(basisB);
  let maxOverlap = 0;
  for (const a of qa) {
    for (const b of qb) {
      maxOverlap = Math.max(maxOverlap, Math.abs(dot(a, b)));
    }
  }
  return maxOverlap;
}

export function rref(matrix, tol = EPS) {
  const a = cloneMatrix(matrix);
  const rows = a.length;
  const cols = a[0].length;
  let lead = 0;
  const pivots = [];
  for (let r = 0; r < rows && lead < cols; r += 1) {
    let i = r;
    while (i < rows && Math.abs(a[i][lead]) < tol) {
      i += 1;
    }
    if (i === rows) {
      lead += 1;
      r -= 1;
      continue;
    }
    [a[i], a[r]] = [a[r], a[i]];
    const pivot = a[r][lead];
    a[r] = a[r].map((value) => value / pivot);
    for (let j = 0; j < rows; j += 1) {
      if (j === r) continue;
      const factor = a[j][lead];
      if (Math.abs(factor) < tol) continue;
      a[j] = a[j].map((value, idx) => value - factor * a[r][idx]);
    }
    pivots.push(lead);
    lead += 1;
  }
  return { matrix: a, pivots };
}

export function nullSpace(matrix, tol = EPS) {
  const { matrix: reduced, pivots } = rref(matrix, tol);
  const cols = matrix[0].length;
  const free = [];
  for (let c = 0; c < cols; c += 1) {
    if (!pivots.includes(c)) free.push(c);
  }
  if (free.length === 0) return [];
  const basis = [];
  for (const freeCol of free) {
    const vector = zeros(cols);
    vector[freeCol] = 1;
    pivots.forEach((pivotCol, row) => {
      vector[pivotCol] = -reduced[row][freeCol];
    });
    basis.push(vector);
  }
  return gramSchmidt(basis, tol);
}

export function matrixRank(matrix, tol = EPS) {
  return rref(matrix, tol).pivots.length;
}

export function rowSpaceResidual(observationRows, targetRow, tol = EPS) {
  const rows = observationRows.filter((row) => row.some((value) => Math.abs(value) > tol));
  if (!rows.length) return norm(targetRow);
  const augmented = [...rows.map((row) => row.slice()), targetRow.slice()];
  const rankBefore = matrixRank(rows, tol);
  const rankAfter = matrixRank(augmented, tol);
  if (rankAfter === rankBefore) return 0;
  const basis = gramSchmidt(rows);
  let projected = zeros(targetRow.length);
  for (const vector of basis) {
    projected = addVec(projected, scaleVec(vector, dot(targetRow, vector)));
  }
  return norm(subVec(targetRow, projected));
}

export function recoverableRowIndices(observationRows, protectedRows, tol = EPS) {
  const residuals = protectedRows.map((row) => rowSpaceResidual(observationRows, row, tol));
  const recoverable = [];
  const unrecoverable = [];
  residuals.forEach((value, index) => {
    if (value <= tol) recoverable.push(index);
    else unrecoverable.push(index);
  });
  return { residuals, recoverable, unrecoverable };
}

export function minimalRowAugmentation(observationRows, protectedRows, candidateRows, tol = EPS) {
  const currentRank = matrixRank(observationRows, tol);
  const neededRank = matrixRank([...observationRows, ...protectedRows], tol);
  const maxAdded = Math.max(candidateRows.length, neededRank - currentRank);
  const exactSets = [];
  const indexList = Array.from({ length: candidateRows.length }, (_, index) => index);
  const choose = (items, size, start = 0, prefix = []) => {
    if (prefix.length === size) {
      exactSets.push(prefix.slice());
      return;
    }
    for (let i = start; i < items.length; i += 1) {
      prefix.push(items[i]);
      choose(items, size, i + 1, prefix);
      prefix.pop();
    }
  };
  for (let size = 1; size <= maxAdded; size += 1) {
    exactSets.length = 0;
    choose(indexList, size);
    const valid = exactSets.filter((combo) => {
      const augmented = [...observationRows, ...combo.map((index) => candidateRows[index])];
      return protectedRows.every((row) => rowSpaceResidual(augmented, row, tol) <= tol);
    });
    if (valid.length) {
      return { minimalAdded: size, exactSets: valid };
    }
  }
  return { minimalAdded: null, exactSets: [] };
}

export function orthogonalComplement(basis, dimension) {
  const q = gramSchmidt(basis);
  const complement = [];
  for (let i = 0; i < dimension; i += 1) {
    let candidate = zeros(dimension);
    candidate[i] = 1;
    for (const qv of [...q, ...complement]) {
      candidate = subVec(candidate, scaleVec(qv, dot(candidate, qv)));
    }
    const nrm = norm(candidate);
    if (nrm > EPS) {
      complement.push(scaleVec(candidate, 1 / nrm));
    }
  }
  return complement;
}

export function formatVector(v, digits = 3) {
  return `[${v.map((value) => Number(value).toFixed(digits)).join(', ')}]`;
}

export function formatMatrix(matrix, digits = 3) {
  return matrix.map((row) => `[${row.map((value) => Number(value).toFixed(digits)).join(', ')}]`).join('\n');
}

export function analyzeExactProjection(config) {
  const angle = (config.angleDeg * Math.PI) / 180;
  const protectedBasis = [[1, 0]];
  const disturbanceBasis = [[Math.cos(angle), Math.sin(angle)]];
  const s = [config.protectedMagnitude, 0];
  const d = scaleVec(disturbanceBasis[0], config.disturbanceMagnitude);
  const x = addVec(s, d);
  const pS = projectorFromBasis(protectedBasis, 2);
  const recovered = matVec(pS, x);
  const overlap = maxBasisOverlap(protectedBasis, disturbanceBasis);
  const exactError = norm(subVec(recovered, s));
  return {
    protectedBasis,
    disturbanceBasis,
    s,
    d,
    x,
    recovered,
    overlap,
    exactError,
    admissible: overlap < 1e-8,
    theoremStatus: overlap < 1e-8 ? 'PROVED' : 'NO-GO EXAMPLE',
  };
}

function bitFlipIndex(index, target) {
  return index ^ (1 << (2 - target));
}

function basisState(index, dimension = 8) {
  return Array.from({ length: dimension }, (_, i) => (i === index ? 1 : 0));
}

function applyBitFlip(state, target) {
  const out = zeros(state.length);
  for (let i = 0; i < state.length; i += 1) {
    out[bitFlipIndex(i, target)] = state[i];
  }
  return out;
}

function qecCodeBasis() {
  return [basisState(0), basisState(7)];
}

function sectorBasisForError(errorIndex) {
  const code = qecCodeBasis();
  if (errorIndex === 0) return code;
  return code.map((vector) => applyBitFlip(vector, errorIndex - 1));
}

function combineBasis(basis, coeffs) {
  return basis.reduce((acc, basisVector, idx) => addVec(acc, scaleVec(basisVector, coeffs[idx])), zeros(basis[0].length));
}

function recoverSectorState(state, sectorBasis, protectedBasis) {
  const coeffs = sectorBasis.map((basisVector) => dot(basisVector, state));
  return combineBasis(protectedBasis, coeffs);
}

export function analyzeQecSector(config) {
  const protectedBasis = qecCodeBasis();
  const alpha = Number(config.alpha);
  const beta = Number(config.beta);
  const normFactor = Math.hypot(alpha, beta) || 1;
  const coeffs = [alpha / normFactor, beta / normFactor];
  const logical = combineBasis(protectedBasis, coeffs);
  const sectorBases = [0, 1, 2, 3].map((index) => sectorBasisForError(index));
  const disturbed = combineBasis(sectorBases[config.errorIndex], coeffs);
  const recovered = recoverSectorState(disturbed, sectorBases[config.errorIndex], protectedBasis);
  const sectorOverlap = sectorBases.map((basisA, i) =>
    sectorBases.map((basisB, j) => (i === j ? 1 : Math.max(...basisA.map((va) => Math.max(...basisB.map((vb) => Math.abs(dot(va, vb))))))))
  );
  const recoveryError = norm(subVec(recovered, logical));
  return {
    logical,
    disturbed,
    recovered,
    sectorOverlap,
    recoveryError,
    sectorLabels: ['I', 'X₁', 'X₂', 'X₃'],
    selectedLabel: ['I', 'X₁', 'X₂', 'X₃'][config.errorIndex],
    exact: recoveryError < 1e-9,
  };
}

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
  const deltaIndex = Math.round((selectedDelta / 1) * (deltas.length - 1));
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
    selectedKappa: collapse[deltaIndex],
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
  const deltaIndex = Math.round((selectedDelta / 3) * (current.deltas.length - 1));
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
    selectedKappa: current.collapse[deltaIndex],
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
  const deltaIndex = Math.round((selectedDelta / 2.5) * (deltas.length - 1));
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
    selectedKappa: collapse[deltaIndex],
    kappa0,
    meanRecoveryError: errors.reduce((sum, value) => sum + value, 0) / errors.length,
    maxRecoveryError: Math.max(...errors),
    observerErrorHistory,
    spectralRadius,
    historyThreshold,
  };
}

function diagonalRecordMatrix(eigenvalues, sensorWeights, horizon) {
  return Array.from({ length: horizon }, (_, t) =>
    sensorWeights.map((weight, index) => weight * (eigenvalues[index] ** t))
  );
}

function activeSensorCount(sensorWeights) {
  return sensorWeights.filter((value) => Math.abs(value) > 1e-9).length;
}

function solveLeastSquares(matrix, rhs) {
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
  const deltaIndex = Math.round((selectedDelta / 2) * (deltas.length - 1));
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
    impossible: predictedMinHorizon === null,
    deltas,
    collapse,
    selectedDelta,
    selectedKappa: collapse[deltaIndex],
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

export const LINEAR_TEMPLATE_LIBRARY = {
  sensor_basis: {
    label: '3-state static record template',
    candidates: [
      { id: 'measure_x1', label: 'measure x1', row: [1, 0, 0] },
      { id: 'measure_x2', label: 'measure x2', row: [0, 1, 0] },
      { id: 'measure_x3', label: 'measure x3', row: [0, 0, 1] },
      { id: 'measure_x2_plus_x3', label: 'measure x2+x3', row: [0, 1, 1] },
      { id: 'measure_x1_plus_x2', label: 'measure x1+x2', row: [1, 1, 0] },
    ],
    protectedOptions: {
      x3: { label: 'coordinate x3', rows: [[0, 0, 1]] },
      x2_plus_x3: { label: 'sum x2+x3', rows: [[0, 1, 1]] },
      tail_pair: { label: 'tail pair (x2, x3)', rows: [[0, 1, 0], [0, 0, 1]] },
      full_state: {
        label: 'full state (x1, x2, x3)',
        rows: [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
      },
    },
    defaultMeasurements: ['measure_x1', 'measure_x2_plus_x3'],
  },
};

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
  const deltaIndex = Math.round((selectedDelta / 2.5) * (deltas.length - 1));
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
    selectedKappa: collapse[deltaIndex],
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
    unrestrictedMinimalAddedMeasurements: unrestrictedMinimalAdded,
    minimalAddedMeasurements: augmentation.minimalAdded,
    stabilitySlopeUpper,
    selectedStabilityUpperBound: stabilitySlopeUpper === null ? null : stabilitySlopeUpper * selectedDelta,
    candidateExactSets: augmentation.exactSets.map((combo) => combo.map((index) => remainingCandidates[index].label)),
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
  const deltaIndex = Math.round(selectedDelta * (deltas.length - 1));
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
    selectedKappa: collapse[deltaIndex],
    selectedLowerBound: noiseLowerBounds[deltaIndex],
    kappa0: epsilon < 1e-9 ? 2 : 0,
    meanRecoveryError: 0,
    maxRecoveryError: 0,
    epsilon,
    amplification: epsilon < 1e-9 ? Infinity : 1 / epsilon,
  };
}

function recoverabilityStatusLabel(result) {
  if (result.exact) return 'Exact';
  if (result.asymptotic) return 'Asymptotic';
  if (result.impossible) return 'Impossible';
  return 'Approximate';
}

function periodicWeakerSuggestions(cutoff) {
  const options = [
    { label: 'leading modal coefficient', threshold: 1 },
    { label: 'first two modal coefficients', threshold: 2 },
    { label: 'low-mode weighted sum', threshold: 2 },
    { label: 'band-limited contrast functional', threshold: 3 },
    { label: 'full weighted modal sum', threshold: 4 },
    { label: 'full four-mode coefficient vector', threshold: 4 },
  ];
  return options.filter((option) => cutoff >= option.threshold).map((option) => option.label);
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

function decorateRecoverabilityGuidance(result, config) {
  const guidance = guidanceForRecoverability(result, config);
  const status = recoverabilityStatusLabel(result);
  return {
    ...result,
    status,
    guidance,
    workflow: [
      { label: 'Define protected variable', status: result.protectedLabel ? 'done' : 'pending', detail: result.protectedLabel },
      { label: 'Check record sufficiency', status: result.exact ? 'done' : result.impossible ? 'blocked' : 'in-progress', detail: result.observationLabel },
      { label: 'Choose architecture', status: guidance.architecture ? 'done' : 'pending', detail: guidance.architecture },
      { label: 'Take next step', status: guidance.nextSteps?.length ? 'ready' : 'pending', detail: guidance.nextSteps?.[0] ?? 'No next step generated' },
    ],
  };
}

export function analyzeRecoverability(config) {
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
    case 'analytic':
    default:
      result = analyzeAnalyticRecoverability(config);
      break;
  }
  return decorateRecoverabilityGuidance(result, config);
}

function gridAxis(n) {
  return Array.from({ length: n }, (_, i) => i / n);
}

function makeField(n, contamination) {
  const x = gridAxis(n);
  const y = gridAxis(n);
  const h = 1 / n;
  const psi = zeros2(n, n);
  const phi = zeros2(n, n);
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < n; j += 1) {
      psi[i][j] = Math.sin(2 * Math.PI * x[i]) * Math.sin(2 * Math.PI * y[j]);
      phi[i][j] = contamination * Math.cos(4 * Math.PI * x[i]) * Math.cos(2 * Math.PI * y[j]);
    }
  }
  const dpsix = centralDiffX(psi, h);
  const dpsiy = centralDiffY(psi, h);
  const gradx = centralDiffX(phi, h);
  const grady = centralDiffY(phi, h);
  const BxPhys = dpsiy;
  const ByPhys = dpsix.map((row) => row.map((value) => -value));
  return {
    h,
    Bx: addField(BxPhys, gradx),
    By: addField(ByPhys, grady),
    BxPhys,
    ByPhys,
  };
}

function addField(a, b) {
  return a.map((row, i) => row.map((value, j) => value + b[i][j]));
}

function subField(a, b) {
  return a.map((row, i) => row.map((value, j) => value - b[i][j]));
}

export function centralDiffX(field, h) {
  const n = field.length;
  return field.map((row, i) =>
    row.map((_, j) => (field[(i + 1) % n][j] - field[(i - 1 + n) % n][j]) / (2 * h))
  );
}

export function centralDiffY(field, h) {
  const n = field.length;
  return field.map((row, i) =>
    row.map((_, j) => (field[i][(j + 1) % n] - field[i][(j - 1 + n) % n]) / (2 * h))
  );
}

export function divergence2d(Bx, By, h) {
  const dBx = centralDiffX(Bx, h);
  const dBy = centralDiffY(By, h);
  return dBx.map((row, i) => row.map((value, j) => value + dBy[i][j]));
}

export function l2NormField(field) {
  const values = field.flat();
  return Math.sqrt(values.reduce((sum, value) => sum + value * value, 0) / values.length);
}

function complex(re, im = 0) {
  return { re, im };
}

function cAdd(a, b) {
  return { re: a.re + b.re, im: a.im + b.im };
}

function cSub(a, b) {
  return { re: a.re - b.re, im: a.im - b.im };
}

function cMul(a, b) {
  return { re: a.re * b.re - a.im * b.im, im: a.re * b.im + a.im * b.re };
}

function cScale(a, scalar) {
  return { re: a.re * scalar, im: a.im * scalar };
}

function cConj(a) {
  return { re: a.re, im: -a.im };
}

function dft2(field) {
  const n = field.length;
  const out = Array.from({ length: n }, () => Array.from({ length: n }, () => complex(0, 0)));
  for (let kx = 0; kx < n; kx += 1) {
    for (let ky = 0; ky < n; ky += 1) {
      let sum = complex(0, 0);
      for (let x = 0; x < n; x += 1) {
        for (let y = 0; y < n; y += 1) {
          const angle = -2 * Math.PI * ((kx * x) / n + (ky * y) / n);
          const phase = complex(Math.cos(angle), Math.sin(angle));
          sum = cAdd(sum, cScale(phase, field[x][y]));
        }
      }
      out[kx][ky] = sum;
    }
  }
  return out;
}

function idft2(fieldHat) {
  const n = fieldHat.length;
  const out = zeros2(n, n);
  for (let x = 0; x < n; x += 1) {
    for (let y = 0; y < n; y += 1) {
      let sum = complex(0, 0);
      for (let kx = 0; kx < n; kx += 1) {
        for (let ky = 0; ky < n; ky += 1) {
          const angle = 2 * Math.PI * ((kx * x) / n + (ky * y) / n);
          const phase = complex(Math.cos(angle), Math.sin(angle));
          sum = cAdd(sum, cMul(fieldHat[kx][ky], phase));
        }
      }
      out[x][y] = sum.re / (n * n);
    }
  }
  return out;
}

function fftFrequency(index, n) {
  return index <= n / 2 ? index : index - n;
}

export function solvePoissonPeriodic(rhs, h) {
  const n = rhs.length;
  const rhsHat = dft2(rhs);
  const phiHat = Array.from({ length: n }, () => Array.from({ length: n }, () => complex(0, 0)));
  for (let kx = 0; kx < n; kx += 1) {
    for (let ky = 0; ky < n; ky += 1) {
      const wx = 2 * Math.PI * fftFrequency(kx, n);
      const wy = 2 * Math.PI * fftFrequency(ky, n);
      const dxSymbol = complex(0, Math.sin(wx * h) / h);
      const dySymbol = complex(0, Math.sin(wy * h) / h);
      const norm2 = dxSymbol.im * dxSymbol.im + dySymbol.im * dySymbol.im;
      if (norm2 > EPS) {
        phiHat[kx][ky] = cScale(rhsHat[kx][ky], -1 / norm2);
      }
    }
  }
  return idft2(phiHat);
}

export function helmholtzProject2d(Bx, By, h) {
  const n = Bx.length;
  const bxHat = dft2(Bx);
  const byHat = dft2(By);
  const gradXHat = Array.from({ length: n }, () => Array.from({ length: n }, () => complex(0, 0)));
  const gradYHat = Array.from({ length: n }, () => Array.from({ length: n }, () => complex(0, 0)));
  for (let kx = 0; kx < n; kx += 1) {
    for (let ky = 0; ky < n; ky += 1) {
      const wx = 2 * Math.PI * fftFrequency(kx, n);
      const wy = 2 * Math.PI * fftFrequency(ky, n);
      const dxSymbol = complex(0, Math.sin(wx * h) / h);
      const dySymbol = complex(0, Math.sin(wy * h) / h);
      const norm2 = dxSymbol.im * dxSymbol.im + dySymbol.im * dySymbol.im;
      if (norm2 <= EPS) continue;
      const divHat = cAdd(cMul(dxSymbol, bxHat[kx][ky]), cMul(dySymbol, byHat[kx][ky]));
      gradXHat[kx][ky] = cScale(cMul(cConj(dxSymbol), divHat), 1 / norm2);
      gradYHat[kx][ky] = cScale(cMul(cConj(dySymbol), divHat), 1 / norm2);
    }
  }
  const gradx = idft2(gradXHat);
  const grady = idft2(gradYHat);
  return {
    BxProj: subField(Bx, gradx),
    ByProj: subField(By, grady),
    gradx,
    grady,
  };
}

export function glmStep2d(Bx, By, psi, h, dt, ch = 1, cp = 1) {
  const dpsix = centralDiffX(psi, h);
  const dpsiy = centralDiffY(psi, h);
  const divB = divergence2d(Bx, By, h);
  const BxNew = subField(Bx, dpsix.map((row) => row.map((value) => dt * value)));
  const ByNew = subField(By, dpsiy.map((row) => row.map((value) => dt * value)));
  const damping = (ch * ch) / Math.max(cp * cp, 1e-12);
  const psiNew = psi.map((row, i) =>
    row.map((value, j) => value - dt * (ch * ch * divB[i][j] + damping * value))
  );
  return { Bx: BxNew, By: ByNew, psi: psiNew };
}

export function analyzeMhdProjection(config) {
  const n = Number(config.gridSize);
  const contamination = Number(config.contamination);
  const glmSteps = Number(config.glmSteps);
  const selectedFrame = clamp(Number(config.frame ?? glmSteps), 0, glmSteps);
  const { h, Bx, By } = makeField(n, contamination);
  const beforeDiv = divergence2d(Bx, By, h);
  const projection = helmholtzProject2d(Bx, By, h, Number(config.poissonIterations));
  const afterExactDiv = divergence2d(projection.BxProj, projection.ByProj, h);
  let psi = zeros2(n, n);
  let BxGlm = cloneMatrix(Bx);
  let ByGlm = cloneMatrix(By);
  const glmHistory = [l2NormField(beforeDiv)];
  const glmFrames = [beforeDiv];
  for (let step = 0; step < glmSteps; step += 1) {
    const next = glmStep2d(BxGlm, ByGlm, psi, h, Number(config.dt), Number(config.ch), Number(config.cp));
    BxGlm = next.Bx;
    ByGlm = next.By;
    psi = next.psi;
    const currentDiv = divergence2d(BxGlm, ByGlm, h);
    glmHistory.push(l2NormField(currentDiv));
    glmFrames.push(currentDiv);
  }
  const afterGlmDiv = divergence2d(BxGlm, ByGlm, h);
  return {
    beforeDiv,
    afterExactDiv,
    afterGlmDiv,
    glmFrames,
    beforeNorm: l2NormField(beforeDiv),
    afterExactNorm: l2NormField(afterExactDiv),
    afterGlmNorm: l2NormField(afterGlmDiv),
    glmHistory,
    selectedFrame,
    selectedGlmDiv: glmFrames[selectedFrame],
    selectedGlmNorm: glmHistory[selectedFrame],
    exactImprovementFactor: l2NormField(beforeDiv) / Math.max(l2NormField(afterExactDiv), 1e-12),
    glmImprovementFactor: l2NormField(beforeDiv) / Math.max(l2NormField(afterGlmDiv), 1e-12),
  };
}

export function analyzeGaugeProjection(config) {
  const base = analyzeMhdProjection(config);
  return {
    ...base,
    beforeGaugeNorm: base.beforeNorm,
    afterExactGaugeNorm: base.afterExactNorm,
    afterGlmGaugeNorm: base.afterGlmNorm,
  };
}

function boundedDivergence2d(Bx, By, h) {
  const dBx = gradientAxis(Bx, h, 0);
  const dBy = gradientAxis(By, h, 1);
  return dBx.map((row, i) => row.map((value, j) => value + dBy[i][j]));
}

function makeBoundedDivergenceFreePair(n) {
  const h = 1 / (n - 1);
  const x = Array.from({ length: n }, (_, i) => i * h);
  const y = Array.from({ length: n }, (_, i) => i * h);
  const psi1 = zeros2(n, n);
  const psi2 = zeros2(n, n);
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < n; j += 1) {
      psi1[i][j] = Math.sin(Math.PI * x[i]) ** 2 * Math.sin(Math.PI * y[j]) ** 2;
      psi2[i][j] = Math.sin(2 * Math.PI * x[i]) ** 2 * Math.sin(Math.PI * y[j]) ** 2;
    }
  }
  const dpsi1x = gradientAxis(psi1, h, 0);
  const dpsi1y = gradientAxis(psi1, h, 1);
  const dpsi2x = gradientAxis(psi2, h, 0);
  const dpsi2y = gradientAxis(psi2, h, 1);
  return {
    h,
    u1x: dpsi1y.map((row) => row.map((value) => -value)),
    u1y: dpsi1x,
    u2x: dpsi2y.map((row) => row.map((value) => -value)),
    u2y: dpsi2x,
  };
}

function boundaryNormalRms(Bx, By) {
  const edgeValues = [
    ...Bx[0],
    ...Bx[Bx.length - 1],
    ...By.map((row) => row[0]),
    ...By.map((row) => row[row.length - 1]),
  ];
  const meanSquare = edgeValues.reduce((sum, value) => sum + value * value, 0) / edgeValues.length;
  return Math.sqrt(meanSquare);
}

function makeBoundedDomainField(n) {
  const h = 1 / (n - 1);
  const x = Array.from({ length: n }, (_, i) => i * h);
  const y = Array.from({ length: n }, (_, i) => i * h);
  const psi = zeros2(n, n);
  const phi = zeros2(n, n);
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < n; j += 1) {
      psi[i][j] = Math.sin(Math.PI * x[i]) ** 2 * Math.sin(Math.PI * y[j]) ** 2;
      phi[i][j] = x[i] * (1 - x[i]) * Math.sin(Math.PI * y[j]);
    }
  }
  const dpsix = gradientAxis(psi, h, 0);
  const dpsiy = gradientAxis(psi, h, 1);
  const gradx = gradientAxis(phi, h, 0);
  const grady = gradientAxis(phi, h, 1);
  const BxPhys = dpsiy.map((row) => row.map((value) => -value));
  const ByPhys = dpsix;
  return {
    h,
    Bx: addField(BxPhys, gradx),
    By: addField(ByPhys, grady),
    BxPhys,
    ByPhys,
  };
}

function gradientAxis(field, h, axis) {
  const rows = field.length;
  const cols = field[0].length;
  return field.map((row, i) =>
    row.map((_, j) => {
      if (axis === 0) {
        if (i === 0) return (field[i + 1][j] - field[i][j]) / h;
        if (i === rows - 1) return (field[i][j] - field[i - 1][j]) / h;
        return (field[i + 1][j] - field[i - 1][j]) / (2 * h);
      }
      if (j === 0) return (field[i][j + 1] - field[i][j]) / h;
      if (j === cols - 1) return (field[i][j] - field[i][j - 1]) / h;
      return (field[i][j + 1] - field[i][j - 1]) / (2 * h);
    })
  );
}

export function analyzeBoundaryProjectionLimit(config = {}) {
  const n = Number(config.gridSize ?? 32);
  const { h, Bx, By, BxPhys, ByPhys } = makeBoundedDomainField(n);
  const beforeDiv = divergence2d(Bx, By, h);
  const projection = helmholtzProject2d(Bx, By, h, Number(config.poissonIterations ?? 320));
  const afterDiv = divergence2d(projection.BxProj, projection.ByProj, h);
  return {
    beforeDiv,
    afterDiv,
    beforeNorm: l2NormField(beforeDiv),
    afterNorm: l2NormField(afterDiv),
    physicalBoundaryNormalRms: boundaryNormalRms(BxPhys, ByPhys),
    projectedBoundaryNormalRms: boundaryNormalRms(projection.BxProj, projection.ByProj),
    transplantFails: boundaryNormalRms(projection.BxProj, projection.ByProj) > 1e-2,
  };
}

export function analyzeCfdProjection(config) {
  const periodicGrid = Number(config.periodicGridSize);
  const boundedGrid = Number(config.boundedGridSize);
  const contamination = Number(config.contamination);
  const { h, Bx, By, BxPhys, ByPhys } = makeField(periodicGrid, contamination);
  const beforePeriodicDiv = divergence2d(Bx, By, h);
  const projection = helmholtzProject2d(Bx, By, h);
  const afterPeriodicDiv = divergence2d(projection.BxProj, projection.ByProj, h);
  const periodicRecoveryError = Math.sqrt(
    projection.BxProj.flat().reduce((sum, value, idx) => {
      const i = Math.floor(idx / periodicGrid);
      const j = idx % periodicGrid;
      return sum + (value - BxPhys[i][j]) ** 2 + (projection.ByProj[i][j] - ByPhys[i][j]) ** 2;
    }, 0) / (periodicGrid * periodicGrid)
  );
  const projection2 = helmholtzProject2d(projection.BxProj, projection.ByProj, h);
  const periodicIdempotenceError = Math.sqrt(
    projection2.BxProj.flat().reduce((sum, value, idx) => {
      const i = Math.floor(idx / periodicGrid);
      const j = idx % periodicGrid;
      return sum + (value - projection.BxProj[i][j]) ** 2 + (projection2.ByProj[i][j] - projection.ByProj[i][j]) ** 2;
    }, 0) / (periodicGrid * periodicGrid)
  );

  const bounded = analyzeBoundaryProjectionLimit({ gridSize: boundedGrid, poissonIterations: config.poissonIterations });
  const boundedPair = makeBoundedDivergenceFreePair(boundedGrid);
  const divergenceOnlyWitness = {
    firstStateDivergenceRms: l2NormField(boundedDivergence2d(boundedPair.u1x, boundedPair.u1y, boundedPair.h)),
    secondStateDivergenceRms: l2NormField(boundedDivergence2d(boundedPair.u2x, boundedPair.u2y, boundedPair.h)),
    stateSeparationRms: Math.sqrt(
      boundedPair.u1x.flat().reduce((sum, value, idx) => {
        const i = Math.floor(idx / boundedGrid);
        const j = idx % boundedGrid;
        return sum + (value - boundedPair.u2x[i][j]) ** 2 + (boundedPair.u1y[i][j] - boundedPair.u2y[i][j]) ** 2;
      }, 0) / (boundedGrid * boundedGrid)
    ),
  };

  return {
    periodicBeforeDiv: beforePeriodicDiv,
    periodicAfterDiv: afterPeriodicDiv,
    periodicBeforeNorm: l2NormField(beforePeriodicDiv),
    periodicAfterNorm: l2NormField(afterPeriodicDiv),
    periodicRecoveryError,
    periodicIdempotenceError,
    boundedBeforeDiv: bounded.beforeDiv,
    boundedAfterDiv: bounded.afterDiv,
    boundedBeforeNorm: bounded.beforeNorm,
    boundedAfterNorm: bounded.afterNorm,
    boundedPhysicalBoundaryNormalRms: bounded.physicalBoundaryNormalRms,
    boundedProjectedBoundaryNormalRms: bounded.projectedBoundaryNormalRms,
    boundedTransplantFails: bounded.transplantFails,
    divergenceOnlyWitness,
  };
}

function rungeKutta4(K, x0, totalTime, steps = 240) {
  const dt = totalTime / steps;
  let x = x0.slice();
  const path = [x.slice()];
  const derivative = (v) => scaleVec(matVec(K, v), -1);
  for (let step = 0; step < steps; step += 1) {
    const k1 = derivative(x);
    const k2 = derivative(addVec(x, scaleVec(k1, dt / 2)));
    const k3 = derivative(addVec(x, scaleVec(k2, dt / 2)));
    const k4 = derivative(addVec(x, scaleVec(k3, dt)));
    const update = addVec(addVec(k1, scaleVec(k2, 2)), addVec(scaleVec(k3, 2), k4));
    x = addVec(x, scaleVec(update, dt / 6));
    path.push(x.slice());
  }
  return path;
}

function flowMatrix(K, totalTime) {
  const n = K.length;
  const columns = [];
  for (let i = 0; i < n; i += 1) {
    const basis = zeros(n);
    basis[i] = 1;
    const path = rungeKutta4(K, basis, totalTime, 320);
    columns.push(path[path.length - 1]);
  }
  return transpose(columns);
}

export function analyzeContinuousGenerator(config) {
  const K = config.matrix;
  const x0 = config.x0;
  const totalTime = Number(config.time);
  const steps = Number(config.steps);
  const kernelBasis = nullSpace(K);
  const disturbanceBasis = orthogonalComplement(kernelBasis, K.length);
  const pS = projectorFromBasis(kernelBasis, K.length);
  const pD = projectorFromBasis(disturbanceBasis, K.length);
  const path = rungeKutta4(K, x0, totalTime, steps);
  const xt = path[path.length - 1];
  const protectedDrift = norm(subVec(matVec(pS, xt), matVec(pS, x0)));
  const disturbanceNorms = path.map((point) => norm(matVec(pD, point)));
  const flow = flowMatrix(K, totalTime);
  const exactResidualMatrix = (() => {
    const ss = matMul(matMul(pS, flow), pS);
    const sd = matMul(matMul(pS, flow), pD);
    const ds = matMul(matMul(pD, flow), pS);
    const dd = matMul(matMul(pD, flow), pD);
    const pSOnly = matMul(pS, pS);
    return [frobeniusNorm(subMat(ss, pSOnly)), frobeniusNorm(sd), frobeniusNorm(ds), frobeniusNorm(dd)];
  })();
  const mixingNorm = frobeniusNorm(matMul(matMul(pS, K), pD));
  const selectedFrame = clamp(Number(config.frame ?? steps), 0, steps);
  const selectedState = path[selectedFrame];
  const selectedTime = (selectedFrame / Math.max(steps, 1)) * totalTime;
  return {
    kernelBasis,
    disturbanceBasis,
    protectedDrift,
    disturbanceBefore: disturbanceNorms[0],
    disturbanceAfter: disturbanceNorms[disturbanceNorms.length - 1],
    disturbanceNorms,
    path,
    xt,
    selectedFrame,
    selectedState,
    selectedTime,
    mixingNorm,
    exactRecoveryResidual: Math.max(...exactResidualMatrix),
    finiteTimeExactRecoveryPossible: disturbanceBasis.length === 0 ? true : Math.max(...exactResidualMatrix) < 1e-6,
  };
}

export function analyzeNoGo(config) {
  switch (config.example) {
    case 'divergence-only': {
      const witness = analyzeCfdProjection({
        periodicGridSize: 12,
        boundedGridSize: 18,
        contamination: 0.22,
        poissonIterations: 320,
      }).divergenceOnlyWitness;
      return {
        title: 'Divergence-only bounded recovery failure',
        status: 'PROVED NO-GO',
        summary: 'Distinct bounded incompressible states can share the same divergence data, so a recovery map that only sees div u cannot recover the full protected class exactly.',
        details: {
          firstStateDivergenceRms: witness.firstStateDivergenceRms,
          secondStateDivergenceRms: witness.secondStateDivergenceRms,
          stateSeparationRms: witness.stateSeparationRms,
        },
      };
    }
    case 'boundary': {
      const result = analyzeBoundaryProjectionLimit({ gridSize: 32, poissonIterations: 320 });
      return {
        title: 'Bounded-domain projection transplant failure',
        status: 'COUNTEREXAMPLE / REJECTED BRIDGE',
        summary: 'The periodic exact projector still removes divergence, but it does not preserve the bounded-domain protected class because the projected field picks up nonzero boundary-normal trace.',
        details: {
          beforeDivNorm: result.beforeNorm,
          afterDivNorm: result.afterNorm,
          physicalBoundaryNormalRms: result.physicalBoundaryNormalRms,
          projectedBoundaryNormalRms: result.projectedBoundaryNormalRms,
        },
      };
    }
    case 'overlap': {
      const x = [1, 0];
      return {
        title: 'Overlap / indistinguishability',
        status: 'PROVED NO-GO',
        summary: 'The same ambient state admits two admissible decompositions, so no single-valued exact recovery map can return both protected components.',
        details: {
          state: x,
          decompositionA: 'x = (1, 0) + (0, 0)',
          decompositionB: 'x = (0, 0) + (1, 0)',
        },
      };
    }
    case 'sector-overlap': {
      return {
        title: 'Sector-overlap detection failure',
        status: 'PROVED NO-GO',
        summary: 'If two candidate sectors share a nonzero vector, no detector can label one as sector i and the other as sector j on that shared vector.',
        details: {
          D1: 'span{e1, e2}',
          D2: 'span{e2, e3}',
          witness: 'e2 lies in both D1 and D2',
        },
      };
    }
    case 'mixing': {
      const result = analyzeContinuousGenerator({
        matrix: [[0, 1], [0, 1]],
        x0: [0, 1],
        time: 1,
        steps: 240,
      });
      return {
        title: 'Mixing into the protected coordinates',
        status: 'PROVED NO-GO',
        summary: 'Protected coordinates drift immediately because P_S K P_D is nonzero.',
        details: {
          mixingNorm: result.mixingNorm,
          protectedDrift: result.protectedDrift,
        },
      };
    }
    case 'rank': {
      return {
        title: 'Insufficient correction image',
        status: 'PROVED NO-GO',
        summary: 'A correction operator of rank 1 cannot exactly remove a 2-dimensional disturbance family.',
        details: {
          disturbanceDimension: 2,
          correctionRank: 1,
        },
      };
    }
    case 'finite-time':
    default: {
      const result = analyzeContinuousGenerator({
        matrix: [[0, 0, 0], [0, 1, 0], [0, 0, 2]],
        x0: [2, -1, 0.5],
        time: 1.5,
        steps: 320,
      });
      return {
        title: 'Finite-time exact recovery failure for smooth linear flows',
        status: 'PROVED NO-GO',
        summary: 'The flow remains invertible at every finite time, so it cannot annihilate a nontrivial disturbance space exactly.',
        details: {
          exactRecoveryResidual: result.exactRecoveryResidual,
          finiteTimeExactRecoveryPossible: result.finiteTimeExactRecoveryPossible,
        },
      };
    }
  }
}
