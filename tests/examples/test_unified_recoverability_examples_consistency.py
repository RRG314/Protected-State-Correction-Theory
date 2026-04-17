from __future__ import annotations

import json
from pathlib import Path
import subprocess

import numpy as np

from ocp.fiber_limits import (
    canonical_model_mismatch_report,
    candidate_library_budget_report,
    canonical_detectable_only_examples,
    control_regime_hierarchy_report,
    coordinate_rank_enumeration_report,
    noisy_restricted_linear_target_hierarchy_report,
    periodic_modal_refinement_report,
    rank_only_classifier_failure_report,
    restricted_linear_family_enlargement_report,
    restricted_linear_fiber_geometry_report,
    restricted_linear_model_mismatch_report,
)
from ocp.recoverability import functional_observability_sweep, periodic_functional_complexity_sweep

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')


def _load() -> dict[str, object]:
    path = ROOT / 'data/generated/unified-recoverability/unified_recoverability_summary.json'
    subprocess.run(
        ['python3', 'scripts/compare/run_fiber_recoverability_examples.py'],
        cwd=ROOT,
        check=True,
    )
    return json.loads(path.read_text())


def test_unified_recoverability_summary_matches_recomputed_examples() -> None:
    data = _load()

    canonical = canonical_detectable_only_examples()
    saved_canonical = data['canonical_detectable_only_examples']
    assert saved_canonical['finite']['detectable_only'] == canonical['finite'].detectable_only
    assert saved_canonical['finite']['strong_exact_recoverable'] == canonical['finite'].strong_exact_recoverable
    assert saved_canonical['finite']['weak_exact_recoverable'] == canonical['finite'].weak_exact_recoverable
    assert np.isclose(saved_canonical['finite']['strong_collision_gap'], canonical['finite'].strong_collision_gap)
    assert np.isclose(saved_canonical['restricted_linear']['strong_rowspace_residual'], canonical['restricted_linear'].strong_rowspace_residual)
    assert np.isclose(saved_canonical['restricted_linear']['weak_rowspace_residual'], canonical['restricted_linear'].weak_rowspace_residual)
    assert saved_canonical['restricted_linear']['detectable_only'] == canonical['restricted_linear'].detectable_only

    rank_only = rank_only_classifier_failure_report((3, 4, 5, 6))
    saved_rank_only = data['rank_only_classifier_failure']
    assert saved_rank_only['witness_count'] == rank_only.witness_count
    assert saved_rank_only['all_same_rank'] == rank_only.all_same_rank
    assert saved_rank_only['all_opposite_verdicts'] == rank_only.all_opposite_verdicts
    assert len(saved_rank_only['rows']) == len(rank_only.rows)
    for saved_row, row in zip(saved_rank_only['rows'], rank_only.rows, strict=True):
        assert saved_row['ambient_dimension'] == row.ambient_dimension
        assert saved_row['protected_rank'] == row.protected_rank
        assert saved_row['observation_rank'] == row.observation_rank
        assert saved_row['exact_rank_observation'] == row.exact_rank_observation
        assert saved_row['fail_rank_observation'] == row.fail_rank_observation
        assert saved_row['exact_recoverable'] == row.exact_recoverable
        assert saved_row['fail_recoverable'] == row.fail_recoverable
        assert np.isclose(saved_row['exact_rowspace_residual'], row.exact_rowspace_residual)
        assert np.isclose(saved_row['fail_rowspace_residual'], row.fail_rowspace_residual)
        assert np.isclose(saved_row['exact_collision_gap'], row.exact_collision_gap)
        assert np.isclose(saved_row['fail_collision_gap'], row.fail_collision_gap)

    coordinate = coordinate_rank_enumeration_report((3, 4, 5))
    saved_coordinate = data['coordinate_rank_enumeration']
    assert saved_coordinate['all_levels_have_exact_and_fail'] == coordinate.all_levels_have_exact_and_fail
    assert len(saved_coordinate['rows']) == len(coordinate.rows)
    for saved_row, row in zip(saved_coordinate['rows'], coordinate.rows, strict=True):
        assert saved_row['ambient_dimension'] == row.ambient_dimension
        assert saved_row['protected_rank'] == row.protected_rank
        assert saved_row['observation_rank'] == row.observation_rank
        assert saved_row['exact_count'] == row.exact_count
        assert saved_row['fail_count'] == row.fail_count

    candidate_library = candidate_library_budget_report((3, 4, 5))
    saved_candidate_library = data['candidate_library_budget']
    assert saved_candidate_library['witness_count'] == candidate_library.witness_count
    assert saved_candidate_library['all_levels_have_exact_and_fail'] == candidate_library.all_levels_have_exact_and_fail
    assert len(saved_candidate_library['rows']) == len(candidate_library.rows)
    for saved_row, row in zip(saved_candidate_library['rows'], candidate_library.rows, strict=True):
        assert saved_row['ambient_dimension'] == row.ambient_dimension
        assert saved_row['protected_rank'] == row.protected_rank
        assert saved_row['selection_size'] == row.selection_size
        assert saved_row['exact_count'] == row.exact_count
        assert saved_row['fail_count'] == row.fail_count
        assert tuple(saved_row['exact_subset']) == row.exact_subset
        assert tuple(saved_row['fail_subset']) == row.fail_subset
        assert np.isclose(saved_row['exact_total_cost'], row.exact_total_cost)
        assert np.isclose(saved_row['fail_total_cost'], row.fail_total_cost)

    noisy = noisy_restricted_linear_target_hierarchy_report(
        np.array(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 1.0],
            ],
            dtype=float,
        ),
        np.array([[0.0, 1.0, 1.0]], dtype=float),
        np.array([[0.0, 0.0, 1.0]], dtype=float),
        noise_radii=(0.0, 0.25, 0.5, 1.0),
        box_radius=1.0,
    )
    saved_noisy = data['noisy_restricted_linear_target_hierarchy']
    assert saved_noisy['weak_exact_recoverable'] == noisy.weak_exact_recoverable
    assert saved_noisy['strong_exact_recoverable'] == noisy.strong_exact_recoverable
    assert saved_noisy['detectable_only'] == noisy.detectable_only
    assert np.isclose(saved_noisy['weak_decoder_operator_norm'], noisy.weak_decoder_operator_norm)
    assert np.isclose(saved_noisy['strong_collision_gap'], noisy.strong_collision_gap)
    assert np.isclose(saved_noisy['strong_uniform_lower_bound'], noisy.strong_uniform_lower_bound)
    assert np.isclose(saved_noisy['weak_discrete_collision_gap'], noisy.weak_discrete_collision_gap)
    assert np.isclose(saved_noisy['strong_discrete_collision_gap'], noisy.strong_discrete_collision_gap)
    for saved_row, row in zip(saved_noisy['rows'], noisy.rows, strict=True):
        assert np.isclose(saved_row['noise_radius'], row.noise_radius)
        assert np.isclose(saved_row['weak_upper_bound'], row.weak_upper_bound)
        assert np.isclose(saved_row['weak_bruteforce_max_error'], row.weak_bruteforce_max_error)
        assert np.isclose(saved_row['strong_uniform_lower_bound'], row.strong_uniform_lower_bound)
        assert np.isclose(saved_row['strong_discrete_collision_gap'], row.strong_discrete_collision_gap)
        assert saved_row['separated'] == row.separated

    fiber_geometry = restricted_linear_fiber_geometry_report(
        np.array(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 1.0],
            ],
            dtype=float,
        ),
        np.array([[0.0, 0.0, 1.0]], dtype=float),
        box_radius=1.0,
    )
    saved_geometry = data['restricted_linear_fiber_geometry']
    assert saved_geometry['coefficient_dimension'] == fiber_geometry.coefficient_dimension
    assert saved_geometry['observation_rank'] == fiber_geometry.observation_rank
    assert saved_geometry['fiber_dimension'] == fiber_geometry.fiber_dimension
    assert saved_geometry['exact_recoverable'] == fiber_geometry.exact_recoverable
    assert saved_geometry['target_mixed_fiber'] == fiber_geometry.target_mixed_fiber
    assert np.isclose(saved_geometry['rowspace_residual'], fiber_geometry.rowspace_residual)
    assert np.isclose(saved_geometry['collision_gap'], fiber_geometry.collision_gap)

    family_enlargement = restricted_linear_family_enlargement_report(
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
    saved_enlargement = data['family_enlargement_false_positive']
    assert saved_enlargement['small_family_dimension'] == family_enlargement.small_family_dimension
    assert saved_enlargement['large_family_dimension'] == family_enlargement.large_family_dimension
    assert np.isclose(saved_enlargement['inclusion_residual'], family_enlargement.inclusion_residual)
    assert saved_enlargement['small_exact_recoverable'] == family_enlargement.small_exact_recoverable
    assert saved_enlargement['large_exact_recoverable'] == family_enlargement.large_exact_recoverable
    assert np.isclose(saved_enlargement['small_rowspace_residual'], family_enlargement.small_rowspace_residual)
    assert np.isclose(saved_enlargement['large_rowspace_residual'], family_enlargement.large_rowspace_residual)
    assert np.isclose(saved_enlargement['small_collision_gap'], family_enlargement.small_collision_gap)
    assert np.isclose(saved_enlargement['large_collision_gap'], family_enlargement.large_collision_gap)
    assert saved_enlargement['false_positive_risk'] == family_enlargement.false_positive_risk
    assert np.isclose(saved_enlargement['larger_family_impossibility_lower_bound'], family_enlargement.larger_family_impossibility_lower_bound)
    assert np.isclose(saved_enlargement['reference_decoder_max_error_on_large_family'], family_enlargement.reference_decoder_max_error_on_large_family)
    assert np.isclose(saved_enlargement['reference_decoder_mean_error_on_large_family'], family_enlargement.reference_decoder_mean_error_on_large_family)

    model_mismatch = restricted_linear_model_mismatch_report(
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
    saved_model_mismatch = data['model_mismatch_stress']
    assert saved_model_mismatch['reference_exact_recoverable'] == model_mismatch.reference_exact_recoverable
    assert saved_model_mismatch['reference_family_dimension'] == model_mismatch.reference_family_dimension
    assert np.isclose(saved_model_mismatch['reference_decoder_operator_norm'], model_mismatch.reference_decoder_operator_norm)
    for saved_row, row in zip(saved_model_mismatch['rows'], model_mismatch.rows, strict=True):
        assert saved_row['label'] == row.label
        assert saved_row['family_dimension'] == row.family_dimension
        assert np.isclose(saved_row['subspace_distance'], row.subspace_distance)
        assert saved_row['exact_recoverable_under_true_family'] == row.exact_recoverable_under_true_family
        assert np.isclose(saved_row['rowspace_residual'], row.rowspace_residual)
        assert np.isclose(saved_row['collision_gap'], row.collision_gap)
        assert np.isclose(saved_row['reference_decoder_max_error'], row.reference_decoder_max_error)
        assert np.isclose(saved_row['reference_decoder_mean_error'], row.reference_decoder_mean_error)

    canonical_model_mismatch = canonical_model_mismatch_report(1.0, beta_values=(0.5, 1.0, 2.0))
    saved_canonical_mismatch = data['canonical_model_mismatch']
    assert np.isclose(saved_canonical_mismatch['beta_reference'], canonical_model_mismatch.beta_reference)
    assert saved_canonical_mismatch['reference_exact_recoverable'] == canonical_model_mismatch.reference_exact_recoverable
    assert np.isclose(saved_canonical_mismatch['reference_decoder_operator_norm'], canonical_model_mismatch.reference_decoder_operator_norm)
    for saved_row, row in zip(saved_canonical_mismatch['rows'], canonical_model_mismatch.rows, strict=True):
        assert np.isclose(saved_row['beta_true'], row.beta_true)
        assert np.isclose(saved_row['beta_reference'], row.beta_reference)
        assert saved_row['exact_recoverable_true_family'] == row.exact_recoverable_true_family
        assert np.isclose(saved_row['subspace_distance'], row.subspace_distance)
        assert np.isclose(saved_row['formula_max_error'], row.formula_max_error)
        assert np.isclose(saved_row['brute_force_max_error'], row.brute_force_max_error)
        assert np.isclose(saved_row['brute_force_mean_error'], row.brute_force_mean_error)

    periodic_refinement = periodic_modal_refinement_report()
    saved_periodic_refinement = data['periodic_refinement_false_positive']
    assert saved_periodic_refinement['cutoff'] == periodic_refinement.cutoff
    assert saved_periodic_refinement['coarse_mode_count'] == periodic_refinement.coarse_mode_count
    assert saved_periodic_refinement['refined_mode_count'] == periodic_refinement.refined_mode_count
    assert saved_periodic_refinement['coarse_exact_recoverable'] == periodic_refinement.coarse_exact_recoverable
    assert saved_periodic_refinement['refined_exact_recoverable'] == periodic_refinement.refined_exact_recoverable
    assert np.isclose(saved_periodic_refinement['coarse_collision_gap'], periodic_refinement.coarse_collision_gap)
    assert np.isclose(saved_periodic_refinement['refined_collision_gap'], periodic_refinement.refined_collision_gap)
    assert saved_periodic_refinement['refinement_false_positive_risk'] == periodic_refinement.refinement_false_positive_risk
    assert np.isclose(saved_periodic_refinement['refined_family_impossibility_lower_bound'], periodic_refinement.refined_family_impossibility_lower_bound)
    assert np.isclose(saved_periodic_refinement['coarse_decoder_max_error_on_refined_family'], periodic_refinement.coarse_decoder_max_error_on_refined_family)
    assert np.isclose(saved_periodic_refinement['coarse_decoder_mean_error_on_refined_family'], periodic_refinement.coarse_decoder_mean_error_on_refined_family)

    periodic = periodic_functional_complexity_sweep(n=14, cutoffs=(2,), delta_count=6)
    periodic_rows = {row['functional_name']: row for row in periodic['rows']}
    saved_periodic = data['periodic_same_record_target_hierarchy']['rows']
    for name, row in periodic_rows.items():
        saved = saved_periodic[name]
        assert saved['exact_recoverable'] == row['exact_recoverable']
        assert saved['predicted_min_cutoff'] == row['predicted_min_cutoff']
        assert np.isclose(saved['collision_max_protected_distance'], row['collision_max_protected_distance'])
        assert np.isclose(saved['mean_recovery_error'], row['mean_recovery_error'])

    control = functional_observability_sweep(epsilon_values=(0.2,), horizons=(1, 2))
    control_rows = {(row['epsilon'], row['horizon']): row for row in control['rows']}
    saved_control = data['control_exact_vs_asymptotic_split']
    assert saved_control['one_step']['exact_recoverable'] == control_rows[(0.2, 1)]['exact_recoverable']
    assert saved_control['two_step']['exact_recoverable'] == control_rows[(0.2, 2)]['exact_recoverable']
    assert np.isclose(saved_control['one_step']['collision_max_protected_distance'], control_rows[(0.2, 1)]['collision_max_protected_distance'])
    assert np.isclose(saved_control['two_step']['max_recovery_error'], control_rows[(0.2, 2)]['max_recovery_error'])
    assert np.isclose(saved_control['observer']['spectral_radius'], control['observer_reports'][0]['spectral_radius'])

    control_hierarchy = control_regime_hierarchy_report(0.2)
    saved_control_hierarchy = data['control_regime_hierarchy']
    assert np.isclose(saved_control_hierarchy['epsilon'], control_hierarchy.epsilon)
    assert saved_control_hierarchy['one_step_exact_recoverable'] == control_hierarchy.one_step_exact_recoverable
    assert saved_control_hierarchy['two_step_exact_recoverable'] == control_hierarchy.two_step_exact_recoverable
    assert saved_control_hierarchy['observer_asymptotic_recoverable'] == control_hierarchy.observer_asymptotic_recoverable
    assert np.isclose(saved_control_hierarchy['one_step_collision_gap'], control_hierarchy.one_step_collision_gap)
    assert np.isclose(saved_control_hierarchy['two_step_collision_gap'], control_hierarchy.two_step_collision_gap)
    assert np.isclose(saved_control_hierarchy['observer_spectral_radius'], control_hierarchy.observer_spectral_radius)
    assert np.isclose(saved_control_hierarchy['observer_final_protected_error'], control_hierarchy.observer_final_protected_error)
