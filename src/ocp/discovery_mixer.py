from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from typing import Any, Sequence
import math
import random
import re

import numpy as np

from .recoverability import (
    EPS,
    diagonal_functional_history_weights,
    diagonal_functional_minimal_horizon,
    restricted_linear_collision_gap,
    restricted_linear_rank_lower_bound,
    restricted_linear_recoverability,
    restricted_linear_rowspace_residual,
)
from .structural_discovery import (
    BOUNDARY_PROTECTED_LABELS,
    CONTROL_FUNCTIONAL_LABELS,
    CONTROL_PROFILES,
    LINEAR_TEMPLATE_LIBRARY,
    PERIODIC_PROTECTED_OPTIONS,
)

Array = np.ndarray

LINEAR_THEOREM_LINKS = (
    'docs/theorem-candidates/constrained-observation-theorems.md',
    'docs/theorem-candidates/capacity-theorems.md',
)
PERIODIC_THEOREM_LINKS = (
    'docs/theorem-candidates/constrained-observation-theorems.md',
    'docs/cfd/incompressible-projection.md',
)
CONTROL_THEOREM_LINKS = (
    'docs/theorem-candidates/constrained-observation-theorems.md',
    'docs/theory/advanced-directions/constrained-observation-results-report.md',
)
BOUNDARY_THEOREM_LINKS = (
    'docs/theorem-candidates/bounded-domain-hodge-theorems.md',
    'docs/cfd/bounded-vs-periodic-projection.md',
)

DIAGONAL_EIGENVALUES = (0.95, 0.8, 0.65, 0.5)


@dataclass(frozen=True)
class MixerObject:
    object_id: str
    label: str
    object_type: str
    family: str
    domain: str
    codomain: str
    dimension: str
    basis: str
    linear_status: str
    support_status: str
    theorem_links: tuple[str, ...]
    compatibility_requirements: tuple[str, ...]
    notes: tuple[str, ...]


@dataclass(frozen=True)
class MixerDiagnostic:
    severity: str
    code: str
    title: str
    detail: str
    theorem_status: str


@dataclass(frozen=True)
class MixerRecommendation:
    action_id: str
    title: str
    action_kind: str
    rationale: str
    theorem_status: str
    estimated_cost: float | None
    cost_unit: str | None
    expected_regime: str
    patch: dict[str, Any] | None


@dataclass(frozen=True)
class MixerComparison:
    before_regime: str
    after_regime: str
    key_metric: str
    before_value: float
    after_value: float
    changed: bool
    narrative: str


@dataclass(frozen=True)
class MixerReport:
    title: str
    mode: str
    family: str
    family_label: str
    validity: str
    regime: str
    exact: bool
    approximate: bool
    asymptotic: bool
    impossible: bool
    unsupported: bool
    theorem_status: str
    support_scope: str
    protected_label: str
    observation_label: str
    architecture_label: str
    target_split_summary: str
    root_cause: str
    missing_structure: str
    objects: tuple[MixerObject, ...]
    diagnostics: tuple[MixerDiagnostic, ...]
    recommendations: tuple[MixerRecommendation, ...]
    chosen_recommendation: MixerRecommendation | None
    comparison: MixerComparison | None
    theorem_links: tuple[str, ...]
    supported_calculations: tuple[str, ...]
    raw_details: dict[str, Any]
    export_rows: tuple[dict[str, Any], ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _regime(*, exact: bool, asymptotic: bool = False, impossible: bool = False, unsupported: bool = False) -> str:
    if unsupported:
        return 'unsupported'
    if exact:
        return 'exact'
    if asymptotic:
        return 'asymptotic'
    if impossible:
        return 'impossible'
    return 'approximate'


def _safe_float(value: str) -> float:
    return float(value.strip())


def _numeric_matrix(text: str) -> list[list[float]]:
    rows: list[list[float]] = []
    for line in text.replace(';', '\n').splitlines():
        cleaned = line.strip()
        if not cleaned:
            continue
        row = [_safe_float(token) for token in re.split(r'[\s,]+', cleaned) if token.strip()]
        rows.append(row)
    return rows


def _expression_tokens(expr: str) -> list[str]:
    normalized = expr.replace(' ', '')
    if not normalized:
        return []
    normalized = normalized.replace('-', '+-')
    if normalized.startswith('+-'):
        normalized = '-' + normalized[2:]
    return [token for token in normalized.split('+') if token]


def _parse_linear_expression(expr: str, *, prefix: str, dimension: int) -> Array:
    text = expr.strip()
    if not text:
        raise ValueError('empty expression')
    if re.search(r'[^0-9A-Za-z_+\-*.\s]', text):
        raise ValueError('unsupported characters in expression')
    if re.search(r'\b(sin|cos|exp|log|\^|/|@)\b', text):
        raise ValueError('nonlinear or unsupported syntax in expression')
    coeffs = np.zeros(int(dimension), dtype=float)
    for token in _expression_tokens(text):
        if re.fullmatch(r'[+-]?\d+(?:\.\d+)?', token):
            raise ValueError('constant offsets are not supported in protected or observation expressions')
        match = re.fullmatch(r'([+-]?(?:\d+(?:\.\d+)?)?)\*?(' + re.escape(prefix) + r'(\d+))', token)
        if not match:
            raise ValueError(f'unsupported token: {token}')
        coeff_text = match.group(1)
        var_index = int(match.group(3)) - 1
        if var_index < 0 or var_index >= dimension:
            raise ValueError(f'variable {prefix}{var_index + 1} is outside the declared basis size {dimension}')
        if coeff_text in ('', '+', None):
            coeff = 1.0
        elif coeff_text == '-':
            coeff = -1.0
        else:
            coeff = float(coeff_text)
        coeffs[var_index] += coeff
    if np.linalg.norm(coeffs) <= EPS:
        raise ValueError('expression reduces to the zero functional')
    return coeffs


def _parse_row_lines(text: str, *, prefix: str, dimension: int) -> list[list[float]]:
    rows: list[list[float]] = []
    for line in text.replace(';', '\n').splitlines():
        cleaned = line.strip()
        if not cleaned:
            continue
        if re.search(r'[A-Za-z]', cleaned):
            rows.append(_parse_linear_expression(cleaned, prefix=prefix, dimension=dimension).tolist())
        else:
            rows.append([_safe_float(token) for token in re.split(r'[\s,]+', cleaned) if token.strip()])
    if not rows:
        raise ValueError('no rows were provided')
    width = len(rows[0])
    if width != dimension:
        raise ValueError(f'row width {width} does not match declared dimension {dimension}')
    if any(len(row) != width for row in rows):
        raise ValueError('rows must all have the same length')
    return rows


def _box_family(dim: int, radius: float = 1.0) -> list[Array]:
    grid = np.linspace(-radius, radius, 5)
    return [np.asarray(point, dtype=float) for point in np.array(np.meshgrid(*([grid] * dim))).T.reshape(-1, dim)]


def _matrix_rank(matrix: Array) -> int:
    if matrix.size == 0:
        return 0
    return int(np.linalg.matrix_rank(np.asarray(matrix, dtype=float), tol=EPS))


def _linear_candidate_exact_sets(observation_rows: Array, protected_rows: Array, candidate_rows: Array) -> tuple[int | None, list[list[int]]]:
    if candidate_rows.size == 0:
        return None, []
    count = candidate_rows.shape[0]
    for size in range(1, count + 1):
        valid: list[list[int]] = []
        index_stack: list[int] = []

        def choose(start: int) -> None:
            if len(index_stack) == size:
                augmented = np.vstack([observation_rows, candidate_rows[index_stack]]) if observation_rows.size else candidate_rows[index_stack]
                residual = restricted_linear_rowspace_residual(augmented, protected_rows)
                if residual <= 1e-8:
                    valid.append(index_stack.copy())
                return
            for index in range(start, count):
                index_stack.append(index)
                choose(index + 1)
                index_stack.pop()

        choose(0)
        if valid:
            return size, valid
    return None, []


def _build_linear_objects(dimension: int, observation_rows: Array, protected_rows: Array, candidate_rows: Array, *, family_label: str, theorem_status: str) -> tuple[MixerObject, ...]:
    objects = [
        MixerObject(
            object_id='state-space',
            label=f'{dimension}-dimensional state space',
            object_type='state_space',
            family=family_label,
            domain='—',
            codomain=f'R^{dimension}',
            dimension=str(dimension),
            basis=', '.join(f'x{i + 1}' for i in range(dimension)),
            linear_status='linear',
            support_status=theorem_status,
            theorem_links=LINEAR_THEOREM_LINKS,
            compatibility_requirements=('shared dimension', 'declared coordinate basis'),
            notes=('admissible family is the coefficient box [-1,1]^n',),
        ),
        MixerObject(
            object_id='record-map',
            label='Observation / record map',
            object_type='record_map',
            family=family_label,
            domain=f'R^{dimension}',
            codomain=f'R^{observation_rows.shape[0]}',
            dimension=f'{observation_rows.shape[0]}x{dimension}',
            basis='row representation',
            linear_status='linear',
            support_status=theorem_status,
            theorem_links=LINEAR_THEOREM_LINKS,
            compatibility_requirements=('row width must equal state dimension',),
            notes=(f'{observation_rows.shape[0]} active observation row(s)',),
        ),
        MixerObject(
            object_id='protected-target',
            label='Protected target',
            object_type='protected_variable',
            family=family_label,
            domain=f'R^{dimension}',
            codomain=f'R^{protected_rows.shape[0]}',
            dimension=f'{protected_rows.shape[0]}x{dimension}',
            basis='row representation',
            linear_status='linear',
            support_status=theorem_status,
            theorem_links=LINEAR_THEOREM_LINKS,
            compatibility_requirements=('target rows must share state dimension',),
            notes=(f'{protected_rows.shape[0]} protected row(s)',),
        ),
    ]
    if candidate_rows.size:
        objects.append(
            MixerObject(
                object_id='candidate-augmentations',
                label='Candidate augmentation library',
                object_type='augmentation_candidate',
                family=family_label,
                domain=f'R^{dimension}',
                codomain=f'R^{candidate_rows.shape[0]}',
                dimension=f'{candidate_rows.shape[0]}x{dimension}',
                basis='row representation',
                linear_status='linear',
                support_status=theorem_status,
                theorem_links=LINEAR_THEOREM_LINKS,
                compatibility_requirements=('candidate rows must share state dimension',),
                notes=('searched only inside the provided candidate library',),
            )
        )
    return tuple(objects)


def analyze_linear_custom_case(
    *,
    dimension: int,
    observation_text: str,
    protected_text: str,
    candidate_text: str = '',
    delta: float = 1.0,
) -> MixerReport:
    diagnostics: list[MixerDiagnostic] = []
    recommendations: list[MixerRecommendation] = []
    theorem_status = 'theorem-backed restricted-linear result'
    try:
        observation_rows = np.asarray(_parse_row_lines(observation_text, prefix='x', dimension=dimension), dtype=float)
        protected_rows = np.asarray(_parse_row_lines(protected_text, prefix='x', dimension=dimension), dtype=float)
        candidate_rows = (
            np.asarray(_parse_row_lines(candidate_text, prefix='x', dimension=dimension), dtype=float)
            if candidate_text.strip()
            else np.zeros((0, dimension), dtype=float)
        )
    except ValueError as exc:
        diagnostics.append(
            MixerDiagnostic(
                severity='error',
                code='unsupported-custom-linear-input',
                title='Custom linear input could not be reduced to a supported class',
                detail=str(exc),
                theorem_status='unsupported',
            )
        )
        return MixerReport(
            title='Custom restricted-linear composition',
            mode='custom',
            family='linear',
            family_label='Restricted-linear family',
            validity='unsupported',
            regime='unsupported',
            exact=False,
            approximate=False,
            asymptotic=False,
            impossible=False,
            unsupported=True,
            theorem_status='unsupported',
            support_scope='Only matrix rows or linear functionals in x1..xn are supported here.',
            protected_label='unsupported protected target',
            observation_label='unsupported custom record',
            architecture_label='restricted-linear exact recovery',
            target_split_summary='No valid target split available because the input was not reducible.',
            root_cause='The custom expression or matrix text could not be parsed into a supported restricted-linear object.',
            missing_structure='Reformulate the input as rows or linear expressions in x1..xn.',
            objects=tuple(),
            diagnostics=tuple(diagnostics),
            recommendations=(
                MixerRecommendation(
                    action_id='reformulate-linear',
                    title='Reformulate as linear rows in x1..xn',
                    action_kind='reformulate',
                    rationale='The current engine only supports custom input that reduces to a matrix-defined restricted-linear family.',
                    theorem_status='unsupported -> nearest supported template',
                    estimated_cost=None,
                    cost_unit=None,
                    expected_regime='unsupported',
                    patch=None,
                ),
            ),
            chosen_recommendation=None,
            comparison=None,
            theorem_links=LINEAR_THEOREM_LINKS,
            supported_calculations=('syntax validation', 'object-class detection'),
            raw_details={'dimension': dimension},
            export_rows=tuple(),
        )

    linear = restricted_linear_recoverability(observation_rows, protected_rows)
    rank_report = restricted_linear_rank_lower_bound(observation_rows, protected_rows)
    row_residual = restricted_linear_rowspace_residual(observation_rows, protected_rows)
    collision_gap = restricted_linear_collision_gap(observation_rows, protected_rows)
    exact = bool(linear.exact_recoverable)
    impossible = not exact
    validity = 'supported'
    weaker_targets: list[str] = []
    basis_targets: list[list[float]] = []
    for index in range(dimension):
        row = np.zeros((1, dimension), dtype=float)
        row[0, index] = 1.0
        if restricted_linear_recoverability(observation_rows, row).exact_recoverable:
            weaker_targets.append(f'coordinate x{index + 1}')
            basis_targets.append(row.reshape(-1).tolist())

    minimal_added, exact_sets = _linear_candidate_exact_sets(observation_rows, protected_rows, candidate_rows)
    chosen = None
    comparison = None
    if not exact and minimal_added is not None and exact_sets:
        combo = exact_sets[0]
        chosen = MixerRecommendation(
            action_id='augment-linear-record',
            title=f'Add {minimal_added} candidate row{'' if minimal_added == 1 else 's'}',
            action_kind='add_measurement',
            rationale='This is the smallest candidate-library augmentation whose row space contains the protected target on the admissible family.',
            theorem_status=theorem_status,
            estimated_cost=float(minimal_added),
            cost_unit='rows',
            expected_regime='exact',
            patch={'candidateIndices': combo},
        )
        augmented = np.vstack([observation_rows, candidate_rows[combo]]) if observation_rows.size else candidate_rows[combo]
        after_gap = restricted_linear_collision_gap(augmented, protected_rows)
        comparison = MixerComparison(
            before_regime='impossible',
            after_regime='exact',
            key_metric='κ(0)',
            before_value=float(collision_gap),
            after_value=float(after_gap),
            changed=after_gap <= 1e-8,
            narrative='The added rows eliminate the protected collision gap by lifting the protected rows into the record row space.',
        )
        recommendations.append(chosen)
    if weaker_targets and impossible:
        recommendations.append(
            MixerRecommendation(
                action_id='weaken-target-linear',
                title=f'Weaken target to {weaker_targets[0]}',
                action_kind='weaken_target',
                rationale='The current record already supports this weaker basis target exactly, so target weakening is a real structural option.',
                theorem_status=theorem_status,
                estimated_cost=None,
                cost_unit=None,
                expected_regime='exact',
                patch={'protectedRows': basis_targets[0]},
            )
        )
    if exact:
        diagnostics.append(
            MixerDiagnostic(
                severity='success',
                code='rowspace-supported',
                title='Protected target lies in the record row space',
                detail='The requested protected rows are already separated on the admissible family, so exact restricted-linear recovery is supported.',
                theorem_status=theorem_status,
            )
        )
    else:
        diagnostics.extend(
            [
                MixerDiagnostic(
                    severity='error',
                    code='rowspace-deficiency',
                    title='Record map does not separate the protected target',
                    detail='At least one protected row lies outside the current observation row space on the admissible family.',
                    theorem_status=theorem_status,
                ),
                MixerDiagnostic(
                    severity='warning',
                    code='collision-gap',
                    title='A protected collision gap survives at zero noise',
                    detail=f'The current κ(0) witness is {collision_gap:.3e}, so exact recovery is blocked until the row-space deficiency is removed.',
                    theorem_status=theorem_status,
                ),
            ]
        )
    objects = _build_linear_objects(dimension, observation_rows, protected_rows, candidate_rows, family_label='Restricted-linear family', theorem_status=theorem_status)
    raw_details = {
        'observation_matrix': observation_rows.tolist(),
        'protected_matrix': protected_rows.tolist(),
        'candidate_rows': candidate_rows.tolist(),
        'rank_observation': rank_report.rank_observation,
        'rank_protected': rank_report.rank_protected,
        'rowspace_residual': row_residual,
        'collision_gap': collision_gap,
        'selected_delta': float(delta),
        'selected_upper_bound': None if linear.recovery_operator is None else float(np.linalg.norm(linear.recovery_operator, ord=2) * delta),
        'minimal_added_rows': minimal_added,
        'candidate_exact_sets': exact_sets,
        'weaker_basis_targets': weaker_targets,
    }
    export_rows = ({
        'family': 'linear',
        'regime': _regime(exact=exact, impossible=impossible),
        'rank_observation': rank_report.rank_observation,
        'rank_protected': rank_report.rank_protected,
        'rowspace_residual': row_residual,
        'collision_gap': collision_gap,
        'minimal_added_rows': -1 if minimal_added is None else minimal_added,
    },)
    return MixerReport(
        title='Custom restricted-linear composition',
        mode='custom',
        family='linear',
        family_label='Restricted-linear family',
        validity=validity,
        regime=_regime(exact=exact, impossible=impossible),
        exact=exact,
        approximate=False,
        asymptotic=False,
        impossible=impossible,
        unsupported=False,
        theorem_status=theorem_status,
        support_scope='Finite-dimensional restricted-linear family on an explicit coefficient box.',
        protected_label=f'{protected_rows.shape[0]} protected row(s)',
        observation_label=f'{observation_rows.shape[0]} observation row(s)',
        architecture_label='restricted-linear exact recovery / augmentation search',
        target_split_summary='; '.join(weaker_targets) if weaker_targets else 'No weaker basis target was automatically certified.',
        root_cause='Current record row space is insufficient.' if impossible else 'Current record row space is sufficient.',
        missing_structure='Add rows until the protected rows lie in the record row space.' if impossible else 'No structural augmentation is required.',
        objects=objects,
        diagnostics=tuple(diagnostics),
        recommendations=tuple(recommendations),
        chosen_recommendation=chosen,
        comparison=comparison,
        theorem_links=LINEAR_THEOREM_LINKS,
        supported_calculations=(
            'rank checks',
            'row-space residual',
            'collision-gap analysis',
            'candidate-library minimal augmentation search',
            'weaker basis-target scan',
        ),
        raw_details=raw_details,
        export_rows=tuple(export_rows),
    )


def analyze_periodic_custom_case(*, functional_text: str, observation: str, cutoff: int, delta: float = 2.0) -> MixerReport:
    diagnostics: list[MixerDiagnostic] = []
    recommendations: list[MixerRecommendation] = []
    theorem_status = 'family-specific periodic threshold result'
    try:
        coeffs = _parse_linear_expression(functional_text, prefix='a', dimension=4)
    except ValueError as exc:
        diagnostics.append(MixerDiagnostic('error', 'unsupported-periodic-expression', 'Periodic functional is unsupported', str(exc), 'unsupported'))
        return MixerReport(
            title='Custom periodic modal composition',
            mode='custom',
            family='periodic',
            family_label='Periodic four-mode modal family',
            validity='unsupported',
            regime='unsupported',
            exact=False,
            approximate=False,
            asymptotic=False,
            impossible=False,
            unsupported=True,
            theorem_status='unsupported',
            support_scope='Only linear functionals in a1..a4 are supported.',
            protected_label='unsupported periodic target',
            observation_label=observation.replace('_', ' '),
            architecture_label='periodic modal recovery',
            target_split_summary='No supported target split available.',
            root_cause='The periodic target could not be reduced to a supported modal functional.',
            missing_structure='Reformulate the target as a linear combination of a1..a4.',
            objects=tuple(),
            diagnostics=tuple(diagnostics),
            recommendations=(
                MixerRecommendation('reformulate-periodic', 'Use a linear modal functional in a1..a4', 'reformulate', 'The current engine only supports modal functionals on the explicit four-mode basis.', 'unsupported -> nearest supported template', None, None, 'unsupported', None),
            ),
            chosen_recommendation=None,
            comparison=None,
            theorem_links=PERIODIC_THEOREM_LINKS,
            supported_calculations=('syntax validation',),
            raw_details={'functional_text': functional_text},
            export_rows=tuple(),
        )
    visible = coeffs.copy()
    if observation == 'full_vorticity':
        exact = True
        impossible = False
        predicted_cutoff = 0
        hidden_l1 = 0.0
        root_cause = 'Full vorticity sees the whole protected support on this finite family.'
        missing = 'None.'
    elif observation == 'cutoff_vorticity':
        predicted_cutoff = max((index + 1 for index, value in enumerate(coeffs) if abs(float(value)) > EPS), default=0)
        visible[int(cutoff):] = 0.0
        hidden_l1 = float(np.sum(np.abs(coeffs[int(cutoff):])))
        exact = hidden_l1 <= EPS
        impossible = not exact
        root_cause = 'The cutoff misses part of the protected support.' if impossible else 'The cutoff contains the whole protected support.'
        missing = f'Raise the cutoff to at least {predicted_cutoff}.' if impossible else 'No cutoff change is needed.'
    else:
        predicted_cutoff = None
        hidden_l1 = float(np.sum(np.abs(coeffs)))
        exact = hidden_l1 <= EPS
        impossible = hidden_l1 > EPS
        root_cause = 'Divergence-only data is blind to the modal target on this family.' if impossible else 'The target is trivial under divergence-only data.'
        missing = 'Switch to a richer record or weaken the target to a divergence certificate.' if impossible else 'No change needed.'
    kappa0 = 2.0 * hidden_l1
    if impossible and observation == 'cutoff_vorticity' and predicted_cutoff is not None:
        chosen = MixerRecommendation(
            'raise-periodic-cutoff',
            f'Raise cutoff to {predicted_cutoff}',
            'add_mode',
            'The protected functional has hidden support above the retained cutoff, so exact recovery begins at the first cutoff containing every active protected mode.',
            theorem_status,
            float(max(0, predicted_cutoff - cutoff)),
            'modes',
            'exact',
            {'periodicCutoff': predicted_cutoff},
        )
        recommendations.append(chosen)
        comparison = MixerComparison('impossible', 'exact', 'κ(0)', float(kappa0), 0.0, True, 'Increasing the cutoff removes every hidden protected coefficient from the zero-noise collision set.')
    elif impossible and observation == 'divergence_only':
        chosen = MixerRecommendation(
            'switch-periodic-record',
            'Switch to full or cutoff vorticity',
            'switch_architecture',
            'The divergence-only record is structurally blind to the periodic modal target, so exact recovery needs a record that actually resolves modal content.',
            'family-specific no-go',
            None,
            None,
            'exact',
            {'periodicObservation': 'full_vorticity'},
        )
        recommendations.append(chosen)
        comparison = MixerComparison('impossible', 'exact', 'κ(0)', float(kappa0), 0.0, True, 'Switching to a vorticity record resolves the modal coefficients that the divergence-only record misses.')
    else:
        chosen = None
        comparison = None
    if impossible and np.linalg.norm(visible) > EPS:
        recommendations.append(
            MixerRecommendation(
                'weaken-periodic-target',
                'Weaken target to visible support only',
                'weaken_target',
                'The visible part of the functional already lies on the retained support, so weakening the target is an honest same-record alternative.',
                theorem_status,
                None,
                None,
                'exact',
                {'periodicFunctionalText': ' + '.join([f'{visible[i]:g}*a{i + 1}' for i in range(4) if abs(visible[i]) > EPS]) or 'a1'},
            )
        )
    diagnostics.append(
        MixerDiagnostic(
            severity='success' if exact else 'error',
            code='periodic-support-check',
            title='Protected support versus retained support',
            detail=root_cause,
            theorem_status=theorem_status,
        )
    )
    objects = (
        MixerObject('periodic-basis', 'Periodic four-mode basis', 'state_space', 'periodic', '—', 'R^4', '4', 'a1..a4', 'linear', theorem_status, PERIODIC_THEOREM_LINKS, ('modal basis fixed to a1..a4',), ('supported periodic toy family',)),
        MixerObject('periodic-record', observation.replace('_', ' '), 'record_map', 'periodic', 'R^4', 'record space', 'family-specific', 'modal/vorticity', 'linear', theorem_status, PERIODIC_THEOREM_LINKS, ('record must be one of the supported periodic choices',), (f'cutoff={cutoff}' if observation == 'cutoff_vorticity' else 'record has fixed support semantics',)),
        MixerObject('periodic-target', 'Custom modal functional', 'protected_variable', 'periodic', 'R^4', 'R', '1x4', 'a1..a4', 'linear', theorem_status, PERIODIC_THEOREM_LINKS, ('functional must be linear in a1..a4',), (functional_text,)),
    )
    export_rows = ({
        'family': 'periodic',
        'regime': _regime(exact=exact, impossible=impossible),
        'observation': observation,
        'cutoff': cutoff,
        'kappa0': kappa0,
        'predicted_min_cutoff': -1 if predicted_cutoff is None else predicted_cutoff,
    },)
    return MixerReport(
        title='Custom periodic modal composition',
        mode='custom',
        family='periodic',
        family_label='Periodic four-mode modal family',
        validity='supported',
        regime=_regime(exact=exact, impossible=impossible),
        exact=exact,
        approximate=False,
        asymptotic=False,
        impossible=impossible,
        unsupported=False,
        theorem_status=theorem_status,
        support_scope='Periodic four-mode family with linear modal functionals.',
        protected_label=functional_text,
        observation_label=observation.replace('_', ' '),
        architecture_label='periodic modal threshold analysis',
        target_split_summary='The visible-support truncation is recoverable under the same record.' if impossible and np.linalg.norm(visible) > EPS else 'No weaker same-record target was generated.',
        root_cause=root_cause,
        missing_structure=missing,
        objects=objects,
        diagnostics=tuple(diagnostics),
        recommendations=tuple(recommendations),
        chosen_recommendation=chosen,
        comparison=comparison,
        theorem_links=PERIODIC_THEOREM_LINKS,
        supported_calculations=('support analysis', 'exact/impossible cutoff logic', 'same-record weaker-target detection'),
        raw_details={'coefficients': coeffs.tolist(), 'visible_coefficients': visible.tolist(), 'hidden_l1': hidden_l1, 'kappa0': kappa0, 'predicted_min_cutoff': predicted_cutoff, 'selected_delta': float(delta)},
        export_rows=tuple(export_rows),
    )


def _parse_control_target(text: str, dimension: int) -> tuple[str, Array]:
    cleaned = text.strip().lower()
    if re.fullmatch(r'moment\((\d+)\)', cleaned):
        order = int(re.fullmatch(r'moment\((\d+)\)', cleaned).group(1))
        lambdas = np.asarray(DIAGONAL_EIGENVALUES[:dimension], dtype=float)
        return f'moment({order})', lambdas**order
    if re.fullmatch(r'x(\d+)', cleaned):
        index = int(re.fullmatch(r'x(\d+)', cleaned).group(1)) - 1
        if index < 0 or index >= dimension:
            raise ValueError('coordinate target index is outside the sensor profile dimension')
        row = np.zeros(dimension, dtype=float)
        row[index] = 1.0
        return f'x{index + 1}', row
    if re.search(r'[A-Za-z]', cleaned):
        return 'custom_functional', _parse_linear_expression(cleaned, prefix='x', dimension=dimension)
    row = np.asarray([_safe_float(token) for token in re.split(r'[\s,]+', cleaned) if token.strip()], dtype=float)
    if row.size != dimension:
        raise ValueError('custom control functional width does not match the sensor profile dimension')
    return 'custom_functional', row


def analyze_control_custom_case(*, sensor_profile_text: str, target_text: str, horizon: int, delta: float = 0.5) -> MixerReport:
    diagnostics: list[MixerDiagnostic] = []
    recommendations: list[MixerRecommendation] = []
    theorem_status = 'family-specific diagonal/history threshold result'
    try:
        sensor_weights = np.asarray([_safe_float(token) for token in re.split(r'[\s,]+', sensor_profile_text.strip()) if token.strip()], dtype=float)
        if sensor_weights.size < 2:
            raise ValueError('at least two sensor weights are required')
        dimension = int(sensor_weights.size)
        target_label, protected_weights = _parse_control_target(target_text, dimension)
    except ValueError as exc:
        diagnostics.append(MixerDiagnostic('error', 'unsupported-control-input', 'Control/history input is unsupported', str(exc), 'unsupported'))
        return MixerReport(
            title='Custom diagonal/history composition',
            mode='custom',
            family='control',
            family_label='Diagonal finite-history family',
            validity='unsupported',
            regime='unsupported',
            exact=False,
            approximate=False,
            asymptotic=False,
            impossible=False,
            unsupported=True,
            theorem_status='unsupported',
            support_scope='Control custom mode only supports diagonal sensor profiles and moment / coordinate / linear-function targets.',
            protected_label='unsupported target',
            observation_label='unsupported history record',
            architecture_label='finite-history exact recovery',
            target_split_summary='No supported target split available.',
            root_cause='The custom control input could not be reduced to the supported diagonal/history family.',
            missing_structure='Use a numeric sensor profile plus moment(k), xi, or a linear functional in x1..xn.',
            objects=tuple(),
            diagnostics=tuple(diagnostics),
            recommendations=(MixerRecommendation('reformulate-control', 'Reformulate as diagonal/history input', 'reformulate', 'The current engine only supports diagonal finite-history reduction for custom control input.', 'unsupported -> nearest supported template', None, None, 'unsupported', None),),
            chosen_recommendation=None,
            comparison=None,
            theorem_links=CONTROL_THEOREM_LINKS,
            supported_calculations=('syntax validation',),
            raw_details={'sensor_profile_text': sensor_profile_text, 'target_text': target_text},
            export_rows=tuple(),
        )
    eigenvalues = DIAGONAL_EIGENVALUES[:dimension]
    O = np.asarray([[sensor_weights[index] * (eigenvalues[index] ** t) for index in range(dimension)] for t in range(int(horizon))], dtype=float)
    L = np.asarray([protected_weights], dtype=float)
    linear = restricted_linear_recoverability(O, L)
    exact = bool(linear.exact_recoverable)
    impossible = not exact
    predicted_min_horizon, weights = diagonal_functional_minimal_horizon(eigenvalues, sensor_weights, protected_weights, max_horizon=max(1, dimension))
    collision_gap = restricted_linear_collision_gap(O, L)
    residual = restricted_linear_rowspace_residual(O, L)
    if impossible and predicted_min_horizon is not None and predicted_min_horizon > horizon:
        chosen = MixerRecommendation(
            'extend-history',
            f'Increase horizon to {predicted_min_horizon}',
            'add_history',
            'The current horizon is too short to interpolate the requested protected functional from the diagonal history record.',
            theorem_status,
            float(predicted_min_horizon - horizon),
            'steps',
            'exact',
            {'controlHorizon': predicted_min_horizon},
        )
        comparison = MixerComparison('impossible', 'exact', 'κ(0)', float(collision_gap), 0.0, True, 'Extending the history horizon provides enough independent rows to interpolate the protected functional exactly.')
        recommendations.append(chosen)
    else:
        chosen = None
        comparison = None
    weaker_targets: list[str] = []
    for order in range(0, 4):
        candidate = np.asarray(eigenvalues, dtype=float) ** order
        if diagonal_functional_history_weights(eigenvalues, sensor_weights, candidate, int(horizon)) is not None:
            weaker_targets.append(f'moment({order})')
    diagnostics.append(MixerDiagnostic('success' if exact else 'error', 'history-threshold', 'Finite-history sufficiency check', 'The record is sufficient for the requested target.' if exact else 'The record horizon is too short for the requested target on the active diagonal family.', theorem_status))
    objects = (
        MixerObject('control-family', 'Diagonal finite-history family', 'admissible_family', 'control', 'state coefficients', f'R^{dimension}', str(dimension), 'diagonal eigenbasis', 'linear', theorem_status, CONTROL_THEOREM_LINKS, ('distinct active eigenvalues', 'declared sensor profile'), (f'sensor profile: {sensor_weights.tolist()}',)),
        MixerObject('control-record', f'{horizon}-step history', 'record_map', 'control', f'R^{dimension}', f'R^{horizon}', f'{horizon}x{dimension}', 'history rows', 'linear', theorem_status, CONTROL_THEOREM_LINKS, ('finite horizon',), ('static finite-history reconstruction',)),
        MixerObject('control-target', target_label, 'protected_variable', 'control', f'R^{dimension}', 'R', f'1x{dimension}', 'diagonal-function weights', 'linear', theorem_status, CONTROL_THEOREM_LINKS, ('target must be diagonal-function reducible',), (target_text,)),
    )
    export_rows = ({'family': 'control', 'regime': _regime(exact=exact, impossible=impossible), 'horizon': horizon, 'predicted_min_horizon': -1 if predicted_min_horizon is None else predicted_min_horizon, 'collision_gap': collision_gap, 'rowspace_residual': residual},)
    return MixerReport(
        title='Custom diagonal/history composition',
        mode='custom',
        family='control',
        family_label='Diagonal finite-history family',
        validity='supported',
        regime=_regime(exact=exact, impossible=impossible),
        exact=exact,
        approximate=False,
        asymptotic=False,
        impossible=impossible,
        unsupported=False,
        theorem_status=theorem_status,
        support_scope='Diagonal finite-history family with moment, coordinate, or linear-function targets.',
        protected_label=target_text,
        observation_label=f'{horizon}-step history',
        architecture_label='finite-history exact recovery',
        target_split_summary='; '.join(weaker_targets) if weaker_targets else 'No weaker moment target was automatically certified.',
        root_cause='The finite history already separates the target.' if exact else 'The finite history is too short for the requested target.',
        missing_structure='Increase the horizon or weaken the target.' if impossible else 'No structural change is needed.',
        objects=objects,
        diagnostics=tuple(diagnostics),
        recommendations=tuple(recommendations),
        chosen_recommendation=chosen,
        comparison=comparison,
        theorem_links=CONTROL_THEOREM_LINKS,
        supported_calculations=('history-threshold detection', 'collision-gap analysis', 'diagonal interpolation weights', 'weaker moment scan'),
        raw_details={'sensor_weights': sensor_weights.tolist(), 'protected_weights': protected_weights.tolist(), 'collision_gap': collision_gap, 'rowspace_residual': residual, 'predicted_min_horizon': predicted_min_horizon, 'interpolation_weights': None if weights is None else weights.tolist(), 'selected_delta': float(delta)},
        export_rows=tuple(export_rows),
    )


def analyze_boundary_structured_case(*, architecture: str, protected_key: str, grid_size: int, delta: float = 0.2) -> MixerReport:
    theorem_status = 'restricted exact bounded-domain result plus counterexample layer'
    strong_target = protected_key == 'bounded_velocity_class'
    transplant_mismatch = 9.676e-2
    compatible_error = 5.172e-15
    exact = architecture == 'boundary_compatible_hodge' or (architecture == 'periodic_transplant' and not strong_target)
    impossible = architecture == 'periodic_transplant' and strong_target
    recommendations: list[MixerRecommendation] = []
    chosen = None
    comparison = None
    if impossible:
        chosen = MixerRecommendation(
            'switch-boundary-architecture',
            'Switch to boundary-compatible Hodge projector',
            'switch_architecture',
            'The periodic transplant removes divergence but leaves the strong bounded protected class because it does not preserve the correct boundary-normal trace.',
            theorem_status,
            None,
            None,
            'exact',
            {'boundaryArchitecture': 'boundary_compatible_hodge'},
        )
        recommendations.append(chosen)
        recommendations.append(
            MixerRecommendation(
                'weaken-boundary-target',
                'Weaken target to divergence certificate',
                'weaken_target',
                'The current transplanted architecture can support a weaker bulk divergence certificate even though it fails on the strong bounded class.',
                'family-specific weaker-target split',
                None,
                None,
                'exact',
                {'boundaryProtected': 'divergence_certificate'},
            )
        )
        comparison = MixerComparison('impossible', 'exact', 'boundary mismatch', transplant_mismatch, compatible_error, True, 'Replacing the transplanted projector with the compatible finite-mode Hodge projector removes the boundary mismatch on its admissible family.')
    diagnostics = (
        MixerDiagnostic('success' if exact else 'error', 'boundary-compatibility', 'Boundary compatibility check', 'The current architecture respects the bounded protected class.' if exact else 'The current projector architecture is incompatible with the bounded protected target.', theorem_status),
    )
    objects = (
        MixerObject('boundary-family', 'Bounded finite-mode Hodge family', 'admissible_family', 'boundary', 'field coefficients', 'bounded velocity class', str(grid_size), 'boundary-compatible finite-mode basis', 'linear', theorem_status, BOUNDARY_THEOREM_LINKS, ('bounded domain', 'compatible trace basis'), (f'grid size {grid_size}',)),
        MixerObject('boundary-record', architecture.replace('_', ' '), 'correction_operator', 'boundary', 'bounded velocity class', 'bounded velocity class', str(grid_size), 'projector architecture', 'linear', theorem_status, BOUNDARY_THEOREM_LINKS, ('projector must respect boundary conditions',), ('transplanted periodic projectors are rejected on the strong target',)),
        MixerObject('boundary-target', BOUNDARY_PROTECTED_LABELS[protected_key], 'protected_variable', 'boundary', 'bounded velocity class', 'certificate', 'family-specific', 'bounded basis', 'linear', theorem_status, BOUNDARY_THEOREM_LINKS, ('target must declare whether boundary compatibility matters',), tuple()),
    )
    return MixerReport(
        title='Structured bounded-domain composition',
        mode='structured',
        family='boundary',
        family_label='Bounded-domain architecture benchmark',
        validity='supported',
        regime=_regime(exact=exact, impossible=impossible),
        exact=exact,
        approximate=False,
        asymptotic=False,
        impossible=impossible,
        unsupported=False,
        theorem_status=theorem_status,
        support_scope='Restricted bounded-domain family with theorem-backed compatible Hodge replacement.',
        protected_label=BOUNDARY_PROTECTED_LABELS[protected_key],
        observation_label=architecture.replace('_', ' '),
        architecture_label=architecture.replace('_', ' '),
        target_split_summary='bulk divergence certificate only' if impossible else 'No weaker target needed.',
        root_cause='The transplanted periodic projector is incompatible with the bounded protected class.' if impossible else 'The architecture is compatible with the current bounded target.',
        missing_structure='Use the boundary-compatible finite-mode Hodge family.' if impossible else 'No structural change is needed.',
        objects=objects,
        diagnostics=diagnostics,
        recommendations=tuple(recommendations),
        chosen_recommendation=chosen,
        comparison=comparison,
        theorem_links=BOUNDARY_THEOREM_LINKS,
        supported_calculations=('boundary compatibility check', 'architecture swap guidance', 'weaker-target alternative'),
        raw_details={'grid_size': grid_size, 'transplant_boundary_mismatch': transplant_mismatch, 'compatible_recovery_error': compatible_error, 'selected_delta': float(delta)},
        export_rows=({'family': 'boundary', 'regime': _regime(exact=exact, impossible=impossible), 'boundary_mismatch': transplant_mismatch, 'compatible_recovery_error': compatible_error},),
    )


def analyze_structured_mixer_case(*, family: str, config: dict[str, Any]) -> MixerReport:
    if family == 'periodic':
        protected_key = str(config.get('periodicProtected', 'full_weighted_sum'))
        meta = PERIODIC_PROTECTED_OPTIONS[protected_key]
        cutoff = int(config.get('periodicCutoff', 1))
        observation = str(config.get('periodicObservation', 'cutoff_vorticity'))
        if meta['kind'] == 'selector':
            coeffs = np.zeros(4, dtype=float)
            if protected_key == 'mode_1_coefficient':
                coeffs[0] = 1.0
            elif protected_key == 'modes_1_2_coefficients':
                coeffs[0:2] = 1.0
            else:
                coeffs[:] = 1.0
        else:
            lookup = {
                'low_mode_sum': np.array([1.0, 1.0, 0.0, 0.0]),
                'bandlimited_contrast': np.array([1.0, -1.0, 1.0, 0.0]),
                'full_weighted_sum': np.array([1.0, 1.0, 1.0, 1.0]),
            }
            coeffs = lookup.get(protected_key, np.array([1.0, 1.0, 1.0, 1.0]))
        expr = ' + '.join([f'{coeff:g}*a{i + 1}' for i, coeff in enumerate(coeffs) if abs(float(coeff)) > EPS])
        report = analyze_periodic_custom_case(functional_text=expr, observation=observation, cutoff=cutoff, delta=float(config.get('periodicDelta', 2.0)))
        return replace(report, mode='structured', title='Structured periodic composition', protected_label=meta['label'])
    if family == 'control':
        profile_key = str(config.get('controlProfile', 'three_active'))
        sensor_profile = CONTROL_PROFILES.get(profile_key, CONTROL_PROFILES['three_active'])
        functional_key = str(config.get('controlFunctional', 'second_moment'))
        target_map = {
            'sensor_sum': 'moment(0)',
            'first_moment': 'moment(1)',
            'second_moment': 'moment(2)',
            'protected_coordinate': 'x3',
        }
        report = analyze_control_custom_case(sensor_profile_text=','.join(f'{value:g}' for value in sensor_profile), target_text=target_map.get(functional_key, 'x3'), horizon=int(config.get('controlHorizon', 2)), delta=float(config.get('controlDelta', 0.5)))
        return replace(report, mode='structured', title='Structured control/history composition', protected_label=CONTROL_FUNCTIONAL_LABELS.get(functional_key, functional_key))
    if family == 'boundary':
        return analyze_boundary_structured_case(architecture=str(config.get('boundaryArchitecture', 'periodic_transplant')), protected_key=str(config.get('boundaryProtected', 'bounded_velocity_class')), grid_size=int(config.get('boundaryGridSize', 17)), delta=float(config.get('boundaryDelta', 0.2)))
    observation_rows = []
    template = LINEAR_TEMPLATE_LIBRARY[str(config.get('linearTemplate', 'sensor_basis'))]
    for candidate in template['candidates']:
        if config.get('linearMeasurements', {}).get(candidate['id']):
            observation_rows.append(candidate['row'])
    protected_key = str(config.get('linearProtected', 'x3'))
    protected = template['protected_options'][protected_key]['rows']
    candidate_rows = [candidate['row'] for candidate in template['candidates'] if not config.get('linearMeasurements', {}).get(candidate['id'])]
    report = analyze_linear_custom_case(
        dimension=3,
        observation_text='\n'.join(','.join(str(value) for value in row) for row in observation_rows) if observation_rows else '0,0,0',
        protected_text='\n'.join(','.join(str(value) for value in row) for row in protected),
        candidate_text='\n'.join(','.join(str(value) for value in row) for row in candidate_rows),
        delta=float(config.get('linearDelta', 1.0)),
    )
    return replace(report, mode='structured', title='Structured restricted-linear composition', protected_label=template['protected_options'][protected_key]['label'])


def _random_linear_case(rng: random.Random) -> tuple[dict[str, Any], MixerReport]:
    template = LINEAR_TEMPLATE_LIBRARY['sensor_basis']
    measurement_ids = [candidate['id'] for candidate in template['candidates']]
    protected_choices = list(template['protected_options'].keys())
    for _ in range(64):
        chosen_measurements = {measurement_id: rng.random() < 0.45 for measurement_id in measurement_ids}
        if not any(chosen_measurements.values()):
            continue
        protected_key = rng.choice(protected_choices)
        report = analyze_structured_mixer_case(
            family='linear',
            config={
                'linearTemplate': 'sensor_basis',
                'linearProtected': protected_key,
                'linearMeasurements': chosen_measurements,
                'linearDelta': 1.0,
            },
        )
        if report.impossible and report.chosen_recommendation is not None:
            return ({'family': 'linear', 'linearTemplate': 'sensor_basis', 'linearProtected': protected_key, 'linearMeasurements': chosen_measurements, 'linearDelta': 1.0}, report)
    fallback = {'family': 'linear', 'linearTemplate': 'sensor_basis', 'linearProtected': 'x3', 'linearMeasurements': {'measure_x1': True, 'measure_x2_plus_x3': True, 'measure_x2': False, 'measure_x3': False, 'measure_x1_plus_x2': False}, 'linearDelta': 1.0}
    return fallback, analyze_structured_mixer_case(family='linear', config=fallback)


def _random_periodic_case(rng: random.Random) -> tuple[dict[str, Any], MixerReport]:
    coeffs = [rng.choice([-2.0, -1.0, 0.0, 1.0, 2.0]) for _ in range(4)]
    if all(abs(value) <= EPS for value in coeffs):
        coeffs[0] = 1.0
    cutoff = rng.randint(1, 3)
    expr = ' + '.join([f'{value:g}*a{i + 1}' for i, value in enumerate(coeffs) if abs(value) > EPS])
    report = analyze_periodic_custom_case(functional_text=expr, observation='cutoff_vorticity', cutoff=cutoff, delta=2.0)
    return ({'family': 'periodic', 'periodicFunctionalText': expr, 'periodicObservation': 'cutoff_vorticity', 'periodicCutoff': cutoff, 'periodicDelta': 2.0}, report)


def _random_control_case(rng: random.Random) -> tuple[dict[str, Any], MixerReport]:
    profile = [rng.choice([0.0, 0.2, 0.4, 1.0]) for _ in range(4)]
    if sum(1 for value in profile if abs(value) > EPS) < 2:
        profile[0] = 1.0
        profile[1] = 0.4
    horizon = rng.randint(1, 3)
    target = rng.choice(['moment(0)', 'moment(1)', 'moment(2)', 'x3', 'x4'])
    report = analyze_control_custom_case(sensor_profile_text=','.join(f'{value:g}' for value in profile), target_text=target, horizon=horizon, delta=0.5)
    return ({'family': 'control', 'controlSensorProfileText': ','.join(f'{value:g}' for value in profile), 'controlTargetText': target, 'controlHorizon': horizon, 'controlDelta': 0.5}, report)


def analyze_random_mixer_case(*, family: str, seed: int) -> tuple[dict[str, Any], MixerReport]:
    rng = random.Random(int(seed))
    if family == 'periodic':
        return _random_periodic_case(rng)
    if family == 'control':
        return _random_control_case(rng)
    return _random_linear_case(rng)


def discovery_mixer_demo_reports() -> dict[str, Any]:
    demos: dict[str, MixerReport] = {}
    demos['periodic_user_builder'] = analyze_structured_mixer_case(family='periodic', config={'periodicProtected': 'full_weighted_sum', 'periodicObservation': 'cutoff_vorticity', 'periodicCutoff': 3, 'periodicDelta': 2.0})
    demos['control_history_builder'] = analyze_structured_mixer_case(family='control', config={'controlProfile': 'three_active', 'controlFunctional': 'second_moment', 'controlHorizon': 2, 'controlDelta': 0.5})
    demos['weaker_stronger_split'] = analyze_periodic_custom_case(functional_text='1*a1 + 1*a2 + 1*a4', observation='cutoff_vorticity', cutoff=2, delta=2.0)
    demos['custom_matrix_builder'] = analyze_linear_custom_case(dimension=3, observation_text='x1\nx2 + x3', protected_text='x3', candidate_text='x2\nx3\nx1 + x2', delta=1.0)
    _, random_demo = analyze_random_mixer_case(family='linear', seed=37)
    demos['random_discovery_case'] = random_demo
    rows = []
    for key, report in demos.items():
        rows.append({
            'demo': key,
            'family': report.family,
            'regime': report.regime,
            'exact': report.exact,
            'unsupported': report.unsupported,
            'root_cause': report.root_cause,
            'chosen_fix': report.chosen_recommendation.title if report.chosen_recommendation else 'none',
            'after_regime': report.comparison.after_regime if report.comparison else report.regime,
        })
    return {
        'summary': {
            'demo_count': len(demos),
            'exact_after_count': sum(1 for report in demos.values() if report.comparison and report.comparison.after_regime == 'exact' or report.exact),
            'unsupported_count': sum(1 for report in demos.values() if report.unsupported),
        },
        'demos': {key: report.to_dict() for key, report in demos.items()},
        'rows': rows,
    }
