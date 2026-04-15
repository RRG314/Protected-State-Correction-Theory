from __future__ import annotations

from dataclasses import asdict, dataclass
from functools import lru_cache
from typing import Any, Mapping, Sequence

import numpy as np

from .design import linear_recoverability_design_report
from .cfd import bounded_hodge_projection_report
from .physics import bounded_domain_projection_counterexample
from .recoverability import (
    EPS,
    diagonal_functional_minimal_horizon,
    diagonal_functional_history_weights,
    periodic_functional_complexity_sweep,
    periodic_protected_complexity_sweep,
    qubit_phase_collision_formula,
    restricted_linear_recoverability,
)

Array = np.ndarray


LINEAR_TEMPLATE_LIBRARY: dict[str, dict[str, Any]] = {
    'sensor_basis': {
        'label': '3-state static record template',
        'candidates': [
            {'id': 'measure_x1', 'label': 'measure x1', 'row': [1.0, 0.0, 0.0]},
            {'id': 'measure_x2', 'label': 'measure x2', 'row': [0.0, 1.0, 0.0]},
            {'id': 'measure_x3', 'label': 'measure x3', 'row': [0.0, 0.0, 1.0]},
            {'id': 'measure_x2_plus_x3', 'label': 'measure x2+x3', 'row': [0.0, 1.0, 1.0]},
            {'id': 'measure_x1_plus_x2', 'label': 'measure x1+x2', 'row': [1.0, 1.0, 0.0]},
        ],
        'protected_options': {
            'x3': {'label': 'coordinate x3', 'rows': [[0.0, 0.0, 1.0]]},
            'x2_plus_x3': {'label': 'sum x2+x3', 'rows': [[0.0, 1.0, 1.0]]},
            'tail_pair': {'label': 'tail pair (x2, x3)', 'rows': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
            'full_state': {
                'label': 'full state (x1, x2, x3)',
                'rows': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            },
        },
        'default_measurements': ('measure_x1', 'measure_x2_plus_x3'),
    }
}

PERIODIC_PROTECTED_OPTIONS: dict[str, dict[str, Any]] = {
    'mode_1_coefficient': {'label': 'leading modal coefficient', 'predicted_min_cutoff': 1, 'kind': 'selector'},
    'modes_1_2_coefficients': {'label': 'first two modal coefficients', 'predicted_min_cutoff': 2, 'kind': 'selector'},
    'full_modal_coefficients': {'label': 'full four-mode coefficient vector', 'predicted_min_cutoff': 4, 'kind': 'selector'},
    'low_mode_sum': {'label': 'low-mode weighted sum', 'predicted_min_cutoff': 2, 'kind': 'functional'},
    'bandlimited_contrast': {'label': 'band-limited contrast functional', 'predicted_min_cutoff': 3, 'kind': 'functional'},
    'full_weighted_sum': {'label': 'full weighted modal sum', 'predicted_min_cutoff': 4, 'kind': 'functional'},
}

CONTROL_PROFILES: dict[str, tuple[float, ...]] = {
    'three_active': (1.0, 0.4, 0.2),
    'two_active': (1.0, 0.0, 0.2),
    'protected_hidden': (1.0, 0.4, 0.0),
}

CONTROL_FUNCTIONAL_LABELS: dict[str, str] = {
    'protected_coordinate': 'third coordinate x3',
    'sensor_sum': 'sensor-weighted state sum',
    'first_moment': 'first sensor moment functional',
    'second_moment': 'second sensor moment functional',
}

BOUNDARY_PROTECTED_LABELS: dict[str, str] = {
    'bounded_velocity_class': 'bounded velocity class with boundary compatibility',
    'divergence_certificate': 'bulk divergence certificate only',
}


@dataclass(frozen=True)
class StructuralFixOption:
    fix_id: str
    title: str
    action_kind: str
    rationale: str
    theorem_status: str
    minimal: bool
    cost: float | None
    cost_unit: str | None
    expected_regime: str
    applies_config: dict[str, Any]


@dataclass(frozen=True)
class StructuralComparison:
    before_regime: str
    after_regime: str
    regime_changed: bool
    key_metric_name: str
    key_metric_before: float
    key_metric_after: float
    exact_after: bool
    impossible_after: bool
    narrative: str


@dataclass(frozen=True)
class StructuralDiscoveryReport:
    family: str
    title: str
    protected_label: str
    observation_label: str
    current_regime: str
    exact: bool
    asymptotic: bool
    impossible: bool
    theorem_status: str
    protected_object: str
    disturbance_description: str
    current_failure_summary: str
    missing_structure: str
    failure_modes: tuple[str, ...]
    weaker_targets: tuple[str, ...]
    recommendations: tuple[StructuralFixOption, ...]
    chosen_fix: StructuralFixOption | None
    comparison: StructuralComparison | None
    proof_links: tuple[str, ...]
    limitations: tuple[str, ...]
    metrics: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        return data


def _regime_label(*, exact: bool, asymptotic: bool, impossible: bool) -> str:
    if exact:
        return 'exact'
    if asymptotic:
        return 'asymptotic'
    if impossible:
        return 'impossible'
    return 'approximate'


def _linear_template_rows(template_name: str, measurement_ids: Sequence[str]) -> tuple[list[dict[str, Any]], list[list[float]], dict[str, Any]]:
    template = LINEAR_TEMPLATE_LIBRARY[template_name]
    active = [candidate for candidate in template['candidates'] if candidate['id'] in measurement_ids]
    return active, [candidate['row'] for candidate in active], template


def _linear_weaker_targets(template_name: str, observation_matrix: Array, protected_key: str) -> tuple[str, ...]:
    template = LINEAR_TEMPLATE_LIBRARY[template_name]
    weaker: list[str] = []
    for key, option in template['protected_options'].items():
        rows = np.asarray(option['rows'], dtype=float)
        report = restricted_linear_recoverability(observation_matrix, rows)
        if report.exact_recoverable and key != protected_key:
            weaker.append(option['label'])
    return tuple(weaker)


@lru_cache(maxsize=8)
def _cached_periodic_protected_sweep() -> dict[str, Any]:
    return periodic_protected_complexity_sweep(cutoffs=(0, 1, 2, 3, 4))


@lru_cache(maxsize=8)
def _cached_periodic_functional_sweep() -> dict[str, Any]:
    return periodic_functional_complexity_sweep(cutoffs=(0, 1, 2, 3, 4))


def _periodic_rows_for_key(protected_key: str) -> tuple[dict[int, Mapping[str, Any]], int]:
    protected_meta = PERIODIC_PROTECTED_OPTIONS[protected_key]
    if protected_meta['kind'] == 'selector':
        sweep = _cached_periodic_protected_sweep()
        rows = [row for row in sweep['rows'] if row['protected_variable'] == protected_key]
    else:
        sweep = _cached_periodic_functional_sweep()
        rows = [row for row in sweep['rows'] if row['functional_name'] == protected_key]
    predicted = int(protected_meta['predicted_min_cutoff'])
    return {int(row['cutoff']): row for row in rows}, predicted


def discover_linear_template_structure(
    *,
    template_name: str = 'sensor_basis',
    protected_key: str = 'x3',
    measurement_ids: Sequence[str] | None = None,
) -> StructuralDiscoveryReport:
    if measurement_ids is None:
        measurement_ids = LINEAR_TEMPLATE_LIBRARY[template_name]['default_measurements']
    active_candidates, active_rows, template = _linear_template_rows(template_name, measurement_ids)
    protected_option = template['protected_options'][protected_key]
    observation = np.asarray(active_rows, dtype=float) if active_rows else np.zeros((0, len(template['candidates'][0]['row'])), dtype=float)
    protected = np.asarray(protected_option['rows'], dtype=float)
    remaining_candidates = [candidate for candidate in template['candidates'] if candidate['id'] not in measurement_ids]
    design = linear_recoverability_design_report(
        observation,
        protected,
        candidate_rows=[candidate['row'] for candidate in remaining_candidates],
    )
    exact = bool(design.exact_recoverable)
    weaker_targets = _linear_weaker_targets(template_name, observation, protected_key)
    failure_modes: list[str] = []
    recommendations: list[StructuralFixOption] = []
    chosen_fix = None
    comparison = None
    current_regime = _regime_label(exact=exact, asymptotic=False, impossible=not exact)
    active_labels = [candidate['label'] for candidate in active_candidates]
    observation_label = ', '.join(active_labels) if active_labels else 'no active measurement rows'

    if not exact:
        if design.nullspace_protected_gap > EPS:
            failure_modes.append('nullspace witness changes the protected target while leaving the record fixed')
        if design.unrecoverable_row_indices:
            failure_modes.append('protected row space is not contained in the active observation row space')
        if design.candidate_exact_sets:
            for combo in design.candidate_exact_sets:
                combo_labels = [remaining_candidates[index]['label'] for index in combo]
                fix = StructuralFixOption(
                    fix_id='add-measurement-' + '-'.join(str(index) for index in combo),
                    title='Add minimal measurement set',
                    action_kind='add_measurement',
                    rationale='These added rows are the smallest candidate-library augmentation that makes the protected row space observable on the restricted family.',
                    theorem_status='proved on the restricted-linear branch',
                    minimal=True,
                    cost=float(len(combo)),
                    cost_unit='measurements',
                    expected_regime='exact',
                    applies_config={'linearMeasurements': {candidate['id']: True for candidate in active_candidates + [remaining_candidates[index] for index in combo]}},
                )
                recommendations.append(fix)
            chosen_fix = recommendations[0]
        if weaker_targets:
            for label in weaker_targets:
                key = next(k for k, option in template['protected_options'].items() if option['label'] == label)
                recommendations.append(
                    StructuralFixOption(
                        fix_id=f'weaken-{key}',
                        title=f'Weaken target to {label}',
                        action_kind='weaken_target',
                        rationale='The current record already supports this weaker protected target exactly, so weakening the target is a real structural option rather than a cosmetic fallback.',
                        theorem_status='proved on the restricted-linear branch',
                        minimal=False,
                        cost=None,
                        cost_unit=None,
                        expected_regime='exact',
                        applies_config={'linearProtected': key},
                    )
                )
        if chosen_fix is None and recommendations:
            chosen_fix = recommendations[0]
        if chosen_fix is not None:
            updated_measurements = tuple(
                key for key, value in chosen_fix.applies_config.get('linearMeasurements', {candidate['id']: True for candidate in active_candidates}).items() if value
            ) or measurement_ids
            updated_protected = chosen_fix.applies_config.get('linearProtected', protected_key)
            after_report = discover_linear_template_structure(
                template_name=template_name,
                protected_key=updated_protected,
                measurement_ids=updated_measurements,
            )
            comparison = StructuralComparison(
                before_regime=current_regime,
                after_regime=after_report.current_regime,
                regime_changed=current_regime != after_report.current_regime,
                key_metric_name='collision gap',
                key_metric_before=float(design.nullspace_protected_gap),
                key_metric_after=float(after_report.metrics['nullspace_protected_gap']),
                exact_after=after_report.exact,
                impossible_after=after_report.impossible,
                narrative='The proposed augmentation removes the protected-variable-changing nullspace witness and moves the restricted family into the exact regime.' if after_report.exact else 'The proposed change does not reach exact recoverability.',
            )
    else:
        recommendations.append(
            StructuralFixOption(
                fix_id='keep-current',
                title='Keep current record',
                action_kind='keep',
                rationale='The protected target already lies in the active row space, so no structural augmentation is needed for exact recovery on this restricted family.',
                theorem_status='proved on the restricted-linear branch',
                minimal=True,
                cost=0.0,
                cost_unit='measurements',
                expected_regime='exact',
                applies_config={'linearMeasurements': {candidate['id']: True for candidate in active_candidates}},
            )
        )

    return StructuralDiscoveryReport(
        family='restricted_linear',
        title='Restricted-linear structural discovery',
        protected_label=protected_option['label'],
        observation_label=observation_label,
        current_regime=current_regime,
        exact=exact,
        asymptotic=False,
        impossible=not exact,
        theorem_status='theorem-backed in the restricted-linear branch',
        protected_object='chosen protected row family Lx on a finite restricted linear state family',
        disturbance_description='state differences that remain invisible to the active record rows',
        current_failure_summary='Exact recovery is blocked because the current measurement rows do not span the protected row family.' if not exact else 'Exact recovery is already supported by row-space inclusion.',
        missing_structure='Add measurement rows that span the unrecoverable protected rows.' if not exact else 'No missing structure remains for the current target.',
        failure_modes=tuple(failure_modes),
        weaker_targets=weaker_targets,
        recommendations=tuple(recommendations),
        chosen_fix=chosen_fix,
        comparison=comparison,
        proof_links=(
            'docs/theory/advanced-directions/pvrt-theory-program.md',
            'docs/theorem-candidates/pvrt-theorem-spine.md',
            'docs/app/structural-discovery-studio.md',
        ),
        limitations=(
            'restricted finite-dimensional linear family only',
            'candidate-library augmentation is exact only inside the provided row library',
        ),
        metrics={
            'rank_observation': int(design.rank_observation),
            'rank_protected': int(design.rank_protected),
            'nullspace_protected_gap': float(design.nullspace_protected_gap),
            'unrestricted_minimal_added_measurements': int(design.unrestricted_minimal_added_measurements),
            'candidate_minimal_added_measurements': design.minimal_added_measurements,
            'row_space_residuals': list(design.row_space_residuals),
            'unrecoverable_row_indices': list(design.unrecoverable_row_indices),
            'weaker_target_count': len(weaker_targets),
        },
    )


def discover_periodic_modal_structure(
    *,
    protected_key: str = 'full_weighted_sum',
    observation: str = 'cutoff_vorticity',
    cutoff: int = 1,
) -> StructuralDiscoveryReport:
    if protected_key not in PERIODIC_PROTECTED_OPTIONS:
        raise KeyError(protected_key)
    protected_meta = PERIODIC_PROTECTED_OPTIONS[protected_key]
    row_by_cutoff, predicted = _periodic_rows_for_key(protected_key)
    current_row = row_by_cutoff[int(cutoff)] if observation == 'cutoff_vorticity' else None
    exact = observation == 'full_vorticity' or (observation == 'cutoff_vorticity' and current_row is not None and bool(current_row['exact_recoverable']))
    impossible = observation == 'divergence_only' or not exact
    current_regime = _regime_label(exact=exact, asymptotic=False, impossible=impossible)
    failure_modes: list[str] = []
    recommendations: list[StructuralFixOption] = []
    chosen_fix = None
    comparison = None
    weaker_targets = tuple(
        meta['label']
        for key, meta in PERIODIC_PROTECTED_OPTIONS.items()
        if key != protected_key and meta['predicted_min_cutoff'] <= (0 if observation == 'divergence_only' else int(cutoff))
    )
    if observation == 'divergence_only':
        failure_modes.append('divergence-only records leave nontrivial incompressible states indistinguishable')
        recommendations.append(
            StructuralFixOption(
                fix_id='switch-to-cutoff',
                title='Switch to a vorticity-based record',
                action_kind='switch_record',
                rationale='The divergence-only no-go blocks exact recovery outright; switching to a vorticity-based record is the smallest meaningful structural change in this finite modal lane.',
                theorem_status='proved no-go plus family-level threshold law',
                minimal=False,
                cost=float(predicted),
                cost_unit='retained cutoff',
                expected_regime='exact',
                applies_config={'periodicObservation': 'cutoff_vorticity', 'periodicCutoff': predicted},
            )
        )
        chosen_fix = recommendations[0]
    elif not exact and current_row is not None:
        failure_modes.append('retained cutoff misses part of the protected modal support')
        recommendations.append(
            StructuralFixOption(
                fix_id='raise-cutoff',
                title=f'Raise cutoff to {predicted}',
                action_kind='add_mode',
                rationale='The protected-support threshold law on the tested modal family says the retained cutoff must include every mode used by the protected variable.',
                theorem_status='family-specific threshold result with repeated falsification',
                minimal=True,
                cost=float(max(0, predicted - int(cutoff))),
                cost_unit='additional cutoff levels',
                expected_regime='exact',
                applies_config={'periodicObservation': 'cutoff_vorticity', 'periodicCutoff': predicted},
            )
        )
        if weaker_targets:
            weaker_key = next(key for key, meta in PERIODIC_PROTECTED_OPTIONS.items() if meta['label'] == weaker_targets[0])
            recommendations.append(
                StructuralFixOption(
                    fix_id=f'weaken-{weaker_key}',
                    title=f'Weaken target to {weaker_targets[0]}',
                    action_kind='weaken_target',
                    rationale='The current retained support already resolves this weaker periodic target exactly.',
                    theorem_status='family-specific threshold result with repeated falsification',
                    minimal=False,
                    cost=None,
                    cost_unit=None,
                    expected_regime='exact',
                    applies_config={'periodicProtected': weaker_key},
                )
            )
        chosen_fix = recommendations[0]
    else:
        recommendations.append(
            StructuralFixOption(
                fix_id='keep-current',
                title='Keep current periodic record',
                action_kind='keep',
                rationale='The retained record already contains the protected support for this finite modal target.',
                theorem_status='family-specific threshold result with repeated falsification',
                minimal=True,
                cost=0.0,
                cost_unit='cutoff levels',
                expected_regime='exact',
                applies_config={'periodicObservation': observation, 'periodicCutoff': cutoff},
            )
        )

    if chosen_fix is not None:
        after_report = discover_periodic_modal_structure(
            protected_key=chosen_fix.applies_config.get('periodicProtected', protected_key),
            observation=chosen_fix.applies_config.get('periodicObservation', observation),
            cutoff=int(chosen_fix.applies_config.get('periodicCutoff', cutoff)),
        )
        current_gap = float(current_row['collision_max_protected_distance']) if current_row is not None else 10.0
        after_gap = float(after_report.metrics['collision_gap'])
        comparison = StructuralComparison(
            before_regime=current_regime,
            after_regime=after_report.current_regime,
            regime_changed=current_regime != after_report.current_regime,
            key_metric_name='collision gap',
            key_metric_before=current_gap,
            key_metric_after=after_gap,
            exact_after=after_report.exact,
            impossible_after=after_report.impossible,
            narrative='The proposed periodic augmentation restores the missing protected modal support and moves the example into the exact branch.' if after_report.exact else 'The proposed periodic change does not restore exact recovery.',
        )

    return StructuralDiscoveryReport(
        family='periodic_modal',
        title='Periodic modal structural discovery',
        protected_label=protected_meta['label'],
        observation_label='full vorticity' if observation == 'full_vorticity' else ('divergence only' if observation == 'divergence_only' else f'cutoff vorticity (cutoff {cutoff})'),
        current_regime=current_regime,
        exact=exact,
        asymptotic=False,
        impossible=impossible,
        theorem_status='family-specific theorem/no-go mix',
        protected_object='chosen periodic modal coefficient or protected functional',
        disturbance_description='unseen modal content or fully unresolved divergence-only ambiguity',
        current_failure_summary='The current periodic record does not resolve every mode used by the protected target.' if not exact else 'The current periodic record resolves the protected support exactly.',
        missing_structure='Retain the full protected modal support in the record, or weaken the target to the currently visible support.' if not exact else 'No missing modal support remains for the current target.',
        failure_modes=tuple(failure_modes),
        weaker_targets=weaker_targets,
        recommendations=tuple(recommendations),
        chosen_fix=chosen_fix,
        comparison=comparison,
        proof_links=(
            'docs/theory/advanced-directions/constrained-observation-results-report.md',
            'docs/theorem-candidates/pvrt-theorem-spine.md',
            'docs/cfd/incompressible-projection.md',
        ),
        limitations=(
            'finite periodic modal family only',
            'protected-support thresholds are family-specific rather than universal PDE laws',
        ),
        metrics={
            'predicted_min_cutoff': predicted,
            'current_cutoff': int(cutoff),
            'collision_gap': float(current_row['collision_max_protected_distance']) if current_row is not None else 10.0,
            'mean_recovery_error': 0.0 if current_row is None else float(current_row['mean_recovery_error']),
            'max_recovery_error': 0.0 if current_row is None else float(current_row['max_recovery_error']),
            'weaker_target_count': len(weaker_targets),
        },
    )


def _control_protected_weights(functional_name: str, sensor_weights: Sequence[float], eigenvalues: Sequence[float]) -> Array:
    couplings = np.asarray(sensor_weights, dtype=float)
    lambdas = np.asarray(eigenvalues, dtype=float)
    if functional_name == 'sensor_sum':
        return couplings.copy()
    if functional_name == 'first_moment':
        return couplings * lambdas
    if functional_name == 'second_moment':
        return couplings * (lambdas**2)
    return np.array([0.0, 0.0, 1.0], dtype=float)


def discover_diagonal_control_structure(
    *,
    profile: str = 'three_active',
    functional_name: str = 'protected_coordinate',
    horizon: int = 2,
) -> StructuralDiscoveryReport:
    sensor_weights = CONTROL_PROFILES[profile]
    eigenvalues = (0.95, 0.8, 0.65)
    protected_weights = _control_protected_weights(functional_name, sensor_weights, eigenvalues)
    predicted_horizon, interpolation_weights = diagonal_functional_minimal_horizon(
        eigenvalues,
        sensor_weights,
        protected_weights,
        max_horizon=4,
    )
    exact = predicted_horizon is not None and int(horizon) >= int(predicted_horizon)
    impossible = predicted_horizon is None or not exact
    current_regime = _regime_label(exact=exact, asymptotic=False, impossible=impossible)
    weaker_targets = tuple(
        CONTROL_FUNCTIONAL_LABELS[name]
        for name in ('sensor_sum', 'first_moment', 'second_moment', 'protected_coordinate')
        if name != functional_name and diagonal_functional_minimal_horizon(
            eigenvalues,
            sensor_weights,
            _control_protected_weights(name, sensor_weights, eigenvalues),
            max_horizon=int(horizon),
        )[0] is not None
    )
    failure_modes: list[str] = []
    recommendations: list[StructuralFixOption] = []
    chosen_fix = None
    comparison = None
    if predicted_horizon is None:
        failure_modes.append('protected functional is not generated by the active sensor moment family')
        if weaker_targets:
            weaker_name = next(name for name, label in CONTROL_FUNCTIONAL_LABELS.items() if label == weaker_targets[0])
            recommendations.append(
                StructuralFixOption(
                    fix_id=f'weaken-{weaker_name}',
                    title=f'Weaken target to {weaker_targets[0]}',
                    action_kind='weaken_target',
                    rationale='The current sensor profile can already reconstruct this lower-complexity functional even though it cannot recover the stronger target.',
                    theorem_status='family-specific threshold result with interpolation checks',
                    minimal=False,
                    cost=None,
                    cost_unit=None,
                    expected_regime='exact',
                    applies_config={'controlFunctional': weaker_name},
                )
            )
            chosen_fix = recommendations[0]
    elif not exact:
        failure_modes.append('finite observation horizon is too short to interpolate the protected functional')
        recommendations.append(
            StructuralFixOption(
                fix_id='increase-horizon',
                title=f'Increase horizon to {predicted_horizon}',
                action_kind='add_history',
                rationale='On the tested diagonal family, exact recovery begins once the history is long enough to interpolate the protected functional on the active sensor spectrum.',
                theorem_status='family-specific threshold result with interpolation checks',
                minimal=True,
                cost=float(int(predicted_horizon) - int(horizon)),
                cost_unit='extra history steps',
                expected_regime='exact',
                applies_config={'controlHorizon': int(predicted_horizon)},
            )
        )
        if weaker_targets:
            weaker_name = next(name for name, label in CONTROL_FUNCTIONAL_LABELS.items() if label == weaker_targets[0])
            recommendations.append(
                StructuralFixOption(
                    fix_id=f'weaken-{weaker_name}',
                    title=f'Weaken target to {weaker_targets[0]}',
                    action_kind='weaken_target',
                    rationale='This weaker functional is already generated by the current history length and sensor profile.',
                    theorem_status='family-specific threshold result with interpolation checks',
                    minimal=False,
                    cost=None,
                    cost_unit=None,
                    expected_regime='exact',
                    applies_config={'controlFunctional': weaker_name},
                )
            )
        chosen_fix = recommendations[0]
    else:
        recommendations.append(
            StructuralFixOption(
                fix_id='keep-current',
                title='Keep current history length',
                action_kind='keep',
                rationale='The current finite history already supports exact interpolation of the chosen protected functional.',
                theorem_status='family-specific threshold result with interpolation checks',
                minimal=True,
                cost=0.0,
                cost_unit='history steps',
                expected_regime='exact',
                applies_config={'controlHorizon': int(horizon)},
            )
        )

    if chosen_fix is not None:
        after_report = discover_diagonal_control_structure(
            profile=profile,
            functional_name=chosen_fix.applies_config.get('controlFunctional', functional_name),
            horizon=int(chosen_fix.applies_config.get('controlHorizon', horizon)),
        )
        before_gap = 0.0 if exact else 2.0
        after_gap = float(after_report.metrics['collision_gap'])
        comparison = StructuralComparison(
            before_regime=current_regime,
            after_regime=after_report.current_regime,
            regime_changed=current_regime != after_report.current_regime,
            key_metric_name='collision gap',
            key_metric_before=before_gap,
            key_metric_after=after_gap,
            exact_after=after_report.exact,
            impossible_after=after_report.impossible,
            narrative='The proposed history augmentation reaches the first exact interpolation horizon for the current protected functional.' if after_report.exact else 'The proposed control-side change does not restore exact static recovery.',
        )

    return StructuralDiscoveryReport(
        family='diagonal_control',
        title='Diagonal control structural discovery',
        protected_label=CONTROL_FUNCTIONAL_LABELS[functional_name],
        observation_label=f'{int(horizon)}-step scalar history on profile {profile}',
        current_regime=current_regime,
        exact=exact,
        asymptotic=False,
        impossible=impossible,
        theorem_status='family-specific threshold result with interpolation checks',
        protected_object='chosen protected functional on a diagonal control family',
        disturbance_description='unresolved hidden functional components under the current history length and sensor profile',
        current_failure_summary='The current history is too short for exact interpolation of the chosen protected functional.' if not exact else 'The current history already interpolates the protected functional exactly.',
        missing_structure='Add more history or weaken the target to a functional generated by the active moment family.' if not exact else 'No missing finite-history structure remains for the current target.',
        failure_modes=tuple(failure_modes),
        weaker_targets=weaker_targets,
        recommendations=tuple(recommendations),
        chosen_fix=chosen_fix,
        comparison=comparison,
        proof_links=(
            'docs/theory/advanced-directions/constrained-observation-results-report.md',
            'docs/theorem-candidates/pvrt-theorem-spine.md',
            'docs/control/worked-linear-example.md',
        ),
        limitations=(
            'diagonal scalar-output family only',
            'history threshold law is currently family-specific rather than a general observer theorem',
        ),
        metrics={
            'predicted_min_horizon': None if predicted_horizon is None else int(predicted_horizon),
            'current_horizon': int(horizon),
            'collision_gap': 0.0 if exact else 2.0,
            'interpolation_available': interpolation_weights is not None,
            'weaker_target_count': len(weaker_targets),
        },
    )


def discover_qubit_target_split(
    *,
    protected_key: str = 'bloch_vector',
    phase_window_deg: float = 30.0,
) -> StructuralDiscoveryReport:
    full_collision = qubit_phase_collision_formula(float(phase_window_deg))
    exact = protected_key == 'z_coordinate' or abs(float(phase_window_deg)) <= EPS
    impossible = not exact
    current_regime = _regime_label(exact=exact, asymptotic=False, impossible=impossible)
    weaker_targets = tuple(() if protected_key == 'z_coordinate' else ('z coordinate only',))
    recommendations: list[StructuralFixOption] = []
    failure_modes: list[str] = []
    chosen_fix = None
    comparison = None
    if not exact:
        failure_modes.append('phase freedom creates record fibers with different Bloch vectors and the same fixed-basis statistics')
        recommendations.append(
            StructuralFixOption(
                fix_id='weaken-z',
                title='Weaken target to z coordinate only',
                action_kind='weaken_target',
                rationale='Under the fixed-basis record, the z coordinate survives exactly even when the full Bloch vector does not.',
                theorem_status='proved family-specific no-go / weaker-target split',
                minimal=True,
                cost=None,
                cost_unit=None,
                expected_regime='exact',
                applies_config={'qubitProtected': 'z_coordinate'},
            )
        )
        recommendations.append(
            StructuralFixOption(
                fix_id='add-basis',
                title='Add a complementary measurement basis',
                action_kind='add_measurement',
                rationale='This is the standard physical way to recover phase-sensitive information, but the repo does not yet prove a theorem for the richer basis family.',
                theorem_status='standard heuristic outside the current theorem spine',
                minimal=False,
                cost=1.0,
                cost_unit='additional basis family',
                expected_regime='likely exact on the enlarged family',
                applies_config={'qubitProtected': 'bloch_vector', 'qubitExtraBasis': True},
            )
        )
        chosen_fix = recommendations[0]
        after_report = discover_qubit_target_split(protected_key='z_coordinate', phase_window_deg=phase_window_deg)
        comparison = StructuralComparison(
            before_regime=current_regime,
            after_regime=after_report.current_regime,
            regime_changed=current_regime != after_report.current_regime,
            key_metric_name='collision law',
            key_metric_before=full_collision,
            key_metric_after=float(after_report.metrics['collision_gap']),
            exact_after=after_report.exact,
            impossible_after=after_report.impossible,
            narrative='Weakening the target removes the phase-sensitive degrees of freedom that the fixed-basis record cannot resolve.',
        )
    else:
        recommendations.append(
            StructuralFixOption(
                fix_id='keep-current',
                title='Keep current target',
                action_kind='keep',
                rationale='The fixed-basis record already recovers the selected protected variable exactly on the current family.',
                theorem_status='proved family-specific split',
                minimal=True,
                cost=0.0,
                cost_unit='basis families',
                expected_regime='exact',
                applies_config={'qubitProtected': protected_key},
            )
        )

    return StructuralDiscoveryReport(
        family='qubit_fixed_basis',
        title='Qubit weaker-versus-stronger structural discovery',
        protected_label='full Bloch vector' if protected_key == 'bloch_vector' else 'z coordinate only',
        observation_label=f'fixed-basis record with phase window {float(phase_window_deg):.1f} degrees',
        current_regime=current_regime,
        exact=exact,
        asymptotic=False,
        impossible=impossible,
        theorem_status='family-specific split and no-go',
        protected_object='chosen qubit protected variable under a fixed-basis classical record',
        disturbance_description='phase-sensitive information lost under the fixed-basis measurement map',
        current_failure_summary='The current fixed-basis record collapses phase-sensitive Bloch information.' if not exact else 'The current fixed-basis record exactly preserves the selected weak protected variable.',
        missing_structure='Either add a complementary basis or weaken the target to the phase-insensitive z coordinate.' if not exact else 'No additional basis structure is needed for the current weak target.',
        failure_modes=tuple(failure_modes),
        weaker_targets=weaker_targets,
        recommendations=tuple(recommendations),
        chosen_fix=chosen_fix,
        comparison=comparison,
        proof_links=(
            'docs/theory/advanced-directions/constrained-observation-results-report.md',
            'docs/theorem-candidates/pvrt-theorem-spine.md',
            'docs/physics/continuous-quantum-error-correction.md',
        ),
        limitations=(
            'fixed-basis toy family only',
            'complementary-basis recommendation is standard physical guidance, not yet a repo theorem',
        ),
        metrics={
            'phase_window_deg': float(phase_window_deg),
            'collision_gap': 0.0 if exact else full_collision,
            'weaker_target_count': len(weaker_targets),
        },
    )


def discover_bounded_boundary_structure(
    *,
    architecture: str = 'periodic_transplant',
    protected_key: str = 'bounded_velocity_class',
    grid_size: int = 17,
) -> StructuralDiscoveryReport:
    transplant = bounded_domain_projection_counterexample(max(grid_size, 9))
    compatible = bounded_hodge_projection_report(n=max(grid_size, 17))
    strong_target = protected_key == 'bounded_velocity_class'
    exact = architecture == 'boundary_compatible_hodge' or (architecture == 'periodic_transplant' and not strong_target)
    impossible = architecture == 'periodic_transplant' and strong_target
    current_regime = _regime_label(exact=exact, asymptotic=False, impossible=impossible)
    recommendations: list[StructuralFixOption] = []
    failure_modes: list[str] = []
    weaker_targets = tuple(() if not strong_target else ('bulk divergence certificate only',))
    chosen_fix = None
    comparison = None

    if not exact:
        failure_modes.append('periodic projector transplant removes divergence but violates bounded boundary compatibility')
        recommendations.append(
            StructuralFixOption(
                fix_id='switch-compatible-hodge',
                title='Switch to boundary-compatible finite-mode Hodge projector',
                action_kind='switch_architecture',
                rationale='The periodic projector is the wrong architecture on this bounded family; the restricted boundary-compatible finite-mode Hodge projector restores exact recovery on its admissible family.',
                theorem_status='restricted exact bounded-domain theorem',
                minimal=True,
                cost=1.0,
                cost_unit='architecture switch',
                expected_regime='exact',
                applies_config={'boundaryArchitecture': 'boundary_compatible_hodge'},
            )
        )
        recommendations.append(
            StructuralFixOption(
                fix_id='weaken-divergence-certificate',
                title='Weaken target to bulk divergence certificate only',
                action_kind='weaken_target',
                rationale='If the application only needs a divergence certificate, the transplanted projector can still support that weaker target even though it fails the strong bounded protected class.',
                theorem_status='validated weaker-target fallback',
                minimal=False,
                cost=None,
                cost_unit=None,
                expected_regime='exact',
                applies_config={'boundaryProtected': 'divergence_certificate'},
            )
        )
        chosen_fix = recommendations[0]
        after_report = discover_bounded_boundary_structure(
            architecture='boundary_compatible_hodge',
            protected_key=protected_key,
            grid_size=grid_size,
        )
        comparison = StructuralComparison(
            before_regime=current_regime,
            after_regime=after_report.current_regime,
            regime_changed=current_regime != after_report.current_regime,
            key_metric_name='boundary mismatch',
            key_metric_before=float(transplant.projected_boundary_normal_rms),
            key_metric_after=float(after_report.metrics['recovery_error']),
            exact_after=after_report.exact,
            impossible_after=after_report.impossible,
            narrative='Switching to the boundary-compatible finite-mode Hodge family repairs the architectural mismatch instead of pretending the periodic projector already solved the bounded problem.',
        )
    else:
        recommendations.append(
            StructuralFixOption(
                fix_id='keep-current',
                title='Keep current bounded-domain architecture',
                action_kind='keep',
                rationale='The current bounded-domain setup already matches the selected protected target.',
                theorem_status='restricted exact bounded-domain theorem' if architecture == 'boundary_compatible_hodge' else 'validated weaker-target fallback',
                minimal=True,
                cost=0.0,
                cost_unit='architecture switches',
                expected_regime='exact',
                applies_config={'boundaryArchitecture': architecture, 'boundaryProtected': protected_key},
            )
        )

    return StructuralDiscoveryReport(
        family='bounded_boundary_architecture',
        title='Bounded-domain structural discovery',
        protected_label=BOUNDARY_PROTECTED_LABELS[protected_key],
        observation_label='boundary-compatible finite-mode Hodge projector' if architecture == 'boundary_compatible_hodge' else 'periodic projector transplanted to a bounded domain',
        current_regime=current_regime,
        exact=exact,
        asymptotic=False,
        impossible=impossible,
        theorem_status='restricted exact bounded-domain theorem plus explicit transplant failure',
        protected_object='bounded divergence-free protected class with boundary compatibility requirements',
        disturbance_description='divergence contamination and architecture-induced boundary mismatch',
        current_failure_summary='The transplanted periodic projector still leaves the bounded protected class because the boundary-normal trace is wrong.' if not exact else 'The current bounded-domain architecture supports the selected target exactly.',
        missing_structure='Switch to a boundary-compatible projector family or weaken the target to what the current architecture actually certifies.' if not exact else 'No additional bounded-domain structure is needed for the current target.',
        failure_modes=tuple(failure_modes),
        weaker_targets=weaker_targets,
        recommendations=tuple(recommendations),
        chosen_fix=chosen_fix,
        comparison=comparison,
        proof_links=(
            'docs/theorem-candidates/bounded-domain-hodge-theorems.md',
            'docs/cfd/bounded-vs-periodic-projection.md',
            'docs/app/structural-discovery-studio.md',
        ),
        limitations=(
            'restricted finite-mode bounded family only',
            'the positive exact statement does not justify arbitrary bounded-domain projector transplants',
        ),
        metrics={
            'transplant_before_divergence': float(transplant.before_l2_divergence),
            'transplant_after_divergence': float(transplant.after_periodic_projection_l2_divergence),
            'transplant_boundary_mismatch': float(transplant.projected_boundary_normal_rms),
            'compatible_recovered_divergence': float(compatible.recovered_divergence_rms),
            'compatible_boundary_normal_rms': float(compatible.recovered_boundary_normal_rms),
            'recovery_error': float(compatible.recovery_l2_error),
            'idempotence_error': float(compatible.idempotence_l2_error),
        },
    )


def structural_discovery_demo_reports() -> dict[str, Any]:
    periodic = discover_periodic_modal_structure(protected_key='full_weighted_sum', observation='cutoff_vorticity', cutoff=3)
    control = discover_diagonal_control_structure(profile='three_active', functional_name='second_moment', horizon=2)
    qubit = discover_qubit_target_split(protected_key='bloch_vector', phase_window_deg=30.0)
    linear = discover_linear_template_structure(template_name='sensor_basis', protected_key='x3', measurement_ids=('measure_x1', 'measure_x2_plus_x3'))
    boundary = discover_bounded_boundary_structure(architecture='periodic_transplant', protected_key='bounded_velocity_class', grid_size=17)

    demos = {
        'periodic_modal_repair': periodic.to_dict(),
        'control_history_repair': control.to_dict(),
        'weaker_vs_stronger_split': qubit.to_dict(),
        'boundary_architecture_repair': boundary.to_dict(),
        'restricted_linear_measurement_repair': linear.to_dict(),
    }
    return {
        'summary': {
            'demo_count': len(demos),
            'exact_after_count': int(sum(1 for report in demos.values() if report['comparison'] and report['comparison']['exact_after'])),
            'families': list(demos.keys()),
        },
        'demos': demos,
    }
