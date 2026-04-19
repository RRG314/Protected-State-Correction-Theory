from __future__ import annotations

"""Structural-information helpers for restricted recoverability analysis.

This module is intentionally scoped:
- it treats exact recoverability as a fiber-constancy question on declared families,
- it exposes branch-limited stability and coarse-graining diagnostics,
- it does not claim a universal scalar information law.
"""

from dataclasses import dataclass
from itertools import product
from typing import Callable, Iterable

import numpy as np

from .recoverability import EPS, restricted_linear_recoverability


Array = np.ndarray


def _as_2d(values: Array) -> Array:
    arr = np.asarray(values, dtype=float)
    if arr.ndim == 1:
        arr = arr[:, None]
    return arr


def _record_key(record_row: Array, decimals: int = 12) -> tuple[float, ...]:
    row = np.asarray(record_row, dtype=float).reshape(-1)
    return tuple(np.round(row, decimals=decimals).tolist())


def _target_distance(a: Array, b: Array) -> float:
    return float(np.linalg.norm(np.asarray(a, dtype=float).reshape(-1) - np.asarray(b, dtype=float).reshape(-1)))


@dataclass(frozen=True)
class StructuralInformationObject:
    """Typed primitive object on a declared finite admissible family.

    The object follows the restricted tuple:
    I = (A, M, T, Pi_M, Pi_T, C_{M,T})
    represented here by samples from A and evaluated records/targets.
    """

    records: Array
    targets: Array

    def __post_init__(self) -> None:
        r = _as_2d(self.records)
        t = _as_2d(self.targets)
        if r.shape[0] != t.shape[0]:
            raise ValueError("records and targets must have the same number of samples")

    @property
    def n_samples(self) -> int:
        return int(_as_2d(self.records).shape[0])

    def exact_recoverable(self, *, tol: float = EPS) -> bool:
        """Exact finite recoverability iff each record fiber has one target value."""
        return self.collapse_modulus_zero() <= float(tol)

    def collapse_modulus_zero(self) -> float:
        """Finite-fiber analog of kappa_{M,T}(0): max target spread at equal record."""
        records = _as_2d(self.records)
        targets = _as_2d(self.targets)
        by_fiber: dict[tuple[float, ...], list[int]] = {}
        for idx, rec in enumerate(records):
            by_fiber.setdefault(_record_key(rec), []).append(idx)
        max_gap = 0.0
        for members in by_fiber.values():
            if len(members) < 2:
                continue
            for i, j in product(members, members):
                if j <= i:
                    continue
                max_gap = max(max_gap, _target_distance(targets[i], targets[j]))
        return float(max_gap)

    def collision_witness(self, *, tol: float = EPS) -> tuple[int, int] | None:
        """Return one target-varying collision witness when exactness fails."""
        records = _as_2d(self.records)
        targets = _as_2d(self.targets)
        by_fiber: dict[tuple[float, ...], list[int]] = {}
        for idx, rec in enumerate(records):
            by_fiber.setdefault(_record_key(rec), []).append(idx)
        for members in by_fiber.values():
            if len(members) < 2:
                continue
            for i, j in product(members, members):
                if j <= i:
                    continue
                if _target_distance(targets[i], targets[j]) > float(tol):
                    return int(i), int(j)
        return None

    def recoverability_defect_mse(self) -> float:
        """D(T|Y) = E ||T - E[T|Y]||^2 for discrete record fibers."""
        records = _as_2d(self.records)
        targets = _as_2d(self.targets)
        by_fiber: dict[tuple[float, ...], list[int]] = {}
        for idx, rec in enumerate(records):
            by_fiber.setdefault(_record_key(rec), []).append(idx)
        loss = 0.0
        for members in by_fiber.values():
            block = targets[members]
            mu = block.mean(axis=0, keepdims=True)
            loss += float(((block - mu) ** 2).sum())
        return float(loss / max(len(targets), 1))


@dataclass(frozen=True)
class RestrictedLinearStabilityBoundResult:
    exact_recoverable: bool
    decoder_operator_norm: float | None
    perturbation_operator_norm: float
    predicted_error_upper_bound: float | None
    empirical_max_error: float | None
    upper_bound_holds_on_box_vertices: bool | None


def restricted_linear_stability_bound(
    observation_matrix: Array,
    protected_matrix: Array,
    perturbation_matrix: Array,
    *,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> RestrictedLinearStabilityBoundResult:
    """Restricted linear perturbation bound above exact factorization core.

    If exact recoverability holds and LF = K OF, then under perturbed record
    O' = O + Delta and fixed decoder K we have on coefficient box ||z||_inf<=B:
        ||K O'F z - LF z|| <= ||K Delta F||_2 * ||z||_2
                           <= ||K Delta F||_2 * sqrt(m) * B
    This function checks the bound on box vertices for the declared linear family.
    """

    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    D = np.asarray(perturbation_matrix, dtype=float)
    if O.shape != D.shape:
        raise ValueError("perturbation_matrix must match observation_matrix shape")

    rep = restricted_linear_recoverability(O, L, tol=tol)
    if (not rep.exact_recoverable) or rep.recovery_operator is None:
        return RestrictedLinearStabilityBoundResult(
            exact_recoverable=False,
            decoder_operator_norm=None,
            perturbation_operator_norm=float(np.linalg.norm(D, ord=2)),
            predicted_error_upper_bound=None,
            empirical_max_error=None,
            upper_bound_holds_on_box_vertices=None,
        )

    K = np.asarray(rep.recovery_operator, dtype=float)
    n = O.shape[1]
    kd_norm = float(np.linalg.norm(K @ D, ord=2))
    predicted = float(kd_norm * np.sqrt(float(n)) * float(box_radius))

    empirical = 0.0
    holds = True
    O_pert = O + D
    for signs in product([-1.0, 1.0], repeat=n):
        z = np.asarray(signs, dtype=float) * float(box_radius)
        err = float(np.linalg.norm((K @ O_pert - L) @ z))
        empirical = max(empirical, err)
        if err > predicted + 1e-9:
            holds = False

    return RestrictedLinearStabilityBoundResult(
        exact_recoverable=True,
        decoder_operator_norm=float(np.linalg.norm(K, ord=2)),
        perturbation_operator_norm=float(np.linalg.norm(D, ord=2)),
        predicted_error_upper_bound=predicted,
        empirical_max_error=float(empirical),
        upper_bound_holds_on_box_vertices=holds,
    )


def recoverability_flow_defect(target_values: Array, label_chain: Iterable[Array]) -> list[float]:
    """Scale-indexed D(T|Y_l) across a declared observation/coarse-graining chain."""
    t = _as_2d(target_values)
    flow: list[float] = []
    for labels in label_chain:
        obj = StructuralInformationObject(records=_as_2d(labels), targets=t)
        flow.append(obj.recoverability_defect_mse())
    return flow


def is_monotone(flow: Iterable[float], *, mode: str = "coarsening", tol: float = 1e-10) -> bool:
    vals = [float(v) for v in flow]
    if mode == "coarsening":
        return bool(all(vals[i + 1] >= vals[i] - tol for i in range(len(vals) - 1)))
    if mode == "refinement":
        return bool(all(vals[i + 1] <= vals[i] + tol for i in range(len(vals) - 1)))
    raise ValueError(f"unsupported mode: {mode}")


def _quantile_code(values: Array, bins: int) -> Array:
    x = np.asarray(values, dtype=float).reshape(-1)
    if x.size == 0:
        return np.zeros(0, dtype=int)
    q = np.linspace(0.0, 1.0, int(max(bins, 2)) + 1)
    edges = np.quantile(x, q)
    edges = np.unique(edges)
    if edges.size <= 2:
        return np.zeros_like(x, dtype=int)
    return np.digitize(x, edges[1:-1], right=False).astype(int)


def descriptor_fiber_metrics(
    descriptor_matrix: Array,
    labels: Array,
    *,
    bins: int = 4,
) -> dict[str, float]:
    """DFMI/IDELB metrics on quantized descriptor fibers."""
    x = _as_2d(descriptor_matrix)
    y = np.asarray(labels, dtype=int).reshape(-1)
    if x.shape[0] != y.shape[0]:
        raise ValueError("descriptor_matrix and labels must share sample count")

    qcols = [_quantile_code(x[:, idx], bins=bins) for idx in range(x.shape[1])]
    fibers = list(zip(*qcols, strict=False))

    counts: dict[tuple[int, ...], list[int]] = {}
    for key, lab in zip(fibers, y, strict=True):
        counts.setdefault(key, [0, 0])
        if int(lab) == 1:
            counts[key][1] += 1
        else:
            counts[key][0] += 1

    mixed = 0
    lower = 0
    for n0, n1 in counts.values():
        if n0 > 0 and n1 > 0:
            mixed += 1
        lower += min(n0, n1)

    total_fibers = max(len(counts), 1)
    n = max(len(y), 1)
    return {
        "n_samples": float(len(y)),
        "n_fibers": float(len(counts)),
        "mixed_fibers": float(mixed),
        "DFMI": float(mixed / total_fibers),
        "IDELB": float(lower / n),
    }


def compatibility_lift(baseline_idelb: float, augmented_idelb: float, *, eps: float = 1e-12) -> dict[str, float]:
    b = float(baseline_idelb)
    a = float(augmented_idelb)
    abs_lift = b - a
    rel_lift = abs_lift / max(abs(b), eps)
    return {"CL_abs": float(abs_lift), "CL_rel": float(rel_lift)}


def bayes_error_binary_from_joint(joint_binary: Array) -> float:
    """Bayes 0-1 error for binary target from joint(T,Y)."""
    p = np.asarray(joint_binary, dtype=float)
    if p.ndim != 2 or p.shape[0] != 2:
        raise ValueError("joint_binary must have shape (2, n)")
    z = p / max(float(np.sum(p)), 1e-12)
    py = np.sum(z, axis=0)
    err = 0.0
    for j, pyj in enumerate(py):
        if pyj <= 0:
            continue
        post = z[:, j] / pyj
        err += pyj * min(float(post[0]), float(post[1]))
    return float(err)


def joint_from_binary_target_and_labels(target_binary: Array, labels: Array) -> Array:
    t = np.asarray(target_binary, dtype=int).reshape(-1)
    y = np.asarray(labels, dtype=int).reshape(-1)
    if t.shape[0] != y.shape[0]:
        raise ValueError("target and labels must share sample count")
    y_min = int(np.min(y))
    if y_min < 0:
        y = y - y_min
    k = int(np.max(y)) + 1 if len(y) else 0
    out = np.zeros((2, k), dtype=float)
    for tt, yy in zip(t, y, strict=True):
        out[int(tt), int(yy)] += 1.0
    return out / max(float(len(y)), 1.0)


def experiment_regret_binary(target_binary: Array, fine_labels: Array, compressed_labels: Array) -> float:
    """Decision-theoretic compression regret proxy.

    Regret = BayesErr(compressed experiment) - BayesErr(fine experiment).
    """
    fine = joint_from_binary_target_and_labels(target_binary, fine_labels)
    coarse = joint_from_binary_target_and_labels(target_binary, compressed_labels)
    return float(bayes_error_binary_from_joint(coarse) - bayes_error_binary_from_joint(fine))

