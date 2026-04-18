# Positive Theorem Candidates

Status labels used:
- `PROVED`
- `PROVED ON SUPPORTED FAMILY`
- `KNOWN / REFRAMED`
- `VALIDATED / NUMERICAL ONLY`
- `CONDITIONAL`
- `DISPROVED`
- `OPEN`

Primary evidence:
- `data/generated/positive_framework/positive_witness_catalog.csv`
- `data/generated/positive_framework/positive_counterexample_catalog.csv`
- `data/generated/context_sensitive_recoverability/agreement_operator_witness_catalog.csv`

## PT-1 Characterization Theorem (CORS)

Statement:
For finite linear context system `(L,{M_c})`, let `G = Q M_1` be the agreement-lift matrix. Then
`shared_exact(L,{M_c})` iff `row(L) subseteq row(G)`.

Status:
- `PROVED ON RESTRICTED CLASS`.

Classification:
- `KNOWN / REFRAMED` mathematically,
- `PLAUSIBLY DISTINCT` as architecture packaging.

Failure boundary:
- any positive free defect `rank([G;L]) - rank(G) > 0`.

## PT-2 Strong Sufficiency Theorem (Compatibility Architecture)

Statement:
If a system is compatibility-organized (`row(L) subseteq row(G)`), then exact shared recoverability is guaranteed.

Status:
- `PROVED ON RESTRICTED CLASS`.

Evidence:
- all CORS-positive witness families (`70`) were exact in this pass.

Weakening that fails:
- replacing compatibility by amount-only descriptors fails (`45` descriptor collisions).

## PT-3 Minimality Theorem (Free Completion Size)

Statement:
Let `r_free^* = rank([G;L]) - rank(G)`. Then:
1. augmentation with fewer than `r_free^*` arbitrary shared rows cannot guarantee exactness,
2. augmentation with `r_free^*` rows from residual target component restores exactness.

Status:
- `PROVED ON RESTRICTED CLASS`.

Classification:
- `PLAUSIBLY DISTINCT` branch-limited repair theorem.

## PT-4 Constrained Augmentation Theorem

Statement:
For declared candidate library `C`, define
`delta_C = rank([G;C;L]) - rank([G;C])`.
Then full-library constrained completion is feasible iff `delta_C = 0`.

Status:
- `PROVED ON RESTRICTED CLASS`.

Classification:
- `PLAUSIBLY DISTINCT` constrained-design certificate.

Weakening that fails:
- using only `library_rank_gain` as criterion is insufficient (counterexamples survive).

## PT-5 Context-Consistency Promotion Theorem (Scoped)

Statement:
Local exactness plus compatibility coherence implies shared exactness.

Formal version:
If `forall c: row(L) subseteq row(M_c)` and `row(L) subseteq row(G)`, then `shared_exact`.

Status:
- `PROVED ON RESTRICTED CLASS`.

Classification:
- `KNOWN / REFRAMED` with branch utility.

## PT-6 Descriptor-Lift Theorem Candidate

Statement:
Amount-only signatures fail to classify shared exactness, but amount signature plus compatibility-lift quantities (`CID`, `r_free^*`) separates opposite-verdict pairs on the supported generated family.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `45` same-amount opposite-verdict pairs,
- `45/45` separated by `CID` and `r_free^*`.

Boundary:
- this is finite-family evidence, not universal classifier theorem.

## PT-7 Robustness Theorem Candidate

Candidate:
Margin-based perturbation stability for shared exactness.

Status:
- `CONDITIONAL` / `OPEN` in this pass.

Reason:
- drift studies show fragility can dominate; no clean universal epsilon-gamma law established across generated family classes.

## Positive theorem extraction verdict

Strongest pushable theorem cluster now:
1. compatibility characterization/sufficiency (PT-1/PT-2),
2. minimal free completion law (PT-3),
3. constrained-library completion criterion (PT-4),
4. finite-family descriptor-lift gain (PT-6).

Anything broader should remain conditional.
