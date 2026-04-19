# Geometry Findings For This Repo (Theorem-Seeking, Falsification-First)

Date: 2026-04-16  
Repository: `repos/ocp-research-program`  
Program context: OCP protected-state correction branches, theorem IDs `OCP-001` to `OCP-053`.

## Scope And Standard Used

This report is repo-native and branch-native.
Only geometry that survives as one of the following is kept:
- exact criterion,
- no-go obstruction,
- quantitative invariant,
- real open-problem leverage.

Rejected by default:
- decorative geometry language,
- universal-unification slogans,
- branch flattening.

## Branch-By-Branch Findings

### 1) Exact finite-dimensional orthogonal projection branch

Existing geometry:
- subspaces `S`, `D`, orthogonality, projector `P_S`, overlap obstruction.

What survives:
- exact projector theorem `OCP-002`, overlap no-go `OCP-003`.

What fails:
- broad non-orthogonal generalization without extra compatibility structure.

Usefulness:
- foundational anchor branch, mathematically clean, low novelty but high structural value.

### 2) Exact sector / QEC branch

Existing geometry:
- sector subspaces, sector overlap, sector-conditioned recovery operators.

What survives:
- exact sector recovery `OCP-019`, sector-overlap no-go `OCP-021`.

What fails:
- any novelty claim beyond conditional QEC anchor without stronger new sector theorem.

Usefulness:
- real theorem branch, but novelty must stay tightly scoped.

### 3) Exact periodic Helmholtz/Leray branch

Existing geometry:
- decomposition into divergence-free plus gradient components,
- exact periodic projector geometry.

What survives:
- exact continuous anchor `OCP-006`, periodic incompressible projection fit `OCP-027`.

What fails:
- naive transfer to bounded-domain exactness.

Usefulness:
- strongest exact continuous anchor in repo.

### 4) Bounded-domain / Hodge / CFD branch

Existing geometry:
- boundary-compatible protected class geometry,
- bounded Hodge decomposition constraints,
- boundary-normal trace as protected-class component.

What survives:
- bounded finite-mode Hodge exact theorem `OCP-044`.

What fails:
- periodic projector transplant (`OCP-023`),
- divergence-only exact bounded recovery (`OCP-028`).

Usefulness:
- highest-value geometry lane for new theorem and new obstruction theory.

### 5) Maxwell / gauge projection branch

Existing geometry:
- transverse/longitudinal split,
- projection-compatible gauge structure.

What survives:
- transverse gauge projection fit `OCP-022` on projection-compatible classes.

What fails:
- broad gauge universalization across branch classes.

Usefulness:
- valid corollary lane, not a standalone unification lane.

### 6) Asymptotic generator branch

Existing geometry:
- invariant split under generator `K`, block coupling, spectral decay structure.

What survives:
- invariant-split generator theorem `OCP-013`, PSD corollary `OCP-014`, mixing no-go `OCP-015`.

What fails:
- finite-time exact recovery in smooth linear-flow branch (`OCP-020`).

Usefulness:
- strong theorem branch with meaningful open robustness problems.

### 7) Constrained-observation / recoverability / restricted-PVRT branch

Existing geometry:
- fibers, row-space/kernel compatibility, collision-gap structure.

What survives:
- fiber exactness `OCP-030`, restricted-linear exactness `OCP-031`, collapse lower bound `OCP-035`,
- same-rank insufficiency `OCP-047`, collision-gap threshold `OCP-043`, minimal augmentation `OCP-045`, exact-regime upper envelope `OCP-046`.

What fails:
- rank-only sufficiency,
- amount-only sufficiency.

Usefulness:
- strongest geometry-based theorem program currently in repo.

### 8) Unified recoverability / impossibility branch

Existing geometry:
- universal fiber-factorization core,
- anti-classifier geometry,
- family-enlargement and model-mismatch geometry.

What survives:
- target coarsening theorem `OCP-048`, no rank-only classifier `OCP-049`, no fixed-library budget-only classifier `OCP-050`, noisy weaker-vs-stronger separation `OCP-051`, family-enlargement false-positive theorem `OCP-052`, canonical model-mismatch instability `OCP-053`.

What fails:
- broad positive universal classifier above fiber level.

Usefulness:
- strongest falsification-first limits branch in repo.

## Geometry Modes (Explicit)

### A. Subspace geometry

Applied to: exact projection, sector/QEC, periodic projection, bounded-mode Hodge.

Status:
- survives where operators and decomposition class are explicit,
- rejected where used as metaphor only.

### B. Operator geometry

Applied to: exact projection, generator branch, constrained-observation linear class.

Status:
- survives strongly through row-space/kernel/block-operator criteria,
- rejected when collapsed to rank-only counts.

### C. Fiber / quotient geometry

Applied to: constrained-observation and unified impossibility branches.

Status:
- survives strongly as exactness/no-go hierarchy backbone,
- rejected in unsupported nonlinear-curvature universal form.

### D. Domain / boundary geometry

Applied to: periodic vs bounded PDE branches.

Status:
- survives strongly; this is where bounded exactness/no-go is decided.

### E. Gauge / orbit geometry

Applied to: Maxwell transverse projection lane.

Status:
- survives on projection-compatible classes,
- rejected as global unification language.

## Theorem-Candidate Status (This Pass)

1. Principal-angle exactness/no-go criterion on supported finite-dimensional families: `PROVED` as reformulation of restricted-linear inclusion criteria.
2. Geometric replacement invariant for same-rank insufficiency: `PROVED` on supported restricted-linear classes.
3. Boundary-geometry obstruction theorem for bounded-domain exact correction: `PROVED` in current obstruction form (`OCP-023`, `OCP-028`).
4. Hodge-compatible exactness theorem on broader explicit bounded families: `PROVED` on finite-mode class (`OCP-044`), broader form `CONDITIONAL`.
5. Quotient/fiber reformulation of weaker-vs-stronger target exactness: forward theorem `PROVED`, converse `DISPROVED`.
6. Geometric stability under small perturbations: broad claim `DISPROVED` without margins; margin-conditioned forms `CONDITIONAL/OPEN`.
7. Geometric collapse theorem under coarse observation: `PROVED` on supported classes (`OCP-035`, `OCP-043`, `OCP-046`).
8. Gauge-orbit exactness theorem on projection-compatible classes: `PROVED` on that class; broad extension `OPEN`.

## Hard Falsifications Kept

1. No rank-only exact classifier (`OCP-049`).
2. No fixed-library budget-only exact classifier (`OCP-050`).
3. Bounded-domain transplant failure (`OCP-023`).
4. Divergence-only bounded exact recovery no-go (`OCP-028`).
5. Finite-time exactness impossibility for smooth linear flows (`OCP-020`).

These are central results, not side notes.

## New Invariant Decision

Stronger-than-rank invariant that matters in this repo:
- protected/observation alignment invariant (row-space inclusion defect; principal-angle equivalent in supported linear class),
- plus collision-gap quantitative obstruction.

Rank/count/budget alone is not sufficient.

## Open-Problem Attackability (Improved)

Most improved attack surfaces after this pass:
1. bounded-domain exactness/obstruction classification beyond current finite-mode theorem,
2. weighted-cost anti-classifier theorem extending `OCP-050`,
3. robust noisy/enlarged-family extension of collision-gap and augmentation logic,
4. perturbation fragility vs margin-protected stability boundary in restricted-linear geometry.

## Novelty Classification (Repo-Honest)

Repo-new:
- integrated anti-classifier + false-positive + model-mismatch theorem package as one limits lane,
- bounded-domain positive/negative geometry split with explicit theorem/no-go pair.

Likely literature-known:
- base projector and Hodge/gauge/fiber factorization foundations,
- basic row-space/kernel equivalences.

Literature-unclear:
- exact packaging strength of fixed-library budget anti-classifier plus family-enlargement theorem layer.

Plausibly literature-distinct:
- branch-safe theorem/falsification architecture that proves where amount-only language fails while preserving executable witnesses.

## Final Program Decision

Geometry should be pursued next in:
- bounded-domain geometry,
- constrained-observation/fiber geometry,
- asymptotic operator geometry.

Geometry should be rejected next in:
- universal amount-only/rank-only/budget-only narratives,
- boundary-oblivious projector claims,
- global quotient/gauge unification slogans.

## Linked Repo Deliverables

Canonical consolidated report (this file):
- `docs/research-program/GEOMETRY_FINDINGS_FOR_REPO_2026-04-16.md`

Detailed pass artifacts:
- `docs/research-program/geometry-pass-2026-04-16/`
