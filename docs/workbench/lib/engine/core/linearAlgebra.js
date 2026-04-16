export const EPS = 1e-10;

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

export function invertMatrix(matrix, tol = EPS) {
  const n = matrix.length;
  const augmented = matrix.map((row, i) => [...row, ...identity(n)[i]]);
  const { matrix: reduced, pivots } = rref(augmented, tol);
  if (pivots.length < n) return null;
  return reduced.map((row) => row.slice(n));
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

