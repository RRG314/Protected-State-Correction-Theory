# OCP Core Paper Positioning Note

Paper: [`papers/ocp_core_paper.md`](../ocp_core_paper.md)

## Likely literature-known background
- Kernel/row-space criteria for linear recoverability in finite-dimensional settings.
- Observability and sensor-placement complexity barriers (NP-hardness, structural constraints).

## Repo-new contributions (within stated scope)
- A theorem-organized anti-classifier package in one restricted-linear framework:
  - same-rank insufficiency,
  - no-rank-only exact classifier,
  - no-fixed-library-budget-only exact classifier.
- Exact minimal augmentation theorem in operational form:
  - `δ(O,L;F)=rank([OF;LF])-rank(OF)` with necessity and sufficiency.
- Explicit status-disciplined examples showing exact/failure/repair transitions.

## Plausibly literature-distinct
- The specific integrated package tying anti-classifier no-go theorems and exact minimal augmentation law into a single recoverability-design narrative may be distinct as a contribution package.

## High-risk claims to avoid without deeper review
- Claiming novelty of the base kernel/row-space exactness criterion itself.
- Claiming universal failure of rank/budget metrics outside restricted-linear family scope.

## Public novelty posture recommended
- Emphasize: precise restricted-class no-go + design theorem package.
- Avoid: universal observability or inverse-problem generalization claims.
