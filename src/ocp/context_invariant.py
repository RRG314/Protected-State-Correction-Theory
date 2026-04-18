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


@dataclass(frozen=True)
class AgreementOperatorRecoverabilityReport:
    context_count: int
    record_dimension: int
    coefficient_dimension: int
    target_dimension: int
    agreement_basis_dimension: int
    lifted_matrix_rank: int
    lifted_residual_norm: float
    invariant_exact_via_agreement: bool
    invariant_exact_direct: bool
    lift_direct_consistent: bool


@dataclass(frozen=True)
class UnconstrainedSharedAugmentationReport:
    minimal_shared_rows_free: int
    lifted_matrix_rank: int
    target_augmented_rank: int
    invariant_exact_before: bool
    invariant_exact_after_constructed: bool
    constructed_shared_rows: Array


@dataclass(frozen=True)
class CandidateLibraryRecoverabilityReport:
    candidate_count: int
    free_threshold: int
    library_rank_gain: int
    library_target_defect: int
    full_pool_feasible: bool
    invariant_exact_with_full_pool: bool
    minimal_rows_if_found: int | None
    search_limit: int
    found_within_limit: bool


def _as_matrix(matrix: Array) -> Array:
    arr = np.asarray(matrix, dtype=float)
    if arr.ndim == 1:
        arr = arr[None, :]
    return arr


def _rowspace_basis(matrix: Array, *, tol: float = EPS) -> Array:
    arr = _as_matrix(matrix)
    if arr.size == 0:
        return np.zeros((0, arr.shape[1]), dtype=float)
    _, singular_values, vh = np.linalg.svd(arr, full_matrices=False)
    rank = int(np.sum(singular_values > tol))
    return vh[:rank]


def _nullspace_basis_rows(matrix: Array, *, tol: float = EPS) -> Array:
    arr = np.asarray(matrix, dtype=float)
    if arr.ndim != 2:
        raise ValueError("matrix must be 2D")
    if arr.shape[0] == 0:
        return np.eye(arr.shape[1], dtype=float)
    _, singular_values, vh = np.linalg.svd(arr, full_matrices=True)
    rank = int(np.sum(singular_values > tol))
    return vh[rank:]


def _dedupe_rows(rows: Sequence[Array], *, tol: float = EPS) -> list[Array]:
    unique: list[Array] = []
    for row in rows:
        vector = np.asarray(row, dtype=float).reshape(-1)
        if np.linalg.norm(vector) <= tol:
            continue
        if any(np.linalg.norm(vector - other) <= tol for other in unique):
            continue
        unique.append(vector)
    return unique


def agreement_basis(context_matrices: Sequence[Array], *, tol: float = EPS) -> Array:
    contexts = [_as_matrix(matrix) for matrix in context_matrices]
    if not contexts:
        raise ValueError("context_matrices must be nonempty")
    p = contexts[0].shape[0]
    d = contexts[0].shape[1]
    for matrix in contexts:
        if matrix.shape[0] != p or matrix.shape[1] != d:
            raise ValueError("all context matrices must share the same shape")
    if len(contexts) == 1:
        return np.eye(p, dtype=float)
    reference = contexts[0]
    constraints = np.vstack([(matrix - reference).T for matrix in contexts[1:]])
    return _nullspace_basis_rows(constraints, tol=tol)


def agreement_lift_matrix(context_matrices: Sequence[Array], *, tol: float = EPS) -> Array:
    contexts = [_as_matrix(matrix) for matrix in context_matrices]
    basis = agreement_basis(contexts, tol=tol)
    return basis @ contexts[0]


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


def agreement_operator_recoverability(
    context_matrices: Sequence[Array],
    target_matrix: Array,
    *,
    tol: float = EPS,
) -> AgreementOperatorRecoverabilityReport:
    contexts = [_as_matrix(matrix) for matrix in context_matrices]
    target = _as_matrix(target_matrix)
    if not contexts:
        raise ValueError("context_matrices must be nonempty")
    if target.shape[1] != contexts[0].shape[1]:
        raise ValueError("target_matrix coefficient dimension must match context matrices")

    lift = agreement_lift_matrix(contexts, tol=tol)
    lift_rep = restricted_linear_recoverability(lift, target, tol=tol)
    direct_rep = context_invariant_recoverability(contexts, target, tol=tol)

    return AgreementOperatorRecoverabilityReport(
        context_count=len(contexts),
        record_dimension=contexts[0].shape[0],
        coefficient_dimension=contexts[0].shape[1],
        target_dimension=target.shape[0],
        agreement_basis_dimension=int(agreement_basis(contexts, tol=tol).shape[0]),
        lifted_matrix_rank=int(np.linalg.matrix_rank(lift, tol)),
        lifted_residual_norm=float(lift_rep.residual_norm),
        invariant_exact_via_agreement=bool(lift_rep.exact_recoverable),
        invariant_exact_direct=bool(direct_rep.invariant_exact),
        lift_direct_consistent=bool(lift_rep.exact_recoverable == direct_rep.invariant_exact),
    )


def unconstrained_shared_augmentation_threshold(
    context_matrices: Sequence[Array],
    target_matrix: Array,
    *,
    tol: float = EPS,
) -> UnconstrainedSharedAugmentationReport:
    contexts = [_as_matrix(matrix) for matrix in context_matrices]
    target = _as_matrix(target_matrix)
    if not contexts:
        raise ValueError("context_matrices must be nonempty")
    if target.shape[1] != contexts[0].shape[1]:
        raise ValueError("target_matrix coefficient dimension must match context matrices")

    lift = agreement_lift_matrix(contexts, tol=tol)
    rank_lift = int(np.linalg.matrix_rank(lift, tol))
    rank_aug = int(np.linalg.matrix_rank(np.vstack([lift, target]), tol))
    minimal_rows = int(rank_aug - rank_lift)

    # Construct one minimal shared row set as rowspace basis of the target component
    # orthogonal to row(lift).
    lift_basis = _rowspace_basis(lift, tol=tol)
    if lift_basis.shape[0] == 0:
        projected = np.zeros_like(target)
    else:
        projected = target @ lift_basis.T @ lift_basis
    residual_component = target - projected
    shared_rows = _rowspace_basis(residual_component, tol=tol)
    if shared_rows.shape[0] != minimal_rows:
        shared_rows = shared_rows[:minimal_rows]

    augmented_contexts = [np.vstack([matrix, shared_rows]) for matrix in contexts]
    after_rep = context_invariant_recoverability(augmented_contexts, target, tol=tol)
    before_rep = context_invariant_recoverability(contexts, target, tol=tol)

    return UnconstrainedSharedAugmentationReport(
        minimal_shared_rows_free=minimal_rows,
        lifted_matrix_rank=rank_lift,
        target_augmented_rank=rank_aug,
        invariant_exact_before=bool(before_rep.invariant_exact),
        invariant_exact_after_constructed=bool(after_rep.invariant_exact),
        constructed_shared_rows=shared_rows,
    )


def candidate_library_recoverability(
    context_matrices: Sequence[Array],
    target_matrix: Array,
    candidate_rows: Sequence[Array],
    *,
    max_search_rows: int | None = None,
    tol: float = EPS,
) -> CandidateLibraryRecoverabilityReport:
    contexts = [_as_matrix(matrix) for matrix in context_matrices]
    target = _as_matrix(target_matrix)
    if not contexts:
        raise ValueError("context_matrices must be nonempty")
    if target.shape[1] != contexts[0].shape[1]:
        raise ValueError("target_matrix coefficient dimension must match context matrices")

    lift = agreement_lift_matrix(contexts, tol=tol)
    rank_lift = int(np.linalg.matrix_rank(lift, tol))
    rank_lift_target = int(np.linalg.matrix_rank(np.vstack([lift, target]), tol))
    free_threshold = int(rank_lift_target - rank_lift)

    candidates = _dedupe_rows(candidate_rows, tol=tol)
    if candidates:
        candidate_matrix = np.vstack(candidates)
        rank_lift_candidate = int(np.linalg.matrix_rank(np.vstack([lift, candidate_matrix]), tol))
        rank_lift_candidate_target = int(np.linalg.matrix_rank(np.vstack([lift, candidate_matrix, target]), tol))
        augmented_full = [np.vstack([matrix, candidate_matrix]) for matrix in contexts]
    else:
        candidate_matrix = np.zeros((0, target.shape[1]), dtype=float)
        rank_lift_candidate = rank_lift
        rank_lift_candidate_target = rank_lift_target
        augmented_full = [matrix.copy() for matrix in contexts]

    library_defect = int(rank_lift_candidate_target - rank_lift_candidate)
    full_pool_feasible = bool(library_defect == 0)
    full_pool_report = context_invariant_recoverability(augmented_full, target, tol=tol)

    if max_search_rows is None:
        search_limit = len(candidates)
    else:
        search_limit = min(int(max_search_rows), len(candidates))
    search_report = minimal_shared_augmentation(
        contexts,
        target,
        candidates,
        max_shared_rows=search_limit,
        tol=tol,
    )

    return CandidateLibraryRecoverabilityReport(
        candidate_count=len(candidates),
        free_threshold=free_threshold,
        library_rank_gain=int(rank_lift_candidate - rank_lift),
        library_target_defect=library_defect,
        full_pool_feasible=full_pool_feasible,
        invariant_exact_with_full_pool=bool(full_pool_report.invariant_exact),
        minimal_rows_if_found=search_report.minimal_shared_rows,
        search_limit=search_limit,
        found_within_limit=bool(search_report.invariant_exact_after_augmentation),
    )


__all__ = [
    "CandidateLibraryRecoverabilityReport",
    "AgreementOperatorRecoverabilityReport",
    "ContextInvariantRecoverabilityReport",
    "SharedAugmentationSearchReport",
    "UnconstrainedSharedAugmentationReport",
    "agreement_basis",
    "agreement_lift_matrix",
    "agreement_operator_recoverability",
    "candidate_library_recoverability",
    "context_invariant_rank_descriptor",
    "context_invariant_recoverability",
    "minimal_shared_augmentation",
    "unconstrained_shared_augmentation_threshold",
]
