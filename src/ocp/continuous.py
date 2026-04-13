from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from .core import orthonormalize_columns

Array = np.ndarray


def _real_if_close(matrix: Array) -> Array:
    return np.real_if_close(matrix, tol=1000)


def matrix_exponential(matrix: Array, time: float) -> Array:
    mat = np.asarray(matrix, dtype=complex)
    eigenvalues, eigenvectors = np.linalg.eig(mat)
    if np.linalg.matrix_rank(eigenvectors) != mat.shape[0]:
        raise ValueError("matrix_exponential currently requires a diagonalizable matrix")
    inv = np.linalg.inv(eigenvectors)
    exp_diag = np.diag(np.exp(time * eigenvalues))
    out = eigenvectors @ exp_diag @ inv
    return _real_if_close(out)


def orthogonal_split_basis(protected_basis: Array, disturbance_basis: Array) -> tuple[Array, Array, Array]:
    q_s = orthonormalize_columns(protected_basis)
    q_d = orthonormalize_columns(disturbance_basis)
    overlap = np.linalg.norm(q_s.T @ q_d, ord=2)
    if overlap > 1e-10:
        raise ValueError("protected and disturbance bases must be orthogonal for the linear OCP flow model")
    q = np.column_stack([q_s, q_d])
    return q_s, q_d, q


def block_decomposition(operator: Array, protected_basis: Array, disturbance_basis: Array) -> tuple[Array, Array, Array, Array]:
    q_s, q_d, q = orthogonal_split_basis(protected_basis, disturbance_basis)
    block = q.T @ np.asarray(operator, dtype=float) @ q
    n_s = q_s.shape[1]
    return (
        block[:n_s, :n_s],
        block[:n_s, n_s:],
        block[n_s:, :n_s],
        block[n_s:, n_s:],
    )


@dataclass(frozen=True)
class LinearGeneratorReport:
    annihilates_protected: bool
    preserves_disturbance: bool
    protected_mixing_norm: float
    disturbance_from_protected_norm: float
    disturbance_decay_margin: float


@dataclass(frozen=True)
class LinearOCPFlow:
    generator: Array
    protected_basis: Array
    disturbance_basis: Array
    tol: float = 1e-10

    def __post_init__(self) -> None:
        q_s, q_d, _ = orthogonal_split_basis(self.protected_basis, self.disturbance_basis)
        object.__setattr__(self, '_q_s', q_s)
        object.__setattr__(self, '_q_d', q_d)

    @property
    def P_S(self) -> Array:
        return self._q_s @ self._q_s.T

    @property
    def P_D(self) -> Array:
        return self._q_d @ self._q_d.T

    @property
    def generator_matrix(self) -> Array:
        return np.asarray(self.generator, dtype=float)

    def report(self) -> LinearGeneratorReport:
        ss, sd, ds, dd = block_decomposition(self.generator_matrix, self.protected_basis, self.disturbance_basis)
        eigenvalues = np.linalg.eigvals(dd)
        decay_margin = float(np.min(np.real(eigenvalues))) if eigenvalues.size else float('inf')
        return LinearGeneratorReport(
            annihilates_protected=np.linalg.norm(ss) + np.linalg.norm(ds) < self.tol,
            preserves_disturbance=np.linalg.norm(sd) < self.tol,
            protected_mixing_norm=float(np.linalg.norm(sd)),
            disturbance_from_protected_norm=float(np.linalg.norm(ds)),
            disturbance_decay_margin=decay_margin,
        )

    def flow_operator(self, time: float) -> Array:
        return matrix_exponential(-self.generator_matrix, time)

    def flow(self, x: Array, time: float) -> Array:
        return _real_if_close(self.flow_operator(time) @ np.asarray(x, dtype=float))

    def protected_component(self, x: Array) -> Array:
        return self.P_S @ np.asarray(x, dtype=float)

    def disturbance_component(self, x: Array) -> Array:
        return self.P_D @ np.asarray(x, dtype=float)

    def preserves_protected_component(self, x: Array, time: float) -> bool:
        evolved = self.flow(x, time)
        return np.allclose(self.protected_component(evolved), self.protected_component(x), atol=self.tol)

    def disturbance_norm(self, x: Array) -> float:
        return float(np.linalg.norm(self.disturbance_component(x)))

    def asymptotic_bound(self, x: Array, time: float) -> float:
        report = self.report()
        if report.disturbance_decay_margin <= 0:
            return float('inf')
        return float(np.exp(-report.disturbance_decay_margin * time) * self.disturbance_norm(x))

    def exact_recovery_residual(self, time: float) -> float:
        flow = self.flow_operator(time)
        ss, sd, ds, dd = block_decomposition(flow, self.protected_basis, self.disturbance_basis)
        identity = np.eye(ss.shape[0])
        return float(
            max(
                np.linalg.norm(ss - identity),
                np.linalg.norm(sd),
                np.linalg.norm(ds),
                np.linalg.norm(dd),
            )
        )

    def finite_time_exact_recovery_possible(self, time: float) -> bool:
        if time <= 0:
            return False
        if self._q_d.shape[1] == 0:
            return True
        return self.exact_recovery_residual(time) < self.tol
