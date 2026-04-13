from __future__ import annotations

from dataclasses import dataclass
import numpy as np

Array = np.ndarray


def _as_basis(matrix: Array) -> Array:
    arr = np.asarray(matrix, dtype=complex)
    if arr.ndim == 1:
        arr = arr[:, None]
    return arr


def orthonormal_sector_basis(basis: Array, *, tol: float = 1e-10) -> Array:
    mat = _as_basis(basis)
    q, _ = np.linalg.qr(mat)
    keep: list[int] = []
    for idx in range(q.shape[1]):
        if np.linalg.norm(q[:, idx]) > tol:
            keep.append(idx)
    if not keep:
        raise ValueError('basis must contain at least one nonzero vector')
    return q[:, keep]


def sector_projector(basis: Array) -> Array:
    q = orthonormal_sector_basis(basis)
    return q @ q.conj().T


def pairwise_sector_overlap_matrix(sector_bases: list[Array]) -> Array:
    q_list = [orthonormal_sector_basis(basis) for basis in sector_bases]
    overlaps = np.zeros((len(q_list), len(q_list)), dtype=float)
    for i, q_i in enumerate(q_list):
        for j, q_j in enumerate(q_list):
            overlaps[i, j] = float(np.linalg.norm(q_i.conj().T @ q_j, ord=2))
    return overlaps


@dataclass(frozen=True)
class SectorRecoveryReport:
    protected_dim: int
    sector_count: int
    pairwise_orthogonal: bool
    max_pairwise_overlap: float
    exact_recovery_errors: list[float]



def sector_recovery_operator(protected_basis: Array, sector_basis: Array, *, tol: float = 1e-10) -> Array:
    protected = _as_basis(protected_basis)
    sector = _as_basis(sector_basis)
    if protected.shape[1] != sector.shape[1]:
        raise ValueError('protected basis and sector basis must have the same number of columns')
    if np.linalg.matrix_rank(protected, tol=tol) != protected.shape[1]:
        raise ValueError('protected basis must have full column rank')
    if np.linalg.matrix_rank(sector, tol=tol) != sector.shape[1]:
        raise ValueError('sector basis must have full column rank')
    return protected @ np.linalg.pinv(sector)



def global_sector_recovery_operator(protected_basis: Array, sector_bases: list[Array], *, tol: float = 1e-10) -> Array:
    if not sector_bases:
        raise ValueError('sector_bases must be non-empty')
    overlaps = pairwise_sector_overlap_matrix(sector_bases)
    max_offdiag = 0.0
    if overlaps.shape[0] > 1:
        mask = ~np.eye(overlaps.shape[0], dtype=bool)
        max_offdiag = float(np.max(overlaps[mask]))
    if max_offdiag > tol:
        raise ValueError('sector bases must be pairwise orthogonal for a single exact sector recovery operator')
    ambient_dim = _as_basis(protected_basis).shape[0]
    out = np.zeros((ambient_dim, ambient_dim), dtype=complex)
    for sector_basis in sector_bases:
        out = out + sector_recovery_operator(protected_basis, sector_basis, tol=tol) @ sector_projector(sector_basis)
    return out



def sector_recovery_report(protected_basis: Array, sector_bases: list[Array], *, tol: float = 1e-10) -> SectorRecoveryReport:
    q_s = orthonormal_sector_basis(protected_basis)
    overlaps = pairwise_sector_overlap_matrix(sector_bases)
    max_pairwise_overlap = 0.0
    if overlaps.shape[0] > 1:
        mask = ~np.eye(overlaps.shape[0], dtype=bool)
        max_pairwise_overlap = float(np.max(overlaps[mask]))
    pairwise_orthogonal = max_pairwise_overlap < tol
    exact_recovery_errors: list[float] = []
    if pairwise_orthogonal:
        global_recovery = global_sector_recovery_operator(protected_basis, sector_bases, tol=tol)
        protected = _as_basis(protected_basis)
        coeffs = np.arange(1, protected.shape[1] + 1, dtype=float) + 0.25
        coeffs = coeffs / np.linalg.norm(coeffs)
        protected_vec = protected @ coeffs
        for sector_basis in sector_bases:
            sector = _as_basis(sector_basis)
            disturbed = sector @ coeffs
            recovered = global_recovery @ disturbed
            exact_recovery_errors.append(float(np.linalg.norm(recovered - protected_vec)))
    return SectorRecoveryReport(
        protected_dim=q_s.shape[1],
        sector_count=len(sector_bases),
        pairwise_orthogonal=pairwise_orthogonal,
        max_pairwise_overlap=max_pairwise_overlap,
        exact_recovery_errors=exact_recovery_errors,
    )
