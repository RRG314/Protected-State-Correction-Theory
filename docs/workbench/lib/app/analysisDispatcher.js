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
} from '../compute.js';
import { analyzeDiscoveryMixer } from '../discoveryMixer.js';

export function analyzeLab(activeLab, labs) {
  switch (activeLab) {
    case 'mixer':
      return analyzeDiscoveryMixer(labs.mixer);
    case 'recoverability':
      return analyzeRecoverability(labs.recoverability);
    case 'benchmark':
      return analyzeBenchmarkConsole(labs.benchmark);
    case 'exact':
      return analyzeExactProjection(labs.exact);
    case 'qec':
      return analyzeQecSector(labs.qec);
    case 'mhd':
      return analyzeMhdProjection(labs.mhd);
    case 'cfd':
      return analyzeCfdProjection(labs.cfd);
    case 'gauge':
      return analyzeGaugeProjection(labs.gauge);
    case 'continuous':
      return analyzeContinuousGenerator(labs.continuous);
    case 'nogo':
    default:
      return analyzeNoGo(labs.nogo);
  }
}
