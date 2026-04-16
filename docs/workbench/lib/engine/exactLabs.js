import {
  EPS,
  zeros,
  dot,
  norm,
  addVec,
  subVec,
  scaleVec,
  matVec,
  projectorFromBasis,
  maxBasisOverlap,
} from './core/linearAlgebra.js';

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
