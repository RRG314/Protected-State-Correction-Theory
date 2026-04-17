from __future__ import annotations

"""Canonical helpers for the fiber-based recoverability / impossibility branch.

This module preserves the earlier executable unified-branch witnesses while
making the fiber language explicit in the local branch's code organization.
The current functions are intentionally restricted to finite or restricted-linear
families where the repo has honest theorem support or executable cross-checks.
"""

from dataclasses import dataclass
from itertools import combinations, product
from typing import Iterable, Sequence

import numpy as np

from .recoverability import (
    Array,
    EPS,
    _periodic_modal_basis_states,
    _truncate_vorticity,
    finite_recoverability_report,
    functional_observability_sweep,
    restricted_linear_collision_gap,
    restricted_linear_rank_lower_bound,
    restricted_linear_recoverability,
    restricted_linear_rowspace_residual,
    same_rank_alignment_counterexample,
)


@dataclass(frozen=True)
class FiniteTargetHierarchyReport:
    strong_exact_recoverable: bool
    weak_exact_recoverable: bool
    detectable_only: bool
    strong_collision_gap: float
    weak_collision_gap: float
    strong_witness_pair: tuple[int, int] | None
    weak_witness_pair: tuple[int, int] | None


@dataclass(frozen=True)
class RestrictedLinearTargetHierarchyReport:
    strong_exact_recoverable: bool
    weak_exact_recoverable: bool
    detectable_only: bool
    strong_rowspace_residual: float
    weak_rowspace_residual: float
    strong_collision_gap: float
    weak_collision_gap: float


@dataclass(frozen=True)
class RankOnlyClassifierFailureRow:
    ambient_dimension: int
    protected_rank: int
    observation_rank: int
    exact_rank_observation: int
    fail_rank_observation: int
    exact_recoverable: bool
    fail_recoverable: bool
    exact_rowspace_residual: float
    fail_rowspace_residual: float
    exact_collision_gap: float
    fail_collision_gap: float


@dataclass(frozen=True)
class RankOnlyClassifierFailureReport:
    witness_count: int
    all_same_rank: bool
    all_opposite_verdicts: bool
    rows: tuple[RankOnlyClassifierFailureRow, ...]


@dataclass(frozen=True)
class CoordinateRankEnumerationRow:
    ambient_dimension: int
    protected_rank: int
    observation_rank: int
    exact_count: int
    fail_count: int


@dataclass(frozen=True)
class CoordinateRankEnumerationReport:
    rows: tuple[CoordinateRankEnumerationRow, ...]
    all_levels_have_exact_and_fail: bool


@dataclass(frozen=True)
class CandidateLibraryBudgetRow:
    ambient_dimension: int
    protected_rank: int
    selection_size: int
    exact_count: int
    fail_count: int
    exact_subset: tuple[int, ...]
    fail_subset: tuple[int, ...]
    exact_total_cost: float
    fail_total_cost: float


@dataclass(frozen=True)
class CandidateLibraryBudgetReport:
    witness_count: int
    all_levels_have_exact_and_fail: bool
    rows: tuple[CandidateLibraryBudgetRow, ...]


@dataclass(frozen=True)
class NoisyHierarchyRow:
    noise_radius: float
    weak_upper_bound: float
    weak_bruteforce_max_error: float
    strong_uniform_lower_bound: float
    strong_discrete_collision_gap: float
    separated: bool


@dataclass(frozen=True)
class NoisyRestrictedLinearTargetHierarchyReport:
    weak_exact_recoverable: bool
    strong_exact_recoverable: bool
    detectable_only: bool
    weak_decoder_operator_norm: float
    strong_collision_gap: float
    strong_uniform_lower_bound: float
    separation_noise_threshold: float | None
    weak_discrete_collision_gap: float
    strong_discrete_collision_gap: float
    rows: tuple[NoisyHierarchyRow, ...]


@dataclass(frozen=True)
class ControlRegimeHierarchyReport:
    epsilon: float
    one_step_exact_recoverable: bool
    two_step_exact_recoverable: bool
    observer_asymptotic_recoverable: bool
    one_step_collision_gap: float
    two_step_collision_gap: float
    observer_spectral_radius: float
    observer_final_protected_error: float


@dataclass(frozen=True)
class RestrictedLinearFiberGeometryReport:
    coefficient_dimension: int
    observation_rank: int
    fiber_dimension: int
    exact_recoverable: bool
    target_mixed_fiber: bool
    rowspace_residual: float
    collision_gap: float


@dataclass(frozen=True)
class RestrictedLinearFamilyEnlargementReport:
    small_family_dimension: int
    large_family_dimension: int
    inclusion_residual: float
    small_exact_recoverable: bool
    large_exact_recoverable: bool
    small_rowspace_residual: float
    large_rowspace_residual: float
    small_collision_gap: float
    large_collision_gap: float
    false_positive_risk: bool
    larger_family_impossibility_lower_bound: float
    reference_decoder_max_error_on_large_family: float | None
    reference_decoder_mean_error_on_large_family: float | None


@dataclass(frozen=True)
class RestrictedLinearModelMismatchRow:
    label: str
    family_dimension: int
    subspace_distance: float
    exact_recoverable_under_true_family: bool
    rowspace_residual: float
    collision_gap: float
    reference_decoder_max_error: float | None
    reference_decoder_mean_error: float | None


@dataclass(frozen=True)
class RestrictedLinearModelMismatchReport:
    reference_exact_recoverable: bool
    reference_family_dimension: int
    reference_decoder_operator_norm: float | None
    rows: tuple[RestrictedLinearModelMismatchRow, ...]


@dataclass(frozen=True)
class CanonicalModelMismatchRow:
    beta_true: float
    beta_reference: float
    exact_recoverable_true_family: bool
    subspace_distance: float
    formula_max_error: float
    brute_force_max_error: float
    brute_force_mean_error: float


@dataclass(frozen=True)
class CanonicalModelMismatchReport:
    beta_reference: float
    reference_exact_recoverable: bool
    reference_decoder_operator_norm: float | None
    rows: tuple[CanonicalModelMismatchRow, ...]


@dataclass(frozen=True)
class PeriodicModalRefinementReport:
    cutoff: int
    coarse_mode_count: int
    refined_mode_count: int
    coarse_exact_recoverable: bool
    refined_exact_recoverable: bool
    coarse_collision_gap: float
    refined_collision_gap: float
    refinement_false_positive_risk: bool
    refined_family_impossibility_lower_bound: float
    coarse_decoder_max_error_on_refined_family: float | None
    coarse_decoder_mean_error_on_refined_family: float | None


def _family_basis_matrix(
    observation_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> Array:
    observation = np.asarray(observation_matrix, dtype=float)
    if family_basis is None:
        return np.eye(observation.shape[1], dtype=float)
    basis = np.asarray(family_basis, dtype=float)
    if basis.ndim == 1:
        basis = basis[:, None]
    q, _ = np.linalg.qr(basis)
    keep = [index for index in range(q.shape[1]) if np.linalg.norm(q[:, index]) > tol]
    return q[:, keep] if keep else np.zeros((basis.shape[0], 0), dtype=float)


def _orthonormal_family_basis(
    family_basis: Array,
    *,
    tol: float = EPS,
) -> Array:
    basis = np.asarray(family_basis, dtype=float)
    if basis.ndim == 1:
        basis = basis[:, None]
    q, _ = np.linalg.qr(basis)
    keep = [index for index in range(q.shape[1]) if np.linalg.norm(q[:, index]) > tol]
    return q[:, keep] if keep else np.zeros((basis.shape[0], 0), dtype=float)


def _restricted_family_matrices(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> tuple[Array, Array]:
    basis = _family_basis_matrix(observation_matrix, family_basis=family_basis, tol=tol)
    return np.asarray(observation_matrix, dtype=float) @ basis, np.asarray(protected_matrix, dtype=float) @ basis


def _coefficient_grid_points(
    dimension: int,
    coefficient_values: Sequence[float],
) -> tuple[Array, ...]:
    values = tuple(float(value) for value in coefficient_values)
    if dimension <= 0:
        return (np.zeros(0, dtype=float),)
    return tuple(np.asarray(point, dtype=float) for point in product(values, repeat=dimension))


def _discrete_restricted_linear_collision_gap(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    coefficient_values: Sequence[float] = (-1.0, 0.0, 1.0),
    tol: float = EPS,
) -> float:
    OF, LF = _restricted_family_matrices(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    points = _coefficient_grid_points(OF.shape[1], coefficient_values)
    max_gap = 0.0
    for left, right in combinations(points, 2):
        if np.linalg.norm(OF @ (left - right)) <= tol:
            max_gap = max(max_gap, float(np.linalg.norm(LF @ (left - right))))
    return float(max_gap)


def _bruteforce_linear_decoder_error(
    observation_matrix: Array,
    protected_matrix: Array,
    decoder: Array,
    *,
    family_basis: Array | None = None,
    noise_radius: float = 0.0,
    coefficient_values: Sequence[float] = (-1.0, 0.0, 1.0),
    noise_multipliers: Sequence[float] = (-1.0, 0.0, 1.0),
) -> float:
    OF, LF = _restricted_family_matrices(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
    )
    points = _coefficient_grid_points(OF.shape[1], coefficient_values)
    noise_values = tuple(float(noise_radius) * float(multiplier) for multiplier in noise_multipliers)
    noise_vectors = _coefficient_grid_points(OF.shape[0], noise_values)
    max_error = 0.0
    decoder_matrix = np.asarray(decoder, dtype=float)
    for coeff in points:
        clean_record = OF @ coeff
        true_target = LF @ coeff
        for noise in noise_vectors:
            estimate = decoder_matrix @ (clean_record + noise)
            max_error = max(max_error, float(np.linalg.norm(estimate - true_target)))
    return float(max_error)


def _restricted_linear_decoder_error_stats(
    observation_matrix: Array,
    protected_matrix: Array,
    decoder: Array,
    *,
    family_basis: Array | None = None,
    coefficient_values: Sequence[float] = (-1.0, 0.0, 1.0),
) -> tuple[float, float]:
    OF, LF = _restricted_family_matrices(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
    )
    points = _coefficient_grid_points(OF.shape[1], coefficient_values)
    decoder_matrix = np.asarray(decoder, dtype=float)
    errors = [
        float(np.linalg.norm(decoder_matrix @ (OF @ coeff) - LF @ coeff))
        for coeff in points
    ]
    return float(max(errors, default=0.0)), float(np.mean(errors) if errors else 0.0)


def _subspace_residual(
    source_basis: Array,
    target_basis: Array,
    *,
    tol: float = EPS,
) -> float:
    source = _orthonormal_family_basis(source_basis, tol=tol)
    target = _orthonormal_family_basis(target_basis, tol=tol)
    if source.shape[1] == 0:
        return 0.0
    if target.shape[1] == 0:
        return float(np.linalg.norm(source, ord=2))
    projector = target @ target.T
    return float(np.linalg.norm(source - projector @ source, ord=2))


def _subspace_distance(
    left_basis: Array,
    right_basis: Array,
    *,
    tol: float = EPS,
) -> float:
    return max(
        _subspace_residual(left_basis, right_basis, tol=tol),
        _subspace_residual(right_basis, left_basis, tol=tol),
    )


def _canonical_mismatch_family(beta: float) -> Array:
    return np.asarray(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [0.0, float(beta)],
        ],
        dtype=float,
    )



def finite_target_hierarchy_report(
    observations: Sequence[Array],
    weak_protected_values: Sequence[Array],
    strong_protected_values: Sequence[Array],
    deltas: Iterable[float],
    *,
    tol: float = EPS,
) -> FiniteTargetHierarchyReport:
    strong = finite_recoverability_report(observations, strong_protected_values, deltas, tol=tol)
    weak = finite_recoverability_report(observations, weak_protected_values, deltas, tol=tol)
    return FiniteTargetHierarchyReport(
        strong_exact_recoverable=bool(strong.exact_recoverable),
        weak_exact_recoverable=bool(weak.exact_recoverable),
        detectable_only=bool((not strong.exact_recoverable) and weak.exact_recoverable),
        strong_collision_gap=float(strong.collision_max_protected_distance),
        weak_collision_gap=float(weak.collision_max_protected_distance),
        strong_witness_pair=strong.witness_pair,
        weak_witness_pair=weak.witness_pair,
    )



def restricted_linear_target_hierarchy_report(
    observation_matrix: Array,
    weak_protected_matrix: Array,
    strong_protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> RestrictedLinearTargetHierarchyReport:
    weak = restricted_linear_recoverability(
        observation_matrix,
        weak_protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    strong = restricted_linear_recoverability(
        observation_matrix,
        strong_protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    return RestrictedLinearTargetHierarchyReport(
        strong_exact_recoverable=bool(strong.exact_recoverable),
        weak_exact_recoverable=bool(weak.exact_recoverable),
        detectable_only=bool((not strong.exact_recoverable) and weak.exact_recoverable),
        strong_rowspace_residual=float(
            restricted_linear_rowspace_residual(
                observation_matrix,
                strong_protected_matrix,
                family_basis=family_basis,
                tol=tol,
            )
        ),
        weak_rowspace_residual=float(
            restricted_linear_rowspace_residual(
                observation_matrix,
                weak_protected_matrix,
                family_basis=family_basis,
                tol=tol,
            )
        ),
        strong_collision_gap=float(
            restricted_linear_collision_gap(
                observation_matrix,
                strong_protected_matrix,
                family_basis=family_basis,
                box_radius=box_radius,
                tol=tol,
            )
        ),
        weak_collision_gap=float(
            restricted_linear_collision_gap(
                observation_matrix,
                weak_protected_matrix,
                family_basis=family_basis,
                box_radius=box_radius,
                tol=tol,
            )
        ),
    )



def rank_only_classifier_failure_report(
    ambient_dimensions: Iterable[int],
    *,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> RankOnlyClassifierFailureReport:
    rows: list[RankOnlyClassifierFailureRow] = []
    all_same_rank = True
    all_opposite = True
    for ambient_dimension in ambient_dimensions:
        n = int(ambient_dimension)
        for protected_rank in range(1, n):
            for observation_rank in range(protected_rank, n):
                witness = same_rank_alignment_counterexample(
                    ambient_dimension=n,
                    protected_rank=protected_rank,
                    observation_rank=observation_rank,
                    box_radius=box_radius,
                    tol=tol,
                )
                exact_rank = restricted_linear_rank_lower_bound(
                    witness.exact_observation_matrix,
                    witness.protected_matrix,
                    tol=tol,
                )
                fail_rank = restricted_linear_rank_lower_bound(
                    witness.fail_observation_matrix,
                    witness.protected_matrix,
                    tol=tol,
                )
                exact_report = restricted_linear_recoverability(
                    witness.exact_observation_matrix,
                    witness.protected_matrix,
                    tol=tol,
                )
                fail_report = restricted_linear_recoverability(
                    witness.fail_observation_matrix,
                    witness.protected_matrix,
                    tol=tol,
                )
                same_rank = exact_rank.rank_observation == fail_rank.rank_observation == observation_rank
                opposite = bool(exact_report.exact_recoverable and (not fail_report.exact_recoverable))
                all_same_rank = all_same_rank and same_rank
                all_opposite = all_opposite and opposite
                rows.append(
                    RankOnlyClassifierFailureRow(
                        ambient_dimension=n,
                        protected_rank=protected_rank,
                        observation_rank=observation_rank,
                        exact_rank_observation=int(exact_rank.rank_observation),
                        fail_rank_observation=int(fail_rank.rank_observation),
                        exact_recoverable=bool(exact_report.exact_recoverable),
                        fail_recoverable=bool(fail_report.exact_recoverable),
                        exact_rowspace_residual=float(witness.exact_rowspace_residual),
                        fail_rowspace_residual=float(witness.fail_rowspace_residual),
                        exact_collision_gap=float(witness.exact_collision_gap),
                        fail_collision_gap=float(witness.fail_collision_gap),
                    )
                )
    return RankOnlyClassifierFailureReport(
        witness_count=len(rows),
        all_same_rank=bool(all_same_rank),
        all_opposite_verdicts=bool(all_opposite),
        rows=tuple(rows),
    )


def coordinate_rank_enumeration_report(
    ambient_dimensions: Iterable[int],
    *,
    tol: float = EPS,
) -> CoordinateRankEnumerationReport:
    rows: list[CoordinateRankEnumerationRow] = []
    all_levels = True
    for ambient_dimension in ambient_dimensions:
        n = int(ambient_dimension)
        for protected_rank in range(1, n):
            protected = np.eye(n, dtype=float)[:protected_rank, :]
            for observation_rank in range(protected_rank, n):
                exact_count = 0
                fail_count = 0
                for combo in combinations(range(n), observation_rank):
                    observation = np.eye(n, dtype=float)[list(combo), :]
                    report = restricted_linear_recoverability(observation, protected, tol=tol)
                    if report.exact_recoverable:
                        exact_count += 1
                    else:
                        fail_count += 1
                rows.append(
                    CoordinateRankEnumerationRow(
                        ambient_dimension=n,
                        protected_rank=protected_rank,
                        observation_rank=observation_rank,
                        exact_count=exact_count,
                        fail_count=fail_count,
                    )
                )
                all_levels = all_levels and exact_count > 0 and fail_count > 0
    return CoordinateRankEnumerationReport(
        rows=tuple(rows),
        all_levels_have_exact_and_fail=bool(all_levels),
    )


def candidate_library_budget_report(
    ambient_dimensions: Iterable[int],
    *,
    tol: float = EPS,
) -> CandidateLibraryBudgetReport:
    rows: list[CandidateLibraryBudgetRow] = []
    all_levels = True
    for ambient_dimension in ambient_dimensions:
        n = int(ambient_dimension)
        library = np.eye(n, dtype=float)
        for protected_rank in range(1, n):
            protected = library[:protected_rank, :]
            for selection_size in range(protected_rank, n):
                exact_count = 0
                fail_count = 0
                exact_subset: tuple[int, ...] | None = None
                fail_subset: tuple[int, ...] | None = None
                for combo in combinations(range(n), selection_size):
                    observation = library[list(combo), :]
                    report = restricted_linear_recoverability(observation, protected, tol=tol)
                    if report.exact_recoverable:
                        exact_count += 1
                        if exact_subset is None:
                            exact_subset = tuple(int(index) for index in combo)
                    else:
                        fail_count += 1
                        if fail_subset is None:
                            fail_subset = tuple(int(index) for index in combo)
                if exact_subset is None or fail_subset is None:
                    raise RuntimeError('expected both exact and fail subsets in the fixed candidate library')
                all_levels = all_levels and exact_count > 0 and fail_count > 0
                rows.append(
                    CandidateLibraryBudgetRow(
                        ambient_dimension=n,
                        protected_rank=protected_rank,
                        selection_size=selection_size,
                        exact_count=exact_count,
                        fail_count=fail_count,
                        exact_subset=exact_subset,
                        fail_subset=fail_subset,
                        exact_total_cost=float(selection_size),
                        fail_total_cost=float(selection_size),
                    )
                )
    return CandidateLibraryBudgetReport(
        witness_count=len(rows),
        all_levels_have_exact_and_fail=bool(all_levels),
        rows=tuple(rows),
    )


def noisy_restricted_linear_target_hierarchy_report(
    observation_matrix: Array,
    weak_protected_matrix: Array,
    strong_protected_matrix: Array,
    noise_radii: Iterable[float],
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    coefficient_values: Sequence[float] = (-1.0, 0.0, 1.0),
    noise_multipliers: Sequence[float] = (-1.0, 0.0, 1.0),
    tol: float = EPS,
) -> NoisyRestrictedLinearTargetHierarchyReport:
    weak_report = restricted_linear_recoverability(
        observation_matrix,
        weak_protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    strong_report = restricted_linear_recoverability(
        observation_matrix,
        strong_protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    if not weak_report.exact_recoverable or weak_report.recovery_operator is None:
        raise ValueError('weak target must be exactly recoverable to form the noisy hierarchy report')

    weak_norm = float(np.linalg.norm(weak_report.recovery_operator, ord=2))
    strong_gap = float(
        restricted_linear_collision_gap(
            observation_matrix,
            strong_protected_matrix,
            family_basis=family_basis,
            box_radius=box_radius,
            tol=tol,
        )
    )
    weak_discrete_gap = float(
        _discrete_restricted_linear_collision_gap(
            observation_matrix,
            weak_protected_matrix,
            family_basis=family_basis,
            coefficient_values=coefficient_values,
            tol=tol,
        )
    )
    strong_discrete_gap = float(
        _discrete_restricted_linear_collision_gap(
            observation_matrix,
            strong_protected_matrix,
            family_basis=family_basis,
            coefficient_values=coefficient_values,
            tol=tol,
        )
    )
    lower_bound = float(0.5 * strong_gap)
    separation_threshold = None if weak_norm <= tol else float(lower_bound / weak_norm)

    rows: list[NoisyHierarchyRow] = []
    for radius in noise_radii:
        noise_radius = float(radius)
        weak_upper_bound = float(weak_norm * noise_radius)
        weak_bruteforce_max_error = float(
            _bruteforce_linear_decoder_error(
                observation_matrix,
                weak_protected_matrix,
                weak_report.recovery_operator,
                family_basis=family_basis,
                noise_radius=noise_radius,
                coefficient_values=coefficient_values,
                noise_multipliers=noise_multipliers,
            )
        )
        rows.append(
            NoisyHierarchyRow(
                noise_radius=noise_radius,
                weak_upper_bound=weak_upper_bound,
                weak_bruteforce_max_error=weak_bruteforce_max_error,
                strong_uniform_lower_bound=lower_bound,
                strong_discrete_collision_gap=strong_discrete_gap,
                separated=bool(weak_upper_bound + tol < lower_bound),
            )
        )

    return NoisyRestrictedLinearTargetHierarchyReport(
        weak_exact_recoverable=bool(weak_report.exact_recoverable),
        strong_exact_recoverable=bool(strong_report.exact_recoverable),
        detectable_only=bool((not strong_report.exact_recoverable) and weak_report.exact_recoverable),
        weak_decoder_operator_norm=weak_norm,
        strong_collision_gap=strong_gap,
        strong_uniform_lower_bound=lower_bound,
        separation_noise_threshold=separation_threshold,
        weak_discrete_collision_gap=weak_discrete_gap,
        strong_discrete_collision_gap=strong_discrete_gap,
        rows=tuple(rows),
    )


def control_regime_hierarchy_report(
    epsilon: float,
    *,
    horizons: Sequence[int] = (1, 2),
    tol: float = EPS,
) -> ControlRegimeHierarchyReport:
    sweep = functional_observability_sweep(epsilon_values=(float(epsilon),), horizons=horizons)
    rows = {(float(row['epsilon']), int(row['horizon'])): row for row in sweep['rows']}
    one_step = rows[(float(epsilon), int(horizons[0]))]
    two_step = rows[(float(epsilon), int(horizons[1]))]
    observer = sweep['observer_reports'][0]
    return ControlRegimeHierarchyReport(
        epsilon=float(epsilon),
        one_step_exact_recoverable=bool(one_step['exact_recoverable']),
        two_step_exact_recoverable=bool(two_step['exact_recoverable']),
        observer_asymptotic_recoverable=bool(observer['spectral_radius'] < 1.0 - tol),
        one_step_collision_gap=float(one_step['collision_max_protected_distance']),
        two_step_collision_gap=float(two_step['collision_max_protected_distance']),
        observer_spectral_radius=float(observer['spectral_radius']),
        observer_final_protected_error=float(observer['protected_error_history'][-1]),
    )


def canonical_detectable_only_examples() -> dict[str, object]:
    finite_report = finite_target_hierarchy_report(
        observations=[
            np.array([0.0]),
            np.array([1.0]),
            np.array([1.0]),
        ],
        weak_protected_values=[
            np.array([0.0]),
            np.array([1.0]),
            np.array([1.0]),
        ],
        strong_protected_values=[
            np.array([0.0]),
            np.array([1.0]),
            np.array([2.0]),
        ],
        deltas=(0.0, 0.5, 1.0),
        tol=EPS,
    )
    restricted_linear_report = restricted_linear_target_hierarchy_report(
        np.array(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 1.0],
            ],
            dtype=float,
        ),
        np.array([[0.0, 1.0, 1.0]], dtype=float),
        np.array([[0.0, 0.0, 1.0]], dtype=float),
        box_radius=1.0,
        tol=EPS,
    )
    noisy_report = noisy_restricted_linear_target_hierarchy_report(
        np.array(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 1.0],
            ],
            dtype=float,
        ),
        np.array([[0.0, 1.0, 1.0]], dtype=float),
        np.array([[0.0, 0.0, 1.0]], dtype=float),
        noise_radii=(0.0, 0.25, 0.5, 1.0),
        box_radius=1.0,
        tol=EPS,
    )
    control_report = control_regime_hierarchy_report(0.2)
    return {
        'finite': finite_report,
        'restricted_linear': restricted_linear_report,
        'noisy_restricted_linear': noisy_report,
        'control': control_report,
    }


def restricted_linear_fiber_geometry_report(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> RestrictedLinearFiberGeometryReport:
    OF, _ = _restricted_family_matrices(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    coefficient_dimension = int(OF.shape[1])
    observation_rank = int(np.linalg.matrix_rank(OF, tol))
    fiber_dimension = int(max(0, coefficient_dimension - observation_rank))
    residual = float(
        restricted_linear_rowspace_residual(
            observation_matrix,
            protected_matrix,
            family_basis=family_basis,
            tol=tol,
        )
    )
    gap = float(
        restricted_linear_collision_gap(
            observation_matrix,
            protected_matrix,
            family_basis=family_basis,
            box_radius=box_radius,
            tol=tol,
        )
    )
    exact = residual <= tol
    return RestrictedLinearFiberGeometryReport(
        coefficient_dimension=coefficient_dimension,
        observation_rank=observation_rank,
        fiber_dimension=fiber_dimension,
        exact_recoverable=bool(exact),
        target_mixed_fiber=bool(not exact),
        rowspace_residual=residual,
        collision_gap=gap,
    )


def restricted_linear_family_enlargement_report(
    observation_matrix: Array,
    protected_matrix: Array,
    small_family_basis: Array,
    large_family_basis: Array,
    *,
    box_radius: float = 1.0,
    coefficient_values: Sequence[float] = (-1.0, 0.0, 1.0),
    tol: float = EPS,
) -> RestrictedLinearFamilyEnlargementReport:
    small_basis = _orthonormal_family_basis(small_family_basis, tol=tol)
    large_basis = _orthonormal_family_basis(large_family_basis, tol=tol)
    inclusion_residual = _subspace_residual(small_basis, large_basis, tol=tol)
    if inclusion_residual > 1e-7:
        raise ValueError('small_family_basis must lie inside the span of large_family_basis')

    small = restricted_linear_recoverability(
        observation_matrix,
        protected_matrix,
        family_basis=small_basis,
        tol=tol,
    )
    large = restricted_linear_recoverability(
        observation_matrix,
        protected_matrix,
        family_basis=large_basis,
        tol=tol,
    )
    small_residual = float(
        restricted_linear_rowspace_residual(
            observation_matrix,
            protected_matrix,
            family_basis=small_basis,
            tol=tol,
        )
    )
    large_residual = float(
        restricted_linear_rowspace_residual(
            observation_matrix,
            protected_matrix,
            family_basis=large_basis,
            tol=tol,
        )
    )
    small_gap = float(
        restricted_linear_collision_gap(
            observation_matrix,
            protected_matrix,
            family_basis=small_basis,
            box_radius=box_radius,
            tol=tol,
        )
    )
    large_gap = float(
        restricted_linear_collision_gap(
            observation_matrix,
            protected_matrix,
            family_basis=large_basis,
            box_radius=box_radius,
            tol=tol,
        )
    )
    max_error = None
    mean_error = None
    if small.exact_recoverable and small.recovery_operator is not None:
        max_error, mean_error = _restricted_linear_decoder_error_stats(
            observation_matrix,
            protected_matrix,
            small.recovery_operator,
            family_basis=large_basis,
            coefficient_values=coefficient_values,
        )

    return RestrictedLinearFamilyEnlargementReport(
        small_family_dimension=int(small_basis.shape[1]),
        large_family_dimension=int(large_basis.shape[1]),
        inclusion_residual=float(inclusion_residual),
        small_exact_recoverable=bool(small.exact_recoverable),
        large_exact_recoverable=bool(large.exact_recoverable),
        small_rowspace_residual=small_residual,
        large_rowspace_residual=large_residual,
        small_collision_gap=small_gap,
        large_collision_gap=large_gap,
        false_positive_risk=bool(small.exact_recoverable and (not large.exact_recoverable)),
        larger_family_impossibility_lower_bound=float(0.5 * large_gap),
        reference_decoder_max_error_on_large_family=max_error,
        reference_decoder_mean_error_on_large_family=mean_error,
    )


def restricted_linear_model_mismatch_report(
    observation_matrix: Array,
    protected_matrix: Array,
    reference_family_basis: Array,
    mismatch_families: dict[str, Array],
    *,
    box_radius: float = 1.0,
    coefficient_values: Sequence[float] = (-1.0, 0.0, 1.0),
    tol: float = EPS,
) -> RestrictedLinearModelMismatchReport:
    reference_basis = _orthonormal_family_basis(reference_family_basis, tol=tol)
    reference = restricted_linear_recoverability(
        observation_matrix,
        protected_matrix,
        family_basis=reference_basis,
        tol=tol,
    )
    decoder_norm = None
    if reference.exact_recoverable and reference.recovery_operator is not None:
        decoder_norm = float(np.linalg.norm(reference.recovery_operator, ord=2))

    rows: list[RestrictedLinearModelMismatchRow] = []
    for label, family_basis in mismatch_families.items():
        basis = _orthonormal_family_basis(family_basis, tol=tol)
        report = restricted_linear_recoverability(
            observation_matrix,
            protected_matrix,
            family_basis=basis,
            tol=tol,
        )
        residual = float(
            restricted_linear_rowspace_residual(
                observation_matrix,
                protected_matrix,
                family_basis=basis,
                tol=tol,
            )
        )
        gap = float(
            restricted_linear_collision_gap(
                observation_matrix,
                protected_matrix,
                family_basis=basis,
                box_radius=box_radius,
                tol=tol,
            )
        )
        max_error = None
        mean_error = None
        if reference.exact_recoverable and reference.recovery_operator is not None:
            max_error, mean_error = _restricted_linear_decoder_error_stats(
                observation_matrix,
                protected_matrix,
                reference.recovery_operator,
                family_basis=basis,
                coefficient_values=coefficient_values,
            )
        rows.append(
            RestrictedLinearModelMismatchRow(
                label=str(label),
                family_dimension=int(basis.shape[1]),
                subspace_distance=float(_subspace_distance(reference_basis, basis, tol=tol)),
                exact_recoverable_under_true_family=bool(report.exact_recoverable),
                rowspace_residual=residual,
                collision_gap=gap,
                reference_decoder_max_error=max_error,
                reference_decoder_mean_error=mean_error,
            )
        )

    return RestrictedLinearModelMismatchReport(
        reference_exact_recoverable=bool(reference.exact_recoverable),
        reference_family_dimension=int(reference_basis.shape[1]),
        reference_decoder_operator_norm=decoder_norm,
        rows=tuple(rows),
    )


def canonical_model_mismatch_report(
    beta_reference: float,
    beta_values: Iterable[float],
    *,
    coefficient_values: Sequence[float] = (-1.0, 0.0, 1.0),
    tol: float = EPS,
) -> CanonicalModelMismatchReport:
    observation = np.asarray(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=float,
    )
    protected = np.asarray([[0.0, 0.0, 1.0]], dtype=float)
    reference_basis = _canonical_mismatch_family(float(beta_reference))
    reference = restricted_linear_recoverability(
        observation,
        protected,
        family_basis=reference_basis,
        tol=tol,
    )
    decoder_norm = None
    if reference.exact_recoverable and reference.recovery_operator is not None:
        decoder_norm = float(np.linalg.norm(reference.recovery_operator, ord=2))

    rows: list[CanonicalModelMismatchRow] = []
    for beta in beta_values:
        beta_true = float(beta)
        true_basis = _canonical_mismatch_family(beta_true)
        true_report = restricted_linear_recoverability(
            observation,
            protected,
            family_basis=true_basis,
            tol=tol,
        )
        brute_force_max = 0.0
        brute_force_mean = 0.0
        if reference.exact_recoverable and reference.recovery_operator is not None:
            brute_force_max, brute_force_mean = _restricted_linear_decoder_error_stats(
                observation,
                protected,
                reference.recovery_operator,
                family_basis=true_basis,
                coefficient_values=coefficient_values,
            )
        formula_max_error = float(abs(beta_true - float(beta_reference)) / np.sqrt(1.0 + beta_true * beta_true))
        rows.append(
            CanonicalModelMismatchRow(
                beta_true=beta_true,
                beta_reference=float(beta_reference),
                exact_recoverable_true_family=bool(true_report.exact_recoverable),
                subspace_distance=float(_subspace_distance(reference_basis, true_basis, tol=tol)),
                formula_max_error=formula_max_error,
                brute_force_max_error=float(brute_force_max),
                brute_force_mean_error=float(brute_force_mean),
            )
        )

    return CanonicalModelMismatchReport(
        beta_reference=float(beta_reference),
        reference_exact_recoverable=bool(reference.exact_recoverable),
        reference_decoder_operator_norm=decoder_norm,
        rows=tuple(rows),
    )


def periodic_modal_refinement_report(
    *,
    cutoff: int = 2,
    coarse_modes: Sequence[tuple[int, int, float]] = ((1, 1, 1.0), (2, 1, 0.8)),
    refined_modes: Sequence[tuple[int, int, float]] = ((1, 1, 1.0), (2, 1, 0.8), (3, 1, 0.6), (4, 1, 0.45)),
    coarse_functional: Sequence[float] = (1.0, -0.5),
    refined_functional: Sequence[float] = (1.0, -0.5, 0.75, 0.25),
    coefficient_values: Sequence[float] = (-1.0, -0.5, 0.0, 0.5, 1.0),
    tol: float = EPS,
) -> PeriodicModalRefinementReport:
    coarse_basis_states = _periodic_modal_basis_states(n=24, modes=coarse_modes)
    refined_basis_states = _periodic_modal_basis_states(n=24, modes=refined_modes)
    coarse_observation = np.column_stack(
        [_truncate_vorticity(state['omega'], int(cutoff)).ravel() for state in coarse_basis_states]
    )
    refined_observation = np.column_stack(
        [_truncate_vorticity(state['omega'], int(cutoff)).ravel() for state in refined_basis_states]
    )
    coarse_target = np.asarray([coarse_functional], dtype=float)
    refined_target = np.asarray([refined_functional], dtype=float)
    coarse = restricted_linear_recoverability(coarse_observation, coarse_target, tol=tol)
    refined = restricted_linear_recoverability(refined_observation, refined_target, tol=tol)
    coarse_gap = float(
        restricted_linear_collision_gap(
            coarse_observation,
            coarse_target,
            box_radius=1.0,
            tol=tol,
        )
    )
    refined_gap = float(
        restricted_linear_collision_gap(
            refined_observation,
            refined_target,
            box_radius=1.0,
            tol=tol,
        )
    )
    max_error = None
    mean_error = None
    if coarse.exact_recoverable and coarse.recovery_operator is not None:
        max_error, mean_error = _restricted_linear_decoder_error_stats(
            refined_observation,
            refined_target,
            coarse.recovery_operator,
            coefficient_values=coefficient_values,
        )

    return PeriodicModalRefinementReport(
        cutoff=int(cutoff),
        coarse_mode_count=len(coarse_modes),
        refined_mode_count=len(refined_modes),
        coarse_exact_recoverable=bool(coarse.exact_recoverable),
        refined_exact_recoverable=bool(refined.exact_recoverable),
        coarse_collision_gap=coarse_gap,
        refined_collision_gap=refined_gap,
        refinement_false_positive_risk=bool(coarse.exact_recoverable and (not refined.exact_recoverable)),
        refined_family_impossibility_lower_bound=float(0.5 * refined_gap),
        coarse_decoder_max_error_on_refined_family=max_error,
        coarse_decoder_mean_error_on_refined_family=mean_error,
    )


__all__ = [
    "FiniteTargetHierarchyReport",
    "RestrictedLinearTargetHierarchyReport",
    "RankOnlyClassifierFailureRow",
    "RankOnlyClassifierFailureReport",
    "CoordinateRankEnumerationRow",
    "CoordinateRankEnumerationReport",
    "CandidateLibraryBudgetRow",
    "CandidateLibraryBudgetReport",
    "NoisyHierarchyRow",
    "NoisyRestrictedLinearTargetHierarchyReport",
    "ControlRegimeHierarchyReport",
    "RestrictedLinearFiberGeometryReport",
    "RestrictedLinearFamilyEnlargementReport",
    "RestrictedLinearModelMismatchRow",
    "RestrictedLinearModelMismatchReport",
    "CanonicalModelMismatchRow",
    "CanonicalModelMismatchReport",
    "PeriodicModalRefinementReport",
    "finite_target_hierarchy_report",
    "restricted_linear_target_hierarchy_report",
    "rank_only_classifier_failure_report",
    "coordinate_rank_enumeration_report",
    "candidate_library_budget_report",
    "noisy_restricted_linear_target_hierarchy_report",
    "control_regime_hierarchy_report",
    "canonical_detectable_only_examples",
    "restricted_linear_fiber_geometry_report",
    "restricted_linear_family_enlargement_report",
    "restricted_linear_model_mismatch_report",
    "canonical_model_mismatch_report",
    "periodic_modal_refinement_report",
]
