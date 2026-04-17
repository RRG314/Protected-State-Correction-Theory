from __future__ import annotations

"""Decision-layer helpers built on top of the recoverability / impossibility branch.

This module is intentionally modest. It does not introduce a new theory branch.
Instead it exposes theorem-linked or validated-family decision corollaries for
supported families:

- continue an exact attempt,
- stop exact pursuit as impossible,
- switch to a weaker target,
- augment the record,
- change architecture,
- stop promoting a fragile exactness claim,
- stop trusting a mismatched inverse map.

The point is practical and falsification-first: turn existing exact/no-go results
into explicit stop/switch/augment guidance without pretending those decisions are
universal theorems in their own right.
"""

from dataclasses import dataclass

import numpy as np

from .cfd import cfd_projection_summary
from .design import linear_recoverability_design_report
from .fiber_limits import (
    EPS,
    canonical_model_mismatch_report,
    control_regime_hierarchy_report,
    restricted_linear_family_enlargement_report,
)
from .recoverability import periodic_functional_complexity_sweep, qubit_record_collapse_sweep


@dataclass(frozen=True)
class DecisionRecommendation:
    action: str
    status: str
    supporting_claims: tuple[str, ...]
    rationale: str


@dataclass(frozen=True)
class DecisionExampleRow:
    family: str
    scenario: str
    action: str
    status: str
    supporting_claims: tuple[str, ...]
    current_regime: str
    rationale: str
    notes: str
    adds_value_beyond_regime: bool


@dataclass(frozen=True)
class DecisionLayerReport:
    rows: tuple[DecisionExampleRow, ...]
    recommended_scope: str
    belongs_in_branch: bool
    deserves_new_branch: bool
    strongest_value: str
    strongest_failure: str


def impossibility_implies_stop(
    collision_gap: float,
    *,
    supporting_claims: tuple[str, ...] = ('OCP-030',),
    tol: float = EPS,
) -> DecisionRecommendation:
    gap = float(collision_gap)
    if gap <= tol:
        raise ValueError('impossibility_implies_stop requires a strictly positive collision gap')
    return DecisionRecommendation(
        action='stop_exact_recovery_attempt',
        status='PROVED',
        supporting_claims=supporting_claims,
        rationale='The current record fibers still mix distinct target values, so exact pursuit should stop rather than pretend the target is uniquely determined.',
    )


def weaker_target_switch_decision(
    *,
    strong_exact_recoverable: bool,
    weak_exact_recoverable: bool,
    supporting_claims: tuple[str, ...] = ('OCP-048', 'OCP-051'),
) -> DecisionRecommendation:
    if strong_exact_recoverable or not weak_exact_recoverable:
        raise ValueError('weaker_target_switch_decision requires strong failure together with weak exact recovery')
    return DecisionRecommendation(
        action='switch_to_weaker_target',
        status='PROVED',
        supporting_claims=supporting_claims,
        rationale='The same record fails the stronger target but exactly determines a coarsened target, so switching target is structurally justified.',
    )


def augmentation_vs_stop_decision(
    *,
    exact_recoverable: bool,
    minimal_added_measurements: int | None,
    budget: int | None,
    supporting_claims: tuple[str, ...] = ('OCP-045', 'OCP-047'),
) -> DecisionRecommendation:
    if exact_recoverable:
        return DecisionRecommendation(
            action='continue_exact_recovery_attempt',
            status='PROVED',
            supporting_claims=supporting_claims,
            rationale='The current record already spans the protected target on the supported family.',
        )
    if minimal_added_measurements is None:
        return DecisionRecommendation(
            action='stop_exact_recovery_attempt',
            status='PROVED',
            supporting_claims=supporting_claims,
            rationale='No supported exact augmentation is currently available, so exact pursuit should stop rather than fabricate a repair.',
        )
    if budget is not None and int(budget) >= int(minimal_added_measurements):
        return DecisionRecommendation(
            action='add_measurements_or_history',
            status='CONDITIONAL',
            supporting_claims=supporting_claims,
            rationale='Exact recovery is blocked now, but the supported family admits a finite minimal augmentation; augment if the available budget meets that exact count.',
        )
    return DecisionRecommendation(
        action='stop_exact_recovery_attempt',
        status='CONDITIONAL',
        supporting_claims=supporting_claims,
        rationale='Exact recovery remains blocked and the available budget is below the supported minimal augmentation count, so exact pursuit should stop unless the budget changes.',
    )


def architecture_change_decision(
    *,
    exact_alternative_available: bool = False,
    asymptotic_alternative_available: bool = False,
    status: str,
    supporting_claims: tuple[str, ...],
    exact_rationale: str,
    asymptotic_rationale: str,
) -> DecisionRecommendation:
    if exact_alternative_available:
        return DecisionRecommendation(
            action='change_architecture',
            status=status,
            supporting_claims=supporting_claims,
            rationale=exact_rationale,
        )
    if asymptotic_alternative_available:
        return DecisionRecommendation(
            action='change_architecture',
            status=status,
            supporting_claims=supporting_claims,
            rationale=asymptotic_rationale,
        )
    raise ValueError('architecture_change_decision requires an exact or asymptotic alternative')


def family_fragility_stop_condition(
    *,
    false_positive_risk: bool,
    supporting_claims: tuple[str, ...] = ('OCP-052',),
) -> DecisionRecommendation:
    if not false_positive_risk:
        return DecisionRecommendation(
            action='continue_exact_recovery_attempt',
            status='PROVED',
            supporting_claims=supporting_claims,
            rationale='No supported family-enlargement witness currently breaks the exact result.',
        )
    return DecisionRecommendation(
        action='stop_promoting_exactness_claim',
        status='PROVED',
        supporting_claims=supporting_claims,
        rationale='Exactness on the narrow family breaks immediately under honest enlargement, so the current positive result should not be promoted without a stronger family-robust proof.',
    )


def model_mismatch_stop_condition(
    *,
    max_error: float,
    tolerated_error: float,
    supporting_claims: tuple[str, ...] = ('OCP-053',),
    tol: float = EPS,
) -> DecisionRecommendation:
    error = float(max_error)
    tolerance = float(tolerated_error)
    if error <= tolerance + tol:
        return DecisionRecommendation(
            action='continue_exact_recovery_attempt',
            status='CONDITIONAL',
            supporting_claims=supporting_claims,
            rationale='The current mismatch witness stays below the tolerated error budget, so no stop decision is forced by this criterion alone.',
        )
    return DecisionRecommendation(
        action='stop_trusting_mismatched_inverse_map',
        status='CONDITIONAL',
        supporting_claims=supporting_claims,
        rationale='The mismatched decoder error exceeds the tolerated budget even with exact data, so the apparent success should be rejected until the family model is revalidated.',
    )


def decision_layer_example_report(
    *,
    linear_budget: int = 1,
    linear_stop_budget: int = 0,
    mismatch_tolerance: float = 0.25,
) -> DecisionLayerReport:
    rows: list[DecisionExampleRow] = []

    linear_design = linear_recoverability_design_report(
        np.array(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 1.0],
            ],
            dtype=float,
        ),
        np.array([[0.0, 0.0, 1.0]], dtype=float),
        candidate_rows=(
            np.array([0.0, 1.0, 0.0], dtype=float),
            np.array([0.0, 0.0, 1.0], dtype=float),
        ),
    )
    augment = augmentation_vs_stop_decision(
        exact_recoverable=linear_design.exact_recoverable,
        minimal_added_measurements=linear_design.minimal_added_measurements,
        budget=linear_budget,
    )
    rows.append(
        DecisionExampleRow(
            family='restricted_linear',
            scenario='exact target blocked but one-row repair exists',
            action=augment.action,
            status=augment.status,
            supporting_claims=augment.supporting_claims,
            current_regime='exact target not identifiable on the current record',
            rationale=augment.rationale,
            notes=f'minimal augmentation count = {linear_design.minimal_added_measurements}; available budget = {linear_budget}',
            adds_value_beyond_regime=True,
        )
    )
    stop_after_budget = augmentation_vs_stop_decision(
        exact_recoverable=linear_design.exact_recoverable,
        minimal_added_measurements=linear_design.minimal_added_measurements,
        budget=linear_stop_budget,
    )
    rows.append(
        DecisionExampleRow(
            family='restricted_linear',
            scenario='same exact blocker but budget is too small',
            action=stop_after_budget.action,
            status=stop_after_budget.status,
            supporting_claims=stop_after_budget.supporting_claims,
            current_regime='exact target not identifiable on the current record',
            rationale=stop_after_budget.rationale,
            notes=f'minimal augmentation count = {linear_design.minimal_added_measurements}; available budget = {linear_stop_budget}',
            adds_value_beyond_regime=True,
        )
    )

    qubit = qubit_record_collapse_sweep(
        phase_windows_deg=(30.0,),
        theta_samples=9,
        phase_samples=9,
        delta_count=10,
    )
    qubit_rows = {(row['protected_variable'], float(row['phase_window_deg'])): row for row in qubit['rows']}
    bloch = qubit_rows[('bloch_vector', 30.0)]
    z_only = qubit_rows[('z_coordinate', 30.0)]
    switch = weaker_target_switch_decision(
        strong_exact_recoverable=bool(bloch['exact_recoverable']),
        weak_exact_recoverable=bool(z_only['exact_recoverable']),
    )
    rows.append(
        DecisionExampleRow(
            family='qubit_phase_loss',
            scenario='phase-sensitive Bloch target fails but z target survives',
            action=switch.action,
            status=switch.status,
            supporting_claims=switch.supporting_claims,
            current_regime='strong target non-identifiable; weaker target exact',
            rationale=switch.rationale,
            notes=f"Bloch collision gap = {bloch['collision_max_protected_distance']:.4f}; z-coordinate gap = {z_only['collision_max_protected_distance']:.4f}",
            adds_value_beyond_regime=True,
        )
    )

    periodic = periodic_functional_complexity_sweep(
        n=14,
        cutoffs=(3, 4),
        delta_count=8,
    )
    periodic_rows = {
        (row['functional_name'], int(row['cutoff'])): row
        for row in periodic['rows']
    }
    full_weighted_sum = periodic_rows[('full_weighted_sum', 3)]
    periodic_decision = augmentation_vs_stop_decision(
        exact_recoverable=bool(full_weighted_sum['exact_recoverable']),
        minimal_added_measurements=int(full_weighted_sum['predicted_min_cutoff']) - int(full_weighted_sum['cutoff']),
        budget=int(full_weighted_sum['predicted_min_cutoff']) - int(full_weighted_sum['cutoff']),
        supporting_claims=('OCP-041',),
    )
    rows.append(
        DecisionExampleRow(
            family='periodic_modal',
            scenario='current cutoff misses the exact functional threshold',
            action=periodic_decision.action,
            status='VALIDATED',
            supporting_claims=('OCP-041',),
            current_regime='strong target not identifiable at current cutoff',
            rationale='The current cutoff leaves hidden protected modes; the natural decision is to refine the record to the first cutoff where the protected functional becomes exact.',
            notes=f"current cutoff = {full_weighted_sum['cutoff']}; predicted exact cutoff = {full_weighted_sum['predicted_min_cutoff']}",
            adds_value_beyond_regime=True,
        )
    )

    control = control_regime_hierarchy_report(0.2)
    control_history = augmentation_vs_stop_decision(
        exact_recoverable=control.one_step_exact_recoverable,
        minimal_added_measurements=1 if control.two_step_exact_recoverable else None,
        budget=1,
        supporting_claims=('OCP-042',),
    )
    rows.append(
        DecisionExampleRow(
            family='control_history',
            scenario='one-step history is insufficient but the next exact horizon is known',
            action=control_history.action,
            status='VALIDATED',
            supporting_claims=('OCP-042',),
            current_regime='finite-history target not identifiable at the current horizon',
            rationale='The current history is too short for exact recovery, but the supported control family has a known finite threshold, so adding history is the justified decision.',
            notes=f'one-step exact = {control.one_step_exact_recoverable}; two-step exact = {control.two_step_exact_recoverable}',
            adds_value_beyond_regime=True,
        )
    )
    observer_switch = architecture_change_decision(
        exact_alternative_available=False,
        asymptotic_alternative_available=control.observer_asymptotic_recoverable,
        status='VALIDATED',
        supporting_claims=('OCP-042', 'OCP-013'),
        exact_rationale='',
        asymptotic_rationale='Finite-history exact recovery is blocked at the current horizon, but the ongoing observer architecture still converges asymptotically on the supported benchmark.',
    )
    rows.append(
        DecisionExampleRow(
            family='control_history',
            scenario='finite-step exactness fails but observer recovery still converges',
            action=observer_switch.action,
            status=observer_switch.status,
            supporting_claims=observer_switch.supporting_claims,
            current_regime='finite-step exact impossible at current horizon, asymptotic observer viable',
            rationale=observer_switch.rationale,
            notes=f'observer spectral radius = {control.observer_spectral_radius:.4f}',
            adds_value_beyond_regime=True,
        )
    )

    cfd = cfd_projection_summary(n_periodic=18, n_bounded=24, contamination=0.2)
    boundary_switch = architecture_change_decision(
        exact_alternative_available=bool(cfd.bounded_hodge_exact.recovery_l2_error < 1e-8),
        asymptotic_alternative_available=False,
        status='PROVED',
        supporting_claims=('OCP-028', 'OCP-029'),
        exact_rationale='The transplanted bounded-domain projector fails the protected boundary class, but the boundary-compatible Hodge architecture restores exact recovery on the supported finite-mode family.',
        asymptotic_rationale='',
    )
    rows.append(
        DecisionExampleRow(
            family='bounded_domain_cfd',
            scenario='wrong projector architecture on the strong bounded target',
            action=boundary_switch.action,
            status=boundary_switch.status,
            supporting_claims=boundary_switch.supporting_claims,
            current_regime='wrong architecture; strong target not recovered',
            rationale=boundary_switch.rationale,
            notes=f"transplant boundary mismatch = {cfd.bounded_transplant.projected_boundary_normal_rms:.4e}; compatible recovery error = {cfd.bounded_hodge_exact.recovery_l2_error:.4e}",
            adds_value_beyond_regime=True,
        )
    )

    family_enlargement = restricted_linear_family_enlargement_report(
        np.array(
            [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
            ],
            dtype=float,
        ),
        np.array([[0.0, 1.0, 1.0, 0.0]], dtype=float),
        np.eye(4, dtype=float)[:, :2],
        np.eye(4, dtype=float)[:, :3],
        box_radius=1.0,
    )
    fragility = family_fragility_stop_condition(false_positive_risk=family_enlargement.false_positive_risk)
    rows.append(
        DecisionExampleRow(
            family='family_enlargement',
            scenario='exact result on the small family breaks immediately on enlargement',
            action=fragility.action,
            status=fragility.status,
            supporting_claims=fragility.supporting_claims,
            current_regime='exact on small family, impossible on enlarged family',
            rationale=fragility.rationale,
            notes=f'large-family lower bound = {family_enlargement.larger_family_impossibility_lower_bound:.4f}',
            adds_value_beyond_regime=True,
        )
    )

    canonical_mismatch = canonical_model_mismatch_report(1.0, beta_values=(0.5, 1.0, 2.0))
    mismatch_row = next(row for row in canonical_mismatch.rows if abs(row.beta_true - 2.0) <= EPS)
    mismatch = model_mismatch_stop_condition(
        max_error=mismatch_row.formula_max_error,
        tolerated_error=mismatch_tolerance,
    )
    rows.append(
        DecisionExampleRow(
            family='model_mismatch',
            scenario='decoder exact on the reference family but wrong on the true family',
            action=mismatch.action,
            status=mismatch.status,
            supporting_claims=mismatch.supporting_claims,
            current_regime='true family exactly identifiable but inverse map mismatched',
            rationale=mismatch.rationale,
            notes=f'tolerated error = {mismatch_tolerance:.3f}; witnessed mismatch error = {mismatch_row.formula_max_error:.4f}',
            adds_value_beyond_regime=True,
        )
    )

    return DecisionLayerReport(
        rows=tuple(rows),
        recommended_scope='integrate as a small theorem-linked decision layer inside the current branch',
        belongs_in_branch=True,
        deserves_new_branch=False,
        strongest_value='It converts exact/no-go/fragility results into explicit stop / switch / augment / architecture-change decisions on supported families and catches false-positive promotions.',
        strongest_failure='By itself it does not create a new universal theorem family; many candidate stopping laws collapse into corollaries of impossibility, augmentation, or fragility theorems already proved elsewhere in the branch.',
    )
