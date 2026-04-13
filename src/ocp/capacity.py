from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from .core import orthonormalize_columns
from .continuous import LinearOCPFlow
from .qec import error_sector_projector

Array = np.ndarray


def _as_matrix(basis: Array) -> Array:
    arr = np.asarray(basis, dtype=float)
    if arr.ndim == 1:
        arr = arr[:, None]
    return arr


def subspace_dimension(basis: Array, *, tol: float = 1e-10) -> int:
    q = orthonormalize_columns(basis, tol=tol)
    return int(q.shape[1])


def intersection_dimension(basis_a: Array, basis_b: Array, *, tol: float = 1e-10) -> int:
    qa = orthonormalize_columns(basis_a, tol=tol)
    qb = orthonormalize_columns(basis_b, tol=tol)
    rank_sum = qa.shape[1] + qb.shape[1]
    combined = np.column_stack([qa, qb])
    rank_combined = np.linalg.matrix_rank(combined, tol=tol)
    dim = rank_sum - rank_combined
    return int(max(dim, 0))


@dataclass(frozen=True)
class ExactLinearCapacity:
    protected_dim: int
    disturbance_dim: int
    ambient_span_dim: int
    intersection_dim: int
    exact_recovery_possible: bool
    min_recovery_rank: int | None
    min_correction_rank: int | None


@dataclass(frozen=True)
class QECSectorCapacity:
    sector_count: int
    pairwise_orthogonal: bool
    minimum_syndrome_outcomes: int | None


@dataclass(frozen=True)
class GeneratorCapacity:
    protected_dim: int
    disturbance_dim: int
    stable_disturbance_dim: int
    neutral_disturbance_dim: int
    unstable_disturbance_dim: int
    split_preserving: bool
    protected_mixing_norm: float
    disturbance_from_protected_norm: float


def exact_linear_capacity(protected_basis: Array, disturbance_basis: Array, *, tol: float = 1e-10) -> ExactLinearCapacity:
    q_s = orthonormalize_columns(protected_basis, tol=tol)
    q_d = orthonormalize_columns(disturbance_basis, tol=tol)
    protected_dim = q_s.shape[1]
    disturbance_dim = q_d.shape[1]
    combined = np.column_stack([q_s, q_d])
    ambient_span_dim = int(np.linalg.matrix_rank(combined, tol=tol))
    overlap_dim = intersection_dimension(q_s, q_d, tol=tol)
    exact_possible = overlap_dim == 0
    return ExactLinearCapacity(
        protected_dim=protected_dim,
        disturbance_dim=disturbance_dim,
        ambient_span_dim=ambient_span_dim,
        intersection_dim=overlap_dim,
        exact_recovery_possible=exact_possible,
        min_recovery_rank=protected_dim if exact_possible else None,
        min_correction_rank=disturbance_dim if exact_possible else None,
    )


def qec_sector_capacity(codewords: list[Array], errors: list[Array], *, tol: float = 1e-9) -> QECSectorCapacity:
    sectors = [error_sector_projector(codewords, error) for error in errors]
    pairwise_orthogonal = True
    for i, proj_i in enumerate(sectors):
        for j, proj_j in enumerate(sectors):
            if i >= j:
                continue
            if np.linalg.norm(proj_i @ proj_j) > tol:
                pairwise_orthogonal = False
                break
        if not pairwise_orthogonal:
            break
    return QECSectorCapacity(
        sector_count=len(sectors),
        pairwise_orthogonal=pairwise_orthogonal,
        minimum_syndrome_outcomes=len(sectors) if pairwise_orthogonal else None,
    )


def generator_capacity(generator: Array, protected_basis: Array, disturbance_basis: Array, *, tol: float = 1e-10) -> GeneratorCapacity:
    flow = LinearOCPFlow(generator, protected_basis, disturbance_basis, tol=tol)
    report = flow.report()
    q_s = orthonormalize_columns(protected_basis, tol=tol)
    q_d = orthonormalize_columns(disturbance_basis, tol=tol)
    q = np.column_stack([q_s, q_d])
    block = q.T @ np.asarray(generator, dtype=float) @ q
    n_s = q_s.shape[1]
    dd = block[n_s:, n_s:]
    eigvals = np.linalg.eigvals(dd)
    stable = int(np.sum(np.real(eigvals) > tol))
    neutral = int(np.sum(np.abs(np.real(eigvals)) <= tol))
    unstable = int(np.sum(np.real(eigvals) < -tol))
    return GeneratorCapacity(
        protected_dim=q_s.shape[1],
        disturbance_dim=q_d.shape[1],
        stable_disturbance_dim=stable,
        neutral_disturbance_dim=neutral,
        unstable_disturbance_dim=unstable,
        split_preserving=bool(report.annihilates_protected and report.preserves_disturbance),
        protected_mixing_norm=float(report.protected_mixing_norm),
        disturbance_from_protected_norm=float(report.disturbance_from_protected_norm),
    )
