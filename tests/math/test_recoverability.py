from __future__ import annotations

import numpy as np

from ocp.recoverability import (
    adversarial_noise_lower_bound,
    analytic_collapse_modulus,
    analytic_noise_lower_bound_sweep,
    control_minimal_complexity_sweep,
    diagonal_functional_complexity_sweep,
    diagonal_functional_history_weights,
    diagonal_functional_minimal_horizon,
    diagonal_history_recovery_weights,
    finite_collapse_modulus,
    finite_recoverability_report,
    functional_observability_sweep,
    minimal_linear_observation_complexity,
    naive_finite_collapse_modulus,
    periodic_cutoff_recoverability_sweep,
    periodic_functional_complexity_sweep,
    periodic_protected_complexity_sweep,
    periodic_velocity_recoverability_sweep,
    qubit_phase_collision_formula,
    qubit_record_collapse_sweep,
    restricted_linear_rank_lower_bound,
    restricted_linear_recoverability,
)


def test_fiber_collision_and_exact_recoverability_match() -> None:
    observations = [np.array([0.0]), np.array([1.0]), np.array([1.0])]
    protected = [np.array([2.0]), np.array([3.0]), np.array([3.0])]
    report = finite_recoverability_report(observations, protected, [0.0, 0.5, 1.0])
    assert report.exact_recoverable is True
    assert report.collision_max_protected_distance == 0.0
    assert report.collapse_values[0] == 0.0

    protected_bad = [np.array([2.0]), np.array([3.0]), np.array([5.0])]
    bad = finite_recoverability_report(observations, protected_bad, [0.0, 0.5, 1.0])
    assert bad.exact_recoverable is False
    assert bad.collision_max_protected_distance > 1.9
    assert bad.collapse_values[0] > 1.9


def test_vectorized_collapse_matches_naive_reference() -> None:
    observations = [np.array([0.0, 0.0]), np.array([0.25, 0.0]), np.array([0.25, 0.4]), np.array([0.5, 0.0])]
    protected = [np.array([0.0]), np.array([1.0]), np.array([1.25]), np.array([2.0])]
    deltas = np.linspace(0.0, 0.6, 7)
    fast = finite_collapse_modulus(observations, protected, deltas)
    slow = naive_finite_collapse_modulus(observations, protected, deltas)
    assert np.allclose(fast, slow)


def test_restricted_linear_recovery_criterion_matches_horizon_boundary() -> None:
    a = 0.95
    b = 0.65
    epsilon = 0.3
    O1 = np.array([[1.0, epsilon]])
    L = np.array([[0.0, 1.0]])
    one_step = restricted_linear_recoverability(O1, L)
    assert one_step.exact_recoverable is False

    O2 = np.array([[1.0, epsilon], [a, epsilon * b]])
    two_step = restricted_linear_recoverability(O2, L)
    assert two_step.exact_recoverable is True
    assert two_step.recovery_operator is not None
    residual = np.linalg.norm(two_step.recovery_operator @ O2 - L)
    assert residual < 1e-8
    rank_bound = restricted_linear_rank_lower_bound(O2, L)
    assert rank_bound.rank_observation >= rank_bound.rank_protected
    assert rank_bound.lower_bound_satisfied is True


def test_analytic_collapse_modulus_has_expected_threshold_behavior() -> None:
    deltas = [0.0, 0.25, 0.5, 1.0]
    exact = analytic_collapse_modulus(0.5, deltas)
    assert exact.exact_recoverable is True
    assert exact.collision_max_protected_distance == 0.0
    assert np.allclose(exact.collapse_values, [0.0, 0.5, 1.0, 2.0])

    impossible = analytic_collapse_modulus(0.0, deltas)
    assert impossible.exact_recoverable is False
    assert impossible.collision_max_protected_distance == 2.0
    assert impossible.collapse_values[0] == 2.0

    observations = [np.array([0.0]), np.array([0.1]), np.array([0.4])]
    protected = [np.array([0.0]), np.array([1.0]), np.array([2.0])]
    assert adversarial_noise_lower_bound(observations, protected, 0.1) == 0.5


def test_analytic_noise_lower_bound_sweep_matches_closed_form() -> None:
    epsilon = 0.25
    sweep = analytic_noise_lower_bound_sweep(epsilon=epsilon, noise_radii=(0.0, 0.05, 0.1, 0.2, 0.5, 0.75))
    for row in sweep['rows']:
        radius = row['noise_radius']
        expected = min(1.0, radius / (2.0 * epsilon))
        assert abs(row['lower_bound'] - expected) < 1e-12


def test_qubit_sweep_keeps_meridian_exact_and_phase_loss_no_go() -> None:
    result = qubit_record_collapse_sweep(theta_samples=9, phase_samples=9, delta_count=8)
    rows = result['rows']

    def row(var: str, phase: float) -> dict[str, float]:
        return next(item for item in rows if item['protected_variable'] == var and item['phase_window_deg'] == phase)

    meridian = row('bloch_vector', 0.0)
    phase_loss = row('bloch_vector', 180.0)
    weak_protected = row('z_coordinate', 180.0)

    assert meridian['exact_recoverable'] is True
    assert meridian['collision_max_protected_distance'] < 1e-8
    assert phase_loss['exact_recoverable'] is False
    assert phase_loss['collision_max_protected_distance'] > 0.5
    assert weak_protected['exact_recoverable'] is True
    assert weak_protected['collision_max_protected_distance'] < 1e-8
    for phase in (0.0, 15.0, 30.0, 60.0, 90.0, 180.0):
        numeric = row('bloch_vector', phase)['collision_max_protected_distance']
        analytic = qubit_phase_collision_formula(phase)
        assert abs(numeric - analytic) < 0.08


def test_qubit_phase_collision_formula_survives_refined_sampling() -> None:
    result = qubit_record_collapse_sweep(
        phase_windows_deg=(5.0, 10.0, 20.0, 45.0, 75.0, 120.0),
        theta_samples=29,
        phase_samples=31,
        delta_count=10,
    )
    rows = {(row['protected_variable'], row['phase_window_deg']): row for row in result['rows']}
    for window in (5.0, 10.0, 20.0, 45.0, 75.0, 120.0):
        numeric = rows[('bloch_vector', window)]['collision_max_protected_distance']
        analytic = qubit_phase_collision_formula(window)
        assert abs(numeric - analytic) < 0.08
        assert rows[('z_coordinate', window)]['collision_max_protected_distance'] < 1e-10


def test_periodic_velocity_sweep_separates_exact_approximate_and_no_go() -> None:
    result = periodic_velocity_recoverability_sweep(n=18, delta_count=10)
    rows = {row['observation']: row for row in result['rows']}

    assert rows['full_vorticity']['exact_recoverable'] is True
    assert rows['full_vorticity']['mean_recovery_error'] < 1e-8

    assert rows['truncated_vorticity']['exact_recoverable'] is False
    assert rows['truncated_vorticity']['mean_recovery_error'] > 1e-3
    assert rows['truncated_vorticity']['mean_recovery_error'] < rows['divergence_only']['mean_recovery_error']

    assert rows['divergence_only']['exact_recoverable'] is False
    assert rows['divergence_only']['collision_max_protected_distance'] > 0.5


def test_periodic_cutoff_threshold_matches_mode_support_expectation() -> None:
    result = periodic_cutoff_recoverability_sweep(n=18, cutoffs=(0, 1, 2, 3), delta_count=10)
    rows = {row['cutoff']: row for row in result['rows']}
    assert rows[0]['exact_recoverable'] is False
    assert rows[1]['exact_recoverable'] is False
    assert rows[2]['exact_recoverable'] is True
    assert rows[3]['exact_recoverable'] is True
    assert rows[1]['rank_observation'] < rows[1]['rank_protected']
    assert rows[2]['rank_observation'] >= rows[2]['rank_protected']
    assert rows[2]['mean_recovery_error'] < 1e-8
    assert rows[1]['collision_max_protected_distance'] > 0.5


def test_periodic_protected_threshold_tracks_minimal_cutoff_by_protected_support() -> None:
    result = periodic_protected_complexity_sweep(n=18, cutoffs=(0, 1, 2, 3), delta_count=10)
    rows = {}
    for row in result['rows']:
        rows[(row['protected_variable'], row['cutoff'])] = row

    expected_thresholds = {
        'mode_1_coefficient': 1,
        'modes_1_2_coefficients': 2,
        'full_modal_coefficients': 3,
    }
    for protected_variable, threshold in expected_thresholds.items():
        for cutoff in (0, 1, 2, 3):
            row = rows[(protected_variable, cutoff)]
            assert row['predicted_min_cutoff'] == threshold
            if cutoff < threshold:
                assert row['exact_recoverable'] is False
                assert row['collision_max_protected_distance'] > 0.1
            else:
                assert row['exact_recoverable'] is True
                assert row['mean_recovery_error'] < 1e-8


def test_periodic_protected_threshold_is_stable_across_discretizations() -> None:
    coarse = periodic_protected_complexity_sweep(n=18, cutoffs=(0, 1, 2, 3), delta_count=8)
    fine = periodic_protected_complexity_sweep(n=24, cutoffs=(0, 1, 2, 3), delta_count=8)

    def threshold_map(result: dict[str, object]) -> dict[str, int]:
        mapping: dict[str, int] = {}
        for row in result['rows']:
            if row['exact_recoverable'] and row['protected_variable'] not in mapping:
                mapping[row['protected_variable']] = row['cutoff']
        return mapping

    assert threshold_map(coarse) == threshold_map(fine) == {
        'mode_1_coefficient': 1,
        'modes_1_2_coefficients': 2,
        'full_modal_coefficients': 3,
    }


def test_functional_observability_sweep_keeps_one_step_impossible_and_two_step_exact() -> None:
    result = functional_observability_sweep(epsilon_values=(0.0, 0.2), horizons=(1, 2))
    rows = result['rows']

    def row(epsilon: float, horizon: int) -> dict[str, float]:
        return next(item for item in rows if abs(item['epsilon'] - epsilon) < 1e-12 and item['horizon'] == horizon)

    one_step = row(0.2, 1)
    two_step = row(0.2, 2)
    zero_eps = row(0.0, 2)

    assert one_step['exact_recoverable'] is False
    assert abs(one_step['collision_max_protected_distance'] - 2.0) < 1e-9
    assert two_step['exact_recoverable'] is True
    assert two_step['max_recovery_error'] < 1e-8
    assert two_step['recoverability_margin'] > 0.03
    assert zero_eps['exact_recoverable'] is False
    assert abs(zero_eps['collision_max_protected_distance'] - 2.0) < 1e-9

    observer = next(item for item in result['observer_reports'] if abs(item['epsilon'] - 0.2) < 1e-12)
    assert observer['spectral_radius'] < 1.0
    assert observer['protected_error_history'][-1] < observer['protected_error_history'][0]


def test_control_minimal_history_threshold_matches_active_sensor_count() -> None:
    result = control_minimal_complexity_sweep(horizons=(1, 2, 3, 4))
    rows = {(row['sensor_profile'], row['horizon']): row for row in result['rows']}

    for horizon in (1, 2, 3, 4):
        three_active = rows[('three_active', horizon)]
        if horizon < 3:
            assert three_active['exact_recoverable'] is False
            assert three_active['collision_max_protected_distance'] > 0.1
        else:
            assert three_active['exact_recoverable'] is True
            assert three_active['mean_recovery_error'] < 1e-8

        two_active = rows[('two_active', horizon)]
        if horizon < 2:
            assert two_active['exact_recoverable'] is False
            assert two_active['collision_max_protected_distance'] > 0.1
        else:
            assert two_active['exact_recoverable'] is True
            assert two_active['mean_recovery_error'] < 1e-8

        hidden = rows[('protected_hidden', horizon)]
        assert hidden['exact_recoverable'] is False
        assert hidden['collision_max_protected_distance'] > 0.1


def test_control_interpolation_formula_matches_linear_recovery_operator() -> None:
    eigenvalues = (0.95, 0.8, 0.65)
    sensor_weights = (1.0, 0.4, 0.2)
    horizon = 3
    protected_index = 2
    weights = diagonal_history_recovery_weights(eigenvalues, sensor_weights, protected_index, horizon)
    assert weights is not None
    O = np.array([[sensor_weights[i] * (eigenvalues[i] ** t) for i in range(3)] for t in range(horizon)], dtype=float)
    L = np.array([[0.0, 0.0, 1.0]])
    linear = restricted_linear_recoverability(O, L)
    assert linear.exact_recoverable is True
    assert linear.recovery_operator is not None
    assert np.linalg.norm(np.asarray(weights).reshape(1, -1) @ O - L) < 1e-10
    assert np.linalg.norm(np.asarray(weights).reshape(1, -1) - linear.recovery_operator) < 1e-8


def test_minimal_linear_observation_complexity_finds_first_exact_level() -> None:
    observation_matrices = [
        np.array([[1.0, 0.0, 0.0]]),
        np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]),
        np.eye(3),
    ]
    protected = np.array([[0.0, 1.0, 1.0]])
    report = minimal_linear_observation_complexity(observation_matrices, protected)
    assert report['minimal_index'] == 2
    assert report['exact_flags'] == [False, False, True]


def test_periodic_functional_threshold_matches_support_max_for_general_functionals() -> None:
    result = periodic_functional_complexity_sweep(n=14, cutoffs=(0, 1, 2, 3, 4), delta_count=6)
    rows = {(row['functional_name'], row['cutoff']): row for row in result['rows']}
    expected = {
        'low_mode_sum': 2,
        'bandlimited_contrast': 3,
        'full_weighted_sum': 4,
    }
    for functional_name, threshold in expected.items():
        for cutoff in (0, 1, 2, 3, 4):
            row = rows[(functional_name, cutoff)]
            assert row['predicted_min_cutoff'] == threshold
            if cutoff < threshold:
                assert row['exact_recoverable'] is False
                assert row['collision_max_protected_distance'] > 0.1
            else:
                assert row['exact_recoverable'] is True
                assert row['mean_recovery_error'] < 1e-8


def test_periodic_functional_hierarchy_keeps_weaker_variable_while_stronger_one_fails() -> None:
    result = periodic_functional_complexity_sweep(n=14, cutoffs=(2,), delta_count=6)
    rows = {row['functional_name']: row for row in result['rows']}
    assert rows['low_mode_sum']['exact_recoverable'] is True
    assert rows['bandlimited_contrast']['exact_recoverable'] is False
    assert rows['full_weighted_sum']['exact_recoverable'] is False


def test_diagonal_functional_minimal_horizon_tracks_polynomial_degree() -> None:
    eigenvalues = (0.95, 0.8, 0.65)
    sensor_weights = (1.0, 0.4, 0.2)
    sensor_sum_horizon, sensor_sum_weights = diagonal_functional_minimal_horizon(eigenvalues, sensor_weights, sensor_weights, max_horizon=4)
    first_moment = [sensor_weights[i] * eigenvalues[i] for i in range(3)]
    first_moment_horizon, first_moment_weights = diagonal_functional_minimal_horizon(eigenvalues, sensor_weights, first_moment, max_horizon=4)
    second_moment = [sensor_weights[i] * (eigenvalues[i] ** 2) for i in range(3)]
    second_moment_horizon, second_moment_weights = diagonal_functional_minimal_horizon(eigenvalues, sensor_weights, second_moment, max_horizon=4)
    hidden_horizon, hidden_weights = diagonal_functional_minimal_horizon(eigenvalues, (1.0, 0.4, 0.0), (0.0, 0.0, 1.0), max_horizon=4)

    assert sensor_sum_horizon == 1
    assert first_moment_horizon == 2
    assert second_moment_horizon == 3
    assert hidden_horizon is None
    assert sensor_sum_weights is not None and abs(sensor_sum_weights[0] - 1.0) < 1e-10
    assert first_moment_weights is not None and abs(first_moment_weights[1] - 1.0) < 1e-10
    assert second_moment_weights is not None and abs(second_moment_weights[2] - 1.0) < 1e-10
    assert hidden_weights is None


def test_diagonal_functional_complexity_generalizes_coordinate_threshold() -> None:
    result = diagonal_functional_complexity_sweep(horizons=(1, 2, 3, 4))
    rows = {(row['sensor_profile'], row['functional_name'], row['horizon']): row for row in result['rows']}

    assert rows[('three_active', 'sensor_sum', 1)]['exact_recoverable'] is True
    assert rows[('three_active', 'first_moment', 1)]['exact_recoverable'] is False
    assert rows[('three_active', 'first_moment', 2)]['exact_recoverable'] is True
    assert rows[('three_active', 'second_moment', 2)]['exact_recoverable'] is False
    assert rows[('three_active', 'second_moment', 3)]['exact_recoverable'] is True
    assert rows[('protected_hidden', 'protected_coordinate', 4)]['exact_recoverable'] is False
    assert rows[('protected_hidden', 'protected_coordinate', 4)]['predicted_min_horizon'] is None


def test_diagonal_functional_weights_match_rowspace_recovery() -> None:
    eigenvalues = (0.95, 0.8, 0.65)
    sensor_weights = (1.0, 0.4, 0.2)
    protected_weights = tuple(sensor_weights[i] * (eigenvalues[i] ** 2) for i in range(3))
    horizon = 3
    weights = diagonal_functional_history_weights(eigenvalues, sensor_weights, protected_weights, horizon)
    assert weights is not None
    O = np.array([[sensor_weights[i] * (eigenvalues[i] ** t) for i in range(3)] for t in range(horizon)], dtype=float)
    L = np.array([protected_weights], dtype=float)
    linear = restricted_linear_recoverability(O, L)
    assert linear.exact_recoverable is True
    assert linear.recovery_operator is not None
    assert np.linalg.norm(np.asarray(weights).reshape(1, -1) @ O - L) < 1e-10
    assert np.linalg.norm(np.asarray(weights).reshape(1, -1) - linear.recovery_operator) < 1e-8


def test_periodic_functional_threshold_random_supports_match_support_formula() -> None:
    functionals = {
        'random_a': (0.4, 0.0, -1.2, 0.0),
        'random_b': (0.0, -0.75, 0.0, 0.2),
        'random_c': (0.3, -0.2, 0.5, -0.1),
    }
    result = periodic_functional_complexity_sweep(n=12, cutoffs=(0, 1, 2, 3, 4), delta_count=6, functionals=functionals)
    rows = {(row['functional_name'], row['cutoff']): row for row in result['rows']}
    expected = {
        'random_a': 3,
        'random_b': 4,
        'random_c': 4,
    }
    for functional_name, threshold in expected.items():
        first_exact = min(row['cutoff'] for row in result['rows'] if row['functional_name'] == functional_name and row['exact_recoverable'])
        assert first_exact == threshold
        for cutoff in range(threshold):
            assert rows[(functional_name, cutoff)]['exact_recoverable'] is False


def test_diagonal_functional_threshold_random_polynomial_targets() -> None:
    eigenvalues = (0.95, 0.8, 0.65)
    sensor_weights = (1.0, 0.4, 0.2)
    test_polynomials = [
        (2.0,),
        (0.1, -0.7),
        (0.25, -0.5, 1.25),
    ]
    expected_horizons = [1, 2, 3]
    for coeffs, expected in zip(test_polynomials, expected_horizons, strict=True):
        protected = []
        for index, lam in enumerate(eigenvalues):
            value = sum(coeff * (lam ** power) for power, coeff in enumerate(coeffs))
            protected.append(sensor_weights[index] * value)
        horizon, _ = diagonal_functional_minimal_horizon(eigenvalues, sensor_weights, protected, max_horizon=4)
        assert horizon == expected
