from __future__ import annotations

from dataclasses import dataclass
import numpy as np

Array = np.ndarray


def _as_matrix(basis: Array) -> Array:
    arr = np.asarray(basis, dtype=float)
    if arr.ndim == 1:
        arr = arr[:, None]
    return arr


def orthonormalize_columns(basis: Array, *, tol: float = 1e-10) -> Array:
    mat = _as_matrix(basis)
    q, _ = np.linalg.qr(mat)
    keep: list[int] = []
    for i in range(q.shape[1]):
        if np.linalg.norm(q[:, i]) > tol:
            keep.append(i)
    if not keep:
        raise ValueError("basis must contain at least one nonzero vector")
    return q[:, keep]


def orthogonal_projector(basis: Array) -> Array:
    q = orthonormalize_columns(basis)
    return q @ q.T


def exact_projection_recovery(x: Array, protected_basis: Array) -> Array:
    p_s = orthogonal_projector(protected_basis)
    return p_s @ np.asarray(x, dtype=float)


@dataclass(frozen=True)
class FiniteOCPSystem:
    protected_basis: Array
    disturbance_basis: Array
    tol: float = 1e-10

    def __post_init__(self) -> None:
        p_s = orthogonal_projector(self.protected_basis)
        p_d = orthogonal_projector(self.disturbance_basis)
        overlap = np.linalg.norm(p_s @ p_d, ord=2)
        if overlap > self.tol:
            raise ValueError(
                "protected and disturbance subspaces are not orthogonal enough for the exact OCP model"
            )

    @property
    def P_S(self) -> Array:
        return orthogonal_projector(self.protected_basis)

    @property
    def P_D(self) -> Array:
        return orthogonal_projector(self.disturbance_basis)

    def decompose(self, x: Array) -> tuple[Array, Array]:
        vec = np.asarray(x, dtype=float)
        s = self.P_S @ vec
        d = self.P_D @ vec
        return s, d

    def exact_recover(self, x: Array) -> Array:
        return self.P_S @ np.asarray(x, dtype=float)

    def continuous_correction(self, x: Array, *, rate: float, time: float) -> Array:
        vec = np.asarray(x, dtype=float)
        s, d = self.decompose(vec)
        return s + np.exp(-rate * time) * d

    def correction_energy(self, x: Array) -> float:
        _, d = self.decompose(x)
        return float(np.linalg.norm(d) ** 2)
