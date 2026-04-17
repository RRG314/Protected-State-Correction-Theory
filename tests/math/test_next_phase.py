from __future__ import annotations

import math

import numpy as np

from ocp.continuous import LinearOCPFlow
from ocp.next_phase import (
    canonical_rank_deficient_fragility_sweep,
    canonical_structure_classes,
    canonical_time_accumulation_example,
    cfd_deep_dive_sweep,
    full_rank_robustness_sweep,
    generator_dynamics_profile,
    principal_angle_defect,
    quantitative_recoverability_profile,
)


def test_principal_angle_defect_matches_exactness_on_rank_one_targets() -> None:
    exact_obs = np.asarray([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=float)
    fail_obs = np.asarray([[1.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=float)
    protected = np.asarray([[1.0, 0.0, 0.0]], dtype=float)

    exact_profile = quantitative_recoverability_profile(exact_obs, protected)
    fail_profile = quantitative_recoverability_profile(fail_obs, protected)

    assert exact_profile.exact_recoverable
    assert exact_profile.principal_angle_defect < 1e-10
    assert fail_profile.exact_recoverable is False
    assert fail_profile.principal_angle_defect > 1e-6


def test_normalized_residual_agrees_with_angle_defect_for_rank_one_target() -> None:
    observation = np.asarray([[1.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=float)
    protected = np.asarray([[1.0, 0.0, 0.0]], dtype=float)

    profile = quantitative_recoverability_profile(observation, protected)
    direct = principal_angle_defect(observation, protected)

    assert abs(profile.normalized_rowspace_residual - direct) < 1e-10


def test_canonical_rank_deficient_fragility_has_nonzero_failure_for_any_positive_epsilon() -> None:
    sweep = canonical_rank_deficient_fragility_sweep((0.0, 1e-4, 1e-3, 1e-2))

    assert sweep.base_exact_recoverable
    assert sweep.first_failure_epsilon is not None
    assert sweep.first_failure_epsilon <= 1e-4 + 1e-12

    # In the canonical construction, the residual is epsilon/sqrt(1+epsilon^2).
    for row in sweep.rows:
        if row.epsilon <= 0.0:
            assert row.exact_recoverable
            continue
        expected = row.epsilon / math.sqrt(1.0 + row.epsilon * row.epsilon)
        assert row.exact_recoverable is False
        assert abs(row.rowspace_residual - expected) < 5e-10


def test_full_rank_robustness_sweep_stays_exact_for_small_perturbations() -> None:
    sweep = full_rank_robustness_sweep((0.0, 0.01, 0.05, 0.1))

    assert sweep.base_exact_recoverable
    assert all(row.exact_recoverable for row in sweep.rows)
    assert all(row.collision_gap < 1e-10 for row in sweep.rows)


def test_time_accumulation_example_has_finite_exact_threshold() -> None:
    report = canonical_time_accumulation_example()

    assert report.exact_threshold_step == 4
    assert [row.exact_recoverable for row in report.rows] == [False, False, False, True]
    assert report.rows[0].rowspace_residual > report.rows[-1].rowspace_residual


def test_generator_dynamics_profile_tracks_decay_and_finite_time_no_go() -> None:
    flow = LinearOCPFlow(
        generator=np.asarray(
            [
                [0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 2.0],
            ],
            dtype=float,
        ),
        protected_basis=np.asarray([[1.0], [0.0], [0.0]], dtype=float),
        disturbance_basis=np.asarray([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]], dtype=float),
    )
    x0 = np.asarray([1.0, 1.0, 1.0], dtype=float)
    report = generator_dynamics_profile(flow, x0, times=(0.0, 0.5, 1.0, 2.0))

    disturbances = [row.disturbance_norm for row in report.rows]
    assert report.disturbance_decay_margin > 0.0
    assert report.finite_time_exact_recovery_possible is False
    assert disturbances[0] > disturbances[-1]
    assert all(row.predicted_upper_bound >= row.disturbance_norm - 1e-10 for row in report.rows)


def test_cfd_deep_dive_rows_keep_bounded_hodge_and_transplant_split() -> None:
    rows = cfd_deep_dive_sweep(grid_sizes=(17, 25), contaminations=(0.1, 0.3))

    assert len(rows) == 4
    for row in rows:
        assert row.periodic_divergence_suppression > 1e6
        assert row.periodic_recovery_error < 1e-8
        assert row.transplant_boundary_normal_rms > 1e-3
        assert row.bounded_hodge_recovery_error < 1e-8
        assert row.bounded_hodge_boundary_normal_rms < 1e-6
        assert row.bounded_hodge_vs_transplant_boundary_ratio > 1e3


def test_canonical_structure_classes_cover_robust_fragile_and_repairable() -> None:
    rows = canonical_structure_classes()
    classes = {row.case_name: row.structural_class for row in rows}

    assert classes['robust-full-information'] == 'robust_exact_full_information'
    assert classes['exact-but-fragile-rank-deficient'] == 'aligned_exact_but_fragile'
    assert classes['augmentation-repairable'] == 'augmentation_repairable_misaligned'
