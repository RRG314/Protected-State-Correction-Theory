from __future__ import annotations

import json
from pathlib import Path
import subprocess

import numpy as np

from ocp.next_phase import (
    canonical_rank_deficient_fragility_sweep,
    canonical_structure_classes,
    canonical_time_accumulation_example,
    cfd_deep_dive_sweep,
    full_rank_robustness_sweep,
    quantitative_recoverability_profile,
)

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')


def _load_summary() -> dict[str, object]:
    path = ROOT / 'data/generated/next-phase/next_phase_summary.json'
    subprocess.run(
        ['python3', 'scripts/compare/run_next_phase_examples.py'],
        cwd=ROOT,
        check=True,
    )
    return json.loads(path.read_text())


def _expected_quantitative_rows() -> list[dict[str, object]]:
    cases = (
        (
            'robust-full-information',
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 1.0],
                ],
                dtype=float,
            ),
            np.asarray([[0.2, -0.7, 1.1]], dtype=float),
        ),
        (
            'exact-but-fragile',
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                ],
                dtype=float,
            ),
            np.asarray([[1.0, 0.0, 0.0]], dtype=float),
        ),
        (
            'augmentation-repairable',
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 1.0],
                ],
                dtype=float,
            ),
            np.asarray([[0.0, 0.0, 1.0]], dtype=float),
        ),
        (
            'collision-dominated',
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                ],
                dtype=float,
            ),
            np.asarray([[0.0, 0.0, 1.0]], dtype=float),
        ),
    )
    rows: list[dict[str, object]] = []
    for name, observation, protected in cases:
        rows.append({'case': name, **quantitative_recoverability_profile(observation, protected).__dict__})
    return rows


def test_next_phase_summary_quantitative_profiles_match_recomputed() -> None:
    data = _load_summary()
    saved_rows = {row['case']: row for row in data['quantitative_profiles']}
    expected_rows = {row['case']: row for row in _expected_quantitative_rows()}
    assert set(saved_rows.keys()) == set(expected_rows.keys())

    for case in saved_rows:
        saved = saved_rows[case]
        expected = expected_rows[case]
        assert saved['exact_recoverable'] == expected['exact_recoverable']
        assert saved['structural_class'] == expected['structural_class']
        assert saved['coefficient_dimension'] == expected['coefficient_dimension']
        assert saved['observation_rank'] == expected['observation_rank']
        assert saved['protected_rank'] == expected['protected_rank']
        assert np.isclose(saved['rowspace_residual'], expected['rowspace_residual'])
        assert np.isclose(saved['normalized_rowspace_residual'], expected['normalized_rowspace_residual'])
        assert np.isclose(saved['principal_angle_defect'], expected['principal_angle_defect'], atol=5e-8)
        assert np.isclose(saved['alignment_score'], expected['alignment_score'])
        assert np.isclose(saved['collision_gap'], expected['collision_gap'])
        assert np.isclose(saved['zero_noise_lower_bound'], expected['zero_noise_lower_bound'])
        if expected['recovery_operator_norm_upper'] is None:
            assert saved['recovery_operator_norm_upper'] is None
        else:
            assert np.isclose(saved['recovery_operator_norm_upper'], expected['recovery_operator_norm_upper'])


def test_next_phase_summary_fragility_dynamics_and_cfd_reports_remain_consistent() -> None:
    data = _load_summary()

    fragile = canonical_rank_deficient_fragility_sweep((0.0, 1e-4, 1e-3, 1e-2, 1e-1))
    saved_fragile = data['rank_deficient_fragility']
    assert saved_fragile['base_exact_recoverable'] == fragile.base_exact_recoverable
    assert np.isclose(saved_fragile['base_rowspace_residual'], fragile.base_rowspace_residual)
    assert np.isclose(saved_fragile['base_principal_angle_defect'], fragile.base_principal_angle_defect, atol=5e-8)
    assert np.isclose(saved_fragile['base_collision_gap'], fragile.base_collision_gap)
    assert np.isclose(saved_fragile['first_failure_epsilon'], fragile.first_failure_epsilon)
    for saved, expected in zip(saved_fragile['rows'], fragile.rows, strict=True):
        assert np.isclose(saved['epsilon'], expected.epsilon)
        assert saved['exact_recoverable'] == expected.exact_recoverable
        assert np.isclose(saved['rowspace_residual'], expected.rowspace_residual)
        assert np.isclose(saved['principal_angle_defect'], expected.principal_angle_defect, atol=5e-8)
        assert np.isclose(saved['collision_gap'], expected.collision_gap)

    robust = full_rank_robustness_sweep((0.0, 1e-2, 5e-2, 1e-1, 2e-1))
    saved_robust = data['full_rank_robustness']
    assert saved_robust['base_exact_recoverable'] == robust.base_exact_recoverable
    assert saved_robust['first_failure_epsilon'] == robust.first_failure_epsilon
    for saved, expected in zip(saved_robust['rows'], robust.rows, strict=True):
        assert np.isclose(saved['epsilon'], expected.epsilon)
        assert saved['exact_recoverable'] == expected.exact_recoverable
        assert np.isclose(saved['rowspace_residual'], expected.rowspace_residual)
        assert np.isclose(saved['principal_angle_defect'], expected.principal_angle_defect, atol=5e-8)
        assert np.isclose(saved['collision_gap'], expected.collision_gap)

    accumulation = canonical_time_accumulation_example()
    saved_acc = data['time_accumulation']
    assert saved_acc['exact_threshold_step'] == accumulation.exact_threshold_step
    for saved, expected in zip(saved_acc['rows'], accumulation.rows, strict=True):
        assert saved['step'] == expected.step
        assert saved['exact_recoverable'] == expected.exact_recoverable
        assert np.isclose(saved['rowspace_residual'], expected.rowspace_residual)
        assert np.isclose(saved['principal_angle_defect'], expected.principal_angle_defect, atol=5e-8)
        assert np.isclose(saved['collision_gap'], expected.collision_gap)

    structures = canonical_structure_classes()
    saved_structures = data['structure_classes']
    for saved, expected in zip(saved_structures, structures, strict=True):
        assert saved['case_name'] == expected.case_name
        assert saved['structural_class'] == expected.structural_class
        assert saved['exact_recoverable'] == expected.exact_recoverable
        assert saved['observation_rank'] == expected.observation_rank
        assert saved['coefficient_dimension'] == expected.coefficient_dimension
        assert np.isclose(saved['rowspace_residual'], expected.rowspace_residual)
        assert np.isclose(saved['principal_angle_defect'], expected.principal_angle_defect, atol=5e-8)
        assert np.isclose(saved['collision_gap'], expected.collision_gap)
        assert saved['unrestricted_minimal_added_measurements'] == expected.unrestricted_minimal_added_measurements

    cfd = cfd_deep_dive_sweep((17, 25, 33), (0.1, 0.2, 0.3))
    saved_cfd = data['cfd_deep_dive']
    assert len(saved_cfd) == len(cfd)
    for saved, expected in zip(saved_cfd, cfd, strict=True):
        assert saved['grid_size'] == expected.grid_size
        assert np.isclose(saved['contamination'], expected.contamination)
        assert np.isclose(saved['periodic_divergence_suppression'], expected.periodic_divergence_suppression)
        assert np.isclose(saved['periodic_recovery_error'], expected.periodic_recovery_error)
        assert np.isclose(saved['transplant_divergence_suppression'], expected.transplant_divergence_suppression)
        assert np.isclose(saved['transplant_boundary_normal_rms'], expected.transplant_boundary_normal_rms)
        assert np.isclose(saved['bounded_hodge_recovery_error'], expected.bounded_hodge_recovery_error)
        assert np.isclose(saved['bounded_hodge_boundary_normal_rms'], expected.bounded_hodge_boundary_normal_rms)
        assert np.isclose(saved['bounded_hodge_vs_transplant_boundary_ratio'], expected.bounded_hodge_vs_transplant_boundary_ratio)
