# Recoverability Paper Claim Status Note

Paper: [`papers/recoverability_paper_final.md`](../recoverability_paper_final.md)

## PROVED Core Claims
1. Exact recoverability iff target is constant on record fibers (factorization criterion).
2. Restricted-linear exactness iff `ker(OF) \subseteq ker(LF)` (equivalently `row(LF) \subseteq row(OF)`).
3. Same-rank insufficiency theorem.
4. No rank-only exact classifier theorem (restricted-linear scope).
5. No fixed-library equal-budget/equal-count exact classifier theorem.
6. Collapse-modulus adversarial lower bound.
7. Nested restricted-linear collision-gap threshold law.
8. Exact-regime upper envelope `kappa(eps) <= ||K||_2 eps` under exact restricted-linear decoding.
9. Same-record weak-vs-strong target split in restricted-linear form.
10. Minimal augmentation theorem:
   `delta(O,L;F)=rank([OF;LF]) - rank(OF)`.

## CONDITIONAL Claims
- None promoted as conditional in the main theorem spine of this paper.

## VALIDATED (Computational Support) Claims
- Finite witness families and stress sweeps in the repository support the theorem package and provide reproducible instances, but the main paper statements are theorem-grade and not promoted from validation alone.

## INTERPRETATION-ONLY Statements
1. Structure-first design guidance for sensor/measurement selection.
2. Practical recommendation to prefer alignment diagnostics over amount diagnostics.

## OPEN / Not Claimed
1. Universal recoverability classifier beyond restricted-linear/support assumptions.
2. Universal scalar capacity law across all observation architectures.
3. Full nonlinear/PDE-wide exact recoverability classification.
