import {
  EPS,
  clamp,
  zeros,
  zeros2,
  cloneMatrix,
  dot,
  norm,
  addVec,
  subVec,
  scaleVec,
  outer,
  addMat,
  subMat,
  scaleMat,
  transpose,
  matVec,
  matMul,
  frobeniusNorm,
  gramSchmidt,
  projectorFromBasis,
  orthogonalComplement,
  invertMatrix,
} from './core/linearAlgebra.js';

function flattenValue(value) {
  if (Array.isArray(value) && Array.isArray(value[0])) {
    return value.flat();
  }
  return value.slice();
}

function rmsMetric(a, b) {
  const flatA = flattenValue(a);
  const flatB = flattenValue(b);
  const diffs = flatA.map((value, index) => value - flatB[index]);
  return norm(diffs) / Math.sqrt(Math.max(flatA.length, 1));
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

function stackFieldVector(Ux, Uy) {
  return [...Ux.flat(), ...Uy.flat()];
}

function unstackFieldVector(vector, n) {
  const size = n * n;
  return {
    Ux: vector.slice(0, size).reduce((rows, value, index) => {
      const row = Math.floor(index / n);
      if (!rows[row]) rows[row] = [];
      rows[row].push(value);
      return rows;
    }, []),
    Uy: vector.slice(size).reduce((rows, value, index) => {
      const row = Math.floor(index / n);
      if (!rows[row]) rows[row] = [];
      rows[row].push(value);
      return rows;
    }, []),
  };
}

function boundedStreamVelocityMode(n, mx, my) {
  const h = 1 / (n - 1);
  const x = Array.from({ length: n }, (_, index) => index * h);
  const y = Array.from({ length: n }, (_, index) => index * h);
  const psi = zeros2(n, n);
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < n; j += 1) {
      psi[i][j] = Math.sin(mx * Math.PI * x[i]) * Math.sin(my * Math.PI * y[j]);
    }
  }
  const dpsix = gradientAxis(psi, h, 0);
  const dpsiy = gradientAxis(psi, h, 1);
  return {
    Ux: dpsiy.map((row) => row.map((value) => -value)),
    Uy: dpsix,
  };
}

function boundedGradientMode(n, mx, my) {
  const h = 1 / (n - 1);
  const x = Array.from({ length: n }, (_, index) => index * h);
  const y = Array.from({ length: n }, (_, index) => index * h);
  const phi = zeros2(n, n);
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < n; j += 1) {
      phi[i][j] = Math.sin(mx * Math.PI * x[i]) * Math.sin(my * Math.PI * y[j]);
    }
  }
  return {
    Ux: gradientAxis(phi, h, 0),
    Uy: gradientAxis(phi, h, 1),
  };
}

function gramProjectorFromColumns(columns) {
  if (!columns.length) return null;
  const gram = columns.map((left) => columns.map((right) => dot(left, right)));
  const inverse = invertMatrix(gram);
  if (!inverse) return null;
  let projector = zeros2(columns[0].length, columns[0].length);
  for (let i = 0; i < columns.length; i += 1) {
    for (let j = 0; j < columns.length; j += 1) {
      projector = addMat(projector, scaleMat(outer(columns[i], columns[j]), inverse[i][j]));
    }
  }
  return projector;
}

export function analyzeBoundedHodgeCompatible(config = {}) {
  const n = Math.max(Number(config.gridSize ?? 17), 9);
  const protectedModes = config.protectedModes ?? [[1, 1], [1, 2], [2, 1]];
  const disturbanceModes = config.disturbanceModes ?? [[1, 1], [2, 1], [1, 2]];
  const protectedWeights = config.protectedWeights ?? protectedModes.map((_, index) => 1 + 0.2 * index);
  const disturbanceWeights = config.disturbanceWeights ?? disturbanceModes.map((_, index) => 0.7 - 0.15 * index);

  const protectedColumns = protectedModes.map(([mx, my]) => {
    const mode = boundedStreamVelocityMode(n, mx, my);
    return stackFieldVector(mode.Ux, mode.Uy);
  });
  const disturbanceColumns = disturbanceModes.map(([mx, my]) => {
    const mode = boundedGradientMode(n, mx, my);
    return stackFieldVector(mode.Ux, mode.Uy);
  });

  const protectedState = protectedColumns.reduce(
    (acc, column, index) => addVec(acc, scaleVec(column, protectedWeights[index])),
    zeros(protectedColumns[0].length)
  );
  const disturbanceState = disturbanceColumns.reduce(
    (acc, column, index) => addVec(acc, scaleVec(column, disturbanceWeights[index])),
    zeros(disturbanceColumns[0].length)
  );
  const state = addVec(protectedState, disturbanceState);

  const projectorQr = projectorFromBasis(protectedColumns, protectedColumns[0].length);
  const projectorGram = gramProjectorFromColumns(protectedColumns);
  const recovered = matVec(projectorQr, state);
  const recoveredIdempotent = matVec(projectorQr, recovered);

  const { Ux: protectedUx, Uy: protectedUy } = unstackFieldVector(protectedState, n);
  const { Ux: recoveredUx, Uy: recoveredUy } = unstackFieldVector(recovered, n);
  const h = 1 / (n - 1);
  const protectedDiv = boundedDivergence2d(protectedUx, protectedUy, h);
  const recoveredDiv = boundedDivergence2d(recoveredUx, recoveredUy, h);
  const qProtected = gramSchmidt(protectedColumns);
  const qDisturbance = gramSchmidt(disturbanceColumns);

  return {
    protectedDiv,
    recoveredDiv,
    protectedDivNorm: l2NormField(protectedDiv),
    recoveredDivNorm: l2NormField(recoveredDiv),
    protectedBoundaryNormalRms: boundaryNormalRms(protectedUx, protectedUy),
    recoveredBoundaryNormalRms: boundaryNormalRms(recoveredUx, recoveredUy),
    orthogonalityResidual: qProtected.length && qDisturbance.length
      ? frobeniusNorm(matMul(qProtected, transpose(qDisturbance)))
      : 0,
    recoveryError: rmsMetric(recovered, protectedState),
    idempotenceError: rmsMetric(recoveredIdempotent, recovered),
    projectorConstructionAgreement: projectorGram ? frobeniusNorm(subMat(projectorQr, projectorGram)) : null,
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
  const boundedCompatible = analyzeBoundedHodgeCompatible({ gridSize: Math.max(boundedGrid, 17) });
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
    boundedCompatibleProtectedDiv: boundedCompatible.protectedDiv,
    boundedCompatibleRecoveredDiv: boundedCompatible.recoveredDiv,
    boundedCompatibleProtectedDivNorm: boundedCompatible.protectedDivNorm,
    boundedCompatibleRecoveredDivNorm: boundedCompatible.recoveredDivNorm,
    boundedCompatibleProtectedBoundaryNormalRms: boundedCompatible.protectedBoundaryNormalRms,
    boundedCompatibleRecoveredBoundaryNormalRms: boundedCompatible.recoveredBoundaryNormalRms,
    boundedCompatibleOrthogonalityResidual: boundedCompatible.orthogonalityResidual,
    boundedCompatibleRecoveryError: boundedCompatible.recoveryError,
    boundedCompatibleIdempotenceError: boundedCompatible.idempotenceError,
    boundedCompatibleProjectorConstructionAgreement: boundedCompatible.projectorConstructionAgreement,
    divergenceOnlyWitness,
  };
}

