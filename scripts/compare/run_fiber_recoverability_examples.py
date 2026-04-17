#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from dataclasses import asdict, is_dataclass
from pathlib import Path

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
OUT = ROOT / 'data/generated/unified-recoverability'


def _serialize(value):
    if is_dataclass(value):
        return {key: _serialize(item) for key, item in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): _serialize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_serialize(item) for item in value]
    return value


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    canonical = canonical_detectable_only_examples()
    rank_only = rank_only_classifier_failure_report((3, 4, 5, 6))
    coordinate_enumeration = coordinate_rank_enumeration_report((3, 4, 5))
    candidate_library = candidate_library_budget_report((3, 4, 5))
    noisy_hierarchy = noisy_restricted_linear_target_hierarchy_report(
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
    canonical_model_mismatch = canonical_model_mismatch_report(
        1.0,
        beta_values=(0.5, 1.0, 2.0),
    )
    periodic_refinement = periodic_modal_refinement_report()
    control_hierarchy = control_regime_hierarchy_report(0.2)

    periodic = periodic_functional_complexity_sweep(n=14, cutoffs=(2,), delta_count=6)
    periodic_rows = {row['functional_name']: row for row in periodic['rows']}

    control = functional_observability_sweep(epsilon_values=(0.2,), horizons=(1, 2))
    control_rows = {(row['epsilon'], row['horizon']): row for row in control['rows']}
    control_observer = control['observer_reports'][0]

    summary = {
        'canonical_detectable_only_examples': _serialize(canonical),
        'rank_only_classifier_failure': {
            'witness_count': rank_only.witness_count,
            'all_same_rank': rank_only.all_same_rank,
            'all_opposite_verdicts': rank_only.all_opposite_verdicts,
            'rows': _serialize(rank_only.rows),
        },
        'coordinate_rank_enumeration': {
            'all_levels_have_exact_and_fail': coordinate_enumeration.all_levels_have_exact_and_fail,
            'rows': _serialize(coordinate_enumeration.rows),
        },
        'candidate_library_budget': {
            'witness_count': candidate_library.witness_count,
            'all_levels_have_exact_and_fail': candidate_library.all_levels_have_exact_and_fail,
            'rows': _serialize(candidate_library.rows),
        },
        'noisy_restricted_linear_target_hierarchy': _serialize(noisy_hierarchy),
        'restricted_linear_fiber_geometry': _serialize(fiber_geometry),
        'family_enlargement_false_positive': _serialize(family_enlargement),
        'model_mismatch_stress': _serialize(model_mismatch),
        'canonical_model_mismatch': _serialize(canonical_model_mismatch),
        'periodic_refinement_false_positive': _serialize(periodic_refinement),
        'periodic_same_record_target_hierarchy': {
            'cutoff': 2,
            'rows': {
                name: {
                    'exact_recoverable': row['exact_recoverable'],
                    'predicted_min_cutoff': row['predicted_min_cutoff'],
                    'collision_max_protected_distance': row['collision_max_protected_distance'],
                    'mean_recovery_error': row['mean_recovery_error'],
                }
                for name, row in periodic_rows.items()
            },
        },
        'control_exact_vs_asymptotic_split': {
            'epsilon': 0.2,
            'one_step': control_rows[(0.2, 1)],
            'two_step': control_rows[(0.2, 2)],
            'observer': control_observer,
        },
        'control_regime_hierarchy': _serialize(control_hierarchy),
    }

    (OUT / 'unified_recoverability_summary.json').write_text(json.dumps(summary, indent=2))

    write_csv(
        OUT / 'rank_only_classifier_witnesses.csv',
        [
            {
                'ambient_dimension': row.ambient_dimension,
                'protected_rank': row.protected_rank,
                'observation_rank': row.observation_rank,
                'exact_rank_observation': row.exact_rank_observation,
                'fail_rank_observation': row.fail_rank_observation,
                'exact_recoverable': row.exact_recoverable,
                'fail_recoverable': row.fail_recoverable,
                'exact_rowspace_residual': row.exact_rowspace_residual,
                'fail_rowspace_residual': row.fail_rowspace_residual,
                'exact_collision_gap': row.exact_collision_gap,
                'fail_collision_gap': row.fail_collision_gap,
            }
            for row in rank_only.rows
        ],
    )

    write_csv(
        OUT / 'coordinate_rank_enumeration.csv',
        [
            {
                'ambient_dimension': row.ambient_dimension,
                'protected_rank': row.protected_rank,
                'observation_rank': row.observation_rank,
                'exact_count': row.exact_count,
                'fail_count': row.fail_count,
            }
            for row in coordinate_enumeration.rows
        ],
    )

    write_csv(
        OUT / 'candidate_library_budget_witnesses.csv',
        [
            {
                'ambient_dimension': row.ambient_dimension,
                'protected_rank': row.protected_rank,
                'selection_size': row.selection_size,
                'exact_count': row.exact_count,
                'fail_count': row.fail_count,
                'exact_subset': ' '.join(str(index) for index in row.exact_subset),
                'fail_subset': ' '.join(str(index) for index in row.fail_subset),
                'exact_total_cost': row.exact_total_cost,
                'fail_total_cost': row.fail_total_cost,
            }
            for row in candidate_library.rows
        ],
    )

    write_csv(
        OUT / 'noisy_restricted_linear_hierarchy.csv',
        [
            {
                'noise_radius': row.noise_radius,
                'weak_upper_bound': row.weak_upper_bound,
                'weak_bruteforce_max_error': row.weak_bruteforce_max_error,
                'strong_uniform_lower_bound': row.strong_uniform_lower_bound,
                'strong_discrete_collision_gap': row.strong_discrete_collision_gap,
                'separated': row.separated,
            }
            for row in noisy_hierarchy.rows
        ],
    )

    write_csv(
        OUT / 'restricted_linear_fiber_geometry.csv',
        [
            {
                'coefficient_dimension': fiber_geometry.coefficient_dimension,
                'observation_rank': fiber_geometry.observation_rank,
                'fiber_dimension': fiber_geometry.fiber_dimension,
                'exact_recoverable': fiber_geometry.exact_recoverable,
                'target_mixed_fiber': fiber_geometry.target_mixed_fiber,
                'rowspace_residual': fiber_geometry.rowspace_residual,
                'collision_gap': fiber_geometry.collision_gap,
            }
        ],
    )

    write_csv(
        OUT / 'family_enlargement_false_positive.csv',
        [
            {
                'small_family_dimension': family_enlargement.small_family_dimension,
                'large_family_dimension': family_enlargement.large_family_dimension,
                'inclusion_residual': family_enlargement.inclusion_residual,
                'small_exact_recoverable': family_enlargement.small_exact_recoverable,
                'large_exact_recoverable': family_enlargement.large_exact_recoverable,
                'small_rowspace_residual': family_enlargement.small_rowspace_residual,
                'large_rowspace_residual': family_enlargement.large_rowspace_residual,
                'small_collision_gap': family_enlargement.small_collision_gap,
                'large_collision_gap': family_enlargement.large_collision_gap,
                'false_positive_risk': family_enlargement.false_positive_risk,
                'larger_family_impossibility_lower_bound': family_enlargement.larger_family_impossibility_lower_bound,
                'reference_decoder_max_error_on_large_family': family_enlargement.reference_decoder_max_error_on_large_family,
                'reference_decoder_mean_error_on_large_family': family_enlargement.reference_decoder_mean_error_on_large_family,
            }
        ],
    )

    write_csv(
        OUT / 'model_mismatch_stress.csv',
        [
            {
                'label': row.label,
                'family_dimension': row.family_dimension,
                'subspace_distance': row.subspace_distance,
                'exact_recoverable_under_true_family': row.exact_recoverable_under_true_family,
                'rowspace_residual': row.rowspace_residual,
                'collision_gap': row.collision_gap,
                'reference_decoder_max_error': row.reference_decoder_max_error,
                'reference_decoder_mean_error': row.reference_decoder_mean_error,
            }
            for row in model_mismatch.rows
        ],
    )

    write_csv(
        OUT / 'canonical_model_mismatch.csv',
        [
            {
                'beta_true': row.beta_true,
                'beta_reference': row.beta_reference,
                'exact_recoverable_true_family': row.exact_recoverable_true_family,
                'subspace_distance': row.subspace_distance,
                'formula_max_error': row.formula_max_error,
                'brute_force_max_error': row.brute_force_max_error,
                'brute_force_mean_error': row.brute_force_mean_error,
            }
            for row in canonical_model_mismatch.rows
        ],
    )

    write_csv(
        OUT / 'periodic_refinement_false_positive.csv',
        [
            {
                'cutoff': periodic_refinement.cutoff,
                'coarse_mode_count': periodic_refinement.coarse_mode_count,
                'refined_mode_count': periodic_refinement.refined_mode_count,
                'coarse_exact_recoverable': periodic_refinement.coarse_exact_recoverable,
                'refined_exact_recoverable': periodic_refinement.refined_exact_recoverable,
                'coarse_collision_gap': periodic_refinement.coarse_collision_gap,
                'refined_collision_gap': periodic_refinement.refined_collision_gap,
                'refinement_false_positive_risk': periodic_refinement.refinement_false_positive_risk,
                'refined_family_impossibility_lower_bound': periodic_refinement.refined_family_impossibility_lower_bound,
                'coarse_decoder_max_error_on_refined_family': periodic_refinement.coarse_decoder_max_error_on_refined_family,
                'coarse_decoder_mean_error_on_refined_family': periodic_refinement.coarse_decoder_mean_error_on_refined_family,
            }
        ],
    )

    write_csv(
        OUT / 'periodic_same_record_target_hierarchy.csv',
        [
            {
                'functional_name': name,
                'cutoff': 2,
                'exact_recoverable': row['exact_recoverable'],
                'predicted_min_cutoff': row['predicted_min_cutoff'],
                'collision_max_protected_distance': row['collision_max_protected_distance'],
                'mean_recovery_error': row['mean_recovery_error'],
            }
            for name, row in periodic_rows.items()
        ],
    )

    write_csv(
        OUT / 'control_exact_vs_asymptotic_split.csv',
        [
            {
                'mode': 'one_step',
                'epsilon': control_rows[(0.2, 1)]['epsilon'],
                'horizon': control_rows[(0.2, 1)]['horizon'],
                'exact_recoverable': control_rows[(0.2, 1)]['exact_recoverable'],
                'collision_max_protected_distance': control_rows[(0.2, 1)]['collision_max_protected_distance'],
                'max_recovery_error': control_rows[(0.2, 1)]['max_recovery_error'],
                'recoverability_margin': control_rows[(0.2, 1)]['recoverability_margin'],
            },
            {
                'mode': 'two_step',
                'epsilon': control_rows[(0.2, 2)]['epsilon'],
                'horizon': control_rows[(0.2, 2)]['horizon'],
                'exact_recoverable': control_rows[(0.2, 2)]['exact_recoverable'],
                'collision_max_protected_distance': control_rows[(0.2, 2)]['collision_max_protected_distance'],
                'max_recovery_error': control_rows[(0.2, 2)]['max_recovery_error'],
                'recoverability_margin': control_rows[(0.2, 2)]['recoverability_margin'],
            },
            {
                'mode': 'observer',
                'epsilon': control_observer['epsilon'],
                'horizon': len(control_observer['protected_error_history']) - 1,
                'exact_recoverable': False,
                'collision_max_protected_distance': '',
                'max_recovery_error': control_observer['protected_error_history'][-1],
                'recoverability_margin': 1.0 - control_observer['spectral_radius'],
            },
        ],
    )

    write_csv(
        OUT / 'control_regime_hierarchy.csv',
        [
            {
                'epsilon': control_hierarchy.epsilon,
                'one_step_exact_recoverable': control_hierarchy.one_step_exact_recoverable,
                'two_step_exact_recoverable': control_hierarchy.two_step_exact_recoverable,
                'observer_asymptotic_recoverable': control_hierarchy.observer_asymptotic_recoverable,
                'one_step_collision_gap': control_hierarchy.one_step_collision_gap,
                'two_step_collision_gap': control_hierarchy.two_step_collision_gap,
                'observer_spectral_radius': control_hierarchy.observer_spectral_radius,
                'observer_final_protected_error': control_hierarchy.observer_final_protected_error,
            }
        ],
    )

    print(f'wrote {(OUT / "unified_recoverability_summary.json")}')


if __name__ == '__main__':
    main()
