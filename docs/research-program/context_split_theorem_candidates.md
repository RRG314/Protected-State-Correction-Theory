# Context Split Theorem Candidates

Status: `EXPLORATION / NON-PROMOTED`

Main track A: conditioned-vs-invariant recoverability.

## Scope

Supported family in this pass:
- finite context sets `C`,
- linear targets `t in R^n`,
- linear observations `M_c in R^{m x n}` with fixed `m` across contexts.

Data reference:
- `data/generated/context_sensitive_recoverability/multicontext_witness_catalog.csv` (`1800` families)
- `local_exact_global_fail_count = 485`

## Theorem Candidate A1 — Conditioned/Invariant Strict Split (Supported Family)

Statement:
There exist context families `{M_c}` and target `t` such that:
1. `forall c`, there exists context-specific decoder `d_c` with `d_c M_c = t` (conditioned exactness),
2. no shared decoder `d_*` satisfies `d_* M_c = t` for all `c` (invariant exactness fails).

Status: `PROVED ON SUPPORTED FAMILY`.

Proof sketch:
Take `M_c = [t + a_c u; u]` with non-parallel `u`, varying coefficients `a_c` across contexts.
For each `c`, choose `d_c = [1, -a_c]` so `d_c M_c = t`.
If one shared `d=[p,q]` existed for all `c`, then `p(t+a_c u)+q u = t` for all `a_c`, forcing contradictory constraints when `a_c` are not all equal.
Hence conditioned exactness does not imply invariant exactness.

Empirical support:
`485` families with `local_exact_all=1` and `shared_exact=0`.

## Theorem Candidate A2 — Shared Decoder Feasibility Criterion

Statement:
Context-invariant exactness holds iff the affine constraint sets
`S_c = {d in R^m : d M_c = t}`
have non-empty intersection.

Status: `PROVED` (linear algebra identity).

Comment:
This is mathematically exact but partly definitional. It is useful as canonical criterion, not standalone novelty.

## Theorem Candidate A3 — CID Characterization

Statement:
`CID_C(t)=0` iff context-invariant exactness holds in the supported family.

Status: `PROVED` (supported family; up to numerical tolerance).

Comment:
This is a direct optimization characterization of A2; additive value is diagnostic convenience.

## Candidate A4 — Descriptor Failure for Context Split

Statement:
Descriptor-only tuples `(n, |C|, m, rank_stack, total_budget, local_exact_all)` do not classify invariant exactness.

Status: `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `16` descriptor groups with opposite `shared_exact` verdicts.
- rank-only mismatch count `497`, budget-only mismatch count `1307` over `1800` families.

## Necessary/Sufficient Conditions (Scoped)

Necessary for invariant exactness:
- conditioned exactness in every context,
- intersection feasibility of affine decoder sets `S_c`.

Sufficient:
- existence of one decoder satisfying all context equations jointly.

Open:
- compact invariant-only condition expressed purely in context geometry without solving the shared system.

## Additive vs Existing OCP Logic

- Additive: explicit contextwise-vs-shared split packaging and witness catalogs.
- Non-additive: row-space and affine-consistency core remains aligned with existing OCP/fiber logic.
