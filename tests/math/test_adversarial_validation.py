from __future__ import annotations

from itertools import product

import numpy as np

from ocp.discovery_mixer import analyze_control_custom_case, analyze_linear_custom_case, analyze_periodic_custom_case
from ocp.recoverability import (
    diagonal_functional_history_weights,
    restricted_linear_collision_gap,
)

DIAGONAL_EIGENVALUES = np.array([0.95, 0.8, 0.65], dtype=float)


def _bruteforce_box_gap(observation: np.ndarray, protected: np.ndarray, *, box_radius: float = 1.0, grid_points: int = 9) -> float:
    dim = observation.shape[1]
    grid = np.linspace(-box_radius, box_radius, grid_points)
    states = np.array(list(product(grid, repeat=dim)), dtype=float)
    records = states @ observation.T
    protected_values = states @ protected.T
    best = 0.0
    for i in range(len(states)):
        for j in range(i + 1, len(states)):
            if np.linalg.norm(records[i] - records[j]) <= 1e-9:
                best = max(best, float(np.linalg.norm(protected_values[i] - protected_values[j])))
    return best


def test_restricted_linear_gap_matches_bruteforce_scan() -> None:
    observation = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 1.0]], dtype=float)
    protected = np.array([[0.0, 0.0, 1.0]], dtype=float)

    exact_gap = restricted_linear_collision_gap(observation, protected, box_radius=1.0)
    brute_gap = _bruteforce_box_gap(observation, protected, box_radius=1.0, grid_points=9)
    assert abs(exact_gap - brute_gap) <= 0.05


def test_same_support_size_periodic_functionals_can_have_different_thresholds() -> None:
    low = analyze_periodic_custom_case(
        functional_text='a2 + a3',
        observation='cutoff_vorticity',
        cutoff=2,
        delta=2.0,
    )
    high = analyze_periodic_custom_case(
        functional_text='a1 + a4',
        observation='cutoff_vorticity',
        cutoff=2,
        delta=2.0,
    )

    assert low.raw_details['predicted_min_cutoff'] == 3
    assert high.raw_details['predicted_min_cutoff'] == 4
    assert low.impossible is True
    assert high.impossible is True


def test_active_sensor_count_heuristic_fails_for_control_thresholds() -> None:
    target = np.array([1.0 * 0.95**2, 0.4 * 0.8**2, 0.2 * 0.65**2], dtype=float)
    report = analyze_control_custom_case(
        sensor_profile_text='1,0.4,0.2',
        target_text=','.join(str(value) for value in target),
        horizon=2,
        delta=0.5,
    )
    direct = diagonal_functional_history_weights(
        DIAGONAL_EIGENVALUES,
        np.array([1.0, 0.4, 0.2], dtype=float),
        target,
        3,
    )
    assert report.raw_details['predicted_min_horizon'] == 3
    assert direct is not None
    assert np.count_nonzero(np.array([1.0, 0.4, 0.2])) == 3


def test_custom_linear_parser_rejects_nonlinear_and_out_of_basis_input() -> None:
    nonlinear = analyze_linear_custom_case(
        dimension=3,
        observation_text='x1\nx2',
        protected_text='sin(x3)',
        candidate_text='x3',
        delta=1.0,
    )
    out_of_basis = analyze_linear_custom_case(
        dimension=3,
        observation_text='x1\nx2',
        protected_text='x4',
        candidate_text='x3',
        delta=1.0,
    )

    assert nonlinear.unsupported is True
    assert out_of_basis.unsupported is True
    assert nonlinear.diagnostics[0].code == 'unsupported-custom-linear-input'
    assert out_of_basis.diagnostics[0].code == 'unsupported-custom-linear-input'


def test_control_parser_rejects_hidden_coordinate_without_fake_repair() -> None:
    hidden = analyze_control_custom_case(
        sensor_profile_text='1,0.4,0',
        target_text='x3',
        horizon=4,
        delta=0.5,
    )
    assert hidden.impossible is True
    assert hidden.chosen_recommendation is None
    assert hidden.comparison is None
