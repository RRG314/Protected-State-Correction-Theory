from __future__ import annotations

from itertools import combinations

import numpy as np

from ocp.capacity import restricted_linear_capacity
from ocp.cfd import bounded_hodge_projection_report
from ocp.continuous import LinearOCPFlow
from ocp.physics import bounded_domain_projection_counterexample
from ocp.recoverability import diagonal_functional_history_weights, restricted_linear_collision_gap

DIAGONAL_EIGENVALUES = np.array([0.95, 0.8, 0.65], dtype=float)
CONTROL_PROFILES = {
    'three_active': np.array([1.0, 0.4, 0.2], dtype=float),
    'two_active': np.array([1.0, 0.0, 0.2], dtype=float),
    'protected_hidden': np.array([1.0, 0.4, 0.0], dtype=float),
}
PERIODIC_THRESHOLDS = {
    'mode_1_coefficient': 1,
    'modes_1_2_coefficients': 2,
    'full_modal_coefficients': 4,
    'low_mode_sum': 2,
    'bandlimited_contrast': 3,
    'full_weighted_sum': 4,
}
PERIODIC_SUPPORTS = {
    'mode_1_coefficient': {1},
    'modes_1_2_coefficients': {1, 2},
    'full_modal_coefficients': {1, 2, 3, 4},
    'low_mode_sum': {1, 2},
    'bandlimited_contrast': {2, 3},
    'full_weighted_sum': {1, 2, 3, 4},
}


def _rowspace_exact(observation: np.ndarray, protected: np.ndarray, *, tol: float = 1e-8) -> bool:
    if observation.size == 0:
        return np.linalg.norm(protected) <= tol
    solution, _, _, _ = np.linalg.lstsq(observation.T, protected.T, rcond=None)
    reconstructed = solution.T @ observation
    return float(np.linalg.norm(reconstructed - protected)) <= tol


def _min_added_rows(observation: np.ndarray, protected: np.ndarray, candidates: np.ndarray) -> int | None:
    if _rowspace_exact(observation, protected):
        return 0
    for size in range(1, candidates.shape[0] + 1):
        for combo in combinations(range(candidates.shape[0]), size):
            augmented = np.vstack([observation, candidates[list(combo)]])
            if _rowspace_exact(augmented, protected):
                return size
    return None


def _direct_control_min_horizon(profile: str, target: str, *, max_horizon: int = 4) -> int | None:
    couplings = CONTROL_PROFILES[profile]
    if target == 'protected_coordinate':
        protected = np.array([0.0, 0.0, 1.0], dtype=float)
    elif target == 'sensor_sum':
        protected = couplings.copy()
    elif target == 'first_moment':
        protected = couplings * DIAGONAL_EIGENVALUES
    elif target == 'second_moment':
        protected = couplings * (DIAGONAL_EIGENVALUES**2)
    else:
        raise ValueError(target)
    active = [index for index, value in enumerate(couplings) if abs(float(value)) > 1e-10]
    if any(abs(float(protected[index])) > 1e-10 for index in range(len(couplings)) if index not in active):
        return None
    for horizon in range(1, max_horizon + 1):
        weights = diagonal_functional_history_weights(DIAGONAL_EIGENVALUES, couplings, protected, horizon)
        if weights is not None:
            return horizon
    return None


def test_restricted_linear_minimal_augmentation_matches_bruteforce_search() -> None:
    observation = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 1.0]], dtype=float)
    protected = np.array([[0.0, 0.0, 1.0]], dtype=float)
    candidates = np.array([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], dtype=float)

    capacity = restricted_linear_capacity(observation, protected)
    assert capacity.exact_recovery_possible is False
    assert capacity.rowspace_deficiency == 1
    assert capacity.min_unrestricted_added_measurements == 1
    assert _min_added_rows(observation, protected, candidates) == 1


def test_same_record_weaker_target_can_be_exact_while_stronger_target_fails() -> None:
    observation = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 1.0]], dtype=float)
    stronger = np.array([[0.0, 0.0, 1.0]], dtype=float)
    weaker = np.array([[0.0, 1.0, 1.0]], dtype=float)

    assert _rowspace_exact(observation, stronger) is False
    assert _rowspace_exact(observation, weaker) is True


def test_periodic_thresholds_track_highest_active_mode_not_support_size() -> None:
    assert PERIODIC_THRESHOLDS['low_mode_sum'] == max(PERIODIC_SUPPORTS['low_mode_sum'])
    assert PERIODIC_THRESHOLDS['bandlimited_contrast'] == max(PERIODIC_SUPPORTS['bandlimited_contrast'])
    assert PERIODIC_THRESHOLDS['full_weighted_sum'] == max(PERIODIC_SUPPORTS['full_weighted_sum'])

    support_size_two_but_high_mode_four = {1, 4}
    support_size_two_but_high_mode_three = {2, 3}
    assert len(support_size_two_but_high_mode_four) == len(support_size_two_but_high_mode_three) == 2
    assert max(support_size_two_but_high_mode_four) == 4
    assert max(support_size_two_but_high_mode_three) == 3


def test_control_thresholds_match_direct_interpolation_logic() -> None:
    assert _direct_control_min_horizon('three_active', 'sensor_sum') == 1
    assert _direct_control_min_horizon('three_active', 'first_moment') == 2
    assert _direct_control_min_horizon('three_active', 'second_moment') == 3
    assert _direct_control_min_horizon('two_active', 'protected_coordinate') == 2
    assert _direct_control_min_horizon('protected_hidden', 'protected_coordinate') is None


def test_bounded_domain_kept_and_rejected_architectures_stay_separate() -> None:
    transplant = bounded_domain_projection_counterexample(n=17)
    bounded_hodge = bounded_hodge_projection_report(n=17)

    assert transplant.projected_boundary_normal_rms > 1e-2
    assert bounded_hodge.recovery_l2_error < 1e-8
    assert bounded_hodge.orthogonality_residual < 1e-8


def test_continuous_branch_keeps_finite_time_exactness_separate_from_asymptotic_decay() -> None:
    flow = LinearOCPFlow(
        np.array([[0.0, 0.0, 0.0], [0.0, 1.0, 1.0], [0.0, 0.0, 1.5]], dtype=float),
        np.array([[1.0], [0.0], [0.0]], dtype=float),
        np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]], dtype=float),
    )
    report = flow.report()

    assert flow.finite_time_exact_recovery_possible(2.0) is False
    assert bool(report.annihilates_protected) is True
    assert bool(report.preserves_disturbance) is True
    assert report.protected_mixing_norm < 1e-8


def test_restricted_linear_collision_gap_stays_positive_on_tracked_impossible_case() -> None:
    observation = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 1.0]], dtype=float)
    protected = np.array([[0.0, 0.0, 1.0]], dtype=float)
    gap = restricted_linear_collision_gap(observation, protected, box_radius=1.0)
    assert gap > 0.5
