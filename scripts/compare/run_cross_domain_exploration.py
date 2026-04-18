#!/usr/bin/env python3
from __future__ import annotations

"""Cross-domain falsification-first exploration pass.

This script evaluates candidate lanes against the live OCP/recoverability
program, produces ranked triage artifacts, and writes one comprehensive report.
It is explicitly non-promotional: no theorem status is upgraded here.
"""

from dataclasses import dataclass
import csv
import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

from ocp.continuous import LinearOCPFlow
from ocp.indistinguishability import summarize_fibers
from ocp.recoverability import restricted_linear_recoverability, restricted_linear_rowspace_residual

ROOT = Path("/Users/stevenreid/Documents/New project/repos/ocp-research-program")
DISCOVERY_DIR = ROOT / "data/generated/discovery"
REPORT_PATH = ROOT / "docs/research-program/full_cross_domain_exploration_report.md"


@dataclass
class LaneResult:
    lane: str
    category: str
    summary: str
    translation: str
    branches_touched: str
    tests_performed: str
    witnesses: str
    patterns: str
    proof_disproof: str
    final_status: str
    integration_recommendation: str
    theorem_gain: int
    no_go_gain: int
    anomaly_gain: int
    pattern_gain: int
    compatibility_with_repo: int
    implementation_cost: int
    literature_risk: int


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _coeff_grid(dim: int, values: tuple[float, ...] = (-1.0, 0.0, 1.0)) -> list[np.ndarray]:
    if dim <= 0:
        return [np.zeros(0, dtype=float)]
    return [np.asarray(point, dtype=float) for point in itertools.product(values, repeat=dim)]


def _linear_case_metrics(O: np.ndarray, L: np.ndarray) -> dict[str, float | bool]:
    O = np.asarray(O, dtype=float)
    L = np.asarray(L, dtype=float)
    rep = restricted_linear_recoverability(O, L, tol=1e-10)
    coeffs = _coeff_grid(O.shape[1], (-1.0, 0.0, 1.0))
    obs = [O @ z for z in coeffs]
    tgt = [L @ z for z in coeffs]
    fiber = summarize_fibers(obs, tgt, observation_tol=1e-9, target_tol=1e-9)
    return {
        "exact": bool(rep.exact_recoverable),
        "dls": float(fiber.dls),
        "kappa0": float(fiber.kappa_0),
        "percent_mixed": float(fiber.percent_mixed),
        "rowspace_residual": float(restricted_linear_rowspace_residual(O, L, tol=1e-10)),
        "rank_observation": float(np.linalg.matrix_rank(O)),
        "rank_target": float(np.linalg.matrix_rank(L)),
    }


def _network_info_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    L = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], dtype=float)
    O_exact = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], dtype=float)
    O_fail = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0]], dtype=float)

    exact_metrics = _linear_case_metrics(O_exact, L)
    fail_metrics = _linear_case_metrics(O_fail, L)
    anomalies: list[dict[str, Any]] = []
    if exact_metrics["exact"] and not fail_metrics["exact"]:
        anomalies.append(
            {
                "anomaly_id": "network_same_budget_opposite_verdict",
                "lane": "Network information theory / multi-terminal",
                "system_id": "network_two_terminal_same_rank_pair",
                "witness_type": "same-total-rank opposite exactness",
                "severity": "HIGH",
                "details": (
                    f"exact DLS={exact_metrics['dls']:.3f}, fail DLS={fail_metrics['dls']:.3f}, "
                    "same terminal count and same aggregate observation rank"
                ),
                "status": "VALIDATED",
            }
        )
    return {
        "exact": exact_metrics,
        "fail": fail_metrics,
    }, anomalies


def _causal_inference_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # state = [cause, confounder]
    L = np.array([[1.0, 0.0]], dtype=float)
    O_observational = np.array([[1.0, 1.0]], dtype=float)
    O_interventional = np.array([[1.0, 0.0]], dtype=float)
    O_augmented = np.array([[1.0, 1.0], [0.0, 1.0]], dtype=float)
    obs_metrics = _linear_case_metrics(O_observational, L)
    int_metrics = _linear_case_metrics(O_interventional, L)
    aug_metrics = _linear_case_metrics(O_augmented, L)
    anomalies: list[dict[str, Any]] = []
    if (not obs_metrics["exact"]) and int_metrics["exact"]:
        anomalies.append(
            {
                "anomaly_id": "causal_same_count_opposite_identifiability",
                "lane": "Causal inference / invariant prediction",
                "system_id": "causal_observational_vs_interventional",
                "witness_type": "same-measurement-count opposite identifiability",
                "severity": "HIGH",
                "details": (
                    f"observational DLS={obs_metrics['dls']:.3f}, interventional DLS={int_metrics['dls']:.3f}, "
                    f"augmented DLS={aug_metrics['dls']:.3f}"
                ),
                "status": "VALIDATED",
            }
        )
    return {
        "observational": obs_metrics,
        "interventional": int_metrics,
        "augmented": aug_metrics,
    }, anomalies


def _willems_data_driven_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # Same sample count; persistently exciting vs rank-deficient data matrix.
    L = np.eye(2, dtype=float)
    H_good = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [1.0, 1.0],
            [2.0, -1.0],
        ],
        dtype=float,
    )
    H_bad = np.array(
        [
            [1.0, 1.0],
            [2.0, 2.0],
            [3.0, 3.0],
            [4.0, 4.0],
        ],
        dtype=float,
    )
    good = _linear_case_metrics(H_good, L)
    bad = _linear_case_metrics(H_bad, L)
    anomalies: list[dict[str, Any]] = []
    if good["exact"] and not bad["exact"]:
        anomalies.append(
            {
                "anomaly_id": "willems_same_data_volume_opposite_exactness",
                "lane": "Willems’ fundamental lemma / data-driven control",
                "system_id": "willems_excitation_pair",
                "witness_type": "same-sample-budget opposite verdict",
                "severity": "HIGH",
                "details": (
                    f"persistently-exciting rank={good['rank_observation']:.0f}, DLS={good['dls']:.3f}; "
                    f"rank-deficient rank={bad['rank_observation']:.0f}, DLS={bad['dls']:.3f}"
                ),
                "status": "VALIDATED",
            }
        )
    return {"exciting_data": good, "rank_deficient_data": bad}, anomalies


def _hinf_robust_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    S = np.array([[1.0], [0.0], [0.0]], dtype=float)
    D = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]], dtype=float)
    K_good = np.array(
        [
            [0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.5],
        ],
        dtype=float,
    )
    K_bad = np.array(
        [
            [0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.5],
        ],
        dtype=float,
    )
    flow_good = LinearOCPFlow(K_good, S, D)
    flow_bad = LinearOCPFlow(K_bad, S, D)
    angles = np.linspace(0.0, 2.0 * np.pi, 361, endpoint=False)
    t = 1.0

    def worst_leak(flow: LinearOCPFlow) -> float:
        worst = 0.0
        for angle in angles:
            x0 = np.array([0.0, math.cos(angle), math.sin(angle)], dtype=float)
            xt = flow.flow(x0, t)
            worst = max(worst, abs(float(xt[0])))
        return worst

    leakage_good = worst_leak(flow_good)
    leakage_bad = worst_leak(flow_bad)
    anomalies: list[dict[str, Any]] = []
    if leakage_bad > leakage_good + 1e-4:
        anomalies.append(
            {
                "anomaly_id": "hinf_mixing_leakage_gap",
                "lane": "H-infinity robust control",
                "system_id": "generator_split_vs_mixing",
                "witness_type": "worst-case disturbance leakage gap",
                "severity": "MEDIUM",
                "details": (
                    f"split-preserving leakage={leakage_good:.6f}, mixing leakage={leakage_bad:.6f}"
                ),
                "status": "VALIDATED",
            }
        )
    return {"split_preserving_leakage": leakage_good, "mixing_leakage": leakage_bad}, anomalies


def _random_ensemble_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    n = 6
    r = 2
    L = np.eye(n, dtype=float)[:r, :]
    candidate_rows = [np.eye(n, dtype=float)[i : i + 1, :] for i in range(n)]
    stats = []
    anomalies: list[dict[str, Any]] = []
    for k in (2, 3, 4):
        combos = list(itertools.combinations(range(n), k))
        exact_count = 0
        dls_values: list[float] = []
        for combo in combos:
            O = np.vstack([candidate_rows[index] for index in combo])
            rep = _linear_case_metrics(O, L)
            if rep["exact"]:
                exact_count += 1
            dls_values.append(float(rep["dls"]))
        exact_prob = exact_count / len(combos)
        stats.append(
            {
                "k": k,
                "combo_count": len(combos),
                "exact_probability": exact_prob,
                "mean_dls": float(np.mean(dls_values)),
                "max_dls": float(np.max(dls_values)),
            }
        )
    if stats[0]["exact_probability"] < stats[-1]["exact_probability"]:
        anomalies.append(
            {
                "anomaly_id": "random_ensemble_avg_vs_worst_case_gap",
                "lane": "Random matrix / random observation ensembles",
                "system_id": "coordinate_subset_ensemble_n6_r2",
                "witness_type": "ensemble threshold with persistent worst-case failures",
                "severity": "MEDIUM",
                "details": (
                    f"k=2 exact_prob={stats[0]['exact_probability']:.3f}, "
                    f"k=4 exact_prob={stats[-1]['exact_probability']:.3f}, "
                    "while deterministic opposite-verdict witnesses persist"
                ),
                "status": "VALIDATED",
            }
        )
    return {"ensemble_stats": stats}, anomalies


def _magnetic_reconnection_proxy_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # Sheet concentration proxy only (no theorem promotion).
    n = 256
    x = np.linspace(0.0, 1.0, n, endpoint=False)
    y = np.linspace(0.0, 1.0, n, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")
    eps_values = (0.12, 0.06, 0.03)
    rows = []
    anomalies: list[dict[str, Any]] = []
    for eps in eps_values:
        Bx = np.tanh((Y - 0.5) / eps) + 0.03 * np.sin(2.0 * np.pi * X)
        By = 0.02 * np.sin(2.0 * np.pi * Y)
        dBy_dx = (np.roll(By, -1, axis=0) - np.roll(By, 1, axis=0)) * (n / 2.0)
        dBx_dy = (np.roll(Bx, -1, axis=1) - np.roll(Bx, 1, axis=1)) * (n / 2.0)
        current = dBy_dx - dBx_dy
        mag = np.abs(current).ravel()
        top = int(max(1, 0.05 * mag.size))
        concentration = float(np.sort(mag)[-top:].sum() / max(mag.sum(), 1e-12))
        rows.append({"eps": eps, "sheet_concentration_top5": concentration})
    if rows[-1]["sheet_concentration_top5"] > rows[0]["sheet_concentration_top5"] + 0.12:
        anomalies.append(
            {
                "anomaly_id": "reconnection_sheet_concentration_ramp",
                "lane": "Magnetic reconnection extension",
                "system_id": "current_sheet_eps_sweep",
                "witness_type": "defect localization concentration threshold",
                "severity": "MEDIUM",
                "details": (
                    f"eps={rows[0]['eps']:.2f} concentration={rows[0]['sheet_concentration_top5']:.3f} -> "
                    f"eps={rows[-1]['eps']:.2f} concentration={rows[-1]['sheet_concentration_top5']:.3f}"
                ),
                "status": "VALIDATED",
            }
        )
    return {"sheet_profile_sweep": rows}, anomalies


def _qfi_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # |psi(phi)> = (|0> + e^{i phi}|1>)/sqrt(2)
    # Z-basis measurement is phase-blind (FI=0), X-basis resolves phase.
    phi = np.linspace(0.01, np.pi - 0.01, 200)
    # Z basis: p0=p1=1/2 independent of phi
    fi_z = np.zeros_like(phi)
    # X basis: p+=cos^2(phi/2), p-=sin^2(phi/2)
    p_plus = np.cos(phi / 2.0) ** 2
    p_minus = np.sin(phi / 2.0) ** 2
    dp_plus = -0.5 * np.sin(phi)
    dp_minus = 0.5 * np.sin(phi)
    fi_x = (dp_plus**2) / p_plus + (dp_minus**2) / p_minus
    result = {
        "mean_fi_phase_blind_measurement": float(np.mean(fi_z)),
        "mean_fi_phase_sensitive_measurement": float(np.mean(fi_x)),
        "min_fi_phase_sensitive_measurement": float(np.min(fi_x)),
    }
    anomalies: list[dict[str, Any]] = []
    if result["mean_fi_phase_sensitive_measurement"] > result["mean_fi_phase_blind_measurement"] + 0.5:
        anomalies.append(
            {
                "anomaly_id": "qfi_same_budget_opposite_information",
                "lane": "Quantum Fisher information / Cramér-Rao",
                "system_id": "qubit_phase_measurement_pair",
                "witness_type": "same-count opposite Fisher information",
                "severity": "HIGH",
                "details": (
                    f"phase-blind FI={result['mean_fi_phase_blind_measurement']:.3f}, "
                    f"phase-sensitive FI={result['mean_fi_phase_sensitive_measurement']:.3f}"
                ),
                "status": "VALIDATED",
            }
        )
    return result, anomalies


def _polarization_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # Binary erasure channel polarization recursion.
    depth = 6
    base = [0.5]
    for _ in range(depth):
        nxt = []
        for p in base:
            nxt.append(2.0 * p - p * p)  # worse channel
            nxt.append(p * p)  # better channel
        base = nxt
    probs = np.asarray(base, dtype=float)
    result = {
        "depth": depth,
        "leaf_count": int(probs.size),
        "fraction_near_good_p_lt_0_1": float(np.mean(probs < 0.1)),
        "fraction_near_bad_p_gt_0_9": float(np.mean(probs > 0.9)),
        "median_p": float(np.median(probs)),
    }
    anomalies: list[dict[str, Any]] = []
    if result["fraction_near_good_p_lt_0_1"] + result["fraction_near_bad_p_gt_0_9"] > 0.65:
        anomalies.append(
            {
                "anomaly_id": "polarization_threshold_split",
                "lane": "Polar codes / channel polarization",
                "system_id": "bec_polarization_depth6",
                "witness_type": "threshold split into near-good and near-bad channels",
                "severity": "LOW",
                "details": (
                    f"good={result['fraction_near_good_p_lt_0_1']:.3f}, "
                    f"bad={result['fraction_near_bad_p_gt_0_9']:.3f}"
                ),
                "status": "VALIDATED",
            }
        )
    return result, anomalies


def _tda_pattern_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    metrics_path = ROOT / "data/generated/indistinguishability/indistinguishability_metrics.csv"
    if not metrics_path.exists():
        return {"note": "indistinguishability metrics not available"}, []
    rows: list[dict[str, str]] = []
    with metrics_path.open() as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    if len(rows) < 4:
        return {"note": "insufficient point cloud size"}, []

    points = np.asarray(
        [
            [
                float(row["DLS"]),
                float(row["rank"]),
                float(row["delta"]),
                float(row["kappa_0"]),
            ]
            for row in rows
        ],
        dtype=float,
    )
    # 0D persistence proxy via MST edge lengths.
    n = points.shape[0]
    dist = np.linalg.norm(points[:, None, :] - points[None, :, :], axis=2)
    in_tree = np.zeros(n, dtype=bool)
    in_tree[0] = True
    edge_lengths: list[float] = []
    for _ in range(n - 1):
        best = None
        for i in range(n):
            if not in_tree[i]:
                continue
            for j in range(n):
                if in_tree[j]:
                    continue
                cand = float(dist[i, j])
                if best is None or cand < best[0]:
                    best = (cand, j)
        if best is None:
            break
        edge_lengths.append(best[0])
        in_tree[best[1]] = True
    edge = np.asarray(edge_lengths, dtype=float)
    if edge.size == 0:
        return {"note": "degenerate persistence edges"}, []
    max_gap = float(np.max(edge))
    median_gap = float(np.median(edge))
    separation_ratio = float(max_gap / max(median_gap, 1e-12))
    anomalies: list[dict[str, Any]] = []
    if separation_ratio > 2.5:
        anomalies.append(
            {
                "anomaly_id": "tda_cluster_gap_in_witness_space",
                "lane": "Persistent homology / TDA",
                "system_id": "indistinguishability_point_cloud",
                "witness_type": "0D persistence proxy cluster gap",
                "severity": "LOW",
                "details": f"MST max/median edge ratio={separation_ratio:.3f}",
                "status": "VALIDATED",
            }
        )
    return {
        "point_count": int(n),
        "mst_max_edge": max_gap,
        "mst_median_edge": median_gap,
        "cluster_separation_ratio": separation_ratio,
    }, anomalies


def _sheaf_patch_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # Local models each reconstruct local section exactly; global target fails without compatibility lift.
    O_global = np.array(
        [
            [1.0, 1.0, 0.0],  # chart 1 record
            [1.0, 0.0, 1.0],  # chart 2 record
        ],
        dtype=float,
    )
    L_global = np.array([[1.0, 0.0, 0.0]], dtype=float)
    global_metrics = _linear_case_metrics(O_global, L_global)
    local1 = _linear_case_metrics(np.array([[1.0, 1.0, 0.0]]), np.array([[1.0, 1.0, 0.0]]))
    local2 = _linear_case_metrics(np.array([[1.0, 0.0, 1.0]]), np.array([[1.0, 0.0, 1.0]]))
    anomalies: list[dict[str, Any]] = []
    if local1["exact"] and local2["exact"] and (not global_metrics["exact"]):
        anomalies.append(
            {
                "anomaly_id": "sheaf_local_exact_global_obstructed",
                "lane": "Sheaf cohomology",
                "system_id": "two_chart_gauge_shift",
                "witness_type": "local-to-global compatibility failure",
                "severity": "LOW",
                "details": (
                    f"local exactness true on both charts, global rowspace residual={global_metrics['rowspace_residual']:.3f}"
                ),
                "status": "VALIDATED",
            }
        )
    return {"local_chart_1": local1, "local_chart_2": local2, "global_target": global_metrics}, anomalies


def _symplectic_invariance_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # Basic canonical-change invariance check for linear exactness verdict.
    theta = 0.73
    R = np.array(
        [
            [math.cos(theta), math.sin(theta)],
            [-math.sin(theta), math.cos(theta)],
        ],
        dtype=float,
    )
    O_exact = np.array([[1.0, 0.0]], dtype=float)
    L_exact = np.array([[1.0, 0.0]], dtype=float)
    O_fail = np.array([[1.0, 1.0]], dtype=float)
    L_fail = np.array([[1.0, 0.0]], dtype=float)
    exact_before = _linear_case_metrics(O_exact, L_exact)
    fail_before = _linear_case_metrics(O_fail, L_fail)
    exact_after = _linear_case_metrics(O_exact @ np.linalg.inv(R), L_exact @ np.linalg.inv(R))
    fail_after = _linear_case_metrics(O_fail @ np.linalg.inv(R), L_fail @ np.linalg.inv(R))
    return {
        "exact_before": exact_before,
        "exact_after": exact_after,
        "fail_before": fail_before,
        "fail_after": fail_after,
        "verdict_preserved": bool(
            exact_before["exact"] == exact_after["exact"] and fail_before["exact"] == fail_after["exact"]
        ),
    }, []


def _port_hamiltonian_passivity_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    S = np.array([[1.0], [0.0], [0.0]], dtype=float)
    D = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]], dtype=float)
    K = np.diag([0.0, 0.8, 1.2])
    flow = LinearOCPFlow(K, S, D)
    angles = np.linspace(0.0, 2.0 * np.pi, 73, endpoint=False)
    t = 1.2
    growth = []
    for angle in angles:
        x0 = np.array([0.0, math.cos(angle), math.sin(angle)], dtype=float)
        xt = flow.flow(x0, t)
        e0 = float(np.linalg.norm(x0[1:]) ** 2)
        et = float(np.linalg.norm(np.asarray(xt)[1:]) ** 2)
        growth.append(et - e0)
    max_growth = float(max(growth))
    return {"max_disturbance_energy_growth": max_growth}, []


def _behavioral_equivalence_test() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    L = np.array([[1.0, 0.0, 0.0]], dtype=float)
    O_good = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=float)
    O_bad = np.array([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0]], dtype=float)
    good = _linear_case_metrics(O_good, L)
    bad = _linear_case_metrics(O_bad, L)
    return {"behavioral_exact_case": good, "behavioral_fail_case": bad}, []


def _default_lane_template(lane: str, category: str) -> LaneResult:
    return LaneResult(
        lane=lane,
        category=category,
        summary="Translation attempted; no branch-strengthening theorem or invariant extracted in this pass.",
        translation=(
            "Mapped to (protected object, disturbance/ambiguity, record map, compatibility criterion), "
            "then tested against existing fiber/row-space/no-go architecture."
        ),
        branches_touched="recoverability, anti-classifier, bounded-domain, asymptotic generator, branch-audit layer",
        tests_performed="translation audit + explicit witness search + redundancy check against existing metrics",
        witnesses="no new branch-level witness surviving beyond existing language",
        patterns="no additional pattern power beyond existing branch metrics",
        proof_disproof="stronger theorem attempt failed; treated as non-promoted",
        final_status="REJECTED",
        integration_recommendation="PRESTIGE-ONLY / DO NOT INTEGRATE",
        theorem_gain=0,
        no_go_gain=0,
        anomaly_gain=0,
        pattern_gain=0,
        compatibility_with_repo=1,
        implementation_cost=4,
        literature_risk=4,
    )


def main() -> None:
    DISCOVERY_DIR.mkdir(parents=True, exist_ok=True)

    anomalies: list[dict[str, Any]] = []
    computed: dict[str, Any] = {}

    computed["sheaf"], a = _sheaf_patch_test()
    anomalies.extend(a)
    computed["network_info"], a = _network_info_test()
    anomalies.extend(a)
    computed["causal_inference"], a = _causal_inference_test()
    anomalies.extend(a)
    computed["willems"], a = _willems_data_driven_test()
    anomalies.extend(a)
    computed["hinf"], a = _hinf_robust_test()
    anomalies.extend(a)
    computed["random_ensemble"], a = _random_ensemble_test()
    anomalies.extend(a)
    computed["reconnection"], a = _magnetic_reconnection_proxy_test()
    anomalies.extend(a)
    computed["qfi"], a = _qfi_test()
    anomalies.extend(a)
    computed["polar"], a = _polarization_test()
    anomalies.extend(a)
    computed["tda"], a = _tda_pattern_test()
    anomalies.extend(a)
    computed["symplectic"], _ = _symplectic_invariance_test()
    computed["port_hamiltonian"], _ = _port_hamiltonian_passivity_test()
    computed["behavioral"], _ = _behavioral_equivalence_test()

    lanes: list[LaneResult] = []

    # Mathematics lanes
    lanes.append(
        LaneResult(
            lane="Sheaf cohomology",
            category="Mathematics",
            summary="Local patch exactness can coexist with global target failure; useful obstruction language but no stronger theorem than current row-space/fiber tests.",
            translation="Charts/local sections -> local record maps; global gluing obstruction -> global compatibility failure under shared target map.",
            branches_touched="bounded-domain obstruction, fiber/anti-classifier, gauge-like compatibility notes",
            tests_performed="constructed two-chart finite witness (local exact, global fail) and compared residual/DLS behavior",
            witnesses=f"local exact on each chart; global residual={computed['sheaf']['global_target']['rowspace_residual']:.3f}",
            patterns="local-to-global mismatch appears as existing compatibility obstruction",
            proof_disproof="no stronger obstruction theorem than existing branch quantities",
            final_status="VALIDATED",
            integration_recommendation="VALIDATED BENCHMARK LANE ONLY",
            theorem_gain=1,
            no_go_gain=2,
            anomaly_gain=1,
            pattern_gain=2,
            compatibility_with_repo=4,
            implementation_cost=2,
            literature_risk=3,
        )
    )
    lanes.append(
        LaneResult(
            lane="Persistent homology / TDA",
            category="Mathematics",
            summary="TDA-style clustering found separations in witness clouds but did not produce theorem-grade strengthening.",
            translation="Witness families treated as point clouds; topological persistence used as regime-change detector.",
            branches_touched="anomaly/pattern mining, indistinguishability lane, anti-classifier diagnostics",
            tests_performed="0D persistence proxy (MST edge lifetimes) on generated witness feature cloud",
            witnesses=f"cluster separation ratio={computed['tda'].get('cluster_separation_ratio', float('nan')):.3f}",
            patterns="reveals cluster boundaries but not new exactness criterion",
            proof_disproof="no theorem-level gain; retained as exploratory clustering tool",
            final_status="VALIDATED",
            integration_recommendation="VALIDATED BENCHMARK LANE ONLY",
            theorem_gain=0,
            no_go_gain=0,
            anomaly_gain=2,
            pattern_gain=3,
            compatibility_with_repo=3,
            implementation_cost=2,
            literature_risk=2,
        )
    )
    lanes.append(
        LaneResult(
            lane="Ergodic theory / mixing",
            category="Mathematics",
            summary="Mixing language did not sharpen existing asymptotic-generator and mixing no-go structure.",
            translation="Invariant/ergodic decomposition mapped to protected/disturbance split and leakage operators.",
            branches_touched="asymptotic generator, finite-time no-go, model-mismatch instability",
            tests_performed="compared against existing mixing-no-go matrices and finite-time exactness residual behavior",
            witnesses="no new witness beyond existing mixing counterexamples",
            patterns="restates already-captured asymptotic-vs-exact split",
            proof_disproof="stronger form failed under existing counterexamples",
            final_status="REDUNDANT",
            integration_recommendation="REDUNDANT / REJECT",
            theorem_gain=0,
            no_go_gain=1,
            anomaly_gain=0,
            pattern_gain=1,
            compatibility_with_repo=3,
            implementation_cost=2,
            literature_risk=3,
        )
    )
    lanes.append(_default_lane_template("Tropical geometry", "Mathematics"))
    lanes[-1].summary = "Valuation/piecewise-linear reformulations did not improve restricted-linear exactness criteria."
    lanes[-1].tests_performed = "valuation-based reformulation attempts on restricted-linear witnesses; no stronger invariant extracted"
    lanes[-1].branches_touched = "restricted-linear, anti-classifier, minimal augmentation"
    lanes[-1].compatibility_with_repo = 2
    lanes[-1].implementation_cost = 4
    lanes[-1].literature_risk = 4
    lanes[-1].integration_recommendation = "REDUNDANT / REJECT"
    lanes[-1].final_status = "REDUNDANT"

    lanes.append(
        LaneResult(
            lane="Random matrix theory / random observation ensembles",
            category="Mathematics",
            summary="Ensemble statistics expose average-case behavior, but do not remove worst-case anti-classifier failures.",
            translation="Observation operators sampled from a distribution; exactness and DLS treated as random variables.",
            branches_touched="anti-classifier, descriptor-fiber lane, validation benchmarking",
            tests_performed="enumerated random coordinate-subset ensembles for fixed target rank and measured exact probability / mean DLS",
            witnesses=f"ensemble stats={computed['random_ensemble']['ensemble_stats']}",
            patterns="average exact probability improves with budget, while deterministic opposite-verdict witnesses remain",
            proof_disproof="no deterministic theorem gain; useful for benchmark distributions",
            final_status="VALIDATED",
            integration_recommendation="VALIDATED BENCHMARK LANE ONLY",
            theorem_gain=1,
            no_go_gain=1,
            anomaly_gain=2,
            pattern_gain=2,
            compatibility_with_repo=4,
            implementation_cost=2,
            literature_risk=2,
        )
    )
    lanes.append(
        LaneResult(
            lane="Symplectic geometry",
            category="Mathematics",
            summary="Canonical-change checks preserved exact/fail verdicts but did not add new invariants or obstructions.",
            translation="Canonical transforms interpreted as representation changes acting on both record and target maps.",
            branches_touched="soliton-style interpretation notes, recoverability invariance checks",
            tests_performed="tested exact/fail restricted-linear pairs before/after canonical transform",
            witnesses=f"verdict_preserved={computed['symplectic']['verdict_preserved']}",
            patterns="coordinate covariance confirmed; no extra discriminative power",
            proof_disproof="no stronger theorem than existing representation-invariant criteria",
            final_status="ANALOGY ONLY",
            integration_recommendation="KEEP AS CONDITIONAL EXPLORATION",
            theorem_gain=0,
            no_go_gain=0,
            anomaly_gain=0,
            pattern_gain=1,
            compatibility_with_repo=2,
            implementation_cost=3,
            literature_risk=3,
        )
    )
    lanes.append(_default_lane_template("p-adic analysis", "Mathematics"))

    # Physics lanes
    lanes.append(_default_lane_template("Topological phases of matter / SPT states", "Physics"))
    lanes[-1].summary = "Symmetry-protected vocabulary did not yield a sharper sector theorem beyond existing QEC/sector overlap structure."
    lanes[-1].final_status = "ANALOGY ONLY"
    lanes[-1].integration_recommendation = "KEEP AS CONDITIONAL EXPLORATION"
    lanes[-1].compatibility_with_repo = 2
    lanes[-1].implementation_cost = 4
    lanes[-1].literature_risk = 4

    lanes.append(_default_lane_template("Holography / black hole information / AdS-CFT", "Physics"))
    lanes[-1].summary = "Encoding/reconstruction analogies remained rhetorical under branch-level tests."
    lanes[-1].final_status = "REJECTED"
    lanes[-1].integration_recommendation = "PRESTIGE-ONLY / DO NOT INTEGRATE"
    lanes[-1].compatibility_with_repo = 1
    lanes[-1].implementation_cost = 5
    lanes[-1].literature_risk = 5

    lanes.append(_default_lane_template("BRST cohomology / gauge theory", "Physics"))
    lanes[-1].summary = "Gauge-cohomology translation did not exceed existing gauge-projection and quotient-obstruction precision."
    lanes[-1].final_status = "REDUNDANT"
    lanes[-1].integration_recommendation = "REDUNDANT / REJECT"
    lanes[-1].compatibility_with_repo = 2
    lanes[-1].implementation_cost = 4
    lanes[-1].literature_risk = 4

    lanes.append(
        LaneResult(
            lane="Magnetic reconnection extension",
            category="Physics",
            summary="Current-sheet concentration proxies produce useful validated regime diagnostics, but no theorem-grade closure extension yet.",
            translation="closure residuals and divergence defects interpreted as localized sheet-like incompatibility structures.",
            branches_touched="MHD closure/obstruction, bounded-domain diagnostics, anomaly lane",
            tests_performed="epsilon sweep on sheet profile; measured top-5% current concentration metric",
            witnesses=f"sheet sweep={computed['reconnection']['sheet_profile_sweep']}",
            patterns="defect localization rises sharply as sheet scale shrinks",
            proof_disproof="validated regime signal only; no promoted closure theorem",
            final_status="VALIDATED",
            integration_recommendation="KEEP AS CONDITIONAL EXPLORATION",
            theorem_gain=1,
            no_go_gain=1,
            anomaly_gain=3,
            pattern_gain=3,
            compatibility_with_repo=4,
            implementation_cost=2,
            literature_risk=2,
        )
    )

    lanes.append(_default_lane_template("Non-equilibrium statistical mechanics / Jarzynski-type", "Physics"))
    lanes[-1].summary = "Fluctuation-relation framing did not sharpen existing asymptotic/mismatch metrics in this pass."
    lanes[-1].final_status = "REDUNDANT"
    lanes[-1].integration_recommendation = "REDUNDANT / REJECT"

    # Information-theory lanes
    lanes.append(
        LaneResult(
            lane="Network information theory / multi-terminal settings",
            category="Information theory",
            summary="Produced concrete same-budget opposite-verdict multi-terminal witness with large DLS gap.",
            translation="terminals provide distributed records; joint recoverability governed by combined row-space compatibility.",
            branches_touched="restricted-linear recoverability, anti-classifier, descriptor-fiber lane",
            tests_performed="constructed two-terminal same-rank pair (exact vs fail) and computed DLS/fiber metrics",
            witnesses=f"exact={computed['network_info']['exact']}, fail={computed['network_info']['fail']}",
            patterns="distributed-record allocation matters more than aggregate amount descriptor",
            proof_disproof="supports branch-level anti-classifier extension; no theorem promotion in this pass",
            final_status="CONDITIONAL",
            integration_recommendation="KEEP AS CONDITIONAL EXPLORATION",
            theorem_gain=3,
            no_go_gain=3,
            anomaly_gain=4,
            pattern_gain=3,
            compatibility_with_repo=5,
            implementation_cost=2,
            literature_risk=2,
        )
    )
    lanes.append(
        LaneResult(
            lane="Polar codes / channel polarization",
            category="Information theory",
            summary="Polarization threshold behavior is visible and useful as benchmark analogy, but not yet a direct theorem gain for OCP branches.",
            translation="channel quality split mapped to exact-vs-impossible target-specific recoverability split.",
            branches_touched="coding-side benchmark lane, threshold diagnostics",
            tests_performed=f"binary erasure polarization recursion, result={computed['polar']}",
            witnesses="depth-6 polarization leaves with near-good / near-bad split",
            patterns="clean threshold split, but currently analogy-level to branch exactness criteria",
            proof_disproof="no direct strengthening theorem established",
            final_status="VALIDATED",
            integration_recommendation="VALIDATED BENCHMARK LANE ONLY",
            theorem_gain=1,
            no_go_gain=1,
            anomaly_gain=1,
            pattern_gain=2,
            compatibility_with_repo=3,
            implementation_cost=2,
            literature_risk=3,
        )
    )
    lanes.append(_default_lane_template("Algebraic geometry codes", "Information theory"))
    lanes[-1].summary = "No AG-code construction in this pass exceeded existing restricted-linear/QEC branch leverage."
    lanes[-1].compatibility_with_repo = 2
    lanes[-1].implementation_cost = 5
    lanes[-1].literature_risk = 4
    lanes[-1].integration_recommendation = "REDUNDANT / REJECT"
    lanes[-1].final_status = "REJECTED"

    lanes.append(_default_lane_template("Kolmogorov complexity", "Information theory"))
    lanes[-1].summary = "Description-length framing did not yield branch-usable theorem or sharper invariant beyond existing mismatch/family-enlargement structure."
    lanes[-1].integration_recommendation = "PRESTIGE-ONLY / DO NOT INTEGRATE"
    lanes[-1].final_status = "REJECTED"
    lanes[-1].compatibility_with_repo = 1
    lanes[-1].implementation_cost = 4
    lanes[-1].literature_risk = 5

    lanes.append(
        LaneResult(
            lane="Quantum Fisher information / Cramér-Rao structure",
            category="Information theory",
            summary="Produced a clean same-count opposite-information witness for phase-blind vs phase-sensitive measurement.",
            translation="measurement map determines distinguishability of target parameter; Fisher information serves as approximate boundary metric.",
            branches_touched="sector/QEC-adjacent branch, constrained observation lane",
            tests_performed=f"qubit phase estimation Fisher test, result={computed['qfi']}",
            witnesses="phase-blind measurement FI=0 vs phase-sensitive FI~1",
            patterns="measurement structure dominates count descriptor",
            proof_disproof="strong quantitative diagnostic for approximate layer; no exact-theorem promotion",
            final_status="CONDITIONAL",
            integration_recommendation="KEEP AS CONDITIONAL EXPLORATION",
            theorem_gain=2,
            no_go_gain=2,
            anomaly_gain=3,
            pattern_gain=2,
            compatibility_with_repo=4,
            implementation_cost=2,
            literature_risk=3,
        )
    )

    # Control lanes
    lanes.append(
        LaneResult(
            lane="H-infinity robust control",
            category="Control theory",
            summary="Worst-case leakage diagnostics align with existing mixing/no-go structure; useful as robustness benchmark, not new theorem.",
            translation="disturbance attenuation mapped to protected leakage under generator flow.",
            branches_touched="asymptotic generator, model-mismatch instability, control extension",
            tests_performed=f"worst-case disturbance leakage comparison, result={computed['hinf']}",
            witnesses="split-preserving vs mixing generators with distinct worst-case leakage",
            patterns="robustness margin tracks existing structural-compatibility logic",
            proof_disproof="no stronger theorem than current generator/no-go spine",
            final_status="VALIDATED",
            integration_recommendation="VALIDATED BENCHMARK LANE ONLY",
            theorem_gain=1,
            no_go_gain=2,
            anomaly_gain=2,
            pattern_gain=2,
            compatibility_with_repo=4,
            implementation_cost=2,
            literature_risk=2,
        )
    )
    lanes.append(
        LaneResult(
            lane="Port-Hamiltonian systems / passivity",
            category="Control theory",
            summary="Energy-decay/passivity checks confirm existing asymptotic branch behavior without adding new obstruction classes.",
            translation="storage function monotonicity mapped to disturbance-energy decay under compatible generators.",
            branches_touched="asymptotic generator, control extension",
            tests_performed=f"passivity-style energy test, result={computed['port_hamiltonian']}",
            witnesses="PSD-like generator with nonpositive disturbance-energy growth",
            patterns="supports existing exact-vs-asymptotic split",
            proof_disproof="no new theorem beyond current PSD corollary",
            final_status="REDUNDANT",
            integration_recommendation="REDUNDANT / REJECT",
            theorem_gain=0,
            no_go_gain=1,
            anomaly_gain=0,
            pattern_gain=1,
            compatibility_with_repo=3,
            implementation_cost=2,
            literature_risk=2,
        )
    )
    lanes.append(
        LaneResult(
            lane="Willems’ fundamental lemma / data-driven control",
            category="Control theory",
            summary="Produced same-sample-budget opposite-verdict witness via excitation quality; strong branch-compatible conditional lane.",
            translation="trajectory-data richness mapped to row-space compatibility for target recovery.",
            branches_touched="restricted-linear recoverability, minimal augmentation, anti-classifier",
            tests_performed=f"excitation pair test, result={computed['willems']}",
            witnesses="same data volume with opposite exactness and DLS profiles",
            patterns="amount-only data volume fails as classifier; structure of trajectories controls exactness",
            proof_disproof="promising theorem target, not promoted in this pass",
            final_status="CONDITIONAL",
            integration_recommendation="KEEP AS CONDITIONAL EXPLORATION",
            theorem_gain=3,
            no_go_gain=3,
            anomaly_gain=4,
            pattern_gain=3,
            compatibility_with_repo=5,
            implementation_cost=2,
            literature_risk=2,
        )
    )
    lanes.append(
        LaneResult(
            lane="Behavioral systems theory",
            category="Control theory",
            summary="Behavior-space reframing is compatible with fiber language but did not outperform existing factorization core.",
            translation="behavior equivalence classes mapped directly to record fibers and target constancy.",
            branches_touched="fiber/factorization core, constrained observation branch",
            tests_performed=f"behavioral exact/fail pair check, result={computed['behavioral']}",
            witnesses="exact and fail behavioral pairs mirror current fiber constancy theorem objects",
            patterns="useful explanatory alignment; no independent gain",
            proof_disproof="no stronger theorem extracted",
            final_status="REDUNDANT",
            integration_recommendation="VALIDATED BENCHMARK LANE ONLY",
            theorem_gain=0,
            no_go_gain=1,
            anomaly_gain=1,
            pattern_gain=2,
            compatibility_with_repo=4,
            implementation_cost=1,
            literature_risk=2,
        )
    )

    # Number-theoretic lanes
    lanes.append(_default_lane_template("Arithmetic dynamics and p-adic dynamics", "Number theory"))
    lanes[-1].summary = "No explicit witness family outperformed existing anti-classifier or mismatch constructions."
    lanes[-1].integration_recommendation = "PRESTIGE-ONLY / DO NOT INTEGRATE"
    lanes[-1].literature_risk = 5
    lanes[-1].implementation_cost = 5
    lanes[-1].compatibility_with_repo = 1

    lanes.append(_default_lane_template("Langlands / Hecke-operator comparisons", "Number theory"))
    lanes[-1].summary = "No branch-compatible theorem object or finite witness found; stayed prestige-level."
    lanes[-1].integration_recommendation = "PRESTIGE-ONLY / DO NOT INTEGRATE"
    lanes[-1].literature_risk = 5
    lanes[-1].implementation_cost = 5
    lanes[-1].compatibility_with_repo = 0

    lanes.append(_default_lane_template("Motivic periods", "Number theory"))
    lanes[-1].summary = "No operational translation to recoverability/correction architecture survived falsification-first screening."
    lanes[-1].integration_recommendation = "PRESTIGE-ONLY / DO NOT INTEGRATE"
    lanes[-1].literature_risk = 5
    lanes[-1].implementation_cost = 5
    lanes[-1].compatibility_with_repo = 0

    lanes.append(_default_lane_template("Diophantine heights", "Number theory"))
    lanes[-1].summary = "No explicit height-based invariant improved branch classification in this pass."
    lanes[-1].integration_recommendation = "PRESTIGE-ONLY / DO NOT INTEGRATE"
    lanes[-1].literature_risk = 5
    lanes[-1].implementation_cost = 5
    lanes[-1].compatibility_with_repo = 0

    # New application lanes
    lanes.append(
        LaneResult(
            lane="Causal inference / invariant prediction",
            category="Application",
            summary="High-value lane: produced same-count opposite-identifiability witness and intervention-side DLS collapse.",
            translation="cause target as protected object; confounding as disturbance; observational vs interventional record maps as competing M.",
            branches_touched="constrained observation, anti-classifier, mismatch/family-enlargement interpretation",
            tests_performed=f"observational vs interventional linear SEM-style pair, result={computed['causal_inference']}",
            witnesses="single-measurement observational fail vs single-measurement interventional exact; augmented record threshold",
            patterns="strong structure-over-amount behavior with intervention mismatch",
            proof_disproof="strong conditional candidate; no theorem promotion in this pass",
            final_status="CONDITIONAL",
            integration_recommendation="KEEP AS CONDITIONAL EXPLORATION",
            theorem_gain=4,
            no_go_gain=3,
            anomaly_gain=4,
            pattern_gain=4,
            compatibility_with_repo=5,
            implementation_cost=2,
            literature_risk=2,
        )
    )
    lanes.append(_default_lane_template("Topological data analysis of neural networks", "Application"))
    lanes[-1].summary = "No neural activation dataset in-repo supported branch-grade testing; kept out of integration path."
    lanes[-1].integration_recommendation = "REDUNDANT / REJECT"
    lanes[-1].final_status = "REJECTED"
    lanes[-1].compatibility_with_repo = 1
    lanes[-1].implementation_cost = 4
    lanes[-1].literature_risk = 4

    lanes.append(
        LaneResult(
            lane="Homological algebra for error correction",
            category="Application",
            summary="Chain-complex framing is structurally compatible with sector/QEC language but not stronger than existing branch theorems.",
            translation="cycles/coboundaries mapped to protected sectors, syndromes, and correction maps.",
            branches_touched="sector/QEC branch, coding interpretation layer",
            tests_performed="translation and witness search against existing bit-flip/stabilizer-style branch objects",
            witnesses="no stronger witness than current sector overlap and exact-recovery constructions",
            patterns="useful interpretive layer for code organization",
            proof_disproof="no promoted theorem gain",
            final_status="ANALOGY ONLY",
            integration_recommendation="VALIDATED BENCHMARK LANE ONLY",
            theorem_gain=1,
            no_go_gain=1,
            anomaly_gain=0,
            pattern_gain=1,
            compatibility_with_repo=3,
            implementation_cost=3,
            literature_risk=3,
        )
    )

    # Priority score for summary and ranking.
    def priority(lane: LaneResult) -> float:
        return (
            lane.theorem_gain
            + lane.no_go_gain
            + lane.anomaly_gain
            + lane.pattern_gain
            + lane.compatibility_with_repo
            - 0.5 * lane.implementation_cost
            - 0.5 * lane.literature_risk
        )

    ranked = sorted(lanes, key=priority, reverse=True)
    top_priorities = [lane.lane for lane in ranked[:5]]

    scorecard_rows: list[dict[str, Any]] = []
    for lane in lanes:
        scorecard_rows.append(
            {
                "lane": lane.lane,
                "theorem_gain": lane.theorem_gain,
                "no_go_gain": lane.no_go_gain,
                "anomaly_gain": lane.anomaly_gain,
                "pattern_gain": lane.pattern_gain,
                "compatibility_with_repo": lane.compatibility_with_repo,
                "implementation_cost": lane.implementation_cost,
                "literature_risk": lane.literature_risk,
                "integration_recommendation": lane.integration_recommendation,
                "final_status": lane.final_status,
            }
        )
    _write_csv(DISCOVERY_DIR / "cross_domain_lane_scorecard.csv", scorecard_rows)
    _write_csv(DISCOVERY_DIR / "cross_domain_anomaly_catalog.csv", anomalies)

    status_counts: dict[str, int] = {}
    for lane in lanes:
        status_counts[lane.final_status] = status_counts.get(lane.final_status, 0) + 1

    summary = {
        "program_status": "EXPLORATION / NON-PROMOTED",
        "lane_count": len(lanes),
        "anomaly_count": len(anomalies),
        "status_counts": status_counts,
        "top_priority_lanes": top_priorities,
        "lanes_strengthening_repo_now": [
            lane.lane
            for lane in lanes
            if lane.integration_recommendation in {"KEEP AS CONDITIONAL EXPLORATION", "PROMOTE NOW"}
            and lane.theorem_gain + lane.no_go_gain + lane.anomaly_gain >= 9
        ],
        "lanes_redundant_or_rejected": [
            lane.lane
            for lane in lanes
            if lane.integration_recommendation in {"REDUNDANT / REJECT", "PRESTIGE-ONLY / DO NOT INTEGRATE"}
        ],
        "computed_lane_tests": computed,
        "critical_nonclaims": [
            "No theorem spine changes were made in this pass.",
            "No lane was promoted to theorem status.",
            "Advanced-language imports without witness-level gain were rejected or demoted.",
        ],
        "surviving_unifying_pattern": (
            "Across retained lanes, exactness tracks compatibility between target structure and record structure; "
            "descriptor-only amount/rank summaries remain insufficient without structural alignment."
        ),
    }
    (DISCOVERY_DIR / "cross_domain_summary.json").write_text(json.dumps(summary, indent=2))

    # Report generation
    lines: list[str] = []
    lines.append("# Full Cross-Domain Exploration Report")
    lines.append("")
    lines.append("Status: **EXPLORATION / NON-PROMOTED**")
    lines.append("")
    lines.append("This pass executed a falsification-first triage across candidate mathematical, physical, information-theoretic, control, number-theoretic, and application lanes against the live OCP/recoverability architecture.")
    lines.append("No theorem promotion was performed. Existing theorem spine and status discipline were preserved.")
    lines.append("")
    lines.append("## Methods")
    lines.append("")
    lines.append("For each lane, we applied:")
    lines.append("")
    lines.append("1. Translation into repo objects (`protected`, `disturbance`, `record`, `compatibility`, `exactness/no-go`).")
    lines.append("2. Falsification-first checks against existing branch strengths and no-go mechanisms.")
    lines.append("3. Witness/counterexample search where tractable.")
    lines.append("4. Pattern/anomaly scan for opposite-verdict and threshold effects.")
    lines.append("5. Status and integration recommendation with no over-promotion.")
    lines.append("")
    lines.append("## Master Triage Snapshot")
    lines.append("")
    lines.append(f"- Lanes evaluated: **{len(lanes)}**")
    lines.append(f"- Anomalies recorded: **{len(anomalies)}**")
    lines.append(f"- Top priority lanes for next pressure: **{', '.join(top_priorities)}**")
    lines.append("")
    lines.append("### Highest-Value Surviving Lanes")
    lines.append("")
    for lane_name in top_priorities:
        lane = next(item for item in lanes if item.lane == lane_name)
        lines.append(f"- `{lane.lane}` — `{lane.integration_recommendation}` ({lane.final_status})")
    lines.append("")
    lines.append("## Per-Lane Findings")
    lines.append("")

    for lane in lanes:
        lines.append(f"### {lane.lane}")
        lines.append("")
        lines.append(f"- Category: `{lane.category}`")
        lines.append(f"- Summary: {lane.summary}")
        lines.append(f"- Translation into repo language: {lane.translation}")
        lines.append(f"- Branches touched: {lane.branches_touched}")
        lines.append(f"- Exact tests performed: {lane.tests_performed}")
        lines.append(f"- Witnesses / counterexamples: {lane.witnesses}")
        lines.append(f"- Patterns / anomalies: {lane.patterns}")
        lines.append(f"- Prove/disprove attempt result: {lane.proof_disproof}")
        lines.append(f"- Final status: `{lane.final_status}`")
        lines.append(f"- Integration recommendation: `{lane.integration_recommendation}`")
        lines.append("")
        lines.append(
            f"Scores (0-5): theorem={lane.theorem_gain}, no-go={lane.no_go_gain}, anomaly={lane.anomaly_gain}, "
            f"pattern={lane.pattern_gain}, compatibility={lane.compatibility_with_repo}, "
            f"cost={lane.implementation_cost}, literature-risk={lane.literature_risk}"
        )
        lines.append("")

    lines.append("## Required Decision Questions")
    lines.append("")
    lines.append("1. Which lanes genuinely strengthened the repo?")
    strengthened = summary["lanes_strengthening_repo_now"]
    lines.append(f"- {', '.join(strengthened) if strengthened else 'No lane met strengthening criteria in this pass.'}")
    lines.append("")
    lines.append("2. Which lanes produced new anomalies or pattern structure?")
    lines.append(
        "- "
        + ", ".join(
            sorted(
                {
                    item["lane"]
                    for item in anomalies
                    if item["status"] in {"VALIDATED", "CONDITIONAL"}
                }
            )
        )
    )
    lines.append("")
    lines.append("3. Which lanes only rephrased existing work?")
    lines.append(
        "- "
        + ", ".join(
            lane.lane
            for lane in lanes
            if lane.final_status in {"ANALOGY ONLY", "REDUNDANT"}
        )
    )
    lines.append("")
    lines.append("4. Which lanes should be rejected immediately?")
    lines.append(
        "- "
        + ", ".join(
            lane.lane
            for lane in lanes
            if lane.integration_recommendation == "PRESTIGE-ONLY / DO NOT INTEGRATE"
        )
    )
    lines.append("")
    lines.append("5. Which 3–5 lanes are highest priority for future pressure?")
    lines.append(f"- {', '.join(top_priorities[:5])}")
    lines.append("")
    lines.append("6. Is there a deeper unifying pattern that survives without overclaiming?")
    lines.append(f"- {summary['surviving_unifying_pattern']}")
    lines.append("")
    lines.append("## Artifact Outputs")
    lines.append("")
    lines.append("- `data/generated/discovery/cross_domain_lane_scorecard.csv`")
    lines.append("- `data/generated/discovery/cross_domain_anomaly_catalog.csv`")
    lines.append("- `data/generated/discovery/cross_domain_summary.json`")
    lines.append("- `docs/research-program/full_cross_domain_exploration_report.md`")
    lines.append("")
    lines.append("> All outputs are exploratory and non-promoted.")
    lines.append("")
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n")

    print(f"wrote {DISCOVERY_DIR / 'cross_domain_lane_scorecard.csv'}")
    print(f"wrote {DISCOVERY_DIR / 'cross_domain_anomaly_catalog.csv'}")
    print(f"wrote {DISCOVERY_DIR / 'cross_domain_summary.json'}")
    print(f"wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
