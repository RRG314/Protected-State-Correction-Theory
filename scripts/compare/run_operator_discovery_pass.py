#!/usr/bin/env python3
"""Theorem/operator discovery pass for context-sensitive recoverability.

Produces:
- data/generated/operator_discovery/operator_witness_catalog.csv
- data/generated/operator_discovery/operator_anomaly_catalog.csv
"""
from __future__ import annotations

import csv
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np

SEED = 20260418
RNG = np.random.default_rng(SEED)
TOL = 1e-8

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "generated" / "operator_discovery"
OUT.mkdir(parents=True, exist_ok=True)


def matrix_rank(m: np.ndarray, tol: float = TOL) -> int:
    return int(np.linalg.matrix_rank(m, tol))


def rowspace_basis(m: np.ndarray, tol: float = TOL) -> np.ndarray:
    if m.size == 0:
        return np.zeros((0, m.shape[1]))
    _, s, vh = np.linalg.svd(m, full_matrices=False)
    r = int(np.sum(s > tol))
    return vh[:r]


def rowspace_residual(tau: np.ndarray, m: np.ndarray) -> float:
    b = rowspace_basis(m)
    if b.shape[0] == 0:
        return float(np.linalg.norm(tau))
    proj = tau @ b.T @ b
    return float(np.linalg.norm(tau - proj))


def exact_recoverable(tau: np.ndarray, m: np.ndarray, tol: float = 1e-7) -> bool:
    return rowspace_residual(tau, m) <= tol


def local_exact_all(tau: np.ndarray, contexts: Sequence[np.ndarray], tol: float = 1e-7) -> bool:
    return all(exact_recoverable(tau, m, tol=tol) for m in contexts)


def shared_decoder_residual(tau: np.ndarray, contexts: Sequence[np.ndarray]) -> float:
    a = np.vstack([m.T for m in contexts])
    b = np.concatenate([tau for _ in contexts])
    d, *_ = np.linalg.lstsq(a, b, rcond=None)
    return float(max(np.linalg.norm(d @ m - tau) for m in contexts))


def shared_exact(tau: np.ndarray, contexts: Sequence[np.ndarray], tol: float = 1e-7) -> bool:
    return shared_decoder_residual(tau, contexts) <= tol


def context_lift_sigma_min(contexts: Sequence[np.ndarray]) -> float:
    a = np.vstack([m.T for m in contexts])
    s = np.linalg.svd(a, compute_uv=False)
    return float(np.min(s)) if s.size else 0.0


def all_binary_states(n: int) -> np.ndarray:
    return np.array(list(itertools.product([0.0, 1.0], repeat=n)), dtype=float)


def cci(tau: np.ndarray, m: np.ndarray, states: np.ndarray) -> float:
    """Collapse/collision index on stacked records.

    Fraction of target-disagreeing pairs among record-colliding pairs.
    """
    fibers: Dict[Tuple[float, ...], List[float]] = defaultdict(list)
    for x in states:
        y = tuple(np.round(m @ x, 8).tolist())
        t = float(np.round(tau @ x, 8))
        fibers[y].append(t)

    total = 0
    diff = 0
    for vals in fibers.values():
        if len(vals) < 2:
            continue
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                total += 1
                if vals[i] != vals[j]:
                    diff += 1
    return 0.0 if total == 0 else float(diff / total)


def random_tau(n: int) -> np.ndarray:
    while True:
        t = RNG.integers(-3, 4, size=n).astype(float)
        if np.linalg.norm(t) > 0:
            return t


def random_nonparallel(tau: np.ndarray) -> np.ndarray:
    n = tau.shape[0]
    while True:
        u = random_tau(n)
        c = abs(float(np.dot(tau, u))) / (np.linalg.norm(tau) * np.linalg.norm(u) + 1e-12)
        if c < 0.95:
            return u


def random_matrix(rows: int, cols: int, low: int = -2, high: int = 3) -> np.ndarray:
    while True:
        m = RNG.integers(low, high, size=(rows, cols)).astype(float)
        if np.any(np.abs(m) > 0):
            return m


def descriptor_sig(n: int, k: int, m: int, rank_stack: int, budget: int) -> str:
    return f"n{n}|k{k}|m{m}|r{rank_stack}|b{budget}"


def candidate_shared_rows(tau: np.ndarray, contexts: Sequence[np.ndarray]) -> List[np.ndarray]:
    n = tau.shape[0]
    pool: List[np.ndarray] = []
    # basis-library rows
    for i in range(min(n, 3)):
        e = np.zeros(n)
        e[i] = 1.0
        pool.append(e)
    # context rows and combinations
    stacked = np.vstack(contexts)
    for i in range(min(4, stacked.shape[0])):
        pool.append(stacked[i])
    for i in range(min(2, stacked.shape[0])):
        for j in range(i + 1, min(4, stacked.shape[0])):
            pool.append(stacked[i] + stacked[j])
            pool.append(stacked[i] - stacked[j])

    uniq: List[np.ndarray] = []
    for v in pool:
        if np.linalg.norm(v) <= TOL:
            continue
        fresh = True
        for u in uniq:
            if np.linalg.norm(v - u) <= 1e-10:
                fresh = False
                break
        if fresh:
            uniq.append(v)
    return uniq


def minimal_shared_aug(
    tau: np.ndarray,
    contexts: Sequence[np.ndarray],
    max_rows: int = 2,
) -> Tuple[Optional[int], Optional[np.ndarray], Optional[float], Optional[float]]:
    if shared_exact(tau, contexts):
        return 0, np.zeros((0, tau.shape[0])), 0.0, shared_decoder_residual(tau, contexts)

    base_cid = shared_decoder_residual(tau, contexts)
    pool = candidate_shared_rows(tau, contexts)
    idxs = list(range(len(pool)))

    best_res = None
    best_u = None
    best_r = None
    for r in range(1, max_rows + 1):
        for comb in itertools.combinations(idxs, r):
            u = np.vstack([pool[i] for i in comb])
            aug_contexts = [np.vstack([m, u]) for m in contexts]
            res = shared_decoder_residual(tau, aug_contexts)
            if best_res is None or res < best_res:
                best_res = res
                best_u = u
                best_r = r
            if res <= 1e-7:
                return r, u, res, base_cid - res

    if best_r is None or best_u is None or best_res is None:
        return None, None, None, None
    return None, best_u, best_res, base_cid - best_res


def generate_family(fid: int) -> dict:
    n = int(RNG.integers(4, 8))
    k = int(RNG.integers(2, 6))
    m = 2
    tau = random_tau(n)
    u = random_nonparallel(tau)

    mode = RNG.choice(
        [
            "shared_exact",
            "local_only",
            "mixed_random",
            "drift_prone",
            "redundant",
            "geometry_split",
        ],
        p=[0.24, 0.30, 0.20, 0.10, 0.10, 0.06],
    )

    contexts: List[np.ndarray] = []

    if mode == "shared_exact":
        v = random_nonparallel(tau)
        a0 = int(RNG.integers(-2, 3))
        for _ in range(k):
            contexts.append(np.vstack([tau + a0 * u, v]))
    elif mode == "local_only":
        for _ in range(k):
            uc = random_nonparallel(tau)
            a = int(RNG.integers(-3, 4)) or 1
            contexts.append(np.vstack([tau + a * uc, uc]))
    elif mode == "drift_prone":
        v = random_nonparallel(tau)
        a0 = int(RNG.integers(-2, 3))
        for _ in range(k):
            eps = float(RNG.uniform(5e-4, 8e-2))
            noise = eps * RNG.normal(size=tau.shape[0])
            contexts.append(np.vstack([tau + a0 * u + noise, v + noise]))
    elif mode == "redundant":
        base = np.vstack([u, 2.0 * u])
        for _ in range(k):
            contexts.append(base.copy())
    elif mode == "geometry_split":
        # same rank/count style but with aligned vs misaligned geometry blocks
        v = random_nonparallel(tau)
        w = random_nonparallel(tau)
        contexts.append(np.vstack([tau + v, v]))
        contexts.append(np.vstack([w, 2.0 * w]))
        while len(contexts) < k:
            contexts.append(np.vstack([tau + random_nonparallel(tau), random_nonparallel(tau)]))
    else:
        for _ in range(k):
            contexts.append(random_matrix(m, n))

    stack = np.vstack(contexts)
    rank_stack = matrix_rank(stack)
    budget = k * m

    states = all_binary_states(min(n, 7))
    if n > 7:
        states = RNG.integers(0, 2, size=(128, n)).astype(float)

    loc = local_exact_all(tau, contexts)
    inv = shared_exact(tau, contexts)
    cid = shared_decoder_residual(tau, contexts)

    cle_res = cid  # context-lifted equation residual (same solvability object)
    cle_ok = int(cle_res <= 1e-7)

    aug_thr, aug_u, aug_res, aug_gain = minimal_shared_aug(tau, contexts, max_rows=2)
    cid_after = "" if aug_res is None else float(aug_res)

    projection_stack = rowspace_residual(tau, stack)
    projection_mean_ctx = float(np.mean([rowspace_residual(tau, m_) for m_ in contexts]))

    return {
        "case_id": f"op_{fid}",
        "mode": mode,
        "n": n,
        "k_contexts": k,
        "m_per_context": m,
        "total_budget": budget,
        "stack_rank": rank_stack,
        "descriptor_signature": descriptor_sig(n, k, m, rank_stack, budget),
        "local_exact_all": int(loc),
        "invariant_exact": int(inv),
        "cid": float(cid),
        "cle_residual": float(cle_res),
        "cle_solved": cle_ok,
        "sigma_min_lift": context_lift_sigma_min(contexts),
        "collapse_index": cci(tau, stack, states),
        "stack_residual": float(projection_stack),
        "stack_alignment": float(max(0.0, 1.0 - projection_stack / (np.linalg.norm(tau) + 1e-12))),
        "shared_aug_threshold": "" if aug_thr is None else int(aug_thr),
        "shared_aug_found": int(aug_thr is not None),
        "cid_after_aug": cid_after,
        "augmentation_gain": "" if aug_gain is None else float(aug_gain),
        "projection_stack_residual": float(projection_stack),
        "projection_mean_context_residual": float(projection_mean_ctx),
        "projection_gain": float(projection_mean_ctx - projection_stack),
        "operator_status": "VALIDATED / EMPIRICAL ONLY",
        "operator_novelty": "REDUCES TO EXISTING OCP LOGIC",
        "notes": "CID/CLE/aug functional are useful but largely compatibility reformulations",
    }


def build_anomalies(rows: Sequence[dict]) -> List[dict]:
    anomalies: List[dict] = []
    idx = 0

    by_sig = defaultdict(list)
    for r in rows:
        by_sig[r["descriptor_signature"]].append(r)

    # A1: same descriptor opposite invariant verdict
    for sig, group in by_sig.items():
        vals = {int(g["invariant_exact"]) for g in group}
        if len(vals) > 1:
            anomalies.append(
                {
                    "anomaly_id": f"op_a_{idx}",
                    "anomaly_type": "same_descriptor_opposite_invariant_verdict",
                    "descriptor_signature": sig,
                    "evidence_cases": ";".join(g["case_id"] for g in group[:10]),
                    "count": len(group),
                    "why_it_matters": "rank/count/budget signature does not classify invariant exactness",
                    "status": "PROVED ON SUPPORTED FAMILY",
                    "notes": "anti-classifier persists under operator diagnostics",
                }
            )
            idx += 1

    # A2: projection blind spot: stack residual ~0 but invariant fails
    p_blind = [
        r for r in rows
        if float(r["projection_stack_residual"]) <= 1e-7 and int(r["invariant_exact"]) == 0
    ]
    if p_blind:
        anomalies.append(
            {
                "anomaly_id": f"op_a_{idx}",
                "anomaly_type": "projection_succeeds_but_shared_decoder_fails",
                "descriptor_signature": "mixed",
                "evidence_cases": ";".join(r["case_id"] for r in p_blind[:20]),
                "count": len(p_blind),
                "why_it_matters": "stack row-space inclusion is insufficient for context-invariant exactness",
                "status": "PROVED ON SUPPORTED FAMILY",
                "notes": "supports conditioned-vs-invariant split",
            }
        )
        idx += 1

    # A3: positive augmentation gain from local-exact/global-fail
    aug_gain = [
        r for r in rows
        if int(r["local_exact_all"]) == 1 and int(r["invariant_exact"]) == 0 and r["augmentation_gain"] != "" and float(r["augmentation_gain"]) > 1e-7
    ]
    if aug_gain:
        anomalies.append(
            {
                "anomaly_id": f"op_a_{idx}",
                "anomaly_type": "positive_augmentation_gain",
                "descriptor_signature": "mixed",
                "evidence_cases": ";".join(r["case_id"] for r in aug_gain[:20]),
                "count": len(aug_gain),
                "why_it_matters": "minimal shared augmentation materially improves compatibility defect",
                "status": "PROVED ON SUPPORTED FAMILY",
                "notes": "candidate augmentation operator is computationally useful",
            }
        )
        idx += 1

    # A4: sigma-min non-predictive split
    # bucket by rounded sigma and descriptor
    bucket = defaultdict(list)
    for r in rows:
        key = (r["descriptor_signature"], round(float(r["sigma_min_lift"]), 2))
        bucket[key].append(r)
    sigma_split = []
    for _, group in bucket.items():
        vals = {int(g["invariant_exact"]) for g in group}
        if len(vals) > 1 and len(group) >= 2:
            sigma_split.extend(group)
    if sigma_split:
        anomalies.append(
            {
                "anomaly_id": f"op_a_{idx}",
                "anomaly_type": "lift_conditioning_not_sufficient",
                "descriptor_signature": "mixed",
                "evidence_cases": ";".join(r["case_id"] for r in sigma_split[:20]),
                "count": len(sigma_split),
                "why_it_matters": "numerical conditioning alone does not determine shared exactness",
                "status": "VALIDATED / EMPIRICAL ONLY",
                "notes": "conditioning is diagnostic, not classifier",
            }
        )
        idx += 1

    return anomalies


def write_csv(path: Path, rows: Sequence[dict], fieldnames: Sequence[str]) -> None:
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames))
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main() -> None:
    rows = [generate_family(i) for i in range(1000)]
    anomalies = build_anomalies(rows)

    write_csv(
        OUT / "operator_witness_catalog.csv",
        rows,
        [
            "case_id",
            "mode",
            "n",
            "k_contexts",
            "m_per_context",
            "total_budget",
            "stack_rank",
            "descriptor_signature",
            "local_exact_all",
            "invariant_exact",
            "cid",
            "cle_residual",
            "cle_solved",
            "sigma_min_lift",
            "collapse_index",
            "stack_residual",
            "stack_alignment",
            "shared_aug_threshold",
            "shared_aug_found",
            "cid_after_aug",
            "augmentation_gain",
            "projection_stack_residual",
            "projection_mean_context_residual",
            "projection_gain",
            "operator_status",
            "operator_novelty",
            "notes",
        ],
    )

    write_csv(
        OUT / "operator_anomaly_catalog.csv",
        anomalies,
        [
            "anomaly_id",
            "anomaly_type",
            "descriptor_signature",
            "evidence_cases",
            "count",
            "why_it_matters",
            "status",
            "notes",
        ],
    )

    summary = {
        "seed": SEED,
        "witness_rows": len(rows),
        "anomaly_rows": len(anomalies),
        "invariant_exact_count": int(sum(int(r["invariant_exact"]) for r in rows)),
        "local_exact_global_fail_count": int(sum(int(r["local_exact_all"]) == 1 and int(r["invariant_exact"]) == 0 for r in rows)),
        "same_descriptor_groups": int(sum(1 for a in anomalies if a["anomaly_type"] == "same_descriptor_opposite_invariant_verdict")),
        "mode_counts": dict(Counter(r["mode"] for r in rows)),
    }
    with (OUT / "summary.json").open("w") as f:
        json.dump(summary, f, indent=2)

    print(f"wrote {OUT / 'operator_witness_catalog.csv'} ({len(rows)} rows)")
    print(f"wrote {OUT / 'operator_anomaly_catalog.csv'} ({len(anomalies)} rows)")
    print(f"wrote {OUT / 'summary.json'}")


if __name__ == "__main__":
    main()
