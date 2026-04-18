#!/usr/bin/env python3
"""Deep continuation pass for context operators and formation bridge tests.

Outputs:
- data/generated/context_sensitive_recoverability/agreement_operator_witness_catalog.csv
- data/generated/context_sensitive_recoverability/agreement_operator_anomaly_catalog.csv
- data/generated/sfpr/formation_deep_bridge_catalog.csv
- data/generated/sfpr/formation_deep_bridge_summary.json
"""
from __future__ import annotations

import csv
import json
import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Sequence

import numpy as np

from ocp.context_invariant import (
    agreement_operator_recoverability,
    candidate_library_recoverability,
    context_invariant_recoverability,
    minimal_shared_augmentation,
    unconstrained_shared_augmentation_threshold,
)
from ocp.recoverability import restricted_linear_recoverability

SEED = 20260418
RNG = np.random.default_rng(SEED)
TOL = 1e-8

ROOT = Path(__file__).resolve().parents[2]
OUT_CTX = ROOT / "data" / "generated" / "context_sensitive_recoverability"
OUT_CTX.mkdir(parents=True, exist_ok=True)
OUT_SFPR = ROOT / "data" / "generated" / "sfpr"
OUT_SFPR.mkdir(parents=True, exist_ok=True)


def _random_invertible(size: int) -> np.ndarray:
    while True:
        matrix = RNG.integers(-3, 4, size=(size, size)).astype(float)
        if abs(np.linalg.det(matrix)) > 1e-6:
            return matrix


def _random_full_row_rank(rows: int, cols: int) -> np.ndarray:
    while True:
        matrix = RNG.integers(-3, 4, size=(rows, cols)).astype(float)
        if np.linalg.matrix_rank(matrix) == rows:
            return matrix


def _random_row_rank_matrix(rows: int, cols: int, rank_target: int) -> np.ndarray:
    if rank_target <= 0 or rank_target > min(rows, cols):
        raise ValueError("invalid rank_target for matrix shape")
    left = _random_full_row_rank(rank_target, cols)
    mix = RNG.integers(-3, 4, size=(rows, rank_target)).astype(float)
    while np.linalg.matrix_rank(mix) < rank_target:
        mix = RNG.integers(-3, 4, size=(rows, rank_target)).astype(float)
    matrix = mix @ left
    return matrix


def _descriptor_signature(target: np.ndarray, contexts: Sequence[np.ndarray]) -> str:
    stack = np.vstack(contexts)
    return (
        f"n{contexts[0].shape[1]}|p{contexts[0].shape[0]}|q{target.shape[0]}|"
        f"k{len(contexts)}|budget{sum(m.shape[0] for m in contexts)}|"
        f"stackr{np.linalg.matrix_rank(stack)}|targetr{np.linalg.matrix_rank(target)}"
    )


def _candidate_rows(target: np.ndarray, contexts: Sequence[np.ndarray]) -> list[np.ndarray]:
    d = target.shape[1]
    rows: list[np.ndarray] = []
    for context in contexts:
        for row in context[: min(2, context.shape[0])]:
            rows.append(row)
    for i in range(min(d, 3)):
        e = np.zeros(d, dtype=float)
        e[i] = 1.0
        rows.append(e)
    stacked = np.vstack(contexts)
    for i in range(min(2, stacked.shape[0])):
        for j in range(i + 1, min(3, stacked.shape[0])):
            rows.append(stacked[i] + stacked[j])
            rows.append(stacked[i] - stacked[j])
    deduped: list[np.ndarray] = []
    for row in rows:
        if np.linalg.norm(row) <= TOL:
            continue
        if not any(np.linalg.norm(row - old) <= 1e-9 for old in deduped):
            deduped.append(row)
    return deduped


def _family_metrics(family_id: str, mode: str, target: np.ndarray, contexts: Sequence[np.ndarray]) -> dict:
    local_flags = [bool(restricted_linear_recoverability(context, target).exact_recoverable) for context in contexts]
    local_exact_all = all(local_flags)
    direct = context_invariant_recoverability(contexts, target)
    agreement = agreement_operator_recoverability(contexts, target)
    free_aug = unconstrained_shared_augmentation_threshold(contexts, target)
    candidates = _candidate_rows(target, contexts)
    restricted_aug = minimal_shared_augmentation(
        contexts,
        target,
        candidates,
        max_shared_rows=2,
    )
    library = candidate_library_recoverability(
        contexts,
        target,
        candidates,
        max_search_rows=2,
    )

    stack = np.vstack(contexts)
    stack_rep = restricted_linear_recoverability(stack, target)
    stack_alignment = 1.0 - (stack_rep.residual_norm / (np.linalg.norm(target) + 1e-12))

    restricted_rows = restricted_aug.minimal_shared_rows
    restricted_rows = "" if restricted_rows is None else int(restricted_rows)

    return {
        "family_id": family_id,
        "mode": mode,
        "n": int(target.shape[1]),
        "p_record": int(contexts[0].shape[0]),
        "q_target": int(target.shape[0]),
        "k_contexts": int(len(contexts)),
        "descriptor_signature": _descriptor_signature(target, contexts),
        "local_exact_all": int(local_exact_all),
        "invariant_exact_direct": int(direct.invariant_exact),
        "invariant_exact_agreement": int(agreement.invariant_exact_via_agreement),
        "lift_direct_consistent": int(agreement.lift_direct_consistent),
        "agreement_basis_dim": int(agreement.agreement_basis_dimension),
        "lifted_rank": int(agreement.lifted_matrix_rank),
        "lifted_residual_norm": float(agreement.lifted_residual_norm),
        "stack_residual_norm": float(stack_rep.residual_norm),
        "stack_alignment": float(stack_alignment),
        "free_aug_threshold": int(free_aug.minimal_shared_rows_free),
        "restricted_aug_threshold": restricted_rows,
        "restricted_aug_found": int(restricted_aug.invariant_exact_after_augmentation),
        "free_aug_constructed_exact": int(free_aug.invariant_exact_after_constructed),
        "candidate_count": int(library.candidate_count),
        "library_rank_gain": int(library.library_rank_gain),
        "library_target_defect": int(library.library_target_defect),
        "library_full_pool_feasible": int(library.full_pool_feasible),
        "library_full_pool_exact": int(library.invariant_exact_with_full_pool),
        "library_search_limit": int(library.search_limit),
        "library_found_within_limit": int(library.found_within_limit),
        "notes": "",
    }


def _latent_pair(pair_id: int) -> tuple[dict, dict, dict[str, tuple[np.ndarray, list[np.ndarray]]]]:
    n = int(RNG.integers(6, 10))
    p = int(RNG.integers(3, 6))
    q = int(RNG.integers(2, min(4, p + 1)))
    k = int(RNG.integers(2, 5))

    base = _random_full_row_rank(p, n)
    selector = _random_row_rank_matrix(q, p, rank_target=q)
    target = selector @ base

    a_shared = _random_invertible(p)
    contexts_good = [a_shared @ base for _ in range(k)]
    good_id = f"ao_pair_{pair_id}_good"
    good = _family_metrics(good_id, "paired_shared", target, contexts_good)

    contexts_bad = [_random_invertible(p) @ base for _ in range(k)]
    bad_id = f"ao_pair_{pair_id}_bad"
    bad = _family_metrics(bad_id, "paired_mismatch", target, contexts_bad)
    return good, bad, {good_id: (target.copy(), [m.copy() for m in contexts_good]), bad_id: (target.copy(), [m.copy() for m in contexts_bad])}


def _extra_family(fid: int) -> tuple[dict, tuple[np.ndarray, list[np.ndarray]]]:
    n = int(RNG.integers(6, 10))
    p = int(RNG.integers(3, 6))
    q = int(RNG.integers(2, min(4, p + 1)))
    k = int(RNG.integers(2, 5))

    target = _random_full_row_rank(q, n)
    mode = str(RNG.choice(["random_mixed", "random_local_candidate", "rank_limited"], p=[0.45, 0.40, 0.15]))

    contexts: list[np.ndarray] = []
    if mode == "random_local_candidate":
        # Guarantee local exactness by embedding target rows plus context-specific nuisance rows.
        for _ in range(k):
            nuisance = _random_full_row_rank(max(1, p - q), n)
            context = np.vstack([target, nuisance])[:p]
            contexts.append(context)
    elif mode == "rank_limited":
        rank_target = int(RNG.integers(1, p))
        for _ in range(k):
            contexts.append(_random_row_rank_matrix(p, n, rank_target=rank_target))
    else:
        for _ in range(k):
            contexts.append(_random_full_row_rank(p, n))

    fam_id = f"ao_extra_{fid}"
    return _family_metrics(fam_id, mode, target, contexts), (target, contexts)


def _build_operator_catalog(
    *,
    pair_count: int,
    extra_count: int,
) -> tuple[list[dict], list[dict], dict[str, tuple[np.ndarray, list[np.ndarray]]]]:
    rows: list[dict] = []
    rows_map: dict[str, tuple[np.ndarray, list[np.ndarray]]] = {}
    for pair_id in range(pair_count):
        good, bad, pair_map = _latent_pair(pair_id)
        rows.extend([good, bad])
        rows_map.update(pair_map)
    for extra_id in range(extra_count):
        row, payload = _extra_family(extra_id)
        rows.append(row)
        rows_map[row["family_id"]] = (payload[0].copy(), [m.copy() for m in payload[1]])

    anomalies: list[dict] = []
    aidx = 0

    by_sig: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_sig[str(row["descriptor_signature"])].append(row)

    for signature, group in by_sig.items():
        values = {int(item["invariant_exact_direct"]) for item in group}
        if len(values) > 1 and len(group) >= 2:
            anomalies.append(
                {
                    "anomaly_id": f"aop_{aidx}",
                    "anomaly_type": "same_descriptor_opposite_invariant_verdict",
                    "descriptor_signature": signature,
                    "evidence_families": ";".join(item["family_id"] for item in group[:12]),
                    "count": int(len(group)),
                    "status": "PROVED ON SUPPORTED FAMILY",
                    "notes": "descriptor-only summaries fail again under agreement-operator diagnostics",
                }
            )
            aidx += 1

    for row in rows:
        if row["restricted_aug_threshold"] != "" and int(row["restricted_aug_threshold"]) > int(row["free_aug_threshold"]):
            anomalies.append(
                {
                    "anomaly_id": f"aop_{aidx}",
                    "anomaly_type": "restricted_augmentation_gap",
                    "descriptor_signature": row["descriptor_signature"],
                    "evidence_families": row["family_id"],
                    "count": 1,
                    "status": "PROVED ON SUPPORTED FAMILY",
                    "notes": "restricted candidate libraries can overestimate true free augmentation threshold",
                }
            )
            aidx += 1

    for row in rows:
        if int(row["library_target_defect"]) > 0:
            anomalies.append(
                {
                    "anomaly_id": f"aop_{aidx}",
                    "anomaly_type": "candidate_library_defect_impossibility",
                    "descriptor_signature": row["descriptor_signature"],
                    "evidence_families": row["family_id"],
                    "count": 1,
                    "status": "PROVED ON SUPPORTED FAMILY",
                    "notes": "positive library defect forbids exact shared recovery for this candidate row library",
                }
            )
            aidx += 1

    for row in rows:
        if int(row["library_rank_gain"]) >= int(row["free_aug_threshold"]) and int(row["library_target_defect"]) > 0:
            anomalies.append(
                {
                    "anomaly_id": f"aop_{aidx}",
                    "anomaly_type": "library_gain_not_sufficient",
                    "descriptor_signature": row["descriptor_signature"],
                    "evidence_families": row["family_id"],
                    "count": 1,
                    "status": "PROVED ON SUPPORTED FAMILY",
                    "notes": "candidate rank gain can match free threshold and still fail due alignment defect",
                }
            )
            aidx += 1

    return rows, anomalies, rows_map


def _formation_transform(mode: str, contexts: Sequence[np.ndarray], target: np.ndarray) -> list[np.ndarray]:
    transformed = [matrix.copy() for matrix in contexts]
    p, n = contexts[0].shape
    if mode == "constraint_generation":
        shared = _random_full_row_rank(1, n)
        transformed = [np.vstack([matrix, shared]) for matrix in transformed]
    elif mode == "context_drift":
        transformed = [matrix + float(RNG.uniform(0.02, 0.15)) * RNG.normal(size=matrix.shape) for matrix in transformed]
    elif mode == "intervention_cleaning":
        a_clean = _random_invertible(p)
        transformed = [a_clean @ matrix for matrix in transformed]
    elif mode == "optimization_induced":
        for idx, matrix in enumerate(transformed):
            scale = float(RNG.uniform(0.5, 2.0))
            transformed[idx] = np.vstack([scale * matrix[0], *matrix[1:]])
    elif mode == "context_conditioned_differentiation":
        for idx, matrix in enumerate(transformed):
            noise = float(0.1 + 0.05 * idx) * RNG.normal(size=matrix.shape)
            transformed[idx] = matrix + noise
    else:
        transformed = [matrix + 0.03 * RNG.normal(size=matrix.shape) for matrix in transformed]
    return transformed


def _build_formation_bridge_rows(
    operator_rows: Sequence[dict],
    rows_map: dict[str, tuple[np.ndarray, list[np.ndarray]]],
    *,
    bridge_count: int,
) -> tuple[list[dict], dict]:
    mechanisms = [
        "constraint_generation",
        "context_drift",
        "intervention_cleaning",
        "optimization_induced",
        "context_conditioned_differentiation",
    ]
    rows: list[dict] = []

    selected_ids = [row["family_id"] for row in operator_rows[:bridge_count]]
    for idx, family_id in enumerate(selected_ids):
        target, contexts = rows_map[family_id]
        mechanism = mechanisms[idx % len(mechanisms)]

        pre = _family_metrics(f"{family_id}_pre", f"bridge_pre_{mechanism}", target, contexts)
        post_contexts = _formation_transform(mechanism, contexts, target)
        post = _family_metrics(f"{family_id}_post", f"bridge_post_{mechanism}", target, post_contexts)

        rows.append(
            {
                "bridge_case_id": f"fdeep_{idx}",
                "source_family_id": family_id,
                "mechanism": mechanism,
                "pre_local_exact": pre["local_exact_all"],
                "pre_invariant_exact": pre["invariant_exact_direct"],
                "post_local_exact": post["local_exact_all"],
                "post_invariant_exact": post["invariant_exact_direct"],
                "pre_lifted_residual_norm": pre["lifted_residual_norm"],
                "post_lifted_residual_norm": post["lifted_residual_norm"],
                "pre_free_aug_threshold": pre["free_aug_threshold"],
                "post_free_aug_threshold": post["free_aug_threshold"],
                "pre_restricted_aug_threshold": pre["restricted_aug_threshold"],
                "post_restricted_aug_threshold": post["restricted_aug_threshold"],
                "local_gain_shared_loss_flag": int(
                    int(post["local_exact_all"]) > int(pre["local_exact_all"])
                    and int(post["invariant_exact_direct"]) < int(pre["invariant_exact_direct"])
                ),
                "threshold_worsened_flag": int(int(post["free_aug_threshold"]) > int(pre["free_aug_threshold"])),
                "threshold_improved_flag": int(int(post["free_aug_threshold"]) < int(pre["free_aug_threshold"])),
                "notes": "EXPLORATION / NON-PROMOTED",
            }
        )

    summary = {
        "seed": SEED,
        "bridge_rows": len(rows),
        "mechanism_counts": dict(Counter(row["mechanism"] for row in rows)),
        "local_gain_shared_loss_count": int(sum(row["local_gain_shared_loss_flag"] for row in rows)),
        "threshold_worsened_count": int(sum(row["threshold_worsened_flag"] for row in rows)),
        "threshold_improved_count": int(sum(row["threshold_improved_flag"] for row in rows)),
        "post_local_not_shared_count": int(
            sum(int(row["post_local_exact"]) == 1 and int(row["post_invariant_exact"]) == 0 for row in rows)
        ),
        "status": "EXPLORATION / NON-PROMOTED",
    }
    return rows, summary


def _write_csv(path: Path, rows: Sequence[dict], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(fieldnames))
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(description="Deep continuation operator + formation pass")
    parser.add_argument("--pair-count", type=int, default=140)
    parser.add_argument("--extra-count", type=int, default=180)
    parser.add_argument("--bridge-count", type=int, default=260)
    args = parser.parse_args()

    operator_rows, operator_anomalies, rows_map = _build_operator_catalog(
        pair_count=args.pair_count,
        extra_count=args.extra_count,
    )

    bridge_rows, bridge_summary = _build_formation_bridge_rows(
        operator_rows,
        rows_map,
        bridge_count=args.bridge_count,
    )

    _write_csv(
        OUT_CTX / "agreement_operator_witness_catalog.csv",
        operator_rows,
        [
            "family_id",
            "mode",
            "n",
            "p_record",
            "q_target",
            "k_contexts",
            "descriptor_signature",
            "local_exact_all",
            "invariant_exact_direct",
            "invariant_exact_agreement",
            "lift_direct_consistent",
            "agreement_basis_dim",
            "lifted_rank",
            "lifted_residual_norm",
            "stack_residual_norm",
            "stack_alignment",
            "free_aug_threshold",
            "restricted_aug_threshold",
            "restricted_aug_found",
            "free_aug_constructed_exact",
            "candidate_count",
            "library_rank_gain",
            "library_target_defect",
            "library_full_pool_feasible",
            "library_full_pool_exact",
            "library_search_limit",
            "library_found_within_limit",
            "notes",
        ],
    )
    _write_csv(
        OUT_CTX / "agreement_operator_anomaly_catalog.csv",
        operator_anomalies,
        [
            "anomaly_id",
            "anomaly_type",
            "descriptor_signature",
            "evidence_families",
            "count",
            "status",
            "notes",
        ],
    )
    _write_csv(
        OUT_SFPR / "formation_deep_bridge_catalog.csv",
        bridge_rows,
        [
            "bridge_case_id",
            "source_family_id",
            "mechanism",
            "pre_local_exact",
            "pre_invariant_exact",
            "post_local_exact",
            "post_invariant_exact",
            "pre_lifted_residual_norm",
            "post_lifted_residual_norm",
            "pre_free_aug_threshold",
            "post_free_aug_threshold",
            "pre_restricted_aug_threshold",
            "post_restricted_aug_threshold",
            "local_gain_shared_loss_flag",
            "threshold_worsened_flag",
            "threshold_improved_flag",
            "notes",
        ],
    )

    summary = {
        "seed": SEED,
        "operator_witness_rows": len(operator_rows),
        "operator_anomaly_rows": len(operator_anomalies),
        "lift_direct_consistent_count": int(sum(int(row["lift_direct_consistent"]) for row in operator_rows)),
        "same_descriptor_opposite_count": int(
            sum(1 for anomaly in operator_anomalies if anomaly["anomaly_type"] == "same_descriptor_opposite_invariant_verdict")
        ),
        "restricted_gap_count": int(
            sum(1 for anomaly in operator_anomalies if anomaly["anomaly_type"] == "restricted_augmentation_gap")
        ),
        "library_defect_count": int(
            sum(1 for anomaly in operator_anomalies if anomaly["anomaly_type"] == "candidate_library_defect_impossibility")
        ),
        "library_gain_not_sufficient_count": int(
            sum(1 for anomaly in operator_anomalies if anomaly["anomaly_type"] == "library_gain_not_sufficient")
        ),
        "formation_bridge_summary": bridge_summary,
        "status": "EXPLORATION / NON-PROMOTED",
    }
    with (OUT_SFPR / "formation_deep_bridge_summary.json").open("w") as f:
        json.dump(summary, f, indent=2)

    print(f"wrote {OUT_CTX / 'agreement_operator_witness_catalog.csv'} ({len(operator_rows)} rows)")
    print(f"wrote {OUT_CTX / 'agreement_operator_anomaly_catalog.csv'} ({len(operator_anomalies)} rows)")
    print(f"wrote {OUT_SFPR / 'formation_deep_bridge_catalog.csv'} ({len(bridge_rows)} rows)")
    print(f"wrote {OUT_SFPR / 'formation_deep_bridge_summary.json'}")


if __name__ == "__main__":
    main()
