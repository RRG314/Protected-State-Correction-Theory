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
import {
  DEFAULT_STATE,
  cloneState,
  decodeShareState,
  encodeShareState,
  exportScenarioCsv,
  exportScenarioPayload,
  exportScenarioReport,
  sanitizeState,
  scenarioEvidenceLevel,
} from '../../docs/workbench/lib/state.js';

function parseArgs(argv) {
  const out = {};
  for (let i = 2; i < argv.length; i += 1) {
    const key = argv[i];
    const value = argv[i + 1];
    if (key.startsWith('--')) {
      out[key.slice(2)] = value;
      i += 1;
    }
  }
  return out;
}

function analyzeLab(lab, config) {
  switch (lab) {
    case 'exact':
      return analyzeExactProjection(config);
    case 'qec':
      return analyzeQecSector(config);
    case 'mhd':
      return analyzeMhdProjection(config);
    case 'cfd':
      return analyzeCfdProjection(config);
    case 'gauge':
      return analyzeGaugeProjection(config);
    case 'continuous':
      return analyzeContinuousGenerator(config);
    case 'nogo':
      return analyzeNoGo(config);
    case 'benchmark':
      return analyzeBenchmarkConsole(config);
    case 'mixer':
      return analyzeDiscoveryMixer(config);
    case 'recoverability':
    default:
      return analyzeRecoverability(config);
  }
}

const args = parseArgs(process.argv);
const lab = args.lab ?? 'recoverability';
const config = args['config-json'] ? JSON.parse(args['config-json']) : {};

const state = cloneState(DEFAULT_STATE);
state.activeLab = lab;
state.labs[lab] = { ...state.labs[lab], ...config };
const safeState = sanitizeState(state);
const analysis = analyzeLab(lab, safeState.labs[lab]);
const shareState = encodeShareState(safeState);
const decoded = decodeShareState(`#state=${shareState}`);
const payload = exportScenarioPayload(safeState, analysis);
const report = exportScenarioReport(safeState, analysis);
const csv = exportScenarioCsv(safeState, analysis);
const output = {
  lab,
  config: safeState.labs[lab],
  analysis,
  payload,
  report,
  csv,
  evidenceLevel: scenarioEvidenceLevel(safeState, analysis),
  shareState,
  roundtripState: decoded,
  roundtripMatches: JSON.stringify(decoded) === JSON.stringify(safeState),
};

process.stdout.write(`${JSON.stringify(output, null, 2)}\n`);
