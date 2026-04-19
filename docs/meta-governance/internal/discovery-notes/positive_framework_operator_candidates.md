# Positive Framework Operator Candidates

Status: operator discovery for positive architecture framing.

Data anchors:
- `data/generated/positive_framework/positive_witness_catalog.csv`
- `data/generated/positive_framework/positive_counterexample_catalog.csv`

## PO-1 Agreement-Lift Operator

Definition:
`G = Q M_1`, where `Q` spans the context agreement row space.

Role:
- architecture-level shared compatibility operator.

Status:
- mathematical: `PROVED ON RESTRICTED CLASS`
- novelty: `KNOWN / REFRAMED`

Adds theorem power?
- yes for explicit architecture characterization,
- no as independent new algebraic object.

## PO-2 Augmentation Completion Operator

Definition:
`A_complete(L,{M_c}) -> U_*` where `U_*` is minimal residual-row augmentation (free class).

Role:
- constructive repair map.

Status:
- `PROVED ON RESTRICTED CLASS` (free class)
- novelty: `PLAUSIBLY DISTINCT` as design procedure packaging.

## PO-3 Candidate-Library Defect Operator

Definition:
`CLDO = delta_C = rank([G;C;L]) - rank([G;C])`.

Role:
- constrained feasibility certificate for architecture repair.

Status:
- `PROVED ON RESTRICTED CLASS`
- novelty: `PLAUSIBLY DISTINCT` / high overlap risk.

## PO-4 Descriptor-Lift Operator

Definition:
`DL(F) = (amount_signature(F), CID(F), r_free^*(F), delta_C(F))`.

Role:
- resolves amount-only descriptor collisions on supported families.

Status:
- `PROVED ON SUPPORTED FAMILY` (finite generated family)
- novelty: `PLAUSIBLY DISTINCT` finite package.

## PO-5 Model-Consistency Stress Operator

Definition:
`MS(F,L,DeltaL) = shared_exact(F,L+DeltaL)` with `DeltaL` orthogonalized against `row(G)`.

Role:
- probes target-mismatch fragility.

Status:
- `VALIDATED / NUMERICAL ONLY`

## Operator verdict

Survivors with practical mathematical value:
1. `G` (agreement-lift) as canonical compatibility operator,
2. `A_complete` as constructive repair operator,
3. `delta_C` as constrained no-go certificate,
4. descriptor-lift tuple as finite-family decision operator.

No independent broad new operator theory survived.
