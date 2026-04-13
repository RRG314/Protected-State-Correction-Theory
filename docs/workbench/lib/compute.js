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
  const { h, Bx, By } = makeField(n, contamination);
  const beforeDiv = divergence2d(Bx, By, h);
  const projection = helmholtzProject2d(Bx, By, h, Number(config.poissonIterations));
  const afterExactDiv = divergence2d(projection.BxProj, projection.ByProj, h);
  let psi = zeros2(n, n);
  let BxGlm = cloneMatrix(Bx);
  let ByGlm = cloneMatrix(By);
  const glmHistory = [l2NormField(beforeDiv)];
  for (let step = 0; step < glmSteps; step += 1) {
    const next = glmStep2d(BxGlm, ByGlm, psi, h, Number(config.dt), Number(config.ch), Number(config.cp));
    BxGlm = next.Bx;
    ByGlm = next.By;
    psi = next.psi;
    glmHistory.push(l2NormField(divergence2d(BxGlm, ByGlm, h)));
  }
  const afterGlmDiv = divergence2d(BxGlm, ByGlm, h);
  return {
    beforeDiv,
    afterExactDiv,
    afterGlmDiv,
    beforeNorm: l2NormField(beforeDiv),
    afterExactNorm: l2NormField(afterExactDiv),
    afterGlmNorm: l2NormField(afterGlmDiv),
    glmHistory,
    exactImprovementFactor: l2NormField(beforeDiv) / Math.max(l2NormField(afterExactDiv), 1e-12),
    glmImprovementFactor: l2NormField(beforeDiv) / Math.max(l2NormField(afterGlmDiv), 1e-12),
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
  const kernelBasis = nullSpace(K);
  const disturbanceBasis = orthogonalComplement(kernelBasis, K.length);
  const pS = projectorFromBasis(kernelBasis, K.length);
  const pD = projectorFromBasis(disturbanceBasis, K.length);
  const path = rungeKutta4(K, x0, Number(config.time), Number(config.steps));
  const xt = path[path.length - 1];
  const protectedDrift = norm(subVec(matVec(pS, xt), matVec(pS, x0)));
  const disturbanceNorms = path.map((point) => norm(matVec(pD, point)));
  const flow = flowMatrix(K, Number(config.time));
  const exactResidualMatrix = (() => {
    const ss = matMul(matMul(pS, flow), pS);
    const sd = matMul(matMul(pS, flow), pD);
    const ds = matMul(matMul(pD, flow), pS);
    const dd = matMul(matMul(pD, flow), pD);
    const pSOnly = matMul(pS, pS);
    return [frobeniusNorm(subMat(ss, pSOnly)), frobeniusNorm(sd), frobeniusNorm(ds), frobeniusNorm(dd)];
  })();
  const mixingNorm = frobeniusNorm(matMul(matMul(pS, K), pD));
  return {
    kernelBasis,
    disturbanceBasis,
    protectedDrift,
    disturbanceBefore: disturbanceNorms[0],
    disturbanceAfter: disturbanceNorms[disturbanceNorms.length - 1],
    disturbanceNorms,
    path,
    xt,
    mixingNorm,
    exactRecoveryResidual: Math.max(...exactResidualMatrix),
    finiteTimeExactRecoveryPossible: disturbanceBasis.length === 0 ? true : Math.max(...exactResidualMatrix) < 1e-6,
  };
}

export function analyzeNoGo(config) {
  switch (config.example) {
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
