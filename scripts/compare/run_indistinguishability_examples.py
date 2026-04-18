#!/usr/bin/env python3
from __future__ import annotations

"""Indistinguishability exploration lane (non-promoted).

This script builds finite-family indistinguishability diagnostics across
supported OCP/recoverability families and writes exploratory artifacts.
"""

import csv
import json
from itertools import product
from pathlib import Path
from typing import Iterable

import numpy as np

from ocp.capacity import restricted_linear_capacity
from ocp.cfd import (
    _bounded_divergence,
    _bounded_gradient_mode,
    _bounded_stream_velocity_mode,
    _orthonormalize_columns,
    _stack_field,
    _unstack_field,
)
from ocp.indistinguishability import pearson_correlation, summarize_fibers
from ocp.mhd import divergence_2d, helmholtz_project_2d
from ocp.recoverability import (
    _periodic_modal_basis_states,
    _truncate_vorticity,
    restricted_linear_collision_gap,
    restricted_linear_recoverability,
    same_rank_alignment_counterexample,
)

ROOT = Path("/Users/stevenreid/Documents/New project/repos/ocp-research-program")
OUT_DIR = ROOT / "data/generated/indistinguishability"
FIG_DIR = ROOT / "figures/indistinguishability"
REPORT_PATH = ROOT / "docs/research-program/indistinguishability_exploration.md"
STATUS_LABEL = "EXPLORATION / NON-PROMOTED"


def _coefficient_grid(dimension: int, values: Iterable[float] = (-1.0, 0.0, 1.0)) -> list[np.ndarray]:
    vals = tuple(float(value) for value in values)
    if dimension <= 0:
        return [np.zeros(0, dtype=float)]
    return [np.asarray(point, dtype=float) for point in product(vals, repeat=dimension)]


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _evaluate_linear_case(
    *,
    system_id: str,
    family: str,
    observation_name: str,
    target_name: str,
    observation_matrix: np.ndarray,
    target_matrix: np.ndarray,
    coefficient_values: tuple[float, ...] = (-1.0, 0.0, 1.0),
    series_key: str | None = None,
    series_level: float | None = None,
) -> tuple[dict[str, object], dict[str, object]]:
    O = np.asarray(observation_matrix, dtype=float)
    L = np.asarray(target_matrix, dtype=float)
    coeffs = _coefficient_grid(int(O.shape[1]), coefficient_values)
    observations = [O @ coeff for coeff in coeffs]
    targets = [L @ coeff for coeff in coeffs]
    fiber = summarize_fibers(observations, targets, observation_tol=1e-9, target_tol=1e-9)
    stability = restricted_linear_recoverability(O, L, tol=1e-10)
    capacity = restricted_linear_capacity(O, L, tol=1e-10)
    gamma_r = float(restricted_linear_collision_gap(O, L, box_radius=1.0, tol=1e-10))

    cluster = "sparse-collision"
    if fiber.dls <= 0.02 and fiber.percent_mixed <= 5.0:
        cluster = "low-loss/pure"
    elif fiber.dls >= 0.35:
        cluster = "high-loss/mixed"
    elif fiber.dls >= 0.12:
        cluster = "moderate-loss"

    row = {
        "system_id": system_id,
        "family": family,
        "rank": int(capacity.rank_observation),
        "max_fiber_size": int(fiber.max_fiber_size),
        "percent_mixed": float(fiber.percent_mixed),
        "DLS": float(fiber.dls),
        "kappa_0": float(fiber.kappa_0),
        "Gamma_r": gamma_r,
        "delta": int(capacity.min_unrestricted_added_measurements),
        "target_rank": int(capacity.rank_protected),
        "exact_recoverable": bool(stability.exact_recoverable),
        "observation_name": observation_name,
        "target_name": target_name,
        "fiber_count": int(fiber.fiber_count),
        "mean_fiber_size": float(fiber.mean_fiber_size),
        "max_mixedness": int(fiber.max_mixedness),
        "mixed_fiber_count": int(fiber.mixed_fiber_count),
        "mean_target_variance": float(fiber.mean_target_variance),
        "max_target_variance": float(fiber.max_target_variance),
        "mean_within_fiber_distance": float(fiber.mean_within_fiber_distance),
        "max_within_fiber_distance": float(fiber.max_within_fiber_distance),
        "cluster": cluster,
        "series_key": "" if series_key is None else series_key,
        "series_level": "" if series_level is None else float(series_level),
        "status_label": STATUS_LABEL,
    }
    aux = {
        "system_id": system_id,
        "fiber_sizes": list(fiber.fiber_sizes),
        "mixedness_values": list(fiber.mixedness_values),
        "cluster_counts": fiber.cluster_counts,
    }
    return row, aux


def _restricted_linear_cases() -> list[tuple[dict[str, object], dict[str, object]]]:
    out: list[tuple[dict[str, object], dict[str, object]]] = []
    for ambient_dimension, protected_rank, observation_rank in ((5, 2, 2), (6, 2, 3)):
        witness = same_rank_alignment_counterexample(
            ambient_dimension=ambient_dimension,
            protected_rank=protected_rank,
            observation_rank=observation_rank,
        )
        out.append(
            _evaluate_linear_case(
                system_id=f"restricted_linear_same_rank_exact_n{ambient_dimension}_r{protected_rank}_k{observation_rank}",
                family="restricted-linear",
                observation_name="same-rank exact observation",
                target_name="protected coordinates",
                observation_matrix=witness.exact_observation_matrix,
                target_matrix=witness.protected_matrix,
                series_key=f"restricted_linear_same_rank_n{ambient_dimension}_r{protected_rank}_k{observation_rank}",
                series_level=1.0,
            )
        )
        out.append(
            _evaluate_linear_case(
                system_id=f"restricted_linear_same_rank_fail_n{ambient_dimension}_r{protected_rank}_k{observation_rank}",
                family="restricted-linear",
                observation_name="same-rank fail observation",
                target_name="protected coordinates",
                observation_matrix=witness.fail_observation_matrix,
                target_matrix=witness.protected_matrix,
                series_key=f"restricted_linear_same_rank_n{ambient_dimension}_r{protected_rank}_k{observation_rank}",
                series_level=2.0,
            )
        )
    return out


def _periodic_modal_cases() -> list[tuple[dict[str, object], dict[str, object]]]:
    out: list[tuple[dict[str, object], dict[str, object]]] = []
    modes = ((1, 1, 1.0), (2, 1, 0.8), (3, 1, 0.6), (4, 1, 0.45))
    basis = _periodic_modal_basis_states(n=24, modes=modes)
    mode_count = len(basis)
    truncations = (1, 2, 4)
    targets = {
        "full_modal_coefficients": np.eye(mode_count, dtype=float),
        "low_mode_sum": np.array([[1.0, 1.0, 0.0, 0.0]], dtype=float),
    }

    for cutoff in truncations:
        observation_matrix = np.column_stack([_truncate_vorticity(state["omega"], int(cutoff)).ravel() for state in basis])
        for target_name, target_matrix in targets.items():
            out.append(
                _evaluate_linear_case(
                    system_id=f"periodic_modal_cutoff_{cutoff}_{target_name}",
                    family="periodic-cfd",
                    observation_name=f"truncated vorticity cutoff={cutoff}",
                    target_name=target_name,
                    observation_matrix=observation_matrix,
                    target_matrix=target_matrix,
                    series_key=f"periodic_modal_{target_name}",
                    series_level=float(cutoff),
                )
            )
    return out


def _bounded_cfd_cases() -> list[tuple[dict[str, object], dict[str, object]]]:
    out: list[tuple[dict[str, object], dict[str, object]]] = []
    n = 33
    protected_modes = ((1, 1), (1, 2))
    disturbance_modes = ((1, 1), (2, 1))
    protected_columns = [_stack_field(*_bounded_stream_velocity_mode(n, mx, my)) for mx, my in protected_modes]
    disturbance_columns = [_stack_field(*_bounded_gradient_mode(n, mx, my)) for mx, my in disturbance_modes]
    basis_matrix = np.column_stack([*protected_columns, *disturbance_columns])
    protected_count = len(protected_columns)
    target_matrix = np.hstack(
        [
            np.eye(protected_count, dtype=float),
            np.zeros((protected_count, basis_matrix.shape[1] - protected_count), dtype=float),
        ]
    )
    q_protected = _orthonormalize_columns(np.column_stack(protected_columns))

    h = 1.0 / (n - 1)

    def divergence_observation(state_vector: np.ndarray) -> np.ndarray:
        Ux, Uy = _unstack_field(state_vector, n)
        return _bounded_divergence(Ux, Uy, h).ravel()

    def protected_projection_observation(state_vector: np.ndarray) -> np.ndarray:
        return q_protected.T @ state_vector

    maps = {
        "divergence-only bounded observation": divergence_observation,
        "full bounded state observation": lambda state: state,
        "protected-projected bounded observation": protected_projection_observation,
    }

    for level, (name, op) in enumerate(maps.items(), start=1):
        observation_matrix = np.column_stack([op(basis_matrix[:, index]) for index in range(basis_matrix.shape[1])])
        out.append(
            _evaluate_linear_case(
                system_id=f"bounded_cfd_{name.replace(' ', '_').replace('-', '_')}",
                family="bounded-cfd",
                observation_name=name,
                target_name="protected stream coefficients",
                observation_matrix=observation_matrix,
                target_matrix=target_matrix,
                series_key="bounded_cfd_observation_family",
                series_level=float(level),
            )
        )
    return out


def _mhd_cases() -> list[tuple[dict[str, object], dict[str, object]]]:
    out: list[tuple[dict[str, object], dict[str, object]]] = []
    n = 32
    h = 1.0 / n
    x = np.linspace(0.0, 1.0, n, endpoint=False)
    y = np.linspace(0.0, 1.0, n, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")

    def ddx(field: np.ndarray) -> np.ndarray:
        return (np.roll(field, -1, axis=0) - np.roll(field, 1, axis=0)) / (2.0 * h)

    def ddy(field: np.ndarray) -> np.ndarray:
        return (np.roll(field, -1, axis=1) - np.roll(field, 1, axis=1)) / (2.0 * h)

    stream_modes = [
        np.sin(2.0 * np.pi * X) * np.sin(2.0 * np.pi * Y),
        0.8 * np.sin(4.0 * np.pi * X) * np.sin(2.0 * np.pi * Y),
    ]
    grad_modes = [
        np.cos(2.0 * np.pi * X) * np.cos(2.0 * np.pi * Y),
        np.cos(4.0 * np.pi * X) * np.cos(2.0 * np.pi * Y),
    ]
    columns: list[np.ndarray] = []
    for stream in stream_modes:
        Bx = ddy(stream)
        By = -ddx(stream)
        columns.append(np.concatenate([Bx.ravel(), By.ravel()]))
    for potential in grad_modes:
        Bx = ddx(potential)
        By = ddy(potential)
        columns.append(np.concatenate([Bx.ravel(), By.ravel()]))
    basis_matrix = np.column_stack(columns)
    protected_count = len(stream_modes)
    target_matrix = np.hstack(
        [
            np.eye(protected_count, dtype=float),
            np.zeros((protected_count, basis_matrix.shape[1] - protected_count), dtype=float),
        ]
    )

    def divergence_only_observation(state_vector: np.ndarray) -> np.ndarray:
        size = n * n
        Bx = state_vector[:size].reshape((n, n))
        By = state_vector[size:].reshape((n, n))
        return divergence_2d(Bx, By, h, h).ravel()

    def projected_field_observation(state_vector: np.ndarray) -> np.ndarray:
        size = n * n
        Bx = state_vector[:size].reshape((n, n))
        By = state_vector[size:].reshape((n, n))
        Bx_proj, By_proj, _, _ = helmholtz_project_2d(Bx, By, h, h)
        return np.concatenate([Bx_proj.ravel(), By_proj.ravel()])

    maps = {
        "mhd divergence-only observation": divergence_only_observation,
        "mhd full field observation": lambda state: state,
        "mhd Helmholtz-projected observation": projected_field_observation,
    }
    for level, (name, op) in enumerate(maps.items(), start=1):
        observation_matrix = np.column_stack([op(basis_matrix[:, index]) for index in range(basis_matrix.shape[1])])
        out.append(
            _evaluate_linear_case(
                system_id=f"mhd_{name.replace(' ', '_').replace('-', '_')}",
                family="mhd-proxy",
                observation_name=name,
                target_name="divergence-free coefficients",
                observation_matrix=observation_matrix,
                target_matrix=target_matrix,
                series_key="mhd_observation_family",
                series_level=float(level),
            )
        )
    return out


def _detect_anomalies(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    if not rows:
        return []
    ranks = np.asarray([float(row["rank"]) for row in rows], dtype=float)
    rank_q25 = float(np.quantile(ranks, 0.25))
    rank_q75 = float(np.quantile(ranks, 0.75))
    anomalies: list[dict[str, object]] = []

    for row in rows:
        system_id = str(row["system_id"])
        rank = float(row["rank"])
        dls = float(row["DLS"])
        delta = float(row["delta"])
        target_rank = float(row["target_rank"])
        exact_recoverable = bool(row["exact_recoverable"])

        if rank >= rank_q75 and dls >= 0.25:
            anomalies.append(
                {
                    "system_id": system_id,
                    "anomaly_type": "high_rank_high_dls",
                    "severity": "HIGH",
                    "details": f"rank={rank:.1f}, DLS={dls:.3f}",
                }
            )
        if rank <= rank_q25 and dls <= 0.03:
            anomalies.append(
                {
                    "system_id": system_id,
                    "anomaly_type": "low_rank_low_dls",
                    "severity": "MEDIUM",
                    "details": f"rank={rank:.1f}, DLS={dls:.3f}",
                }
            )
        if rank >= target_rank and dls >= 0.10:
            anomalies.append(
                {
                    "system_id": system_id,
                    "anomaly_type": "rank_predicts_success_but_dls_high",
                    "severity": "HIGH",
                    "details": f"rank={rank:.1f}, target_rank={target_rank:.1f}, DLS={dls:.3f}",
                }
            )
        if exact_recoverable and dls > 1e-8:
            anomalies.append(
                {
                    "system_id": system_id,
                    "anomaly_type": "dls_contradicts_exact_recoverability",
                    "severity": "HIGH",
                    "details": f"exact_recoverable=True but DLS={dls:.6f}",
                }
            )
        if (not exact_recoverable) and dls <= 1e-8:
            anomalies.append(
                {
                    "system_id": system_id,
                    "anomaly_type": "zero_dls_but_nonexact",
                    "severity": "MEDIUM",
                    "details": f"exact_recoverable=False with DLS={dls:.6f}",
                }
            )
        if delta <= 1.0 and dls >= 0.35:
            anomalies.append(
                {
                    "system_id": system_id,
                    "anomaly_type": "high_dls_small_delta",
                    "severity": "MEDIUM",
                    "details": f"delta={delta:.1f}, DLS={dls:.3f}",
                }
            )

    grouped: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        key = str(row.get("series_key", "")).strip()
        if not key:
            continue
        grouped.setdefault(key, []).append(row)
    for series_key, series_rows in grouped.items():
        valid = [row for row in series_rows if str(row.get("series_level", "")).strip()]
        if len(valid) < 2:
            continue
        valid.sort(key=lambda item: float(item["series_level"]))
        for first, second in zip(valid[:-1], valid[1:], strict=True):
            dls_drop = float(first["DLS"]) - float(second["DLS"])
            delta_drop = float(first["delta"]) - float(second["delta"])
            if dls_drop >= 0.25 and delta_drop >= 1.0:
                anomalies.append(
                    {
                        "system_id": str(second["system_id"]),
                        "anomaly_type": "augmentation_threshold_dls_drop",
                        "severity": "HIGH",
                        "details": (
                            f"series={series_key}, DLS drop={dls_drop:.3f}, "
                            f"delta drop={delta_drop:.1f} ({first['system_id']} -> {second['system_id']})"
                        ),
                    }
                )
    return anomalies


def _build_plots(rows: list[dict[str, object]], all_fiber_sizes: list[int], out_dir: Path) -> list[str]:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    out_dir.mkdir(parents=True, exist_ok=True)
    files: list[str] = []
    families = sorted({str(row["family"]) for row in rows})
    palette = plt.cm.tab10(np.linspace(0.05, 0.95, max(1, len(families))))
    color_by_family = {family: palette[index % len(palette)] for index, family in enumerate(families)}

    # DLS vs rank
    fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
    for family in families:
        subset = [row for row in rows if row["family"] == family]
        ax.scatter(
            [row["rank"] for row in subset],
            [row["DLS"] for row in subset],
            label=family,
            color=color_by_family[family],
            s=45,
            alpha=0.85,
        )
    ax.set_xlabel("Observation Rank")
    ax.set_ylabel("DLS")
    ax.set_title("DLS vs Rank (Exploration)")
    ax.legend(frameon=False, fontsize=8)
    for ext in ("png", "pdf"):
        path = out_dir / f"dls_vs_rank.{ext}"
        fig.savefig(path, dpi=180 if ext == "png" else None)
        files.append(str(path.relative_to(ROOT)))
    plt.close(fig)

    # DLS vs augmentation delta
    fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
    for family in families:
        subset = [row for row in rows if row["family"] == family]
        ax.scatter(
            [row["delta"] for row in subset],
            [row["DLS"] for row in subset],
            label=family,
            color=color_by_family[family],
            s=45,
            alpha=0.85,
        )
    ax.set_xlabel("Minimal Augmentation delta")
    ax.set_ylabel("DLS")
    ax.set_title("DLS vs Augmentation delta (Exploration)")
    ax.legend(frameon=False, fontsize=8)
    for ext in ("png", "pdf"):
        path = out_dir / f"dls_vs_delta.{ext}"
        fig.savefig(path, dpi=180 if ext == "png" else None)
        files.append(str(path.relative_to(ROOT)))
    plt.close(fig)

    # Fiber size histogram (all systems pooled)
    fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
    if all_fiber_sizes:
        bins = np.arange(0.5, max(all_fiber_sizes) + 1.5, 1.0)
        ax.hist(all_fiber_sizes, bins=bins, color="#31688e", alpha=0.85, edgecolor="white")
    ax.set_xlabel("Fiber size")
    ax.set_ylabel("Count")
    ax.set_title("Fiber Size Histogram (All Exploration Systems)")
    for ext in ("png", "pdf"):
        path = out_dir / f"fiber_size_histogram.{ext}"
        fig.savefig(path, dpi=180 if ext == "png" else None)
        files.append(str(path.relative_to(ROOT)))
    plt.close(fig)

    # Mixed vs pure fiber distribution by family
    family_pure = {family: 0 for family in families}
    family_mixed = {family: 0 for family in families}
    for row in rows:
        family = str(row["family"])
        mixed = int(row["mixed_fiber_count"])
        total = int(row["fiber_count"])
        family_mixed[family] += mixed
        family_pure[family] += max(total - mixed, 0)

    fig, ax = plt.subplots(figsize=(8.0, 4.8), constrained_layout=True)
    x = np.arange(len(families))
    pure_values = np.asarray([family_pure[family] for family in families], dtype=float)
    mixed_values = np.asarray([family_mixed[family] for family in families], dtype=float)
    ax.bar(x, pure_values, label="pure fibers", color="#35b779")
    ax.bar(x, mixed_values, bottom=pure_values, label="mixed fibers", color="#440154")
    ax.set_xticks(x)
    ax.set_xticklabels(families, rotation=15, ha="right")
    ax.set_ylabel("Fiber count")
    ax.set_title("Mixed vs Pure Fiber Distribution")
    ax.legend(frameon=False, fontsize=8)
    for ext in ("png", "pdf"):
        path = out_dir / f"mixed_vs_pure_distribution.{ext}"
        fig.savefig(path, dpi=180 if ext == "png" else None)
        files.append(str(path.relative_to(ROOT)))
    plt.close(fig)

    return files


def _write_report(
    *,
    rows: list[dict[str, object]],
    summary: dict[str, object],
    anomalies: list[dict[str, object]],
    report_path: Path,
) -> None:
    family_counts = summary["family_counts"]
    correlation_rows = summary["correlations"]
    strongest_dls = sorted(rows, key=lambda row: float(row["DLS"]), reverse=True)[:5]
    strongest_shift = summary["threshold_events"][:5]

    lines = [
        "# Indistinguishability Exploration",
        "",
        f"Status: **{STATUS_LABEL}**",
        "",
        "This lane adds a finite-family indistinguishability analysis layer to supported OCP/recoverability families.",
        "It is diagnostic only and does not modify theorem status, theorem spine, or promotion decisions.",
        "",
        "## Definitions Used",
        "",
        "- Equivalence relation: `x ~ x'` iff `M(x) = M(x')`.",
        "- Fiber: `Fib(y) = {x in A : M(x)=y}`.",
        "- Mixed fiber: a fiber containing more than one distinct target value.",
        "- Distinguishability Loss Score (DLS): estimated probability that two states with the same record have different targets.",
        "",
        "## Families Covered",
        "",
        "| Family | Systems |",
        "| --- | ---: |",
    ]
    for family, count in family_counts.items():
        lines.append(f"| {family} | {count} |")

    lines.extend(
        [
            "",
            "## Comparison to Existing Metrics",
            "",
            "| Comparison | Pearson correlation |",
            "| --- | ---: |",
        ]
    )
    for name, value in correlation_rows.items():
        formatted = "n/a" if value is None else f"{float(value):.3f}"
        lines.append(f"| {name} | {formatted} |")

    lines.extend(
        [
            "",
            "Interpretation for this pass: DLS is strongly coupled to fiber-collision metrics (`kappa_0`, `Gamma_r`) and only partially aligned with rank and augmentation count.",
            "That behavior is expected for an indistinguishability-based diagnostic and is kept exploratory.",
            "",
            "## Anomaly Cases (Automatic Flags)",
            "",
            f"Flag count: **{len(anomalies)}**",
            "",
            "| System | Type | Severity | Details |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in anomalies[:20]:
        lines.append(
            f"| {row['system_id']} | {row['anomaly_type']} | {row['severity']} | {row['details']} |"
        )
    if len(anomalies) > 20:
        lines.append(f"| ... | ... | ... | {len(anomalies) - 20} additional flags in artifact CSV |")

    lines.extend(
        [
            "",
            "## Threshold Behavior",
            "",
            "The following transitions show the largest DLS drops tied to observation-family changes.",
            "",
            "| Series | From -> To | DLS drop | delta drop |",
            "| --- | --- | ---: | ---: |",
        ]
    )
    if strongest_shift:
        for event in strongest_shift:
            lines.append(
                f"| {event['series_key']} | {event['from_system']} -> {event['to_system']} | "
                f"{event['dls_drop']:.3f} | {event['delta_drop']:.1f} |"
            )
    else:
        lines.append("| none detected | n/a | n/a | n/a |")

    lines.extend(
        [
            "",
            "## Highest-DLS Systems",
            "",
            "| System | Family | Rank | DLS | percent mixed | delta |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in strongest_dls:
        lines.append(
            f"| {row['system_id']} | {row['family']} | {int(row['rank'])} | "
            f"{float(row['DLS']):.3f} | {float(row['percent_mixed']):.1f}% | {float(row['delta']):.1f} |"
        )

    lane_value = str(summary["lane_value_assessment"])
    lines.extend(
        [
            "",
            "## Lane Assessment",
            "",
            f"Assessment: **{lane_value}**",
            "",
            "Current readout: indistinguishability metrics provide clearer failure interpretation and anti-classifier diagnostics on sampled families.",
            "The lane remains exploratory and non-promoted until additional families and stress checks are completed.",
            "",
            "## Artifacts",
            "",
            "- `data/generated/indistinguishability/indistinguishability_metrics.csv`",
            "- `data/generated/indistinguishability/indistinguishability_anomalies.csv`",
            "- `data/generated/indistinguishability/indistinguishability_summary.json`",
            "- `figures/indistinguishability/dls_vs_rank.png`",
            "- `figures/indistinguishability/dls_vs_delta.png`",
            "- `figures/indistinguishability/fiber_size_histogram.png`",
            "- `figures/indistinguishability/mixed_vs_pure_distribution.png`",
            "",
            "> Label reminder: EXPLORATION / NON-PROMOTED.",
        ]
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    evaluated = (
        _restricted_linear_cases()
        + _periodic_modal_cases()
        + _bounded_cfd_cases()
        + _mhd_cases()
    )
    rows = [item[0] for item in evaluated]
    aux = [item[1] for item in evaluated]

    all_fiber_sizes: list[int] = []
    all_mixedness: list[int] = []
    for item in aux:
        all_fiber_sizes.extend(int(value) for value in item["fiber_sizes"])
        all_mixedness.extend(int(value) for value in item["mixedness_values"])

    anomalies = _detect_anomalies(rows)

    threshold_events: list[dict[str, object]] = []
    grouped: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        key = str(row.get("series_key", "")).strip()
        if not key:
            continue
        grouped.setdefault(key, []).append(row)
    for key, group in grouped.items():
        valid = [row for row in group if str(row.get("series_level", "")).strip()]
        if len(valid) < 2:
            continue
        valid.sort(key=lambda item: float(item["series_level"]))
        for first, second in zip(valid[:-1], valid[1:], strict=True):
            threshold_events.append(
                {
                    "series_key": key,
                    "from_system": first["system_id"],
                    "to_system": second["system_id"],
                    "dls_drop": float(first["DLS"]) - float(second["DLS"]),
                    "delta_drop": float(first["delta"]) - float(second["delta"]),
                }
            )
    threshold_events.sort(key=lambda row: float(row["dls_drop"]), reverse=True)

    correlations = {
        "DLS vs rank": pearson_correlation(
            [float(row["DLS"]) for row in rows],
            [float(row["rank"]) for row in rows],
        ),
        "DLS vs kappa_0": pearson_correlation(
            [float(row["DLS"]) for row in rows],
            [float(row["kappa_0"]) for row in rows],
        ),
        "DLS vs Gamma_r": pearson_correlation(
            [float(row["DLS"]) for row in rows],
            [float(row["Gamma_r"]) for row in rows],
        ),
        "DLS vs delta": pearson_correlation(
            [float(row["DLS"]) for row in rows],
            [float(row["delta"]) for row in rows],
        ),
    }

    anomaly_types = sorted({str(item["anomaly_type"]) for item in anomalies})
    high_signal = any(item["anomaly_type"] in {"high_rank_high_dls", "rank_predicts_success_but_dls_high"} for item in anomalies)
    threshold_signal = any(float(item["dls_drop"]) >= 0.25 and float(item["delta_drop"]) >= 1.0 for item in threshold_events)
    if high_signal or threshold_signal:
        lane_value = "adds exploratory predictive signal (non-promoted)"
    elif anomalies:
        lane_value = "adds clearer interpretation only (non-promoted)"
    else:
        lane_value = "redundant on current sampled families"

    family_counts: dict[str, int] = {}
    for row in rows:
        family = str(row["family"])
        family_counts[family] = family_counts.get(family, 0) + 1

    plot_files = _build_plots(rows, all_fiber_sizes, FIG_DIR)
    _write_csv(OUT_DIR / "indistinguishability_metrics.csv", rows)
    _write_csv(OUT_DIR / "indistinguishability_anomalies.csv", anomalies)

    summary = {
        "status_label": STATUS_LABEL,
        "system_count": len(rows),
        "family_counts": family_counts,
        "anomaly_count": len(anomalies),
        "anomaly_types": anomaly_types,
        "correlations": correlations,
        "threshold_events": threshold_events,
        "lane_value_assessment": lane_value,
        "plot_files": plot_files,
        "notes": [
            "Exploration lane only.",
            "No theorem promotion and no theorem-spine edits were applied.",
            "Metrics are finite-family diagnostics, not universal classifiers.",
        ],
    }
    (OUT_DIR / "indistinguishability_summary.json").write_text(json.dumps(summary, indent=2))
    _write_report(rows=rows, summary=summary, anomalies=anomalies, report_path=REPORT_PATH)

    print(f"wrote {OUT_DIR / 'indistinguishability_metrics.csv'}")
    print(f"wrote {OUT_DIR / 'indistinguishability_anomalies.csv'}")
    print(f"wrote {OUT_DIR / 'indistinguishability_summary.json'}")
    print(f"wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()

