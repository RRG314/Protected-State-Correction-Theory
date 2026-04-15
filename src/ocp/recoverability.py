from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import math
from typing import Callable, Iterable, Sequence

import numpy as np

Array = np.ndarray
Metric = Callable[[Array, Array], float]

EPS = 1e-10


def euclidean_metric(a: Array, b: Array) -> float:
    return float(np.linalg.norm(np.asarray(a, dtype=float) - np.asarray(b, dtype=float)))


def scalar_metric(a: Array, b: Array) -> float:
    return float(abs(float(np.asarray(a, dtype=float).reshape(-1)[0]) - float(np.asarray(b, dtype=float).reshape(-1)[0])))


def rms_metric(a: Array, b: Array) -> float:
    diff = np.asarray(a, dtype=float).reshape(-1) - np.asarray(b, dtype=float).reshape(-1)
    if diff.size == 0:
        return 0.0
    return float(np.linalg.norm(diff) / math.sqrt(diff.size))


def _pairwise_distance_matrix(values: Sequence[Array], metric: Metric) -> Array:
    arr = np.asarray([np.asarray(value, dtype=float).reshape(-1) for value in values], dtype=float)
    if arr.ndim == 1:
        arr = arr[:, None]
    if metric in (euclidean_metric, scalar_metric, rms_metric):
        diff = arr[:, None, :] - arr[None, :, :]
        norms = np.linalg.norm(diff, axis=2)
        if metric is rms_metric:
            scale = math.sqrt(arr.shape[1]) if arr.shape[1] else 1.0
            return norms / scale
        return norms
    out = np.zeros((len(values), len(values)), dtype=float)
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            distance = metric(arr[i], arr[j])
            out[i, j] = distance
            out[j, i] = distance
    return out


@dataclass(frozen=True)
class FiniteRecoverabilityReport:
    exact_recoverable: bool
    collision_max_protected_distance: float
    collapse_deltas: tuple[float, ...]
    collapse_values: tuple[float, ...]
    witness_pair: tuple[int, int] | None


@dataclass(frozen=True)
class RestrictedLinearRecoverabilityReport:
    exact_recoverable: bool
    null_intersection_dimension: int
    recovery_operator: Array | None
    residual_norm: float


@dataclass(frozen=True)
class RestrictedLinearStabilityReport:
    exact_recoverable: bool
    recovery_operator: Array | None
    recovery_operator_norm_upper: float | None
    rowspace_residual: float
    collision_gap: float


@dataclass(frozen=True)
class SameRankRecoverabilityCounterexample:
    ambient_dimension: int
    protected_rank: int
    observation_rank: int
    protected_matrix: Array
    exact_observation_matrix: Array
    fail_observation_matrix: Array
    exact_rowspace_residual: float
    fail_rowspace_residual: float
    exact_collision_gap: float
    fail_collision_gap: float


@dataclass(frozen=True)
class AnalyticCollapseBenchmark:
    epsilon: float
    deltas: tuple[float, ...]
    collapse_values: tuple[float, ...]
    exact_recoverable: bool
    collision_max_protected_distance: float


@dataclass(frozen=True)
class NoiseLowerBoundRow:
    noise_radius: float
    lower_bound: float


@dataclass(frozen=True)
class QubitRecoverabilityRow:
    protected_variable: str
    phase_window_deg: float
    exact_recoverable: bool
    collision_max_protected_distance: float
    mean_recovery_error: float
    max_recovery_error: float


@dataclass(frozen=True)
class PeriodicCutoffRecoverabilityRow:
    cutoff: int
    exact_recoverable: bool
    rank_observation: int
    rank_protected: int
    collision_max_protected_distance: float
    mean_recovery_error: float
    max_recovery_error: float


@dataclass(frozen=True)
class PeriodicRecoverabilityRow:
    observation: str
    exact_recoverable: bool
    collision_max_protected_distance: float
    mean_recovery_error: float
    max_recovery_error: float


@dataclass(frozen=True)
class PeriodicProtectedComplexityRow:
    protected_variable: str
    cutoff: int
    predicted_min_cutoff: int
    exact_recoverable: bool
    rank_observation: int
    rank_protected: int
    collision_max_protected_distance: float
    mean_recovery_error: float
    max_recovery_error: float


@dataclass(frozen=True)
class FunctionalRecoverabilityRow:
    epsilon: float
    horizon: int
    exact_recoverable: bool
    collision_max_protected_distance: float
    recoverability_margin: float
    mean_recovery_error: float
    max_recovery_error: float


@dataclass(frozen=True)
class ObserverConvergenceReport:
    epsilon: float
    gain: Array
    spectral_radius: float
    protected_error_history: tuple[float, ...]


@dataclass(frozen=True)
class LinearRankLowerBoundReport:
    rank_observation: int
    rank_protected: int
    lower_bound_satisfied: bool


@dataclass(frozen=True)
class ControlComplexityRow:
    sensor_profile: str
    active_sensor_count: int
    protected_index: int
    horizon: int
    predicted_min_horizon: int | None
    exact_recoverable: bool
    rank_observation: int
    rank_protected: int
    collision_max_protected_distance: float
    mean_recovery_error: float
    max_recovery_error: float
    interpolation_residual: float | None


@dataclass(frozen=True)
class PeriodicFunctionalComplexityRow:
    functional_name: str
    cutoff: int
    predicted_min_cutoff: int
    exact_recoverable: bool
    rank_observation: int
    rank_protected: int
    collision_max_protected_distance: float
    mean_recovery_error: float
    max_recovery_error: float


@dataclass(frozen=True)
class DiagonalFunctionalComplexityRow:
    sensor_profile: str
    functional_name: str
    horizon: int
    predicted_min_horizon: int | None
    exact_recoverable: bool
    rank_observation: int
    rank_protected: int
    collision_max_protected_distance: float
    mean_recovery_error: float
    max_recovery_error: float
    interpolation_residual: float | None


@dataclass(frozen=True)
class NestedLinearThresholdRow:
    level: int | float | str
    exact_recoverable: bool
    rowspace_residual: float
    collision_gap: float
    zero_noise_lower_bound: float


@dataclass(frozen=True)
class PeriodicThresholdStressRow:
    case_name: str
    functional_name: str
    support_size: int
    cutoff: int
    predicted_min_cutoff: int
    observed_min_cutoff: int | None
    exact_recoverable: bool
    rowspace_residual: float
    collision_gap: float
    mean_recovery_error: float
    max_recovery_error: float


@dataclass(frozen=True)
class DiagonalPolynomialThresholdRow:
    case_name: str
    functional_name: str
    support_size: int
    polynomial_degree: int | None
    horizon: int
    predicted_min_horizon: int | None
    observed_min_horizon: int | None
    exact_recoverable: bool
    rowspace_residual: float
    collision_gap: float
    mean_recovery_error: float
    max_recovery_error: float



def finite_collapse_modulus(
    observations: Sequence[Array],
    protected_values: Sequence[Array],
    deltas: Iterable[float],
    *,
    observation_metric: Metric = euclidean_metric,
    protected_metric: Metric = euclidean_metric,
) -> Array:
    obs_matrix = _pairwise_distance_matrix(observations, observation_metric)
    prot_matrix = _pairwise_distance_matrix(protected_values, protected_metric)
    out = []
    for delta in deltas:
        mask = obs_matrix <= delta + EPS
        out.append(float(np.max(prot_matrix[mask])))
    return np.asarray(out, dtype=float)


def naive_finite_collapse_modulus(
    observations: Sequence[Array],
    protected_values: Sequence[Array],
    deltas: Iterable[float],
    *,
    observation_metric: Metric = euclidean_metric,
    protected_metric: Metric = euclidean_metric,
) -> Array:
    out = []
    for delta in deltas:
        max_gap = 0.0
        for i in range(len(observations)):
            for j in range(len(observations)):
                if observation_metric(observations[i], observations[j]) <= float(delta) + EPS:
                    max_gap = max(max_gap, protected_metric(protected_values[i], protected_values[j]))
        out.append(float(max_gap))
    return np.asarray(out, dtype=float)



def fiber_collision_gap(
    observations: Sequence[Array],
    protected_values: Sequence[Array],
    *,
    observation_metric: Metric = euclidean_metric,
    protected_metric: Metric = euclidean_metric,
    tol: float = EPS,
) -> tuple[float, tuple[int, int] | None]:
    obs_matrix = _pairwise_distance_matrix(observations, observation_metric)
    prot_matrix = _pairwise_distance_matrix(protected_values, protected_metric)
    upper = np.triu(np.ones_like(obs_matrix, dtype=bool), k=1)
    collision_mask = (obs_matrix <= tol) & upper
    if not np.any(collision_mask):
        return 0.0, None
    max_gap = float(np.max(prot_matrix[collision_mask]))
    if max_gap <= tol:
        return max_gap, None
    indices = np.argwhere(collision_mask & (prot_matrix >= max_gap - tol))
    i, j = indices[0]
    return max_gap, (int(i), int(j))



def finite_recoverability_report(
    observations: Sequence[Array],
    protected_values: Sequence[Array],
    deltas: Iterable[float],
    *,
    observation_metric: Metric = euclidean_metric,
    protected_metric: Metric = euclidean_metric,
    tol: float = EPS,
) -> FiniteRecoverabilityReport:
    deltas_tuple = tuple(float(value) for value in deltas)
    collapse = finite_collapse_modulus(
        observations,
        protected_values,
        deltas_tuple,
        observation_metric=observation_metric,
        protected_metric=protected_metric,
    )
    collision_gap, witness = fiber_collision_gap(
        observations,
        protected_values,
        observation_metric=observation_metric,
        protected_metric=protected_metric,
        tol=tol,
    )
    return FiniteRecoverabilityReport(
        exact_recoverable=collision_gap <= tol,
        collision_max_protected_distance=float(collision_gap),
        collapse_deltas=deltas_tuple,
        collapse_values=tuple(float(value) for value in collapse),
        witness_pair=witness,
    )


def adversarial_noise_lower_bound(
    observations: Sequence[Array],
    protected_values: Sequence[Array],
    noise_radius: float,
    *,
    observation_metric: Metric = euclidean_metric,
    protected_metric: Metric = euclidean_metric,
) -> float:
    collapse_value = finite_collapse_modulus(
        observations,
        protected_values,
        [float(noise_radius)],
        observation_metric=observation_metric,
        protected_metric=protected_metric,
    )[0]
    return float(0.5 * collapse_value)



def _orthonormalize_columns(matrix: Array, *, tol: float = EPS) -> Array:
    mat = np.asarray(matrix, dtype=float)
    if mat.ndim == 1:
        mat = mat[:, None]
    q, _ = np.linalg.qr(mat)
    keep = [i for i in range(q.shape[1]) if np.linalg.norm(q[:, i]) > tol]
    return q[:, keep] if keep else np.zeros((mat.shape[0], 0))



def _null_space(matrix: Array, *, tol: float = EPS) -> Array:
    u, s, vh = np.linalg.svd(np.asarray(matrix, dtype=float), full_matrices=True)
    rank = int(np.sum(s > tol))
    return vh[rank:].T.copy()


def _compressed_observation_matrix(matrix: Array, *, tol: float = EPS) -> Array:
    obs = np.asarray(matrix, dtype=float)
    if obs.size == 0:
        return obs.copy()
    u, s, vh = np.linalg.svd(obs, full_matrices=False)
    rank = int(np.sum(s > tol))
    if rank == 0:
        return np.zeros((0, obs.shape[1]), dtype=float)
    return np.diag(s[:rank]) @ vh[:rank, :]



def restricted_linear_recoverability(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> RestrictedLinearRecoverabilityReport:
    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    if family_basis is None:
        F = np.eye(O.shape[1])
    else:
        F = _orthonormalize_columns(np.asarray(family_basis, dtype=float), tol=tol)
    OF = O @ F
    LF = L @ F
    null = _null_space(OF, tol=tol)
    if null.size == 0:
        null_dim = 0
        exact = True
    else:
        null_dim = null.shape[1]
        exact = np.linalg.norm(LF @ null) <= tol
    recovery = None
    residual = math.inf
    if exact:
        recovery = LF @ np.linalg.pinv(OF, rcond=tol)
        residual = float(np.linalg.norm(recovery @ OF - LF))
    return RestrictedLinearRecoverabilityReport(
        exact_recoverable=bool(exact),
        null_intersection_dimension=null_dim,
        recovery_operator=recovery,
        residual_norm=float(residual),
    )


def restricted_linear_rank_lower_bound(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> LinearRankLowerBoundReport:
    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    if family_basis is None:
        F = np.eye(O.shape[1])
    else:
        F = _orthonormalize_columns(np.asarray(family_basis, dtype=float), tol=tol)
    rank_observation = int(np.linalg.matrix_rank(O @ F, tol=tol))
    rank_protected = int(np.linalg.matrix_rank(L @ F, tol=tol))
    return LinearRankLowerBoundReport(
        rank_observation=rank_observation,
        rank_protected=rank_protected,
        lower_bound_satisfied=bool(rank_observation >= rank_protected),
    )


def restricted_linear_rowspace_residual(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> float:
    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    if family_basis is None:
        F = np.eye(O.shape[1])
    else:
        F = _orthonormalize_columns(np.asarray(family_basis, dtype=float), tol=tol)
    OF = O @ F
    LF = L @ F
    if OF.size == 0 or np.linalg.norm(OF) <= tol:
        return float(np.linalg.norm(LF))
    projector = np.linalg.pinv(OF, rcond=tol) @ OF
    return float(np.linalg.norm(LF - LF @ projector))


def restricted_linear_collision_gap(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> float:
    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    if family_basis is None:
        F = np.eye(O.shape[1])
    else:
        F = _orthonormalize_columns(np.asarray(family_basis, dtype=float), tol=tol)
    return _box_collision_gap_from_nullspace(O @ F, L @ F, box_radius=box_radius, tol=tol)


def restricted_linear_stability_report(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> RestrictedLinearStabilityReport:
    linear = restricted_linear_recoverability(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    rowspace_residual = restricted_linear_rowspace_residual(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        tol=tol,
    )
    collision_gap = restricted_linear_collision_gap(
        observation_matrix,
        protected_matrix,
        family_basis=family_basis,
        box_radius=box_radius,
        tol=tol,
    )
    recovery_operator_norm_upper = None
    if linear.exact_recoverable and linear.recovery_operator is not None:
        recovery_operator_norm_upper = float(np.linalg.norm(linear.recovery_operator, ord=2))
    return RestrictedLinearStabilityReport(
        exact_recoverable=bool(linear.exact_recoverable),
        recovery_operator=None if linear.recovery_operator is None else np.asarray(linear.recovery_operator, dtype=float),
        recovery_operator_norm_upper=recovery_operator_norm_upper,
        rowspace_residual=float(rowspace_residual),
        collision_gap=float(collision_gap),
    )


def same_rank_alignment_counterexample(
    ambient_dimension: int,
    protected_rank: int,
    observation_rank: int,
    *,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> SameRankRecoverabilityCounterexample:
    n = int(ambient_dimension)
    r = int(protected_rank)
    k = int(observation_rank)
    if r <= 0:
        raise ValueError('protected_rank must be positive')
    if not (r <= k < n):
        raise ValueError('observation_rank must satisfy protected_rank <= observation_rank < ambient_dimension')

    protected_matrix = np.eye(n, dtype=float)[:r, :]
    exact_indices = list(range(k))
    fail_indices = list(range(1, r)) + list(range(r, k + 1))
    exact_observation_matrix = np.eye(n, dtype=float)[exact_indices, :]
    fail_observation_matrix = np.eye(n, dtype=float)[fail_indices, :]

    exact_residual = restricted_linear_rowspace_residual(exact_observation_matrix, protected_matrix, tol=tol)
    fail_residual = restricted_linear_rowspace_residual(fail_observation_matrix, protected_matrix, tol=tol)
    exact_gap = restricted_linear_collision_gap(
        exact_observation_matrix,
        protected_matrix,
        box_radius=box_radius,
        tol=tol,
    )
    fail_gap = restricted_linear_collision_gap(
        fail_observation_matrix,
        protected_matrix,
        box_radius=box_radius,
        tol=tol,
    )
    exact_report = restricted_linear_recoverability(exact_observation_matrix, protected_matrix, tol=tol)
    fail_report = restricted_linear_recoverability(fail_observation_matrix, protected_matrix, tol=tol)
    if not exact_report.exact_recoverable or fail_report.exact_recoverable:
        raise RuntimeError('constructed same-rank alignment counterexample did not realize the intended exact/impossible split')

    return SameRankRecoverabilityCounterexample(
        ambient_dimension=n,
        protected_rank=r,
        observation_rank=k,
        protected_matrix=protected_matrix,
        exact_observation_matrix=exact_observation_matrix,
        fail_observation_matrix=fail_observation_matrix,
        exact_rowspace_residual=float(exact_residual),
        fail_rowspace_residual=float(fail_residual),
        exact_collision_gap=float(exact_gap),
        fail_collision_gap=float(fail_gap),
    )


def minimal_linear_observation_complexity(
    observation_matrices: Sequence[Array],
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    tol: float = EPS,
) -> dict[str, object]:
    reports = [
        restricted_linear_recoverability(matrix, protected_matrix, family_basis=family_basis, tol=tol)
        for matrix in observation_matrices
    ]
    rowspace_residuals = [
        restricted_linear_rowspace_residual(matrix, protected_matrix, family_basis=family_basis, tol=tol)
        for matrix in observation_matrices
    ]
    collision_gaps = [
        restricted_linear_collision_gap(matrix, protected_matrix, family_basis=family_basis, tol=tol)
        for matrix in observation_matrices
    ]
    minimal_index = next((index for index, report in enumerate(reports) if report.exact_recoverable), None)
    return {
        'minimal_index': minimal_index,
        'exact_flags': [bool(report.exact_recoverable) for report in reports],
        'null_dimensions': [int(report.null_intersection_dimension) for report in reports],
        'residual_norms': [float(report.residual_norm) for report in reports],
        'rowspace_residuals': [float(value) for value in rowspace_residuals],
        'collision_gaps': [float(value) for value in collision_gaps],
        'zero_noise_lower_bounds': [float(0.5 * value) for value in collision_gaps],
    }


def nested_linear_threshold_profile(
    observation_matrices: Sequence[Array],
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    box_radius: float = 1.0,
    level_labels: Sequence[int | float | str] | None = None,
    tol: float = EPS,
) -> dict[str, object]:
    if level_labels is None:
        labels = list(range(len(observation_matrices)))
    else:
        labels = list(level_labels)
    if len(labels) != len(observation_matrices):
        raise ValueError('level_labels must match the observation matrix count')

    rows: list[NestedLinearThresholdRow] = []
    for label, matrix in zip(labels, observation_matrices, strict=True):
        linear = restricted_linear_recoverability(matrix, protected_matrix, family_basis=family_basis, tol=tol)
        residual = restricted_linear_rowspace_residual(matrix, protected_matrix, family_basis=family_basis, tol=tol)
        gap = restricted_linear_collision_gap(
            matrix,
            protected_matrix,
            family_basis=family_basis,
            box_radius=box_radius,
            tol=tol,
        )
        rows.append(
            NestedLinearThresholdRow(
                level=int(label) if isinstance(label, (int, np.integer)) else label,
                exact_recoverable=bool(linear.exact_recoverable),
                rowspace_residual=float(residual),
                collision_gap=float(gap),
                zero_noise_lower_bound=float(0.5 * gap),
            )
        )
    minimal_index = next((index for index, row in enumerate(rows) if row.exact_recoverable), None)
    minimal_label = None if minimal_index is None else labels[minimal_index]
    collision_gaps = [float(row.collision_gap) for row in rows]
    rowspace_residuals = [float(row.rowspace_residual) for row in rows]
    return {
        'level_labels': labels,
        'rows': [row.__dict__ for row in rows],
        'minimal_index': minimal_index,
        'minimal_label': minimal_label,
        'gap_monotone_nonincreasing': bool(
            all(collision_gaps[index + 1] <= collision_gaps[index] + tol for index in range(len(collision_gaps) - 1))
        ),
        'residual_monotone_nonincreasing': bool(
            all(rowspace_residuals[index + 1] <= rowspace_residuals[index] + tol for index in range(len(rowspace_residuals) - 1))
        ),
        'exact_gap_match': bool(
            all((row.exact_recoverable and row.collision_gap <= tol) or ((not row.exact_recoverable) and row.collision_gap > tol) for row in rows)
        ),
    }


def recoverability_margin_sampled(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    family_basis: Array | None = None,
    samples: int = 720,
    tol: float = EPS,
) -> float:
    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    if family_basis is None:
        F = np.eye(O.shape[1])
    else:
        F = _orthonormalize_columns(np.asarray(family_basis, dtype=float), tol=tol)
    dim = F.shape[1]
    if dim == 0:
        return 0.0
    if dim == 1:
        points = [np.array([1.0]), np.array([-1.0])]
    else:
        angles = np.linspace(0.0, 2.0 * np.pi, samples, endpoint=False)
        if dim != 2:
            raise ValueError('sampled recoverability margin currently supports one- or two-dimensional family coordinates')
        points = [np.array([math.cos(theta), math.sin(theta)]) for theta in angles]
    best = math.inf
    for coeff in points:
        z = F @ coeff
        protected = L @ z
        protected_norm = float(np.linalg.norm(protected))
        if protected_norm <= tol:
            continue
        obs_norm = float(np.linalg.norm(O @ z))
        best = min(best, obs_norm / protected_norm)
    return 0.0 if not math.isfinite(best) else float(best)



def analytic_collapse_modulus(epsilon: float, deltas: Iterable[float], *, protected_diameter: float = 2.0) -> AnalyticCollapseBenchmark:
    eps = abs(float(epsilon))
    delta_tuple = tuple(float(delta) for delta in deltas)
    if eps <= EPS:
        values = tuple(float(protected_diameter) for _ in delta_tuple)
        return AnalyticCollapseBenchmark(
            epsilon=float(epsilon),
            deltas=delta_tuple,
            collapse_values=values,
            exact_recoverable=False,
            collision_max_protected_distance=float(protected_diameter),
        )
    values = tuple(float(min(protected_diameter, delta / eps)) for delta in delta_tuple)
    return AnalyticCollapseBenchmark(
        epsilon=float(epsilon),
        deltas=delta_tuple,
        collapse_values=values,
        exact_recoverable=True,
        collision_max_protected_distance=0.0,
    )


def qubit_phase_collision_formula(phase_window_deg: float) -> float:
    window = abs(math.radians(float(phase_window_deg)))
    return float(2.0 * math.sin(min(window, 0.5 * math.pi)))


def bloch_vector(theta: float, phi: float) -> Array:
    return np.array(
        [
            math.sin(theta) * math.cos(phi),
            math.sin(theta) * math.sin(phi),
            math.cos(theta),
        ],
        dtype=float,
    )



def qubit_z_record(theta: float) -> Array:
    p0 = math.cos(theta / 2.0) ** 2
    return np.array([p0, 1.0 - p0], dtype=float)



def qubit_record_collapse_sweep(
    *,
    phase_windows_deg: Sequence[float] = (0.0, 15.0, 30.0, 60.0, 90.0, 135.0, 180.0),
    theta_samples: int = 21,
    phase_samples: int = 13,
    delta_count: int = 40,
) -> dict[str, object]:
    theta_grid = np.linspace(0.1, math.pi - 0.1, theta_samples)
    delta_grid = np.linspace(0.0, 1.0, delta_count)
    rows: list[QubitRecoverabilityRow] = []
    curves: dict[str, dict[str, list[float]]] = {}

    for protected_variable in ('bloch_vector', 'z_coordinate'):
        per_mode_curves: dict[str, list[float]] = {}
        for window in phase_windows_deg:
            phase_window = math.radians(window)
            if phase_window <= EPS:
                phi_grid = np.array([0.0])
            else:
                phi_grid = np.linspace(-phase_window, phase_window, phase_samples)
            observations: list[Array] = []
            protected_values: list[Array] = []
            recovery_errors: list[float] = []
            for theta, phi in product(theta_grid, phi_grid):
                observations.append(qubit_z_record(float(theta)))
                if protected_variable == 'bloch_vector':
                    protected = bloch_vector(float(theta), float(phi))
                    estimated = bloch_vector(float(theta), 0.0)
                else:
                    protected = np.array([math.cos(theta)], dtype=float)
                    estimated = np.array([math.cos(theta)], dtype=float)
                protected_values.append(protected)
                recovery_errors.append(float(np.linalg.norm(estimated - protected)))
            metric = euclidean_metric if protected_variable == 'bloch_vector' else scalar_metric
            report = finite_recoverability_report(
                observations,
                protected_values,
                delta_grid,
                observation_metric=euclidean_metric,
                protected_metric=metric,
            )
            rows.append(
                QubitRecoverabilityRow(
                    protected_variable=protected_variable,
                    phase_window_deg=float(window),
                    exact_recoverable=report.exact_recoverable,
                    collision_max_protected_distance=report.collision_max_protected_distance,
                    mean_recovery_error=float(np.mean(recovery_errors)),
                    max_recovery_error=float(np.max(recovery_errors)),
                )
            )
            per_mode_curves[str(window)] = list(report.collapse_values)
        curves[protected_variable] = per_mode_curves

    return {
        'phase_windows_deg': list(float(value) for value in phase_windows_deg),
        'delta_grid': list(float(value) for value in delta_grid),
        'rows': [row.__dict__ for row in rows],
        'curves': curves,
        'analytic_boundary': {
            'bloch_vector': [qubit_phase_collision_formula(window) for window in phase_windows_deg],
            'z_coordinate': [0.0 for _ in phase_windows_deg],
        },
    }



def _periodic_wavenumbers(n: int, h: float) -> tuple[Array, Array]:
    freqs = 2.0 * np.pi * np.fft.fftfreq(n, d=h)
    return freqs[:, None], freqs[None, :]



def _spectral_derivative_x(field: Array, h: float) -> Array:
    kx, _ = _periodic_wavenumbers(field.shape[0], h)
    return np.fft.ifftn(1j * kx * np.fft.fftn(field)).real



def _spectral_derivative_y(field: Array, h: float) -> Array:
    _, ky = _periodic_wavenumbers(field.shape[1], h)
    return np.fft.ifftn(1j * ky * np.fft.fftn(field)).real



def _stream_to_velocity(stream: Array, h: float) -> tuple[Array, Array]:
    return -_spectral_derivative_y(stream, h), _spectral_derivative_x(stream, h)



def _stream_to_vorticity(stream: Array, h: float) -> Array:
    kx, ky = _periodic_wavenumbers(stream.shape[0], h)
    k2 = kx**2 + ky**2
    stream_hat = np.fft.fftn(stream)
    return np.fft.ifftn(-k2 * stream_hat).real



def _velocity_from_vorticity(vorticity: Array, h: float, *, cutoff: int | None = None) -> tuple[Array, Array]:
    n = vorticity.shape[0]
    kx, ky = _periodic_wavenumbers(n, h)
    k2 = kx**2 + ky**2
    omega_hat = np.fft.fftn(vorticity)
    if cutoff is not None:
        fx = np.abs(np.fft.fftfreq(n) * n)[:, None]
        fy = np.abs(np.fft.fftfreq(n) * n)[None, :]
        mask = (fx <= cutoff) & (fy <= cutoff)
        omega_hat = np.where(mask, omega_hat, 0.0)
    psi_hat = np.zeros_like(omega_hat)
    mask = k2 > EPS
    psi_hat[mask] = -omega_hat[mask] / k2[mask]
    ux = np.fft.ifftn(-1j * ky * psi_hat).real
    uy = np.fft.ifftn(1j * kx * psi_hat).real
    return ux, uy



def _periodic_velocity_family(n: int = 24) -> list[dict[str, Array]]:
    h = 1.0 / n
    x = np.linspace(0.0, 1.0, n, endpoint=False)
    y = np.linspace(0.0, 1.0, n, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing='ij')
    family = []
    coeff_grid = (-1.0, -0.5, 0.5, 1.0)
    for a, b in product(coeff_grid, coeff_grid):
        stream = (
            a * np.sin(2.0 * np.pi * X) * np.sin(2.0 * np.pi * Y)
            + 0.8 * b * np.sin(4.0 * np.pi * X) * np.sin(2.0 * np.pi * Y)
        )
        ux, uy = _stream_to_velocity(stream, h)
        omega = _stream_to_vorticity(stream, h)
        family.append({
            'coefficients': np.array([a, b], dtype=float),
            'stream': stream,
            'ux': ux,
            'uy': uy,
            'omega': omega,
            'h': np.array([h], dtype=float),
        })
    return family


def _periodic_basis_states(n: int = 24) -> list[dict[str, Array]]:
    h = 1.0 / n
    x = np.linspace(0.0, 1.0, n, endpoint=False)
    y = np.linspace(0.0, 1.0, n, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing='ij')
    modes = [
        np.sin(2.0 * np.pi * X) * np.sin(2.0 * np.pi * Y),
        0.8 * np.sin(4.0 * np.pi * X) * np.sin(2.0 * np.pi * Y),
    ]
    basis_states = []
    for index, stream in enumerate(modes):
        ux, uy = _stream_to_velocity(stream, h)
        omega = _stream_to_vorticity(stream, h)
        basis_states.append({
            'index': np.array([index], dtype=float),
            'stream': stream,
            'ux': ux,
            'uy': uy,
            'omega': omega,
            'h': np.array([h], dtype=float),
        })
    return basis_states


def _truncate_vorticity(vorticity: Array, cutoff: int) -> Array:
    n = vorticity.shape[0]
    omega_hat = np.fft.fftn(vorticity)
    fx = np.abs(np.fft.fftfreq(n) * n)[:, None]
    fy = np.abs(np.fft.fftfreq(n) * n)[None, :]
    low = np.where((fx <= cutoff) & (fy <= cutoff), omega_hat, 0.0)
    return np.fft.ifftn(low).real


def periodic_cutoff_recoverability_sweep(
    *,
    n: int = 24,
    cutoffs: Sequence[int] = (0, 1, 2, 3),
    delta_count: int = 40,
) -> dict[str, object]:
    basis = _periodic_basis_states(n=n)
    family = _periodic_velocity_family(n=n)
    h = float(family[0]['h'][0])
    delta_grid = np.linspace(0.0, 6.0, delta_count)
    rows: list[PeriodicCutoffRecoverabilityRow] = []
    curves: dict[str, list[float]] = {}

    protected_matrix = np.column_stack(
        [
            np.concatenate([state['ux'].ravel(), state['uy'].ravel()])
            for state in basis
        ]
    )

    for cutoff in cutoffs:
        if cutoff <= 0:
            observation_matrix = np.zeros((basis[0]['omega'].size, len(basis)), dtype=float)
        else:
            observation_matrix = np.column_stack(
                [_truncate_vorticity(state['omega'], int(cutoff)).ravel() for state in basis]
            )
        linear = restricted_linear_recoverability(observation_matrix, protected_matrix)
        rank_report = restricted_linear_rank_lower_bound(observation_matrix, protected_matrix)

        observations: list[Array] = []
        protected_values: list[Array] = []
        recovery_errors: list[float] = []
        for state in family:
            protected = np.concatenate([state['ux'].ravel(), state['uy'].ravel()])
            observed = np.zeros_like(state['omega']) if cutoff <= 0 else _truncate_vorticity(state['omega'], int(cutoff))
            observations.append(observed.ravel())
            protected_values.append(protected)
            if linear.exact_recoverable:
                estimate = linear.recovery_operator @ observed.ravel()
            else:
                ux_rec, uy_rec = _velocity_from_vorticity(observed, h)
                estimate = np.concatenate([ux_rec.ravel(), uy_rec.ravel()])
            recovery_errors.append(rms_metric(estimate, protected))

        report = finite_recoverability_report(
            observations,
            protected_values,
            delta_grid,
            observation_metric=rms_metric,
            protected_metric=rms_metric,
        )
        rows.append(
            PeriodicCutoffRecoverabilityRow(
                cutoff=int(cutoff),
                exact_recoverable=bool(linear.exact_recoverable),
                rank_observation=rank_report.rank_observation,
                rank_protected=rank_report.rank_protected,
                collision_max_protected_distance=report.collision_max_protected_distance,
                mean_recovery_error=float(np.mean(recovery_errors)),
                max_recovery_error=float(np.max(recovery_errors)),
            )
        )
        curves[str(int(cutoff))] = list(report.collapse_values)

    return {
        'delta_grid': list(float(value) for value in delta_grid),
        'rows': [row.__dict__ for row in rows],
        'curves': curves,
    }



def _stream_mode(n: int, kx: int, ky: int, weight: float = 1.0) -> Array:
    x = np.linspace(0.0, 1.0, n, endpoint=False)
    y = np.linspace(0.0, 1.0, n, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing='ij')
    return float(weight) * np.sin(2.0 * np.pi * kx * X) * np.sin(2.0 * np.pi * ky * Y)


def _periodic_modal_basis_states(
    *,
    n: int = 24,
    modes: Sequence[tuple[int, int, float]] = ((1, 1, 1.0), (2, 1, 0.8), (3, 1, 0.6)),
) -> list[dict[str, Array]]:
    h = 1.0 / n
    basis_states = []
    for index, (kx, ky, weight) in enumerate(modes):
        stream = _stream_mode(n, kx, ky, weight)
        ux, uy = _stream_to_velocity(stream, h)
        omega = _stream_to_vorticity(stream, h)
        basis_states.append(
            {
                'index': np.array([index], dtype=float),
                'mode': np.array([kx, ky], dtype=float),
                'ux': ux,
                'uy': uy,
                'omega': omega,
                'h': np.array([h], dtype=float),
            }
        )
    return basis_states


def _periodic_modal_family(
    *,
    n: int = 24,
    modes: Sequence[tuple[int, int, float]] = ((1, 1, 1.0), (2, 1, 0.8), (3, 1, 0.6)),
    coeff_grid: Sequence[float] = (-1.0, -0.5, 0.0, 0.5, 1.0),
) -> list[dict[str, Array]]:
    basis = _periodic_modal_basis_states(n=n, modes=modes)
    family = []
    for coeffs in product(coeff_grid, repeat=len(basis)):
        ux = np.zeros_like(basis[0]['ux'])
        uy = np.zeros_like(basis[0]['uy'])
        omega = np.zeros_like(basis[0]['omega'])
        for coeff, state in zip(coeffs, basis, strict=True):
            ux = ux + float(coeff) * state['ux']
            uy = uy + float(coeff) * state['uy']
            omega = omega + float(coeff) * state['omega']
        family.append(
            {
                'coefficients': np.asarray(coeffs, dtype=float),
                'ux': ux,
                'uy': uy,
                'omega': omega,
                'h': basis[0]['h'],
            }
        )
    return family


def periodic_protected_complexity_sweep(
    *,
    n: int = 24,
    modes: Sequence[tuple[int, int, float]] = ((1, 1, 1.0), (2, 1, 0.8), (3, 1, 0.6)),
    cutoffs: Sequence[int] = (0, 1, 2, 3),
    delta_count: int = 40,
) -> dict[str, object]:
    basis = _periodic_modal_basis_states(n=n, modes=modes)
    family = _periodic_modal_family(n=n, modes=modes)
    delta_grid = np.linspace(0.0, 3.0, delta_count)
    mode_cutoffs = [max(abs(kx), abs(ky)) for kx, ky, _ in modes]
    selectors: dict[str, Array] = {
        'mode_1_coefficient': np.array([[1.0, 0.0, 0.0]], dtype=float),
        'modes_1_2_coefficients': np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=float),
        'full_modal_coefficients': np.eye(len(modes), dtype=float),
    }
    rows: list[PeriodicProtectedComplexityRow] = []
    curves: dict[str, list[float]] = {}

    basis_observations_by_cutoff = {
        int(cutoff): np.column_stack([_truncate_vorticity(state['omega'], int(cutoff)).ravel() for state in basis])
        if int(cutoff) > 0
        else np.zeros((basis[0]['omega'].size, len(basis)), dtype=float)
        for cutoff in cutoffs
    }
    sample_observations_by_cutoff = {
        int(cutoff): [
            (_truncate_vorticity(state['omega'], int(cutoff)).ravel() if int(cutoff) > 0 else np.zeros(state['omega'].size, dtype=float))
            for state in family
        ]
        for cutoff in cutoffs
    }

    for protected_name, selector in selectors.items():
        support = [index for index in range(selector.shape[1]) if np.linalg.norm(selector[:, index]) > EPS]
        predicted_min_cutoff = int(max(mode_cutoffs[index] for index in support))
        protected_values = [selector @ state['coefficients'] for state in family]
        for cutoff in cutoffs:
            observation_matrix = basis_observations_by_cutoff[int(cutoff)]
            linear = restricted_linear_recoverability(observation_matrix, selector)
            rank_report = restricted_linear_rank_lower_bound(observation_matrix, selector)
            observations = sample_observations_by_cutoff[int(cutoff)]
            if linear.exact_recoverable and linear.recovery_operator is not None:
                estimator = linear.recovery_operator
            else:
                estimator = selector @ np.linalg.pinv(observation_matrix, rcond=EPS)
            errors = [
                euclidean_metric(estimator @ observation, protected)
                for observation, protected in zip(observations, protected_values, strict=True)
            ]
            report = finite_recoverability_report(
                observations,
                protected_values,
                delta_grid,
                observation_metric=euclidean_metric,
                protected_metric=euclidean_metric,
            )
            rows.append(
                PeriodicProtectedComplexityRow(
                    protected_variable=protected_name,
                    cutoff=int(cutoff),
                    predicted_min_cutoff=predicted_min_cutoff,
                    exact_recoverable=bool(linear.exact_recoverable),
                    rank_observation=rank_report.rank_observation,
                    rank_protected=rank_report.rank_protected,
                    collision_max_protected_distance=report.collision_max_protected_distance,
                    mean_recovery_error=float(np.mean(errors)),
                    max_recovery_error=float(np.max(errors)),
                )
            )
            curves[f'{protected_name}:cutoff={int(cutoff)}'] = list(report.collapse_values)

    return {
        'delta_grid': list(float(value) for value in delta_grid),
        'mode_cutoffs': mode_cutoffs,
        'rows': [row.__dict__ for row in rows],
        'modes': [{'kx': int(kx), 'ky': int(ky), 'weight': float(weight)} for kx, ky, weight in modes],
        'curves': curves,
    }


def periodic_functional_complexity_sweep(
    *,
    n: int = 24,
    modes: Sequence[tuple[int, int, float]] = ((1, 1, 1.0), (2, 1, 0.8), (3, 1, 0.6), (4, 1, 0.45)),
    cutoffs: Sequence[int] = (0, 1, 2, 3, 4),
    delta_count: int = 40,
    functionals: dict[str, Sequence[float]] | None = None,
) -> dict[str, object]:
    if functionals is None:
        functionals = {
            'low_mode_sum': (1.0, 1.0, 0.0, 0.0),
            'bandlimited_contrast': (0.0, 1.0, -1.0, 0.0),
            'full_weighted_sum': (1.0, -0.5, 0.75, 0.25),
        }
    basis = _periodic_modal_basis_states(n=n, modes=modes)
    delta_grid = np.linspace(0.0, 4.0, delta_count)
    mode_cutoffs = [max(abs(kx), abs(ky)) for kx, ky, _ in modes]
    rows: list[PeriodicFunctionalComplexityRow] = []
    curves: dict[str, list[float]] = {}
    coeff_grid = np.linspace(-1.0, 1.0, 7)
    coefficient_family = [np.asarray(coeffs, dtype=float) for coeffs in product(coeff_grid, repeat=len(modes))]

    basis_observations_by_cutoff = {
        int(cutoff): np.column_stack([_truncate_vorticity(state['omega'], int(cutoff)).ravel() for state in basis])
        if int(cutoff) > 0
        else np.zeros((basis[0]['omega'].size, len(basis)), dtype=float)
        for cutoff in cutoffs
    }

    for functional_name, coefficients in functionals.items():
        selector = np.asarray([coefficients], dtype=float)
        if selector.shape[1] != len(modes):
            raise ValueError('periodic functional coefficients must match the number of modes')
        support = [index for index, value in enumerate(selector.reshape(-1)) if abs(float(value)) > EPS]
        predicted_min_cutoff = 0 if not support else int(max(mode_cutoffs[index] for index in support))
        for cutoff in cutoffs:
            observation_matrix = basis_observations_by_cutoff[int(cutoff)]
            compressed_observation_matrix = _compressed_observation_matrix(observation_matrix)
            linear = restricted_linear_recoverability(observation_matrix, selector)
            rank_report = restricted_linear_rank_lower_bound(observation_matrix, selector)
            estimator = linear.recovery_operator if linear.exact_recoverable and linear.recovery_operator is not None else selector @ np.linalg.pinv(observation_matrix, rcond=EPS)
            observations = [compressed_observation_matrix @ coeffs for coeffs in coefficient_family]
            protected_values = [selector @ coeffs for coeffs in coefficient_family]
            errors = [
                scalar_metric(estimator @ (observation_matrix @ coeffs), protected)
                for coeffs, protected in zip(coefficient_family, protected_values, strict=True)
            ]
            report = finite_recoverability_report(observations, protected_values, delta_grid, observation_metric=euclidean_metric, protected_metric=scalar_metric)
            collision_gap = _box_collision_gap_from_nullspace(observation_matrix, selector)
            rows.append(
                PeriodicFunctionalComplexityRow(
                    functional_name=str(functional_name),
                    cutoff=int(cutoff),
                    predicted_min_cutoff=predicted_min_cutoff,
                    exact_recoverable=bool(linear.exact_recoverable),
                    rank_observation=rank_report.rank_observation,
                    rank_protected=rank_report.rank_protected,
                    collision_max_protected_distance=float(collision_gap),
                    mean_recovery_error=float(np.mean(errors)),
                    max_recovery_error=float(np.max(errors)),
                )
            )
            curves[f'{functional_name}:cutoff={int(cutoff)}'] = list(report.collapse_values)

    return {
        'delta_grid': list(float(value) for value in delta_grid),
        'mode_cutoffs': mode_cutoffs,
        'rows': [row.__dict__ for row in rows],
        'modes': [{'kx': int(kx), 'ky': int(ky), 'weight': float(weight)} for kx, ky, weight in modes],
        'functionals': {name: [float(value) for value in values] for name, values in functionals.items()},
        'curves': curves,
    }


def periodic_velocity_recoverability_sweep(
    *,
    n: int = 24,
    delta_count: int = 40,
) -> dict[str, object]:
    family = _periodic_velocity_family(n=n)
    h = float(family[0]['h'][0])
    delta_grid = np.linspace(0.0, 6.0, delta_count)
    rows: list[PeriodicRecoverabilityRow] = []
    curves: dict[str, list[float]] = {}

    configs = {
        'full_vorticity': {'cutoff': None},
        'truncated_vorticity': {'cutoff': 1},
        'divergence_only': {'cutoff': 'divergence'},
    }

    for name, config in configs.items():
        observations: list[Array] = []
        protected_values: list[Array] = []
        recovery_errors: list[float] = []
        for state in family:
            protected = np.concatenate([state['ux'].ravel(), state['uy'].ravel()])
            protected_values.append(protected)
            if config['cutoff'] == 'divergence':
                observation = np.zeros(state['omega'].size, dtype=float)
                estimate = np.zeros_like(protected)
            else:
                observation = state['omega'].ravel()
                ux_rec, uy_rec = _velocity_from_vorticity(state['omega'], h, cutoff=config['cutoff'])
                estimate = np.concatenate([ux_rec.ravel(), uy_rec.ravel()])
                if config['cutoff'] == 1:
                    omega_hat = np.fft.fftn(state['omega'])
                    fx = np.abs(np.fft.fftfreq(n) * n)[:, None]
                    fy = np.abs(np.fft.fftfreq(n) * n)[None, :]
                    low = np.where((fx <= 1) & (fy <= 1), omega_hat, 0.0)
                    observation = np.fft.ifftn(low).real.ravel()
            observations.append(observation)
            recovery_errors.append(float(np.linalg.norm(estimate - protected) / math.sqrt(protected.size)))
        report = finite_recoverability_report(
            observations,
            protected_values,
            delta_grid,
            observation_metric=rms_metric,
            protected_metric=rms_metric,
        )
        rows.append(
            PeriodicRecoverabilityRow(
                observation=name,
                exact_recoverable=report.exact_recoverable,
                collision_max_protected_distance=report.collision_max_protected_distance,
                mean_recovery_error=float(np.mean(recovery_errors)),
                max_recovery_error=float(np.max(recovery_errors)),
            )
        )
        curves[name] = list(report.collapse_values)

    return {
        'delta_grid': list(float(value) for value in delta_grid),
        'rows': [row.__dict__ for row in rows],
        'curves': curves,
    }



def _lti_record_matrix(a: float, b: float, epsilon: float, horizon: int) -> Array:
    rows = []
    for t in range(horizon):
        rows.append([a**t, epsilon * (b**t)])
    return np.asarray(rows, dtype=float)



def _observer_gain(a: float, b: float, epsilon: float, poles: tuple[float, float] = (0.2, 0.3)) -> Array:
    s = poles[0] + poles[1]
    p = poles[0] * poles[1]
    mat = np.array([[1.0, epsilon], [b, a * epsilon]], dtype=float)
    rhs = np.array([a + b - s, a * b - p], dtype=float)
    if abs(np.linalg.det(mat)) <= EPS:
        raise ValueError('observer gain is undefined for the non-observable parameter choice')
    return np.linalg.solve(mat, rhs)



def _simulate_observer(a: float, b: float, epsilon: float, gain: Array, steps: int = 18) -> ObserverConvergenceReport:
    A = np.diag([a, b])
    C = np.array([[1.0, epsilon]], dtype=float)
    L = np.asarray(gain, dtype=float).reshape(2, 1)
    x = np.array([1.2, -0.8], dtype=float)
    xhat = np.array([-0.4, 0.5], dtype=float)
    errors = [abs(xhat[1] - x[1])]
    for _ in range(steps):
        y = float((C @ x).item())
        yhat = float((C @ xhat).item())
        x = A @ x
        xhat = A @ xhat + (L[:, 0] * (y - yhat))
        errors.append(abs(xhat[1] - x[1]))
    eig = np.linalg.eigvals(A - L @ C)
    return ObserverConvergenceReport(
        epsilon=float(epsilon),
        gain=np.asarray(gain, dtype=float),
        spectral_radius=float(max(abs(eig))),
        protected_error_history=tuple(float(value) for value in errors),
    )


def _box_collision_gap_from_nullspace(
    observation_matrix: Array,
    protected_matrix: Array,
    *,
    box_radius: float = 1.0,
    tol: float = EPS,
) -> float:
    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    null = _null_space(O, tol=tol)
    if null.size == 0:
        return 0.0
    basis = np.asarray(null, dtype=float)
    null_dim = basis.shape[1]
    bound = 2.0 * float(box_radius)
    if null_dim == 1:
        direction = basis[:, 0]
        protected_gain = float(np.linalg.norm(L @ direction))
        if protected_gain <= tol:
            return 0.0
        coordinate_limits = [bound / abs(value) for value in direction if abs(value) > tol]
        if not coordinate_limits:
            return 0.0
        return float(protected_gain * min(coordinate_limits))

    candidates = [np.zeros(null_dim, dtype=float)]
    coordinate_indices = range(basis.shape[0])
    for fixed_coords in product(coordinate_indices, repeat=null_dim):
        if len(set(fixed_coords)) != null_dim:
            continue
        sub = basis[list(fixed_coords), :]
        if np.linalg.matrix_rank(sub, tol=tol) < null_dim:
            continue
        for signs in product((-bound, bound), repeat=null_dim):
            alpha = np.linalg.solve(sub, np.asarray(signs, dtype=float))
            state_gap = basis @ alpha
            if np.any(np.abs(state_gap) > bound + 1e-9):
                continue
            candidates.append(alpha)

    best = 0.0
    for alpha in candidates:
        state_gap = basis @ alpha
        best = max(best, float(np.linalg.norm(L @ state_gap)))
    return float(best)



def functional_observability_sweep(
    *,
    a: float = 0.95,
    b: float = 0.65,
    epsilon_values: Sequence[float] = (0.0, 0.05, 0.1, 0.2, 0.35, 0.5, 0.8),
    horizons: Sequence[int] = (1, 2, 3),
) -> dict[str, object]:
    delta_grid = np.linspace(0.0, 4.0, 40)
    coeffs = np.linspace(-1.0, 1.0, 9)
    family_states = [np.array([x1, x2], dtype=float) for x1, x2 in product(coeffs, coeffs)]
    rows: list[FunctionalRecoverabilityRow] = []
    curves: dict[str, list[float]] = {}
    observer_reports: list[dict[str, object]] = []
    L = np.array([[0.0, 1.0]], dtype=float)

    for epsilon in epsilon_values:
        if abs(epsilon) > EPS:
            try:
                gain = _observer_gain(a, b, epsilon)
                observer = _simulate_observer(a, b, epsilon, gain)
                observer_reports.append(
                    {
                        'epsilon': observer.epsilon,
                        'gain': observer.gain.tolist(),
                        'spectral_radius': observer.spectral_radius,
                        'protected_error_history': list(observer.protected_error_history),
                    }
                )
            except ValueError:
                pass
        for horizon in horizons:
            O = _lti_record_matrix(a, b, epsilon, horizon)
            linear = restricted_linear_recoverability(O, L)
            margin = recoverability_margin_sampled(O, L)
            collision_gap = _box_collision_gap_from_nullspace(O, L)
            observations = []
            protected_values = []
            recovery_errors = []
            if linear.exact_recoverable and linear.recovery_operator is not None:
                K = linear.recovery_operator
            else:
                K = None
            for state in family_states:
                record = O @ state
                protected = L @ state
                observations.append(record)
                protected_values.append(protected)
                if K is None:
                    estimate = np.zeros_like(protected)
                else:
                    estimate = K @ record
                recovery_errors.append(float(np.linalg.norm(estimate - protected)))
            report = finite_recoverability_report(
                observations,
                protected_values,
                delta_grid,
                observation_metric=euclidean_metric,
                protected_metric=scalar_metric,
            )
            key = f'eps={epsilon:.3f}-T={horizon}'
            curves[key] = list(report.collapse_values)
            rows.append(
                FunctionalRecoverabilityRow(
                    epsilon=float(epsilon),
                    horizon=int(horizon),
                    exact_recoverable=linear.exact_recoverable,
                    collision_max_protected_distance=float(collision_gap),
                    recoverability_margin=float(margin),
                    mean_recovery_error=float(np.mean(recovery_errors)),
                    max_recovery_error=float(np.max(recovery_errors)),
                )
            )
    return {
        'a': float(a),
        'b': float(b),
        'delta_grid': list(float(value) for value in delta_grid),
        'rows': [row.__dict__ for row in rows],
        'curves': curves,
        'observer_reports': observer_reports,
    }


def _diagonal_record_matrix(eigenvalues: Sequence[float], sensor_weights: Sequence[float], horizon: int) -> Array:
    lambdas = np.asarray(eigenvalues, dtype=float)
    couplings = np.asarray(sensor_weights, dtype=float)
    rows = []
    for t in range(horizon):
        rows.append((couplings * (lambdas**t)).tolist())
    return np.asarray(rows, dtype=float)


def _active_sensor_indices(sensor_weights: Sequence[float], *, tol: float = EPS) -> list[int]:
    return [index for index, value in enumerate(sensor_weights) if abs(float(value)) > tol]


def diagonal_history_recovery_weights(
    eigenvalues: Sequence[float],
    sensor_weights: Sequence[float],
    protected_index: int,
    horizon: int,
    *,
    tol: float = EPS,
) -> Array | None:
    active = _active_sensor_indices(sensor_weights, tol=tol)
    if protected_index not in active:
        return None
    if len(active) > horizon:
        return None
    lambdas = np.asarray([float(eigenvalues[index]) for index in active], dtype=float)
    if np.min(np.abs(np.diff(np.sort(lambdas)))) <= tol:
        raise ValueError('distinct active eigenvalues are required for the interpolation-based recovery formula')
    targets = np.asarray(
        [1.0 / float(sensor_weights[index]) if index == protected_index else 0.0 for index in active],
        dtype=float,
    )
    vandermonde = np.asarray([[float(eigenvalues[index]) ** t for t in range(len(active))] for index in active], dtype=float)
    coeffs = np.linalg.solve(vandermonde, targets)
    weights = np.zeros(int(horizon), dtype=float)
    weights[: len(active)] = coeffs
    return weights


def diagonal_functional_history_weights(
    eigenvalues: Sequence[float],
    sensor_weights: Sequence[float],
    protected_weights: Sequence[float],
    horizon: int,
    *,
    tol: float = EPS,
) -> Array | None:
    couplings = np.asarray(sensor_weights, dtype=float)
    protected = np.asarray(protected_weights, dtype=float)
    active = _active_sensor_indices(couplings, tol=tol)
    inactive = [index for index in range(len(couplings)) if index not in active]
    if any(abs(float(protected[index])) > tol for index in inactive):
        return None
    if not active:
        return None
    lambdas = np.asarray([float(eigenvalues[index]) for index in active], dtype=float)
    if len(np.unique(np.round(lambdas, 12))) != len(lambdas):
        raise ValueError('distinct active eigenvalues are required for the interpolation-based functional recovery formula')
    targets = np.asarray([protected[index] / couplings[index] for index in active], dtype=float)
    if horizon <= 0:
        return None
    vandermonde = np.asarray([[lambdas[row] ** power for power in range(int(horizon))] for row in range(len(active))], dtype=float)
    coeffs, residuals, _, _ = np.linalg.lstsq(vandermonde, targets, rcond=tol)
    residual = float(np.linalg.norm(vandermonde @ coeffs - targets))
    if residual > 1e-8:
        return None
    weights = np.zeros(int(horizon), dtype=float)
    weights[:] = coeffs[: int(horizon)]
    return weights


def diagonal_functional_minimal_horizon(
    eigenvalues: Sequence[float],
    sensor_weights: Sequence[float],
    protected_weights: Sequence[float],
    *,
    max_horizon: int | None = None,
    tol: float = EPS,
) -> tuple[int | None, Array | None]:
    couplings = np.asarray(sensor_weights, dtype=float)
    active = _active_sensor_indices(couplings, tol=tol)
    if max_horizon is None:
        max_horizon = max(1, len(active))
    for horizon in range(1, int(max_horizon) + 1):
        weights = diagonal_functional_history_weights(
            eigenvalues,
            sensor_weights,
            protected_weights,
            horizon,
            tol=tol,
        )
        if weights is not None:
            return int(horizon), weights
    return None, None


def control_minimal_complexity_sweep(
    *,
    eigenvalues: Sequence[float] = (0.95, 0.8, 0.65),
    sensor_profiles: dict[str, Sequence[float]] | None = None,
    protected_index: int = 2,
    horizons: Sequence[int] = (1, 2, 3, 4),
    box_radius: float = 1.0,
    tol: float = EPS,
) -> dict[str, object]:
    if sensor_profiles is None:
        sensor_profiles = {
            'three_active': (1.0, 0.4, 0.2),
            'two_active': (1.0, 0.0, 0.2),
            'protected_hidden': (1.0, 0.4, 0.0),
        }
    n = len(tuple(eigenvalues))
    delta_grid = np.linspace(0.0, 2.0, 40)
    coeff_grid = np.linspace(-box_radius, box_radius, 7)
    family_states = [np.asarray(state, dtype=float) for state in product(coeff_grid, repeat=n)]
    rows: list[ControlComplexityRow] = []
    curves: dict[str, list[float]] = {}
    interpolation_checks: list[dict[str, object]] = []
    L = np.zeros((1, n), dtype=float)
    L[0, int(protected_index)] = 1.0

    for label, sensor_weights in sensor_profiles.items():
        active = _active_sensor_indices(sensor_weights)
        predicted_min_horizon = len(active) if protected_index in active else None
        for horizon in horizons:
            O = _diagonal_record_matrix(eigenvalues, sensor_weights, int(horizon))
            linear = restricted_linear_recoverability(O, L)
            rank_report = restricted_linear_rank_lower_bound(O, L)
            collision_gap = _box_collision_gap_from_nullspace(O, L, box_radius=box_radius)
            interpolation_weights = None
            interpolation_residual = None
            if predicted_min_horizon is not None and horizon >= predicted_min_horizon:
                interpolation_weights = diagonal_history_recovery_weights(
                    eigenvalues,
                    sensor_weights,
                    protected_index,
                    horizon,
                    tol=tol,
                )
                interpolation_residual = float(
                    np.linalg.norm(np.asarray(interpolation_weights, dtype=float).reshape(1, -1) @ O - L)
                )
            if linear.exact_recoverable and linear.recovery_operator is not None:
                estimator = linear.recovery_operator
            else:
                estimator = np.zeros((1, int(horizon)), dtype=float)

            observations: list[Array] = []
            protected_values: list[Array] = []
            recovery_errors: list[float] = []
            for state in family_states:
                record = O @ state
                protected = L @ state
                observations.append(record)
                protected_values.append(protected)
                estimate = estimator @ record
                recovery_errors.append(scalar_metric(estimate, protected))

            report = finite_recoverability_report(
                observations,
                protected_values,
                delta_grid,
                observation_metric=euclidean_metric,
                protected_metric=scalar_metric,
            )
            curves[f'{label}:H={int(horizon)}'] = list(report.collapse_values)
            rows.append(
                ControlComplexityRow(
                    sensor_profile=str(label),
                    active_sensor_count=len(active),
                    protected_index=int(protected_index),
                    horizon=int(horizon),
                    predicted_min_horizon=predicted_min_horizon,
                    exact_recoverable=bool(linear.exact_recoverable),
                    rank_observation=rank_report.rank_observation,
                    rank_protected=rank_report.rank_protected,
                    collision_max_protected_distance=float(collision_gap),
                    mean_recovery_error=float(np.mean(recovery_errors)),
                    max_recovery_error=float(np.max(recovery_errors)),
                    interpolation_residual=interpolation_residual,
                )
            )
            interpolation_checks.append(
                {
                    'sensor_profile': str(label),
                    'horizon': int(horizon),
                    'predicted_min_horizon': predicted_min_horizon,
                    'linear_exact': bool(linear.exact_recoverable),
                    'interpolation_available': interpolation_weights is not None,
                    'interpolation_residual': interpolation_residual,
                    'prediction_matches': bool(
                        linear.exact_recoverable == (predicted_min_horizon is not None and horizon >= predicted_min_horizon)
                    ),
                }
            )

    return {
        'eigenvalues': [float(value) for value in eigenvalues],
        'protected_index': int(protected_index),
        'delta_grid': list(float(value) for value in delta_grid),
        'rows': [row.__dict__ for row in rows],
        'curves': curves,
        'interpolation_checks': interpolation_checks,
    }


def diagonal_functional_complexity_sweep(
    *,
    eigenvalues: Sequence[float] = (0.95, 0.8, 0.65),
    sensor_profiles: dict[str, Sequence[float]] | None = None,
    horizons: Sequence[int] = (1, 2, 3, 4),
    box_radius: float = 1.0,
    tol: float = EPS,
) -> dict[str, object]:
    if sensor_profiles is None:
        sensor_profiles = {
            'three_active': (1.0, 0.4, 0.2),
            'two_active': (1.0, 0.0, 0.2),
            'protected_hidden': (1.0, 0.4, 0.0),
        }
    lambdas = np.asarray(eigenvalues, dtype=float)
    n = len(lambdas)
    delta_grid = np.linspace(0.0, 2.0, 40)
    coeff_grid = np.linspace(-box_radius, box_radius, 7)
    family_states = [np.asarray(state, dtype=float) for state in product(coeff_grid, repeat=n)]
    rows: list[DiagonalFunctionalComplexityRow] = []
    curves: dict[str, list[float]] = {}
    interpolation_checks: list[dict[str, object]] = []

    for label, sensor_weights in sensor_profiles.items():
        couplings = np.asarray(sensor_weights, dtype=float)
        functionals: dict[str, Array] = {
            'sensor_sum': couplings.copy(),
            'first_moment': couplings * lambdas,
            'second_moment': couplings * (lambdas**2),
            'protected_coordinate': np.array([0.0, 0.0, 1.0], dtype=float),
        }
        for functional_name, protected_weights in functionals.items():
            predicted_min_horizon, predicted_weights = diagonal_functional_minimal_horizon(
                eigenvalues,
                sensor_weights,
                protected_weights,
                max_horizon=max(horizons),
                tol=tol,
            )
            L = np.asarray([protected_weights], dtype=float)
            for horizon in horizons:
                O = _diagonal_record_matrix(eigenvalues, sensor_weights, int(horizon))
                linear = restricted_linear_recoverability(O, L)
                rank_report = restricted_linear_rank_lower_bound(O, L)
                collision_gap = _box_collision_gap_from_nullspace(O, L, box_radius=box_radius)
                interpolation_weights = diagonal_functional_history_weights(
                    eigenvalues,
                    sensor_weights,
                    protected_weights,
                    int(horizon),
                    tol=tol,
                )
                interpolation_residual = None
                if interpolation_weights is not None:
                    interpolation_residual = float(
                        np.linalg.norm(np.asarray(interpolation_weights, dtype=float).reshape(1, -1) @ O - L)
                    )
                estimator = linear.recovery_operator if linear.exact_recoverable and linear.recovery_operator is not None else np.zeros((1, int(horizon)), dtype=float)

                observations: list[Array] = []
                protected_values: list[Array] = []
                errors: list[float] = []
                for state in family_states:
                    record = O @ state
                    protected = L @ state
                    observations.append(record)
                    protected_values.append(protected)
                    estimate = estimator @ record
                    errors.append(scalar_metric(estimate, protected))

                report = finite_recoverability_report(
                    observations,
                    protected_values,
                    delta_grid,
                    observation_metric=euclidean_metric,
                    protected_metric=scalar_metric,
                )
                rows.append(
                    DiagonalFunctionalComplexityRow(
                        sensor_profile=str(label),
                        functional_name=str(functional_name),
                        horizon=int(horizon),
                        predicted_min_horizon=predicted_min_horizon,
                        exact_recoverable=bool(linear.exact_recoverable),
                        rank_observation=rank_report.rank_observation,
                        rank_protected=rank_report.rank_protected,
                        collision_max_protected_distance=float(collision_gap),
                        mean_recovery_error=float(np.mean(errors)),
                        max_recovery_error=float(np.max(errors)),
                        interpolation_residual=interpolation_residual,
                    )
                )
                curves[f'{label}:{functional_name}:H={int(horizon)}'] = list(report.collapse_values)
                interpolation_checks.append(
                    {
                        'sensor_profile': str(label),
                        'functional_name': str(functional_name),
                        'horizon': int(horizon),
                        'predicted_min_horizon': predicted_min_horizon,
                        'prediction_matches': bool(
                            linear.exact_recoverable
                            == (predicted_min_horizon is not None and int(horizon) >= predicted_min_horizon)
                        ),
                        'interpolation_available': interpolation_weights is not None,
                        'interpolation_residual': interpolation_residual,
                        'exact_recoverable': bool(linear.exact_recoverable),
                    }
                )

    return {
        'eigenvalues': [float(value) for value in eigenvalues],
        'delta_grid': list(float(value) for value in delta_grid),
        'rows': [row.__dict__ for row in rows],
        'curves': curves,
        'interpolation_checks': interpolation_checks,
    }


def _coefficient_grid_family(dim: int, *, box_radius: float = 1.0, points_per_axis: int = 5) -> list[Array]:
    coeff_grid = np.linspace(-float(box_radius), float(box_radius), int(points_per_axis))
    return [np.asarray(coeffs, dtype=float) for coeffs in product(coeff_grid, repeat=int(dim))]


def _linear_recovery_error_stats(
    observation_matrix: Array,
    protected_matrix: Array,
    coefficient_family: Sequence[Array],
    *,
    tol: float = EPS,
) -> tuple[float, float]:
    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(protected_matrix, dtype=float)
    linear = restricted_linear_recoverability(O, L, tol=tol)
    if linear.exact_recoverable and linear.recovery_operator is not None:
        estimator = linear.recovery_operator
    else:
        estimator = L @ np.linalg.pinv(O, rcond=tol)
    metric: Metric = scalar_metric if L.shape[0] == 1 else euclidean_metric
    errors = [metric(estimator @ (O @ coeffs), L @ coeffs) for coeffs in coefficient_family]
    return float(np.mean(errors)), float(np.max(errors))


def periodic_threshold_stress_sweep(
    *,
    n: int = 18,
    cutoffs: Sequence[int] | None = None,
    box_radius: float = 1.0,
    points_per_axis: int = 5,
    cases: dict[str, dict[str, object]] | None = None,
    tol: float = EPS,
) -> dict[str, object]:
    if cases is None:
        cases = {
            'strict_cutoffs': {
                'modes': ((1, 1, 1.0), (2, 1, 0.8), (3, 1, 0.6), (4, 1, 0.45)),
                'functionals': {
                    'low_mode_sum': (1.0, 1.0, 0.0, 0.0),
                    'bandlimited_contrast': (0.0, 1.0, -1.0, 0.0),
                    'full_weighted_sum': (1.0, -0.5, 0.75, 0.25),
                },
            },
            'repeated_cutoffs': {
                'modes': ((1, 1, 1.0), (1, 2, 0.9), (2, 1, 0.85), (2, 2, 0.7), (3, 1, 0.55)),
                'functionals': {
                    'repeated_cutoff_mass': (0.0, 1.0, 1.0, 1.0, 0.0),
                    'mixed_tail': (0.2, 0.0, -0.3, 0.0, 0.5),
                },
            },
        }

    rows: list[PeriodicThresholdStressRow] = []
    summaries: list[dict[str, object]] = []
    for case_name, case in cases.items():
        modes = tuple(case['modes'])
        functionals = dict(case['functionals'])
        basis = _periodic_modal_basis_states(n=n, modes=modes)
        mode_cutoffs = [max(abs(kx), abs(ky)) for kx, ky, _ in modes]
        case_cutoffs = tuple(range(0, max(mode_cutoffs) + 1)) if cutoffs is None else tuple(int(value) for value in cutoffs)
        basis_observations = [
            np.column_stack([_truncate_vorticity(state['omega'], int(cutoff)).ravel() for state in basis])
            if int(cutoff) > 0
            else np.zeros((basis[0]['omega'].size, len(basis)), dtype=float)
            for cutoff in case_cutoffs
        ]
        coefficient_family = _coefficient_grid_family(len(modes), box_radius=box_radius, points_per_axis=points_per_axis)

        for functional_name, coefficients in functionals.items():
            selector = np.asarray([coefficients], dtype=float)
            support = [index for index, value in enumerate(selector.reshape(-1)) if abs(float(value)) > tol]
            predicted_min_cutoff = 0 if not support else int(max(mode_cutoffs[index] for index in support))
            profile = nested_linear_threshold_profile(
                basis_observations,
                selector,
                box_radius=box_radius,
                level_labels=case_cutoffs,
                tol=tol,
            )
            observed_min_cutoff = None if profile['minimal_label'] is None else int(profile['minimal_label'])
            summaries.append(
                {
                    'case_name': str(case_name),
                    'functional_name': str(functional_name),
                    'support_size': len(support),
                    'predicted_min_cutoff': predicted_min_cutoff,
                    'observed_min_cutoff': observed_min_cutoff,
                    'gap_monotone_nonincreasing': profile['gap_monotone_nonincreasing'],
                    'exact_gap_match': profile['exact_gap_match'],
                }
            )
            for cutoff, observation_matrix, row in zip(case_cutoffs, basis_observations, profile['rows'], strict=True):
                mean_error, max_error = _linear_recovery_error_stats(observation_matrix, selector, coefficient_family, tol=tol)
                rows.append(
                    PeriodicThresholdStressRow(
                        case_name=str(case_name),
                        functional_name=str(functional_name),
                        support_size=len(support),
                        cutoff=int(cutoff),
                        predicted_min_cutoff=predicted_min_cutoff,
                        observed_min_cutoff=observed_min_cutoff,
                        exact_recoverable=bool(row['exact_recoverable']),
                        rowspace_residual=float(row['rowspace_residual']),
                        collision_gap=float(row['collision_gap']),
                        mean_recovery_error=mean_error,
                        max_recovery_error=max_error,
                    )
                )

    return {
        'rows': [row.__dict__ for row in rows],
        'summaries': summaries,
        'cases': {
            name: {
                'modes': [{'kx': int(kx), 'ky': int(ky), 'weight': float(weight)} for kx, ky, weight in case['modes']],
                'functionals': {fname: [float(value) for value in values] for fname, values in case['functionals'].items()},
            }
            for name, case in cases.items()
        },
    }


def diagonal_polynomial_threshold_sweep(
    *,
    horizons: Sequence[int] | None = None,
    box_radius: float = 1.0,
    points_per_axis: int = 5,
    cases: dict[str, dict[str, object]] | None = None,
    tol: float = EPS,
) -> dict[str, object]:
    if cases is None:
        cases = {
            'four_active': {
                'eigenvalues': (0.97, 0.83, 0.71, 0.59),
                'sensor_weights': (1.0, 0.7, 0.45, 0.2),
                'functionals': {
                    'degree_0_constant': {'polynomial_coeffs': (1.0,)},
                    'degree_1_affine': {'polynomial_coeffs': (0.5, -1.2)},
                    'degree_2_quadratic': {'polynomial_coeffs': (0.2, -0.4, 0.8)},
                    'degree_3_cubic': {'polynomial_coeffs': (0.1, 0.2, -0.3, 1.0)},
                },
            },
            'hidden_last': {
                'eigenvalues': (0.97, 0.83, 0.71, 0.59),
                'sensor_weights': (1.0, 0.7, 0.45, 0.0),
                'functionals': {
                    'degree_1_affine': {'polynomial_coeffs': (1.0, -0.4)},
                    'hidden_coordinate': {'protected_weights': (0.0, 0.0, 0.0, 1.0)},
                },
            },
        }

    rows: list[DiagonalPolynomialThresholdRow] = []
    summaries: list[dict[str, object]] = []
    for case_name, case in cases.items():
        eigenvalues = tuple(float(value) for value in case['eigenvalues'])
        sensor_weights = tuple(float(value) for value in case['sensor_weights'])
        n = len(eigenvalues)
        case_horizons = tuple(range(1, n + 2)) if horizons is None else tuple(int(value) for value in horizons)
        observation_family = [_diagonal_record_matrix(eigenvalues, sensor_weights, int(horizon)) for horizon in case_horizons]
        coefficient_family = _coefficient_grid_family(n, box_radius=box_radius, points_per_axis=points_per_axis)

        for functional_name, descriptor in case['functionals'].items():
            polynomial_coeffs = descriptor.get('polynomial_coeffs')
            if polynomial_coeffs is not None:
                polynomial_degree = max(index for index, value in enumerate(polynomial_coeffs) if abs(float(value)) > tol)
                protected_weights = tuple(
                    float(sensor_weights[index]) * sum(float(coeff) * (float(eigenvalues[index]) ** power) for power, coeff in enumerate(polynomial_coeffs))
                    for index in range(n)
                )
            else:
                polynomial_degree = None
                protected_weights = tuple(float(value) for value in descriptor['protected_weights'])
            protected_vector = np.asarray(protected_weights, dtype=float)
            support_size = int(np.sum(np.abs(protected_vector) > tol))
            predicted_min_horizon, _ = diagonal_functional_minimal_horizon(
                eigenvalues,
                sensor_weights,
                protected_weights,
                max_horizon=max(case_horizons),
                tol=tol,
            )
            selector = np.asarray([protected_weights], dtype=float)
            profile = nested_linear_threshold_profile(
                observation_family,
                selector,
                box_radius=box_radius,
                level_labels=case_horizons,
                tol=tol,
            )
            observed_min_horizon = None if profile['minimal_label'] is None else int(profile['minimal_label'])
            summaries.append(
                {
                    'case_name': str(case_name),
                    'functional_name': str(functional_name),
                    'support_size': support_size,
                    'polynomial_degree': polynomial_degree,
                    'predicted_min_horizon': predicted_min_horizon,
                    'observed_min_horizon': observed_min_horizon,
                    'gap_monotone_nonincreasing': profile['gap_monotone_nonincreasing'],
                    'exact_gap_match': profile['exact_gap_match'],
                }
            )
            for horizon, observation_matrix, row in zip(case_horizons, observation_family, profile['rows'], strict=True):
                mean_error, max_error = _linear_recovery_error_stats(observation_matrix, selector, coefficient_family, tol=tol)
                rows.append(
                    DiagonalPolynomialThresholdRow(
                        case_name=str(case_name),
                        functional_name=str(functional_name),
                        support_size=support_size,
                        polynomial_degree=polynomial_degree,
                        horizon=int(horizon),
                        predicted_min_horizon=predicted_min_horizon,
                        observed_min_horizon=observed_min_horizon,
                        exact_recoverable=bool(row['exact_recoverable']),
                        rowspace_residual=float(row['rowspace_residual']),
                        collision_gap=float(row['collision_gap']),
                        mean_recovery_error=mean_error,
                        max_recovery_error=max_error,
                    )
                )

    return {
        'rows': [row.__dict__ for row in rows],
        'summaries': summaries,
        'cases': {
            name: {
                'eigenvalues': [float(value) for value in case['eigenvalues']],
                'sensor_weights': [float(value) for value in case['sensor_weights']],
                'functionals': {
                    functional_name: {
                        key: [float(value) for value in values]
                        for key, values in descriptor.items()
                    }
                    for functional_name, descriptor in case['functionals'].items()
                },
            }
            for name, case in cases.items()
        },
    }


def analytic_noise_lower_bound_sweep(
    *,
    epsilon: float,
    noise_radii: Sequence[float] = tuple(np.linspace(0.0, 0.5, 11)),
) -> dict[str, object]:
    rows = [
        NoiseLowerBoundRow(
            noise_radius=float(radius),
            lower_bound=float(0.5 * analytic_collapse_modulus(epsilon, [radius]).collapse_values[0]),
        )
        for radius in noise_radii
    ]
    return {
        'epsilon': float(epsilon),
        'rows': [row.__dict__ for row in rows],
    }
