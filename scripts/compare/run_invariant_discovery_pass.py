#!/usr/bin/env python3
"""Invariant discovery and stress pass for OCP/recoverability ecosystem.

Outputs:
- data/generated/invariants/invariant_witness_catalog.csv
- data/generated/invariants/invariant_stress_catalog.csv
- data/generated/invariants/summary.json
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any, Callable, Iterable

import numpy as np

from ocp.context_invariant import (
    agreement_operator_recoverability,
    candidate_library_recoverability,
    context_invariant_recoverability,
    minimal_shared_augmentation,
    unconstrained_shared_augmentation_threshold,
)
from ocp.recoverability import (
    restricted_linear_collision_gap,
    restricted_linear_rank_lower_bound,
    restricted_linear_recoverability,
    restricted_linear_rowspace_residual,
    same_rank_alignment_counterexample,
)

SEED = 20260418
RNG = np.random.default_rng(SEED)
TOL = 1e-8

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "generated" / "invariants"
OUT.mkdir(parents=True, exist_ok=True)

# Runtime controls tuned for deterministic completion.
N_FAMILY_A = 8
N_CONTEXT_PAIR_TARGET = 4
MAX_CONTEXT_PAIR_ATTEMPTS = 800
MAX_BASE_STRESS = 6


def _rank(m: np.ndarray) -> int:
    return int(np.linalg.matrix_rank(m, TOL))


def _random_vector(n: int) -> np.ndarray:
    while True:
        v = RNG.integers(-3, 4, size=n).astype(float)
        if np.linalg.norm(v) > TOL:
            return v


def _random_nonparallel(v: np.ndarray) -> np.ndarray:
    while True:
        u = _random_vector(v.shape[0])
        cos = abs(float(np.dot(v, u))) / (np.linalg.norm(v) * np.linalg.norm(u) + 1e-12)
        if cos < 0.95:
            return u


def _random_full_row_rank(rows: int, cols: int) -> np.ndarray:
    while True:
        m = RNG.integers(-3, 4, size=(rows, cols)).astype(float)
        if _rank(m) == rows:
            return m


def _random_invertible(size: int) -> np.ndarray:
    while True:
        a = RNG.integers(-3, 4, size=(size, size)).astype(float)
        if abs(np.linalg.det(a)) > 1e-6:
            return a


def _candidate_rows(target: np.ndarray, contexts: list[np.ndarray]) -> list[np.ndarray]:
    d = target.shape[1]
    rows: list[np.ndarray] = []
    for context in contexts:
        for row in context[: min(1, context.shape[0])]:
            rows.append(np.asarray(row, dtype=float))
    for i in range(min(d, 2)):
        e = np.zeros(d, dtype=float)
        e[i] = 1.0
        rows.append(e)
    stacked = np.vstack(contexts)
    for i in range(min(2, stacked.shape[0])):
        for j in range(i + 1, min(3, stacked.shape[0])):
            rows.append(stacked[i] + stacked[j])
            rows.append(stacked[i] - stacked[j])

    uniq: list[np.ndarray] = []
    for row in rows:
        if np.linalg.norm(row) <= TOL:
            continue
        if any(np.linalg.norm(row - old) <= 1e-9 for old in uniq):
            continue
        uniq.append(row)
    return uniq


def _nullspace_rowspace_orth_residual(v: np.ndarray, m: np.ndarray) -> np.ndarray:
    if m.size == 0:
        return v.copy()
    _, s, vh = np.linalg.svd(m, full_matrices=False)
    r = int(np.sum(s > TOL))
    if r == 0:
        return v.copy()
    basis = vh[:r]
    return v - (v @ basis.T) @ basis


def _amount_signature(n: int, p: int, q: int, k: int, stack_rank: int) -> str:
    return f"n{n}|p{p}|q{q}|k{k}|b{p*k}|r{stack_rank}"


def _compute_metrics(
    target: np.ndarray,
    contexts: list[np.ndarray],
    *,
    include_library_search: bool = False,
) -> dict[str, Any]:
    k = len(contexts)
    p, n = contexts[0].shape
    q = target.shape[0]

    local_flags = [bool(restricted_linear_recoverability(m, target).exact_recoverable) for m in contexts]
    local_exact_all = bool(all(local_flags))

    stack = np.vstack(contexts)
    stack_rep = restricted_linear_recoverability(stack, target)
    rank_lb = restricted_linear_rank_lower_bound(stack, target)

    rowspace_residual = float(restricted_linear_rowspace_residual(stack, target))
    if int(stack_rep.null_intersection_dimension) <= 2:
        collision_gap = float(restricted_linear_collision_gap(stack, target))
        collision_gap_mode = "exact_low_null_dim"
    else:
        # Full collision-gap computation scales combinatorially with nullspace
        # dimension; use residual proxy for high-null synthetic sweeps.
        collision_gap = rowspace_residual
        collision_gap_mode = "proxy_rowspace_residual"

    ctx = context_invariant_recoverability(contexts, target)
    agr = agreement_operator_recoverability(contexts, target)
    free = unconstrained_shared_augmentation_threshold(contexts, target)

    if include_library_search:
        candidates = _candidate_rows(target, contexts)
        restr = minimal_shared_augmentation(contexts, target, candidates, max_shared_rows=2)
        lib = candidate_library_recoverability(contexts, target, candidates, max_search_rows=2)
        restricted_rows = "" if restr.minimal_shared_rows is None else int(restr.minimal_shared_rows)
        delta_c = int(lib.library_target_defect)
        library_rank_gain = int(lib.library_rank_gain)
        library_full_feasible = int(lib.full_pool_feasible)
        restricted_aug_found = int(restr.invariant_exact_after_augmentation)
    else:
        # Fast path for stress perturbations: preserve exactness/CID/free-threshold
        # diagnostics and skip bounded candidate-library combinatorics.
        delta_c = int(free.minimal_shared_rows_free)
        library_rank_gain = 0
        library_full_feasible = 0
        restricted_aug_found = 0
        restricted_rows = ""

    return {
        "n": int(n),
        "p": int(p),
        "q": int(q),
        "k": int(k),
        "total_budget": int(p * k),
        "stack_rank": int(_rank(stack)),
        "target_rank": int(_rank(target)),
        "amount_signature": _amount_signature(n, p, q, k, _rank(stack)),
        "local_exact_all": int(local_exact_all),
        "invariant_exact": int(ctx.invariant_exact),
        "exact_stack": int(stack_rep.exact_recoverable),
        "rank_lb_satisfied": int(rank_lb.lower_bound_satisfied),
        "null_intersection_dim": int(stack_rep.null_intersection_dimension),
        "rowspace_residual": rowspace_residual,
        "collision_gap": collision_gap,
        "collision_gap_mode": collision_gap_mode,
        "cid": float(ctx.invariant_residual_max_context),
        "context_gap": int(local_exact_all) - int(ctx.invariant_exact),
        "agreement_basis_dim": int(agr.agreement_basis_dimension),
        "lift_rank": int(agr.lifted_matrix_rank),
        "lift_residual": float(agr.lifted_residual_norm),
        "delta_free": int(free.minimal_shared_rows_free),
        "delta_c": delta_c,
        "library_rank_gain": library_rank_gain,
        "library_full_feasible": library_full_feasible,
        "restricted_aug_found": restricted_aug_found,
        "restricted_aug_rows": restricted_rows,
    }


def _build_shared_exact_family() -> tuple[np.ndarray, list[np.ndarray]]:
    n = int(RNG.integers(6, 10))
    p = int(RNG.integers(4, 6))
    q = int(RNG.integers(2, min(4, p)))
    k = int(RNG.integers(2, 5))

    D = _random_full_row_rank(q, p)
    M1 = _random_full_row_rank(p, n)
    target = D @ M1

    # Keep decoder rows in agreement subspace by adding rows from null(D).
    z = np.linalg.svd(D, full_matrices=True)[2][q:]
    contexts = []
    for _ in range(k):
        if z.size == 0:
            delta = np.zeros_like(M1)
        else:
            W = RNG.integers(-2, 3, size=(z.shape[0], n)).astype(float)
            delta = z.T @ W
        contexts.append(M1 + delta)
    return target, contexts


def _build_local_global_split_pair() -> tuple[np.ndarray, list[np.ndarray], list[np.ndarray]]:
    n = int(RNG.integers(6, 10))
    k = int(RNG.integers(2, 5))
    t = _random_vector(n)

    u0 = _random_nonparallel(t)
    a0 = int(RNG.integers(-3, 4))
    if a0 == 0:
        a0 = 1

    # Shared decoder exists with coefficients [1, -a0] for all contexts.
    exact_contexts = [np.vstack([t + a0 * u0, u0]) for _ in range(k)]

    fail_contexts = []
    for idx in range(k):
        # Local exactness holds with [1, -a_i] in each context.
        # Distinct a_i force incompatibility for any shared decoder.
        uc = _random_nonparallel(t)
        ac = idx + 1
        fail_contexts.append(np.vstack([t + ac * uc, uc]))

    target = t[None, :]
    return target, exact_contexts, fail_contexts


def _descriptor_stats(rows: list[dict[str, Any]], descriptor_fn: Callable[[dict[str, Any]], tuple[Any, ...]]) -> tuple[float, float]:
    # Verdict is invariant exactness.
    fibers: dict[tuple[Any, ...], list[int]] = {}
    for row in rows:
        key = descriptor_fn(row)
        fibers.setdefault(key, []).append(int(row["invariant_exact"]))

    mixed = 0
    total = len(rows)
    idelb_numer = 0
    for verdicts in fibers.values():
        e = sum(verdicts)
        f = len(verdicts) - e
        if e > 0 and f > 0:
            mixed += 1
        idelb_numer += min(e, f)

    dfmi = float(mixed / max(len(fibers), 1))
    idelb = float(idelb_numer / max(total, 1))
    return dfmi, idelb


def main() -> None:
    rows: list[dict[str, Any]] = []
    payload: dict[str, tuple[np.ndarray, list[np.ndarray]]] = {}

    sid = 0

    # Family A: Compatibility organized exact systems.
    for _ in range(N_FAMILY_A):
        target, contexts = _build_shared_exact_family()
        m = _compute_metrics(target, contexts)
        row = {
            "system_id": f"inv_{sid}",
            "row_kind": "system",
            "family": "compatibility_exact",
            "group_id": "",
            "role": "exact",
            **m,
            "notes": "agreement compatibility satisfied",
            "descriptor_dfmi": "",
            "descriptor_idelb": "",
            "descriptor_cl": "",
        }
        rows.append(row)
        payload[row["system_id"]] = (target, contexts)
        sid += 1

    # Family B: Local exact / global fail pairs.
    pair_id = 0
    pair_attempts = 0
    while pair_id < N_CONTEXT_PAIR_TARGET:
        pair_attempts += 1
        target, exact_contexts, fail_contexts = _build_local_global_split_pair()
        me = _compute_metrics(target, exact_contexts)
        mf = _compute_metrics(target, fail_contexts)
        if not (me["invariant_exact"] == 1 and mf["local_exact_all"] == 1 and mf["invariant_exact"] == 0):
            # Extremely rare numerical edge case under tolerance.
            continue

        gid = f"pair_{pair_id}"
        row_e = {
            "system_id": f"inv_{sid}",
            "row_kind": "system",
            "family": "context_pair",
            "group_id": gid,
            "role": "same_amount_exact",
            **me,
            "notes": "descriptor pair exact",
            "descriptor_dfmi": "",
            "descriptor_idelb": "",
            "descriptor_cl": "",
        }
        sid += 1
        row_f = {
            "system_id": f"inv_{sid}",
            "row_kind": "system",
            "family": "context_pair",
            "group_id": gid,
            "role": "same_amount_fail",
            **mf,
            "notes": "descriptor pair fail",
            "descriptor_dfmi": "",
            "descriptor_idelb": "",
            "descriptor_cl": "",
        }
        sid += 1

        rows.extend([row_e, row_f])
        payload[row_e["system_id"]] = (target, exact_contexts)
        payload[row_f["system_id"]] = (target, fail_contexts)
        pair_id += 1

    # Family C: same-rank single-context opposite-verdict witnesses.
    for ambient in [5, 6, 7, 8]:
        for protected_rank in [2, 3]:
            if protected_rank >= ambient:
                continue
            obs_rank = min(ambient - 1, protected_rank + 1)
            if obs_rank < protected_rank:
                continue
            ex = same_rank_alignment_counterexample(ambient, protected_rank, obs_rank)

            for role, O, exact, res, gap in [
                (
                    "same_rank_exact",
                    ex.exact_observation_matrix,
                    1,
                    float(ex.exact_rowspace_residual),
                    float(ex.exact_collision_gap),
                ),
                (
                    "same_rank_fail",
                    ex.fail_observation_matrix,
                    0,
                    float(ex.fail_rowspace_residual),
                    float(ex.fail_collision_gap),
                ),
            ]:
                target = ex.protected_matrix
                contexts = [O]
                m = _compute_metrics(target, contexts)
                m["rowspace_residual"] = res
                m["collision_gap"] = gap
                m["invariant_exact"] = exact
                m["local_exact_all"] = exact
                m["context_gap"] = 0
                row = {
                    "system_id": f"inv_{sid}",
                    "row_kind": "system",
                    "family": "same_rank_single_context",
                    "group_id": f"sr_{ambient}_{protected_rank}_{obs_rank}",
                    "role": role,
                    **m,
                    "notes": "canonical same-rank witness",
                    "descriptor_dfmi": "",
                    "descriptor_idelb": "",
                    "descriptor_cl": "",
                }
                rows.append(row)
                payload[row["system_id"]] = (target, contexts)
                sid += 1

    # Descriptor-fiber meta rows (DFMI/IDELB/CL) over system rows.
    system_rows = [r for r in rows if r["row_kind"] == "system"]
    dfmi_amt, idelb_amt = _descriptor_stats(
        system_rows,
        lambda r: (r["amount_signature"],),
    )
    dfmi_lift, idelb_lift = _descriptor_stats(
        system_rows,
        lambda r: (r["amount_signature"], int(r["delta_free"]), int(r["delta_c"]), int(r["local_exact_all"])),
    )
    cl = float(idelb_amt - idelb_lift)

    rows.append(
        {
            "system_id": "meta_amount",
            "row_kind": "meta_descriptor",
            "family": "descriptor_fiber",
            "group_id": "",
            "role": "amount_only",
            "n": "",
            "p": "",
            "q": "",
            "k": "",
            "total_budget": "",
            "stack_rank": "",
            "target_rank": "",
            "amount_signature": "meta",
            "local_exact_all": "",
            "invariant_exact": "",
            "exact_stack": "",
            "rank_lb_satisfied": "",
            "null_intersection_dim": "",
            "rowspace_residual": "",
            "collision_gap": "",
            "collision_gap_mode": "",
            "cid": "",
            "context_gap": "",
            "agreement_basis_dim": "",
            "lift_rank": "",
            "lift_residual": "",
            "delta_free": "",
            "delta_c": "",
            "library_rank_gain": "",
            "library_full_feasible": "",
            "restricted_aug_found": "",
            "restricted_aug_rows": "",
            "notes": "descriptor-fiber meta invariant",
            "descriptor_dfmi": dfmi_amt,
            "descriptor_idelb": idelb_amt,
            "descriptor_cl": 0.0,
        }
    )
    rows.append(
        {
            "system_id": "meta_lift",
            "row_kind": "meta_descriptor",
            "family": "descriptor_fiber",
            "group_id": "",
            "role": "amount_plus_lift",
            "n": "",
            "p": "",
            "q": "",
            "k": "",
            "total_budget": "",
            "stack_rank": "",
            "target_rank": "",
            "amount_signature": "meta",
            "local_exact_all": "",
            "invariant_exact": "",
            "exact_stack": "",
            "rank_lb_satisfied": "",
            "null_intersection_dim": "",
            "rowspace_residual": "",
            "collision_gap": "",
            "collision_gap_mode": "",
            "cid": "",
            "context_gap": "",
            "agreement_basis_dim": "",
            "lift_rank": "",
            "lift_residual": "",
            "delta_free": "",
            "delta_c": "",
            "library_rank_gain": "",
            "library_full_feasible": "",
            "restricted_aug_found": "",
            "restricted_aug_rows": "",
            "notes": "descriptor-fiber meta invariant",
            "descriptor_dfmi": dfmi_lift,
            "descriptor_idelb": idelb_lift,
            "descriptor_cl": cl,
        }
    )

    # Stress catalog.
    stress_rows: list[dict[str, Any]] = []
    stid = 0
    base_ids = [r["system_id"] for r in system_rows if int(r["invariant_exact"]) == 1][:MAX_BASE_STRESS]

    for base_id in base_ids:
        target, contexts = payload[base_id]
        base = _compute_metrics(target, contexts, include_library_search=False)

        # Stress 1: target mismatch outside agreement-lift rowspace.
        lift = agreement_operator_recoverability(contexts, target)
        # Recompute lift matrix quickly via available function in context module by importing there would be extra.
        # Use stacked contexts rowspace as conservative direction finder.
        stack = np.vstack(contexts)
        direction = _nullspace_rowspace_orth_residual(_random_vector(target.shape[1]), stack)
        if np.linalg.norm(direction) <= TOL:
            direction = _random_vector(target.shape[1])
        mismatch_target = target + direction[None, :]
        m1 = _compute_metrics(mismatch_target, contexts, include_library_search=False)
        stress_rows.append(
            {
                "stress_id": f"str_{stid}",
                "base_system_id": base_id,
                "stress_type": "target_mismatch",
                "stress_param": float(np.linalg.norm(direction)),
                "base_local_exact": int(base["local_exact_all"]),
                "base_invariant_exact": int(base["invariant_exact"]),
                "stressed_local_exact": int(m1["local_exact_all"]),
                "stressed_invariant_exact": int(m1["invariant_exact"]),
                "base_cid": float(base["cid"]),
                "stressed_cid": float(m1["cid"]),
                "base_delta_free": int(base["delta_free"]),
                "stressed_delta_free": int(m1["delta_free"]),
                "base_delta_c": int(base["delta_c"]),
                "stressed_delta_c": int(m1["delta_c"]),
                "base_rowspace_residual": float(base["rowspace_residual"]),
                "stressed_rowspace_residual": float(m1["rowspace_residual"]),
                "base_collision_gap": float(base["collision_gap"]),
                "stressed_collision_gap": float(m1["collision_gap"]),
                "fragility_flag": int(int(base["invariant_exact"]) == 1 and int(m1["invariant_exact"]) == 0),
                "repair_cost_increase": int(m1["delta_free"]) - int(base["delta_free"]),
                "notes": "model-mismatch stress",
            }
        )
        stid += 1

        # Stress 2: family enlargement by one context that is local-exact but incompatible.
        tvec = target[0]
        u = _random_nonparallel(tvec)
        a = int(RNG.integers(-3, 4))
        if a == 0:
            a = 1
        p0, d0 = contexts[0].shape
        extra = np.zeros((p0, d0), dtype=float)
        extra[0] = tvec + a * u
        extra[1] = u
        for rr in range(2, p0):
            extra[rr] = _random_nonparallel(tvec)
        enlarged = [*contexts, extra]
        m2 = _compute_metrics(target, enlarged, include_library_search=False)
        stress_rows.append(
            {
                "stress_id": f"str_{stid}",
                "base_system_id": base_id,
                "stress_type": "family_enlargement",
                "stress_param": 1,
                "base_local_exact": int(base["local_exact_all"]),
                "base_invariant_exact": int(base["invariant_exact"]),
                "stressed_local_exact": int(m2["local_exact_all"]),
                "stressed_invariant_exact": int(m2["invariant_exact"]),
                "base_cid": float(base["cid"]),
                "stressed_cid": float(m2["cid"]),
                "base_delta_free": int(base["delta_free"]),
                "stressed_delta_free": int(m2["delta_free"]),
                "base_delta_c": int(base["delta_c"]),
                "stressed_delta_c": int(m2["delta_c"]),
                "base_rowspace_residual": float(base["rowspace_residual"]),
                "stressed_rowspace_residual": float(m2["rowspace_residual"]),
                "base_collision_gap": float(base["collision_gap"]),
                "stressed_collision_gap": float(m2["collision_gap"]),
                "fragility_flag": int(int(base["invariant_exact"]) == 1 and int(m2["invariant_exact"]) == 0),
                "repair_cost_increase": int(m2["delta_free"]) - int(base["delta_free"]),
                "notes": "enlargement stress",
            }
        )
        stid += 1

        # Stress 3: observation perturbation.
        eps = float(RNG.uniform(1e-4, 3e-2))
        noisy = [m + eps * RNG.normal(size=m.shape) for m in contexts]
        m3 = _compute_metrics(target, noisy, include_library_search=False)
        stress_rows.append(
            {
                "stress_id": f"str_{stid}",
                "base_system_id": base_id,
                "stress_type": "observation_noise",
                "stress_param": eps,
                "base_local_exact": int(base["local_exact_all"]),
                "base_invariant_exact": int(base["invariant_exact"]),
                "stressed_local_exact": int(m3["local_exact_all"]),
                "stressed_invariant_exact": int(m3["invariant_exact"]),
                "base_cid": float(base["cid"]),
                "stressed_cid": float(m3["cid"]),
                "base_delta_free": int(base["delta_free"]),
                "stressed_delta_free": int(m3["delta_free"]),
                "base_delta_c": int(base["delta_c"]),
                "stressed_delta_c": int(m3["delta_c"]),
                "base_rowspace_residual": float(base["rowspace_residual"]),
                "stressed_rowspace_residual": float(m3["rowspace_residual"]),
                "base_collision_gap": float(base["collision_gap"]),
                "stressed_collision_gap": float(m3["collision_gap"]),
                "fragility_flag": int(int(base["invariant_exact"]) == 1 and int(m3["invariant_exact"]) == 0),
                "repair_cost_increase": int(m3["delta_free"]) - int(base["delta_free"]),
                "notes": "noise stress",
            }
        )
        stid += 1

    witness_fields = [
        "system_id",
        "row_kind",
        "family",
        "group_id",
        "role",
        "n",
        "p",
        "q",
        "k",
        "total_budget",
        "stack_rank",
        "target_rank",
        "amount_signature",
        "local_exact_all",
        "invariant_exact",
        "exact_stack",
        "rank_lb_satisfied",
        "null_intersection_dim",
        "rowspace_residual",
        "collision_gap",
        "collision_gap_mode",
        "cid",
        "context_gap",
        "agreement_basis_dim",
        "lift_rank",
        "lift_residual",
        "delta_free",
        "delta_c",
        "library_rank_gain",
        "library_full_feasible",
        "restricted_aug_found",
        "restricted_aug_rows",
        "descriptor_dfmi",
        "descriptor_idelb",
        "descriptor_cl",
        "notes",
    ]

    stress_fields = [
        "stress_id",
        "base_system_id",
        "stress_type",
        "stress_param",
        "base_local_exact",
        "base_invariant_exact",
        "stressed_local_exact",
        "stressed_invariant_exact",
        "base_cid",
        "stressed_cid",
        "base_delta_free",
        "stressed_delta_free",
        "base_delta_c",
        "stressed_delta_c",
        "base_rowspace_residual",
        "stressed_rowspace_residual",
        "base_collision_gap",
        "stressed_collision_gap",
        "fragility_flag",
        "repair_cost_increase",
        "notes",
    ]

    with (OUT / "invariant_witness_catalog.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=witness_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    with (OUT / "invariant_stress_catalog.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=stress_fields)
        writer.writeheader()
        for row in stress_rows:
            writer.writerow(row)

    summary = {
        "seed": SEED,
        "witness_rows": len(rows),
        "stress_rows": len(stress_rows),
        "system_rows": sum(1 for r in rows if r["row_kind"] == "system"),
        "meta_rows": sum(1 for r in rows if r["row_kind"] == "meta_descriptor"),
        "family_counts": dict(Counter(r["family"] for r in rows if r["row_kind"] == "system")),
        "stress_counts": dict(Counter(r["stress_type"] for r in stress_rows)),
        "context_pair_generation": {
            "target_pairs": N_CONTEXT_PAIR_TARGET,
            "achieved_pairs": pair_id,
            "attempts": pair_attempts,
            "max_attempts": MAX_CONTEXT_PAIR_ATTEMPTS,
        },
        "descriptor_meta": {
            "amount_dfmi": dfmi_amt,
            "amount_idelb": idelb_amt,
            "lift_dfmi": dfmi_lift,
            "lift_idelb": idelb_lift,
            "compatibility_lift": cl,
        },
        "status": "EXPLORATION / NON-PROMOTED",
    }
    with (OUT / "summary.json").open("w") as f:
        json.dump(summary, f, indent=2)

    print(f"wrote {OUT / 'invariant_witness_catalog.csv'} ({len(rows)} rows)")
    print(f"wrote {OUT / 'invariant_stress_catalog.csv'} ({len(stress_rows)} rows)")
    print(f"wrote {OUT / 'summary.json'}")


if __name__ == "__main__":
    main()
