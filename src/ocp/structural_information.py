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


@dataclass(frozen=True)
class PrimitiveObjectEquivalenceCertificate:
    """Restricted certificate linking primitive-object exactness to OCP-030/OCP-031."""

    kernel_inclusion_holds: bool
    linear_decoder_exact: bool
    fiber_constancy_exact: bool
    collapse_modulus_zero: float
    all_equivalent: bool
    kernel_witness_norm_inf: float | None
    witness_pair_present: bool


@dataclass(frozen=True)
class AmountScalarNonReducibilityReport:
    """Certificate for scalar non-reducibility on declared amount-code class."""

    nonreducible: bool
    n_codes: int
    mixed_codes: int
    witness_code: tuple[int, ...] | None
    witness_indices: tuple[int, int] | None


@dataclass(frozen=True)
class GarblingFlowReport:
    """Finite-state dynamic defect flow under target-independent garbling."""

    flow: tuple[float, ...]
    monotone_nondecreasing: bool


@dataclass(frozen=True)
class PrimitiveReparameterizationReport:
    """Restricted reparameterization invariance report for primitive-object exactness."""

    reparameterization_invertible: bool
    baseline_exact: bool
    transformed_exact: bool
    invariance_holds: bool
    baseline_collapse_modulus_zero: float
    transformed_collapse_modulus_zero: float


@dataclass(frozen=True)
class PerturbationRobustnessCertificate:
    """Restricted robustness certificate around the full-column-rank regime."""

    baseline_exact: bool
    baseline_full_column_rank: bool
    sigma_min_of: float
    perturbation_of_norm: float
    guaranteed_exact_by_margin: bool
    exact_after_perturbation: bool


@dataclass(frozen=True)
class NonlinearPostCompositionReport:
    """Finite-family exactness comparison for nonlinear post-composition of records."""

    map_injective_on_records: bool
    exact_before: bool
    exact_after: bool
    exactness_equivalence_holds: bool


@dataclass(frozen=True)
class TargetPostCompositionReport:
    """Finite-family exactness comparison for nonlinear post-composition of targets."""

    map_injective_on_targets: bool
    exact_before: bool
    exact_after: bool
    exactness_equivalence_holds: bool


@dataclass(frozen=True)
class BscHorizonThresholdReport:
    """Threshold-horizon report for BSC semigroup defect floor crossing."""

    epsilon: float
    defect_floor: float
    reached: bool
    horizon: int | None
    flow_prefix: tuple[float, ...]


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


def _null_space(matrix: Array, *, tol: float = EPS) -> Array:
    m = np.asarray(matrix, dtype=float)
    if m.size == 0:
        return np.zeros((m.shape[1], 0), dtype=float)
    _, s, vh = np.linalg.svd(m, full_matrices=True)
    rank = int(np.sum(s > tol))
    return vh[rank:, :].T


def _linear_family_basis(observation_matrix: Array, family_basis: Array | None) -> Array:
    O = np.asarray(observation_matrix, dtype=float)
    if family_basis is None:
        return np.eye(O.shape[1], dtype=float)
    F = np.asarray(family_basis, dtype=float)
    if F.ndim != 2:
        raise ValueError("family_basis must be a 2D array")
    return F


def primitive_object_from_restricted_linear(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    include_zero: bool = True,
) -> StructuralInformationObject:
    """Build finite primitive-object samples for a restricted-linear box family.

    The sampled family uses the coefficient vertex set `z_i in {-B, +B}` and
    optional center `z=0`. This keeps the object finite and deterministic while
    still exposing exactness failures in the supported witness classes.
    """

    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    F = _linear_family_basis(O, family_basis)
    m = int(F.shape[1])
    if m <= 0:
        raise ValueError("family basis must have at least one column")

    z_rows = [np.asarray(signs, dtype=float) * float(box_radius) for signs in product([-1.0, 1.0], repeat=m)]
    if include_zero:
        z_rows.append(np.zeros(m, dtype=float))
    Z = np.asarray(z_rows, dtype=float)
    X = (F @ Z.T).T
    records = (O @ X.T).T
    targets = (L @ X.T).T
    return StructuralInformationObject(records=records, targets=targets)


def primitive_object_ocp_equivalence_certificate(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> PrimitiveObjectEquivalenceCertificate:
    """Restricted equivalence certificate for primitive object exactness.

    On declared finite-dimensional linear families:
    - OCP-031 exactness criterion: `ker(OF) subset ker(LF)`,
    - OCP-030 exactness criterion: target constancy on record fibers.

    The certificate checks both symbolic criteria and finite primitive-object
    witnesses on the declared coefficient-box family. When kernel inclusion
    fails, it injects an analytic collision witness pair to avoid grid-miss
    artifacts.
    """

    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    F = _linear_family_basis(O, family_basis)
    OF = O @ F
    LF = L @ F

    rep = restricted_linear_recoverability(O, L, family_basis=F, tol=tol)
    linear_exact = bool(rep.exact_recoverable)

    null = _null_space(OF, tol=tol)
    kernel_inclusion = True
    witness_h = None
    if null.size > 0:
        leaks = LF @ null
        leak_norms = np.linalg.norm(leaks, axis=0)
        j = int(np.argmax(leak_norms))
        if float(leak_norms[j]) > float(tol):
            kernel_inclusion = False
            witness_h = null[:, j]

    obj = primitive_object_from_restricted_linear(O, L, family_basis=F, box_radius=box_radius, include_zero=True)
    collapse = float(obj.collapse_modulus_zero())
    fiber_exact = bool(collapse <= float(tol))
    witness_present = bool(obj.collision_witness(tol=tol) is not None)

    # If symbolic kernel inclusion fails but the finite grid missed a collision,
    # append analytic witness points (0, scaled null vector) and re-check.
    if (not kernel_inclusion) and (not witness_present) and (witness_h is not None):
        hinf = float(np.max(np.abs(witness_h)))
        if hinf > float(tol):
            scale = float(box_radius / hinf)
            z0 = np.zeros_like(witness_h)
            z1 = scale * witness_h
            X = np.asarray([F @ z0, F @ z1], dtype=float)
            rec = (O @ X.T).T
            tgt = (L @ X.T).T
            augmented = StructuralInformationObject(
                records=np.vstack([_as_2d(obj.records), rec]),
                targets=np.vstack([_as_2d(obj.targets), tgt]),
            )
            collapse = float(augmented.collapse_modulus_zero())
            fiber_exact = bool(collapse <= float(tol))
            witness_present = bool(augmented.collision_witness(tol=tol) is not None)

    all_equiv = bool(kernel_inclusion == linear_exact == fiber_exact)
    return PrimitiveObjectEquivalenceCertificate(
        kernel_inclusion_holds=bool(kernel_inclusion),
        linear_decoder_exact=bool(linear_exact),
        fiber_constancy_exact=bool(fiber_exact),
        collapse_modulus_zero=float(collapse),
        all_equivalent=all_equiv,
        kernel_witness_norm_inf=(None if witness_h is None else float(np.max(np.abs(witness_h)))),
        witness_pair_present=bool(witness_present),
    )


def primitive_object_reparameterization_certificate(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    reparameterization: Array,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> PrimitiveReparameterizationReport:
    """Check exactness invariance under restricted-linear family reparameterization.

    If `x = F z` is reparameterized as `x = F Q u` with invertible `Q`, then the
    represented admissible family is unchanged and exactness verdict should match.
    For non-invertible `Q`, invariance is not guaranteed and can fail.
    """

    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    F = _linear_family_basis(O, family_basis)
    Q = np.asarray(reparameterization, dtype=float)
    if Q.ndim != 2 or Q.shape[0] != F.shape[1]:
        raise ValueError("reparameterization must have shape (m, m2) with m = family basis columns")

    base = primitive_object_ocp_equivalence_certificate(
        O,
        L,
        family_basis=F,
        box_radius=box_radius,
        tol=tol,
    )
    transformed = primitive_object_ocp_equivalence_certificate(
        O,
        L,
        family_basis=F @ Q,
        box_radius=box_radius,
        tol=tol,
    )

    invertible = bool(Q.shape[0] == Q.shape[1] and abs(float(np.linalg.det(Q))) > float(tol))
    invariance = bool(base.fiber_constancy_exact == transformed.fiber_constancy_exact)
    return PrimitiveReparameterizationReport(
        reparameterization_invertible=invertible,
        baseline_exact=bool(base.fiber_constancy_exact),
        transformed_exact=bool(transformed.fiber_constancy_exact),
        invariance_holds=invariance,
        baseline_collapse_modulus_zero=float(base.collapse_modulus_zero),
        transformed_collapse_modulus_zero=float(transformed.collapse_modulus_zero),
    )


def full_column_rank_margin(
    observation_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> float:
    """Smallest singular value of OF when OF has full column rank; otherwise 0."""

    O = np.asarray(observation_matrix, dtype=float)
    F = _linear_family_basis(O, family_basis)
    OF = O @ F
    m = int(OF.shape[1])
    s = np.linalg.svd(OF, full_matrices=False, compute_uv=False)
    if int(np.sum(s > tol)) < m:
        return 0.0
    return float(np.min(s))


def perturbation_robustness_certificate(
    observation_matrix: Array,
    protected_matrix: Array,
    perturbation_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> PerturbationRobustnessCertificate:
    """Restricted robustness certificate for exactness under perturbations.

    If baseline exactness holds and OF has full column rank with margin sigma_min,
    then every perturbation with ||Delta F||_2 < sigma_min keeps OF full-column-rank
    and therefore preserves exactness (kernel becomes trivial).
    """

    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    D = np.asarray(perturbation_matrix, dtype=float)
    F = _linear_family_basis(O, family_basis)
    if D.shape != O.shape:
        raise ValueError("perturbation_matrix must match observation_matrix shape")

    base = restricted_linear_recoverability(O, L, family_basis=F, tol=tol)
    OF = O @ F
    m = int(OF.shape[1])
    rank = int(np.linalg.matrix_rank(OF, tol=tol))
    full_rank = bool(rank == m)
    sigma_min = float(full_column_rank_margin(O, family_basis=F, tol=tol))
    delta_norm = float(np.linalg.norm(D @ F, ord=2))
    guaranteed = bool(base.exact_recoverable and full_rank and delta_norm < sigma_min - float(tol))

    after = restricted_linear_recoverability(O + D, L, family_basis=F, tol=tol)
    return PerturbationRobustnessCertificate(
        baseline_exact=bool(base.exact_recoverable),
        baseline_full_column_rank=full_rank,
        sigma_min_of=float(sigma_min),
        perturbation_of_norm=float(delta_norm),
        guaranteed_exact_by_margin=guaranteed,
        exact_after_perturbation=bool(after.exact_recoverable),
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


def amount_scalar_nonreducibility_certificate(amount_codes: Array, labels: Array) -> AmountScalarNonReducibilityReport:
    """No-go certificate for scalar classifiers of declared amount-code class.

    If two samples share the same amount-code tuple but opposite labels, then no
    deterministic scalar `s(phi(code))` can exactly classify all samples because
    equal inputs map to equal outputs.
    """

    x = _as_2d(amount_codes)
    y = np.asarray(labels, dtype=int).reshape(-1)
    if x.shape[0] != y.shape[0]:
        raise ValueError("amount_codes and labels must share sample count")

    by_code: dict[tuple[int, ...], list[int]] = {}
    for idx in range(x.shape[0]):
        key = tuple(int(v) for v in np.asarray(x[idx], dtype=int).tolist())
        by_code.setdefault(key, []).append(idx)

    mixed = 0
    witness_code = None
    witness_pair = None
    for code, members in by_code.items():
        labs = {int(y[i]) for i in members}
        if len(labs) > 1:
            mixed += 1
            if witness_pair is None:
                i0 = next(i for i in members if int(y[i]) == 0)
                i1 = next(i for i in members if int(y[i]) == 1)
                witness_pair = (int(i0), int(i1))
                witness_code = code

    return AmountScalarNonReducibilityReport(
        nonreducible=bool(mixed > 0),
        n_codes=int(len(by_code)),
        mixed_codes=int(mixed),
        witness_code=witness_code,
        witness_indices=witness_pair,
    )


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


def mmse_binary_from_joint(joint_binary: Array) -> float:
    """Optimal squared-loss Bayes risk for binary target values {0,1}."""
    p = np.asarray(joint_binary, dtype=float)
    if p.ndim != 2 or p.shape[0] != 2:
        raise ValueError("joint_binary must have shape (2, n)")
    z = p / max(float(np.sum(p)), 1e-12)
    py = np.sum(z, axis=0)
    mmse = 0.0
    for j, pyj in enumerate(py):
        if pyj <= 0:
            continue
        q = float(z[1, j] / pyj)
        mmse += pyj * q * (1.0 - q)
    return float(mmse)


def mmse_discrete_from_joint(joint: Array, target_values: Array) -> float:
    """Optimal squared-loss Bayes risk for finite discrete targets.

    Parameters
    ----------
    joint:
        Joint table P(T=i, Y=j) with shape (n_t, n_y).
    target_values:
        Numeric values associated with target states i=0..n_t-1.
    """

    p = np.asarray(joint, dtype=float)
    v = np.asarray(target_values, dtype=float).reshape(-1)
    if p.ndim != 2:
        raise ValueError("joint must be a matrix with shape (n_t, n_y)")
    if p.shape[0] != v.shape[0]:
        raise ValueError("target_values length must match joint target dimension")

    z = p / max(float(np.sum(p)), 1e-12)
    py = np.sum(z, axis=0)
    risk = 0.0
    for j, pyj in enumerate(py):
        if pyj <= 0:
            continue
        post = z[:, j] / pyj
        mu = float(np.dot(post, v))
        risk += pyj * float(np.dot(post, (v - mu) ** 2))
    return float(risk)


def joint_pushforward_through_kernel(joint_binary: Array, kernel: Array) -> Array:
    """Push forward P(T,Y) through target-independent garbling Y' ~ K(.|Y)."""
    j = np.asarray(joint_binary, dtype=float)
    k = np.asarray(kernel, dtype=float)
    if j.ndim != 2:
        raise ValueError("joint must have shape (n_t, n_y)")
    if k.ndim != 2 or k.shape[0] != j.shape[1]:
        raise ValueError("kernel must have shape (n_y, n_y_next)")
    row_sums = np.sum(k, axis=1, keepdims=True)
    if np.any(row_sums <= 0):
        raise ValueError("kernel rows must have positive sum")
    k_norm = k / row_sums
    return j @ k_norm


def garbling_mmse_flow_binary(
    joint_binary: Array,
    kernel: Array,
    *,
    steps: int,
) -> GarblingFlowReport:
    """MMSE flow under repeated target-independent garbling semigroup."""
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    cur = np.asarray(joint_binary, dtype=float)
    vals = [float(mmse_binary_from_joint(cur))]
    for _ in range(steps):
        cur = joint_pushforward_through_kernel(cur, kernel)
        vals.append(float(mmse_binary_from_joint(cur)))
    monotone = bool(all(vals[i + 1] >= vals[i] - 1e-12 for i in range(len(vals) - 1)))
    return GarblingFlowReport(flow=tuple(vals), monotone_nondecreasing=monotone)


def garbling_mmse_flow_discrete(
    joint: Array,
    target_values: Array,
    kernel: Array,
    *,
    steps: int,
) -> GarblingFlowReport:
    """MMSE flow for finite targets under repeated target-independent garbling."""

    if steps < 0:
        raise ValueError("steps must be nonnegative")
    cur = np.asarray(joint, dtype=float)
    vals = [float(mmse_discrete_from_joint(cur, target_values))]
    for _ in range(steps):
        cur = joint_pushforward_through_kernel(cur, kernel)
        vals.append(float(mmse_discrete_from_joint(cur, target_values)))
    monotone = bool(all(vals[i + 1] >= vals[i] - 1e-12 for i in range(len(vals) - 1)))
    return GarblingFlowReport(flow=tuple(vals), monotone_nondecreasing=monotone)


def bsc_effective_flip_probability(epsilon: float, steps: int) -> float:
    """Effective flip probability for t-step composition of BSC(epsilon)."""

    eps = float(epsilon)
    if not (0.0 <= eps <= 0.5):
        raise ValueError("epsilon must be in [0, 0.5]")
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    return float(0.5 * (1.0 - (1.0 - 2.0 * eps) ** float(steps)))


def bsc_mmse_flow_from_perfect_observation(
    epsilon: float,
    *,
    steps: int,
) -> GarblingFlowReport:
    """Closed-form MMSE flow for binary target from perfect record then BSC semigroup.

    Assumes:
    - binary target with prior 0.5,
    - initial record is exact target label,
    - each step applies BSC(epsilon) target-independently.
    """

    eps = float(epsilon)
    if not (0.0 <= eps <= 0.5):
        raise ValueError("epsilon must be in [0, 0.5]")
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    vals: list[float] = []
    for t in range(steps + 1):
        e_t = bsc_effective_flip_probability(eps, t)
        vals.append(float(e_t * (1.0 - e_t)))
    monotone = bool(all(vals[i + 1] >= vals[i] - 1e-12 for i in range(len(vals) - 1)))
    return GarblingFlowReport(flow=tuple(vals), monotone_nondecreasing=monotone)


def bsc_horizon_threshold(
    epsilon: float,
    defect_floor: float,
    *,
    max_steps: int = 10_000,
) -> BscHorizonThresholdReport:
    """Minimal horizon where BSC semigroup MMSE reaches a declared defect floor."""

    eps = float(epsilon)
    floor = float(defect_floor)
    if not (0.0 <= eps <= 0.5):
        raise ValueError("epsilon must be in [0, 0.5]")
    if not (0.0 <= floor <= 0.25):
        raise ValueError("defect_floor must be in [0, 0.25]")
    if max_steps < 0:
        raise ValueError("max_steps must be nonnegative")
    flow: list[float] = []
    reached = False
    horizon: int | None = None
    for t in range(max_steps + 1):
        e_t = bsc_effective_flip_probability(eps, t)
        d_t = float(e_t * (1.0 - e_t))
        flow.append(d_t)
        if d_t >= floor - 1e-12:
            reached = True
            horizon = t
            break
    return BscHorizonThresholdReport(
        epsilon=eps,
        defect_floor=floor,
        reached=reached,
        horizon=horizon,
        flow_prefix=tuple(flow),
    )


def target_dependent_transition_no_go_example() -> GarblingFlowReport:
    """Counterexample: target-dependent transition can reduce defect.

    Start from no-information records (single label) and then emit target as the
    next record. This violates target-independent garbling assumptions and yields
    a strict MMSE decrease, so broad monotonicity fails without assumptions.
    """

    # Joint for binary target with a single uninformative record symbol.
    joint0 = np.asarray([[0.5], [0.5]], dtype=float)
    mmse0 = float(mmse_binary_from_joint(joint0))  # = 0.25

    # Target-dependent transition creates perfect information in one step.
    joint1 = np.asarray(
        [
            [0.5, 0.0],
            [0.0, 0.5],
        ],
        dtype=float,
    )
    mmse1 = float(mmse_binary_from_joint(joint1))  # = 0.0
    flow = (mmse0, mmse1)
    return GarblingFlowReport(flow=flow, monotone_nondecreasing=bool(flow[1] >= flow[0] - 1e-12))


def postcomposition_exactness_report(
    records: Array,
    targets: Array,
    post_map: Callable[[Array], Array],
    *,
    tol: float = EPS,
) -> NonlinearPostCompositionReport:
    """Finite-family exactness report for nonlinear post-composition of records."""

    rec = _as_2d(records)
    tgt = _as_2d(targets)
    if rec.shape[0] != tgt.shape[0]:
        raise ValueError("records and targets must share sample count")
    before = StructuralInformationObject(records=rec, targets=tgt)
    transformed = _as_2d(post_map(rec))
    if transformed.shape[0] != rec.shape[0]:
        raise ValueError("post_map must preserve sample count")
    after = StructuralInformationObject(records=transformed, targets=tgt)

    # Injective on sampled records means transformed keys are unique per record key.
    rec_keys = [_record_key(r) for r in rec]
    tr_keys = [_record_key(r) for r in transformed]
    pair_map: dict[tuple[float, ...], tuple[float, ...]] = {}
    injective = True
    for rk, tk in zip(rec_keys, tr_keys, strict=True):
        if rk in pair_map and pair_map[rk] != tk:
            injective = False
            break
        pair_map[rk] = tk
    # Also require no collision between distinct record keys.
    if injective:
        reverse: dict[tuple[float, ...], tuple[float, ...]] = {}
        for rk, tk in pair_map.items():
            if tk in reverse and reverse[tk] != rk:
                injective = False
                break
            reverse[tk] = rk

    exact_before = bool(before.exact_recoverable(tol=tol))
    exact_after = bool(after.exact_recoverable(tol=tol))
    return NonlinearPostCompositionReport(
        map_injective_on_records=injective,
        exact_before=exact_before,
        exact_after=exact_after,
        exactness_equivalence_holds=bool(exact_before == exact_after),
    )


def target_postcomposition_exactness_report(
    records: Array,
    targets: Array,
    target_map: Callable[[Array], Array],
    *,
    tol: float = EPS,
) -> TargetPostCompositionReport:
    """Finite-family exactness report for nonlinear post-composition of targets.

    If the target post-map is injective on realized target support, exactness is
    preserved. Non-injective target coarsening can convert nonexact fine targets
    into exact coarse targets on the same record map.
    """

    rec = _as_2d(records)
    tgt = _as_2d(targets)
    if rec.shape[0] != tgt.shape[0]:
        raise ValueError("records and targets must share sample count")

    before = StructuralInformationObject(records=rec, targets=tgt)
    mapped = _as_2d(target_map(tgt))
    if mapped.shape[0] != tgt.shape[0]:
        raise ValueError("target_map must preserve sample count")
    after = StructuralInformationObject(records=rec, targets=mapped)

    tgt_keys = [_record_key(v) for v in tgt]
    map_keys = [_record_key(v) for v in mapped]
    pair_map: dict[tuple[float, ...], tuple[float, ...]] = {}
    injective = True
    for tk, mk in zip(tgt_keys, map_keys, strict=True):
        if tk in pair_map and pair_map[tk] != mk:
            injective = False
            break
        pair_map[tk] = mk
    if injective:
        reverse: dict[tuple[float, ...], tuple[float, ...]] = {}
        for tk, mk in pair_map.items():
            if mk in reverse and reverse[mk] != tk:
                injective = False
                break
            reverse[mk] = tk

    exact_before = bool(before.exact_recoverable(tol=tol))
    exact_after = bool(after.exact_recoverable(tol=tol))
    return TargetPostCompositionReport(
        map_injective_on_targets=injective,
        exact_before=exact_before,
        exact_after=exact_after,
        exactness_equivalence_holds=bool(exact_before == exact_after),
    )


def amount_scalar_exact_classifier_possible(amount_codes: Array, labels: Array) -> bool:
    """Exact deterministic classifier feasibility from declared amount-code classes.

    Feasible iff every amount-code class has a single label value.
    """

    rep = amount_scalar_nonreducibility_certificate(amount_codes, labels)
    return bool(not rep.nonreducible)
