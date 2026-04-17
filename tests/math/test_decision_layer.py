from __future__ import annotations

from ocp.decision_layer import (
    augmentation_vs_stop_decision,
    decision_layer_example_report,
    family_fragility_stop_condition,
    impossibility_implies_stop,
    model_mismatch_stop_condition,
    weaker_target_switch_decision,
)


def test_impossibility_implies_stop_returns_stop_action() -> None:
    decision = impossibility_implies_stop(1.0)
    assert decision.action == 'stop_exact_recovery_attempt'
    assert decision.status == 'PROVED'
    assert 'OCP-030' in decision.supporting_claims


def test_weaker_target_switch_requires_strong_failure_and_weak_success() -> None:
    decision = weaker_target_switch_decision(
        strong_exact_recoverable=False,
        weak_exact_recoverable=True,
    )
    assert decision.action == 'switch_to_weaker_target'
    assert decision.status == 'PROVED'
    assert decision.supporting_claims == ('OCP-048', 'OCP-051')


def test_augmentation_vs_stop_tracks_budget() -> None:
    augment = augmentation_vs_stop_decision(
        exact_recoverable=False,
        minimal_added_measurements=1,
        budget=1,
    )
    stop = augmentation_vs_stop_decision(
        exact_recoverable=False,
        minimal_added_measurements=1,
        budget=0,
    )
    assert augment.action == 'add_measurements_or_history'
    assert augment.status == 'CONDITIONAL'
    assert stop.action == 'stop_exact_recovery_attempt'
    assert stop.status == 'CONDITIONAL'


def test_fragility_and_model_mismatch_conditions_become_stop_cautions() -> None:
    fragility = family_fragility_stop_condition(false_positive_risk=True)
    mismatch = model_mismatch_stop_condition(max_error=0.4472, tolerated_error=0.25)
    assert fragility.action == 'stop_promoting_exactness_claim'
    assert fragility.status == 'PROVED'
    assert mismatch.action == 'stop_trusting_mismatched_inverse_map'
    assert mismatch.status == 'CONDITIONAL'


def test_decision_layer_example_report_stays_small_and_branch_local() -> None:
    report = decision_layer_example_report()
    assert report.belongs_in_branch is True
    assert report.deserves_new_branch is False
    assert len(report.rows) >= 8
    family_actions = {(row.family, row.action) for row in report.rows}
    assert ('restricted_linear', 'add_measurements_or_history') in family_actions
    assert ('qubit_phase_loss', 'switch_to_weaker_target') in family_actions
    assert ('bounded_domain_cfd', 'change_architecture') in family_actions
    assert ('family_enlargement', 'stop_promoting_exactness_claim') in family_actions
    assert ('model_mismatch', 'stop_trusting_mismatched_inverse_map') in family_actions
