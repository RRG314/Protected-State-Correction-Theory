from __future__ import annotations

"""Context-invariant recoverability diagnostics (exploration / candidate layer).

This module studies a stricter regime than standard restricted-linear
recoverability: a *single* decoder must work across multiple observation
contexts. It is intended for candidate-lane extraction and validation, not for
automatic theorem promotion.
"""

from dataclasses import dataclass
from itertools import combinations
from typing import Sequence

import numpy as np

from .recoverability import EPS, restricted_linear_recoverability

Array = np.ndarray


@dataclass(frozen=True)
class ContextInvariantRecoverabilityReport:
    context_count: int
    record_dimension: int
    coefficient_dimension: int
    target_dimension: int
    per_context_exact_flags: tuple[bool, ...]
    conditioned_exact: bool
    invariant_exact: bool
    invariant_residual_fro: float
    invariant_residual_max_context: float
    common_decoder: Array | None
    system_matrix_rank: int
    system_rows: int
    system_cols: int


@dataclass(frozen=True)
class SharedAugmentationSearchReport:
    minimal_shared_rows: int | None
    successful_row_indices: tuple[int, ...] | None
    search_limit: int
    invariant_exact_after_augmentation: bool


def _as_matrix(matrix: Array) -> Array:
    arr = np.asarray(matrix, dtype=float)
    if arr.ndim == 1:
        arr = arr[None, :]
    return arr


def _build_linear_system(
    context_matrices: Sequence[Array],
    target_matrix: Array,
) -> tuple[Array, Array, int, int]:
    A = [_as_matrix(matrix) for matrix in context_matrices]
    if not A:
        raise ValueError("context_matrices must be nonempty")
    p = A[0].shape[0]
    d = A[0].shape[1]
    for matrix in A:
        if matrix.shape[0] != p:
            raise ValueError("all context matrices must have the same record dimension")
        if matrix.shape[1] != d:
            raise ValueError("all context matrices must have the same coefficient dimension")

    L = _as_matrix(target_matrix)
    if L.shape[1] != d:
        raise ValueError("target_matrix coefficient dimension must match context matrices")
    q = L.shape[0]

    blocks = []
    rhs = []
    eye_q = np.eye(q, dtype=float)
    for matrix in A:
        blocks.append(np.kron(matrix.T, eye_q))
        rhs.append(L.reshape(-1, order="F"))
    M = np.vstack(blocks)
    b = np.concatenate(rhs)
    return M, b, p, q


def context_invariant_recoverability(
    context_matrices: Sequence[Array],
    target_matrix: Array,
    *,
    tol: float = EPS,
) -> ContextInvariantRecoverabilityReport:
    contexts = [_as_matrix(matrix) for matrix in context_matrices]
    target = _as_matrix(target_matrix)
    per_context_exact: list[bool] = []
    for matrix in contexts:
        rep = restricted_linear_recoverability(matrix, target, tol=tol)
        per_context_exact.append(bool(rep.exact_recoverable))
    conditioned_exact = bool(all(per_context_exact))

    M, b, p, q = _build_linear_system(contexts, target)
    solution, *_ = np.linalg.lstsq(M, b, rcond=None)
    residual = M @ solution - b
    residual_fro = float(np.linalg.norm(residual))
    decoder = solution.reshape((q, p), order="F")
    context_residuals = [float(np.linalg.norm(decoder @ matrix - target, ord="fro")) for matrix in contexts]
    residual_max_context = float(max(context_residuals)) if context_residuals else 0.0
    invariant_exact = bool(residual_max_context <= tol)
    rank = int(np.linalg.matrix_rank(M, tol))

    return ContextInvariantRecoverabilityReport(
        context_count=len(contexts),
        record_dimension=p,
        coefficient_dimension=contexts[0].shape[1],
        target_dimension=q,
        per_context_exact_flags=tuple(per_context_exact),
        conditioned_exact=conditioned_exact,
        invariant_exact=invariant_exact,
        invariant_residual_fro=residual_fro,
        invariant_residual_max_context=residual_max_context,
        common_decoder=None if not invariant_exact else decoder,
        system_matrix_rank=rank,
        system_rows=int(M.shape[0]),
        system_cols=int(M.shape[1]),
    )


def minimal_shared_augmentation(
    context_matrices: Sequence[Array],
    target_matrix: Array,
    candidate_rows: Sequence[Array],
    *,
    max_shared_rows: int | None = None,
    tol: float = EPS,
) -> SharedAugmentationSearchReport:
    contexts = [_as_matrix(matrix) for matrix in context_matrices]
    if not contexts:
        raise ValueError("context_matrices must be nonempty")
    row_candidates = [_as_matrix(row) for row in candidate_rows]
    if not row_candidates:
        rep = context_invariant_recoverability(contexts, target_matrix, tol=tol)
        return SharedAugmentationSearchReport(
            minimal_shared_rows=0 if rep.invariant_exact else None,
            successful_row_indices=() if rep.invariant_exact else None,
            search_limit=0,
            invariant_exact_after_augmentation=rep.invariant_exact,
        )

    if max_shared_rows is None:
        max_shared_rows = len(row_candidates)

    # First test unaugmented.
    base = context_invariant_recoverability(contexts, target_matrix, tol=tol)
    if base.invariant_exact:
        return SharedAugmentationSearchReport(
            minimal_shared_rows=0,
            successful_row_indices=(),
            search_limit=max_shared_rows,
            invariant_exact_after_augmentation=True,
        )

    for added in range(1, max_shared_rows + 1):
        for combo in combinations(range(len(row_candidates)), added):
            shared = np.vstack([row_candidates[index] for index in combo])
            augmented = [np.vstack([matrix, shared]) for matrix in contexts]
            rep = context_invariant_recoverability(augmented, target_matrix, tol=tol)
            if rep.invariant_exact:
                return SharedAugmentationSearchReport(
                    minimal_shared_rows=added,
                    successful_row_indices=tuple(int(index) for index in combo),
                    search_limit=max_shared_rows,
                    invariant_exact_after_augmentation=True,
                )
    return SharedAugmentationSearchReport(
        minimal_shared_rows=None,
        successful_row_indices=None,
        search_limit=max_shared_rows,
        invariant_exact_after_augmentation=False,
    )


def context_invariant_rank_descriptor(context_matrices: Sequence[Array], target_matrix: Array) -> dict[str, int]:
    contexts = [_as_matrix(matrix) for matrix in context_matrices]
    target = _as_matrix(target_matrix)
    if not contexts:
        raise ValueError("context_matrices must be nonempty")
    descriptor = {
        "context_count": len(contexts),
        "record_dimension": int(contexts[0].shape[0]),
        "coefficient_dimension": int(contexts[0].shape[1]),
        "target_rank": int(np.linalg.matrix_rank(target)),
        "total_observation_rank": int(np.linalg.matrix_rank(np.vstack(contexts))),
    }
    for index, matrix in enumerate(contexts):
        descriptor[f"context_{index + 1}_rank"] = int(np.linalg.matrix_rank(matrix))
    return descriptor


__all__ = [
    "ContextInvariantRecoverabilityReport",
    "SharedAugmentationSearchReport",
    "context_invariant_rank_descriptor",
    "context_invariant_recoverability",
    "minimal_shared_augmentation",
]

