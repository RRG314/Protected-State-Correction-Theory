#!/usr/bin/env python3
"""Generate SFPR discovery artifacts with falsification-first synthetic witnesses.

This script intentionally produces exploratory, non-promoted artifacts.
"""
from __future__ import annotations

import csv
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np

SEED = 20260418
TOL = 1e-8
RNG = np.random.default_rng(SEED)

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "data" / "generated" / "sfpr"
OUT_DIR.mkdir(parents=True, exist_ok=True)


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


def alignment_score(tau: np.ndarray, m: np.ndarray) -> float:
    denom = float(np.linalg.norm(tau))
    if denom <= TOL:
        return 1.0
    res = rowspace_residual(tau, m)
    return float(max(0.0, 1.0 - res / denom))


def exact_recoverable(tau: np.ndarray, m: np.ndarray) -> bool:
    return rowspace_residual(tau, m) <= 1e-7


def all_binary_states(n: int) -> np.ndarray:
    return np.array(list(itertools.product([0.0, 1.0], repeat=n)), dtype=float)


def compute_dls(m: np.ndarray, tau: np.ndarray, states: np.ndarray) -> float:
    fibers: Dict[Tuple[float, ...], List[float]] = defaultdict(list)
    for x in states:
        y = tuple(np.round(m @ x, 8).tolist())
        t = float(np.round(tau @ x, 8))
        fibers[y].append(t)

    diff_pairs = 0
    total_pairs = 0
    for vals in fibers.values():
        if len(vals) < 2:
            continue
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                total_pairs += 1
                if vals[i] != vals[j]:
                    diff_pairs += 1
    if total_pairs == 0:
        return 0.0
    return diff_pairs / total_pairs


def logdet_info(m: np.ndarray) -> float:
    gram = m @ m.T
    eps = 1e-6
    gram = gram + eps * np.eye(gram.shape[0])
    sign, ld = np.linalg.slogdet(gram)
    if sign <= 0:
        return float("-inf")
    return float(ld)


def descriptor_signature(n: int, m_rows: int, rank: int, info: float) -> str:
    info_bucket = "infneg" if not np.isfinite(info) else f"{round(info, 2):.2f}"
    return f"n{n}|m{m_rows}|r{rank}|i{info_bucket}"


def random_int_matrix(rows: int, cols: int, low: int = -2, high: int = 3) -> np.ndarray:
    while True:
        m = RNG.integers(low, high, size=(rows, cols)).astype(float)
        if np.any(np.abs(m) > 0):
            return m


def random_tau(n: int) -> np.ndarray:
    while True:
        t = RNG.integers(-2, 3, size=n).astype(float)
        if np.linalg.norm(t) > 0:
            return t


def cid_metric(contexts: Sequence[np.ndarray], tau: np.ndarray) -> Tuple[float, List[float], bool, bool]:
    # Shared decoder d: d M_c = tau for each context c.
    a_blocks = []
    b_blocks = []
    local_residuals = []
    local_exact_all = True
    for mc in contexts:
        a_blocks.append(mc.T)
        b_blocks.append(tau)
        lr = rowspace_residual(tau, mc)
        local_residuals.append(lr)
        if lr > 1e-7:
            local_exact_all = False

    a = np.vstack(a_blocks)
    b = np.concatenate(b_blocks)
    d, *_ = np.linalg.lstsq(a, b, rcond=None)
    per_ctx = [float(np.linalg.norm(d @ mc - tau)) for mc in contexts]
    cid = float(max(per_ctx))
    global_exact = cid <= 1e-7
    return cid, local_residuals, local_exact_all, global_exact


def fisher_floor_like(tau: np.ndarray, m: np.ndarray) -> float:
    # Target-specific sensitivity proxy: squared alignment score.
    a = alignment_score(tau, m)
    return float(a * a)


def psi_metric(terminals: Sequence[np.ndarray], tau: np.ndarray, states: np.ndarray) -> Tuple[float, float, List[float]]:
    single_dls = [compute_dls(mt, tau, states) for mt in terminals]
    joint = np.vstack(terminals)
    joint_dls = compute_dls(joint, tau, states)
    psi = min(single_dls) - joint_dls
    return float(psi), float(joint_dls), [float(x) for x in single_dls]


def write_csv(path: Path, rows: List[dict], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def generate_single_context(rows: List[dict], thresholds: List[dict], start_id: int = 0, count: int = 700) -> int:
    idx = start_id
    for _ in range(count):
        n = int(RNG.integers(4, 8))
        m_rows = int(RNG.integers(1, 5))
        m = random_int_matrix(m_rows, n)
        tau = random_tau(n)
        states = all_binary_states(min(n, 6))
        states = states if n <= 6 else RNG.integers(0, 2, size=(64, n)).astype(float)

        rank = matrix_rank(m)
        info = logdet_info(m)
        dls = compute_dls(m, tau, states)
        exact = exact_recoverable(tau, m)
        tsf = fisher_floor_like(tau, m)
        res = rowspace_residual(tau, m)

        rows.append(
            {
                "witness_id": f"single_{idx}",
                "family": "single_context",
                "n": n,
                "m_total": m_rows,
                "rank": rank,
                "total_info": round(info, 8) if np.isfinite(info) else "-inf",
                "descriptor_signature": descriptor_signature(n, m_rows, rank, info),
                "local_exact": int(exact),
                "global_exact": int(exact),
                "dls": round(dls, 8),
                "cid": 0.0,
                "psi": "",
                "il": "",
                "tsf": round(tsf, 8),
                "alignment": round(alignment_score(tau, m), 8),
                "residual": round(res, 8),
                "rank_only_pred": int(rank == n),
                "budget_only_pred": int(m_rows >= max(1, n // 2)),
                "target_class": "linear_scalar",
                "notes": "",
            }
        )

        # threshold chain by one-measurement augmentation
        m0 = m.copy()
        exact_prev = exact
        for step in range(1, 4):
            add = random_int_matrix(1, n)
            m0 = np.vstack([m0, add])
            exact_now = exact_recoverable(tau, m0)
            thresholds.append(
                {
                    "series_id": f"single_thr_{idx}",
                    "family": "single_context",
                    "step": step,
                    "n": n,
                    "m_total": m0.shape[0],
                    "rank": matrix_rank(m0),
                    "exact": int(exact_now),
                    "dls": round(compute_dls(m0, tau, states), 8),
                    "alignment": round(alignment_score(tau, m0), 8),
                    "flip_vs_prev": int(exact_now != exact_prev),
                    "driver": "one_measurement_augmentation",
                }
            )
            exact_prev = exact_now

        idx += 1
    return idx


def generate_multi_context(rows: List[dict], persistence_rows: List[dict], start_id: int = 0, count: int = 550) -> int:
    idx = start_id
    for _ in range(count):
        n = int(RNG.integers(4, 7))
        m_dim = 2
        k = int(RNG.integers(2, 5))
        tau = random_tau(n)
        u = random_tau(n)

        while abs(float(np.dot(tau, u))) > 0.9 * np.linalg.norm(tau) * np.linalg.norm(u):
            u = random_tau(n)

        contexts = []
        mode = RNG.choice(["shared_exact", "local_only", "mixed"], p=[0.35, 0.45, 0.20])
        if mode == "shared_exact":
            a0 = float(RNG.integers(-2, 3))
            for _c in range(k):
                mc = np.vstack([tau + a0 * u, u])
                contexts.append(mc)
        elif mode == "local_only":
            for _c in range(k):
                ac = float(RNG.integers(-3, 4))
                if ac == 0:
                    ac = 1.0
                mc = np.vstack([tau + ac * u, u])
                contexts.append(mc)
        else:
            for _c in range(k):
                mc = random_int_matrix(m_dim, n)
                contexts.append(mc)

        states = all_binary_states(min(n, 6))
        states = states if n <= 6 else RNG.integers(0, 2, size=(64, n)).astype(float)
        cid, local_residuals, local_exact_all, global_exact = cid_metric(contexts, tau)

        stacked = np.vstack(contexts)
        rank = matrix_rank(stacked)
        info = logdet_info(stacked)
        dls = compute_dls(stacked, tau, states)

        rows.append(
            {
                "witness_id": f"ctx_{idx}",
                "family": "multi_context_shared",
                "n": n,
                "m_total": int(stacked.shape[0]),
                "rank": rank,
                "total_info": round(info, 8) if np.isfinite(info) else "-inf",
                "descriptor_signature": descriptor_signature(n, int(stacked.shape[0]), rank, info),
                "local_exact": int(local_exact_all),
                "global_exact": int(global_exact),
                "dls": round(dls, 8),
                "cid": round(cid, 8),
                "psi": "",
                "il": "",
                "tsf": round(fisher_floor_like(tau, stacked), 8),
                "alignment": round(alignment_score(tau, stacked), 8),
                "residual": round(rowspace_residual(tau, stacked), 8),
                "rank_only_pred": int(rank == n),
                "budget_only_pred": int(stacked.shape[0] >= max(1, n // 2)),
                "target_class": "context_shared_decoder",
                "notes": mode,
            }
        )

        if local_exact_all and not global_exact:
            persistence_rows.append(
                {
                    "anomaly_id": f"p_ctx_{idx}",
                    "type": "local_exact_global_fail",
                    "family": "multi_context_shared",
                    "n": n,
                    "contexts": k,
                    "descriptor_signature": descriptor_signature(n, int(stacked.shape[0]), rank, info),
                    "local_exact": 1,
                    "global_exact": 0,
                    "fragility_metric": round(cid, 8),
                    "trigger": "shared_decoder_constraint",
                    "notes": "each context individually exact but no shared decoder",
                }
            )

        # perturbation fragility test
        eps = float(RNG.uniform(1e-4, 1e-1))
        perturbed = [mc + eps * RNG.normal(size=mc.shape) for mc in contexts]
        cid_p, _, local_p, global_p = cid_metric(perturbed, tau)
        if int(global_p) != int(global_exact):
            persistence_rows.append(
                {
                    "anomaly_id": f"p_ctx_flip_{idx}",
                    "type": "context_drift_flip",
                    "family": "multi_context_shared",
                    "n": n,
                    "contexts": k,
                    "descriptor_signature": descriptor_signature(n, int(stacked.shape[0]), rank, info),
                    "local_exact": int(local_p),
                    "global_exact": int(global_p),
                    "fragility_metric": round(cid_p, 8),
                    "trigger": f"eps={eps:.5f}",
                    "notes": "global verdict changed under context drift",
                }
            )

        idx += 1
    return idx


def generate_multi_terminal(rows: List[dict], thresholds: List[dict], start_id: int = 0, count: int = 550) -> int:
    idx = start_id
    for _ in range(count):
        n = 6
        tau = random_tau(n)
        u = random_tau(n)
        v = random_tau(n)
        w = random_tau(n)
        states = all_binary_states(6)

        mode = RNG.choice(["complementary_success", "redundant_failure", "mixed"], p=[0.4, 0.35, 0.25])
        if mode == "complementary_success":
            t1 = np.vstack([tau + u, u])
            t2 = np.vstack([v, w])
        elif mode == "redundant_failure":
            t1 = np.vstack([u, v])
            t2 = np.vstack([u + v, w])
        else:
            t1 = random_int_matrix(2, n)
            t2 = random_int_matrix(2, n)

        joint = np.vstack([t1, t2])
        rank = matrix_rank(joint)
        info = logdet_info(joint)
        exact_joint = exact_recoverable(tau, joint)
        local_exact = int(exact_recoverable(tau, t1) or exact_recoverable(tau, t2))
        psi, joint_dls, single_dls = psi_metric([t1, t2], tau, states)

        rows.append(
            {
                "witness_id": f"mt_{idx}",
                "family": "multi_terminal_allocation",
                "n": n,
                "m_total": 4,
                "rank": rank,
                "total_info": round(info, 8) if np.isfinite(info) else "-inf",
                "descriptor_signature": descriptor_signature(n, 4, rank, info),
                "local_exact": local_exact,
                "global_exact": int(exact_joint),
                "dls": round(joint_dls, 8),
                "cid": "",
                "psi": round(psi, 8),
                "il": "",
                "tsf": round(fisher_floor_like(tau, joint), 8),
                "alignment": round(alignment_score(tau, joint), 8),
                "residual": round(rowspace_residual(tau, joint), 8),
                "rank_only_pred": int(rank == n),
                "budget_only_pred": int(4 >= n // 2),
                "target_class": "distributed_target",
                "notes": f"mode={mode};single_dls={single_dls}",
            }
        )

        # allocation threshold series (repartitioning one measurement)
        candidates = [tau + u, u, v, w, u + v, tau + w]
        exact_prev = None
        for step in range(1, 4):
            rows_per_terminal = [2 + (step % 2), 2 - (step % 2)]
            t1s = np.vstack(candidates[: rows_per_terminal[0]])
            t2s = np.vstack(candidates[-rows_per_terminal[1] :])
            js = np.vstack([t1s, t2s])
            exact_now = int(exact_recoverable(tau, js))
            thresholds.append(
                {
                    "series_id": f"mt_thr_{idx}",
                    "family": "multi_terminal_allocation",
                    "step": step,
                    "n": n,
                    "m_total": int(js.shape[0]),
                    "rank": matrix_rank(js),
                    "exact": exact_now,
                    "dls": round(compute_dls(js, tau, states), 8),
                    "alignment": round(alignment_score(tau, js), 8),
                    "flip_vs_prev": "" if exact_prev is None else int(exact_now != exact_prev),
                    "driver": "allocation_geometry",
                }
            )
            exact_prev = exact_now

        idx += 1
    return idx


def generate_intervention(rows: List[dict], start_id: int = 0, count: int = 350) -> int:
    idx = start_id
    for _ in range(count):
        n = 5
        tau = random_tau(n)
        u = random_tau(n)
        states = all_binary_states(5)

        # observational map tends to entangle target with nuisance
        obs = np.vstack([tau + u, u + random_tau(n)])
        itv = np.vstack([tau, random_tau(n)])

        mode = RNG.choice(["lift", "no_change", "reverse"], p=[0.55, 0.35, 0.10])
        if mode == "no_change":
            itv = obs.copy()
        elif mode == "reverse":
            obs, itv = itv, obs

        exact_obs = exact_recoverable(tau, obs)
        exact_itv = exact_recoverable(tau, itv)
        il = rowspace_residual(tau, obs) - rowspace_residual(tau, itv)

        for label, m in [("obs", obs), ("itv", itv)]:
            rank = matrix_rank(m)
            info = logdet_info(m)
            rows.append(
                {
                    "witness_id": f"intv_{idx}_{label}",
                    "family": "intervention_split",
                    "n": n,
                    "m_total": int(m.shape[0]),
                    "rank": rank,
                    "total_info": round(info, 8) if np.isfinite(info) else "-inf",
                    "descriptor_signature": descriptor_signature(n, int(m.shape[0]), rank, info),
                    "local_exact": int(exact_obs if label == "obs" else exact_itv),
                    "global_exact": int(exact_obs if label == "obs" else exact_itv),
                    "dls": round(compute_dls(m, tau, states), 8),
                    "cid": "",
                    "psi": "",
                    "il": round(il, 8),
                    "tsf": round(fisher_floor_like(tau, m), 8),
                    "alignment": round(alignment_score(tau, m), 8),
                    "residual": round(rowspace_residual(tau, m), 8),
                    "rank_only_pred": int(rank == n),
                    "budget_only_pred": int(m.shape[0] >= n // 2),
                    "target_class": "causal_context",
                    "notes": f"mode={mode};pair={idx}",
                }
            )
        idx += 1
    return idx


def all_k_subsets(rows: np.ndarray, k: int):
    for idxs in itertools.combinations(range(rows.shape[0]), k):
        yield rows[list(idxs)]


def generate_design_conflict(rows: List[dict], start_id: int = 0, count: int = 320) -> int:
    idx = start_id
    for _ in range(count):
        n = 4
        tau = random_tau(n)
        pool = random_int_matrix(6, n)
        k = 2
        states = all_binary_states(4)

        best_d = None
        best_d_score = -float("inf")
        best_a = None
        best_a_score = -float("inf")

        for cand in all_k_subsets(pool, k):
            d_score = logdet_info(cand)
            a_score = alignment_score(tau, cand)
            if d_score > best_d_score:
                best_d_score = d_score
                best_d = cand.copy()
            if a_score > best_a_score:
                best_a_score = a_score
                best_a = cand.copy()

        assert best_d is not None and best_a is not None

        for label, m in [("d_opt", best_d), ("alpha_opt", best_a)]:
            rank = matrix_rank(m)
            info = logdet_info(m)
            exact = exact_recoverable(tau, m)
            rows.append(
                {
                    "witness_id": f"design_{idx}_{label}",
                    "family": "design_conflict",
                    "n": n,
                    "m_total": k,
                    "rank": rank,
                    "total_info": round(info, 8) if np.isfinite(info) else "-inf",
                    "descriptor_signature": descriptor_signature(n, k, rank, info),
                    "local_exact": int(exact),
                    "global_exact": int(exact),
                    "dls": round(compute_dls(m, tau, states), 8),
                    "cid": "",
                    "psi": "",
                    "il": "",
                    "tsf": round(fisher_floor_like(tau, m), 8),
                    "alignment": round(alignment_score(tau, m), 8),
                    "residual": round(rowspace_residual(tau, m), 8),
                    "rank_only_pred": int(rank == n),
                    "budget_only_pred": int(k >= n // 2),
                    "target_class": "design_target",
                    "notes": f"pair={idx};label={label};d_score={best_d_score:.4f};a_score={best_a_score:.4f}",
                }
            )
        idx += 1
    return idx


def generate_formation(rows: List[dict], formation_rows: List[dict], start_id: int = 0, per_route: int = 80) -> int:
    idx = start_id
    routes = [
        "constraint_generation",
        "symmetry_breaking",
        "context_conditioned_differentiation",
        "feedback_induced_organization",
        "local_to_global_organization",
        "intervention_generated_structure",
        "optimization_induced_structure",
    ]

    for route in routes:
        for j in range(per_route):
            n = 5
            tau = random_tau(n)
            states = all_binary_states(5)

            pre = random_int_matrix(2, n)
            post = pre.copy()

            if route == "constraint_generation":
                post = np.vstack([pre, tau])
            elif route == "symmetry_breaking":
                u = random_tau(n)
                pre = np.vstack([u, -u])
                post = np.vstack([u, tau + u])
            elif route == "context_conditioned_differentiation":
                u = random_tau(n)
                pre = np.vstack([tau + u, u])
                post = np.vstack([tau + (j % 3 + 1) * u, u])
            elif route == "feedback_induced_organization":
                step = (j % 5 + 1) / 5.0
                post = pre + step * np.outer(np.ones(pre.shape[0]), tau / (np.linalg.norm(tau) + 1e-9))
            elif route == "local_to_global_organization":
                u = random_tau(n)
                pre = np.vstack([tau + u, u])
                post = np.vstack([tau + 2.0 * u, u])
            elif route == "intervention_generated_structure":
                u = random_tau(n)
                pre = np.vstack([tau + u, random_tau(n)])
                post = np.vstack([tau, random_tau(n)])
            elif route == "optimization_induced_structure":
                pool = random_int_matrix(5, n)
                best_a = None
                best_s = -1.0
                for cand in all_k_subsets(pool, 2):
                    s = alignment_score(tau, cand)
                    if s > best_s:
                        best_s = s
                        best_a = cand
                pre = pool[:2]
                post = best_a.copy() if best_a is not None else pool[:2]

            pre_exact = exact_recoverable(tau, pre)
            post_exact = exact_recoverable(tau, post)
            pre_dls = compute_dls(pre, tau, states)
            post_dls = compute_dls(post, tau, states)
            pre_align = alignment_score(tau, pre)
            post_align = alignment_score(tau, post)

            formation_rows.append(
                {
                    "formation_id": f"form_{idx}",
                    "route": route,
                    "n": n,
                    "pre_m": pre.shape[0],
                    "post_m": post.shape[0],
                    "pre_rank": matrix_rank(pre),
                    "post_rank": matrix_rank(post),
                    "pre_exact": int(pre_exact),
                    "post_exact": int(post_exact),
                    "pre_dls": round(pre_dls, 8),
                    "post_dls": round(post_dls, 8),
                    "pre_alignment": round(pre_align, 8),
                    "post_alignment": round(post_align, 8),
                    "new_structure_flag": int((post_align > pre_align + 1e-6) or (post_dls < pre_dls - 1e-6)),
                    "recoverability_change": int(post_exact) - int(pre_exact),
                    "notes": "",
                }
            )

            for label, m, exact_val, dls_val, align_val in [
                ("pre", pre, pre_exact, pre_dls, pre_align),
                ("post", post, post_exact, post_dls, post_align),
            ]:
                info = logdet_info(m)
                rows.append(
                    {
                        "witness_id": f"formation_{idx}_{label}",
                        "family": "formation_bridge",
                        "n": n,
                        "m_total": int(m.shape[0]),
                        "rank": matrix_rank(m),
                        "total_info": round(info, 8) if np.isfinite(info) else "-inf",
                        "descriptor_signature": descriptor_signature(n, int(m.shape[0]), matrix_rank(m), info),
                        "local_exact": int(exact_val),
                        "global_exact": int(exact_val),
                        "dls": round(dls_val, 8),
                        "cid": "",
                        "psi": "",
                        "il": "",
                        "tsf": round(fisher_floor_like(tau, m), 8),
                        "alignment": round(align_val, 8),
                        "residual": round(rowspace_residual(tau, m), 8),
                        "rank_only_pred": int(matrix_rank(m) == n),
                        "budget_only_pred": int(m.shape[0] >= n // 2),
                        "target_class": "formation_target",
                        "notes": f"route={route};pair={idx};label={label}",
                    }
                )
            idx += 1
    return idx


def generate_persistence(rows: List[dict], persistence_rows: List[dict], thresholds: List[dict], start_id: int = 0, count: int = 300) -> int:
    idx = start_id
    for _ in range(count):
        n = int(RNG.integers(4, 7))
        tau = random_tau(n)
        base = random_int_matrix(3, n)
        states = all_binary_states(min(n, 6))
        if n > 6:
            states = RNG.integers(0, 2, size=(64, n)).astype(float)

        exact_base = exact_recoverable(tau, base)
        info_base = logdet_info(base)
        rows.append(
            {
                "witness_id": f"persist_{idx}_base",
                "family": "persistence_bridge",
                "n": n,
                "m_total": int(base.shape[0]),
                "rank": matrix_rank(base),
                "total_info": round(info_base, 8) if np.isfinite(info_base) else "-inf",
                "descriptor_signature": descriptor_signature(n, int(base.shape[0]), matrix_rank(base), info_base),
                "local_exact": int(exact_base),
                "global_exact": int(exact_base),
                "dls": round(compute_dls(base, tau, states), 8),
                "cid": "",
                "psi": "",
                "il": "",
                "tsf": round(fisher_floor_like(tau, base), 8),
                "alignment": round(alignment_score(tau, base), 8),
                "residual": round(rowspace_residual(tau, base), 8),
                "rank_only_pred": int(matrix_rank(base) == n),
                "budget_only_pred": int(base.shape[0] >= n // 2),
                "target_class": "persistence_target",
                "notes": "base",
            }
        )

        # perturbation/coarsening sequence
        exact_prev = exact_base
        for step, eps in enumerate([0.001, 0.01, 0.05, 0.1], start=1):
            noise = eps * RNG.normal(size=base.shape)
            m_eps = base + noise
            exact_now = exact_recoverable(tau, m_eps)
            dls_now = compute_dls(m_eps, tau, states)
            thresholds.append(
                {
                    "series_id": f"persist_thr_{idx}",
                    "family": "persistence_bridge",
                    "step": step,
                    "n": n,
                    "m_total": int(m_eps.shape[0]),
                    "rank": matrix_rank(m_eps),
                    "exact": int(exact_now),
                    "dls": round(dls_now, 8),
                    "alignment": round(alignment_score(tau, m_eps), 8),
                    "flip_vs_prev": int(exact_now != exact_prev),
                    "driver": f"noise_eps_{eps}",
                }
            )
            if exact_now != exact_prev:
                persistence_rows.append(
                    {
                        "anomaly_id": f"p_noise_{idx}_{step}",
                        "type": "noise_fragility_flip",
                        "family": "persistence_bridge",
                        "n": n,
                        "contexts": 1,
                        "descriptor_signature": descriptor_signature(
                            n, int(m_eps.shape[0]), matrix_rank(m_eps), logdet_info(m_eps)
                        ),
                        "local_exact": int(exact_now),
                        "global_exact": int(exact_now),
                        "fragility_metric": float(eps),
                        "trigger": "noise",
                        "notes": "exactness flip under perturbation",
                    }
                )
            exact_prev = exact_now

        # model mismatch test
        wrong_basis = random_int_matrix(base.shape[0], n)
        mismatch_res = rowspace_residual(tau, wrong_basis)
        if mismatch_res > rowspace_residual(tau, base) + 1e-6:
            persistence_rows.append(
                {
                    "anomaly_id": f"p_mismatch_{idx}",
                    "type": "model_mismatch_instability",
                    "family": "persistence_bridge",
                    "n": n,
                    "contexts": 1,
                    "descriptor_signature": descriptor_signature(n, int(base.shape[0]), matrix_rank(base), info_base),
                    "local_exact": int(exact_base),
                    "global_exact": int(exact_base),
                    "fragility_metric": round(mismatch_res, 8),
                    "trigger": "representation_change",
                    "notes": "wrong representation increases residual",
                }
            )

        idx += 1
    return idx


def build_anomaly_catalog(witness_rows: List[dict], threshold_rows: List[dict], persistence_rows: List[dict], formation_rows: List[dict]) -> List[dict]:
    anomalies: List[dict] = []

    grouped: Dict[Tuple[str, str], List[dict]] = defaultdict(list)
    for r in witness_rows:
        grouped[(r["family"], r["descriptor_signature"])].append(r)

    aid = 0
    for (fam, sig), rs in grouped.items():
        verdicts = {int(x["global_exact"]) for x in rs}
        if len(verdicts) > 1:
            anomalies.append(
                {
                    "anomaly_id": f"a_{aid}",
                    "type": "same_descriptor_opposite_verdict",
                    "family": fam,
                    "descriptor_signature": sig,
                    "count": len(rs),
                    "evidence": ";".join(x["witness_id"] for x in rs[:6]),
                    "severity": "high",
                }
            )
            aid += 1

    by_pair: Dict[str, Dict[str, dict]] = defaultdict(dict)
    for r in witness_rows:
        if r["family"] != "design_conflict":
            continue
        pair = r["notes"].split("pair=")[1].split(";")[0]
        label = "d_opt" if "label=d_opt" in r["notes"] else "alpha_opt"
        by_pair[pair][label] = r
    for pair, item in by_pair.items():
        if "d_opt" in item and "alpha_opt" in item:
            d = item["d_opt"]
            a = item["alpha_opt"]
            if int(d["global_exact"]) < int(a["global_exact"]):
                anomalies.append(
                    {
                        "anomaly_id": f"a_{aid}",
                        "type": "design_failure_conflict",
                        "family": "design_conflict",
                        "descriptor_signature": d["descriptor_signature"],
                        "count": 2,
                        "evidence": f"{d['witness_id']} vs {a['witness_id']}",
                        "severity": "high",
                    }
                )
                aid += 1

    intv_pairs: Dict[str, Dict[str, dict]] = defaultdict(dict)
    for r in witness_rows:
        if r["family"] != "intervention_split":
            continue
        pair = r["notes"].split("pair=")[1]
        lbl = "obs" if r["witness_id"].endswith("_obs") else "itv"
        intv_pairs[pair][lbl] = r
    for pair, item in intv_pairs.items():
        if "obs" in item and "itv" in item:
            obs = item["obs"]
            itv = item["itv"]
            if int(obs["global_exact"]) != int(itv["global_exact"]):
                anomalies.append(
                    {
                        "anomaly_id": f"a_{aid}",
                        "type": "intervention_vs_observation_split",
                        "family": "intervention_split",
                        "descriptor_signature": obs["descriptor_signature"],
                        "count": 2,
                        "evidence": f"{obs['witness_id']} -> {itv['witness_id']}",
                        "severity": "high",
                    }
                )
                aid += 1

    for t in threshold_rows:
        if str(t["flip_vs_prev"]) == "1":
            anomalies.append(
                {
                    "anomaly_id": f"a_{aid}",
                    "type": "threshold_flip",
                    "family": t["family"],
                    "descriptor_signature": f"{t['series_id']}|step{t['step']}",
                    "count": 1,
                    "evidence": f"exact flip at step={t['step']} driver={t['driver']}",
                    "severity": "medium",
                }
            )
            aid += 1

    for f in formation_rows:
        if int(f["new_structure_flag"]) == 1 and int(f["recoverability_change"]) <= 0:
            anomalies.append(
                {
                    "anomaly_id": f"a_{aid}",
                    "type": "formation_without_recoverability",
                    "family": "formation_bridge",
                    "descriptor_signature": f["route"],
                    "count": 1,
                    "evidence": f["formation_id"],
                    "severity": "medium",
                }
            )
            aid += 1

    for p in persistence_rows:
        anomalies.append(
            {
                "anomaly_id": f"a_{aid}",
                "type": p["type"],
                "family": p["family"],
                "descriptor_signature": p["descriptor_signature"],
                "count": 1,
                "evidence": p["anomaly_id"],
                "severity": "medium" if "flip" in p["type"] else "high",
            }
        )
        aid += 1

    return anomalies


def build_summary(witness_rows: List[dict], anomalies: List[dict], threshold_rows: List[dict], formation_rows: List[dict], persistence_rows: List[dict]) -> dict:
    by_family = Counter(r["family"] for r in witness_rows)
    anomalies_by_type = Counter(a["type"] for a in anomalies)
    anomalies_by_family = Counter(a["family"] for a in anomalies)

    local_global_fail = sum(1 for r in witness_rows if r["family"] == "multi_context_shared" and int(r["local_exact"]) == 1 and int(r["global_exact"]) == 0)
    amount_only_fail = sum(1 for a in anomalies if a["type"] == "same_descriptor_opposite_verdict")
    design_conflicts = sum(1 for a in anomalies if a["type"] == "design_failure_conflict")
    intervention_splits = sum(1 for a in anomalies if a["type"] == "intervention_vs_observation_split")
    threshold_flips = sum(1 for a in anomalies if a["type"] == "threshold_flip")

    return {
        "status": "EXPLORATION / NON-PROMOTED",
        "seed": SEED,
        "witness_count": len(witness_rows),
        "anomaly_count": len(anomalies),
        "threshold_count": len(threshold_rows),
        "formation_witness_count": len(formation_rows),
        "persistence_anomaly_count": len(persistence_rows),
        "families": dict(by_family),
        "anomalies_by_type": dict(anomalies_by_type),
        "anomalies_by_family": dict(anomalies_by_family),
        "key_support_counts": {
            "conditioned_vs_invariant_split_support": local_global_fail,
            "amount_only_insufficiency_support": amount_only_fail,
            "design_failure_support": design_conflicts,
            "intervention_split_support": intervention_splits,
            "threshold_flip_support": threshold_flips,
        },
        "notes": {
            "scope": "finite/synthetic linear and context-structured families",
            "promotion": "no theorem-spine promotion",
        },
    }


def main() -> None:
    witness_rows: List[dict] = []
    threshold_rows: List[dict] = []
    formation_rows: List[dict] = []
    persistence_rows: List[dict] = []

    idx = 0
    idx = generate_single_context(witness_rows, threshold_rows, idx, count=700)
    idx = generate_multi_context(witness_rows, persistence_rows, idx, count=550)
    idx = generate_multi_terminal(witness_rows, threshold_rows, idx, count=550)
    idx = generate_intervention(witness_rows, idx, count=350)
    idx = generate_design_conflict(witness_rows, idx, count=320)
    idx = generate_formation(witness_rows, formation_rows, idx, per_route=80)
    idx = generate_persistence(witness_rows, persistence_rows, threshold_rows, idx, count=300)

    anomalies = build_anomaly_catalog(witness_rows, threshold_rows, persistence_rows, formation_rows)
    summary = build_summary(witness_rows, anomalies, threshold_rows, formation_rows, persistence_rows)

    witness_fields = [
        "witness_id",
        "family",
        "n",
        "m_total",
        "rank",
        "total_info",
        "descriptor_signature",
        "local_exact",
        "global_exact",
        "dls",
        "cid",
        "psi",
        "il",
        "tsf",
        "alignment",
        "residual",
        "rank_only_pred",
        "budget_only_pred",
        "target_class",
        "notes",
    ]
    threshold_fields = [
        "series_id",
        "family",
        "step",
        "n",
        "m_total",
        "rank",
        "exact",
        "dls",
        "alignment",
        "flip_vs_prev",
        "driver",
    ]
    anomaly_fields = ["anomaly_id", "type", "family", "descriptor_signature", "count", "evidence", "severity"]
    formation_fields = [
        "formation_id",
        "route",
        "n",
        "pre_m",
        "post_m",
        "pre_rank",
        "post_rank",
        "pre_exact",
        "post_exact",
        "pre_dls",
        "post_dls",
        "pre_alignment",
        "post_alignment",
        "new_structure_flag",
        "recoverability_change",
        "notes",
    ]
    persistence_fields = [
        "anomaly_id",
        "type",
        "family",
        "n",
        "contexts",
        "descriptor_signature",
        "local_exact",
        "global_exact",
        "fragility_metric",
        "trigger",
        "notes",
    ]

    write_csv(OUT_DIR / "witness_catalog.csv", witness_rows, witness_fields)
    write_csv(OUT_DIR / "anomaly_catalog.csv", anomalies, anomaly_fields)
    write_csv(OUT_DIR / "threshold_catalog.csv", threshold_rows, threshold_fields)
    write_csv(OUT_DIR / "formation_witnesses.csv", formation_rows, formation_fields)
    write_csv(OUT_DIR / "persistence_anomalies.csv", persistence_rows, persistence_fields)

    with (OUT_DIR / "summary.json").open("w") as f:
        json.dump(summary, f, indent=2)

    print(f"wrote {OUT_DIR / 'witness_catalog.csv'} ({len(witness_rows)} rows)")
    print(f"wrote {OUT_DIR / 'anomaly_catalog.csv'} ({len(anomalies)} rows)")
    print(f"wrote {OUT_DIR / 'threshold_catalog.csv'} ({len(threshold_rows)} rows)")
    print(f"wrote {OUT_DIR / 'formation_witnesses.csv'} ({len(formation_rows)} rows)")
    print(f"wrote {OUT_DIR / 'persistence_anomalies.csv'} ({len(persistence_rows)} rows)")
    print(f"wrote {OUT_DIR / 'summary.json'}")


if __name__ == "__main__":
    main()
