import { LINEAR_TEMPLATE_LIBRARY } from '../domain/templates.js';
import { DIAGONAL_EIGENVALUES, DISCOVERY_MIXER_LIBRARY, DISCOVERY_MIXER_DEMOS } from '../domain/discoveryMixerCatalog.js';
import { clamp, matrixRank, minimalRowAugmentation, norm, nullSpace, rowSpaceResidual } from './core/linearAlgebra.js';
import { analyzeRecoverability, diagonalRecordMatrix, solveLeastSquares } from './recoverabilityEngine.js';
import { analyzeBoundaryProjectionLimit } from './physicsEngine.js';

const EPS = 1e-10;

function capitalize(value) {
  return value.charAt(0).toUpperCase() + value.slice(1);
}

function boxCollisionGap(observationRows, protectedRows, boxRadius = 1) {
  const basis = nullSpace(observationRows.length ? observationRows : [[0, 0, 0]]);
  if (!basis.length) return 0;
  const bound = 2 * boxRadius;
  if (basis.length === 1) {
    const direction = basis[0];
    const protectedGains = protectedRows.map((row) => row.reduce((sum, value, index) => sum + value * direction[index], 0));
    const protectedGain = norm(protectedGains);
    if (protectedGain <= EPS) return 0;
    const coordinateLimits = direction.filter((value) => Math.abs(value) > EPS).map((value) => bound / Math.abs(value));
    if (!coordinateLimits.length) return 0;
    return protectedGain * Math.min(...coordinateLimits);
  }
  let best = 0;
  const signCount = 1 << basis.length;
  for (let mask = 0; mask < signCount; mask += 1) {
    const alpha = basis.map((_, index) => (mask & (1 << index) ? bound : -bound));
    const stateGap = Array.from({ length: basis[0].length }, (_, row) => basis.reduce((sum, vector, col) => sum + vector[row] * alpha[col], 0));
    if (stateGap.some((value) => Math.abs(value) > bound + 1e-9)) continue;
    const protectedGap = norm(protectedRows.map((row) => row.reduce((sum, value, index) => sum + value * stateGap[index], 0)));
    best = Math.max(best, protectedGap);
  }
  return best;
}

function parseNumericRows(text) {
  return text
    .replaceAll(';', '\n')
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => line.split(/[\s,]+/).filter(Boolean).map((token) => Number(token)));
}

function expressionTokens(expr) {
  let normalized = expr.replace(/\s+/g, '');
  if (!normalized) return [];
  normalized = normalized.replace(/-/g, '+-');
  if (normalized.startsWith('+-')) normalized = `-${normalized.slice(2)}`;
  return normalized.split('+').filter(Boolean);
}

function parseLinearExpression(expr, { prefix, dimension }) {
  const text = expr.trim();
  if (!text) throw new Error('empty expression');
  if (/[^0-9A-Za-z_+\-*.\s]/.test(text)) throw new Error('unsupported characters in expression');
  if (/\b(sin|cos|exp|log)\b/.test(text) || /[\^/@]/.test(text)) throw new Error('nonlinear or unsupported syntax in expression');
  const coeffs = Array.from({ length: dimension }, () => 0);
  for (const token of expressionTokens(text)) {
    if (/^[+-]?\d+(?:\.\d+)?$/.test(token)) {
      throw new Error('constant offsets are not supported in protected or observation expressions');
    }
    const match = token.match(new RegExp(`^([+-]?(?:\\d+(?:\\.\\d+)?)?)\\*?(${prefix}(\\d+))$`));
    if (!match) throw new Error(`unsupported token: ${token}`);
    const coeffText = match[1];
    const varIndex = Number(match[3]) - 1;
    if (varIndex < 0 || varIndex >= dimension) throw new Error(`variable ${prefix}${varIndex + 1} is outside the declared basis size ${dimension}`);
    let coeff = 1;
    if (coeffText === '-' ) coeff = -1;
    else if (coeffText && coeffText !== '+') coeff = Number(coeffText);
    coeffs[varIndex] += coeff;
  }
  if (norm(coeffs) <= EPS) throw new Error('expression reduces to the zero functional');
  return coeffs;
}

function parseRows(text, { prefix, dimension }) {
  const rows = text
    .replaceAll(';', '\n')
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => (/[A-Za-z]/.test(line) ? parseLinearExpression(line, { prefix, dimension }) : line.split(/[\s,]+/).filter(Boolean).map(Number)));
  if (!rows.length) throw new Error('no rows were provided');
  const width = rows[0].length;
  if (width !== dimension) throw new Error(`row width ${width} does not match declared dimension ${dimension}`);
  if (rows.some((row) => row.length !== width)) throw new Error('rows must all have the same length');
  return rows;
}

function diagonalHistoryWeights(eigenvalues, sensorWeights, protectedWeights, horizon) {
  const active = sensorWeights.map((value, index) => ({ value, index })).filter((item) => Math.abs(item.value) > EPS);
  const inactive = sensorWeights.map((value, index) => ({ value, index })).filter((item) => Math.abs(item.value) <= EPS);
  if (inactive.some((item) => Math.abs(protectedWeights[item.index]) > EPS)) return null;
  if (!active.length) return null;
  const lambdas = active.map((item) => eigenvalues[item.index]);
  if (new Set(lambdas.map((value) => value.toFixed(12))).size !== lambdas.length) return null;
  const targets = active.map((item) => protectedWeights[item.index] / sensorWeights[item.index]);
  const vandermonde = active.map((item) => Array.from({ length: horizon }, (_, power) => eigenvalues[item.index] ** power));
  const solution = solveLeastSquares(vandermonde, targets);
  if (!solution) return null;
  const reconstructed = vandermonde.map((row) => row.reduce((sum, value, index) => sum + value * solution[index], 0));
  const residual = norm(reconstructed.map((value, index) => value - targets[index]));
  return residual <= 1e-8 ? solution : null;
}

function solveLinearSystem(matrix, rhs) {
  const a = matrix.map((row, index) => [...row, rhs[index]]);
  const rows = a.length;
  const cols = a[0].length - 1;
  let lead = 0;
  for (let r = 0; r < rows && lead < cols; r += 1) {
    let i = r;
    while (i < rows && Math.abs(a[i][lead]) < EPS) i += 1;
    if (i === rows) {
      lead += 1;
      r -= 1;
      continue;
    }
    [a[i], a[r]] = [a[r], a[i]];
    const pivot = a[r][lead];
    for (let j = lead; j <= cols; j += 1) a[r][j] /= pivot;
    for (let k = 0; k < rows; k += 1) {
      if (k === r) continue;
      const factor = a[k][lead];
      if (Math.abs(factor) < EPS) continue;
      for (let j = lead; j <= cols; j += 1) a[k][j] -= factor * a[r][j];
    }
    lead += 1;
  }
  const solution = Array.from({ length: cols }, () => 0);
  for (let i = 0; i < rows; i += 1) {
    const pivotIndex = a[i].findIndex((value, index) => index < cols && Math.abs(value) > 1e-8);
    if (pivotIndex >= 0) solution[pivotIndex] = a[i][cols];
  }
  return solution;
}

function controlTarget(text, dimension) {
  const cleaned = text.trim().toLowerCase();
  const momentMatch = cleaned.match(/^moment\((\d+)\)$/);
  if (momentMatch) {
    const order = Number(momentMatch[1]);
    return {
      label: `moment(${order})`,
      weights: DIAGONAL_EIGENVALUES.slice(0, dimension).map((value) => value ** order),
    };
  }
  const coordinateMatch = cleaned.match(/^x(\d+)$/);
  if (coordinateMatch) {
    const index = Number(coordinateMatch[1]) - 1;
    if (index < 0 || index >= dimension) throw new Error('coordinate target index is outside the sensor profile dimension');
    return {
      label: `x${index + 1}`,
      weights: Array.from({ length: dimension }, (_, idx) => (idx === index ? 1 : 0)),
    };
  }
  if (/[A-Za-z]/.test(cleaned)) {
    return {
      label: 'custom linear functional',
      weights: parseLinearExpression(cleaned, { prefix: 'x', dimension }),
    };
  }
  const weights = cleaned.split(/[\s,]+/).filter(Boolean).map(Number);
  if (weights.length !== dimension) throw new Error('custom control functional width does not match the sensor profile dimension');
  return { label: 'custom linear functional', weights };
}

function buildObjectsLinear(dimension, observationRows, protectedRows, candidateRows, supportStatus) {
  const objects = [
    {
      objectId: 'state-space', label: `${dimension}-dimensional state space`, objectType: 'state_space', family: 'linear', domain: '—', codomain: `R^${dimension}`,
      dimension: `${dimension}`, basis: Array.from({ length: dimension }, (_, index) => `x${index + 1}`).join(', '), linearStatus: 'linear', supportStatus,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theorem-candidates/capacity-theorems.md'],
      compatibilityRequirements: ['shared dimension', 'declared coordinate basis'], notes: ['admissible family is the coefficient box [-1,1]^n'],
    },
    {
      objectId: 'record-map', label: 'Observation / record map', objectType: 'record_map', family: 'linear', domain: `R^${dimension}`, codomain: `R^${observationRows.length}`,
      dimension: `${observationRows.length}x${dimension}`, basis: 'row representation', linearStatus: 'linear', supportStatus,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theorem-candidates/capacity-theorems.md'],
      compatibilityRequirements: ['row width must equal state dimension'], notes: [`${observationRows.length} active observation row(s)`],
    },
    {
      objectId: 'protected-target', label: 'Protected target', objectType: 'protected_variable', family: 'linear', domain: `R^${dimension}`, codomain: `R^${protectedRows.length}`,
      dimension: `${protectedRows.length}x${dimension}`, basis: 'row representation', linearStatus: 'linear', supportStatus,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theorem-candidates/capacity-theorems.md'],
      compatibilityRequirements: ['target rows must share state dimension'], notes: [`${protectedRows.length} protected row(s)`],
    },
  ];
  if (candidateRows.length) {
    objects.push({
      objectId: 'candidate-augmentations', label: 'Candidate augmentation library', objectType: 'augmentation_candidate', family: 'linear', domain: `R^${dimension}`, codomain: `R^${candidateRows.length}`,
      dimension: `${candidateRows.length}x${dimension}`, basis: 'row representation', linearStatus: 'linear', supportStatus,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theorem-candidates/capacity-theorems.md'],
      compatibilityRequirements: ['candidate rows must share state dimension'], notes: ['searched only inside the provided candidate library'],
    });
  }
  return objects;
}

function uppercaseRegime(regime) {
  return regime === 'exact' ? 'Exact' : regime === 'impossible' ? 'Impossible' : regime === 'asymptotic' ? 'Asymptotic' : regime === 'unsupported' ? 'Unsupported' : 'Approximate';
}

function analyzeCustomLinear(config) {
  const dimension = Math.max(1, Number(config.customLinearDimension ?? 3));
  try {
    const observationRows = parseRows(config.customLinearObservationText, { prefix: 'x', dimension });
    const protectedRows = parseRows(config.customLinearProtectedText, { prefix: 'x', dimension });
    const candidateRows = String(config.customLinearCandidateText ?? '').trim()
      ? parseRows(config.customLinearCandidateText, { prefix: 'x', dimension })
      : [];
    const exact = protectedRows.every((row) => rowSpaceResidual(observationRows, row) <= 1e-8);
    const collisionGap = boxCollisionGap(observationRows, protectedRows, 1);
    const rankObservation = observationRows.length ? matrixRank(observationRows) : 0;
    const rankProtected = protectedRows.length ? matrixRank(protectedRows) : 0;
    const augmentation = candidateRows.length ? minimalRowAugmentation(observationRows, protectedRows, candidateRows) : { minimalAdded: null, exactSets: [] };
    const weakerTargets = Array.from({ length: dimension }, (_, index) => index).filter((index) => rowSpaceResidual(observationRows, [Array.from({ length: dimension }, (_, j) => (j === index ? 1 : 0))][0]) <= 1e-8).map((index) => `coordinate x${index + 1}`);
    const rowResiduals = protectedRows.map((row) => rowSpaceResidual(observationRows, row));
    const recommendations = [];
    let comparison = null;
    let chosenRecommendation = null;
    if (!exact && augmentation.minimalAdded !== null && augmentation.exactSets.length) {
      const combo = augmentation.exactSets[0];
      const addedRows = combo.map((index) => candidateRows[index]);
      const afterRows = [...observationRows, ...addedRows];
      const afterGap = boxCollisionGap(afterRows, protectedRows, 1);
      chosenRecommendation = {
        title: `Add ${augmentation.minimalAdded} candidate row${augmentation.minimalAdded === 1 ? '' : 's'}`,
        actionKind: 'add_measurement',
        rationale: 'This is the smallest candidate-library augmentation that lifts the protected rows into the record row space.',
        theoremStatus: 'restricted theorem-backed (restricted-linear)',
        minimal: true,
        availableInStudio: true,
        patch: { mode: 'custom', customFamily: 'linear', customLinearObservationText: [...observationRows, ...addedRows].map((row) => row.join(',')).join('\n') },
      };
      recommendations.push(chosenRecommendation);
      comparison = {
        beforeRegime: 'impossible', afterRegime: 'exact', keyMetricName: 'κ(0)', keyMetricBefore: collisionGap, keyMetricAfter: afterGap,
        narrative: 'Adding the proposed rows removes the protected collision gap by repairing the row-space deficiency.', changed: true,
      };
    }
    if (!exact && weakerTargets.length) {
      recommendations.push({
        title: `Weaken target to ${weakerTargets[0]}`,
        actionKind: 'weaken_target',
        rationale: 'The current record already supports this weaker basis target exactly.',
        theoremStatus: 'restricted theorem-backed (restricted-linear)',
        minimal: false,
        availableInStudio: false,
      });
    }
    return {
      title: 'Custom restricted-linear composition',
      mode: 'custom',
      family: 'linear',
      familyLabel: 'Restricted-linear family',
      validity: 'supported',
      regime: exact ? 'exact' : 'impossible',
      status: uppercaseRegime(exact ? 'exact' : 'impossible'),
      exact,
      approximate: false,
      asymptotic: false,
      impossible: !exact,
      unsupported: false,
      theoremStatus: 'restricted theorem-backed (restricted-linear)',
      supportScope: 'Finite-dimensional restricted-linear family on an explicit coefficient box.',
      protectedLabel: `${protectedRows.length} protected row(s)`,
      observationLabel: `${observationRows.length} observation row(s)`,
      architectureLabel: 'restricted-linear exact recovery / augmentation search',
      targetSplitSummary: weakerTargets.length ? weakerTargets.join(', ') : 'No weaker basis target was automatically certified.',
      rootCause: exact ? 'Current record row space is sufficient.' : 'Current record row space is insufficient.',
      missingStructure: exact ? 'No structural augmentation is required.' : 'Add rows until the protected rows lie in the record row space.',
      objects: buildObjectsLinear(dimension, observationRows, protectedRows, candidateRows, 'restricted theorem-backed (restricted-linear)'),
      diagnostics: [
        {
          severity: exact ? 'success' : 'error',
          code: exact ? 'rowspace-supported' : 'rowspace-deficiency',
          title: exact ? 'Protected target lies in the record row space' : 'Record map does not separate the protected target',
          detail: exact ? 'The requested protected rows are already separated on the admissible family.' : 'At least one protected row lies outside the current observation row space on the admissible family.',
          theoremStatus: 'restricted theorem-backed (restricted-linear)',
        },
        ...(!exact ? [{ severity: 'warning', code: 'collision-gap', title: 'A protected collision gap survives at zero noise', detail: `The current κ(0) witness is ${collisionGap.toExponential(3)}.`, theoremStatus: 'restricted theorem-backed (restricted-linear)' }] : []),
      ],
      recommendations,
      chosenRecommendation,
      comparison,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theorem-candidates/capacity-theorems.md'],
      supportedCalculations: ['rank checks', 'row-space residual', 'collision-gap analysis', 'candidate-library minimal augmentation search', 'weaker basis-target scan'],
      rawDetails: {
        observationMatrix: observationRows,
        protectedMatrix: protectedRows,
        candidateRows,
        rankObservation,
        rankProtected,
        rowResiduals,
        collisionGap,
        selectedDelta: Number(config.customDelta ?? 1),
        minimalAddedRows: augmentation.minimalAdded,
        candidateExactSets: augmentation.exactSets,
        weakerBasisTargets: weakerTargets,
      },
      exportRows: [{ family: 'linear', regime: exact ? 'exact' : 'impossible', rankObservation, rankProtected, rowspaceResidual: Math.max(...rowResiduals), collisionGap, minimalAddedRows: augmentation.minimalAdded ?? -1 }],
    };
  } catch (error) {
    return {
      title: 'Custom restricted-linear composition',
      mode: 'custom',
      family: 'linear',
      familyLabel: 'Restricted-linear family',
      validity: 'unsupported',
      regime: 'unsupported',
      status: 'Unsupported',
      exact: false,
      approximate: false,
      asymptotic: false,
      impossible: false,
      unsupported: true,
      theoremStatus: 'unsupported',
      supportScope: 'Only matrix rows or linear functionals in x1..xn are supported here.',
      protectedLabel: 'unsupported protected target',
      observationLabel: 'unsupported custom record',
      architectureLabel: 'restricted-linear exact recovery',
      targetSplitSummary: 'No valid target split available because the input was not reducible.',
      rootCause: 'The custom expression or matrix text could not be parsed into a supported restricted-linear object.',
      missingStructure: 'Reformulate the input as rows or linear expressions in x1..xn.',
      objects: [],
      diagnostics: [{ severity: 'error', code: 'unsupported-custom-linear-input', title: 'Custom linear input could not be reduced to a supported class', detail: error.message, theoremStatus: 'unsupported' }],
      recommendations: [{ title: 'Reformulate as linear rows in x1..xn', actionKind: 'reformulate', rationale: 'The current engine only supports custom input that reduces to a matrix-defined restricted-linear family.', theoremStatus: 'unsupported -> nearest supported template', minimal: false, availableInStudio: false }],
      chosenRecommendation: null,
      comparison: null,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theorem-candidates/capacity-theorems.md'],
      supportedCalculations: ['syntax validation', 'object-class detection'],
      rawDetails: { dimension },
      exportRows: [],
    };
  }
}

function analyzeCustomPeriodic(config) {
  try {
    const coeffs = parseLinearExpression(config.customPeriodicFunctionalText, { prefix: 'a', dimension: 4 });
    const observation = config.customPeriodicObservation ?? 'cutoff_vorticity';
    const cutoff = Number(config.customPeriodicCutoff ?? 2);
    const visible = coeffs.slice();
    let exact = false;
    let impossible = false;
    let predictedMinCutoff = null;
    let hiddenL1 = 0;
    let rootCause = '';
    let missingStructure = '';
    if (observation === 'full_vorticity') {
      exact = true;
      rootCause = 'Full vorticity sees the whole protected support on this finite family.';
      missingStructure = 'No structural change is needed.';
    } else if (observation === 'cutoff_vorticity') {
      predictedMinCutoff = coeffs.reduce((best, value, index) => (Math.abs(value) > EPS ? Math.max(best, index + 1) : best), 0);
      for (let i = cutoff; i < visible.length; i += 1) visible[i] = 0;
      hiddenL1 = coeffs.slice(cutoff).reduce((sum, value) => sum + Math.abs(value), 0);
      exact = hiddenL1 <= EPS;
      impossible = !exact;
      rootCause = impossible ? 'The retained cutoff misses part of the protected modal support.' : 'The retained cutoff contains the whole protected support.';
      missingStructure = impossible ? `Raise the cutoff to at least ${predictedMinCutoff}.` : 'No structural change is needed.';
    } else {
      hiddenL1 = coeffs.reduce((sum, value) => sum + Math.abs(value), 0);
      exact = hiddenL1 <= EPS;
      impossible = !exact;
      rootCause = impossible ? 'Divergence-only data is blind to the modal target on this finite family.' : 'The target is trivial under divergence-only data.';
      missingStructure = impossible ? 'Switch to a richer record or weaken the target to visible support.' : 'No structural change is needed.';
    }
    const kappa0 = 2 * hiddenL1;
    const recommendations = [];
    let chosenRecommendation = null;
    let comparison = null;
    if (impossible && observation === 'cutoff_vorticity' && predictedMinCutoff !== null) {
      chosenRecommendation = {
        title: `Raise cutoff to ${predictedMinCutoff}`,
        actionKind: 'add_mode',
        rationale: 'Exact recovery begins at the first cutoff containing the whole protected support.',
        theoremStatus: 'family-specific periodic threshold result',
        minimal: true,
        availableInStudio: true,
        patch: { mode: 'custom', customFamily: 'periodic', customPeriodicCutoff: predictedMinCutoff },
      };
      recommendations.push(chosenRecommendation);
      comparison = { beforeRegime: 'impossible', afterRegime: 'exact', keyMetricName: 'κ(0)', keyMetricBefore: kappa0, keyMetricAfter: 0, narrative: 'Raising the cutoff removes every hidden protected coefficient from the zero-noise collision set.', changed: true };
    } else if (impossible && observation === 'divergence_only') {
      chosenRecommendation = {
        title: 'Switch to full vorticity',
        actionKind: 'switch_architecture',
        rationale: 'The divergence-only record is structurally blind to the periodic modal target.',
        theoremStatus: 'family-specific no-go',
        minimal: true,
        availableInStudio: true,
        patch: { mode: 'custom', customFamily: 'periodic', customPeriodicObservation: 'full_vorticity' },
      };
      recommendations.push(chosenRecommendation);
      comparison = { beforeRegime: 'impossible', afterRegime: 'exact', keyMetricName: 'κ(0)', keyMetricBefore: kappa0, keyMetricAfter: 0, narrative: 'Switching to a vorticity record resolves the modal coefficients the divergence-only record misses.', changed: true };
    }
    if (impossible && norm(visible) > EPS) {
      const visibleExpr = visible.map((value, index) => (Math.abs(value) > EPS ? `${value}*a${index + 1}` : null)).filter(Boolean).join(' + ');
      recommendations.push({ title: 'Weaken target to visible support only', actionKind: 'weaken_target', rationale: 'The visible part of the functional already lives on the retained support.', theoremStatus: 'family-specific periodic threshold result', minimal: false, availableInStudio: true, patch: { mode: 'custom', customFamily: 'periodic', customPeriodicFunctionalText: visibleExpr || 'a1' } });
    }
    return {
      title: 'Custom periodic modal composition',
      mode: 'custom',
      family: 'periodic',
      familyLabel: 'Periodic four-mode modal family',
      validity: 'supported',
      regime: exact ? 'exact' : 'impossible',
      status: uppercaseRegime(exact ? 'exact' : 'impossible'),
      exact,
      approximate: false,
      asymptotic: false,
      impossible,
      unsupported: false,
      theoremStatus: 'family-specific periodic threshold result',
      supportScope: 'Periodic four-mode family with linear modal functionals.',
      protectedLabel: config.customPeriodicFunctionalText,
      observationLabel: observation.replaceAll('_', ' '),
      architectureLabel: 'periodic modal threshold analysis',
      targetSplitSummary: impossible && norm(visible) > EPS ? 'The visible-support truncation is recoverable under the same record.' : 'No weaker same-record target was generated.',
      rootCause,
      missingStructure,
      objects: [
        { objectId: 'periodic-basis', label: 'Periodic four-mode basis', objectType: 'state_space', family: 'periodic', domain: '—', codomain: 'R^4', dimension: '4', basis: 'a1..a4', linearStatus: 'linear', supportStatus: 'family-specific periodic threshold result', theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../cfd/incompressible-projection.md'], compatibilityRequirements: ['modal basis fixed to a1..a4'], notes: ['supported periodic toy family'] },
        { objectId: 'periodic-record', label: observation.replaceAll('_', ' '), objectType: 'record_map', family: 'periodic', domain: 'R^4', codomain: 'record space', dimension: 'family-specific', basis: 'modal/vorticity', linearStatus: 'linear', supportStatus: 'family-specific periodic threshold result', theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../cfd/incompressible-projection.md'], compatibilityRequirements: ['record must be one of the supported periodic choices'], notes: [observation === 'cutoff_vorticity' ? `cutoff=${cutoff}` : 'record has fixed support semantics'] },
        { objectId: 'periodic-target', label: 'Custom modal functional', objectType: 'protected_variable', family: 'periodic', domain: 'R^4', codomain: 'R', dimension: '1x4', basis: 'a1..a4', linearStatus: 'linear', supportStatus: 'family-specific periodic threshold result', theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../cfd/incompressible-projection.md'], compatibilityRequirements: ['functional must be linear in a1..a4'], notes: [config.customPeriodicFunctionalText] },
      ],
      diagnostics: [{ severity: exact ? 'success' : 'error', code: 'periodic-support-check', title: 'Protected support versus retained support', detail: rootCause, theoremStatus: 'family-specific periodic threshold result' }],
      recommendations,
      chosenRecommendation,
      comparison,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../cfd/incompressible-projection.md'],
      supportedCalculations: ['support analysis', 'exact/impossible cutoff logic', 'same-record weaker-target detection'],
      rawDetails: { coefficients: coeffs, visibleCoefficients: visible, hiddenL1, kappa0, predictedMinCutoff, selectedDelta: Number(config.customDelta ?? 2) },
      exportRows: [{ family: 'periodic', regime: exact ? 'exact' : 'impossible', observation, cutoff, kappa0, predictedMinCutoff: predictedMinCutoff ?? -1 }],
    };
  } catch (error) {
    return {
      title: 'Custom periodic modal composition',
      mode: 'custom', family: 'periodic', familyLabel: 'Periodic four-mode modal family', validity: 'unsupported', regime: 'unsupported', status: 'Unsupported', exact: false, approximate: false, asymptotic: false, impossible: false, unsupported: true,
      theoremStatus: 'unsupported', supportScope: 'Only linear functionals in a1..a4 are supported.', protectedLabel: 'unsupported periodic target', observationLabel: (config.customPeriodicObservation ?? 'cutoff_vorticity').replaceAll('_', ' '), architectureLabel: 'periodic modal recovery', targetSplitSummary: 'No supported target split available.', rootCause: 'The periodic target could not be reduced to a supported modal functional.', missingStructure: 'Reformulate the target as a linear combination of a1..a4.', objects: [], diagnostics: [{ severity: 'error', code: 'unsupported-periodic-expression', title: 'Periodic functional is unsupported', detail: error.message, theoremStatus: 'unsupported' }], recommendations: [{ title: 'Use a linear modal functional in a1..a4', actionKind: 'reformulate', rationale: 'The current engine only supports modal functionals on the explicit four-mode basis.', theoremStatus: 'unsupported -> nearest supported template', minimal: false, availableInStudio: false }], chosenRecommendation: null, comparison: null,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../cfd/incompressible-projection.md'], supportedCalculations: ['syntax validation'], rawDetails: { functionalText: config.customPeriodicFunctionalText }, exportRows: [],
    };
  }
}

function analyzeCustomControl(config) {
  try {
    const sensorWeights = String(config.customControlSensorProfileText ?? '')
      .trim()
      .split(/[\s,]+/)
      .filter(Boolean)
      .map(Number);
    if (sensorWeights.length < 2) throw new Error('at least two sensor weights are required');
    const dimension = sensorWeights.length;
    const target = controlTarget(config.customControlTargetText ?? 'x3', dimension);
    const eigenvalues = DIAGONAL_EIGENVALUES.slice(0, dimension);
    const horizon = Math.max(1, Number(config.customControlHorizon ?? 2));
    const recordMatrix = diagonalRecordMatrix(eigenvalues, sensorWeights, horizon);
    const exact = rowSpaceResidual(recordMatrix, target.weights) <= 1e-8;
    const predictedMinHorizon = (() => {
      for (let h = 1; h <= dimension; h += 1) {
        if (diagonalHistoryWeights(eigenvalues, sensorWeights, target.weights, h)) return h;
      }
      return null;
    })();
    const collisionGap = boxCollisionGap(recordMatrix, [target.weights], 1);
    const weakerTargets = Array.from({ length: 4 }, (_, order) => ({ order, weights: eigenvalues.map((value) => value ** order) }))
      .filter((item) => diagonalHistoryWeights(eigenvalues, sensorWeights, item.weights, horizon))
      .map((item) => `moment(${item.order})`);
    const recommendations = [];
    let chosenRecommendation = null;
    let comparison = null;
    if (!exact && predictedMinHorizon !== null && predictedMinHorizon > horizon) {
      chosenRecommendation = {
        title: `Increase horizon to ${predictedMinHorizon}`,
        actionKind: 'add_history',
        rationale: 'The current horizon is too short to interpolate the requested protected functional from the diagonal history record.',
        theoremStatus: 'family-specific diagonal/history threshold result',
        minimal: true,
        availableInStudio: true,
        patch: { mode: 'custom', customFamily: 'control', customControlHorizon: predictedMinHorizon },
      };
      recommendations.push(chosenRecommendation);
      comparison = { beforeRegime: 'impossible', afterRegime: 'exact', keyMetricName: 'κ(0)', keyMetricBefore: collisionGap, keyMetricAfter: 0, narrative: 'Extending the finite history adds enough independent rows to interpolate the protected functional exactly.', changed: true };
    }
    if (!exact && weakerTargets.length) {
      recommendations.push({ title: `Weaken target to ${weakerTargets[0]}`, actionKind: 'weaken_target', rationale: 'The current history already supports this weaker moment target exactly.', theoremStatus: 'family-specific diagonal/history threshold result', minimal: false, availableInStudio: true, patch: { mode: 'custom', customFamily: 'control', customControlTargetText: weakerTargets[0] } });
    }
    return {
      title: 'Custom diagonal/history composition',
      mode: 'custom',
      family: 'control',
      familyLabel: 'Diagonal finite-history family',
      validity: 'supported',
      regime: exact ? 'exact' : 'impossible',
      status: uppercaseRegime(exact ? 'exact' : 'impossible'),
      exact,
      approximate: false,
      asymptotic: false,
      impossible: !exact,
      unsupported: false,
      theoremStatus: 'family-specific diagonal/history threshold result',
      supportScope: 'Diagonal finite-history family with moment, coordinate, or linear-function targets.',
      protectedLabel: config.customControlTargetText,
      observationLabel: `${horizon}-step history`,
      architectureLabel: 'finite-history exact recovery',
      targetSplitSummary: weakerTargets.length ? weakerTargets.join(', ') : 'No weaker moment target was automatically certified.',
      rootCause: exact ? 'The finite history already separates the target.' : 'The finite history is too short for the requested target.',
      missingStructure: exact ? 'No structural change is needed.' : 'Increase the horizon or weaken the target.',
      objects: [
        { objectId: 'control-family', label: 'Diagonal finite-history family', objectType: 'admissible_family', family: 'control', domain: 'state coefficients', codomain: `R^${dimension}`, dimension: `${dimension}`, basis: 'diagonal eigenbasis', linearStatus: 'linear', supportStatus: 'family-specific diagonal/history threshold result', theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theory/advanced-directions/constrained-observation-results-report.md'], compatibilityRequirements: ['distinct active eigenvalues', 'declared sensor profile'], notes: [`sensor profile: ${sensorWeights.join(', ')}`] },
        { objectId: 'control-record', label: `${horizon}-step history`, objectType: 'record_map', family: 'control', domain: `R^${dimension}`, codomain: `R^${horizon}`, dimension: `${horizon}x${dimension}`, basis: 'history rows', linearStatus: 'linear', supportStatus: 'family-specific diagonal/history threshold result', theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theory/advanced-directions/constrained-observation-results-report.md'], compatibilityRequirements: ['finite horizon'], notes: ['static finite-history reconstruction'] },
        { objectId: 'control-target', label: target.label, objectType: 'protected_variable', family: 'control', domain: `R^${dimension}`, codomain: 'R', dimension: `1x${dimension}`, basis: 'diagonal-function weights', linearStatus: 'linear', supportStatus: 'family-specific diagonal/history threshold result', theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theory/advanced-directions/constrained-observation-results-report.md'], compatibilityRequirements: ['target must be diagonal-function reducible'], notes: [config.customControlTargetText] },
      ],
      diagnostics: [{ severity: exact ? 'success' : 'error', code: 'history-threshold', title: 'Finite-history sufficiency check', detail: exact ? 'The record is sufficient for the requested target.' : 'The record horizon is too short for the requested target on the active diagonal family.', theoremStatus: 'family-specific diagonal/history threshold result' }],
      recommendations,
      chosenRecommendation,
      comparison,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theory/advanced-directions/constrained-observation-results-report.md'],
      supportedCalculations: ['history-threshold detection', 'collision-gap analysis', 'diagonal interpolation weights', 'weaker moment scan'],
      rawDetails: { sensorWeights, protectedWeights: target.weights, predictedMinHorizon, collisionGap, selectedDelta: Number(config.customDelta ?? 0.5) },
      exportRows: [{ family: 'control', regime: exact ? 'exact' : 'impossible', horizon, predictedMinHorizon: predictedMinHorizon ?? -1, collisionGap }],
    };
  } catch (error) {
    return {
      title: 'Custom diagonal/history composition', mode: 'custom', family: 'control', familyLabel: 'Diagonal finite-history family', validity: 'unsupported', regime: 'unsupported', status: 'Unsupported', exact: false, approximate: false, asymptotic: false, impossible: false, unsupported: true,
      theoremStatus: 'unsupported', supportScope: 'Control custom mode only supports diagonal sensor profiles and moment / coordinate / linear-function targets.', protectedLabel: 'unsupported target', observationLabel: 'unsupported history record', architectureLabel: 'finite-history exact recovery', targetSplitSummary: 'No supported target split available.', rootCause: 'The custom control input could not be reduced to the supported diagonal/history family.', missingStructure: 'Use a numeric sensor profile plus moment(k), xi, or a linear functional in x1..xn.', objects: [], diagnostics: [{ severity: 'error', code: 'unsupported-control-input', title: 'Control/history input is unsupported', detail: error.message, theoremStatus: 'unsupported' }], recommendations: [{ title: 'Reformulate as diagonal/history input', actionKind: 'reformulate', rationale: 'The current engine only supports diagonal finite-history reduction for custom control input.', theoremStatus: 'unsupported -> nearest supported template', minimal: false, availableInStudio: false }], chosenRecommendation: null, comparison: null,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../theory/advanced-directions/constrained-observation-results-report.md'], supportedCalculations: ['syntax validation'], rawDetails: { sensorProfileText: config.customControlSensorProfileText, targetText: config.customControlTargetText }, exportRows: [],
    };
  }
}

function structuredMixerPatch(mode, family, patch) {
  return { mode, family, ...patch };
}

function analyzeStructuredMixer(config) {
  const family = config.family ?? 'linear';
  if (family === 'periodic') {
    const periodicConfig = {
      system: 'periodic',
      periodicProtected: config.structuredPeriodicProtected ?? 'full_weighted_sum',
      periodicObservation: config.structuredPeriodicObservation ?? 'cutoff_vorticity',
      periodicCutoff: Number(config.structuredPeriodicCutoff ?? 3),
      periodicDelta: Number(config.structuredDelta ?? 2),
    };
    const result = analyzeRecoverability(periodicConfig);
    return {
      title: 'Structured periodic composition',
      mode: 'structured', family: 'periodic', familyLabel: 'Periodic modal family', validity: 'supported', regime: result.exact ? 'exact' : result.impossible ? 'impossible' : 'approximate', status: result.status,
      exact: result.exact, approximate: !result.exact && !result.impossible, asymptotic: result.asymptotic, impossible: result.impossible, unsupported: false,
      theoremStatus: result.theoremStatus, supportScope: 'Periodic modal family on the supported finite four-mode benchmark.', protectedLabel: result.protectedLabel, observationLabel: result.observationLabel, architectureLabel: result.recommendedArchitecture,
      targetSplitSummary: result.weakerRecoverableTargets.length ? result.weakerRecoverableTargets.join(', ') : 'No weaker target was detected.',
      rootCause: result.structuralBlocker, missingStructure: result.missingStructure,
      objects: [
        { objectId: 'periodic-family', label: 'Periodic modal family', objectType: 'admissible_family', family: 'periodic', domain: 'modal coefficients', codomain: 'periodic record', dimension: 'four-mode basis', basis: 'a1..a4', linearStatus: 'linear', supportStatus: result.theoremStatus, theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../cfd/incompressible-projection.md'], compatibilityRequirements: ['supported periodic basis'], notes: ['family-specific threshold law'] },
        { objectId: 'periodic-target', label: result.protectedLabel, objectType: 'protected_variable', family: 'periodic', domain: 'modal coefficients', codomain: 'protected value', dimension: 'family-specific', basis: 'a1..a4', linearStatus: 'linear', supportStatus: result.theoremStatus, theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../cfd/incompressible-projection.md'], compatibilityRequirements: ['protected support must fit retained support'], notes: [] },
        { objectId: 'periodic-record', label: result.observationLabel, objectType: 'record_map', family: 'periodic', domain: 'modal coefficients', codomain: 'record space', dimension: 'family-specific', basis: 'cutoff / vorticity', linearStatus: 'linear', supportStatus: result.theoremStatus, theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../cfd/incompressible-projection.md'], compatibilityRequirements: ['supported periodic record choices'], notes: [] },
      ],
      diagnostics: result.failureModes.map((detail, index) => ({ severity: result.exact ? 'success' : index === 0 ? 'error' : 'warning', code: `structured-periodic-${index}`, title: index === 0 ? 'Periodic support check' : 'Derived diagnosis', detail, theoremStatus: result.theoremStatus })),
      recommendations: result.recommendations.filter((item) => item.availableInStudio).map((item) => ({ ...item, patch: structuredMixerPatch('structured', 'periodic', { structuredPeriodicProtected: config.structuredPeriodicProtected ?? 'full_weighted_sum', structuredPeriodicObservation: config.structuredPeriodicObservation ?? 'cutoff_vorticity', structuredPeriodicCutoff: item.patch?.periodicCutoff ?? config.structuredPeriodicCutoff ?? 3, structuredDelta: config.structuredDelta ?? 2 }) })),
      chosenRecommendation: result.chosenRecommendation ? { ...result.chosenRecommendation, patch: structuredMixerPatch('structured', 'periodic', { structuredPeriodicProtected: config.structuredPeriodicProtected ?? 'full_weighted_sum', structuredPeriodicObservation: config.structuredPeriodicObservation ?? 'cutoff_vorticity', structuredPeriodicCutoff: result.chosenRecommendation.patch?.periodicCutoff ?? config.structuredPeriodicCutoff ?? 3, structuredDelta: config.structuredDelta ?? 2 }) } : null,
      comparison: result.comparison,
      theoremLinks: ['../theorem-candidates/constrained-observation-theorems.md', '../cfd/incompressible-projection.md'],
      supportedCalculations: ['threshold detection', 'same-record weaker-target detection', 'before/after cutoff comparison'],
      rawDetails: { predictedMinCutoff: result.predictedMinCutoff, kappa0: result.kappa0, selectedDelta: result.selectedDelta },
      exportRows: [{ family: 'periodic', regime: result.regime, predictedMinCutoff: result.predictedMinCutoff ?? -1, kappa0: result.kappa0, selectedDelta: result.selectedDelta }],
    };
  }
  if (family === 'control') {
    const report = analyzeCustomControl({
      customControlSensorProfileText: { three_active: '1,0.4,0.2', two_active: '1,0,0.2', protected_hidden: '1,0.4,0' }[config.structuredControlProfile ?? 'three_active'],
      customControlTargetText: { sensor_sum: 'moment(0)', first_moment: 'moment(1)', second_moment: 'moment(2)', protected_coordinate: 'x3' }[config.structuredControlFunctional ?? 'second_moment'],
      customControlHorizon: config.structuredControlHorizon ?? 2,
      customDelta: config.structuredDelta ?? 0.5,
      mode: 'structured', family: 'control',
    });
    const targetKeyByLabel = {
      'moment(0)': 'sensor_sum',
      'moment(1)': 'first_moment',
      'moment(2)': 'second_moment',
      x3: 'protected_coordinate',
    };
    const mappedRecommendations = report.recommendations.map((item) => {
      if (item.actionKind === 'add_history' && item.patch?.customControlHorizon) {
        return {
          ...item,
          patch: structuredMixerPatch('structured', 'control', {
            structuredControlProfile: config.structuredControlProfile ?? 'three_active',
            structuredControlFunctional: config.structuredControlFunctional ?? 'second_moment',
            structuredControlHorizon: item.patch.customControlHorizon,
            structuredDelta: config.structuredDelta ?? 0.5,
          }),
        };
      }
      if (item.actionKind === 'weaken_target') {
        const mappedTarget = targetKeyByLabel[item.patch?.customControlTargetText];
        if (mappedTarget) {
          return {
            ...item,
            patch: structuredMixerPatch('structured', 'control', {
              structuredControlProfile: config.structuredControlProfile ?? 'three_active',
              structuredControlFunctional: mappedTarget,
              structuredControlHorizon: config.structuredControlHorizon ?? 2,
              structuredDelta: config.structuredDelta ?? 0.5,
            }),
          };
        }
      }
      return {
        ...item,
        availableInStudio: false,
        patch: undefined,
      };
    });
    const chosenRecommendation = report.chosenRecommendation?.actionKind === 'add_history' && report.chosenRecommendation.patch?.customControlHorizon
      ? {
          ...report.chosenRecommendation,
          patch: structuredMixerPatch('structured', 'control', {
            structuredControlProfile: config.structuredControlProfile ?? 'three_active',
            structuredControlFunctional: config.structuredControlFunctional ?? 'second_moment',
            structuredControlHorizon: report.chosenRecommendation.patch.customControlHorizon,
            structuredDelta: config.structuredDelta ?? 0.5,
          }),
        }
      : null;
    return {
      ...report,
      title: 'Structured diagonal/history composition',
      mode: 'structured',
      family: 'control',
      recommendations: mappedRecommendations,
      chosenRecommendation,
    };
  }
  if (family === 'boundary') {
    const strong = (config.structuredBoundaryProtected ?? 'bounded_velocity_class') === 'bounded_velocity_class';
    const architecture = config.structuredBoundaryArchitecture ?? 'periodic_transplant';
    const transplant = analyzeBoundaryProjectionLimit({ gridSize: Number(config.structuredBoundaryGridSize ?? 17), poissonIterations: 320 });
    const exact = architecture === 'boundary_compatible_hodge' || (!strong && architecture === 'periodic_transplant');
    const impossible = architecture === 'periodic_transplant' && strong;
    const chosenRecommendation = impossible ? {
      title: 'Switch to boundary-compatible Hodge projector', actionKind: 'switch_architecture', rationale: 'The transplanted periodic projector violates the bounded-domain boundary trace required by the strong target.', theoremStatus: 'restricted theorem-backed (bounded-domain Hodge + counterexample layer)', minimal: true, availableInStudio: true, patch: structuredMixerPatch('structured', 'boundary', { structuredBoundaryArchitecture: 'boundary_compatible_hodge', structuredBoundaryProtected: config.structuredBoundaryProtected ?? 'bounded_velocity_class', structuredBoundaryGridSize: config.structuredBoundaryGridSize ?? 17, structuredDelta: config.structuredDelta ?? 0.2 }),
    } : null;
    return {
      title: 'Structured bounded-domain composition', mode: 'structured', family: 'boundary', familyLabel: 'Bounded-domain architecture benchmark', validity: 'supported', regime: exact ? 'exact' : 'impossible', status: uppercaseRegime(exact ? 'exact' : 'impossible'), exact, approximate: false, asymptotic: false, impossible, unsupported: false,
      theoremStatus: 'restricted theorem-backed (bounded-domain Hodge + counterexample layer)', supportScope: 'Restricted bounded-domain family with compatible Hodge replacement.', protectedLabel: strong ? 'bounded velocity class with boundary compatibility' : 'bulk divergence certificate only', observationLabel: architecture.replaceAll('_', ' '), architectureLabel: architecture.replaceAll('_', ' '), targetSplitSummary: strong ? 'bulk divergence certificate only' : 'No weaker target needed.',
      rootCause: impossible ? 'The transplanted periodic projector is incompatible with the bounded protected class.' : 'The current architecture is compatible with the bounded protected target.', missingStructure: impossible ? 'Use the boundary-compatible finite-mode Hodge family.' : 'No structural change is needed.',
      objects: [
        { objectId: 'boundary-family', label: 'Bounded finite-mode Hodge family', objectType: 'admissible_family', family: 'boundary', domain: 'field coefficients', codomain: 'bounded velocity class', dimension: `${config.structuredBoundaryGridSize ?? 17}`, basis: 'boundary-compatible finite-mode basis', linearStatus: 'linear', supportStatus: 'restricted theorem-backed (bounded-domain Hodge + counterexample layer)', theoremLinks: ['../theorem-candidates/bounded-domain-hodge-theorems.md', '../cfd/bounded-vs-periodic-projection.md'], compatibilityRequirements: ['bounded domain', 'compatible trace basis'], notes: [] },
        { objectId: 'boundary-record', label: architecture.replaceAll('_', ' '), objectType: 'correction_operator', family: 'boundary', domain: 'bounded velocity class', codomain: 'bounded velocity class', dimension: 'family-specific', basis: 'projector architecture', linearStatus: 'linear', supportStatus: 'restricted theorem-backed (bounded-domain Hodge + counterexample layer)', theoremLinks: ['../theorem-candidates/bounded-domain-hodge-theorems.md', '../cfd/bounded-vs-periodic-projection.md'], compatibilityRequirements: ['projector must respect boundary conditions'], notes: [] },
        { objectId: 'boundary-target', label: strong ? 'bounded velocity class with boundary compatibility' : 'bulk divergence certificate only', objectType: 'protected_variable', family: 'boundary', domain: 'bounded velocity class', codomain: 'certificate', dimension: 'family-specific', basis: 'bounded basis', linearStatus: 'linear', supportStatus: 'restricted theorem-backed (bounded-domain Hodge + counterexample layer)', theoremLinks: ['../theorem-candidates/bounded-domain-hodge-theorems.md', '../cfd/bounded-vs-periodic-projection.md'], compatibilityRequirements: ['target must declare whether boundary compatibility matters'], notes: [] },
      ],
      diagnostics: [{ severity: exact ? 'success' : 'error', code: 'boundary-compatibility', title: 'Boundary compatibility check', detail: impossible ? 'The current projector architecture is incompatible with the bounded protected target.' : 'The current architecture respects the bounded protected class.', theoremStatus: 'restricted theorem-backed (bounded-domain Hodge + counterexample layer)' }],
      recommendations: chosenRecommendation ? [chosenRecommendation, { title: 'Weaken target to divergence certificate', actionKind: 'weaken_target', rationale: 'The transplanted architecture can support a weaker bulk divergence certificate even though it fails on the strong bounded class.', theoremStatus: 'family-specific weaker-target split', minimal: false, availableInStudio: true, patch: structuredMixerPatch('structured', 'boundary', { structuredBoundaryArchitecture: 'periodic_transplant', structuredBoundaryProtected: 'divergence_certificate', structuredBoundaryGridSize: config.structuredBoundaryGridSize ?? 17, structuredDelta: config.structuredDelta ?? 0.2 }) }] : [],
      chosenRecommendation,
      comparison: chosenRecommendation ? { beforeRegime: 'impossible', afterRegime: 'exact', keyMetricName: 'boundary mismatch', keyMetricBefore: transplant.projectedBoundaryNormalRms, keyMetricAfter: 5.172e-15, narrative: 'Switching to the compatible Hodge architecture removes the boundary mismatch on the restricted admissible family.', changed: true } : null,
      theoremLinks: ['../theorem-candidates/bounded-domain-hodge-theorems.md', '../cfd/bounded-vs-periodic-projection.md'],
      supportedCalculations: ['boundary compatibility check', 'architecture swap guidance', 'weaker-target alternative'],
      rawDetails: { boundaryMismatch: transplant.projectedBoundaryNormalRms, selectedDelta: Number(config.structuredDelta ?? 0.2) },
      exportRows: [{ family: 'boundary', regime: exact ? 'exact' : 'impossible', boundaryMismatch: transplant.projectedBoundaryNormalRms }],
    };
  }
  const report = analyzeCustomLinear({
    customLinearDimension: 3,
    customLinearObservationText: Object.entries(config.structuredLinearMeasurements ?? {}).filter(([, enabled]) => enabled).map(([id]) => LINEAR_TEMPLATE_LIBRARY.sensor_basis.candidates.find((candidate) => candidate.id === id)?.row.join(',')).filter(Boolean).join('\n') || '0,0,0',
    customLinearProtectedText: LINEAR_TEMPLATE_LIBRARY.sensor_basis.protectedOptions[config.structuredLinearProtected ?? 'x3'].rows.map((row) => row.join(',')).join('\n'),
    customLinearCandidateText: LINEAR_TEMPLATE_LIBRARY.sensor_basis.candidates.filter((candidate) => !(config.structuredLinearMeasurements ?? {})[candidate.id]).map((candidate) => candidate.row.join(',')).join('\n'),
    customDelta: config.structuredDelta ?? 1,
  });
  const candidateIdByRow = new Map(
    LINEAR_TEMPLATE_LIBRARY.sensor_basis.candidates.map((candidate) => [candidate.row.join(','), candidate.id])
  );
  const protectedKeyByRows = new Map(
    Object.entries(LINEAR_TEMPLATE_LIBRARY.sensor_basis.protectedOptions).map(([key, value]) => [value.rows.map((row) => row.join(',')).join('\n'), key])
  );
  const structuredRecommendations = report.recommendations.map((item) => {
    if (item.actionKind === 'add_measurement' && item.patch?.customLinearObservationText) {
      const nextMeasurements = Object.fromEntries(
        LINEAR_TEMPLATE_LIBRARY.sensor_basis.candidates.map((candidate) => [candidate.id, false])
      );
      item.patch.customLinearObservationText
        .split('\n')
        .map((line) => line.trim())
        .filter(Boolean)
        .forEach((line) => {
          const row = line.split(/[\s,]+/).filter(Boolean).map(Number).join(',');
          const id = candidateIdByRow.get(row);
          if (id) nextMeasurements[id] = true;
        });
      return {
        ...item,
        patch: structuredMixerPatch('structured', 'linear', {
          structuredLinearProtected: config.structuredLinearProtected ?? 'x3',
          structuredLinearMeasurements: nextMeasurements,
          structuredDelta: config.structuredDelta ?? 1,
        }),
      };
    }
    if (item.actionKind === 'weaken_target' && item.patch?.customLinearProtectedText) {
      const mappedTarget = protectedKeyByRows.get(item.patch.customLinearProtectedText);
      if (mappedTarget) {
        return {
          ...item,
          patch: structuredMixerPatch('structured', 'linear', {
            structuredLinearProtected: mappedTarget,
            structuredLinearMeasurements: config.structuredLinearMeasurements ?? {},
            structuredDelta: config.structuredDelta ?? 1,
          }),
        };
      }
    }
    return {
      ...item,
      availableInStudio: false,
      patch: undefined,
    };
  });
  const chosenRecommendation = report.chosenRecommendation?.actionKind === 'add_measurement'
    ? structuredRecommendations.find((item) => item.title === report.chosenRecommendation.title) ?? null
    : null;
  return {
    ...report,
    title: 'Structured restricted-linear composition',
    mode: 'structured',
    family: 'linear',
    recommendations: structuredRecommendations,
    chosenRecommendation,
  };
}

function analyzeRandomMixer(config) {
  const family = config.randomFamily ?? 'linear';
  const seed = Number(config.randomSeed ?? 37);
  const rng = seededRandom(seed);
  const trials = Math.max(1, Number(config.randomTrials ?? 16));
  let generated = null;
  let report = null;
  for (let attempt = 0; attempt < trials; attempt += 1) {
    if (family === 'periodic') {
      const coeffs = Array.from({ length: 4 }, () => [-2, -1, 0, 1, 2][Math.floor(rng() * 5)]);
      if (coeffs.every((value) => Math.abs(value) <= EPS)) coeffs[0] = 1;
      const cutoff = 1 + Math.floor(rng() * 3);
      generated = {
        mode: 'custom', customFamily: 'periodic', customPeriodicFunctionalText: coeffs.map((value, index) => (Math.abs(value) > EPS ? `${value}*a${index + 1}` : null)).filter(Boolean).join(' + '), customPeriodicObservation: 'cutoff_vorticity', customPeriodicCutoff: cutoff, customDelta: 2,
      };
      report = analyzeCustomPeriodic(generated);
    } else if (family === 'control') {
      const profile = Array.from({ length: 4 }, () => [0, 0.2, 0.4, 1][Math.floor(rng() * 4)]);
      if (profile.filter((value) => Math.abs(value) > EPS).length < 2) {
        profile[0] = 1;
        profile[1] = 0.4;
      }
      generated = {
        mode: 'custom', customFamily: 'control', customControlSensorProfileText: profile.join(','), customControlTargetText: ['moment(0)', 'moment(1)', 'moment(2)', 'x3', 'x4'][Math.floor(rng() * 5)], customControlHorizon: 1 + Math.floor(rng() * 3), customDelta: 0.5,
      };
      report = analyzeCustomControl(generated);
    } else {
      const measurementIds = LINEAR_TEMPLATE_LIBRARY.sensor_basis.candidates.map((candidate) => candidate.id);
      const measurements = Object.fromEntries(measurementIds.map((id) => [id, rng() < 0.45]));
      if (!Object.values(measurements).some(Boolean)) measurements.measure_x1 = true;
      generated = {
        mode: 'structured', family: 'linear', structuredLinearProtected: ['x3', 'x2_plus_x3', 'tail_pair'][Math.floor(rng() * 3)], structuredLinearMeasurements: measurements, structuredDelta: 1,
      };
      report = analyzeStructuredMixer(generated);
    }
    if (config.randomObjective === 'failure' ? report.impossible && report.chosenRecommendation : true) break;
  }
  return {
    ...report,
    title: 'Structured random exploration',
    mode: 'random',
    randomSeed: seed,
    generatedConfig: generated,
    diagnostics: [
      { severity: 'info', code: 'random-seed', title: 'Reproducible seeded search', detail: `This case was generated with seed ${seed} after at most ${trials} constrained trials.`, theoremStatus: 'empirical but reproducible' },
      ...report.diagnostics,
    ],
    exportRows: [...(report.exportRows ?? []), { family, randomSeed: seed, regime: report.regime }],
  };
}

function seededRandom(seed) {
  let state = seed >>> 0;
  return () => {
    state = (1664525 * state + 1013904223) >>> 0;
    return state / 0x100000000;
  };
}

function mergePatch(config, patch) {
  return { ...config, ...patch };
}

export function analyzeDiscoveryMixer(config = {}) {
  if ((config.mode ?? 'structured') === 'demo') {
    const demo = DISCOVERY_MIXER_DEMOS[config.demoKey ?? 'periodic_builder'];
    if (!demo) return analyzeDiscoveryMixer({ mode: 'structured', family: 'linear' });
    return analyzeDiscoveryMixer({ ...config, ...demo.patch, mode: demo.mode, family: demo.family });
  }
  if ((config.mode ?? 'structured') === 'random') {
    return analyzeRandomMixer(config);
  }
  if ((config.mode ?? 'structured') === 'custom') {
    if ((config.customFamily ?? 'linear') === 'periodic') return analyzeCustomPeriodic(config);
    if ((config.customFamily ?? 'linear') === 'control') return analyzeCustomControl(config);
    return analyzeCustomLinear(config);
  }
  return analyzeStructuredMixer(config);
}

export function applyDiscoveryMixerRecommendation(config, recommendation) {
  if (!recommendation?.patch) return config;
  return mergePatch(config, recommendation.patch);
}
