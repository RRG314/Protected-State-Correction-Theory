from __future__ import annotations

import numpy as np

from ocp.design import (
    linear_recoverability_design_report,
    minimal_candidate_augmentation,
    recoverable_protected_rows,
    restricted_row_space_residuals,
)


def test_row_space_residuals_detect_recoverable_and_unrecoverable_rows() -> None:
    observation = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ]
    )
    protected = np.array(
        [
            [0.0, 1.0, 1.0],
            [0.0, 0.0, 1.0],
        ]
    )
    residuals = restricted_row_space_residuals(observation, protected)
    assert residuals[0] < 1e-10
    assert residuals[1] > 0.5

    recoverable, unrecoverable, residuals_check = recoverable_protected_rows(observation, protected)
    assert recoverable == (0,)
    assert unrecoverable == (1,)
    assert np.allclose(residuals, residuals_check)


def test_minimal_candidate_augmentation_finds_single_measurement_fix() -> None:
    observation = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ]
    )
    protected = np.array(
        [
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    candidates = [
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([1.0, 1.0, 0.0]),
    ]
    report = minimal_candidate_augmentation(observation, protected, candidates, max_added_measurements=2)
    assert report.minimal_added_measurements == 1
    assert set(report.candidate_exact_sets) == {(0,), (1,), (2,)}


def test_design_report_exposes_nullspace_witness_and_minimal_fix() -> None:
    observation = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ]
    )
    protected = np.array([[0.0, 0.0, 1.0]])
    candidates = [
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([1.0, 1.0, 0.0]),
    ]
    report = linear_recoverability_design_report(observation, protected, candidate_rows=candidates)
    assert report.exact_recoverable is False
    assert report.recoverable_row_indices == ()
    assert report.unrecoverable_row_indices == (0,)
    assert report.nullspace_witness is not None
    assert report.nullspace_protected_gap > 0.5
    assert report.minimal_added_measurements == 1
    assert set(report.candidate_exact_sets) == {(0,), (1,), (2,)}


def test_design_report_respects_family_basis_restriction() -> None:
    observation = np.array([[1.0, 0.0, 0.0]])
    protected = np.array([[0.0, 0.0, 1.0]])
    family_basis = np.array(
        [
            [1.0, 0.0],
            [0.0, 0.0],
            [0.0, 1.0],
        ]
    )
    candidates = [np.array([0.0, 0.0, 1.0])]
    report = linear_recoverability_design_report(
        observation,
        protected,
        candidate_rows=candidates,
        family_basis=family_basis,
    )
    assert report.exact_recoverable is False
    assert report.rank_observation == 1
    assert report.rank_protected == 1
    assert report.minimal_added_measurements == 1

    fixed = linear_recoverability_design_report(
        np.vstack([observation, candidates[0]]),
        protected,
        family_basis=family_basis,
    )
    assert fixed.exact_recoverable is True
    assert fixed.unrecoverable_row_indices == ()
