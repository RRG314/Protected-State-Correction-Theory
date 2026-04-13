import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';
import {
  analyzeContinuousGenerator,
  analyzeExactProjection,
  analyzeGaugeProjection,
  analyzeMhdProjection,
  analyzeNoGo,
  analyzeQecSector,
} from '../../docs/workbench/lib/compute.js';
import { DEFAULT_STATE } from '../../docs/workbench/lib/state.js';

const ROOT = '/Users/stevenreid/Documents/New project/repos/ocp-research-program';
const OUT = resolve(ROOT, 'data/generated/validations/workbench_examples.json');
mkdirSync(resolve(ROOT, 'data/generated/validations'), { recursive: true });

const examples = {
  exact: analyzeExactProjection(DEFAULT_STATE.labs.exact),
  qec: analyzeQecSector(DEFAULT_STATE.labs.qec),
  mhd: analyzeMhdProjection(DEFAULT_STATE.labs.mhd),
  gauge: analyzeGaugeProjection(DEFAULT_STATE.labs.gauge ?? DEFAULT_STATE.labs.mhd),
  continuous: analyzeContinuousGenerator(DEFAULT_STATE.labs.continuous),
  nogo: analyzeNoGo(DEFAULT_STATE.labs.nogo),
  boundaryNoGo: analyzeNoGo({ example: 'boundary' }),
};

writeFileSync(OUT, JSON.stringify(examples, null, 2));
console.log(`wrote ${OUT}`);
