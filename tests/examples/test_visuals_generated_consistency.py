from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from ocp.visuals import (
    alignment_landscape_data,
    augmentation_direction_scan_data,
    contamination_sweep_visual_data,
    core_geometry_data,
    dynamic_rate_visual_data,
    family_enlargement_visual_data,
    minimal_augmentation_data,
    perturbation_fragility_data,
    recoverability_transition_data,
    same_rank_data,
    threshold_surfaces_data,
)

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')


def _load_summary() -> dict[str, object]:
    path = ROOT / 'data/generated/visuals/visual_summary.json'
    if not path.exists():
        pytest.skip(f'missing generated artifact: {path}')
    return json.loads(path.read_text(encoding='utf-8'))


def test_generated_visual_summary_matches_current_core_examples() -> None:
    data = _load_summary()

    core_saved = data['A_core_geometry']
    core_now = core_geometry_data()
    assert np.isclose(core_saved['exact_2d']['projection_error_norm'], core_now['exact_2d']['projection_error_norm'])
    assert np.isclose(core_saved['misaligned_2d']['projection_error_norm'], core_now['misaligned_2d']['projection_error_norm'])
    assert core_saved['overlap_3d']['intersection_dimension'] == core_now['overlap_3d']['intersection_dimension']

    same_saved = data['D_same_rank']
    same_now = same_rank_data()
    assert same_saved['rank_exact'] == same_now['rank_exact']
    assert same_saved['rank_fail'] == same_now['rank_fail']
    assert np.isclose(same_saved['exact_rowspace_residual'], same_now['exact_rowspace_residual'])
    assert np.isclose(same_saved['fail_rowspace_residual'], same_now['fail_rowspace_residual'])

    aug_saved = data['E_minimal_augmentation']
    aug_now = minimal_augmentation_data()
    assert aug_saved['delta_formula'] == aug_now['delta_formula']
    assert aug_saved['exact_before'] == aug_now['exact_before']
    assert aug_saved['exact_after'] == aug_now['exact_after']
    assert np.isclose(aug_saved['residual_before'], aug_now['residual_before'])
    assert np.isclose(aug_saved['residual_after'], aug_now['residual_after'])


def test_generated_visual_summary_matches_transition_and_threshold_regimes() -> None:
    data = _load_summary()

    trans_saved = data['C_transition']
    trans_now = recoverability_transition_data()
    assert np.isclose(trans_saved['exact_to_impossible_threshold_alpha'], trans_now['exact_to_impossible_threshold_alpha'])
    assert trans_saved['rows'][-1]['exact_recoverable'] == trans_now['rows'][-1]['exact_recoverable']
    assert trans_saved['rows'][-1]['fiber_count'] == trans_now['rows'][-1]['fiber_count']

    thresh_saved = data['G_threshold_surfaces']
    thresh_now = threshold_surfaces_data()
    assert thresh_saved['control_surface']['regime_matrix'] == thresh_now['control_surface']['regime_matrix']
    assert thresh_saved['noise_surface']['regime_matrix'] == thresh_now['noise_surface']['regime_matrix']

    align_saved = data['I_alignment_landscape']
    align_now = alignment_landscape_data()
    assert np.isclose(align_saved['exact_fraction'], align_now['exact_fraction'])
    assert np.isclose(
        np.asarray(align_saved['rowspace_residual_matrix'], dtype=float).max(),
        np.asarray(align_now['rowspace_residual_matrix'], dtype=float).max(),
    )

    perturb_saved = data['J_perturbation_fragility']
    perturb_now = perturbation_fragility_data()
    assert perturb_saved['center_index'] == perturb_now['center_index']
    assert np.isclose(
        np.asarray(perturb_saved['rowspace_residual_matrix'], dtype=float).max(),
        np.asarray(perturb_now['rowspace_residual_matrix'], dtype=float).max(),
    )

    family_saved = data['K_family_enlargement']
    family_now = family_enlargement_visual_data()
    assert family_saved['small_family']['exact_recoverable'] == family_now['small_family']['exact_recoverable']
    assert family_saved['enlarged_family']['exact_recoverable'] == family_now['enlarged_family']['exact_recoverable']
    assert np.isclose(family_saved['enlarged_family']['collision_gap'], family_now['enlarged_family']['collision_gap'])

    dynamic_saved = data['L_dynamic_rates']
    dynamic_now = dynamic_rate_visual_data()
    assert dynamic_saved['exact_matrix'] == dynamic_now['exact_matrix']
    assert np.allclose(
        np.asarray(dynamic_saved['recoverability_margin_matrix'], dtype=float),
        np.asarray(dynamic_now['recoverability_margin_matrix'], dtype=float),
    )

    augment_saved = data['M_augmentation_direction_scan']
    augment_now = augmentation_direction_scan_data()
    assert augment_saved['exact_flags'] == augment_now['exact_flags']
    assert np.allclose(
        np.asarray(augment_saved['rowspace_residuals'], dtype=float),
        np.asarray(augment_now['rowspace_residuals'], dtype=float),
    )

    contamination_saved = data['N_contamination_sweep']
    contamination_now = contamination_sweep_visual_data()
    assert contamination_saved['contamination_values'] == contamination_now['contamination_values']
    assert np.allclose(
        np.asarray([row['bounded_boundary_normal_projected_rms'] for row in contamination_saved['rows']], dtype=float),
        np.asarray([row['bounded_boundary_normal_projected_rms'] for row in contamination_now['rows']], dtype=float),
    )
