import { LATEST_VALIDATION_SNAPSHOT as SNAPSHOT } from '../generatedValidationSnapshot.js';

export const LATEST_VALIDATION_SNAPSHOT = SNAPSHOT;

export function emptyValidationSnapshot() {
  return {
    generatedAt: null,
    readiness: {
      knownCaseValidation: false,
      guidedDiscovery: false,
      unsupportedFreeExploration: false,
    },
    counts: {
      qualifiedModules: 0,
      knownAnswerPassed: 0,
      knownAnswerTotal: 0,
      workflowPassed: 0,
      workflowTotal: 0,
      adversarialPassed: 0,
      adversarialTotal: 0,
    },
    limitations: [],
    moduleHealth: [],
  };
}
