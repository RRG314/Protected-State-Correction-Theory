from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from ocp.cfd import cfd_projection_summary
from ocp.continuous import LinearOCPFlow
from ocp.recoverability import (
    finite_collapse_modulus,
    diagonal_functional_complexity_sweep,
    diagonal_polynomial_threshold_sweep,
    nested_linear_threshold_profile,
    periodic_functional_complexity_sweep,
    periodic_threshold_stress_sweep,
    restricted_linear_stability_report,
    same_rank_alignment_counterexample,
)


ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')


def _load_json(path: Path) -> dict[str, object]:
    if not path.exists():
        pytest.skip(f'missing generated artifact: {path}')
    return json.loads(path.read_text())


def test_operator_examples_json_matches_recomputed_cfd_and_generator_examples() -> None:
    data = _load_json(ROOT / 'data/generated/validations/operator_examples.json')

    cfd = cfd_projection_summary(n_periodic=48, n_bounded=32, contamination=0.2)
    saved_cfd = data['cfd']
    assert np.isclose(saved_cfd['periodic']['before_l2_divergence'], cfd.periodic.before_l2_divergence)
    assert np.isclose(saved_cfd['periodic']['after_projection_l2_divergence'], cfd.periodic.after_projection_l2_divergence)
    assert np.isclose(saved_cfd['periodic']['recovery_l2_error'], cfd.periodic.recovery_l2_error)
    assert np.isclose(saved_cfd['bounded_hodge_exact']['recovery_l2_error'], cfd.bounded_hodge_exact.recovery_l2_error)
    assert np.isclose(
        saved_cfd['bounded_hodge_exact']['orthogonality_residual'],
        cfd.bounded_hodge_exact.orthogonality_residual,
    )
    assert np.isclose(saved_cfd['bounded_transplant']['projected_boundary_normal_rms'], cfd.bounded_transplant.projected_boundary_normal_rms)
    assert np.isclose(
        saved_cfd['divergence_only_no_go_witness']['state_separation_rms'],
        cfd.divergence_only_witness.state_separation_rms,
    )

    generator = np.array(
        [
            [0.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
            [0.0, 0.0, 1.5],
        ]
    )
    protected = np.array([[1.0], [0.0], [0.0]])
    disturbance = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    flow = LinearOCPFlow(generator, protected, disturbance)
    saved_flow = data['continuous_generators']['finite_time_exact_recovery_no_go']
    recomputed = [flow.exact_recovery_residual(time) for time in saved_flow['times']]
    assert np.allclose(saved_flow['exact_recovery_residuals'], recomputed)
    assert saved_flow['exact_recovery_possible'] == [False, False, False]

    saved_capacity = data['capacity']['restricted_linear']
    assert saved_capacity['rowspace_deficiency'] == 1
    assert saved_capacity['min_unrestricted_added_measurements'] == 1


def test_recoverability_summary_json_matches_recomputed_threshold_sweeps() -> None:
    data = _load_json(ROOT / 'data/generated/recoverability/recoverability_summary.json')

    periodic = periodic_functional_complexity_sweep()
    saved_periodic_rows = {
        (row['functional_name'], row['cutoff']): row for row in data['periodic_functional_complexity_sweep']['rows']
    }
    for row in periodic['rows']:
        key = (row['functional_name'], row['cutoff'])
        saved = saved_periodic_rows[key]
        assert saved['predicted_min_cutoff'] == row['predicted_min_cutoff']
        assert saved['exact_recoverable'] == row['exact_recoverable']
        assert np.isclose(saved['collision_max_protected_distance'], row['collision_max_protected_distance'])
        assert np.isclose(saved['mean_recovery_error'], row['mean_recovery_error'])

    diagonal = diagonal_functional_complexity_sweep()
    saved_diagonal_rows = {
        (row['sensor_profile'], row['functional_name'], row['horizon']): row
        for row in data['diagonal_functional_complexity_sweep']['rows']
    }
    for row in diagonal['rows']:
        key = (row['sensor_profile'], row['functional_name'], row['horizon'])
        saved = saved_diagonal_rows[key]
        assert saved['predicted_min_horizon'] == row['predicted_min_horizon']
        assert saved['exact_recoverable'] == row['exact_recoverable']
        assert np.isclose(saved['collision_max_protected_distance'], row['collision_max_protected_distance'])
        assert np.isclose(saved['mean_recovery_error'], row['mean_recovery_error'])

    periodic_stress = periodic_threshold_stress_sweep()
    saved_periodic_stress_rows = {
        (row['case_name'], row['functional_name'], row['cutoff']): row
        for row in data['periodic_threshold_stress_sweep']['rows']
    }
    for row in periodic_stress['rows']:
        key = (row['case_name'], row['functional_name'], row['cutoff'])
        saved = saved_periodic_stress_rows[key]
        assert saved['predicted_min_cutoff'] == row['predicted_min_cutoff']
        assert saved['observed_min_cutoff'] == row['observed_min_cutoff']
        assert saved['exact_recoverable'] == row['exact_recoverable']
        assert np.isclose(saved['collision_gap'], row['collision_gap'])
        assert np.isclose(saved['rowspace_residual'], row['rowspace_residual'])

    diagonal_polynomial = diagonal_polynomial_threshold_sweep()
    saved_diagonal_polynomial_rows = {
        (row['case_name'], row['functional_name'], row['horizon']): row
        for row in data['diagonal_polynomial_threshold_sweep']['rows']
    }
    for row in diagonal_polynomial['rows']:
        key = (row['case_name'], row['functional_name'], row['horizon'])
        saved = saved_diagonal_polynomial_rows[key]
        assert saved['predicted_min_horizon'] == row['predicted_min_horizon']
        assert saved['observed_min_horizon'] == row['observed_min_horizon']
        assert saved['exact_recoverable'] == row['exact_recoverable']
        assert np.isclose(saved['collision_gap'], row['collision_gap'])
        assert np.isclose(saved['rowspace_residual'], row['rowspace_residual'])

    nested = nested_linear_threshold_profile(
        [
            np.zeros((1, 4), dtype=float),
            np.diag([1.0, 0.0, 0.0, 0.0]),
            np.diag([1.0, 1.0, 0.0, 0.0]),
            np.diag([1.0, 1.0, 1.0, 0.0]),
            np.diag([1.0, 1.0, 1.0, 1.0]),
        ],
        np.array([[1.0, -0.5, 0.75, 0.25]], dtype=float),
        box_radius=1.0,
        level_labels=[0, 1, 2, 3, 4],
    )
    saved_nested = data['nested_linear_threshold_profile']
    assert saved_nested['minimal_label'] == nested['minimal_label']
    assert saved_nested['gap_monotone_nonincreasing'] == nested['gap_monotone_nonincreasing']
    for saved_row, row in zip(saved_nested['rows'], nested['rows'], strict=True):
        assert saved_row['level'] == row['level']
        assert saved_row['exact_recoverable'] == row['exact_recoverable']
        assert np.isclose(saved_row['collision_gap'], row['collision_gap'])
        assert np.isclose(saved_row['rowspace_residual'], row['rowspace_residual'])

    pvrt_observation = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=float)
    pvrt_protected = np.array([[1.0, -0.5, 0.0]], dtype=float)
    pvrt_report = restricted_linear_stability_report(pvrt_observation, pvrt_protected, box_radius=1.0)
    saved_pvrt = data['pvrt_linear_stability_example']
    assert saved_pvrt['exact_recoverable'] is True
    assert np.isclose(saved_pvrt['recovery_operator_norm_upper'], pvrt_report.recovery_operator_norm_upper)
    assert np.isclose(saved_pvrt['rowspace_residual'], pvrt_report.rowspace_residual)
    assert np.isclose(saved_pvrt['collision_gap'], pvrt_report.collision_gap)
    delta_grid = np.asarray(saved_pvrt['delta_grid'], dtype=float)
    coeffs = [np.asarray(values, dtype=float) for values in np.array(np.meshgrid(*([np.linspace(-1.0, 1.0, 5)] * 3), indexing='ij')).reshape(3, -1).T]
    observations = [pvrt_observation @ coeff for coeff in coeffs]
    protected_values = [pvrt_protected @ coeff for coeff in coeffs]
    recomputed_collapse = finite_collapse_modulus(observations, protected_values, delta_grid)
    assert np.allclose(saved_pvrt['collapse_values'], recomputed_collapse)

    pvrt_counterexample = same_rank_alignment_counterexample(ambient_dimension=5, protected_rank=2, observation_rank=2)
    saved_counterexample = data['pvrt_same_rank_counterexample']
    assert saved_counterexample['ambient_dimension'] == pvrt_counterexample.ambient_dimension
    assert saved_counterexample['protected_rank'] == pvrt_counterexample.protected_rank
    assert saved_counterexample['observation_rank'] == pvrt_counterexample.observation_rank
    assert np.isclose(saved_counterexample['exact_rowspace_residual'], pvrt_counterexample.exact_rowspace_residual)
    assert np.isclose(saved_counterexample['fail_rowspace_residual'], pvrt_counterexample.fail_rowspace_residual)
    assert np.isclose(saved_counterexample['exact_collision_gap'], pvrt_counterexample.exact_collision_gap)
    assert np.isclose(saved_counterexample['fail_collision_gap'], pvrt_counterexample.fail_collision_gap)
