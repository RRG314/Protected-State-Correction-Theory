import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';
import {
  analyzeBenchmarkConsole,
  analyzeCfdProjection,
  analyzeContinuousGenerator,
  analyzeExactProjection,
  analyzeGaugeProjection,
  analyzeMhdProjection,
  analyzeNoGo,
  analyzeQecSector,
  analyzeRecoverability,
} from '../../docs/workbench/lib/compute.js';
import { analyzeDiscoveryMixer } from '../../docs/workbench/lib/discoveryMixer.js';
import { DEFAULT_STATE } from '../../docs/workbench/lib/state.js';

const ROOT = '/Users/stevenreid/Documents/New project/repos/ocp-research-program';
const OUT = resolve(ROOT, 'data/generated/validations/workbench_examples.json');
mkdirSync(resolve(ROOT, 'data/generated/validations'), { recursive: true });

const examples = {
  recoverability: analyzeRecoverability(DEFAULT_STATE.labs.recoverability),
  recoverabilityQubit: analyzeRecoverability({
    ...DEFAULT_STATE.labs.recoverability,
    system: 'qubit',
    qubitProtected: 'bloch_vector',
    qubitPhaseWindowDeg: 30,
    qubitDelta: 0.2,
  }),
  recoverabilityControl: analyzeRecoverability({
    ...DEFAULT_STATE.labs.recoverability,
    system: 'control',
    controlEpsilon: 0.2,
    controlHorizon: 2,
    controlDelta: 0.5,
  }),
  recoverabilityPeriodicThreshold: analyzeRecoverability({
    ...DEFAULT_STATE.labs.recoverability,
    system: 'periodic',
    periodicProtected: 'bandlimited_contrast',
    periodicObservation: 'cutoff_vorticity',
    periodicCutoff: 3,
    periodicDelta: 1.0,
  }),
  recoverabilityControlThreshold: analyzeRecoverability({
    ...DEFAULT_STATE.labs.recoverability,
    system: 'control',
    controlMode: 'diagonal_threshold',
    controlProfile: 'three_active',
    controlFunctional: 'second_moment',
    controlHorizon: 3,
    controlDelta: 0.5,
  }),
  recoverabilityBoundaryArchitecture: analyzeRecoverability({
    ...DEFAULT_STATE.labs.recoverability,
    system: 'boundary',
    boundaryArchitecture: 'periodic_transplant',
    boundaryProtected: 'bounded_velocity_class',
    boundaryGridSize: 17,
    boundaryDelta: 0.2,
  }),
  mixerStructuredLinear: analyzeDiscoveryMixer({
    ...DEFAULT_STATE.labs.mixer,
    mode: 'structured',
    family: 'linear',
  }),
  mixerPeriodicDemo: analyzeDiscoveryMixer({
    ...DEFAULT_STATE.labs.mixer,
    mode: 'demo',
    demoKey: 'periodic_builder',
  }),
  mixerCustomLinear: analyzeDiscoveryMixer({
    ...DEFAULT_STATE.labs.mixer,
    mode: 'custom',
    customFamily: 'linear',
    customLinearDimension: 3,
    customLinearObservationText: 'x1\nx2 + x3',
    customLinearProtectedText: 'x3',
    customLinearCandidateText: 'x2\nx3\nx1 + x2',
  }),
  mixerBoundary: analyzeDiscoveryMixer({
    ...DEFAULT_STATE.labs.mixer,
    mode: 'structured',
    family: 'boundary',
    structuredBoundaryArchitecture: 'periodic_transplant',
    structuredBoundaryProtected: 'bounded_velocity_class',
  }),
  exact: analyzeExactProjection(DEFAULT_STATE.labs.exact),
  qec: analyzeQecSector(DEFAULT_STATE.labs.qec),
  mhd: analyzeMhdProjection(DEFAULT_STATE.labs.mhd),
  cfd: analyzeCfdProjection(DEFAULT_STATE.labs.cfd),
  gauge: analyzeGaugeProjection(DEFAULT_STATE.labs.gauge ?? DEFAULT_STATE.labs.mhd),
  continuous: analyzeContinuousGenerator(DEFAULT_STATE.labs.continuous),
  nogo: analyzeNoGo(DEFAULT_STATE.labs.nogo),
  boundaryNoGo: analyzeNoGo({ example: 'boundary' }),
  benchmark: analyzeBenchmarkConsole(DEFAULT_STATE.labs.benchmark),
};

writeFileSync(OUT, JSON.stringify(examples, null, 2));
console.log(`wrote ${OUT}`);
