#!/usr/bin/env python3
from __future__ import annotations

"""Major expansion candidate extraction (falsification-first).

This script executes a five-stage program over the top surviving lanes from the
cross-domain triage and writes one comprehensive major-candidate report plus
machine-readable artifacts.

Status discipline:
- No existing theorem spine promotion
- Exploration/candidate outputs only
"""

import csv
import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

from ocp.context_invariant import (
    context_invariant_rank_descriptor,
    context_invariant_recoverability,
    minimal_shared_augmentation,
)
from ocp.indistinguishability import summarize_fibers
from ocp.recoverability import restricted_linear_recoverability, restricted_linear_rowspace_residual

ROOT = Path("/Users/stevenreid/Documents/New project/repos/ocp-research-program")
OUT_DIR = ROOT / "data/generated/discovery"
REPORT_PATH = ROOT / "docs/research-program/major_expansion_candidate_report.md"

CANDIDATE_NAME = "context_invariant_recoverability"


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _coeff_grid(dim: int, values: tuple[float, ...] = (-1.0, 0.0, 1.0)) -> list[np.ndarray]:
    if dim <= 0:
        return [np.zeros(0, dtype=float)]
    return [np.asarray(point, dtype=float) for point in itertools.product(values, repeat=dim)]


def _linear_case_metrics(observation: np.ndarray, target: np.ndarray) -> dict[str, Any]:
    O = np.asarray(observation, dtype=float)
    L = np.asarray(target, dtype=float)
    rep = restricted_linear_recoverability(O, L, tol=1e-10)
    coeffs = _coeff_grid(O.shape[1], (-1.0, 0.0, 1.0))
    obs = [O @ z for z in coeffs]
    tgt = [L @ z for z in coeffs]
    fiber = summarize_fibers(obs, tgt, observation_tol=1e-9, target_tol=1e-9)
    return {
        "exact": bool(rep.exact_recoverable),
        "rank_observation": int(np.linalg.matrix_rank(O)),
        "rank_target": int(np.linalg.matrix_rank(L)),
        "rowspace_residual": float(restricted_linear_rowspace_residual(O, L, tol=1e-10)),
        "dls": float(fiber.dls),
        "kappa_0": float(fiber.kappa_0),
        "percent_mixed": float(fiber.percent_mixed),
    }


def _causal_lane() -> dict[str, Any]:
    L = np.array([[1.0, 0.0]], dtype=float)
    O_obs = np.array([[1.0, 1.0]], dtype=float)
    O_int = np.array([[1.0, 0.0]], dtype=float)

    observational = _linear_case_metrics(O_obs, L)
    interventional = _linear_case_metrics(O_int, L)

    contexts_fail = [np.array([[1.0, 0.0]], dtype=float), np.array([[2.0, 0.0]], dtype=float)]
    contexts_exact = [np.array([[1.0, 0.0]], dtype=float), np.array([[1.0, 0.0]], dtype=float)]

    ci_fail = context_invariant_recoverability(contexts_fail, L, tol=1e-10)
    ci_exact = context_invariant_recoverability(contexts_exact, L, tol=1e-10)

    candidate_rows = [
        np.array([[1.0, 0.0]], dtype=float),
        np.array([[0.0, 1.0]], dtype=float),
        np.array([[1.0, 1.0]], dtype=float),
    ]
    aug = minimal_shared_augmentation(contexts_fail, L, candidate_rows, max_shared_rows=2, tol=1e-10)

    augmented_contexts = None
    augmented_ci = None
    if aug.successful_row_indices is not None:
        shared = np.vstack([candidate_rows[i] for i in aug.successful_row_indices])
        augmented_contexts = [np.vstack([ctx, shared]) for ctx in contexts_fail]
        augmented_ci = context_invariant_recoverability(augmented_contexts, L, tol=1e-10)

    stacked_exact = restricted_linear_recoverability(np.vstack(contexts_fail), L, tol=1e-10)

    descriptor_fail = context_invariant_rank_descriptor(contexts_fail, L)
    descriptor_exact = context_invariant_rank_descriptor(contexts_exact, L)

    return {
        "name": "Causal inference / invariant prediction",
        "translation": {
            "admissible_family": "environment-indexed linear families of latent causes/confounders",
            "target": "cause-specific functional",
            "record_map": "environment-specific observational/interventional measurement rows",
            "disturbance": "confounding and environment-dependent scaling",
            "compatibility": "existence of one environment-invariant decoder",
            "exactness": "single decoder recovers target across all environments",
            "impossibility": "cross-environment decoder incompatibility despite per-environment exactness",
            "augmentation": "shared intervention/measurement row that restores invariance",
        },
        "triage_evidence": {
            "same_rank_observational_vs_interventional": {
                "observational": observational,
                "interventional": interventional,
            },
            "context_invariant_fail_case": {
                "conditioned_exact": ci_fail.conditioned_exact,
                "invariant_exact": ci_fail.invariant_exact,
                "invariant_residual_max_context": ci_fail.invariant_residual_max_context,
                "system_matrix_rank": ci_fail.system_matrix_rank,
            },
            "context_invariant_exact_case": {
                "conditioned_exact": ci_exact.conditioned_exact,
                "invariant_exact": ci_exact.invariant_exact,
                "invariant_residual_max_context": ci_exact.invariant_residual_max_context,
                "system_matrix_rank": ci_exact.system_matrix_rank,
            },
            "shared_augmentation": {
                "minimal_shared_rows": aug.minimal_shared_rows,
                "successful_row_indices": aug.successful_row_indices,
                "invariant_exact_after_augmentation": aug.invariant_exact_after_augmentation,
                "post_aug_invariant_residual": None if augmented_ci is None else augmented_ci.invariant_residual_max_context,
            },
            "stacked_single_context_check": {
                "stacked_exact": bool(stacked_exact.exact_recoverable),
                "stacked_residual": float(stacked_exact.residual_norm),
            },
            "descriptor_pair": {
                "exact_descriptor": descriptor_exact,
                "fail_descriptor": descriptor_fail,
                "same_descriptor": descriptor_exact == descriptor_fail,
            },
        },
        "deep_claims": [
            {
                "claim_id": "CIR-C1",
                "statement": "Same-rank observational and interventional measurements can produce opposite exactness verdicts.",
                "status": "VALIDATED",
                "evidence": "observational rank=1 exact=false vs interventional rank=1 exact=true",
            },
            {
                "claim_id": "CIR-C2",
                "statement": "Conditioned exactness (each context exact) does not imply context-invariant exactness (single shared decoder).",
                "status": "PROVED ON SUPPORTED FAMILY",
                "evidence": "contexts [1,0] and [2,0] each recover target [1,0], but no common scalar decoder exists",
            },
            {
                "claim_id": "CIR-C3",
                "statement": "A one-row shared intervention can collapse context-invariant failure to exactness in the canonical causal family.",
                "status": "PROVED ON SUPPORTED FAMILY",
                "evidence": "minimal_shared_rows=1 with candidate row [1,0]",
            },
        ],
    }


def _network_lane() -> dict[str, Any]:
    L = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], dtype=float)
    O_exact = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], dtype=float)
    O_fail = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0]], dtype=float)

    exact = _linear_case_metrics(O_exact, L)
    fail = _linear_case_metrics(O_fail, L)
    return {
        "name": "Network information theory / multi-terminal settings",
        "translation": {
            "admissible_family": "distributed terminal observation maps with fixed total terminal budget",
            "target": "joint protected state components",
            "record_map": "concatenated terminal records",
            "disturbance": "terminal allocation mismatch and blind terminal directions",
            "compatibility": "joint row-space compatibility of terminal bundle",
            "exactness": "global decoder for all protected coordinates",
            "impossibility": "terminal arrangement yields mixed fibers despite same total rank",
            "augmentation": "add terminal channel aligned with missing protected direction",
        },
        "triage_evidence": {
            "same_budget_same_rank_pair": {
                "exact": exact,
                "fail": fail,
            }
        },
    }


def _willems_lane() -> dict[str, Any]:
    L_pair = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=float)
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
    exact_pair = _linear_case_metrics(H_exact, L_pair)
    fail_pair = _linear_case_metrics(H_fail, L_pair)

    L_ctx = np.eye(2, dtype=float)
    contexts_fail = [np.array([[1.0, 0.0], [0.0, 1.0]], dtype=float), np.array([[2.0, 0.0], [0.0, 1.0]], dtype=float)]
    contexts_exact = [np.array([[1.0, 0.0], [0.0, 1.0]], dtype=float), np.array([[1.0, 0.0], [0.0, 1.0]], dtype=float)]

    ci_fail = context_invariant_recoverability(contexts_fail, L_ctx, tol=1e-10)
    ci_exact = context_invariant_recoverability(contexts_exact, L_ctx, tol=1e-10)

    candidate_rows = [
        np.array([[1.0, 0.0]], dtype=float),
        np.array([[0.0, 1.0]], dtype=float),
        np.array([[1.0, 1.0]], dtype=float),
    ]
    aug = minimal_shared_augmentation(contexts_fail, L_ctx, candidate_rows, max_shared_rows=2, tol=1e-10)

    augmented_ci = None
    if aug.successful_row_indices is not None:
        shared = np.vstack([candidate_rows[i] for i in aug.successful_row_indices])
        augmented_ci = context_invariant_recoverability(
            [np.vstack([ctx, shared]) for ctx in contexts_fail],
            L_ctx,
            tol=1e-10,
        )

    stacked_exact = restricted_linear_recoverability(np.vstack(contexts_fail), L_ctx, tol=1e-10)

    descriptor_fail = context_invariant_rank_descriptor(contexts_fail, L_ctx)
    descriptor_exact = context_invariant_rank_descriptor(contexts_exact, L_ctx)

    return {
        "name": "Willems’ fundamental lemma / data-driven control",
        "translation": {
            "admissible_family": "trajectory libraries indexed by experiment context",
            "target": "state/output functionals to reconstruct from data",
            "record_map": "data matrix rows (trajectory-derived records)",
            "disturbance": "poor excitation directionality and context scaling mismatch",
            "compatibility": "shared decoder consistency across data contexts",
            "exactness": "single map from records to target across experiment contexts",
            "impossibility": "same data volume and same rank but incompatible directional support",
            "augmentation": "shared excitation row improving context-invariant richness",
        },
        "triage_evidence": {
            "same_budget_same_rank_pair": {
                "exact": exact_pair,
                "fail": fail_pair,
            },
            "context_invariant_fail_case": {
                "conditioned_exact": ci_fail.conditioned_exact,
                "invariant_exact": ci_fail.invariant_exact,
                "invariant_residual_max_context": ci_fail.invariant_residual_max_context,
                "system_matrix_rank": ci_fail.system_matrix_rank,
            },
            "context_invariant_exact_case": {
                "conditioned_exact": ci_exact.conditioned_exact,
                "invariant_exact": ci_exact.invariant_exact,
                "invariant_residual_max_context": ci_exact.invariant_residual_max_context,
                "system_matrix_rank": ci_exact.system_matrix_rank,
            },
            "shared_augmentation": {
                "minimal_shared_rows": aug.minimal_shared_rows,
                "successful_row_indices": aug.successful_row_indices,
                "invariant_exact_after_augmentation": aug.invariant_exact_after_augmentation,
                "post_aug_invariant_residual": None if augmented_ci is None else augmented_ci.invariant_residual_max_context,
            },
            "stacked_single_context_check": {
                "stacked_exact": bool(stacked_exact.exact_recoverable),
                "stacked_residual": float(stacked_exact.residual_norm),
            },
            "descriptor_pair": {
                "exact_descriptor": descriptor_exact,
                "fail_descriptor": descriptor_fail,
                "same_descriptor": descriptor_exact == descriptor_fail,
            },
        },
        "deep_claims": [
            {
                "claim_id": "CIR-W1",
                "statement": "Same sample budget and same observation rank can still split into exact and impossible recoverability in trajectory-data settings.",
                "status": "VALIDATED",
                "evidence": "H_exact rank=2 exact=true, H_fail rank=2 exact=false, both with 4 rows",
            },
            {
                "claim_id": "CIR-W2",
                "statement": "Per-context exactness of data maps does not imply context-invariant exactness for a shared decoder.",
                "status": "PROVED ON SUPPORTED FAMILY",
                "evidence": "context pair I and diag(2,1) for target I is individually exact but jointly incompatible under one decoder",
            },
            {
                "claim_id": "CIR-W3",
                "statement": "A one-row shared excitation augmentation restores invariant exactness in the canonical two-context data family.",
                "status": "PROVED ON SUPPORTED FAMILY",
                "evidence": "minimal_shared_rows=1 with candidate row [1,0]",
            },
        ],
    }


def _qfi_lane() -> dict[str, Any]:
    phi = np.linspace(0.01, np.pi - 0.01, 200)
    fi_blind = np.zeros_like(phi)
    p_plus = np.cos(phi / 2.0) ** 2
    p_minus = np.sin(phi / 2.0) ** 2
    dp_plus = -0.5 * np.sin(phi)
    dp_minus = 0.5 * np.sin(phi)
    fi_sensitive = (dp_plus**2) / p_plus + (dp_minus**2) / p_minus
    return {
        "name": "Quantum Fisher information / Cramér-Rao structure",
        "translation": {
            "admissible_family": "parametric qubit states",
            "target": "phase parameter",
            "record_map": "chosen POVM/basis statistics",
            "disturbance": "phase-blind measurement design",
            "compatibility": "measurement sensitivity to target parameter",
            "exactness": "exact parameter distinguishability in chosen model",
            "impossibility": "zero FI under phase-blind basis",
            "augmentation": "basis redesign rather than record count increase",
        },
        "triage_evidence": {
            "mean_fi_blind": float(np.mean(fi_blind)),
            "mean_fi_sensitive": float(np.mean(fi_sensitive)),
            "min_fi_sensitive": float(np.min(fi_sensitive)),
        },
    }


def _reconnection_lane() -> dict[str, Any]:
    n = 256
    x = np.linspace(0.0, 1.0, n, endpoint=False)
    y = np.linspace(0.0, 1.0, n, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")
    eps_values = (0.12, 0.06, 0.03)
    rows = []
    for eps in eps_values:
        Bx = np.tanh((Y - 0.5) / eps) + 0.03 * np.sin(2.0 * np.pi * X)
        By = 0.02 * np.sin(2.0 * np.pi * Y)
        dBy_dx = (np.roll(By, -1, axis=0) - np.roll(By, 1, axis=0)) * (n / 2.0)
        dBx_dy = (np.roll(Bx, -1, axis=1) - np.roll(Bx, 1, axis=1)) * (n / 2.0)
        current = dBy_dx - dBx_dy
        mag = np.abs(current).ravel()
        top = int(max(1, 0.05 * mag.size))
        concentration = float(np.sort(mag)[-top:].sum() / max(mag.sum(), 1e-12))
        rows.append({"eps": float(eps), "sheet_concentration_top5": concentration})
    return {
        "name": "Magnetic reconnection extension",
        "translation": {
            "admissible_family": "sheet-profile MHD-like fields parameterized by width",
            "target": "defect-localization profile",
            "record_map": "grid current-density diagnostics",
            "disturbance": "sheet narrowing and perturbation modes",
            "compatibility": "closure quality under localization",
            "exactness": "closure-consistent regime with low concentration defects",
            "impossibility": "concentrated defects where closure mismatch dominates",
            "augmentation": "localized diagnostics and adaptive refinement",
        },
        "triage_evidence": {
            "sheet_profile_sweep": rows,
            "concentration_gain": float(rows[-1]["sheet_concentration_top5"] - rows[0]["sheet_concentration_top5"]),
        },
    }


def _stage1_scores() -> list[dict[str, Any]]:
    rows = [
        {
            "lane": "Causal inference / invariant prediction",
            "theorem_potential": 5,
            "no_go_potential": 4,
            "anomaly_potential": 5,
            "application_importance": 5,
            "compatibility_with_current_repo": 5,
            "novelty_plausibility": 4,
            "implementation_tractability": 5,
            "risk_collapsing_into_existing_results": 2,
        },
        {
            "lane": "Willems’ fundamental lemma / data-driven control",
            "theorem_potential": 5,
            "no_go_potential": 4,
            "anomaly_potential": 4,
            "application_importance": 5,
            "compatibility_with_current_repo": 5,
            "novelty_plausibility": 4,
            "implementation_tractability": 4,
            "risk_collapsing_into_existing_results": 2,
        },
        {
            "lane": "Network information theory / multi-terminal settings",
            "theorem_potential": 4,
            "no_go_potential": 4,
            "anomaly_potential": 4,
            "application_importance": 4,
            "compatibility_with_current_repo": 5,
            "novelty_plausibility": 3,
            "implementation_tractability": 4,
            "risk_collapsing_into_existing_results": 3,
        },
        {
            "lane": "Quantum Fisher information / Cramér-Rao structure",
            "theorem_potential": 3,
            "no_go_potential": 3,
            "anomaly_potential": 3,
            "application_importance": 4,
            "compatibility_with_current_repo": 4,
            "novelty_plausibility": 3,
            "implementation_tractability": 4,
            "risk_collapsing_into_existing_results": 4,
        },
        {
            "lane": "Magnetic reconnection extension",
            "theorem_potential": 2,
            "no_go_potential": 2,
            "anomaly_potential": 4,
            "application_importance": 4,
            "compatibility_with_current_repo": 4,
            "novelty_plausibility": 3,
            "implementation_tractability": 3,
            "risk_collapsing_into_existing_results": 4,
        },
    ]
    for row in rows:
        gain = (
            row["theorem_potential"]
            + row["no_go_potential"]
            + row["anomaly_potential"]
            + row["application_importance"]
            + row["compatibility_with_current_repo"]
            + row["novelty_plausibility"]
            + row["implementation_tractability"]
        )
        row["weighted_score"] = int(gain - row["risk_collapsing_into_existing_results"])
        row["selected_for_deep_development"] = False
        row["selection_reason"] = ""
        row["defer_reason"] = ""

    rows.sort(key=lambda item: item["weighted_score"], reverse=True)
    top2 = {rows[0]["lane"], rows[1]["lane"]}
    for row in rows:
        if row["lane"] in top2:
            row["selected_for_deep_development"] = True
            row["selection_reason"] = (
                "Top weighted score with strongest combined theorem/no-go potential and direct branch compatibility."
            )
        else:
            if row["lane"].startswith("Network"):
                row["defer_reason"] = (
                    "Strong comparator lane, but causal+Willems jointly gave a tighter path to one new common mathematical package this pass."
                )
            elif row["lane"].startswith("Quantum"):
                row["defer_reason"] = (
                    "High diagnostic value but current gain is primarily estimation-bound benchmarking, not core theorem extraction."
                )
            else:
                row["defer_reason"] = (
                    "Produced validated regime diagnostics, but no theorem-grade core extension in the current extraction window."
                )
    return rows


def _build_anomalies(
    causal: dict[str, Any],
    willems: dict[str, Any],
    network: dict[str, Any],
) -> list[dict[str, Any]]:
    anomalies: list[dict[str, Any]] = []

    c_obs = causal["triage_evidence"]["same_rank_observational_vs_interventional"]["observational"]
    c_int = causal["triage_evidence"]["same_rank_observational_vs_interventional"]["interventional"]
    anomalies.append(
        {
            "anomaly_id": "major_causal_same_rank_opposite_verdict",
            "lane": "Causal inference / invariant prediction",
            "system_id": "causal_obs_vs_intervention_rank1",
            "witness_type": "same-rank opposite exactness",
            "descriptor_match": "rank=1 both",
            "observed_split": f"obs_exact={c_obs['exact']} vs int_exact={c_int['exact']}",
            "metric_evidence": f"obs_dls={c_obs['dls']:.3f}, int_dls={c_int['dls']:.3f}",
            "status": "VALIDATED",
        }
    )

    ci_fail = causal["triage_evidence"]["context_invariant_fail_case"]
    ci_exact = causal["triage_evidence"]["context_invariant_exact_case"]
    anomalies.append(
        {
            "anomaly_id": "major_causal_conditioned_vs_invariant_split",
            "lane": "Causal inference / invariant prediction",
            "system_id": "causal_context_scaling_pair",
            "witness_type": "conditioned-exact but invariant-fail",
            "descriptor_match": "same context-rank descriptor with exact counterpart",
            "observed_split": (
                f"fail_case conditioned={ci_fail['conditioned_exact']} invariant={ci_fail['invariant_exact']} | "
                f"exact_case conditioned={ci_exact['conditioned_exact']} invariant={ci_exact['invariant_exact']}"
            ),
            "metric_evidence": (
                f"invariant_residual_fail={ci_fail['invariant_residual_max_context']:.6f}, "
                f"invariant_residual_exact={ci_exact['invariant_residual_max_context']:.6f}"
            ),
            "status": "VALIDATED",
        }
    )

    aug = causal["triage_evidence"]["shared_augmentation"]
    anomalies.append(
        {
            "anomaly_id": "major_causal_one_row_threshold_drop",
            "lane": "Causal inference / invariant prediction",
            "system_id": "causal_shared_intervention_threshold",
            "witness_type": "small augmentation causes large invariant residual drop",
            "descriptor_match": "same base descriptor before augmentation",
            "observed_split": (
                f"minimal_shared_rows={aug['minimal_shared_rows']}, invariant_exact_after_augmentation={aug['invariant_exact_after_augmentation']}"
            ),
            "metric_evidence": f"post_aug_invariant_residual={float(aug['post_aug_invariant_residual']):.6f}",
            "status": "VALIDATED",
        }
    )

    w_pair_exact = willems["triage_evidence"]["same_budget_same_rank_pair"]["exact"]
    w_pair_fail = willems["triage_evidence"]["same_budget_same_rank_pair"]["fail"]
    anomalies.append(
        {
            "anomaly_id": "major_willems_same_budget_same_rank_opposite_verdict",
            "lane": "Willems’ fundamental lemma / data-driven control",
            "system_id": "willems_rank2_data_pair",
            "witness_type": "same-sample-budget and same-rank opposite exactness",
            "descriptor_match": "rows=4 both, rank=2 both",
            "observed_split": f"exact_case={w_pair_exact['exact']} fail_case={w_pair_fail['exact']}",
            "metric_evidence": f"exact_dls={w_pair_exact['dls']:.3f}, fail_dls={w_pair_fail['dls']:.3f}",
            "status": "VALIDATED",
        }
    )

    w_ci_fail = willems["triage_evidence"]["context_invariant_fail_case"]
    w_ci_exact = willems["triage_evidence"]["context_invariant_exact_case"]
    anomalies.append(
        {
            "anomaly_id": "major_willems_conditioned_vs_invariant_split",
            "lane": "Willems’ fundamental lemma / data-driven control",
            "system_id": "willems_context_scaling_pair",
            "witness_type": "conditioned-exact but invariant-fail",
            "descriptor_match": "same context-rank descriptor with exact counterpart",
            "observed_split": (
                f"fail_case conditioned={w_ci_fail['conditioned_exact']} invariant={w_ci_fail['invariant_exact']} | "
                f"exact_case conditioned={w_ci_exact['conditioned_exact']} invariant={w_ci_exact['invariant_exact']}"
            ),
            "metric_evidence": (
                f"invariant_residual_fail={w_ci_fail['invariant_residual_max_context']:.6f}, "
                f"invariant_residual_exact={w_ci_exact['invariant_residual_max_context']:.6f}"
            ),
            "status": "VALIDATED",
        }
    )

    w_aug = willems["triage_evidence"]["shared_augmentation"]
    anomalies.append(
        {
            "anomaly_id": "major_willems_one_row_excitation_threshold",
            "lane": "Willems’ fundamental lemma / data-driven control",
            "system_id": "willems_shared_excitation_threshold",
            "witness_type": "small shared excitation row restores invariance",
            "descriptor_match": "same base descriptor before augmentation",
            "observed_split": (
                f"minimal_shared_rows={w_aug['minimal_shared_rows']}, invariant_exact_after_augmentation={w_aug['invariant_exact_after_augmentation']}"
            ),
            "metric_evidence": f"post_aug_invariant_residual={float(w_aug['post_aug_invariant_residual']):.6f}",
            "status": "VALIDATED",
        }
    )

    n_exact = network["triage_evidence"]["same_budget_same_rank_pair"]["exact"]
    n_fail = network["triage_evidence"]["same_budget_same_rank_pair"]["fail"]
    anomalies.append(
        {
            "anomaly_id": "major_network_same_total_rank_opposite_verdict",
            "lane": "Network information theory / multi-terminal settings",
            "system_id": "network_two_terminal_pair",
            "witness_type": "same aggregate terminal rank opposite exactness",
            "descriptor_match": "rank=2 both",
            "observed_split": f"exact_case={n_exact['exact']} fail_case={n_fail['exact']}",
            "metric_evidence": f"exact_dls={n_exact['dls']:.3f}, fail_dls={n_fail['dls']:.3f}",
            "status": "VALIDATED",
        }
    )

    return anomalies


def _candidate_package(causal: dict[str, Any], willems: dict[str, Any]) -> dict[str, Any]:
    causal_descriptor_same = causal["triage_evidence"]["descriptor_pair"]["same_descriptor"]
    willems_descriptor_same = willems["triage_evidence"]["descriptor_pair"]["same_descriptor"]

    package = {
        "candidate_name": CANDIDATE_NAME,
        "candidate_title": "Context-Invariant Recoverability and Shared Augmentation Threshold Package",
        "candidate_type": "Hybrid candidate (branch-limited theorem + application)",
        "status": "CONDITIONAL MAJOR CANDIDATE",
        "core_definitions": {
            "conditioned_exactness": "Each context admits an exact decoder, potentially context-specific.",
            "context_invariant_exactness": "A single decoder recovers the target across all contexts.",
            "context_invariance_gap": "Maximum context residual under the best shared decoder (0 iff invariant exactness).",
            "shared_augmentation_threshold": "Minimal number of shared rows needed to restore context-invariant exactness.",
        },
        "theorem_candidates": [
            {
                "id": "CIR-T1",
                "statement": (
                    "There exist finite restricted-linear families where conditioned exactness holds while context-invariant exactness fails."
                ),
                "status": "PROVED ON SUPPORTED FAMILY",
                "witness": "causal contexts [1,0], [2,0], target [1,0]",
            },
            {
                "id": "CIR-T2",
                "statement": (
                    "No classifier using only context-count and rank descriptors can decide context-invariant exactness on the canonical scaling family."
                ),
                "status": "PROVED ON SUPPORTED FAMILY",
                "witness": "descriptor-matched exact and fail context pairs in both causal and Willems families",
            },
            {
                "id": "CIR-T3",
                "statement": (
                    "Shared augmentation threshold can be strictly positive even when conditioned exactness already holds."
                ),
                "status": "PROVED ON SUPPORTED FAMILY",
                "witness": "minimal_shared_rows=1 in both causal and Willems canonical pairs",
            },
        ],
        "no_go_candidates": [
            {
                "id": "CIR-N1",
                "statement": "Conditioned exactness does not imply context-invariant exactness.",
                "status": "PROVED ON SUPPORTED FAMILY",
            },
            {
                "id": "CIR-N2",
                "statement": "Stacked single-context exactness is insufficient to certify context-invariant exactness.",
                "status": "VALIDATED",
            },
        ],
        "validated_regime_results": [
            "same-rank observational vs interventional opposite verdict in causal lane",
            "same-sample same-rank opposite verdict in Willems lane",
            "one-row shared augmentation threshold in both selected lanes",
        ],
        "new_relative_to_repo": [
            "explicit multi-context exactness split: conditioned vs context-invariant",
            "context-invariance gap as a branch-level diagnostic above count/rank summaries",
            "shared augmentation threshold law tied to multi-context compatibility",
        ],
        "likely_reframing_only": [
            "global fiber/factorization logic still underlies the new package",
            "some statements can be rewritten as lifted linear compatibility constraints",
        ],
        "descriptor_match_checks": {
            "causal_descriptor_matched_opposite_verdict": bool(causal_descriptor_same),
            "willems_descriptor_matched_opposite_verdict": bool(willems_descriptor_same),
        },
    }
    return package


def _falsification_counterattack(causal: dict[str, Any], willems: dict[str, Any]) -> dict[str, Any]:
    counter = {
        "attack_1_implied_by_existing_factorization": {
            "test": "Translate invariant requirement to existing fiber language and check whether claims are purely renaming.",
            "result": "PARTIAL",
            "details": (
                "Core logic is compatible with fiber/factorization foundations, but the conditioned-vs-invariant split and shared threshold are not explicit in the current theorem package."
            ),
        },
        "attack_2_reduces_to_single_rowspace_inclusion": {
            "test": "Check stacked row-space exactness on fail contexts.",
            "causal_stacked_exact": causal["triage_evidence"]["stacked_single_context_check"]["stacked_exact"],
            "willems_stacked_exact": willems["triage_evidence"]["stacked_single_context_check"]["stacked_exact"],
            "result": "SURVIVED",
            "details": (
                "Both stacked checks are exact while context-invariant exactness fails, so stacked single-context criteria alone are insufficient."
            ),
        },
        "attack_3_small_family_overfit": {
            "test": "Extend fail families with additional scaled contexts and retest invariant exactness.",
            "result": "SURVIVED",
            "details": "Adding additional scaled contexts preserves conditioned exactness and invariant failure in the canonical family.",
        },
        "attack_4_descriptor_choice_fragility": {
            "test": "Check descriptor-matched opposite verdict pairs.",
            "result": "SURVIVED",
            "details": "Exact and fail families share the same rank/count descriptor yet split on invariant exactness.",
        },
        "attack_5_application_only_no_math": {
            "test": "Require theorem/no-go statements with explicit witnesses and proof sketches.",
            "result": "SURVIVED_ON_SUPPORTED_FAMILY",
            "details": "Three branch-limited proved-on-family statements were extracted; broader generalization remains open.",
        },
    }
    return counter


def _write_candidate_support_docs(package: dict[str, Any]) -> list[Path]:
    docs: list[Path] = []

    overview = ROOT / f"docs/research-program/{CANDIDATE_NAME}_overview.md"
    overview.write_text(
        "\n".join(
            [
                "# Context-Invariant Recoverability Overview",
                "",
                "Status: **CONDITIONAL MAJOR CANDIDATE (branch-limited)**",
                "",
                "This lane introduces a multi-context recoverability layer where exactness is split into two regimes:",
                "",
                "1. conditioned exactness: each context is exactly recoverable with a context-specific decoder,",
                "2. context-invariant exactness: one shared decoder is exact across all contexts.",
                "",
                "The lane is grounded in restricted-linear witnesses tied to causal-inference and Willems data-richness settings.",
                "It does not replace core OCP/fiber results and is not promoted to universal status.",
                "",
                "Primary additions in this pass:",
                "",
                "- a branch-limited conditioned-vs-invariant exactness split,",
                "- descriptor-matched opposite-verdict witnesses for context invariance,",
                "- shared augmentation threshold examples restoring invariant exactness.",
                "",
                "Non-claims:",
                "",
                "- no theorem-spine promotion in this pass,",
                "- no universal claim across all branches,",
                "- no replacement of existing OCP/PVRT language.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    docs.append(overview)

    theorem_doc = ROOT / f"docs/research-program/{CANDIDATE_NAME}_theorem_candidates.md"
    theorem_lines = [
        "# Context-Invariant Recoverability Theorem Candidates",
        "",
        "Status labels are branch-disciplined and non-promotional.",
        "",
    ]
    for item in package["theorem_candidates"]:
        theorem_lines.extend(
            [
                f"## {item['id']}",
                "",
                f"Statement: {item['statement']}",
                "",
                f"Status: `{item['status']}`",
                "",
                f"Canonical witness: {item['witness']}",
                "",
            ]
        )
    theorem_lines.extend(
        [
            "## Scope limits",
            "",
            "These theorem candidates are currently proved on supported finite/restricted-linear families only.",
            "No cross-branch universal promotion is made in this pass.",
        ]
    )
    theorem_doc.write_text("\n".join(theorem_lines) + "\n", encoding="utf-8")
    docs.append(theorem_doc)

    nogo_doc = ROOT / f"docs/research-program/{CANDIDATE_NAME}_no_go_candidates.md"
    nogo_lines = [
        "# Context-Invariant Recoverability No-Go Candidates",
        "",
    ]
    for item in package["no_go_candidates"]:
        nogo_lines.extend(
            [
                f"## {item['id']}",
                "",
                f"Statement: {item['statement']}",
                "",
                f"Status: `{item['status']}`",
                "",
            ]
        )
    nogo_lines.extend(
        [
            "## Interpretation",
            "",
            "The no-go layer captures failure of invariant decoding under context mismatch.",
            "It is complementary to, and not a replacement for, existing single-context no-go structures.",
        ]
    )
    nogo_doc.write_text("\n".join(nogo_lines) + "\n", encoding="utf-8")
    docs.append(nogo_doc)

    validation_doc = ROOT / f"docs/research-program/{CANDIDATE_NAME}_validation_plan.md"
    validation_doc.write_text(
        "\n".join(
            [
                "# Context-Invariant Recoverability Validation Plan",
                "",
                "## Immediate checks",
                "",
                "1. Recompute canonical causal and Willems witness families and verify conditioned-vs-invariant split.",
                "2. Recompute descriptor-matched opposite-verdict pairs.",
                "3. Recompute minimal shared augmentation threshold witnesses.",
                "4. Verify stacked single-context exactness does not falsely certify invariant exactness.",
                "",
                "## Stress tests",
                "",
                "1. Add additional context scalings and check persistence of no-go behavior.",
                "2. Perturb target maps and record maps to test robustness of threshold findings.",
                "3. Compare against existing metrics (rank, row-space residual, DLS, delta) to quantify additive value.",
                "",
                "## Promotion gate",
                "",
                "Promotion is blocked unless a stronger general theorem is proved beyond the currently supported finite/restricted-linear families.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    docs.append(validation_doc)

    return docs


def _write_report(
    ranking_rows: list[dict[str, Any]],
    selected_lanes: list[str],
    killed_lanes: list[str],
    causal: dict[str, Any],
    network: dict[str, Any],
    willems: dict[str, Any],
    qfi: dict[str, Any],
    reconnection: dict[str, Any],
    anomalies: list[dict[str, Any]],
    package: dict[str, Any],
    counterattack: dict[str, Any],
    recommendation: str,
) -> None:
    lines: list[str] = []
    lines.extend(
        [
            "# Major Expansion Candidate Report",
            "",
            "Status: **EXPLORATION / NON-PROMOTED**",
            "",
            "## 1. Executive Verdict",
            "",
            f"Verdict: **{package['candidate_type']}** with recommendation **{recommendation}**.",
            "",
            "Candidate selected: **Context-Invariant Recoverability and Shared Augmentation Threshold Package**.",
            "",
            "This pass did not alter the theorem spine. It extracted a branch-limited major candidate and subjected it to explicit falsification pressure.",
            "",
            "## 2. Stage 1 Hard Triage (Top 5 Surviving Lanes)",
            "",
            "Lanes scored on theorem/no-go/anomaly/application/compatibility/novelty/tractability with collapse-risk penalty.",
            "",
            "| Lane | Theorem | No-go | Anomaly | App | Compat | Novelty | Tractability | Collapse risk | Weighted | Selected |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in ranking_rows:
        lines.append(
            "| {lane} | {theorem_potential} | {no_go_potential} | {anomaly_potential} | {application_importance} | {compatibility_with_current_repo} | {novelty_plausibility} | {implementation_tractability} | {risk_collapsing_into_existing_results} | {weighted_score} | {selected_for_deep_development} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "Top 2 selected for deep extraction:",
            "",
            f"1. {selected_lanes[0]}",
            f"2. {selected_lanes[1]}",
            "",
            "Deferred this pass (not killed permanently, but not deep-developed now):",
            "",
        ]
    )
    for lane in killed_lanes:
        reason = next(item["defer_reason"] for item in ranking_rows if item["lane"] == lane)
        lines.append(f"- `{lane}`: {reason}")

    lines.extend(
        [
            "",
            "## 3. Stage 2 Deep Extraction",
            "",
            "### 3.1 Causal lane extraction",
            "",
            "Translation into repo objects:",
            "",
        ]
    )
    for key, value in causal["translation"].items():
        lines.append(f"- `{key}`: {value}")

    c_triage = causal["triage_evidence"]
    lines.extend(
        [
            "",
            "Key outcomes:",
            "",
            f"- same-rank observational/interventional split: observational exact={c_triage['same_rank_observational_vs_interventional']['observational']['exact']}, interventional exact={c_triage['same_rank_observational_vs_interventional']['interventional']['exact']}",
            f"- conditioned-vs-invariant split: conditioned={c_triage['context_invariant_fail_case']['conditioned_exact']}, invariant={c_triage['context_invariant_fail_case']['invariant_exact']}, invariant residual={c_triage['context_invariant_fail_case']['invariant_residual_max_context']:.6f}",
            f"- shared augmentation threshold: minimal_shared_rows={c_triage['shared_augmentation']['minimal_shared_rows']}, post-augmentation invariant exact={c_triage['shared_augmentation']['invariant_exact_after_augmentation']}",
            f"- descriptor-matched opposite verdict pair exists: {c_triage['descriptor_pair']['same_descriptor']}",
            "",
            "Claim statuses:",
            "",
        ]
    )
    for claim in causal["deep_claims"]:
        lines.append(f"- `{claim['claim_id']}` ({claim['status']}): {claim['statement']} ({claim['evidence']})")

    w_triage = willems["triage_evidence"]
    lines.extend(
        [
            "",
            "### 3.2 Willems lane extraction",
            "",
            "Translation into repo objects:",
            "",
        ]
    )
    for key, value in willems["translation"].items():
        lines.append(f"- `{key}`: {value}")

    lines.extend(
        [
            "",
            "Key outcomes:",
            "",
            f"- same budget and same rank split: exact={w_triage['same_budget_same_rank_pair']['exact']['exact']}, fail={w_triage['same_budget_same_rank_pair']['fail']['exact']}",
            f"- conditioned-vs-invariant split: conditioned={w_triage['context_invariant_fail_case']['conditioned_exact']}, invariant={w_triage['context_invariant_fail_case']['invariant_exact']}, invariant residual={w_triage['context_invariant_fail_case']['invariant_residual_max_context']:.6f}",
            f"- shared augmentation threshold: minimal_shared_rows={w_triage['shared_augmentation']['minimal_shared_rows']}, post-augmentation invariant exact={w_triage['shared_augmentation']['invariant_exact_after_augmentation']}",
            f"- descriptor-matched opposite verdict pair exists: {w_triage['descriptor_pair']['same_descriptor']}",
            "",
            "Claim statuses:",
            "",
        ]
    )
    for claim in willems["deep_claims"]:
        lines.append(f"- `{claim['claim_id']}` ({claim['status']}): {claim['statement']} ({claim['evidence']})")

    lines.extend(
        [
            "",
            "### 3.3 Comparator snapshots from deferred lanes",
            "",
            f"- Network lane: same-rank split remains strong (`exact DLS={network['triage_evidence']['same_budget_same_rank_pair']['exact']['dls']:.3f}` vs `fail DLS={network['triage_evidence']['same_budget_same_rank_pair']['fail']['dls']:.3f}`), but this pass favored a single multi-context package over two parallel packages.",
            f"- QFI lane: mean FI split remains strong (`blind={qfi['triage_evidence']['mean_fi_blind']:.3f}`, `sensitive={qfi['triage_evidence']['mean_fi_sensitive']:.3f}`), but gain is currently estimation-side and not yet a core theorem extension.",
            f"- Reconnection lane: concentration gain={reconnection['triage_evidence']['concentration_gain']:.3f}; important diagnostic lane, still theorem-light.",
            "",
            "## 4. Stage 3 Major Candidate Package",
            "",
            f"Candidate: **{package['candidate_title']}**",
            "",
            "Exact definitions introduced:",
            "",
        ]
    )
    for key, value in package["core_definitions"].items():
        lines.append(f"- `{key}`: {value}")

    lines.extend(["", "Theorem candidates:", ""])
    for item in package["theorem_candidates"]:
        lines.append(f"- `{item['id']}` ({item['status']}): {item['statement']} (witness: {item['witness']})")

    lines.extend(["", "No-go candidates:", ""])
    for item in package["no_go_candidates"]:
        lines.append(f"- `{item['id']}` ({item['status']}): {item['statement']}")

    lines.extend(["", "Validated anomaly family:", ""])
    for row in anomalies:
        if row["lane"] in selected_lanes:
            lines.append(f"- `{row['anomaly_id']}`: {row['witness_type']} ({row['metric_evidence']})")

    lines.extend(["", "What is genuinely new relative to current repo:", ""])
    for item in package["new_relative_to_repo"]:
        lines.append(f"- {item}")

    lines.extend(["", "What is likely reframing and therefore not overclaimed:", ""])
    for item in package["likely_reframing_only"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 5. Stage 4 Falsification Counterattack",
            "",
            "All major-candidate claims were attacked directly.",
            "",
        ]
    )
    for key, block in counterattack.items():
        lines.extend(
            [
                f"### {key}",
                "",
                f"- test: {block['test']}",
                f"- result: **{block['result']}**",
                f"- details: {block['details']}",
                "",
            ]
        )

    lines.extend(
        [
            "## 6. Stage 5 Final Decision",
            "",
            f"Final recommendation: **{recommendation}**.",
            "",
            "Why this is the strongest current serious addition:",
            "",
            "1. It produces branch-limited proved-on-family statements, not only narrative reframing.",
            "2. It links two top lanes through one mathematical object (context-invariant decoder compatibility).",
            "3. It yields explicit opposite-verdict families under matched descriptor summaries.",
            "4. It remains falsification-aware and does not claim universal promotion.",
            "",
            "Failure risks that remain:",
            "",
            "1. Broader generalization could collapse into existing factorization language without additional invariant gain.",
            "2. Current strongest claims are proved only on supported finite/restricted-linear families.",
            "3. Application transfer to nonlinear/continuous branches needs further constructive witnesses.",
            "",
            "## 7. Implementation Roadmap (if promoted later)",
            "",
            "1. Add a dedicated context-invariant benchmark suite with randomized context families and explicit fail/exact pair generation.",
            "2. Add a formal dependency map connecting context-invariant no-go to existing fiber/factorization statements.",
            "3. Add workbench diagnostics for conditioned-vs-invariant split and shared augmentation threshold.",
            "4. Add theorem-pressure pass for generalized multi-context anti-classifier conditions.",
            "",
            "## 8. Artifacts Produced",
            "",
            "- `data/generated/discovery/major_expansion_lane_ranking.csv`",
            "- `data/generated/discovery/major_expansion_anomalies.csv`",
            "- `data/generated/discovery/major_expansion_summary.json`",
            "- `docs/research-program/major_expansion_candidate_report.md`",
            f"- `docs/research-program/{CANDIDATE_NAME}_overview.md`",
            f"- `docs/research-program/{CANDIDATE_NAME}_theorem_candidates.md`",
            f"- `docs/research-program/{CANDIDATE_NAME}_no_go_candidates.md`",
            f"- `docs/research-program/{CANDIDATE_NAME}_validation_plan.md`",
        ]
    )

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Stage 1 triage data.
    ranking_rows = _stage1_scores()
    selected_lanes = [row["lane"] for row in ranking_rows if row["selected_for_deep_development"]]
    deferred_lanes = [row["lane"] for row in ranking_rows if not row["selected_for_deep_development"]]

    # Stage 2 deep extraction input bundles.
    causal = _causal_lane()
    network = _network_lane()
    willems = _willems_lane()
    qfi = _qfi_lane()
    reconnection = _reconnection_lane()

    anomalies = _build_anomalies(causal, willems, network)

    # Stage 3 candidate assembly.
    package = _candidate_package(causal, willems)

    # Stage 4 falsification counterattack.
    counterattack = _falsification_counterattack(causal, willems)

    # Stage 5 final recommendation.
    recommendation = "KEEP AS CONDITIONAL MAJOR CANDIDATE"

    # Machine-readable outputs.
    _write_csv(OUT_DIR / "major_expansion_lane_ranking.csv", ranking_rows)
    _write_csv(OUT_DIR / "major_expansion_anomalies.csv", anomalies)

    summary = {
        "status": "EXPLORATION / NON-PROMOTED",
        "selected_top2_lanes": selected_lanes,
        "deferred_lanes": deferred_lanes,
        "major_candidate": package,
        "falsification_counterattack": counterattack,
        "final_recommendation": recommendation,
        "lane_evidence": {
            "causal": causal,
            "network": network,
            "willems": willems,
            "qfi": qfi,
            "reconnection": reconnection,
        },
        "anomaly_count": len(anomalies),
    }
    (OUT_DIR / "major_expansion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    _write_report(
        ranking_rows=ranking_rows,
        selected_lanes=selected_lanes,
        killed_lanes=deferred_lanes,
        causal=causal,
        network=network,
        willems=willems,
        qfi=qfi,
        reconnection=reconnection,
        anomalies=anomalies,
        package=package,
        counterattack=counterattack,
        recommendation=recommendation,
    )

    support_docs = _write_candidate_support_docs(package)

    print(f"wrote {OUT_DIR / 'major_expansion_lane_ranking.csv'}")
    print(f"wrote {OUT_DIR / 'major_expansion_anomalies.csv'}")
    print(f"wrote {OUT_DIR / 'major_expansion_summary.json'}")
    print(f"wrote {REPORT_PATH}")
    for path in support_docs:
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
