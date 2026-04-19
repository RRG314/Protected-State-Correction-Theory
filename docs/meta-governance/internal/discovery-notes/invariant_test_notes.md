# Invariant Test Notes

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

Primary generator:
- `scripts/compare/run_invariant_discovery_pass.py`

Primary outputs:
- `data/generated/invariants/invariant_witness_catalog.csv`
- `data/generated/invariants/invariant_stress_catalog.csv`
- `data/generated/invariants/summary.json`

## Test Matrix

## Test A: Compatibility-organized exact families

Question:
- Do compatibility-organized constructions produce invariant exactness with zero augmentation deficiency?

Metric set:
- `invariant_exact`, `cid`, `delta_free`, `rowspace_residual`, `null_intersection_dim`.

Success criterion:
- exact rows have `invariant_exact=1`, `cid≈0`, `delta_free=0`.

Observed:
- satisfied on the compatibility-exact rows.

Conclusion scope:
- supports positive compatibility implication on supported synthetic class.

## Test B: Context pair opposite verdicts

Question:
- Can same-amount constructions yield opposite shared exactness while retaining local exactness?

Metric set:
- `amount_signature`, `local_exact_all`, `invariant_exact`, `context_gap`, `cid`, `delta_free`.

Success criterion:
- paired rows with identical amount signature but opposite invariant verdict.

Observed:
- context-pair rows contain exact/fail opposite verdicts with local exactness maintained in fail rows.

Conclusion scope:
- anti-classifier evidence in context-sensitive setting.

## Test C: Same-rank canonical witnesses

Question:
- Does rank equality fail to classify exactness in canonical linear pairs?

Metric set:
- same `stack_rank`, opposite `rowspace_residual`/`collision_gap` and `invariant_exact`.

Success criterion:
- same rank, opposite exactness.

Observed:
- present across all canonical same-rank witness groups.

Conclusion scope:
- rank-only descriptor no-go supported.

## Test D: Descriptor-fiber meta invariants

Question:
- Does compatibility-lifted descriptor reduce irreducible ambiguity relative to amount-only descriptor?

Metric set:
- DFMI, IDELB, CL.

Success criterion:
- `IDELB(lifted) < IDELB(amount-only)`.

Observed:
- in invariant run summary: amount IDELB `0.25`, lifted IDELB `0.0`, CL `0.25`.
- in existing descriptor branch: rank IDELB `0.5` reduced to `0.0` with compatibility proxy.

Conclusion scope:
- robust descriptor-lift signal on current catalogs.

## Test E: Stress fragility

Question:
- Do target mismatch, enlargement, and noise destroy exactness and increase repair cost?

Metric set:
- `fragility_flag`, `stressed_invariant_exact`, `repair_cost_increase`, `stressed_cid - base_cid`.

Success criterion:
- positive flip counts with defect/cost increase.

Observed:
- `18/18` stress rows flipped (`6/6` per stress type).
- repair-cost increase positive in every row.

Conclusion scope:
- fragility existence established in supported synthetic stress set.

## Collision-gap computation note

Exact question:
- Is collision-gap exactly computed or approximated in each row?

Implementation decision:
- `collision_gap_mode=exact_low_null_dim` when nullspace dimension <= 2.
- `collision_gap_mode=proxy_rowspace_residual` otherwise.

Reason:
- exact collision-gap routine scales combinatorially with nullspace dimension in current implementation.

Interpretation rule:
- only rows marked `exact_low_null_dim` may be used for exact collision-gap theorem statements.
- proxy-mode rows are diagnostic only.

## What these tests do not prove

1. They do not provide global closed-form augmentation laws.
2. They do not establish universal stability constants.
3. They do not establish branch-independent novelty for all candidate invariants.
4. They do not replace core fiber/row-space exact criteria.
