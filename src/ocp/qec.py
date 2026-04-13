from __future__ import annotations

from dataclasses import dataclass
import itertools
import numpy as np

Array = np.ndarray

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)


def ket(bits: str) -> Array:
    state = np.array([1.0 + 0.0j])
    for bit in bits:
        if bit not in {"0", "1"}:
            raise ValueError("bits must be a binary string")
        vec = np.array([1.0, 0.0], dtype=complex) if bit == "0" else np.array([0.0, 1.0], dtype=complex)
        state = np.kron(state, vec)
    return state


def normalize(v: Array) -> Array:
    nrm = np.linalg.norm(v)
    if nrm == 0:
        raise ValueError("cannot normalize zero vector")
    return v / nrm


def code_projector(codewords: list[Array]) -> Array:
    cols = np.column_stack([normalize(v) for v in codewords])
    return cols @ cols.conj().T


def error_sector_projector(codewords: list[Array], error: Array) -> Array:
    cols = np.column_stack([normalize(error @ v) for v in codewords])
    return cols @ cols.conj().T


def pauli_x_error(n_qubits: int, target: int) -> Array:
    ops = []
    for idx in range(n_qubits):
        ops.append(X if idx == target else I2)
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out


def bitflip_three_qubit_code() -> tuple[list[Array], list[Array]]:
    codewords = [ket("000"), ket("111")]
    errors = [np.eye(8, dtype=complex)] + [pauli_x_error(3, i) for i in range(3)]
    return codewords, errors


def bitflip_three_qubit_recovery_operators() -> tuple[list[Array], list[Array], list[Array]]:
    codewords, errors = bitflip_three_qubit_code()
    sector_projectors = [error_sector_projector(codewords, error) for error in errors]
    recovery_operators = [error.conj().T @ projector for error, projector in zip(errors, sector_projectors)]
    return codewords, sector_projectors, recovery_operators


def coherent_recovery_map(state: Array, recovery_operators: list[Array]) -> Array:
    vec = np.asarray(state, dtype=complex)
    return sum(operator @ vec for operator in recovery_operators)


@dataclass
class KnillLaflammeReport:
    holds: bool
    alpha: Array
    max_residual: float
    pairwise_image_overlap: float


def knill_laflamme_report(codewords: list[Array], errors: list[Array], *, tol: float = 1e-9) -> KnillLaflammeReport:
    p = code_projector(codewords)
    n = len(errors)
    alpha = np.zeros((n, n), dtype=complex)
    max_residual = 0.0

    for i, e_i in enumerate(errors):
        for j, e_j in enumerate(errors):
            middle = p @ e_i.conj().T @ e_j @ p
            scalar = np.trace(middle) / np.trace(p)
            alpha[i, j] = scalar
            residual = np.linalg.norm(middle - scalar * p)
            max_residual = max(max_residual, float(residual))

    pairwise_image_overlap = 0.0
    code_cols = np.column_stack([normalize(v) for v in codewords])
    for i, j in itertools.combinations(range(n), 2):
        img_i = errors[i] @ code_cols
        img_j = errors[j] @ code_cols
        overlap = np.linalg.norm(img_i.conj().T @ img_j, ord=2)
        pairwise_image_overlap = max(pairwise_image_overlap, float(overlap))

    return KnillLaflammeReport(
        holds=max_residual < tol,
        alpha=alpha,
        max_residual=max_residual,
        pairwise_image_overlap=pairwise_image_overlap,
    )
