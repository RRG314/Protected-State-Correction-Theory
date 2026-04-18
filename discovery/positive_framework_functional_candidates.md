# Positive Framework Functional Candidates

Status: functional discovery for positive architecture and repair.

## PF-1 Context Compatibility Defect

Definition:
`CID(F,L) = min_D max_c ||D M_c - L||`.

Use:
- zero-test for shared exactness,
- severity ranking when exactness fails.

Status:
- `PROVED ON RESTRICTED CLASS` for zero-equivalence,
- `KNOWN / REFRAMED` as object.

## PF-2 Free Architecture Defect

Definition:
`Delta_free(F,L) = rank([G;L]) - rank(G)`.

Use:
- minimal free augmentation count,
- positive architecture defect magnitude.

Status:
- `PROVED ON RESTRICTED CLASS`.

## PF-3 Constrained Architecture Defect

Definition:
`Delta_C(F,L) = rank([G;C;L]) - rank([G;C])`.

Use:
- constrained feasibility certificate,
- no-go boundary for candidate row libraries.

Status:
- `PROVED ON RESTRICTED CLASS`.

## PF-4 Descriptor-Lift Functional

Definition:
`Phi(F) = (amount_signature, CID, Delta_free, Delta_C)`.

Use:
- resolves amount-only collisions on supported finite families.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `45` descriptor collisions separated in generated pair families.

## PF-5 Mismatch Stress Functional

Definition:
`MS(F,L,DeltaL) = CID(F,L+DeltaL) - CID(F,L)` with `DeltaL` chosen outside `row(G)`.

Use:
- measures target-model sensitivity.

Status:
- `VALIDATED / NUMERICAL ONLY`.

## PF-6 Enlargement Fragility Functional

Definition:
`EF(F,L;M_new) = I(shared_exact(F,L)) - I(shared_exact(F U {M_new},L))`.

Use:
- family-enlargement false-positive detection.

Status:
- `PROVED ON SUPPORTED FAMILY` as binary fragility indicator,
- quantitative generalization `OPEN`.

## Functional verdict

Most useful and pushable now:
1. `Delta_free` and `Delta_C` (repair planning),
2. `CID` (coherence defect),
3. `Phi` (finite-family descriptor-lift classifier).

All are branch-limited and should be presented as scoped architecture functionals, not universal invariants.
