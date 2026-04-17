import { buildResultEnvelope } from '../domain/resultModel.js';
import { sanitizeState } from './scenarioSerialization.js';

export function scenarioEvidenceLevel(state, analysis) {
  const activeLab = sanitizeState(state).activeLab;
  if (activeLab === 'recoverability') {
    if (state.labs.recoverability.system === 'linear') return 'restricted theorem-backed (restricted-linear)';
    if (state.labs.recoverability.system === 'boundary') {
      return state.labs.recoverability.boundaryArchitecture === 'boundary_compatible_hodge'
        ? 'restricted theorem-backed (bounded-domain finite-mode Hodge)'
        : 'theorem-backed counterexample (bounded-domain transplant limit)';
    }
    if (state.labs.recoverability.system === 'analytic') return 'validated family-specific (analytic benchmark)';
    if (state.labs.recoverability.system === 'qubit') return 'validated family-specific (qubit record family)';
    if (state.labs.recoverability.system === 'periodic') return 'validated family-specific (periodic threshold family)';
    if (state.labs.recoverability.system === 'control') return 'validated family-specific (control threshold/asymptotic benchmark)';
  }
  if (activeLab === 'exact' || activeLab === 'qec' || activeLab === 'mhd' || activeLab === 'gauge') {
    return 'theorem-backed';
  }
  if (activeLab === 'cfd' || activeLab === 'nogo' || activeLab === 'continuous') {
    return 'validated family-specific';
  }
  if (activeLab === 'benchmark') {
    return 'benchmark empirical';
  }
  if (activeLab === 'mixer') return analysis?.theoremStatus ?? 'validated family-specific (typed composition)';
  return analysis?.theoremStatus ?? 'validated family-specific';
}

function formatValue(value) {
  if (typeof value === 'number') {
    if (!Number.isFinite(value)) return String(value);
    if (Math.abs(value) >= 1000 || (Math.abs(value) > 0 && Math.abs(value) < 1e-2)) {
      return value.toExponential(3);
    }
    return value.toFixed(3);
  }
  if (typeof value === 'string') return value;
  if (typeof value === 'boolean') return value ? 'yes' : 'no';
  return JSON.stringify(value, null, 2);
}

function configLines(config) {
  return Object.entries(config)
    .map(([key, value]) => `- \`${key}\`: ${formatValue(value)}`)
    .join('\n');
}

function metricLines(analysis) {
  const pairs = [];
  for (const [key, value] of Object.entries(analysis ?? {})) {
    if (['number', 'string', 'boolean'].includes(typeof value)) {
      pairs.push([key, value]);
      continue;
    }
    if (value && typeof value === 'object' && !Array.isArray(value)) {
      for (const [nestedKey, nestedValue] of Object.entries(value)) {
        if (['number', 'string', 'boolean'].includes(typeof nestedValue)) {
          pairs.push([`${key}.${nestedKey}`, nestedValue]);
        }
      }
    }
  }
  const trimmed = pairs.slice(0, 24);
  return trimmed.map(([key, value]) => `- \`${key}\`: ${formatValue(value)}`).join('\n');
}

export function exportScenarioPayload(state, analysis) {
  const safeState = sanitizeState(state);
  const evidenceLevel = scenarioEvidenceLevel(safeState, analysis);
  return {
    exportedAt: new Date().toISOString(),
    workbenchVersion: 'structural-discovery-v3',
    activeLab: safeState.activeLab,
    evidenceLevel,
    resultEnvelope: buildResultEnvelope({ activeLab: safeState.activeLab, evidenceLevel, analysis, state: safeState }),
    state: safeState,
    analysis,
  };
}

export function exportScenarioReport(state, analysis) {
  const safeState = sanitizeState(state);
  const activeLab = safeState.activeLab;
  const config = safeState.labs[activeLab];
  const evidenceLevel = scenarioEvidenceLevel(state, analysis);
  const resultEnvelope = buildResultEnvelope({ activeLab, evidenceLevel, analysis, state: safeState });
  const title = `Protected-State Correction Workbench Report — ${activeLab}`;
  const recommendations = Array.isArray(analysis?.recommendations)
    ? analysis.recommendations.map((item) => `- ${item.title}: ${item.rationale}`).join('\n')
    : '';
  const comparison = analysis?.comparison
    ? [
        `- before regime: ${analysis.comparison.beforeRegime}`,
        `- after regime: ${analysis.comparison.afterRegime}`,
        `- key metric: ${analysis.comparison.keyMetricName}`,
        `- before metric: ${formatValue(analysis.comparison.keyMetricBefore)}`,
        `- after metric: ${formatValue(analysis.comparison.keyMetricAfter)}`,
        `- narrative: ${analysis.comparison.narrative}`,
      ].join('\n')
    : '- no before/after comparison available for the current state';
  const benchmarkValidation =
    activeLab === 'benchmark' && analysis?.validationSnapshot
      ? [
          `- last validation snapshot: ${analysis.validationSnapshot.generatedAt ?? 'not generated'}`,
          `- known-answer checks: ${analysis.validationSnapshot.counts?.knownAnswerPassed ?? 0}/${analysis.validationSnapshot.counts?.knownAnswerTotal ?? 0}`,
          `- adversarial checks: ${analysis.validationSnapshot.counts?.adversarialPassed ?? 0}/${analysis.validationSnapshot.counts?.adversarialTotal ?? 0}`,
          `- workflow passes: ${analysis.validationSnapshot.counts?.workflowPassed ?? 0}/${analysis.validationSnapshot.counts?.workflowTotal ?? 0}`,
          `- guided discovery ready: ${analysis.validationSnapshot.readiness?.guidedDiscovery ? 'yes' : 'no'}`,
        ].join('\n')
      : null;
  const objectLines = Array.isArray(analysis?.objects)
    ? analysis.objects
        .map((item) => `- ${item.objectType}: ${item.label} (${item.supportStatus ?? item.theoremStatus ?? 'status not set'})`)
        .join('\n')
    : '';
  return [
    `# ${title}`,
    '',
    `- exported at: ${new Date().toISOString()}`,
    `- active lab: ${activeLab}`,
    `- evidence level: ${evidenceLevel}`,
    '',
    '## Summary',
    '',
    activeLab === 'recoverability'
      ? `${analysis?.status ?? 'Unknown'} — ${analysis?.classification ?? 'No classification available.'}`
      : `${analysis?.title ?? analysis?.systemLabel ?? activeLab} — ${analysis?.status ?? analysis?.classification ?? 'Workbench output'}`,
    '',
    '## Unified Result Envelope',
    '',
    `- regime: ${resultEnvelope.regime}`,
    analysis?.resultScopeLabel ? `- support scope: ${analysis.resultScopeLabel}` : null,
    analysis?.identifiabilityStatus ? `- identifiability status: ${analysis.identifiabilityStatus}` : null,
    analysis?.decisionPosture?.label ? `- decision posture: ${analysis.decisionPosture.label}` : null,
    `- root cause: ${resultEnvelope.rootCause}`,
    `- weaker targets: ${resultEnvelope.weakerTargets.length ? resultEnvelope.weakerTargets.join(', ') : 'none'}`,
    `- stronger target requirements: ${resultEnvelope.strongerTargetRequirements ?? 'none'}`,
    '',
    '## Configuration',
    '',
    configLines(config),
    '',
    '## Analysis',
    '',
    analysis?.structuralBlocker
      ? `- blocker: ${analysis.structuralBlocker}`
      : analysis?.summary
        ? `- summary: ${analysis.summary}`
        : '- summary: see metrics below',
    analysis?.fiberSummary ? `- fiber structure: ${analysis.fiberSummary}` : null,
    analysis?.missingStructure ? `- missing structure: ${analysis.missingStructure}` : null,
    analysis?.recommendedArchitecture ? `- recommended architecture: ${analysis.recommendedArchitecture}` : null,
    analysis?.decisionPosture?.rationale ? `- decision rationale: ${analysis.decisionPosture.rationale}` : null,
    analysis?.guidance?.noGo ? `- no-go / boundary: ${analysis.guidance.noGo}` : null,
    analysis?.falsePositiveWarnings?.length ? `- false-positive warnings: ${analysis.falsePositiveWarnings.join(' | ')}` : null,
    '',
    '## Key Metrics',
    '',
    metricLines(analysis),
    '',
    '## Recommendations',
    '',
    recommendations || '- no additional recommendation list for the current lab',
    '',
    activeLab === 'mixer' ? '## Typed Objects' : null,
    '',
    activeLab === 'mixer' ? objectLines || '- no typed object inventory available' : null,
    '',
    '## Before / After',
    '',
    comparison,
    '',
    '## Reproducibility',
    '',
    '- export source: static Protected-State Correction Workbench',
    '- data origin: current in-browser configuration and analysis result',
    '- provenance: use the JSON export for exact state replay and the share link for direct UI reconstruction',
    '',
    activeLab === 'benchmark' ? '## Validation Snapshot' : null,
    '',
    activeLab === 'benchmark' ? benchmarkValidation ?? '- no validation snapshot available' : null,
    '',
  ]
    .filter(Boolean)
    .join('\n');
}

export function exportScenarioCsv(state, analysis) {
  const activeLab = sanitizeState(state).activeLab;
  if (activeLab === 'recoverability') {
    const rows = [['series', 'x', 'y']];
    if (Array.isArray(analysis?.deltas) && Array.isArray(analysis?.collapse)) {
      analysis.deltas.forEach((delta, index) => {
        rows.push(['collapse', String(delta), String(analysis.collapse[index])]);
      });
    }
    if (Array.isArray(analysis?.thresholdCutoffs) && Array.isArray(analysis?.thresholdKappa0)) {
      analysis.thresholdCutoffs.forEach((cutoff, index) => {
        rows.push(['threshold_kappa0', String(cutoff), String(analysis.thresholdKappa0[index])]);
      });
    }
    if (Array.isArray(analysis?.historyThreshold)) {
      analysis.historyThreshold.forEach((item) => {
        rows.push(['history_threshold', String(item.horizon), String(item.kappa0)]);
      });
    }
    if (Array.isArray(analysis?.boundaryArchitectureSeries)) {
      analysis.boundaryArchitectureSeries.forEach((item) => {
        rows.push(['boundary_architecture', String(item.x), String(item.y)]);
      });
    }
    return rows.map((row) => row.join(',')).join('\n');
  }
  if (activeLab === 'benchmark' && Array.isArray(analysis?.demoRows)) {
    const header = ['demo', 'family', 'before_regime', 'after_regime', 'metric_name', 'metric_before', 'metric_after', 'fix'];
    const body = analysis.demoRows.map((row) =>
      [row.demo, row.family, row.beforeRegime, row.afterRegime, row.metricName, row.metricBefore, row.metricAfter, row.fixTitle]
        .map((value) => `"${String(value).replaceAll('"', '""')}"`)
        .join(',')
    );
    return [header.join(','), ...body].join('\n');
  }
  if (activeLab === 'mixer' && Array.isArray(analysis?.exportRows) && analysis.exportRows.length) {
    const header = Object.keys(analysis.exportRows[0]);
    const body = analysis.exportRows.map((row) =>
      header.map((key) => `"${String(row[key] ?? '').replaceAll('"', '""')}"`).join(',')
    );
    return [header.join(','), ...body].join('\n');
  }
  return null;
}
