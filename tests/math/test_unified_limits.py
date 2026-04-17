from __future__ import annotations

import numpy as np

from ocp.fiber_limits import (
    canonical_model_mismatch_report,
    candidate_library_budget_report,
    canonical_detectable_only_examples,
    control_regime_hierarchy_report,
    coordinate_rank_enumeration_report,
    finite_target_hierarchy_report,
    noisy_restricted_linear_target_hierarchy_report,
    periodic_modal_refinement_report,
    rank_only_classifier_failure_report,
    restricted_linear_family_enlargement_report,
    restricted_linear_fiber_geometry_report,
    restricted_linear_model_mismatch_report,
    restricted_linear_target_hierarchy_report,
)


def test_finite_target_hierarchy_detects_detectable_only_split() -> None:
    report = finite_target_hierarchy_report(
        observations=[np.array([0.0]), np.array([1.0]), np.array([1.0])],
        weak_protected_values=[np.array([0.0]), np.array([1.0]), np.array([1.0])],
        strong_protected_values=[np.array([0.0]), np.array([1.0]), np.array([2.0])],
        deltas=(0.0, 0.5, 1.0),
    )
    assert report.strong_exact_recoverable is False
    assert report.weak_exact_recoverable is True
    assert report.detectable_only is True
    assert report.strong_collision_gap > 0.5
    assert report.weak_collision_gap < 1e-10
    assert report.strong_witness_pair is not None
    assert report.weak_witness_pair is None


def test_restricted_linear_target_hierarchy_keeps_weaker_target_only() -> None:
    observation = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ],
        dtype=float,
    )
    weak = np.array([[0.0, 1.0, 1.0]], dtype=float)
    strong = np.array([[0.0, 0.0, 1.0]], dtype=float)
    report = restricted_linear_target_hierarchy_report(observation, weak, strong)
    assert report.weak_exact_recoverable is True
    assert report.strong_exact_recoverable is False
    assert report.detectable_only is True
    assert report.weak_rowspace_residual < 1e-10
    assert report.weak_collision_gap < 1e-10
    assert report.strong_rowspace_residual > 0.1
    assert report.strong_collision_gap > 0.5


def test_rank_only_classifier_failure_report_sweeps_small_dimensions() -> None:
    report = rank_only_classifier_failure_report((3, 4, 5))
    assert report.witness_count == 19
    assert report.all_same_rank is True
    assert report.all_opposite_verdicts is True
    for row in report.rows:
        assert row.exact_rank_observation == row.fail_rank_observation == row.observation_rank
        assert row.exact_recoverable is True
        assert row.fail_recoverable is False
        assert row.exact_rowspace_residual < 1e-10
        assert row.fail_rowspace_residual > 0.1
        assert row.exact_collision_gap < 1e-10
        assert row.fail_collision_gap > 0.1


def test_coordinate_enumeration_independently_finds_exact_and_fail_cases() -> None:
    report = coordinate_rank_enumeration_report((3, 4, 5))
    assert report.all_levels_have_exact_and_fail is True
    for row in report.rows:
        assert row.exact_count > 0
        assert row.fail_count > 0


def test_candidate_library_budget_report_finds_same_budget_opposite_verdicts() -> None:
    report = candidate_library_budget_report((3, 4, 5))
    assert report.witness_count == 19
    assert report.all_levels_have_exact_and_fail is True
    for row in report.rows:
        assert row.exact_count > 0
        assert row.fail_count > 0
        assert len(row.exact_subset) == row.selection_size
        assert len(row.fail_subset) == row.selection_size
        assert row.exact_total_cost == row.fail_total_cost == float(row.selection_size)
        assert row.exact_subset != row.fail_subset


def test_noisy_restricted_linear_target_hierarchy_keeps_quantitative_separation() -> None:
    observation = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ],
        dtype=float,
    )
    weak = np.array([[0.0, 1.0, 1.0]], dtype=float)
    strong = np.array([[0.0, 0.0, 1.0]], dtype=float)
    report = noisy_restricted_linear_target_hierarchy_report(
        observation,
        weak,
        strong,
        noise_radii=(0.0, 0.25, 0.5, 1.0),
    )
    assert report.weak_exact_recoverable is True
    assert report.strong_exact_recoverable is False
    assert report.detectable_only is True
    assert report.weak_decoder_operator_norm > 0.9
    assert report.strong_collision_gap > 1.9
    assert report.strong_uniform_lower_bound > 0.9
    assert report.weak_discrete_collision_gap < 1e-10
    assert report.strong_discrete_collision_gap > 1.9
    assert report.separation_noise_threshold is not None
    rows = {row.noise_radius: row for row in report.rows}
    assert rows[0.0].weak_upper_bound < 1e-10
    assert rows[0.0].weak_bruteforce_max_error < 1e-10
    assert rows[0.25].weak_bruteforce_max_error <= rows[0.25].weak_upper_bound + 1e-10
    assert rows[0.5].separated is True
    assert rows[1.0].strong_uniform_lower_bound == report.strong_uniform_lower_bound


def test_control_regime_hierarchy_report_keeps_exact_vs_asymptotic_split() -> None:
    report = control_regime_hierarchy_report(0.2)
    assert report.one_step_exact_recoverable is False
    assert report.two_step_exact_recoverable is True
    assert report.observer_asymptotic_recoverable is True
    assert report.one_step_collision_gap > 0.1
    assert report.two_step_collision_gap < 1e-10
    assert report.observer_spectral_radius < 1.0
    assert report.observer_final_protected_error < 0.1


def test_restricted_linear_fiber_geometry_report_tracks_mixed_vs_constant_fibers() -> None:
    exact = restricted_linear_fiber_geometry_report(
        np.array(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 1.0],
            ],
            dtype=float,
        ),
        np.array([[0.0, 1.0, 1.0]], dtype=float),
    )
    fail = restricted_linear_fiber_geometry_report(
        np.array(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 1.0],
            ],
            dtype=float,
        ),
        np.array([[0.0, 0.0, 1.0]], dtype=float),
    )
    assert exact.coefficient_dimension == 3
    assert exact.observation_rank == 2
    assert exact.fiber_dimension == 1
    assert exact.exact_recoverable is True
    assert exact.target_mixed_fiber is False
    assert exact.rowspace_residual < 1e-10
    assert exact.collision_gap < 1e-10
    assert fail.fiber_dimension == 1
    assert fail.exact_recoverable is False
    assert fail.target_mixed_fiber is True
    assert fail.rowspace_residual > 0.1
    assert fail.collision_gap > 1.9


def test_restricted_linear_family_enlargement_report_catches_false_positive_risk() -> None:
    report = restricted_linear_family_enlargement_report(
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
    assert report.inclusion_residual < 1e-10
    assert report.small_exact_recoverable is True
    assert report.large_exact_recoverable is False
    assert report.false_positive_risk is True
    assert report.small_rowspace_residual < 1e-10
    assert report.large_rowspace_residual > 0.1
    assert report.small_collision_gap < 1e-10
    assert report.large_collision_gap > 1.9
    assert report.larger_family_impossibility_lower_bound > 0.9
    assert report.reference_decoder_max_error_on_large_family is not None
    assert report.reference_decoder_max_error_on_large_family > 0.9


def test_restricted_linear_model_mismatch_report_detects_decoder_drift() -> None:
    report = restricted_linear_model_mismatch_report(
        np.array(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
            ],
            dtype=float,
        ),
        np.array([[0.0, 0.0, 1.0]], dtype=float),
        np.array(
            [
                [1.0, 0.0],
                [0.0, 1.0],
                [0.0, 1.0],
            ],
            dtype=float,
        ),
        {
            'beta=0.5': np.array(
                [
                    [1.0, 0.0],
                    [0.0, 1.0],
                    [0.0, 0.5],
                ],
                dtype=float,
            ),
            'beta=1.0': np.array(
                [
                    [1.0, 0.0],
                    [0.0, 1.0],
                    [0.0, 1.0],
                ],
                dtype=float,
            ),
            'beta=2.0': np.array(
                [
                    [1.0, 0.0],
                    [0.0, 1.0],
                    [0.0, 2.0],
                ],
                dtype=float,
            ),
        },
    )
    assert report.reference_exact_recoverable is True
    assert report.reference_decoder_operator_norm is not None
    rows = {row.label: row for row in report.rows}
    assert rows['beta=1.0'].exact_recoverable_under_true_family is True
    assert rows['beta=1.0'].reference_decoder_max_error is not None
    assert rows['beta=1.0'].reference_decoder_max_error < 1e-10
    assert rows['beta=0.5'].reference_decoder_max_error is not None
    assert rows['beta=0.5'].reference_decoder_max_error > 0.44
    assert rows['beta=2.0'].reference_decoder_max_error is not None
    assert rows['beta=2.0'].reference_decoder_max_error > 0.44
    assert rows['beta=0.5'].subspace_distance > 0.1
    assert rows['beta=2.0'].subspace_distance > 0.1


def test_periodic_modal_refinement_report_catches_discretization_false_positive() -> None:
    report = periodic_modal_refinement_report()
    assert report.coarse_exact_recoverable is True
    assert report.refined_exact_recoverable is False
    assert report.refinement_false_positive_risk is True
    assert report.coarse_collision_gap < 1e-10
    assert report.refined_collision_gap > 0.1
    assert report.refined_family_impossibility_lower_bound > 0.05
    assert report.coarse_decoder_max_error_on_refined_family is not None
    assert report.coarse_decoder_max_error_on_refined_family > 0.1


def test_canonical_model_mismatch_report_matches_exact_formula() -> None:
    report = canonical_model_mismatch_report(1.0, beta_values=(0.5, 1.0, 2.0))
    assert report.reference_exact_recoverable is True
    assert report.reference_decoder_operator_norm is not None
    rows = {row.beta_true: row for row in report.rows}
    assert rows[1.0].exact_recoverable_true_family is True
    assert rows[1.0].formula_max_error < 1e-10
    assert rows[1.0].brute_force_max_error < 1e-10
    assert np.isclose(rows[0.5].formula_max_error, rows[0.5].brute_force_max_error)
    assert np.isclose(rows[2.0].formula_max_error, rows[2.0].brute_force_max_error)
    assert rows[0.5].formula_max_error > 0.44
    assert rows[2.0].formula_max_error > 0.44


def test_canonical_detectable_only_examples_match_expected_status() -> None:
    examples = canonical_detectable_only_examples()
    finite = examples['finite']
    restricted_linear = examples['restricted_linear']
    noisy = examples['noisy_restricted_linear']
    control = examples['control']
    assert finite.detectable_only is True
    assert finite.strong_exact_recoverable is False
    assert finite.weak_exact_recoverable is True
    assert restricted_linear.detectable_only is True
    assert restricted_linear.strong_exact_recoverable is False
    assert restricted_linear.weak_exact_recoverable is True
    assert noisy.detectable_only is True
    assert noisy.strong_uniform_lower_bound > 0.9
    assert noisy.rows[1].weak_bruteforce_max_error <= noisy.rows[1].weak_upper_bound + 1e-10
    assert control.one_step_exact_recoverable is False
    assert control.two_step_exact_recoverable is True
