# Invariant Expansion Report

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This report audits where existing invariants were expanded, where scope was tightened, and where results remain conditional.

## Data used

- `data/generated/context_sensitive_recoverability/multicontext_witness_catalog.csv` (`1800` rows)
- `data/generated/context_sensitive_recoverability/augmentation_threshold_catalog.csv` (`506` local-exact/global-fail rows)
- `data/generated/context_sensitive_recoverability/agreement_operator_anomaly_catalog.csv` (`87` anomalies)
- `data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.json`
- `data/generated/invariants/invariant_witness_catalog.csv` (`32` system rows)
- `data/generated/invariants/invariant_stress_catalog.csv` (`18` stress rows)

## A. Fiber / Factorization Invariant

Expansion result:
- No change to exact theorem statement; still canonical.
- Expansion work focused on linking factorization exactness to context-sensitive CID and augmentation layers.

Status:
- Exact theorem: `PROVED`.
- Quantitative stability extension: `OPEN`.

## B. Row-space / Kernel Compatibility

Expansion result:
- Retained as the exact restricted-linear criterion.
- Added explicit split between exact collision-gap computation and proxy mode for high-null synthetic sweeps.

New control introduced:
- `collision_gap_mode` in invariant witness output.
- Modes:
  - `exact_low_null_dim`
  - `proxy_rowspace_residual`

Status:
- Exact criterion: `PROVED`.
- Proxy regime: `VALIDATED / NUMERICAL ONLY`.

## C. Minimal Augmentation Deficiency

Expansion result:
- Existing context-sensitive catalogs confirm positive shared augmentation thresholds on local-exact/global-fail families.

Observed (supported family):
- In `augmentation_threshold_catalog.csv` (`506` rows):
  - threshold `1`: `347`
  - threshold `2`: `159`

Status:
- Existence and positivity on supported class: `PROVED ON SUPPORTED FAMILY`.
- Closed-form threshold law across broader classes: `OPEN`.

## D. Collapse Modulus / Collision Gap

Expansion result:
- Clarified where gap acts as exact threshold versus expensive diagnostic.
- Added explicit computational guardrail in invariant pass to avoid misrepresenting high-null numerical sweeps as exact collision-gap evaluations.

Status:
- Low-null exact computation: `PROVED ON SUPPORTED FAMILY`.
- High-null proxy usage: `VALIDATED / NUMERICAL ONLY`.

## E. Descriptor-Fiber Invariants (DFMI / IDELB / CL)

Expansion result:
- Reconfirmed strongest anti-classifier signal in existing descriptor branch.

From `meta_classifier_invariants.json`:
- `rank_tuple_(n,r,k)`:
  - ambiguity rate `1.0`
  - IDELB `0.5`
- `rank_tuple_plus_rowspace_proxy`:
  - ambiguity rate `0.0`
  - IDELB `0.0`
- `budget_tuple_(n,r,selection,cost)`:
  - ambiguity rate `1.0`
  - IDELB `0.285714...`

Compatibility lift:
- CL (rank-only to rank+compatibility proxy) = `0.5` error-lift reduction.

From invariant pass (`summary.json`):
- amount-only: DFMI `0.3478`, IDELB `0.25`
- amount+lift: DFMI `0.0`, IDELB `0.0`
- CL `0.25`

Status:
- Descriptor-fiber anti-classifier lower bounds on supported catalogs: `PROVED ON SUPPORTED FAMILY`.
- Distributional guarantees under broader families: `CONDITIONAL`.

## F. Alignment / Compatibility Candidates

Expansion result:
- Agreement-lift and candidate-library defects were treated as invariant candidates, not theorem promotion.

From `agreement_operator_anomaly_catalog.csv`:
- same-descriptor opposite-invariant verdict: `59`
- candidate-library defect impossibility: `14`
- library-gain-not-sufficient: `14`

Interpretation:
- Rank gain is not sufficient when compatibility direction is wrong.

Status:
- Candidate-library defect no-go (supported class): `PROVED ON SUPPORTED FAMILY`.
- Broad alignment invariant generality: `CONDITIONAL`.

## G. Context-sensitive Local/Global Split Quantities

Expansion result:
- Context gap and CID were stress-tested on both large existing catalogs and new invariant pass.

From multicontext catalog (`1800` rows):
- local exact & shared fail (`context_invariance_gap=1`): `506`
- shared exact: `113`

From invariant pass (`32` rows):
- context gap `1`: `4`
- CID-vs-exactness violations: `0`

Status:
- Gap existence and diagnostic value: `PROVED ON SUPPORTED FAMILY`.
- Necessary/sufficient coherence criterion for full generality: `OPEN`.

## H. Stress Behavior (enlargement, mismatch, perturbation)

Expansion result:
- Added compact stress catalog (`18` rows).
- All stress scenarios flipped previously exact base systems in this sweep.

By type:
- target mismatch: `6/6` fragility flips
- family enlargement: `6/6` fragility flips
- observation noise: `6/6` fragility flips

Status:
- Fragility existence: `PROVED ON SUPPORTED FAMILY`.
- Quantitative rate laws: `VALIDATED / NUMERICAL ONLY`.

## Expansion conclusions

1. Strongest expansions are in context-sensitive and descriptor-fiber quantitative invariants.
2. Augmentation deficiency remains the top constructive invariant lane.
3. Collision-gap remains important but must be scope-labeled by computational regime.
4. Alignment/compatibility candidates are useful and promising, but still branch-limited.
