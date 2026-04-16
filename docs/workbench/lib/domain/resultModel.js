function inferRegime(analysis) {
  if (analysis?.unsupported) return 'unsupported';
  if (analysis?.exact) return 'exact';
  if (analysis?.asymptotic) return 'asymptotic';
  if (analysis?.impossible) return 'impossible';
  if (analysis?.approximate) return 'approximate';
  if (typeof analysis?.regime === 'string') return analysis.regime;
  return 'conditional';
}

function quantitativeSummary(analysis) {
  const summary = {};
  for (const key of [
    'selectedDelta',
    'selectedKappa',
    'kappa0',
    'selectedLowerBound',
    'meanRecoveryError',
    'maxRecoveryError',
    'predictedMinCutoff',
    'predictedMinHorizon',
    'minimalAddedMeasurements',
    'unrestrictedMinimalAddedMeasurements',
    'transplantBoundaryMismatch',
    'compatibleRecoveryError',
    'mixingNorm',
    'exactRecoveryResidual',
  ]) {
    if (analysis?.[key] !== undefined) {
      summary[key] = analysis[key];
    }
  }
  return summary;
}

export function buildResultEnvelope({ activeLab, evidenceLevel, analysis, state }) {
  return {
    lab: activeLab,
    regime: inferRegime(analysis),
    rootCause:
      analysis?.rootCause
      ?? analysis?.structuralBlocker
      ?? analysis?.summary
      ?? analysis?.classification
      ?? analysis?.status
      ?? 'No root-cause summary available.',
    evidenceLevel,
    theoremLinks: analysis?.theoremLinks ?? [],
    quantitativeSummary: quantitativeSummary(analysis),
    thresholdInfo: {
      predictedMinCutoff: analysis?.predictedMinCutoff ?? null,
      predictedMinHorizon: analysis?.predictedMinHorizon ?? null,
      thresholdCutoffs: analysis?.thresholdCutoffs ?? null,
      historyThreshold: analysis?.historyThreshold ?? null,
    },
    augmentationCandidates: analysis?.recommendations ?? [],
    weakerTargets:
      analysis?.weakerRecoverableTargets
      ?? analysis?.weakerProtectedOptions
      ?? analysis?.weakerBoundaryTargets
      ?? [],
    strongerTargetRequirements: analysis?.missingStructure ?? null,
    beforeScenario: analysis?.comparison ? {
      regime: analysis.comparison.beforeRegime,
      metricName: analysis.comparison.keyMetricName,
      metricValue: analysis.comparison.keyMetricBefore,
    } : null,
    afterScenario: analysis?.comparison ? {
      regime: analysis.comparison.afterRegime,
      metricName: analysis.comparison.keyMetricName,
      metricValue: analysis.comparison.keyMetricAfter,
    } : null,
    warnings: analysis?.unsupported ? ['unsupported input or unsupported family reduction'] : [],
    reproducibility: {
      activeLab,
      state: state?.labs?.[activeLab] ?? null,
    },
  };
}
