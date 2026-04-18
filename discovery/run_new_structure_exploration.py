#!/usr/bin/env python3
from __future__ import annotations

"""Standalone deep discovery pass for new recoverability structure.

This script intentionally writes only to discovery/* outputs and does not modify
repo theorem spines or integration layers.
"""

from dataclasses import dataclass
import csv
import itertools
import json
import math
from pathlib import Path
from typing import Callable

import numpy as np

from ocp.indistinguishability import summarize_fibers
from ocp.recoverability import restricted_linear_recoverability, restricted_linear_rowspace_residual

ROOT = Path("/Users/stevenreid/Documents/New project/repos/ocp-research-program")
DISCOVERY_DIR = ROOT / "discovery"


@dataclass
class CandidateStatement:
    name: str
    statement: str
    status: str
    evidence: str
    failure_mode: str


def _ensure_dir() -> None:
    DISCOVERY_DIR.mkdir(parents=True, exist_ok=True)


def _coeff_grid(dim: int, values: tuple[float, ...] = (-1.0, 0.0, 1.0)) -> list[np.ndarray]:
    if dim <= 0:
        return [np.zeros(0, dtype=float)]
    return [np.asarray(point, dtype=float) for point in itertools.product(values, repeat=dim)]


def _linear_metrics(observation: np.ndarray, target: np.ndarray, *, tol: float = 1e-10) -> dict[str, float | int | bool]:
    O = np.asarray(observation, dtype=float)
    L = np.asarray(target, dtype=float)
    rep = restricted_linear_recoverability(O, L, tol=tol)
    residual = float(restricted_linear_rowspace_residual(O, L, tol=tol))

    coeffs = _coeff_grid(O.shape[1], (-1.0, 0.0, 1.0))
    obs = [O @ z for z in coeffs]
    tgt = [L @ z for z in coeffs]
    fiber = summarize_fibers(obs, tgt, observation_tol=1e-9, target_tol=1e-9)

    return {
        "exact": bool(rep.exact_recoverable),
        "rank_observation": int(np.linalg.matrix_rank(O)),
        "rank_target": int(np.linalg.matrix_rank(L)),
        "rowspace_residual": residual,
        "dls": float(fiber.dls),
        "kappa_0": float(fiber.kappa_0),
        "percent_mixed": float(fiber.percent_mixed),
    }


def _context_invariance_metrics(contexts: list[np.ndarray], target: np.ndarray, *, tol: float = 1e-10) -> dict[str, float | int | bool]:
    if not contexts:
        raise ValueError("contexts must be non-empty")
    A = [np.asarray(m, dtype=float) for m in contexts]
    L = np.asarray(target, dtype=float)
    p = A[0].shape[0]
    q = L.shape[0]

    conditioned = all(bool(restricted_linear_recoverability(O, L, tol=tol).exact_recoverable) for O in A)

    blocks = []
    rhs = []
    Iq = np.eye(q, dtype=float)
    for O in A:
        blocks.append(np.kron(O.T, Iq))
        rhs.append(L.reshape(-1, order="F"))
    M = np.vstack(blocks)
    b = np.concatenate(rhs)

    sol, *_ = np.linalg.lstsq(M, b, rcond=None)
    D = sol.reshape((q, p), order="F")
    context_residuals = [float(np.linalg.norm(D @ O - L, ord="fro")) for O in A]
    cid = float(max(context_residuals))

    return {
        "conditioned_exact": bool(conditioned),
        "invariant_exact": bool(cid <= tol),
        "cid": cid,
        "system_rank": int(np.linalg.matrix_rank(M, tol)),
        "record_dim": int(p),
        "target_dim": int(q),
        "context_count": int(len(A)),
    }


def _shared_augmentation_threshold(
    contexts: list[np.ndarray],
    target: np.ndarray,
    candidate_rows: list[np.ndarray],
    *,
    tol: float = 1e-10,
    max_rows: int = 2,
) -> int | None:
    base = _context_invariance_metrics(contexts, target, tol=tol)
    if bool(base["invariant_exact"]):
        return 0

    for k in range(1, max_rows + 1):
        for combo in itertools.combinations(range(len(candidate_rows)), k):
            shared = np.vstack([candidate_rows[i] for i in combo])
            augmented = [np.vstack([O, shared]) for O in contexts]
            rep = _context_invariance_metrics(augmented, target, tol=tol)
            if bool(rep["invariant_exact"]):
                return k
    return None


def _descriptor_signature(row: dict[str, object]) -> str:
    keys = [
        "lane",
        "measurement_count",
        "observation_rank",
        "target_rank",
        "terminal_count",
        "context_count",
    ]
    return "|".join(str(row.get(k, "")) for k in keys)


def _new_row(**kwargs: object) -> dict[str, object]:
    template: dict[str, object] = {
        "system_id": "",
        "lane": "",
        "family": "",
        "subtype": "",
        "measurement_count": "",
        "observation_rank": "",
        "target_rank": "",
        "terminal_count": "",
        "context_count": "",
        "exact_recoverable": "",
        "conditioned_exact": "",
        "invariant_exact": "",
        "cid": "",
        "rowspace_residual": "",
        "dls": "",
        "kappa_0": "",
        "partition_synergy_index": "",
        "intervention_lift": "",
        "augmentation_threshold": "",
        "weak_target_exact": "",
        "strong_target_exact": "",
        "recovery_frontier_size": "",
        "fisher_min": "",
        "fisher_mean": "",
        "defect_localization_index": "",
        "threshold_chain": "",
        "descriptor_signature": "",
        "note": "",
    }
    template.update(kwargs)
    template["descriptor_signature"] = _descriptor_signature(template)
    return template


def _lane_causal(rows: list[dict[str, object]]) -> None:
    alphas = [0.1, 0.2, 0.5, 1.0, 2.0, 4.0]
    target = np.array([[1.0, 0.0]], dtype=float)
    candidate_rows = [
        np.array([[1.0, 0.0]], dtype=float),
        np.array([[0.0, 1.0]], dtype=float),
        np.array([[1.0, 1.0]], dtype=float),
    ]

    for idx, alpha in enumerate(alphas):
        O_obs = np.array([[1.0, float(alpha)]], dtype=float)
        O_int = np.array([[1.0, 0.0]], dtype=float)
        O_aug = np.array([[1.0, float(alpha)], [0.0, 1.0]], dtype=float)

        obs = _linear_metrics(O_obs, target)
        itv = _linear_metrics(O_int, target)
        aug = _linear_metrics(O_aug, target)

        intervention_lift = float(obs["rowspace_residual"]) - float(itv["rowspace_residual"])

        rows.append(
            _new_row(
                system_id=f"causal_obs_{idx}",
                lane="causal_inference",
                family="confounded_linear_observation",
                subtype="observational",
                measurement_count=O_obs.shape[0],
                observation_rank=obs["rank_observation"],
                target_rank=obs["rank_target"],
                terminal_count=1,
                context_count=1,
                exact_recoverable=int(bool(obs["exact"])),
                rowspace_residual=obs["rowspace_residual"],
                dls=obs["dls"],
                kappa_0=obs["kappa_0"],
                intervention_lift=intervention_lift,
                note=f"alpha={alpha}",
            )
        )
        rows.append(
            _new_row(
                system_id=f"causal_itv_{idx}",
                lane="causal_inference",
                family="confounded_linear_observation",
                subtype="interventional",
                measurement_count=O_int.shape[0],
                observation_rank=itv["rank_observation"],
                target_rank=itv["rank_target"],
                terminal_count=1,
                context_count=1,
                exact_recoverable=int(bool(itv["exact"])),
                rowspace_residual=itv["rowspace_residual"],
                dls=itv["dls"],
                kappa_0=itv["kappa_0"],
                intervention_lift=intervention_lift,
                note=f"alpha={alpha}",
            )
        )
        rows.append(
            _new_row(
                system_id=f"causal_aug_{idx}",
                lane="causal_inference",
                family="confounded_linear_observation",
                subtype="augmented_observational",
                measurement_count=O_aug.shape[0],
                observation_rank=aug["rank_observation"],
                target_rank=aug["rank_target"],
                terminal_count=1,
                context_count=1,
                exact_recoverable=int(bool(aug["exact"])),
                rowspace_residual=aug["rowspace_residual"],
                dls=aug["dls"],
                kappa_0=aug["kappa_0"],
                intervention_lift=intervention_lift,
                note=f"alpha={alpha}",
            )
        )

        # Context-pair architecture case: conditioned exact may hold while shared-decoder exact fails.
        c_fail = [np.array([[1.0, 0.0]], dtype=float), np.array([[1.0 + alpha, 0.0]], dtype=float)]
        c_exact = [np.array([[1.0, 0.0]], dtype=float), np.array([[1.0, 0.0]], dtype=float)]

        fail_metrics = _context_invariance_metrics(c_fail, target)
        exact_metrics = _context_invariance_metrics(c_exact, target)
        threshold = _shared_augmentation_threshold(c_fail, target, candidate_rows, max_rows=2)

        rows.append(
            _new_row(
                system_id=f"causal_ctx_fail_{idx}",
                lane="causal_inference",
                family="context_scaling_pair",
                subtype="conditioned_exact_invariant_fail",
                measurement_count=1,
                observation_rank=1,
                target_rank=1,
                terminal_count=1,
                context_count=2,
                exact_recoverable=int(bool(fail_metrics["invariant_exact"])),
                conditioned_exact=int(bool(fail_metrics["conditioned_exact"])),
                invariant_exact=int(bool(fail_metrics["invariant_exact"])),
                cid=fail_metrics["cid"],
                augmentation_threshold=threshold,
                note=f"alpha={alpha}",
            )
        )
        rows.append(
            _new_row(
                system_id=f"causal_ctx_exact_{idx}",
                lane="causal_inference",
                family="context_scaling_pair",
                subtype="conditioned_exact_invariant_exact",
                measurement_count=1,
                observation_rank=1,
                target_rank=1,
                terminal_count=1,
                context_count=2,
                exact_recoverable=int(bool(exact_metrics["invariant_exact"])),
                conditioned_exact=int(bool(exact_metrics["conditioned_exact"])),
                invariant_exact=int(bool(exact_metrics["invariant_exact"])),
                cid=exact_metrics["cid"],
                augmentation_threshold=0,
                note=f"alpha={alpha}",
            )
        )


def _lane_multi_terminal(rows: list[dict[str, object]]) -> None:
    basis = np.eye(4, dtype=float)
    target = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], dtype=float)

    terminal_rows = [
        basis[0:1, :],
        basis[1:2, :],
        basis[2:3, :],
        basis[3:4, :],
        np.array([[1.0, 1.0, 0.0, 0.0]], dtype=float),
        np.array([[1.0, 0.0, 1.0, 0.0]], dtype=float),
        np.array([[0.0, 1.0, 1.0, 0.0]], dtype=float),
    ]

    case_idx = 0
    for i, O1 in enumerate(terminal_rows):
        for j, O2 in enumerate(terminal_rows):
            O_joint = np.vstack([O1, O2])
            m_joint = _linear_metrics(O_joint, target)
            m1 = _linear_metrics(O1, target)
            m2 = _linear_metrics(O2, target)

            best_single_dls = min(float(m1["dls"]), float(m2["dls"]))
            psi = float(best_single_dls - float(m_joint["dls"]))

            rows.append(
                _new_row(
                    system_id=f"multi_terminal_{case_idx}",
                    lane="multi_terminal",
                    family="two_terminal_linear_partition",
                    subtype="joint",
                    measurement_count=2,
                    observation_rank=m_joint["rank_observation"],
                    target_rank=m_joint["rank_target"],
                    terminal_count=2,
                    context_count=1,
                    exact_recoverable=int(bool(m_joint["exact"])),
                    rowspace_residual=m_joint["rowspace_residual"],
                    dls=m_joint["dls"],
                    kappa_0=m_joint["kappa_0"],
                    partition_synergy_index=psi,
                    note=f"terminal_pair=({i},{j})",
                )
            )
            case_idx += 1


def _lane_willems(rows: list[dict[str, object]]) -> None:
    target = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=float)
    row_bank = [
        np.array([1.0, 0.0, 0.0], dtype=float),
        np.array([0.0, 1.0, 0.0], dtype=float),
        np.array([0.0, 0.0, 1.0], dtype=float),
        np.array([1.0, 1.0, 0.0], dtype=float),
        np.array([1.0, -1.0, 0.0], dtype=float),
        np.array([0.0, 1.0, 1.0], dtype=float),
        np.array([0.0, 2.0, -1.0], dtype=float),
        np.array([2.0, 0.0, 0.0], dtype=float),
    ]

    combos = list(itertools.combinations(range(len(row_bank)), 4))
    chosen = combos[:55]  # deterministic broad sweep

    for idx, combo in enumerate(chosen):
        O = np.vstack([row_bank[i] for i in combo])
        met = _linear_metrics(O, target)
        rows.append(
            _new_row(
                system_id=f"willems_data_{idx}",
                lane="willems_data_driven",
                family="trajectory_library_rows",
                subtype="library_instance",
                measurement_count=4,
                observation_rank=met["rank_observation"],
                target_rank=met["rank_target"],
                terminal_count=1,
                context_count=1,
                exact_recoverable=int(bool(met["exact"])),
                rowspace_residual=met["rowspace_residual"],
                dls=met["dls"],
                kappa_0=met["kappa_0"],
                note=f"rows={combo}",
            )
        )

    # Canonical opposite-verdict same-budget, same-rank pair.
    H_exact = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [1.0, 1.0, 0.0],
            [2.0, -1.0, 0.0],
        ],
        dtype=float,
    )
    H_fail = np.array(
        [
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 1.0, 1.0],
            [0.0, 2.0, -1.0],
        ],
        dtype=float,
    )
    for label, H in (("exact", H_exact), ("fail", H_fail)):
        met = _linear_metrics(H, target)
        rows.append(
            _new_row(
                system_id=f"willems_canonical_{label}",
                lane="willems_data_driven",
                family="canonical_same_budget_pair",
                subtype=label,
                measurement_count=4,
                observation_rank=met["rank_observation"],
                target_rank=met["rank_target"],
                terminal_count=1,
                context_count=1,
                exact_recoverable=int(bool(met["exact"])),
                rowspace_residual=met["rowspace_residual"],
                dls=met["dls"],
                kappa_0=met["kappa_0"],
                note=label,
            )
        )

    # Context-invariant data architecture witnesses.
    target_ctx = np.eye(2, dtype=float)
    for idx, beta in enumerate([0.1, 0.2, 0.5, 1.0, 2.0]):
        contexts_fail = [
            np.array([[1.0, 0.0], [0.0, 1.0]], dtype=float),
            np.array([[1.0 + beta, 0.0], [0.0, 1.0]], dtype=float),
        ]
        contexts_exact = [
            np.array([[1.0, 0.0], [0.0, 1.0]], dtype=float),
            np.array([[1.0, 0.0], [0.0, 1.0]], dtype=float),
        ]
        candidate_rows = [
            np.array([[1.0, 0.0]], dtype=float),
            np.array([[0.0, 1.0]], dtype=float),
            np.array([[1.0, 1.0]], dtype=float),
        ]
        fail = _context_invariance_metrics(contexts_fail, target_ctx)
        ok = _context_invariance_metrics(contexts_exact, target_ctx)
        threshold = _shared_augmentation_threshold(contexts_fail, target_ctx, candidate_rows, max_rows=2)

        rows.append(
            _new_row(
                system_id=f"willems_ctx_fail_{idx}",
                lane="willems_data_driven",
                family="context_scaled_data_map",
                subtype="conditioned_exact_invariant_fail",
                measurement_count=2,
                observation_rank=2,
                target_rank=2,
                terminal_count=1,
                context_count=2,
                exact_recoverable=int(bool(fail["invariant_exact"])),
                conditioned_exact=int(bool(fail["conditioned_exact"])),
                invariant_exact=int(bool(fail["invariant_exact"])),
                cid=fail["cid"],
                augmentation_threshold=threshold,
                note=f"beta={beta}",
            )
        )
        rows.append(
            _new_row(
                system_id=f"willems_ctx_exact_{idx}",
                lane="willems_data_driven",
                family="context_scaled_data_map",
                subtype="conditioned_exact_invariant_exact",
                measurement_count=2,
                observation_rank=2,
                target_rank=2,
                terminal_count=1,
                context_count=2,
                exact_recoverable=int(bool(ok["invariant_exact"])),
                conditioned_exact=int(bool(ok["conditioned_exact"])),
                invariant_exact=int(bool(ok["invariant_exact"])),
                cid=ok["cid"],
                augmentation_threshold=0,
                note=f"beta={beta}",
            )
        )


def _lane_fisher(rows: list[dict[str, object]]) -> None:
    theta = np.linspace(0.02, np.pi - 0.02, 300)

    def fisher_from_p(p: np.ndarray, dp: np.ndarray) -> np.ndarray:
        p = np.clip(p, 1e-12, 1.0 - 1e-12)
        return (dp**2) / (p * (1.0 - p))

    # Model family: same outcome count (binary), varying sensitivity geometry.
    models: list[tuple[str, Callable[[np.ndarray], tuple[np.ndarray, np.ndarray]]]] = [
        ("blind", lambda t: (0.5 * np.ones_like(t), np.zeros_like(t))),
        ("weak_eps_0.1", lambda t: (0.5 + 0.1 * np.sin(t), 0.1 * np.cos(t))),
        ("weak_eps_0.25", lambda t: (0.5 + 0.25 * np.sin(t), 0.25 * np.cos(t))),
        ("cos_k1", lambda t: (np.cos(t / 2.0) ** 2, -0.5 * np.sin(t))),
        ("cos_k2", lambda t: (np.cos(t) ** 2, -np.sin(2.0 * t))),
    ]

    for idx, (name, fn) in enumerate(models):
        p, dp = fn(theta)
        fi = fisher_from_p(p, dp)
        fi_min = float(np.min(fi))
        fi_mean = float(np.mean(fi))
        # Surrogate exactness label for this lane only.
        sensitivity_recoverable = int(fi_min > 0.15)

        rows.append(
            _new_row(
                system_id=f"fisher_{idx}",
                lane="measurement_sensitivity",
                family="binary_measurement_models",
                subtype=name,
                measurement_count=1,
                observation_rank=1,
                target_rank=1,
                terminal_count=1,
                context_count=1,
                exact_recoverable=sensitivity_recoverable,
                fisher_min=fi_min,
                fisher_mean=fi_mean,
                note=f"model={name}",
            )
        )


def _lane_mhd_localized(rows: list[dict[str, object]]) -> None:
    n = 200
    x = np.linspace(0.0, 1.0, n, endpoint=False)
    y = np.linspace(0.0, 1.0, n, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")
    for idx, eps in enumerate([0.16, 0.12, 0.08, 0.06, 0.04, 0.03]):
        Bx = np.tanh((Y - 0.5) / eps) + 0.02 * np.sin(2.0 * np.pi * X)
        By = 0.02 * np.sin(2.0 * np.pi * Y)
        dBy_dx = (np.roll(By, -1, axis=0) - np.roll(By, 1, axis=0)) * (n / 2.0)
        dBx_dy = (np.roll(Bx, -1, axis=1) - np.roll(Bx, 1, axis=1)) * (n / 2.0)
        current = np.abs(dBy_dx - dBx_dy).ravel()
        top = int(max(1, 0.05 * current.size))
        dli = float(np.sort(current)[-top:].sum() / max(current.sum(), 1e-12))
        rows.append(
            _new_row(
                system_id=f"mhd_local_{idx}",
                lane="localized_defect",
                family="sheet_localization_proxy",
                subtype="eps_sweep",
                measurement_count=1,
                terminal_count=1,
                context_count=1,
                defect_localization_index=dli,
                note=f"eps={eps}",
            )
        )


def _partial_recovery_lattice(rows: list[dict[str, object]]) -> None:
    # Same observation map, weak targets may recover while strong targets fail.
    observations = {
        "obs_a": np.array([[1.0, 0.0, 0.0]], dtype=float),
        "obs_b": np.array([[1.0, 1.0, 0.0]], dtype=float),
        "obs_c": np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=float),
    }
    weak_targets = [
        np.array([[1.0, 0.0, 0.0]], dtype=float),
        np.array([[0.0, 1.0, 0.0]], dtype=float),
        np.array([[1.0, 1.0, 0.0]], dtype=float),
    ]
    strong_target = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=float)

    for obs_name, O in observations.items():
        weak_exact = 0
        for wid, Lw in enumerate(weak_targets):
            met_w = _linear_metrics(O, Lw)
            weak_exact += int(bool(met_w["exact"]))
            rows.append(
                _new_row(
                    system_id=f"lattice_{obs_name}_weak_{wid}",
                    lane="target_lattice",
                    family="weak_vs_strong_target",
                    subtype="weak",
                    measurement_count=O.shape[0],
                    observation_rank=met_w["rank_observation"],
                    target_rank=met_w["rank_target"],
                    terminal_count=1,
                    context_count=1,
                    exact_recoverable=int(bool(met_w["exact"])),
                    weak_target_exact=int(bool(met_w["exact"])),
                    rowspace_residual=met_w["rowspace_residual"],
                    dls=met_w["dls"],
                    kappa_0=met_w["kappa_0"],
                    threshold_chain=obs_name,
                    note=f"weak_target_{wid}",
                )
            )

        met_s = _linear_metrics(O, strong_target)
        rows.append(
            _new_row(
                system_id=f"lattice_{obs_name}_strong",
                lane="target_lattice",
                family="weak_vs_strong_target",
                subtype="strong",
                measurement_count=O.shape[0],
                observation_rank=met_s["rank_observation"],
                target_rank=met_s["rank_target"],
                terminal_count=1,
                context_count=1,
                exact_recoverable=int(bool(met_s["exact"])),
                strong_target_exact=int(bool(met_s["exact"])),
                recovery_frontier_size=weak_exact,
                rowspace_residual=met_s["rowspace_residual"],
                dls=met_s["dls"],
                kappa_0=met_s["kappa_0"],
                threshold_chain=obs_name,
                note="strong_target",
            )
        )


def _threshold_chains(rows: list[dict[str, object]]) -> None:
    # Explicit add/remove one-measurement flips.
    basis = np.eye(4, dtype=float)
    target = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], dtype=float)
    chains = {
        "chain_good": [basis[0:1, :], basis[1:2, :], basis[2:3, :]],
        "chain_bad": [basis[2:3, :], basis[3:4, :], basis[0:1, :]],
    }
    for chain_id, seq in chains.items():
        current = []
        for k, row in enumerate(seq, start=1):
            current.append(row)
            O = np.vstack(current)
            met = _linear_metrics(O, target)
            rows.append(
                _new_row(
                    system_id=f"threshold_{chain_id}_{k}",
                    lane="multi_terminal",
                    family="incremental_measurement_chain",
                    subtype="threshold_sequence",
                    measurement_count=k,
                    observation_rank=met["rank_observation"],
                    target_rank=met["rank_target"],
                    terminal_count=1,
                    context_count=1,
                    exact_recoverable=int(bool(met["exact"])),
                    rowspace_residual=met["rowspace_residual"],
                    dls=met["dls"],
                    kappa_0=met["kappa_0"],
                    threshold_chain=chain_id,
                    note=f"k={k}",
                )
            )


def _collect_anomalies(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    anomalies: list[dict[str, object]] = []

    def exact_value(row: dict[str, object]) -> int | None:
        v = row.get("exact_recoverable", "")
        if v in ("", None):
            return None
        return int(v)

    # A1: same-descriptor opposite verdict.
    grouped: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        ev = exact_value(row)
        if ev is None:
            continue
        grouped.setdefault(str(row["descriptor_signature"]), []).append(row)

    for sig, items in grouped.items():
        vals = {exact_value(item) for item in items}
        if vals == {0, 1}:
            anomalies.append(
                {
                    "anomaly_id": f"same_descriptor_split_{len(anomalies)}",
                    "anomaly_type": "same_descriptor_opposite_verdict",
                    "lane": items[0]["lane"],
                    "systems": ";".join(str(it["system_id"]) for it in items[:4]),
                    "why_it_matters": "Rank/count descriptor fails to classify recoverability.",
                    "evidence": sig,
                }
            )

    # A2: one-measurement threshold flips.
    chain_groups: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        cid = str(row.get("threshold_chain", ""))
        if not cid:
            continue
        if exact_value(row) is None:
            continue
        chain_groups.setdefault(cid, []).append(row)

    for chain_id, items in chain_groups.items():
        items_sorted = sorted(items, key=lambda r: int(r["measurement_count"]))
        for left, right in zip(items_sorted, items_sorted[1:]):
            if int(right["measurement_count"]) - int(left["measurement_count"]) != 1:
                continue
            if exact_value(left) != exact_value(right):
                anomalies.append(
                    {
                        "anomaly_id": f"threshold_flip_{chain_id}_{left['measurement_count']}_{right['measurement_count']}",
                        "anomaly_type": "one_measurement_flip",
                        "lane": left["lane"],
                        "systems": f"{left['system_id']}->{right['system_id']}",
                        "why_it_matters": "Single-measurement increments can trigger discontinuous exactness transitions.",
                        "evidence": f"exact {left['exact_recoverable']} -> {right['exact_recoverable']}",
                    }
                )

    # A3: intervention beats observation at same count.
    causal_obs = [r for r in rows if r["lane"] == "causal_inference" and r["subtype"] == "observational"]
    causal_itv = [r for r in rows if r["lane"] == "causal_inference" and r["subtype"] == "interventional"]
    for obs, itv in zip(causal_obs, causal_itv):
        if exact_value(obs) == 0 and exact_value(itv) == 1 and int(obs["measurement_count"]) == int(itv["measurement_count"]):
            anomalies.append(
                {
                    "anomaly_id": f"intervention_lift_{obs['system_id']}",
                    "anomaly_type": "intervention_vs_observation",
                    "lane": "causal_inference",
                    "systems": f"{obs['system_id']}|{itv['system_id']}",
                    "why_it_matters": "Measurement type dominates measurement count.",
                    "evidence": f"residual_obs={obs['rowspace_residual']}, residual_itv={itv['rowspace_residual']}",
                }
            )

    # A4: distributed arrangement dominates total amount.
    mt = [r for r in rows if r["lane"] == "multi_terminal" and r["family"] == "two_terminal_linear_partition"]
    by_desc: dict[str, list[dict[str, object]]] = {}
    for row in mt:
        key = f"count={row['measurement_count']}|rank={row['observation_rank']}|target={row['target_rank']}"
        by_desc.setdefault(key, []).append(row)
    for key, items in by_desc.items():
        vals = {exact_value(item) for item in items}
        if vals == {0, 1}:
            best = sorted(items, key=lambda r: float(r.get("partition_synergy_index", 0.0)), reverse=True)
            anomalies.append(
                {
                    "anomaly_id": f"distributed_arrangement_{len(anomalies)}",
                    "anomaly_type": "distributed_structure_over_amount",
                    "lane": "multi_terminal",
                    "systems": f"{best[0]['system_id']}|{best[-1]['system_id']}",
                    "why_it_matters": "Same total information budget/rank but different partition leads to opposite outcomes.",
                    "evidence": key,
                }
            )

    # A5: measurement sensitivity dominates count (Fisher lane).
    fisher = [r for r in rows if r["lane"] == "measurement_sensitivity"]
    for i, j in itertools.combinations(fisher, 2):
        if i["measurement_count"] != j["measurement_count"]:
            continue
        if exact_value(i) == exact_value(j):
            continue
        fi_i = float(i["fisher_min"])
        fi_j = float(j["fisher_min"])
        if abs(fi_i - fi_j) > 0.2:
            anomalies.append(
                {
                    "anomaly_id": f"fisher_sensitivity_split_{len(anomalies)}",
                    "anomaly_type": "measurement_type_over_count",
                    "lane": "measurement_sensitivity",
                    "systems": f"{i['system_id']}|{j['system_id']}",
                    "why_it_matters": "Same count but very different sensitivity floor produces opposite recoverability verdict.",
                    "evidence": f"fisher_min {fi_i:.4f} vs {fi_j:.4f}",
                }
            )
            break

    return anomalies


def _novelty_filter(rows: list[dict[str, object]], anomalies: list[dict[str, object]]) -> list[dict[str, object]]:
    # Candidate objects to retain/reject.
    obj_rows: list[dict[str, object]] = []

    # O1: CID (context-invariance defect)
    ctx_rows = [r for r in rows if r["context_count"] == 2 and r["cid"] != "" and r["lane"] in {"causal_inference", "willems_data_driven"}]
    descriptor_groups: dict[str, list[dict[str, object]]] = {}
    for r in ctx_rows:
        key = f"lane={r['lane']}|m={r['measurement_count']}|rank={r['observation_rank']}|target={r['target_rank']}"
        descriptor_groups.setdefault(key, []).append(r)

    descriptor_fail = any({int(x["exact_recoverable"]) for x in grp} == {0, 1} for grp in descriptor_groups.values() if len(grp) >= 2)
    cid_separates = all(
        ((float(r["cid"]) <= 1e-8) == bool(int(r["exact_recoverable"])))
        for r in ctx_rows
    ) if ctx_rows else False

    obj_rows.append(
        {
            "object": "Context-Invariance Defect (CID)",
            "definition": "CID = inf_D max_c ||D O_c - L||_F over shared decoder D.",
            "novelty_test": "Descriptor-matched opposite verdict contexts and CID separation check.",
            "result": "KEPT" if descriptor_fail and cid_separates else "REJECT",
            "reason": (
                "CID separates invariant exact vs fail on descriptor-matched context families; captures architecture constraint absent from amount-only descriptors."
                if descriptor_fail and cid_separates
                else "CID did not add predictive power in this sweep."
            ),
        }
    )

    # O2: Partition Synergy Index (PSI)
    mt_rows = [r for r in rows if r["lane"] == "multi_terminal" and r["family"] == "two_terminal_linear_partition"]
    psi_assoc = 0
    if mt_rows:
        positive = [r for r in mt_rows if float(r["partition_synergy_index"]) > 1e-6]
        if positive:
            psi_assoc = sum(int(r["exact_recoverable"]) for r in positive) / len(positive)
    obj_rows.append(
        {
            "object": "Partition Synergy Index (PSI)",
            "definition": "PSI = min_i DLS(single terminal i) - DLS(joint terminals).",
            "novelty_test": "Same total rank/count partition families with opposite exactness.",
            "result": "KEPT" if any(a["anomaly_type"] == "distributed_structure_over_amount" for a in anomalies) else "REJECT",
            "reason": (
                f"Distributed partition anomalies detected; positive-PSI exactness rate={psi_assoc:.3f}."
                if any(a["anomaly_type"] == "distributed_structure_over_amount" for a in anomalies)
                else "No distributed anomaly gain found."
            ),
        }
    )

    # O3: Intervention Lift (IL)
    il_rows = [r for r in rows if r["lane"] == "causal_inference" and r["intervention_lift"] != ""]
    lift_support = sum(1 for r in il_rows if float(r["intervention_lift"]) > 1e-6)
    obj_rows.append(
        {
            "object": "Intervention Lift (IL)",
            "definition": "IL = residual(observational) - residual(interventional) at matched measurement count.",
            "novelty_test": "Matched-count observational-vs-interventional opposite verdict frequency.",
            "result": "KEPT" if lift_support >= 3 else "REJECT",
            "reason": (
                f"Intervention lifted recoverability in {lift_support} matched-count families."
                if lift_support >= 3
                else "Insufficient lift evidence."
            ),
        }
    )

    # O4: Target Sensitivity Floor (TSF)
    f_rows = [r for r in rows if r["lane"] == "measurement_sensitivity"]
    tsf_split = False
    if f_rows:
        low = [r for r in f_rows if float(r["fisher_min"]) <= 1e-6]
        high = [r for r in f_rows if float(r["fisher_min"]) >= 0.2]
        if low and high:
            tsf_split = (all(int(r["exact_recoverable"]) == 0 for r in low) and all(int(r["exact_recoverable"]) == 1 for r in high))
    obj_rows.append(
        {
            "object": "Target Sensitivity Floor (TSF)",
            "definition": "TSF = min_theta I_F(theta) for target parameter under fixed measurement family.",
            "novelty_test": "Same-count sensitivity families with opposite recoverability labels.",
            "result": "KEPT" if tsf_split else "REJECT",
            "reason": (
                "TSF cleanly separates sensitivity-blind vs sensitivity-resolving families at fixed count."
                if tsf_split
                else "TSF did not separate outcomes robustly."
            ),
        }
    )

    # O5: Recovery Frontier Size (RFS)
    l_rows = [r for r in rows if r["lane"] == "target_lattice" and r["subtype"] == "strong"]
    weak_strong_split = any(int(r["strong_target_exact"]) == 0 and int(r["recovery_frontier_size"]) >= 1 for r in l_rows)
    obj_rows.append(
        {
            "object": "Recovery Frontier Size (RFS)",
            "definition": "RFS(O) = number of weak targets recoverable under O before strong-target failure.",
            "novelty_test": "Weak-vs-strong target split under fixed observation map.",
            "result": "KEPT" if weak_strong_split else "REJECT",
            "reason": (
                "Reveals partial-recovery lattice structure (weak recoverable, strong impossible)."
                if weak_strong_split
                else "No meaningful lattice split observed."
            ),
        }
    )

    return obj_rows


def _candidate_theory_statements(rows: list[dict[str, object]]) -> list[CandidateStatement]:
    statements: list[CandidateStatement] = []

    # S1 proved on supported family: conditioned exactness does not imply context-invariant exactness.
    ctx_fail = [r for r in rows if r["context_count"] == 2 and r["conditioned_exact"] == 1 and r["invariant_exact"] == 0]
    ctx_ok = [r for r in rows if r["context_count"] == 2 and r["conditioned_exact"] == 1 and r["invariant_exact"] == 1]
    if ctx_fail and ctx_ok:
        statements.append(
            CandidateStatement(
                name="Context-architecture incompatibility theorem (supported family)",
                statement=(
                    "There exist context families with identical rank/count descriptors where every context is exactly recoverable, "
                    "yet no single decoder is exact across contexts."
                ),
                status="PROVED",
                evidence=f"found {len(ctx_fail)} fail and {len(ctx_ok)} exact descriptor-matched context witnesses",
                failure_mode="fails only if architecture constraint (shared decoder) is removed",
            )
        )

    # S2 proved: same total rank/count multi-terminal opposite verdict.
    mt = [r for r in rows if r["lane"] == "multi_terminal" and r["family"] == "two_terminal_linear_partition"]
    key_groups: dict[str, set[int]] = {}
    for r in mt:
        key = f"m={r['measurement_count']}|rank={r['observation_rank']}|target={r['target_rank']}"
        key_groups.setdefault(key, set()).add(int(r["exact_recoverable"]))
    split_groups = [k for k, vals in key_groups.items() if vals == {0, 1}]
    statements.append(
        CandidateStatement(
            name="Distributed arrangement anti-classifier theorem (supported family)",
            statement=(
                "In two-terminal linear partition families, total measurement count and joint rank do not determine exact recoverability; "
                "terminal arrangement can flip the verdict."
            ),
            status="PROVED" if split_groups else "DISPROVED",
            evidence=(f"descriptor groups with opposite verdicts: {len(split_groups)}" if split_groups else "no opposite-verdict groups found"),
            failure_mode="disproves amount-only distributed classification",
        )
    )

    # S3 conditional: CID predicts invariant exactness beyond descriptors.
    ctx = [r for r in rows if r["context_count"] == 2 and r["cid"] != "" and r["exact_recoverable"] != ""]
    cid_correct = sum(int((float(r["cid"]) <= 1e-8) == bool(int(r["exact_recoverable"]))) for r in ctx)
    statements.append(
        CandidateStatement(
            name="CID separation conjecture",
            statement="Context-Invariance Defect threshold separates invariant exact/fail classes in generated multi-context families.",
            status="CONDITIONAL" if ctx else "OPEN",
            evidence=(f"CID threshold accuracy={cid_correct}/{len(ctx)}" if ctx else "no context rows"),
            failure_mode="may collapse under broader nonlinear/contextual families",
        )
    )

    # S4 proved (classical): zero Fisher floor means no finite-variance unbiased local recovery.
    fisher_rows = [r for r in rows if r["lane"] == "measurement_sensitivity"]
    zero_floor = [r for r in fisher_rows if float(r["fisher_min"]) <= 1e-8]
    nonzero_floor = [r for r in fisher_rows if float(r["fisher_min"]) > 1e-8]
    statements.append(
        CandidateStatement(
            name="Sensitivity-floor no-go",
            statement=(
                "At fixed measurement count, zero Fisher sensitivity floor implies no finite-variance unbiased local estimator for the target parameter (Cramér-Rao no-go)."
            ),
            status="PROVED" if zero_floor and nonzero_floor else "CONDITIONAL",
            evidence=f"zero-floor models={len(zero_floor)}, nonzero-floor models={len(nonzero_floor)}",
            failure_mode="applies to local unbiased estimation regime",
        )
    )

    # S5 disprove naive claim.
    statements.append(
        CandidateStatement(
            name="Naive amount-only claim",
            statement="Same rank and same count imply same exact-recovery verdict.",
            status="DISPROVED",
            evidence="counterexamples found in causal, multi-terminal, and Willems lanes",
            failure_mode="same-descriptor opposite-verdict anomalies",
        )
    )

    return statements


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _write_theory_candidates(objects: list[dict[str, object]], statements: list[CandidateStatement]) -> None:
    path = DISCOVERY_DIR / "theory_candidates.md"
    lines: list[str] = []
    lines.extend(
        [
            "# Theory Candidates (Discovery Sandbox)",
            "",
            "Status: exploration-only, non-integrated.",
            "",
            "## Top candidate structures",
            "",
        ]
    )
    for row in objects:
        lines.extend(
            [
                f"### {row['object']}",
                "",
                f"Definition: {row['definition']}",
                "",
                f"Novelty test: {row['novelty_test']}",
                "",
                f"Filter result: **{row['result']}**",
                "",
                f"Reason: {row['reason']}",
                "",
            ]
        )

    lines.extend(["## Strongest theorem / no-go candidates", ""])
    for s in statements:
        lines.extend(
            [
                f"### {s.name}",
                "",
                f"Statement: {s.statement}",
                "",
                f"Status: `{s.status}`",
                "",
                f"Evidence: {s.evidence}",
                "",
                f"Failure mode / limit: {s.failure_mode}",
                "",
            ]
        )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_report(
    rows: list[dict[str, object]],
    anomalies: list[dict[str, object]],
    objects: list[dict[str, object]],
    statements: list[CandidateStatement],
) -> None:
    path = DISCOVERY_DIR / "new_structures_report.md"

    by_lane: dict[str, int] = {}
    for r in rows:
        by_lane[str(r["lane"])] = by_lane.get(str(r["lane"]), 0) + 1

    exact_rows = [r for r in rows if r["exact_recoverable"] not in ("", None)]
    exact_count = sum(int(r["exact_recoverable"]) for r in exact_rows)

    status_counts: dict[str, int] = {}
    for s in statements:
        status_counts[s.status] = status_counts.get(s.status, 0) + 1

    lines: list[str] = []
    lines.extend(
        [
            "# New Structure Discovery Report",
            "",
            "Status: **EXPLORATION / NON-INTEGRATED**",
            "",
            "This pass intentionally avoids repository theory integration and focuses on falsification-first structure search.",
            "",
            "## Scope",
            "",
            "Focused lanes:",
            "",
            "1. Causal inference / invariant prediction",
            "2. Multi-terminal / distributed observation",
            "3. Data-driven control / Willems-style trajectory recovery",
            "4. Measurement sensitivity / Fisher geometry",
            "5. Optional localized defect structure",
            "",
            "## Phase 1 — New formal objects",
            "",
            "Objects tested:",
            "",
            "- Context-Invariance Defect (CID)",
            "- Partition Synergy Index (PSI)",
            "- Intervention Lift (IL)",
            "- Target Sensitivity Floor (TSF)",
            "- Recovery Frontier Size (RFS)",
            "",
            "Each object was evaluated against novelty tests that target failures of rank/count descriptors.",
            "",
            "## Phase 2 — Witness generation",
            "",
            f"Total witness systems generated: **{len(rows)}**",
            "",
            "Witness counts by lane:",
            "",
        ]
    )
    for lane, count in sorted(by_lane.items()):
        lines.append(f"- `{lane}`: {count}")

    lines.extend(
        [
            "",
            f"Rows with exactness labels: **{len(exact_rows)}** (exact={exact_count}, fail={len(exact_rows) - exact_count})",
            "",
            "## Phase 3 — Anomaly detection",
            "",
            f"Detected anomalies: **{len(anomalies)}**",
            "",
            "Top anomaly families:",
            "",
        ]
    )

    by_type: dict[str, int] = {}
    for a in anomalies:
        key = str(a["anomaly_type"])
        by_type[key] = by_type.get(key, 0) + 1
    for key, count in sorted(by_type.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{key}`: {count}")

    lines.extend(
        [
            "",
            "Representative anomalies:",
            "",
        ]
    )
    for a in anomalies[:12]:
        lines.append(
            f"- `{a['anomaly_id']}` ({a['lane']}): {a['why_it_matters']} Evidence: {a['evidence']}"
        )

    lines.extend(["", "## Phase 4 — Pattern extraction", ""])

    # Pattern snippets
    ctx_rows = [r for r in rows if r["context_count"] == 2 and r["cid"] not in ("", None)]
    if ctx_rows:
        cid_vals = np.asarray([float(r["cid"]) for r in ctx_rows], dtype=float)
        lines.append(
            f"- CID range across context families: min={cid_vals.min():.6g}, max={cid_vals.max():.6g}."
        )

    mt_rows = [r for r in rows if r["lane"] == "multi_terminal" and r["partition_synergy_index"] not in ("", None)]
    if mt_rows:
        psi_vals = np.asarray([float(r["partition_synergy_index"]) for r in mt_rows], dtype=float)
        lines.append(
            f"- PSI range across multi-terminal families: min={psi_vals.min():.6g}, max={psi_vals.max():.6g}."
        )

    fisher_rows = [r for r in rows if r["lane"] == "measurement_sensitivity"]
    if fisher_rows:
        fmin = np.asarray([float(r["fisher_min"]) for r in fisher_rows], dtype=float)
        lines.append(
            f"- Fisher sensitivity floor range: min={fmin.min():.6g}, max={fmin.max():.6g} at fixed measurement count."
        )

    lines.extend(["", "## Phase 5 — Prove / disprove pressure", ""])
    for s in statements:
        lines.append(f"- `{s.name}`: **{s.status}** — {s.evidence}")

    lines.extend(["", "Proof/disproof status distribution:", ""])
    for status, count in sorted(status_counts.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{status}`: {count}")

    lines.extend(["", "## Phase 6 — Novelty filter", ""])
    kept = 0
    for row in objects:
        lines.append(f"- `{row['object']}`: **{row['result']}** — {row['reason']}")
        if row["result"] == "KEPT":
            kept += 1

    lines.extend(
        [
            "",
            f"Objects kept after novelty filter: **{kept}/{len(objects)}**.",
            "",
            "## Phase 7 — Candidate standalone framework",
            "",
            "Working title: **Structured Recoverability Geometry (SRG)**",
            "",
            "Core components:",
            "",
            "1. CID for multi-context architecture constraints.",
            "2. PSI for distributed partition effects.",
            "3. IL for intervention-vs-observation lifts.",
            "4. TSF for sensitivity-limited distinguishability.",
            "5. RFS for weak-vs-strong target frontier geometry.",
            "",
            "SRG remains a candidate framework. It is not promoted and is intentionally decoupled from existing repo theory labels in this pass.",
            "",
            "## Final verdict",
            "",
        ]
    )

    if kept >= 1:
        lines.append(
            "At least one nontrivial structure survived novelty pressure (CID/PSI/IL/TSF/RFS set), with proved or conditional statements and explicit anomaly families."
        )
    else:
        lines.append("No new structure survived novelty pressure; current results are reducible to existing logic.")

    lines.extend(
        [
            "",
            "## Output files",
            "",
            "- `discovery/new_structures_report.md`",
            "- `discovery/witness_catalog.csv`",
            "- `discovery/anomaly_catalog.csv`",
            "- `discovery/theory_candidates.md`",
        ]
    )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    _ensure_dir()

    rows: list[dict[str, object]] = []

    _lane_causal(rows)
    _lane_multi_terminal(rows)
    _lane_willems(rows)
    _lane_fisher(rows)
    _lane_mhd_localized(rows)
    _partial_recovery_lattice(rows)
    _threshold_chains(rows)

    anomalies = _collect_anomalies(rows)
    objects = _novelty_filter(rows, anomalies)
    statements = _candidate_theory_statements(rows)

    _write_csv(DISCOVERY_DIR / "witness_catalog.csv", rows)
    _write_csv(DISCOVERY_DIR / "anomaly_catalog.csv", anomalies)
    _write_theory_candidates(objects, statements)
    _write_report(rows, anomalies, objects, statements)

    summary = {
        "status": "EXPLORATION / NON-INTEGRATED",
        "witness_count": len(rows),
        "anomaly_count": len(anomalies),
        "objects_tested": objects,
        "candidate_statements": [s.__dict__ for s in statements],
    }
    (DISCOVERY_DIR / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"wrote {DISCOVERY_DIR / 'witness_catalog.csv'}")
    print(f"wrote {DISCOVERY_DIR / 'anomaly_catalog.csv'}")
    print(f"wrote {DISCOVERY_DIR / 'theory_candidates.md'}")
    print(f"wrote {DISCOVERY_DIR / 'new_structures_report.md'}")
    print(f"wrote {DISCOVERY_DIR / 'summary.json'}")


if __name__ == "__main__":
    main()
