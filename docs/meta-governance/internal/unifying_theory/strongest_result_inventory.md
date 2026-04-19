# Strongest Result Inventory

Date: 2026-04-17
Scope: OCP, soliton-geometry-research, MHD closure paper lane, SDS/engineering layers that survive as serious results.

Status vocabulary used in this inventory:
- `PROVED`
- `PROVED ON SUPPORTED FAMILY`
- `CONDITIONAL`
- `VALIDATED`
- `OPEN`
- `ANALOGY ONLY`
- `REJECTED`

## Inventory Table

| ID | Branch | Result (exact statement form) | Status | Object Type | Captures | Unification Class |
|---|---|---|---|---|---|---|
| INV-01 | OCP core | Exact orthogonal projector recovery on `H = S ⊕ D`, `S ⟂ D` (`OCP-002`) | `PROVED` | operator/state decomposition | exact correction | branch anchor, not universal |
| INV-02 | OCP core no-go | If `S ∩ D ≠ {0}`, exact single-valued recovery fails (`OCP-003`) | `PROVED` | subspace overlap | impossibility by indistinguishability | candidate universal no-go pattern |
| INV-03 | Fiber limits | Exact recoverability iff target is fiber-constant / factors through record (`OCP-030`) | `PROVED` | maps `(A, M, T)` | exactness criterion | **universal core candidate** |
| INV-04 | Restricted-linear | Exactness iff `ker(OF) ⊆ ker(LF)` or `row(LF) ⊆ row(OF)` (`OCP-031`) | `PROVED` | finite-dimensional linear family | structural compatibility | branch-limited strengthening |
| INV-05 | Restricted-linear design | Minimal augmentation law `δ(O,L;F)=rank([OF;LF])-rank(OF)` (`OCP-045`) | `PROVED` | measurement architecture | constructive repair | branch-limited strengthening |
| INV-06 | Anti-classifier | Same-rank insufficiency (`OCP-047`) | `PROVED` | observation family | amount/rank failure | branch-limited core theme |
| INV-07 | Anti-classifier | No rank-only exact classifier (`OCP-049`) | `PROVED` | classifier logic | no amount-only law | branch-limited core |
| INV-08 | Anti-classifier | No fixed-library budget-only exact classifier (`OCP-050`) | `PROVED` | design catalog/budget | no budget-only law | branch-limited core |
| INV-09 | Fragility | Family-enlargement false-positive theorem (`OCP-052`) | `PROVED` | admissible-family nesting | exactness fragility | branch-limited core |
| INV-10 | Fragility | Canonical model-mismatch instability theorem (`OCP-053`) | `PROVED` (with canonical scope) | decoder/family mismatch | instability under wrong model | branch-limited core |
| INV-11 | PDE bounded-domain | Periodic projector transplant fails for bounded protected class (`OCP-023`) | `PROVED` | architecture/domain | architecture mismatch | branch-limited core |
| INV-12 | PDE bounded-domain | Divergence-only bounded no-go (`OCP-028`) | `PROVED` | record insufficiency | detectable but not exact | branch-limited core |
| INV-13 | PDE bounded-domain | Boundary-compatible finite-mode Hodge exact theorem (`OCP-044`) | `PROVED` (restricted) | domain-compatible operator | restricted exactness | branch-limited strengthening |
| INV-14 | Soliton recoverability | Symmetry non-identifiability no-go on restricted one-soliton quotient lane | `PROVED` | quotient manifold `(P/G)` | symmetry-induced ambiguity | restricted exact analogue |
| INV-15 | Soliton recoverability | Same-count opposite-verdict witness package in tested lane | `PROVED ON SUPPORTED FAMILY` + `CONDITIONAL` continuous | observation families | amount/count insufficiency | restricted analogue |
| INV-16 | Soliton projection lane | Projection/reduction split between near-preserving and no-go operators | `VALIDATED` + `CONDITIONAL` theorem | operator class on manifold | preservation vs failure | restricted analogue |
| INV-17 | MHD closure | Constant-`η` exact closure classes on declared cylindrical families | `PROVED` | Euler-potential ansatz families | exact closure | domain branch theorem |
| INV-18 | MHD closure | Variable-`η` obstruction with annular-only nontrivial survivors on supported radial classes | `PROVED ON SUPPORTED FAMILY` | coefficient/domain class | obstruction + survivor split | branch-limited core |
| INV-19 | MHD closure | No smooth axis-touching nonconstant survivor on supported radial classes | `PROVED` (supported class) | domain regularity | topology/boundary obstruction | branch-limited core |
| INV-20 | MHD mixed lane | Mixed tokamak-adjacent constant-`η` factorization + restricted annular variable-`η` exact ODE branch | `PROVED` (restricted) | mixed ansatz family | restricted exact + obstruction | branch-specific strengthening |
| INV-21 | SDS structural-discovery layer | Typed composition + failure diagnosis + repair workflow with evidence labels in supported families | `VALIDATED` | engineering/theorem-linked lab | navigation from impossible to repaired | engineering consequence layer |
| INV-22 | Two-reservoir SDS engineering lane (`topological-adam`) | SDS-gated optimizer branch is real, stable, benchmark-competitive but not default-superior | `VALIDATED` (empirical), superiority `OPEN` | optimization architecture | bounded two-reservoir control effect | adjacent engineering lane only |

## Cross-Inventory Notes

1. The strongest cross-branch abstract object is still `(A, M, T)` with fiber/compatibility logic.
2. “Same amount is not enough” survives strongly in restricted-linear and restricted-soliton families, but is not promoted as a universal theorem over all nonlinear branches.
3. MHD contributes a strong obstruction/survivor domain-compatibility branch, not a direct linear recoverability theorem transfer.
4. SDS contributes serious engineering and navigation layers; current SDS/two-reservoir findings are not promoted as theorem-core mathematics.
