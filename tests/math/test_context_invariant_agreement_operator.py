from __future__ import annotations

import numpy as np

from ocp.context_invariant import (
    agreement_lift_matrix,
    agreement_operator_recoverability,
    candidate_library_recoverability,
    context_invariant_recoverability,
    minimal_shared_augmentation,
    unconstrained_shared_augmentation_threshold,
)
from ocp.recoverability import restricted_linear_recoverability


def _random_invertible(rng: np.random.Generator, size: int) -> np.ndarray:
    while True:
        matrix = rng.integers(-3, 4, size=(size, size)).astype(float)
        if abs(np.linalg.det(matrix)) > 1e-6:
            return matrix


def _random_full_row_rank(rng: np.random.Generator, rows: int, cols: int) -> np.ndarray:
    while True:
        matrix = rng.integers(-3, 4, size=(rows, cols)).astype(float)
        if np.linalg.matrix_rank(matrix) == rows:
            return matrix


def _latent_family(
    rng: np.random.Generator,
    *,
    record_dimension: int = 4,
    coefficient_dimension: int = 6,
    target_dimension: int = 2,
    context_count: int = 3,
) -> tuple[np.ndarray, list[np.ndarray]]:
    base = _random_full_row_rank(rng, record_dimension, coefficient_dimension)
    selector = np.hstack([np.eye(target_dimension), np.zeros((target_dimension, record_dimension - target_dimension))])
    target = selector @ base
    contexts = []
    for _ in range(context_count):
        a = _random_invertible(rng, record_dimension)
        contexts.append(a @ base)
    return target, contexts


def _rank(matrix: np.ndarray) -> int:
    if matrix.size == 0:
        return 0
    return int(np.linalg.matrix_rank(matrix))


def test_agreement_operator_matches_direct_invariant_exactness() -> None:
    rng = np.random.default_rng(20260418)
    for _ in range(120):
        target, contexts = _latent_family(rng)
        direct = context_invariant_recoverability(contexts, target)
        agreement = agreement_operator_recoverability(contexts, target)
        assert agreement.lift_direct_consistent
        assert agreement.invariant_exact_direct == direct.invariant_exact
        assert agreement.invariant_exact_via_agreement == direct.invariant_exact


def test_unconstrained_shared_augmentation_threshold_constructs_exact_repair() -> None:
    rng = np.random.default_rng(20260419)
    for _ in range(80):
        target, contexts = _latent_family(rng, context_count=4)
        lift = agreement_lift_matrix(contexts)
        threshold = unconstrained_shared_augmentation_threshold(contexts, target)

        expected = int(_rank(np.vstack([lift, target])) - _rank(lift))
        assert threshold.minimal_shared_rows_free == expected
        assert threshold.constructed_shared_rows.shape[0] == expected
        assert threshold.invariant_exact_after_constructed

        if threshold.invariant_exact_before:
            assert threshold.minimal_shared_rows_free == 0
        else:
            assert threshold.minimal_shared_rows_free >= 1


def test_restricted_search_never_beats_unconstrained_threshold() -> None:
    rng = np.random.default_rng(20260420)
    for _ in range(70):
        target, contexts = _latent_family(rng, context_count=3)
        free = unconstrained_shared_augmentation_threshold(contexts, target).minimal_shared_rows_free

        # Candidate pool intentionally restricted to measured rows and standard basis rows.
        candidates = []
        for context in contexts:
            for row in context[:2]:
                candidates.append(row)
        for i in range(min(target.shape[1], 3)):
            e = np.zeros(target.shape[1], dtype=float)
            e[i] = 1.0
            candidates.append(e)

        restricted = minimal_shared_augmentation(contexts, target, candidates, max_shared_rows=3)
        if restricted.minimal_shared_rows is not None:
            assert restricted.minimal_shared_rows >= free


def test_lift_solver_equivalence_to_restricted_linear_recoverability() -> None:
    rng = np.random.default_rng(20260421)
    for _ in range(60):
        target, contexts = _latent_family(rng)
        lift = agreement_lift_matrix(contexts)
        lift_rep = restricted_linear_recoverability(lift, target)
        agreement = agreement_operator_recoverability(contexts, target)
        assert bool(lift_rep.exact_recoverable) == agreement.invariant_exact_via_agreement


def test_candidate_library_defect_matches_full_pool_exactness() -> None:
    rng = np.random.default_rng(20260422)
    for _ in range(100):
        target, contexts = _latent_family(rng, context_count=4)
        candidates = []
        for context in contexts:
            candidates.extend(context[:2])
        report = candidate_library_recoverability(
            contexts,
            target,
            candidates,
            max_search_rows=3,
        )
        assert report.full_pool_feasible == report.invariant_exact_with_full_pool
        assert report.library_target_defect >= 0
        assert report.library_rank_gain >= 0
        assert report.free_threshold >= 0


def test_positive_library_defect_blocks_recovery_for_that_library() -> None:
    rng = np.random.default_rng(20260423)
    hits = 0
    for _ in range(140):
        target, contexts = _latent_family(rng, context_count=4)
        lift = agreement_lift_matrix(contexts)
        if _rank(np.vstack([lift, target])) == _rank(lift):
            continue
        candidate_rows = [row.copy() for row in lift[: min(2, lift.shape[0])]]
        report = candidate_library_recoverability(
            contexts,
            target,
            candidate_rows,
            max_search_rows=max(1, len(candidate_rows)),
        )
        if report.library_target_defect > 0:
            hits += 1
            assert not report.full_pool_feasible
            assert not report.invariant_exact_with_full_pool
            assert not report.found_within_limit
    assert hits >= 15


def test_library_rank_gain_is_not_sufficient_for_exactness() -> None:
    # Deterministic construction:
    # G = span(e1), target requires one missing direction e2 (free threshold = 1),
    # candidate contributes e3 (same rank gain but wrong direction).
    contexts = [
        np.array([[1.0, 0.0, 0.0, 0.0]]),
        np.array([[1.0, 0.0, 0.0, 0.0]]),
    ]
    target = np.array([[1.0, 1.0, 0.0, 0.0]])
    candidates = [np.array([0.0, 0.0, 1.0, 0.0])]

    report = candidate_library_recoverability(
        contexts,
        target,
        candidates,
        max_search_rows=1,
    )

    assert report.free_threshold == 1
    assert report.library_rank_gain == 1
    assert report.library_target_defect == 1
    assert not report.full_pool_feasible
    assert not report.invariant_exact_with_full_pool
