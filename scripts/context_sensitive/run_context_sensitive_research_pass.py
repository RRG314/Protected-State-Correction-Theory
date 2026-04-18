#!/usr/bin/env python3
"""Focused research generator for context-sensitive recoverability next phase.

Main track:
- conditioned vs invariant split
- shared augmentation threshold
- multicontext opposite-verdict families

Secondary track:
- formation mechanisms (exploratory, non-promoted)
"""
from __future__ import annotations

import csv
import itertools
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

SEED = 20260418
RNG = np.random.default_rng(SEED)
TOL = 1e-8

ROOT = Path(__file__).resolve().parents[2]
OUT_MAIN = ROOT / "data" / "generated" / "context_sensitive_recoverability"
OUT_MAIN.mkdir(parents=True, exist_ok=True)
OUT_SFPR = ROOT / "data" / "generated" / "sfpr"
OUT_SFPR.mkdir(parents=True, exist_ok=True)


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


def alignment(tau: np.ndarray, m: np.ndarray) -> float:
    denom = float(np.linalg.norm(tau))
    if denom <= TOL:
        return 1.0
    return float(max(0.0, 1.0 - rowspace_residual(tau, m) / denom))


def exact_recoverable(tau: np.ndarray, m: np.ndarray, tol: float = 1e-7) -> bool:
    return rowspace_residual(tau, m) <= tol


def shared_decoder_residual(tau: np.ndarray, contexts: Sequence[np.ndarray]) -> float:
    """Shared decoder d such that d M_c = tau for each context c.

    Requires fixed measurement width per context (same m rows), as in this pass.
    """
    a_blocks = [m.T for m in contexts]
    b = np.concatenate([tau for _ in contexts])
    a = np.vstack(a_blocks)
    d, *_ = np.linalg.lstsq(a, b, rcond=None)
    residuals = [float(np.linalg.norm(d @ m - tau)) for m in contexts]
    return float(max(residuals))


def shared_exact(tau: np.ndarray, contexts: Sequence[np.ndarray], tol: float = 1e-7) -> bool:
    return shared_decoder_residual(tau, contexts) <= tol


def local_exact_all(tau: np.ndarray, contexts: Sequence[np.ndarray], tol: float = 1e-7) -> bool:
    return all(exact_recoverable(tau, m, tol=tol) for m in contexts)


def all_binary_states(n: int) -> np.ndarray:
    return np.array(list(itertools.product([0.0, 1.0], repeat=n)), dtype=float)


def dls(tau: np.ndarray, m: np.ndarray, states: np.ndarray) -> float:
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
    return 0.0 if total == 0 else diff / total


def logdet_info(m: np.ndarray) -> float:
    gram = m @ m.T + 1e-8 * np.eye(m.shape[0])
    sign, val = np.linalg.slogdet(gram)
    return float(val) if sign > 0 else float("-inf")


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


def candidate_shared_rows(tau: np.ndarray, contexts: Sequence[np.ndarray], max_rows: int = 3) -> List[np.ndarray]:
    """Build candidate pool for augmentation search.

    Deliberately excludes direct target-row injection to avoid trivial thresholds.
    """
    n = tau.shape[0]
    pool: List[np.ndarray] = []
    for i in range(min(n, 4)):
        e = np.zeros(n)
        e[i] = 1.0
        pool.append(e)
    # add averaged nuisance rows from contexts
    stacked = np.vstack(contexts)
    for i in range(min(6, stacked.shape[0])):
        pool.append(stacked[i])
    # add linear combinations of context rows (measurement-library style, still no direct tau row)
    for i in range(min(3, stacked.shape[0])):
        for j in range(i + 1, min(5, stacked.shape[0])):
            pool.append(stacked[i] + stacked[j])
            pool.append(stacked[i] - stacked[j])
    # dedupe
    uniq: List[np.ndarray] = []
    for v in pool:
        if np.linalg.norm(v) <= TOL:
            continue
        is_new = True
        for u in uniq:
            if np.linalg.norm(v - u) <= 1e-10:
                is_new = False
                break
        if is_new:
            uniq.append(v)
    return uniq


def minimal_shared_augmentation_threshold(
    tau: np.ndarray,
    contexts: Sequence[np.ndarray],
    max_rows: int = 4,
) -> Tuple[Optional[int], Optional[np.ndarray], Optional[float]]:
    """Return minimal shared rows added to each context to achieve shared exactness."""
    if shared_exact(tau, contexts):
        return 0, np.zeros((0, tau.shape[0])), 0.0

    pool = candidate_shared_rows(tau, contexts, max_rows=max_rows)
    idxs = list(range(len(pool)))

    for r in range(1, max_rows + 1):
        best = None
        best_res = None
        for comb in itertools.combinations(idxs, r):
            u = np.vstack([pool[i] for i in comb])
            aug_contexts = [np.vstack([m, u]) for m in contexts]
            res = shared_decoder_residual(tau, aug_contexts)
            if best_res is None or res < best_res:
                best_res = res
                best = u
            if res <= 1e-7:
                return r, u, res
        # if no exact at this r, continue
    return None, None, None


@dataclass
class ContextFamily:
    family_id: str
    mode: str
    n: int
    k: int
    m: int
    tau: np.ndarray
    contexts: List[np.ndarray]


def build_context_family(fid: int) -> ContextFamily:
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
            "redundant_measurement",
        ],
        p=[0.30, 0.30, 0.20, 0.10, 0.10],
    )

    contexts: List[np.ndarray] = []

    if mode == "shared_exact":
        # Same context geometry across c -> shared decoder exists.
        a0 = int(RNG.integers(-2, 3))
        v = random_nonparallel(tau)
        for _ in range(k):
            contexts.append(np.vstack([tau + a0 * u, v]))
    elif mode == "local_only":
        # Each context individually exact, but coefficients vary so no shared decoder.
        coeffs = [int(RNG.integers(-3, 4)) or 1 for _ in range(k)]
        for a in coeffs:
            uc = random_nonparallel(tau)
            contexts.append(np.vstack([tau + a * uc, uc]))
    elif mode == "drift_prone":
        # Start near shared-exact but with small context-dependent drift.
        v = random_nonparallel(tau)
        a0 = int(RNG.integers(-2, 3))
        for _ in range(k):
            eps = float(RNG.uniform(1e-3, 8e-2))
            noise = eps * RNG.normal(size=tau.shape[0])
            contexts.append(np.vstack([tau + a0 * u + noise, v + noise]))
    elif mode == "redundant_measurement":
        # High redundancy; often same descriptor as informative families but opposite verdict.
        base = np.vstack([u, 2.0 * u])
        for _ in range(k):
            contexts.append(base.copy())
    else:
        for _ in range(k):
            contexts.append(random_matrix(m, n))

    return ContextFamily(
        family_id=f"ctxfam_{fid}",
        mode=mode,
        n=n,
        k=k,
        m=m,
        tau=tau,
        contexts=contexts,
    )


def generate_extra_context(cf: ContextFamily) -> np.ndarray:
    n = cf.n
    tau = cf.tau
    u = random_nonparallel(tau)
    if cf.mode == "shared_exact":
        # Preserve compatible geometry often.
        v = random_nonparallel(tau)
        a = int(RNG.integers(-2, 3))
        return np.vstack([tau + a * u, v])
    if cf.mode == "local_only":
        # Add locally exact but potentially incompatible context.
        a = int(RNG.integers(-3, 4)) or 1
        return np.vstack([tau + a * u, u])
    if cf.mode == "drift_prone":
        v = random_nonparallel(tau)
        eps = float(RNG.uniform(1e-3, 8e-2))
        noise = eps * RNG.normal(size=tau.shape[0])
        return np.vstack([tau + u + noise, v + noise])
    if cf.mode == "redundant_measurement":
        return np.vstack([u, 2.0 * u])
    return random_matrix(cf.m, n)


def compute_family_record(cf: ContextFamily) -> dict:
    stack = np.vstack(cf.contexts)
    states = all_binary_states(min(cf.n, 7))
    if cf.n > 7:
        states = RNG.integers(0, 2, size=(128, cf.n)).astype(float)

    loc_exact = local_exact_all(cf.tau, cf.contexts)
    sh_exact = shared_exact(cf.tau, cf.contexts)
    cid = shared_decoder_residual(cf.tau, cf.contexts)

    # Family enlargement test: append one context.
    extra = generate_extra_context(cf)
    enlarged_contexts = list(cf.contexts) + [extra]
    enlarged_shared = shared_exact(cf.tau, enlarged_contexts)
    enlarged_local = local_exact_all(cf.tau, enlarged_contexts)

    rank_stack = matrix_rank(stack)
    budget = cf.k * cf.m

    dls_vals = [dls(cf.tau, m, states) for m in cf.contexts]
    dls_joint = dls(cf.tau, stack, states)

    thr, u_rows, thr_res = minimal_shared_augmentation_threshold(cf.tau, cf.contexts, max_rows=4)

    return {
        "family_id": cf.family_id,
        "mode": cf.mode,
        "n": cf.n,
        "k_contexts": cf.k,
        "m_per_context": cf.m,
        "total_budget": budget,
        "stack_rank": rank_stack,
        "descriptor_signature": descriptor_sig(cf.n, cf.k, cf.m, rank_stack, budget),
        "local_exact_all": int(loc_exact),
        "shared_exact": int(sh_exact),
        "context_invariance_gap": int(loc_exact) - int(sh_exact),
        "cid": round(float(cid), 10),
        "mean_local_dls": round(float(np.mean(dls_vals)), 10),
        "joint_dls": round(float(dls_joint), 10),
        "stack_alignment": round(float(alignment(cf.tau, stack)), 10),
        "stack_residual": round(float(rowspace_residual(cf.tau, stack)), 10),
        "stack_logdet_info": round(float(logdet_info(stack)), 10),
        "rank_only_pred_shared": int(rank_stack == cf.n),
        "budget_only_pred_shared": int(budget >= cf.n),
        "enlarged_shared_exact": int(enlarged_shared),
        "enlarged_local_exact_all": int(enlarged_local),
        "enlargement_flip": int(int(enlarged_shared) != int(sh_exact)),
        "shared_aug_threshold": "" if thr is None else int(thr),
        "shared_aug_found": int(thr is not None),
        "shared_aug_rows": "" if u_rows is None else int(u_rows.shape[0]),
        "shared_aug_residual": "" if thr_res is None else round(float(thr_res), 10),
        "notes": "",
    }


def generate_multicontext_catalog(num_families: int = 1800) -> Tuple[List[dict], List[dict], List[dict]]:
    families: List[ContextFamily] = [build_context_family(i) for i in range(num_families)]
    records = [compute_family_record(cf) for cf in families]

    # Augmentation catalog: all local exact + shared fail families and any threshold families.
    aug_rows: List[dict] = []
    for r in records:
        if int(r["local_exact_all"]) == 1 and int(r["shared_exact"]) == 0:
            aug_rows.append(
                {
                    "family_id": r["family_id"],
                    "mode": r["mode"],
                    "descriptor_signature": r["descriptor_signature"],
                    "n": r["n"],
                    "k_contexts": r["k_contexts"],
                    "m_per_context": r["m_per_context"],
                    "total_budget": r["total_budget"],
                    "stack_rank": r["stack_rank"],
                    "local_exact_all": r["local_exact_all"],
                    "shared_exact": r["shared_exact"],
                    "shared_aug_threshold": r["shared_aug_threshold"],
                    "shared_aug_found": r["shared_aug_found"],
                    "context_invariance_gap": r["context_invariance_gap"],
                    "cid": r["cid"],
                    "stack_alignment": r["stack_alignment"],
                    "stack_residual": r["stack_residual"],
                    "notes": "local_exact_global_fail",
                }
            )

    # Multicontext anomaly catalog
    anomalies: List[dict] = []

    # Same descriptor opposite shared verdict
    by_sig = defaultdict(list)
    for r in records:
        by_sig[r["descriptor_signature"]].append(r)

    aidx = 0
    for sig, rows in by_sig.items():
        vals = {int(x["shared_exact"]) for x in rows}
        if len(vals) > 1:
            anomalies.append(
                {
                    "anomaly_id": f"mc_a_{aidx}",
                    "anomaly_type": "same_descriptor_opposite_shared_verdict",
                    "descriptor_signature": sig,
                    "family_count": len(rows),
                    "shared_exact_values": ",".join(str(v) for v in sorted(vals)),
                    "evidence_families": ";".join(x["family_id"] for x in rows[:8]),
                    "severity": "high",
                    "notes": "same rank/count/budget signature with opposite invariant verdict",
                }
            )
            aidx += 1

    # Threshold and drift style anomalies
    for r in records:
        # gap anomaly
        if int(r["local_exact_all"]) == 1 and int(r["shared_exact"]) == 0:
            anomalies.append(
                {
                    "anomaly_id": f"mc_a_{aidx}",
                    "anomaly_type": "conditioned_exact_invariant_fail",
                    "descriptor_signature": r["descriptor_signature"],
                    "family_count": 1,
                    "shared_exact_values": "0",
                    "evidence_families": r["family_id"],
                    "severity": "high",
                    "notes": "context-invariance gap",
                }
            )
            aidx += 1
        if r["shared_aug_found"] == 1 and r["shared_aug_threshold"] not in ("", 0):
            anomalies.append(
                {
                    "anomaly_id": f"mc_a_{aidx}",
                    "anomaly_type": "positive_shared_augmentation_threshold",
                    "descriptor_signature": r["descriptor_signature"],
                    "family_count": 1,
                    "shared_exact_values": str(r["shared_exact"]),
                    "evidence_families": r["family_id"],
                    "severity": "medium",
                    "notes": f"threshold={r['shared_aug_threshold']}",
                }
            )
            aidx += 1
        if int(r["enlargement_flip"]) == 1:
            anomalies.append(
                {
                    "anomaly_id": f"mc_a_{aidx}",
                    "anomaly_type": "family_enlargement_flip",
                    "descriptor_signature": r["descriptor_signature"],
                    "family_count": 1,
                    "shared_exact_values": f"{r['shared_exact']}->{r['enlarged_shared_exact']}",
                    "evidence_families": r["family_id"],
                    "severity": "medium",
                    "notes": "shared verdict changed after adding one context",
                }
            )
            aidx += 1

    return records, aug_rows, anomalies


def write_csv(path: Path, rows: List[dict], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def generate_formation_secondary(num_rows: int = 900) -> List[dict]:
    routes = [
        "constraint_generation",
        "symmetry_breaking",
        "context_conditioned_differentiation",
        "intervention_generated_structure",
        "feedback_induced_structure",
        "local_to_global_organization",
        "optimization_induced_structure",
    ]

    rows: List[dict] = []

    for i in range(num_rows):
        route = routes[i % len(routes)]
        n = int(RNG.integers(4, 8))
        tau = random_tau(n)
        u = random_nonparallel(tau)
        states = all_binary_states(min(n, 7))
        if n > 7:
            states = RNG.integers(0, 2, size=(128, n)).astype(float)

        # two-context setting for bridge tests
        m1_pre = random_matrix(2, n)
        m2_pre = random_matrix(2, n)

        m1_post = m1_pre.copy()
        m2_post = m2_pre.copy()

        if route == "constraint_generation":
            m1_post = np.vstack([m1_pre, tau])
            m2_post = np.vstack([m2_pre, tau])
        elif route == "symmetry_breaking":
            m1_pre = np.vstack([u, -u])
            m2_pre = np.vstack([u, -u])
            m1_post = np.vstack([u, tau + u])
            m2_post = np.vstack([u, tau - u])
        elif route == "context_conditioned_differentiation":
            m1_pre = np.vstack([tau + u, u])
            m2_pre = np.vstack([tau - u, u])
            a = int(RNG.integers(1, 4))
            b = int(RNG.integers(1, 4))
            m1_post = np.vstack([tau + a * u, u])
            m2_post = np.vstack([tau - b * u, u])
        elif route == "intervention_generated_structure":
            conf = random_nonparallel(tau)
            m1_pre = np.vstack([tau + conf, conf])
            m2_pre = np.vstack([tau + conf, random_nonparallel(tau)])
            m1_post = np.vstack([tau, conf])
            m2_post = np.vstack([tau, random_nonparallel(tau)])
        elif route == "feedback_induced_structure":
            step = float(RNG.uniform(0.1, 0.8))
            bias = np.outer(np.ones(2), tau / (np.linalg.norm(tau) + 1e-12))
            m1_post = m1_pre + step * bias
            m2_post = m2_pre + 0.5 * step * bias
        elif route == "local_to_global_organization":
            m1_pre = np.vstack([tau + u, u])
            m2_pre = np.vstack([tau + 2 * u, u])
            m1_post = np.vstack([tau + u, random_nonparallel(tau)])
            m2_post = np.vstack([tau + 2 * u, random_nonparallel(tau)])
        elif route == "optimization_induced_structure":
            pool = random_matrix(7, n)
            # choose post rows by max alignment independently in each context
            best_idx = np.argsort([alignment(tau, np.vstack([pool[a], pool[b]])) for a, b in itertools.combinations(range(7), 2)])
            # simple deterministic selection
            cands = list(itertools.combinations(range(7), 2))
            p1 = cands[best_idx[-1]]
            p2 = cands[best_idx[-2]] if len(best_idx) > 1 else cands[best_idx[-1]]
            m1_post = np.vstack([pool[p1[0]], pool[p1[1]]])
            m2_post = np.vstack([pool[p2[0]], pool[p2[1]]])

        pre_contexts = [m1_pre, m2_pre]
        post_contexts = [m1_post, m2_post]

        pre_local = int(local_exact_all(tau, pre_contexts))
        post_local = int(local_exact_all(tau, post_contexts))
        pre_shared = int(shared_exact(tau, pre_contexts))
        post_shared = int(shared_exact(tau, post_contexts))

        pre_stack = np.vstack(pre_contexts)
        post_stack = np.vstack(post_contexts)

        pre_align = alignment(tau, pre_stack)
        post_align = alignment(tau, post_stack)
        pre_dls = dls(tau, pre_stack, states)
        post_dls = dls(tau, post_stack, states)

        created = int((post_align > pre_align + 1e-7) or (post_dls < pre_dls - 1e-7))

        pre_thr, _, _ = minimal_shared_augmentation_threshold(tau, pre_contexts, max_rows=4)
        post_thr, _, _ = minimal_shared_augmentation_threshold(tau, post_contexts, max_rows=4)

        rows.append(
            {
                "formation_case_id": f"fsec_{i}",
                "mechanism": route,
                "n": n,
                "k_contexts": 2,
                "pre_local_exact": pre_local,
                "pre_shared_exact": pre_shared,
                "post_local_exact": post_local,
                "post_shared_exact": post_shared,
                "pre_context_gap": pre_local - pre_shared,
                "post_context_gap": post_local - post_shared,
                "pre_alignment": round(float(pre_align), 10),
                "post_alignment": round(float(post_align), 10),
                "pre_dls": round(float(pre_dls), 10),
                "post_dls": round(float(post_dls), 10),
                "structure_created_flag": created,
                "recoverability_change_shared": post_shared - pre_shared,
                "recoverability_change_local": post_local - pre_local,
                "pre_shared_aug_threshold": "" if pre_thr is None else int(pre_thr),
                "post_shared_aug_threshold": "" if post_thr is None else int(post_thr),
                "threshold_flip_flag": int((pre_thr is None and post_thr is not None) or (pre_thr is not None and post_thr is not None and pre_thr != post_thr)),
                "notes": "EXPLORATION/NON-PROMOTED",
            }
        )

    return rows


def save_outputs(main_rows: List[dict], aug_rows: List[dict], anomalies: List[dict], formation_rows: List[dict]) -> None:
    write_csv(
        OUT_MAIN / "multicontext_witness_catalog.csv",
        main_rows,
        [
            "family_id",
            "mode",
            "n",
            "k_contexts",
            "m_per_context",
            "total_budget",
            "stack_rank",
            "descriptor_signature",
            "local_exact_all",
            "shared_exact",
            "context_invariance_gap",
            "cid",
            "mean_local_dls",
            "joint_dls",
            "stack_alignment",
            "stack_residual",
            "stack_logdet_info",
            "rank_only_pred_shared",
            "budget_only_pred_shared",
            "enlarged_shared_exact",
            "enlarged_local_exact_all",
            "enlargement_flip",
            "shared_aug_threshold",
            "shared_aug_found",
            "shared_aug_rows",
            "shared_aug_residual",
            "notes",
        ],
    )

    write_csv(
        OUT_MAIN / "augmentation_threshold_catalog.csv",
        aug_rows,
        [
            "family_id",
            "mode",
            "descriptor_signature",
            "n",
            "k_contexts",
            "m_per_context",
            "total_budget",
            "stack_rank",
            "local_exact_all",
            "shared_exact",
            "shared_aug_threshold",
            "shared_aug_found",
            "context_invariance_gap",
            "cid",
            "stack_alignment",
            "stack_residual",
            "notes",
        ],
    )

    write_csv(
        OUT_MAIN / "multicontext_anomaly_catalog.csv",
        anomalies,
        [
            "anomaly_id",
            "anomaly_type",
            "descriptor_signature",
            "family_count",
            "shared_exact_values",
            "evidence_families",
            "severity",
            "notes",
        ],
    )

    write_csv(
        OUT_SFPR / "formation_secondary_witnesses.csv",
        formation_rows,
        [
            "formation_case_id",
            "mechanism",
            "n",
            "k_contexts",
            "pre_local_exact",
            "pre_shared_exact",
            "post_local_exact",
            "post_shared_exact",
            "pre_context_gap",
            "post_context_gap",
            "pre_alignment",
            "post_alignment",
            "pre_dls",
            "post_dls",
            "structure_created_flag",
            "recoverability_change_shared",
            "recoverability_change_local",
            "pre_shared_aug_threshold",
            "post_shared_aug_threshold",
            "threshold_flip_flag",
            "notes",
        ],
    )


def compute_summary(main_rows: List[dict], aug_rows: List[dict], anomalies: List[dict], formation_rows: List[dict]) -> dict:
    mismatch_rank = sum(int(r["rank_only_pred_shared"]) != int(r["shared_exact"]) for r in main_rows)
    mismatch_budget = sum(int(r["budget_only_pred_shared"]) != int(r["shared_exact"]) for r in main_rows)
    local_global_split = sum(int(r["local_exact_all"]) == 1 and int(r["shared_exact"]) == 0 for r in main_rows)
    enlargement_flips = sum(int(r["enlargement_flip"]) == 1 for r in main_rows)
    shared_exact_count = sum(int(r["shared_exact"]) == 1 for r in main_rows)

    by_mech = Counter(r["mechanism"] for r in formation_rows)
    struct_created = sum(int(r["structure_created_flag"]) == 1 for r in formation_rows)
    bridge_local_not_shared = sum(
        int(r["post_local_exact"]) == 1 and int(r["post_shared_exact"]) == 0 for r in formation_rows
    )
    formation_worse_shared = sum(int(r["recoverability_change_shared"]) < 0 for r in formation_rows)

    return {
        "status": "EXPLORATION / NON-PROMOTED",
        "seed": SEED,
        "main_track": {
            "multicontext_families": len(main_rows),
            "local_exact_global_fail_count": local_global_split,
            "shared_exact_count": shared_exact_count,
            "rank_only_mismatch_count": mismatch_rank,
            "budget_only_mismatch_count": mismatch_budget,
            "family_enlargement_flip_count": enlargement_flips,
            "augmentation_catalog_rows": len(aug_rows),
            "anomaly_rows": len(anomalies),
            "anomaly_type_counts": dict(Counter(a["anomaly_type"] for a in anomalies)),
        },
        "secondary_track": {
            "formation_rows": len(formation_rows),
            "mechanism_counts": dict(by_mech),
            "structure_created_count": struct_created,
            "post_local_not_shared_count": bridge_local_not_shared,
            "shared_recoverability_decrease_count": formation_worse_shared,
        },
    }


def main() -> None:
    main_rows, aug_rows, anomalies = generate_multicontext_catalog(num_families=1800)
    formation_rows = generate_formation_secondary(num_rows=980)
    save_outputs(main_rows, aug_rows, anomalies, formation_rows)

    summary = compute_summary(main_rows, aug_rows, anomalies, formation_rows)
    with (OUT_MAIN / "summary.json").open("w") as f:
        json.dump(summary, f, indent=2)

    print(f"wrote {OUT_MAIN / 'multicontext_witness_catalog.csv'} ({len(main_rows)} rows)")
    print(f"wrote {OUT_MAIN / 'augmentation_threshold_catalog.csv'} ({len(aug_rows)} rows)")
    print(f"wrote {OUT_MAIN / 'multicontext_anomaly_catalog.csv'} ({len(anomalies)} rows)")
    print(f"wrote {OUT_SFPR / 'formation_secondary_witnesses.csv'} ({len(formation_rows)} rows)")
    print(f"wrote {OUT_MAIN / 'summary.json'}")


if __name__ == "__main__":
    main()
