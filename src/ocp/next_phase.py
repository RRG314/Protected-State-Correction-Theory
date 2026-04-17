from __future__ import annotations

"""Next-phase quantitative/stability/dynamic helpers.

This module deepens the theorem-first recoverability program from binary
exact/impossible outputs into computable quantitative and fragility layers.
All helpers are intentionally scoped to finite/restricted-linear or already-
validated bounded-domain and generator lanes.
"""

from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np

from .cfd import cfd_projection_summary
from .continuous import LinearOCPFlow
from .design import linear_recoverability_design_report
from .recoverability import (
    EPS,
    Array,
    restricted_linear_collision_gap,
    restricted_linear_recoverability,
    restricted_linear_rowspace_residual,
)


def _orthonormal_columns(matrix: Array, *, tol: float = EPS) -> Array:
    mat = np.asarray(matrix, dtype=float)
    if mat.ndim == 1:
        mat = mat[:, None]
    if mat.size == 0:
        return np.zeros((mat.shape[0], 0), dtype=float)
    u, s, _ = np.linalg.svd(mat, full_matrices=False)
    rank = int(np.sum(s > tol))
    if rank == 0:
        return np.zeros((mat.shape[0], 0), dtype=float)
    return u[:, :rank].copy()


def _family_basis(dimension: int, family_basis: Array | None, *, tol: float = EPS) -> Array:
    if family_basis is None:
        return np.eye(int(dimension), dtype=float)
    return _orthonormal_columns(np.asarray(family_basis, dtype=float), tol=tol)


def _effective_matrices(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> tuple[Array, Array]:
    observation = np.asarray(observation_matrix, dtype=float)
    protected = np.asarray(protected_matrix, dtype=float)
    basis = _family_basis(observation.shape[1], family_basis, tol=tol)
    return observation @ basis, protected @ basis


def _rowspace_basis(matrix: Array, *, tol: float = EPS) -> Array:
    mat = np.asarray(matrix, dtype=float)
    if mat.ndim == 1:
        mat = mat[None, :]
    if mat.size == 0:
        return np.zeros((mat.shape[1], 0), dtype=float)
    _, s, vh = np.linalg.svd(mat, full_matrices=False)
    rank = int(np.sum(s > tol))
    if rank == 0:
        return np.zeros((mat.shape[1], 0), dtype=float)
    return vh[:rank, :].T.copy()


def principal_angle_defect(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> float:
    """Return sin(theta_max) between row(protected) and row(observation).

    Value is in [0,1]. Exact recoverability in the restricted-linear branch
    is equivalent to this defect being zero.
    """

    OF, LF = _effective_matrices(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    target_basis = _rowspace_basis(LF, tol=tol)
    obs_basis = _rowspace_basis(OF, tol=tol)

    target_dim = int(target_basis.shape[1])
    obs_dim = int(obs_basis.shape[1])
    if target_dim == 0:
        return 0.0
    if obs_dim == 0:
        return 1.0

    cosines = np.linalg.svd(target_basis.T @ obs_basis, compute_uv=False)
    if target_dim > obs_dim:
        min_cos = 0.0
    else:
        min_cos = float(np.min(cosines)) if cosines.size else 0.0
    min_cos = float(np.clip(min_cos, 0.0, 1.0))
    return float(np.sqrt(max(0.0, 1.0 - min_cos * min_cos)))


def normalized_rowspace_defect(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> float:
    OF, LF = _effective_matrices(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    if np.linalg.norm(LF, ord=2) <= tol:
        return 0.0
    residual = restricted_linear_rowspace_residual(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    return float(residual / np.linalg.norm(LF, ord=2))


@dataclass(frozen=True)
class QuantitativeRecoverabilityProfile:
    exact_recoverable: bool
    coefficient_dimension: int
    observation_rank: int
    protected_rank: int
    rowspace_residual: float
    normalized_rowspace_residual: float
    principal_angle_defect: float
    alignment_score: float
    collision_gap: float
    zero_noise_lower_bound: float
    recovery_operator_norm_upper: float | None
    unrestricted_minimal_added_measurements: int
    structural_class: str


@dataclass(frozen=True)
class ObservationPerturbationRow:
    epsilon: float
    exact_recoverable: bool
    rowspace_residual: float
    principal_angle_defect: float
    collision_gap: float


@dataclass(frozen=True)
class ObservationPerturbationSweep:
    base_exact_recoverable: bool
    base_rowspace_residual: float
    base_principal_angle_defect: float
    base_collision_gap: float
    first_failure_epsilon: float | None
    rows: tuple[ObservationPerturbationRow, ...]


@dataclass(frozen=True)
class DynamicAccumulationRow:
    step: int
    exact_recoverable: bool
    rowspace_residual: float
    principal_angle_defect: float
    collision_gap: float
    unrestricted_minimal_added_measurements: int


@dataclass(frozen=True)
class DynamicAccumulationReport:
    exact_threshold_step: int | None
    rows: tuple[DynamicAccumulationRow, ...]


@dataclass(frozen=True)
class GeneratorDynamicsRow:
    time: float
    disturbance_norm: float
    predicted_upper_bound: float
    ratio_to_bound: float | None


@dataclass(frozen=True)
class GeneratorDynamicsReport:
    disturbance_decay_margin: float
    finite_time_exact_recovery_possible: bool
    rows: tuple[GeneratorDynamicsRow, ...]


@dataclass(frozen=True)
class CfdDeepDiveRow:
    grid_size: int
    contamination: float
    periodic_divergence_suppression: float
    periodic_recovery_error: float
    transplant_divergence_suppression: float
    transplant_boundary_normal_rms: float
    bounded_hodge_recovery_error: float
    bounded_hodge_boundary_normal_rms: float
    bounded_hodge_vs_transplant_boundary_ratio: float


@dataclass(frozen=True)
class StructureClassRow:
    case_name: str
    structural_class: str
    exact_recoverable: bool
    observation_rank: int
    coefficient_dimension: int
    rowspace_residual: float
    principal_angle_defect: float
    collision_gap: float
    unrestricted_minimal_added_measurements: int


_FULL_INFORMATION_CLASS = "robust_exact_full_information"
_FRAGILE_EXACT_CLASS = "aligned_exact_but_fragile"
_REPAIRABLE_CLASS = "augmentation_repairable_misaligned"
_COLLISION_CLASS = "collision_dominated_impossible"
_MISALIGNED_CLASS = "misaligned_impossible"


def classify_structure(
    *,
    exact_recoverable: bool,
    observation_rank: int,
    coefficient_dimension: int,
    collision_gap: float,
    unrestricted_minimal_added_measurements: int,
    tol: float = EPS,
) -> str:
    if exact_recoverable:
        if observation_rank >= coefficient_dimension:
            return _FULL_INFORMATION_CLASS
        return _FRAGILE_EXACT_CLASS
    if unrestricted_minimal_added_measurements > 0:
        return _REPAIRABLE_CLASS
    if collision_gap > tol:
        return _COLLISION_CLASS
    return _MISALIGNED_CLASS


def quantitative_recoverability_profile(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> QuantitativeRecoverabilityProfile:
    linear = restricted_linear_recoverability(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    design = linear_recoverability_design_report(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    OF, LF = _effective_matrices(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    row_residual = float(
        restricted_linear_rowspace_residual(
            observation_matrix,
            protected_matrix,
            family_basis=family_basis,
            tol=tol,
        )
    )
    angle_defect = float(
        principal_angle_defect(
            observation_matrix,
            protected_matrix,
            family_basis=family_basis,
            tol=tol,
        )
    )
    alignment = float(max(0.0, 1.0 - angle_defect))
    gap = float(
        restricted_linear_collision_gap(
            observation_matrix,
            protected_matrix,
            family_basis=family_basis,
            box_radius=box_radius,
            tol=tol,
        )
    )
    op_norm = None
    if linear.exact_recoverable and linear.recovery_operator is not None:
        op_norm = float(np.linalg.norm(linear.recovery_operator, ord=2))
    structure = classify_structure(
        exact_recoverable=bool(linear.exact_recoverable),
        observation_rank=int(np.linalg.matrix_rank(OF, tol)),
        coefficient_dimension=int(OF.shape[1]),
        collision_gap=gap,
        unrestricted_minimal_added_measurements=int(design.unrestricted_minimal_added_measurements),
        tol=tol,
    )
    return QuantitativeRecoverabilityProfile(
        exact_recoverable=bool(linear.exact_recoverable),
        coefficient_dimension=int(OF.shape[1]),
        observation_rank=int(np.linalg.matrix_rank(OF, tol)),
        protected_rank=int(np.linalg.matrix_rank(LF, tol)),
        rowspace_residual=row_residual,
        normalized_rowspace_residual=float(normalized_rowspace_defect(observation_matrix, protected_matrix, family_basis=family_basis, tol=tol)),
        principal_angle_defect=angle_defect,
        alignment_score=alignment,
        collision_gap=gap,
        zero_noise_lower_bound=float(0.5 * gap),
        recovery_operator_norm_upper=op_norm,
        unrestricted_minimal_added_measurements=int(design.unrestricted_minimal_added_measurements),
        structural_class=structure,
    )


def perturb_observation_sweep(
    observation_matrix: Array,
    protected_matrix: Array,
    perturbation_direction: Array,
    epsilons: Iterable[float],
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> ObservationPerturbationSweep:
    observation = np.asarray(observation_matrix, dtype=float)
    direction = np.asarray(perturbation_direction, dtype=float)
    if observation.shape != direction.shape:
        raise ValueError("perturbation_direction must match observation_matrix shape")
    norm = float(np.linalg.norm(direction, ord="fro"))
    if norm <= tol:
        raise ValueError("perturbation_direction must be nonzero")
    unit = direction / norm

    base = quantitative_recoverability_profile(
        observation,
        protected_matrix,
        family_basis=family_basis,
        box_radius=box_radius,
        tol=tol,
    )

    rows: list[ObservationPerturbationRow] = []
    first_failure = None
    for raw_eps in epsilons:
        epsilon = float(raw_eps)
        perturbed = observation + epsilon * unit
        profile = quantitative_recoverability_profile(
            perturbed,
            protected_matrix,
            family_basis=family_basis,
            box_radius=box_radius,
            tol=tol,
        )
        rows.append(
            ObservationPerturbationRow(
                epsilon=epsilon,
                exact_recoverable=bool(profile.exact_recoverable),
                rowspace_residual=float(profile.rowspace_residual),
                principal_angle_defect=float(profile.principal_angle_defect),
                collision_gap=float(profile.collision_gap),
            )
        )
        if first_failure is None and base.exact_recoverable and (not profile.exact_recoverable):
            first_failure = epsilon

    return ObservationPerturbationSweep(
        base_exact_recoverable=bool(base.exact_recoverable),
        base_rowspace_residual=float(base.rowspace_residual),
        base_principal_angle_defect=float(base.principal_angle_defect),
        base_collision_gap=float(base.collision_gap),
        first_failure_epsilon=first_failure,
        rows=tuple(rows),
    )


def canonical_rank_deficient_fragility_sweep(
    epsilons: Iterable[float],
    *,
    ambient_dimension: int = 4,
    observation_rank: int = 2,
    tol: float = EPS,
) -> ObservationPerturbationSweep:
    n = int(ambient_dimension)
    k = int(observation_rank)
    if not (1 <= k < n):
        raise ValueError("observation_rank must satisfy 1 <= observation_rank < ambient_dimension")

    observation = np.eye(n, dtype=float)[:k, :]
    protected = np.asarray([[1.0] + [0.0] * (n - 1)], dtype=float)
    direction = np.zeros_like(observation)
    direction[0, k] = 1.0

    return perturb_observation_sweep(
        observation,
        protected,
        direction,
        epsilons,
        box_radius=1.0,
        tol=tol,
    )


def full_rank_robustness_sweep(
    epsilons: Iterable[float],
    *,
    tol: float = EPS,
) -> ObservationPerturbationSweep:
    observation = np.asarray(
        [
            [2.0, 0.1, 0.0],
            [0.0, 1.5, 0.2],
            [0.0, 0.0, 1.1],
        ],
        dtype=float,
    )
    protected = np.asarray([[0.7, -0.4, 0.5]], dtype=float)
    direction = np.asarray(
        [
            [0.0, 1.0, 0.0],
            [1.0, 0.0, -1.0],
            [0.0, 1.0, 1.0],
        ],
        dtype=float,
    )
    return perturb_observation_sweep(observation, protected, direction, epsilons, box_radius=1.0, tol=tol)


def time_accumulated_recoverability_profile(
    observation_sequence: Sequence[Array],
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> DynamicAccumulationReport:
    if not observation_sequence:
        raise ValueError("observation_sequence must be nonempty")

    rows: list[DynamicAccumulationRow] = []
    exact_threshold = None
    stacked = np.asarray(observation_sequence[0], dtype=float)
    for index, observation in enumerate(observation_sequence, start=1):
        if index == 1:
            stacked = np.asarray(observation, dtype=float)
        else:
            stacked = np.vstack([stacked, np.asarray(observation, dtype=float)])
        profile = quantitative_recoverability_profile(
            stacked,
            protected_matrix,
            family_basis=family_basis,
            box_radius=box_radius,
            tol=tol,
        )
        rows.append(
            DynamicAccumulationRow(
                step=index,
                exact_recoverable=bool(profile.exact_recoverable),
                rowspace_residual=float(profile.rowspace_residual),
                principal_angle_defect=float(profile.principal_angle_defect),
                collision_gap=float(profile.collision_gap),
                unrestricted_minimal_added_measurements=int(profile.unrestricted_minimal_added_measurements),
            )
        )
        if exact_threshold is None and profile.exact_recoverable:
            exact_threshold = index

    return DynamicAccumulationReport(exact_threshold_step=exact_threshold, rows=tuple(rows))


def canonical_time_accumulation_example(*, tol: float = EPS) -> DynamicAccumulationReport:
    sequence = (
        np.asarray([[1.0, 0.0, 0.0, 0.0]], dtype=float),
        np.asarray([[0.0, 1.0, 0.0, 0.0]], dtype=float),
        np.asarray([[0.0, 0.0, 1.0, 0.0]], dtype=float),
        np.asarray([[0.0, 0.0, 0.0, 1.0]], dtype=float),
    )
    protected = np.asarray([[0.0, 0.0, 1.0, 1.0]], dtype=float)
    return time_accumulated_recoverability_profile(sequence, protected, tol=tol)


def generator_dynamics_profile(
    flow: LinearOCPFlow,
    x0: Array,
    times: Iterable[float],
    *,
    tol: float = EPS,
) -> GeneratorDynamicsReport:
    report = flow.report()
    rows: list[GeneratorDynamicsRow] = []
    for raw_time in times:
        time = float(raw_time)
        evolved = flow.flow(x0, time)
        disturbance = float(flow.disturbance_norm(evolved))
        bound = float(flow.asymptotic_bound(x0, time))
        ratio = None
        if np.isfinite(bound) and bound > tol:
            ratio = float(disturbance / bound)
        rows.append(
            GeneratorDynamicsRow(
                time=time,
                disturbance_norm=disturbance,
                predicted_upper_bound=bound,
                ratio_to_bound=ratio,
            )
        )
    finite_exact = any(flow.finite_time_exact_recovery_possible(float(t)) for t in times if float(t) > 0.0)
    return GeneratorDynamicsReport(
        disturbance_decay_margin=float(report.disturbance_decay_margin),
        finite_time_exact_recovery_possible=bool(finite_exact),
        rows=tuple(rows),
    )


def cfd_deep_dive_sweep(
    grid_sizes: Iterable[int],
    contaminations: Iterable[float],
    *,
    tol: float = EPS,
) -> tuple[CfdDeepDiveRow, ...]:
    rows: list[CfdDeepDiveRow] = []
    contamination_values = tuple(float(value) for value in contaminations)
    for n in grid_sizes:
        grid = int(n)
        for contamination in contamination_values:
            summary = cfd_projection_summary(
                n_periodic=max(24, grid),
                n_bounded=max(16, grid),
                contamination=contamination,
            )
            periodic_suppression = float(
                summary.periodic.before_l2_divergence
                / max(summary.periodic.after_projection_l2_divergence, tol)
            )
            transplant_suppression = float(
                summary.bounded_transplant.before_l2_divergence
                / max(summary.bounded_transplant.after_periodic_projection_l2_divergence, tol)
            )
            boundary_ratio = float(
                summary.bounded_transplant.projected_boundary_normal_rms
                / max(summary.bounded_hodge_exact.recovered_boundary_normal_rms, tol)
            )
            rows.append(
                CfdDeepDiveRow(
                    grid_size=grid,
                    contamination=contamination,
                    periodic_divergence_suppression=periodic_suppression,
                    periodic_recovery_error=float(summary.periodic.recovery_l2_error),
                    transplant_divergence_suppression=transplant_suppression,
                    transplant_boundary_normal_rms=float(summary.bounded_transplant.projected_boundary_normal_rms),
                    bounded_hodge_recovery_error=float(summary.bounded_hodge_exact.recovery_l2_error),
                    bounded_hodge_boundary_normal_rms=float(summary.bounded_hodge_exact.recovered_boundary_normal_rms),
                    bounded_hodge_vs_transplant_boundary_ratio=boundary_ratio,
                )
            )
    return tuple(rows)


def canonical_structure_classes(*, tol: float = EPS) -> tuple[StructureClassRow, ...]:
    cases = (
        (
            "robust-full-information",
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 1.0],
                ],
                dtype=float,
            ),
            np.asarray([[0.0, 0.0, 1.0]], dtype=float),
        ),
        (
            "exact-but-fragile-rank-deficient",
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                ],
                dtype=float,
            ),
            np.asarray([[1.0, 0.0, 0.0]], dtype=float),
        ),
        (
            "augmentation-repairable",
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 1.0],
                ],
                dtype=float,
            ),
            np.asarray([[0.0, 0.0, 1.0]], dtype=float),
        ),
    )

    out: list[StructureClassRow] = []
    for name, observation, protected in cases:
        profile = quantitative_recoverability_profile(
            observation,
            protected,
            box_radius=1.0,
            tol=tol,
        )
        out.append(
            StructureClassRow(
                case_name=name,
                structural_class=profile.structural_class,
                exact_recoverable=bool(profile.exact_recoverable),
                observation_rank=int(profile.observation_rank),
                coefficient_dimension=int(profile.coefficient_dimension),
                rowspace_residual=float(profile.rowspace_residual),
                principal_angle_defect=float(profile.principal_angle_defect),
                collision_gap=float(profile.collision_gap),
                unrestricted_minimal_added_measurements=int(profile.unrestricted_minimal_added_measurements),
            )
        )

    return tuple(out)


__all__ = [
    "QuantitativeRecoverabilityProfile",
    "ObservationPerturbationRow",
    "ObservationPerturbationSweep",
    "DynamicAccumulationRow",
    "DynamicAccumulationReport",
    "GeneratorDynamicsRow",
    "GeneratorDynamicsReport",
    "CfdDeepDiveRow",
    "StructureClassRow",
    "principal_angle_defect",
    "normalized_rowspace_defect",
    "classify_structure",
    "quantitative_recoverability_profile",
    "perturb_observation_sweep",
    "canonical_rank_deficient_fragility_sweep",
    "full_rank_robustness_sweep",
    "time_accumulated_recoverability_profile",
    "canonical_time_accumulation_example",
    "generator_dynamics_profile",
    "cfd_deep_dive_sweep",
    "canonical_structure_classes",
]
