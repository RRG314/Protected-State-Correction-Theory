from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from ocp.cfd import cfd_projection_summary
from ocp.continuous import LinearOCPFlow
from ocp.recoverability import diagonal_functional_complexity_sweep, periodic_functional_complexity_sweep


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
