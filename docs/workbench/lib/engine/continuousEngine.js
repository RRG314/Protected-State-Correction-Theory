import {
  clamp,
  zeros,
  identity,
  addVec,
  subVec,
  scaleVec,
  addMat,
  subMat,
  scaleMat,
  transpose,
  matVec,
  matMul,
  norm,
  frobeniusNorm,
  nullSpace,
  orthogonalComplement,
  projectorFromBasis,
} from './core/linearAlgebra.js';

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

