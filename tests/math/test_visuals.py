from __future__ import annotations

import numpy as np

from ocp.visuals import (
    alignment_landscape_data,
    augmentation_direction_scan_data,
    contamination_sweep_visual_data,
    core_geometry_data,
    cross_system_status_data,
    dynamic_rate_visual_data,
    family_enlargement_visual_data,
    fiber_toy_data,
    minimal_augmentation_data,
    periodic_vs_bounded_data,
    perturbation_fragility_data,
    recoverability_transition_data,
    same_rank_data,
    threshold_surfaces_data,
)


def test_core_geometry_exact_and_failure_cases_are_correct() -> None:
    data = core_geometry_data()
    exact = data['exact_2d']
    fail = data['misaligned_2d']
    overlap = data['overlap_3d']

    assert exact['projection_error_norm'] < 1e-12
    assert fail['projection_error_norm'] > 1e-3
    assert overlap['intersection_dimension'] == 1
    assert overlap['same_state_residual_norm'] < 1e-12


def test_fiber_toy_constancy_theorem_visual_data_is_correct() -> None:
    data = fiber_toy_data()
    const_checks = data['fiber_constancy_tau_constant']
    nonconst_checks = data['fiber_constancy_tau_nonconstant']

    assert all(const_checks)
    assert not all(nonconst_checks)
    assert any(not value for value in nonconst_checks)


def test_transition_data_has_exact_to_impossible_threshold() -> None:
    data = recoverability_transition_data(alphas=(1.0, 0.5, 0.25, 0.0))
    rows = data['rows']

    assert rows[0]['exact_recoverable'] is True
    assert rows[-1]['exact_recoverable'] is False
    assert data['exact_to_impossible_threshold_alpha'] == 0.0
    assert rows[-1]['fiber_count'] < rows[0]['fiber_count']


def test_same_rank_visual_data_preserves_opposite_verdict_witness() -> None:
    data = same_rank_data()

    assert data['rank_exact'] == data['rank_fail']
    assert data['exact_recoverable'] is True
    assert data['fail_recoverable'] is False
    assert data['exact_rowspace_residual'] < 1e-12
    assert data['fail_rowspace_residual'] > 1e-6


def test_minimal_augmentation_formula_and_repair_are_correct() -> None:
    data = minimal_augmentation_data()

    assert data['delta_formula'] == data['design_unrestricted_minimal_added_measurements']
    assert data['delta_formula'] == 1
    assert data['exact_before'] is False
    assert data['exact_after'] is True
    assert data['residual_after'] < data['residual_before']


def test_periodic_vs_bounded_visual_data_matches_branch_split() -> None:
    data = periodic_vs_bounded_data(n_periodic=24, n_bounded=16, contamination=0.2)
    periodic = data['periodic']
    bounded = data['bounded_transplant']
    canonical = data['canonical_summary']

    assert periodic['after_l2_divergence'] < periodic['before_l2_divergence']
    assert periodic['recovery_l2_error'] < 1e-6
    assert bounded['after_l2_divergence'] < bounded['before_l2_divergence']
    assert bounded['boundary_normal_projected_rms'] > bounded['boundary_normal_physical_rms']
    assert canonical['bounded_transplant_projected_boundary_normal_rms'] > 1e-3
    assert canonical['bounded_hodge_recovered_boundary_normal_rms'] < 1e-6


def test_threshold_surfaces_cover_exact_approx_asymptotic_impossible() -> None:
    data = threshold_surfaces_data()
    control = np.asarray(data['control_surface']['regime_matrix'], dtype=int)
    noise = np.asarray(data['noise_surface']['regime_matrix'], dtype=int)
    all_ids = set(np.unique(np.concatenate([control.ravel(), noise.ravel()])))

    assert {0, 1, 2, 3}.issubset(all_ids)


def test_cross_system_map_has_required_status_classes() -> None:
    data = cross_system_status_data()
    statuses = {row['status'] for row in data['systems']}

    assert 'exact_anchor' in statuses
    assert 'asymptotic_only' in statuses
    assert 'no_go_boundary' in statuses
    assert 'branch_limited_theory' in statuses


def test_alignment_landscape_confirms_rank_is_insufficient() -> None:
    data = alignment_landscape_data(theta_count=41, phi_count=61)
    residual = np.asarray(data['rowspace_residual_matrix'], dtype=float)
    exact = np.asarray(data['exact_mask_matrix'], dtype=int)
    gap = np.asarray(data['collision_gap_matrix'], dtype=float)

    assert residual.min() <= 1e-10
    assert residual.max() > 0.1
    assert np.any(exact == 1)
    assert np.any(exact == 0)
    assert gap.max() > 0.1


def test_perturbation_fragility_is_exact_only_at_center() -> None:
    data = perturbation_fragility_data(perturb_values=np.linspace(-0.5, 0.5, 41))
    residual = np.asarray(data['rowspace_residual_matrix'], dtype=float)
    exact = np.asarray(data['exact_mask_matrix'], dtype=int)
    center = int(data['center_index'])

    assert exact[center, center] == 1
    assert int(np.sum(exact)) == 1
    assert residual[center, center] <= 1e-10
    assert residual.max() > residual[center, center] + 1e-2


def test_family_enlargement_witness_preserves_false_positive_pattern() -> None:
    data = family_enlargement_visual_data()
    small = data['small_family']
    large = data['enlarged_family']

    assert small['exact_recoverable'] is True
    assert large['exact_recoverable'] is False
    assert small['collision_gap'] <= 1e-10
    assert large['collision_gap'] > 0.1
    assert all(len(values) == 1 for values in small['fiber_target_sets'])
    assert any(len(values) > 1 for values in large['fiber_target_sets'])


def test_dynamic_rate_data_has_stable_observer_and_history_split() -> None:
    data = dynamic_rate_visual_data()
    exact = np.asarray(data['exact_matrix'], dtype=int)
    observers = data['observer_reports']

    assert np.any(exact == 1)
    assert np.any(exact == 0)
    assert observers
    for row in observers:
        assert float(row['spectral_radius']) < 1.0
        errors = np.asarray(row['protected_error_history'], dtype=float)
        assert errors[-1] < errors[0]


def test_augmentation_direction_scan_shows_direction_sensitive_repair() -> None:
    data = augmentation_direction_scan_data()
    exact = np.asarray(data['exact_flags'], dtype=int)
    residual = np.asarray(data['rowspace_residuals'], dtype=float)

    assert np.any(exact == 1)
    assert np.any(exact == 0)
    assert len(data['fail_indices']) >= 2
    assert residual.min() <= 1e-10
    assert residual.max() > 0.1


def test_contamination_sweep_preserves_periodic_vs_bounded_split() -> None:
    data = contamination_sweep_visual_data(contamination_values=(0.05, 0.1, 0.2, 0.4))
    rows = data['rows']

    assert rows
    for row in rows:
        assert row['periodic_after_l2_divergence'] < row['periodic_before_l2_divergence']
        assert row['periodic_recovery_l2_error'] < 1e-5
        assert row['bounded_boundary_normal_projected_rms'] > row['bounded_boundary_normal_physical_rms']
        assert row['bounded_boundary_normal_projected_rms'] > row['bounded_hodge_recovered_boundary_normal_rms']
