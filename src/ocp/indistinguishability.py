from __future__ import annotations

"""Finite-family indistinguishability metrics for exploratory analysis lanes.

This module is intentionally scoped to executable finite families and
restricted-linear families represented by sampled states. It does not provide
theorem-status claims; it provides diagnostics for the exploration layer.
"""

from dataclasses import dataclass
import math
from typing import Sequence

import numpy as np

Array = np.ndarray


def _as_flat_array(value: Array) -> Array:
    return np.asarray(value, dtype=float).reshape(-1)


def _quantized_key(value: Array, *, tol: float) -> tuple[int, ...]:
    if tol <= 0.0:
        raise ValueError("tol must be positive")
    arr = _as_flat_array(value)
    return tuple(np.rint(arr / tol).astype(np.int64).tolist())


def _pairwise_distances(values: Sequence[Array]) -> Array:
    if not values:
        return np.zeros((0, 0), dtype=float)
    arr = np.asarray([_as_flat_array(value) for value in values], dtype=float)
    if arr.ndim == 1:
        arr = arr[:, None]
    diff = arr[:, None, :] - arr[None, :, :]
    return np.linalg.norm(diff, axis=2)


@dataclass(frozen=True)
class FiberSummary:
    fiber_count: int
    max_fiber_size: int
    mean_fiber_size: float
    fiber_size_histogram: dict[str, int]
    percent_mixed: float
    max_mixedness: int
    mixed_fiber_count: int
    dls: float
    kappa_0: float
    mean_target_variance: float
    max_target_variance: float
    mean_within_fiber_distance: float
    max_within_fiber_distance: float
    cluster_counts: dict[str, int]
    fiber_sizes: tuple[int, ...]
    mixedness_values: tuple[int, ...]


def summarize_fibers(
    observations: Sequence[Array],
    targets: Sequence[Array],
    *,
    observation_tol: float = 1e-9,
    target_tol: float = 1e-9,
) -> FiberSummary:
    if len(observations) != len(targets):
        raise ValueError("observations and targets must have matching lengths")
    if not observations:
        return FiberSummary(
            fiber_count=0,
            max_fiber_size=0,
            mean_fiber_size=0.0,
            fiber_size_histogram={},
            percent_mixed=0.0,
            max_mixedness=0,
            mixed_fiber_count=0,
            dls=0.0,
            kappa_0=0.0,
            mean_target_variance=0.0,
            max_target_variance=0.0,
            mean_within_fiber_distance=0.0,
            max_within_fiber_distance=0.0,
            cluster_counts={},
            fiber_sizes=(),
            mixedness_values=(),
        )

    groups: dict[tuple[int, ...], list[int]] = {}
    for index, observation in enumerate(observations):
        key = _quantized_key(observation, tol=observation_tol)
        groups.setdefault(key, []).append(index)

    fiber_sizes: list[int] = []
    mixedness_values: list[int] = []
    within_max_values: list[float] = []
    within_mean_values: list[float] = []
    variance_values: list[float] = []
    cluster_counts = {
        "pure": 0,
        "mixed_low": 0,
        "mixed_medium": 0,
        "mixed_high": 0,
    }
    mismatch_pairs = 0
    total_pairs = 0

    for indices in groups.values():
        fiber_sizes.append(len(indices))
        fiber_targets = [_as_flat_array(targets[index]) for index in indices]
        target_keys = {_quantized_key(target, tol=target_tol) for target in fiber_targets}
        mixedness = len(target_keys)
        mixedness_values.append(mixedness)

        pairwise = _pairwise_distances(fiber_targets)
        if pairwise.size:
            upper = np.triu_indices(pairwise.shape[0], k=1)
            distances = pairwise[upper]
            if distances.size:
                total_pairs += int(distances.size)
                mismatch_pairs += int(np.sum(distances > target_tol))
                max_distance = float(np.max(distances))
                mean_distance = float(np.mean(distances))
            else:
                max_distance = 0.0
                mean_distance = 0.0
        else:
            max_distance = 0.0
            mean_distance = 0.0
        within_max_values.append(max_distance)
        within_mean_values.append(mean_distance)

        target_matrix = np.asarray(fiber_targets, dtype=float)
        if target_matrix.ndim == 1:
            target_matrix = target_matrix[:, None]
        variance = float(np.var(target_matrix, axis=0).mean()) if target_matrix.size else 0.0
        variance_values.append(variance)

        if mixedness <= 1 or max_distance <= target_tol:
            cluster_counts["pure"] += 1
        elif max_distance <= 0.5:
            cluster_counts["mixed_low"] += 1
        elif max_distance <= 2.0:
            cluster_counts["mixed_medium"] += 1
        else:
            cluster_counts["mixed_high"] += 1

    histogram: dict[str, int] = {}
    for size in fiber_sizes:
        key = str(size)
        histogram[key] = histogram.get(key, 0) + 1

    mixed_fiber_count = sum(1 for value in mixedness_values if value > 1)
    percent_mixed = float(100.0 * mixed_fiber_count / max(len(mixedness_values), 1))
    dls = float(mismatch_pairs / total_pairs) if total_pairs > 0 else 0.0
    kappa_0 = float(max(within_max_values)) if within_max_values else 0.0
    mean_target_variance = float(np.mean(variance_values)) if variance_values else 0.0
    max_target_variance = float(np.max(variance_values)) if variance_values else 0.0
    mean_within_distance = float(np.mean(within_mean_values)) if within_mean_values else 0.0
    max_within_distance = float(np.max(within_max_values)) if within_max_values else 0.0

    return FiberSummary(
        fiber_count=len(fiber_sizes),
        max_fiber_size=max(fiber_sizes),
        mean_fiber_size=float(np.mean(fiber_sizes)),
        fiber_size_histogram=histogram,
        percent_mixed=percent_mixed,
        max_mixedness=max(mixedness_values),
        mixed_fiber_count=mixed_fiber_count,
        dls=dls,
        kappa_0=kappa_0,
        mean_target_variance=mean_target_variance,
        max_target_variance=max_target_variance,
        mean_within_fiber_distance=mean_within_distance,
        max_within_fiber_distance=max_within_distance,
        cluster_counts=cluster_counts,
        fiber_sizes=tuple(int(value) for value in fiber_sizes),
        mixedness_values=tuple(int(value) for value in mixedness_values),
    )


def pearson_correlation(xs: Sequence[float], ys: Sequence[float]) -> float | None:
    if len(xs) != len(ys):
        raise ValueError("xs and ys must have matching lengths")
    x = np.asarray(xs, dtype=float)
    y = np.asarray(ys, dtype=float)
    valid = np.isfinite(x) & np.isfinite(y)
    x = x[valid]
    y = y[valid]
    if x.size < 2 or y.size < 2:
        return None
    x_std = float(np.std(x))
    y_std = float(np.std(y))
    if x_std <= 0.0 or y_std <= 0.0:
        return None
    corr = float(np.corrcoef(x, y)[0, 1])
    if math.isnan(corr):
        return None
    return corr


__all__ = [
    "FiberSummary",
    "pearson_correlation",
    "summarize_fibers",
]

