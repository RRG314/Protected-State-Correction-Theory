from __future__ import annotations

from ocp.structural_discovery import (
    discover_bounded_boundary_structure,
    discover_diagonal_control_structure,
    discover_linear_template_structure,
    discover_periodic_modal_structure,
    discover_qubit_target_split,
    structural_discovery_demo_reports,
)


def test_structural_discovery_periodic_demo_detects_missing_support_and_repairs_it() -> None:
    report = discover_periodic_modal_structure(
        protected_key='full_weighted_sum',
        observation='cutoff_vorticity',
        cutoff=3,
    )
    assert report.current_regime == 'impossible'
    assert 'retained cutoff misses part of the protected modal support' in report.failure_modes
    assert report.chosen_fix is not None
    assert report.chosen_fix.action_kind == 'add_mode'
    assert report.chosen_fix.applies_config['periodicCutoff'] == 4
    assert report.comparison is not None
    assert report.comparison.after_regime == 'exact'
    assert report.comparison.regime_changed is True
    assert report.metrics['predicted_min_cutoff'] == 4


def test_structural_discovery_control_demo_detects_history_insufficiency_and_repairs_it() -> None:
    report = discover_diagonal_control_structure(
        profile='three_active',
        functional_name='second_moment',
        horizon=2,
    )
    assert report.current_regime == 'impossible'
    assert 'finite observation horizon is too short to interpolate the protected functional' in report.failure_modes
    assert report.chosen_fix is not None
    assert report.chosen_fix.action_kind == 'add_history'
    assert report.chosen_fix.applies_config['controlHorizon'] == 3
    assert report.comparison is not None
    assert report.comparison.after_regime == 'exact'
    assert report.metrics['predicted_min_horizon'] == 3


def test_structural_discovery_qubit_demo_distinguishes_stronger_and_weaker_targets() -> None:
    report = discover_qubit_target_split(protected_key='bloch_vector', phase_window_deg=30.0)
    assert report.current_regime == 'impossible'
    assert report.weaker_targets == ('z coordinate only',)
    assert report.chosen_fix is not None
    assert report.chosen_fix.action_kind == 'weaken_target'
    assert report.chosen_fix.applies_config['qubitProtected'] == 'z_coordinate'
    assert report.comparison is not None
    assert report.comparison.after_regime == 'exact'
    assert report.recommendations[1].theorem_status == 'standard heuristic outside the current theorem spine'


def test_structural_discovery_linear_demo_finds_candidate_library_fix() -> None:
    report = discover_linear_template_structure(
        template_name='sensor_basis',
        protected_key='x3',
        measurement_ids=('measure_x1', 'measure_x2_plus_x3'),
    )
    assert report.current_regime == 'impossible'
    assert report.metrics['candidate_minimal_added_measurements'] == 1
    assert report.chosen_fix is not None
    assert report.chosen_fix.action_kind == 'add_measurement'
    assert report.comparison is not None
    assert report.comparison.after_regime == 'exact'
    assert 'nullspace witness changes the protected target while leaving the record fixed' in report.failure_modes


def test_structural_discovery_boundary_demo_detects_architecture_mismatch_and_repairs_it() -> None:
    report = discover_bounded_boundary_structure(
        architecture='periodic_transplant',
        protected_key='bounded_velocity_class',
        grid_size=17,
    )
    assert report.current_regime == 'impossible'
    assert 'periodic projector transplant removes divergence but violates bounded boundary compatibility' in report.failure_modes
    assert report.chosen_fix is not None
    assert report.chosen_fix.action_kind == 'switch_architecture'
    assert report.chosen_fix.applies_config['boundaryArchitecture'] == 'boundary_compatible_hodge'
    assert report.comparison is not None
    assert report.comparison.after_regime == 'exact'
    assert report.metrics['transplant_boundary_mismatch'] > 1e-2
    assert report.metrics['recovery_error'] < 1e-8


def test_structural_discovery_demo_bundle_contains_four_reproducible_regime_changes() -> None:
    bundle = structural_discovery_demo_reports()
    assert bundle['summary']['demo_count'] == 5
    assert bundle['summary']['exact_after_count'] == 5
    assert set(bundle['demos']) == {
        'periodic_modal_repair',
        'control_history_repair',
        'weaker_vs_stronger_split',
        'boundary_architecture_repair',
        'restricted_linear_measurement_repair',
    }
