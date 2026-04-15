import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';
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
    periodicProtected: 'full_modal_coefficients',
    periodicObservation: 'cutoff_vorticity',
    periodicCutoff: 2,
    periodicDelta: 1.0,
  }),
  recoverabilityControlThreshold: analyzeRecoverability({
    ...DEFAULT_STATE.labs.recoverability,
    system: 'control',
    controlMode: 'diagonal_threshold',
    controlProfile: 'three_active',
    controlHorizon: 3,
    controlDelta: 0.5,
  }),
  exact: analyzeExactProjection(DEFAULT_STATE.labs.exact),
  qec: analyzeQecSector(DEFAULT_STATE.labs.qec),
  mhd: analyzeMhdProjection(DEFAULT_STATE.labs.mhd),
  cfd: analyzeCfdProjection(DEFAULT_STATE.labs.cfd),
  gauge: analyzeGaugeProjection(DEFAULT_STATE.labs.gauge ?? DEFAULT_STATE.labs.mhd),
  continuous: analyzeContinuousGenerator(DEFAULT_STATE.labs.continuous),
  nogo: analyzeNoGo(DEFAULT_STATE.labs.nogo),
  boundaryNoGo: analyzeNoGo({ example: 'boundary' }),
};

writeFileSync(OUT, JSON.stringify(examples, null, 2));
console.log(`wrote ${OUT}`);
