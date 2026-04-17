# Branch-By-Branch Geometry Opportunity Table

This table is restricted to the eight required branches and uses current claim/test support only.

## Geometry Tested

Tested across branches:
- subspace geometry (orthogonality, overlap, sector intersections),
- operator geometry (kernel/image/row-space structure),
- fiber/quotient geometry (target constancy on fibers),
- domain/boundary geometry (boundary-trace compatibility),
- gauge/orbit geometry (projection-compatible gauge directions).

## Opportunity Matrix

| Branch | Existing Geometric Objects | Geometry Type | Already Secretly Geometric? | Strongest Current Result | Geometry Headroom | Geometry Failure Risk | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1. Exact finite-dimensional orthogonal projection | `H = S \oplus D`, orthogonal projectors `P_S`, `P_D`, overlap `S \cap D` | subspace geometry + operator geometry | Yes | `OCP-002`, `OCP-003` | principal-angle/no-overlap diagnostics, perturbation fragility quantification | low for exact class, high for forced non-orthogonal generalization | Keep as backbone; add diagnostics, not rebranding |
| 2. Exact sector / QEC | sector subspaces `D_i`, pairwise overlaps, syndrome-conditioned operator `\sum_i B_S B_i^+ Q_i` | subspace geometry + sector/orbit-like geometry | Yes | `OCP-019`, `OCP-021`, conditional `OCP-005` | overlap geometry and detector ambiguity bounds can sharpen | high novelty-overclaim risk (close to standard QEC language) | Keep narrow; only retain theorem-grade overlap/distinguishability results |
| 3. Exact periodic Helmholtz/Leray | decomposition `B = B_df + \nabla \phi`, Leray projector, orthogonality residual | subspace geometry + operator geometry + domain geometry (periodic) | Yes | `OCP-006` | projector-quality and subspace-gap stability phrasing | low in periodic setting | Keep; strongest continuous exact anchor |
| 4. Bounded-domain / Hodge / CFD | bounded protected class with boundary-trace constraints, stream/gradient mode families, bounded projector | domain/boundary geometry + Hodge geometry + operator geometry | Yes | no-go `OCP-023`, `OCP-028`; positive subcase `OCP-044`; conditional class `OCP-029` | strongest open theorem lane: boundary obstruction/classification | high if boundary data treated as optional | Invest heavily; geometry is essential, not optional |
| 5. Maxwell / gauge projection | transverse/longitudinal split, Coulomb-gauge projector, gauge-invisible directions | gauge/orbit geometry + projector geometry | Mostly yes (as corollary) | `OCP-022` | quotient-by-gauge language can cleanly align with projector class | high if pushed beyond projection-compatible domains | Keep as corollary lane, avoid universal claims |
| 6. Asymptotic generator | invariant split under `K`, block form, mixing block `P_S K P_D`, decay on disturbance block | operator geometry + spectral geometry | Yes | `OCP-013`, `OCP-014`, `OCP-015`, `OCP-020` | robust perturbation geometry, nonnormal obstruction analysis | medium if extending beyond split-preserving class | Invest; high theorem potential |
| 7. Constrained-observation / recoverability / restricted-PVRT | fibers, row spaces, kernels, collision gaps, nested record refinements | fiber/quotient geometry + operator geometry | Yes | `OCP-030`–`OCP-043`, `OCP-045`–`OCP-047` | principal-angle/inclusion-defect sharpening, weighted-cost geometry | medium if over-generalized to unsupported nonlinear classes | Invest heavily; strongest geometry payoff |
| 8. Unified recoverability / impossibility | universal fiber exactness, anti-classifier package, family enlargement/mismatch | fiber/quotient geometry + model-class geometry | Yes | `OCP-048`–`OCP-053` | clearer geometric anti-universal statement across fields | high if forced into one positive universal law | Keep as limits branch; unify only where proven |

## Branch-Level Keep/Reject Notes

1. Keep geometry in branches 1, 3, 4, 6, 7, 8 as theorem/no-go critical structure.
2. Keep branch 2 geometry only when sector overlap and distinguishability are explicit, test-backed, and theorem-linked.
3. Keep branch 5 geometry only as projection-compatible gauge corollary.
4. Reject any cross-branch proposal that removes domain assumptions, boundary assumptions, or admissible-family assumptions.

## What Survived

- branch-local geometry that yields exactness criteria, no-go obstructions, or executable invariants.

## What Failed

- universal geometry claims that flatten branch assumptions into one amount-only or quotient-only story.

## Novelty Tiering (Per Table)

Repo-new (strongest in this table):
- branch 4 bounded-domain positive/negative split packaged as obstruction + restricted exact class,
- branches 7/8 anti-classifier and false-positive package tied to fiber geometry.

Likely literature-known:
- branch 1 and branch 3 projector geometry core,
- branch 5 gauge projector core,
- much of branch 2 base QEC-sector structure.

Literature-unclear:
- exact theorem-level framing of branch 8 family-enlargement/model-mismatch package as a unified limits lane.

Plausibly literature-distinct:
- branch 7 + 8 combined theorem/falsification/executable-witness workflow for anti-amount exactness boundaries.

## Next Moves

1. Branch 4: pursue boundary obstruction theorem family.
2. Branch 6: pursue perturbation-robust split criteria with explicit geometric margins.
3. Branch 7/8: pursue weighted-cost geometry-constrained anti-classifier theorem.
