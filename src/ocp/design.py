from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Sequence

import numpy as np

from .recoverability import EPS, _compressed_observation_matrix, _null_space, _orthonormalize_columns, restricted_linear_recoverability

Array = np.ndarray


@dataclass(frozen=True)
class LinearRecoverabilityDesignReport:
    exact_recoverable: bool
    rank_observation: int
    rank_protected: int
    recoverable_row_indices: tuple[int, ...]
    unrecoverable_row_indices: tuple[int, ...]
    row_space_residuals: tuple[float, ...]
    nullspace_witness: Array | None
    nullspace_protected_gap: float
    unrestricted_minimal_added_measurements: int
    minimal_added_measurements: int | None
    candidate_exact_sets: tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class CandidateAugmentationReport:
    minimal_added_measurements: int | None
    candidate_exact_sets: tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class UnrestrictedAugmentationReport:
    minimal_added_measurements: int
    rowspace_deficiency: int
    restricted_augmentation_rows: Array
    ambient_augmentation_rows: Array
    exact_recoverable_after_augmentation: bool
    residual_norm_after_augmentation: float



def _restricted_matrices(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> tuple[Array, Array]:
    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    if family_basis is None:
        F = np.eye(O.shape[1])
    else:
        F = _orthonormalize_columns(np.asarray(family_basis, dtype=float), tol=tol)
    return O @ F, L @ F



def restricted_row_space_residuals(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> Array:
    OF, LF = _restricted_matrices(observation_matrix, protected_matrix, family_basis=family_basis, tol=tol)
    if LF.ndim == 1:
        LF = LF[None, :]
    if OF.size == 0:
        return np.linalg.norm(LF, axis=1)
    row_basis = _compressed_observation_matrix(OF, tol=tol)
    if row_basis.size == 0:
        return np.linalg.norm(LF, axis=1)
    column_basis = row_basis.T
    projector = column_basis @ np.linalg.pinv(column_basis, rcond=tol)
    residuals = []
    for row in LF:
        target = np.asarray(row, dtype=float)
        residual = target - projector @ target
        residuals.append(float(np.linalg.norm(residual)))
    return np.asarray(residuals, dtype=float)



def recoverable_protected_rows(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> tuple[tuple[int, ...], tuple[int, ...], Array]:
    residuals = restricted_row_space_residuals(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    recoverable = tuple(int(index) for index, value in enumerate(residuals) if float(value) <= tol)
    unrecoverable = tuple(int(index) for index, value in enumerate(residuals) if float(value) > tol)
    return recoverable, unrecoverable, residuals



def minimal_candidate_augmentation(
    observation_matrix: Array,
    protected_matrix: Array,
    candidate_rows: Sequence[Array],
    *,
    family_basis: Array | None = None,
    max_added_measurements: int | None = None,
    tol: float = EPS,
) -> CandidateAugmentationReport:
    candidates = [np.asarray(row, dtype=float).reshape(1, -1) for row in candidate_rows]
    if not candidates:
        return CandidateAugmentationReport(minimal_added_measurements=None, candidate_exact_sets=())
    if max_added_measurements is None:
        max_added_measurements = len(candidates)
    exact_sets: list[tuple[int, ...]] = []
    for size in range(1, max_added_measurements + 1):
        for combo in combinations(range(len(candidates)), size):
            augmented = np.vstack([np.asarray(observation_matrix, dtype=float), *[candidates[index] for index in combo]])
            report = restricted_linear_recoverability(augmented, protected_matrix, family_basis=family_basis, tol=tol)
            if report.exact_recoverable:
                exact_sets.append(tuple(int(index) for index in combo))
        if exact_sets:
            return CandidateAugmentationReport(
                minimal_added_measurements=int(size),
                candidate_exact_sets=tuple(exact_sets),
            )
    return CandidateAugmentationReport(minimal_added_measurements=None, candidate_exact_sets=())


def unrestricted_exact_augmentation(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> UnrestrictedAugmentationReport:
    OF, LF = _restricted_matrices(observation_matrix, protected_matrix, family_basis=family_basis, tol=tol)
    rank_observation = int(np.linalg.matrix_rank(OF, tol=tol))
    rank_total = int(np.linalg.matrix_rank(np.vstack([OF, LF]), tol=tol))
    deficiency = int(rank_total - rank_observation)

    row_basis = _compressed_observation_matrix(OF, tol=tol)
    working_basis = row_basis.copy()
    complement_rows: list[Array] = []
    if LF.ndim == 1:
        LF = LF[None, :]
    for row in LF:
        candidate = np.asarray(row, dtype=float).copy()
        if working_basis.size:
            projector = np.linalg.pinv(working_basis, rcond=tol) @ working_basis
            candidate = candidate - candidate @ projector
        norm = float(np.linalg.norm(candidate))
        if norm > tol:
            candidate = candidate / norm
            complement_rows.append(candidate.copy())
            working_basis = np.vstack([working_basis, candidate]) if working_basis.size else candidate[None, :]

    restricted_rows = np.vstack(complement_rows) if complement_rows else np.zeros((0, OF.shape[1]), dtype=float)
    if restricted_rows.shape[0] != deficiency:
        raise ValueError('computed unrestricted augmentation does not match the row-space deficiency')

    if family_basis is None:
        F = np.eye(np.asarray(observation_matrix, dtype=float).shape[1])
    else:
        F = _orthonormalize_columns(np.asarray(family_basis, dtype=float), tol=tol)
    ambient_rows = restricted_rows @ F.T
    augmented = np.vstack([np.asarray(observation_matrix, dtype=float), ambient_rows]) if ambient_rows.size else np.asarray(observation_matrix, dtype=float)
    exact_report = restricted_linear_recoverability(augmented, protected_matrix, family_basis=family_basis, tol=tol)
    return UnrestrictedAugmentationReport(
        minimal_added_measurements=deficiency,
        rowspace_deficiency=deficiency,
        restricted_augmentation_rows=restricted_rows,
        ambient_augmentation_rows=ambient_rows,
        exact_recoverable_after_augmentation=bool(exact_report.exact_recoverable),
        residual_norm_after_augmentation=float(exact_report.residual_norm),
    )



def nullspace_witness_for_protected_loss(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> tuple[Array | None, float]:
    OF, LF = _restricted_matrices(observation_matrix, protected_matrix, family_basis=family_basis, tol=tol)
    null = _null_space(OF, tol=tol)
    if null.size == 0:
        return None, 0.0
    best_vector = None
    best_gap = 0.0
    for index in range(null.shape[1]):
        direction = np.asarray(null[:, index], dtype=float)
        if np.max(np.abs(direction)) <= tol:
            continue
        scaled = direction * (float(box_radius) / np.max(np.abs(direction)))
        gap = float(np.linalg.norm(LF @ scaled))
        if gap > best_gap + tol:
            best_gap = gap
            best_vector = scaled
    return best_vector, best_gap



def linear_recoverability_design_report(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    candidate_rows: Sequence[Array] | None = None,
    family_basis: Array | None = None,
    max_added_measurements: int | None = None,
    tol: float = EPS,
) -> LinearRecoverabilityDesignReport:
    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    exact_report = restricted_linear_recoverability(O, L, family_basis=family_basis, tol=tol)
    OF, LF = _restricted_matrices(O, L, family_basis=family_basis, tol=tol)
    recoverable, unrecoverable, residuals = recoverable_protected_rows(O, L, family_basis=family_basis, tol=tol)
    witness, gap = nullspace_witness_for_protected_loss(O, L, family_basis=family_basis, tol=tol)
    unrestricted = unrestricted_exact_augmentation(O, L, family_basis=family_basis, tol=tol)
    augmentation = (
        minimal_candidate_augmentation(
            O,
            L,
            candidate_rows,
            family_basis=family_basis,
            max_added_measurements=max_added_measurements,
            tol=tol,
        )
        if candidate_rows is not None
        else CandidateAugmentationReport(minimal_added_measurements=None, candidate_exact_sets=())
    )
    return LinearRecoverabilityDesignReport(
        exact_recoverable=bool(exact_report.exact_recoverable),
        rank_observation=int(np.linalg.matrix_rank(OF, tol=tol)),
        rank_protected=int(np.linalg.matrix_rank(LF, tol=tol)),
        recoverable_row_indices=recoverable,
        unrecoverable_row_indices=unrecoverable,
        row_space_residuals=tuple(float(value) for value in residuals),
        nullspace_witness=None if witness is None else np.asarray(witness, dtype=float),
        nullspace_protected_gap=float(gap),
        unrestricted_minimal_added_measurements=int(unrestricted.minimal_added_measurements),
        minimal_added_measurements=augmentation.minimal_added_measurements,
        candidate_exact_sets=augmentation.candidate_exact_sets,
    )
