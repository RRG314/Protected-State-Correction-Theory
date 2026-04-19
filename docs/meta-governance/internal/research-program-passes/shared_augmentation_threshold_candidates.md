# Shared Augmentation Threshold Candidates

Status: `EXPLORATION / NON-PROMOTED`

Main track B: minimal shared augmentation needed to restore context-invariant exactness.

## Definition (frozen)

For context family `{M_c}` and target `t`, shared augmentation threshold is
`r_*(C,t) = min r` such that there exists shared `U in R^{r x n}` with
`exists d_*: d_* [M_c; U] = t` for all contexts `c`.

In this pass, augmentation search is restricted to a measurement-library candidate set (context rows, basis rows, and row combinations), explicitly excluding direct target-row injection.

## Data

- `data/generated/context_sensitive_recoverability/augmentation_threshold_catalog.csv`
- rows: `506` (all with `local_exact_all=1`, `shared_exact=0`)

Observed threshold distribution (supported families):
- `r*=1`: `347`
- `r*=2`: `159`
- `r*>2`: not observed in this search class

## Candidate B1 — Positive Threshold Existence

Statement:
There exist families where conditioned exactness holds but context-invariant exactness fails and a positive shared augmentation (`r*>0`) is required.

Status: `PROVED ON SUPPORTED FAMILY`.

Evidence:
`506` families satisfy local-exact/global-fail with positive threshold.

## Candidate B2 — Threshold Boundedness in Current Search Class

Statement:
For local-only generator families in this pass, an augmentation is found with `r* in {1,2}` under the restricted measurement-library candidate pool.

Status: `PROVED ON SUPPORTED FAMILY`.

Scope note:
This is a generator- and candidate-pool-bounded result, not a universal bound.

## Candidate B3 — Geometry Dependence

Statement:
`r_*` depends on context geometry (decoder-affine incompatibility), not just budget/rank totals.

Status: `CONDITIONAL` (strong empirical support).

Evidence:
- same descriptor signatures can have opposite shared verdicts,
- threshold values vary (`1` vs `2`) under same high-level family class.

## Candidate B4 — Relation to Existing Delta-Style Augmentation

Claim:
Shared augmentation threshold extends single-context minimal augmentation by adding cross-context compatibility constraints.

Status: `PARTIALLY SURVIVES`.

Assessment:
- Not a replacement for existing `delta` logic.
- Additive only when shared decoder constraints matter.

## Candidate B5 — Candidate-Library Defect Feasibility Law

Objects (agreement-lift form):
- `G = Q M_1` (agreement-lifted matrix),
- candidate library `C`,
- defect `delta_C = rank([G; C; t]) - rank([G; C])`.

Statement:
Full-library constrained augmentation is feasible iff `delta_C = 0`.

Status:
- `PROVED ON RESTRICTED CLASS`.

Current continuation evidence:
- `14` explicit `delta_C > 0` impossibility cases in
  `data/generated/context_sensitive_recoverability/agreement_operator_witness_catalog.csv`.

## Candidate B6 — Library Gain Insufficiency

Statement:
`library_rank_gain >= r_free^*` is necessary but not sufficient for constrained augmentation feasibility.

Status:
- `PROVED ON RESTRICTED CLASS` (deterministic counterexample + continuation sweep).

## Counterpressure / Falsification Notes

1. If augmentation class allows adding `t` directly as a row, thresholds collapse trivially to `1` in many families.
2. Therefore augmentation claims must always specify admissible augmentation class.
3. Current results are robust inside the stated class but not yet generalized.

## Next proof targets

1. necessary and sufficient linear condition for `r*=1` under constrained augmentation pool,
2. lower bounds for `r_*` from affine-set intersection dimension,
3. non-synthetic family tests for threshold persistence.
