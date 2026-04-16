import { analyzeContinuousGenerator } from './continuousEngine.js';
import { analyzeCfdProjection, analyzeBoundaryProjectionLimit } from './physicsEngine.js';

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
