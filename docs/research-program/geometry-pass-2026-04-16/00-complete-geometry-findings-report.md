# Complete Geometry Findings Report (Falsification-First)

Date: 2026-04-16  
Scope: full OCP research repository geometry exploration pass, branch-by-branch, theorem-seeking, falsification-first.

## 0. Executive Verdict

Geometry is already core mathematical structure in this repository, not decorative language.
The strongest result of this pass is selective survival:
- geometry strongly improves exactness/no-go power in bounded-domain, constrained-observation/fiber, and asymptotic-generator branches,
- geometry is useful but mostly reformulative in some exact projection and sector lanes,
- universal amount-only/rank-only/budget-only claims are decisively falsified,
- universal one-geometry unification claims are rejected.

## 1. Branch Audit: Where Geometry Already Exists

### Branch 1: Exact finite-dimensional orthogonal projection

Geometric objects:
- protected/disturbance subspaces `S, D`,
- orthogonal projectors,
- overlap/intersection obstruction.

Geometry type:
- subspace geometry,
- operator geometry.

Already secretly geometric:
- yes.

Current theorem power:
- strong backbone (`OCP-002`, `OCP-003`).

Potential strengthening:
- diagnostics/robustness language (principal-angle inclusion defects) can sharpen interpretation.

Likely redundancy risk:
- medium if geometry only renames existing projector algebra.

### Branch 2: Exact sector / QEC

Geometric objects:
- sector subspaces `D_i`, sector overlaps, distinguishability structure,
- sector-conditioned recovery operator.

Geometry type:
- subspace geometry,
- sector/orbit-like geometry.

Already secretly geometric:
- yes.

Current theorem power:
- real exact sector theorem and overlap no-go (`OCP-019`, `OCP-021`).

Potential strengthening:
- overlap/transversality diagnostics can sharpen no-go edge.

Likely redundancy risk:
- high novelty-overclaim risk if restated as generic QEC geometry without new theorem content.

### Branch 3: Exact periodic Helmholtz/Leray

Geometric objects:
- decomposition into divergence-free plus gradient components,
- periodic Hodge/Leray projector.

Geometry type:
- subspace geometry,
- operator geometry,
- domain geometry (periodic class).

Already secretly geometric:
- yes.

Current theorem power:
- strongest exact continuous anchor (`OCP-006`, `OCP-027`).

Potential strengthening:
- stability diagnostics, projector-quality perturbation analysis.

Likely redundancy risk:
- low in periodic class.

### Branch 4: Bounded-domain / Hodge / CFD

Geometric objects:
- bounded-domain protected class with boundary structure,
- stream/gradient mode decompositions,
- boundary trace compatibility constraints.

Geometry type:
- domain/boundary geometry,
- Hodge geometry,
- operator geometry.

Already secretly geometric:
- yes.

Current theorem power:
- positive restricted theorem + strong no-go package (`OCP-044`, `OCP-023`, `OCP-028`).

Potential strengthening:
- highest-value open lane: broader boundary-compatible exactness/obstruction theory.

Likely redundancy risk:
- low; geometry is essential here.

### Branch 5: Maxwell / gauge projection

Geometric objects:
- transverse/longitudinal split,
- gauge-invisible directions,
- transverse projector.

Geometry type:
- gauge/orbit geometry,
- projector geometry.

Already secretly geometric:
- mostly yes (corollary-level).

Current theorem power:
- valid exact fit on projection-compatible classes (`OCP-022`).

Potential strengthening:
- clarify quotient/orbit interpretation only where operator class is explicit.

Likely redundancy risk:
- high if generalized beyond projection-compatible assumptions.

### Branch 6: Asymptotic generator

Geometric objects:
- invariant split under `K`, block geometry, disturbance decay spectrum,
- protected-mixing block obstruction.

Geometry type:
- operator geometry,
- spectral geometry.

Already secretly geometric:
- yes.

Current theorem power:
- strong theorem branch (`OCP-013`, `OCP-014`, `OCP-015`, `OCP-020`).

Potential strengthening:
- robust perturbation geometry under controlled off-diagonal mixing.

Likely redundancy risk:
- medium outside split-preserving class.

### Branch 7: Constrained-observation / recoverability / restricted-PVRT

Geometric objects:
- observation fibers,
- row-space/kernel alignment,
- collision-gap geometry,
- nested refinement geometry.

Geometry type:
- fiber/quotient geometry,
- operator geometry.

Already secretly geometric:
- yes.

Current theorem power:
- strongest theorem package in repo (`OCP-030` through `OCP-047`, `OCP-045`, `OCP-046`).

Potential strengthening:
- weighted-cost geometry and robust-noisy/enlarged-family theorem extensions.

Likely redundancy risk:
- medium only when overextended beyond supported restricted classes.

### Branch 8: Unified recoverability / impossibility

Geometric objects:
- universal fiber-factorization exactness core,
- anti-classifier geometry,
- family-enlargement and model-mismatch geometry.

Geometry type:
- fiber/quotient geometry,
- model-class/operator geometry.

Already secretly geometric:
- yes.

Current theorem power:
- strongest negative theorem package (`OCP-048` to `OCP-053`).

Potential strengthening:
- weighted-cost and geometry-constrained anti-classifier extensions.

Likely redundancy risk:
- high if forced into one broad positive universal law.

## 2. Geometry Modes (A-E) With Accept/Reject Decisions

### A. Subspace geometry

Definition in repo language:
- orthogonality/intersection/overlap between protected and disturbance subspaces or sectors.

Applies to:
- branches 1, 2, 3, 4 (restricted bounded families), 6.

Survives where:
- projector exactness/no-go, sector overlap no-go, bounded Hodge subcases.

Rejected where:
- used as vague metaphor without explicit operator/decomposition hypotheses.

### B. Operator geometry

Definition:
- row-space/kernel/image structure, block couplings, spectral decay directions.

Applies to:
- branches 1, 3, 4, 6, 7, 8.

Survives where:
- exactness criteria and no-go thresholds are operator-characterized.

Rejected where:
- reduced to raw rank counts without alignment structure.

### C. Fiber/quotient geometry

Definition:
- fibers as record equivalence classes; exactness as target constancy on fibers.

Applies to:
- branches 7 and 8 primarily, with dictionary bridges into others.

Survives where:
- exact recoverability, anti-classifier theorems, weaker/stronger target hierarchy.

Rejected where:
- used to claim universal nonlinear geometric classification unsupported by current admissible families.

### D. Domain/boundary geometry

Definition:
- geometric structure of domain and boundary traces as part of protected-class definition.

Applies to:
- branches 3 and 4, extension relevance for 5.

Survives where:
- bounded-domain obstruction and boundary-compatible exactness theorems.

Rejected where:
- boundary is treated as secondary afterthought to divergence-only metrics.

### E. Gauge/orbit geometry

Definition:
- invisible gauge directions as orbit classes; correction as orbit-class representative projection.

Applies to:
- branch 5 directly, branch 3 as structural analog.

Survives where:
- projection-compatible operator classes.

Rejected where:
- generalized into cross-branch universal framework without explicit operators/domain assumptions.

## 3. Priority Open Directions: Findings

### 3.1 Bounded-domain exact projection/Hodge/CFD

Survived:
- boundary-compatible finite-mode exact theorem (`OCP-044`),
- strong boundary obstruction no-go (`OCP-023`, `OCP-028`).

Failed:
- naive periodic transplant,
- divergence-only exact recovery language.

Upgrade achieved:
- no-go sharpened into boundary-geometry obstruction (not just empirical mismatch).

### 3.2 Constrained-observation geometry

Survived:
- fiber exactness backbone (`OCP-030`),
- same-rank insufficiency and anti-classifier package,
- weaker-vs-stronger hierarchy with quantitative noisy separation.

Failed:
- rank-only sufficiency claims,
- budget-only sufficiency claims.

Upgrade achieved:
- geometric separator stronger than rank: inclusion defect / row-space residual / collision-gap package.

### 3.3 Gauge/transverse projection geometry

Survived:
- clean shared projector class across Maxwell transverse and periodic projection branches.

Failed:
- broad quotient/gauge universalization.

Upgrade achieved:
- sharper scope control: exact corollary lane, not a new universal theorem lane.

### 3.4 Sector/QEC geometry

Survived:
- exact sector theorem with overlap no-go remains real and useful.

Failed:
- attempts to promote sector geometry as broadly novel beyond current exact-anchor package.

Upgrade achieved:
- sector overlap/detectability interpreted as precise geometric obstruction.

### 3.5 Asymptotic branch geometry

Survived:
- invariant-split and mixing no-go structure as strong operator geometry.

Failed:
- finite-time exact recovery in smooth linear flow branch (`OCP-020`).

Upgrade achieved:
- clearer geometric separation between asymptotic suppression and exact correction regimes.

## 4. Theorem Candidate Attempts: Verdicts

1. Principal-angle exactness/no-go criterion on supported finite-dimensional families:
- `PROVED` as restricted-linear geometric reformulation (equivalent to row-space inclusion).

2. Geometric replacement invariant for same-rank insufficiency:
- `PROVED` on supported restricted-linear classes.

3. Boundary-geometry obstruction theorem for bounded-domain exact correction:
- `PROVED` in obstruction form via existing no-go package.

4. Hodge-compatible exactness theorem on broader explicit bounded families:
- `PROVED` on explicit finite-mode family; `CONDITIONAL` beyond that.

5. Quotient/fiber reformulation of weaker-vs-stronger exactness:
- forward structure `PROVED`; converse equivalence `DISPROVED`.

6. Geometric stability theorem under small perturbations:
- broad form `DISPROVED`; margin-hypothesis forms remain `CONDITIONAL`/`OPEN`.

7. Geometric collapse theorem under coarse observation:
- `PROVED` on supported classes via collapse/collision-gap theorems.

8. Gauge-orbit exactness theorem on projection-compatible classes:
- `PROVED` on projection-compatible classes; broad extension `OPEN/unsupported`.

## 5. Failure Audit (Explicit)

Geometry rejected as non-helpful when it was:
- rank-only/count-only/budget-only relabeling,
- analogy without branch-specific theorem consequences,
- uncomputable under current admissible families,
- weaker than existing theorem statements,
- universalizing beyond validated domain/operator assumptions.

Major rejected directions:
- amount-only geometric classifiers,
- boundary-oblivious projector geometry,
- universal quotient/gauge stories,
- unsupported nonlinear fiber-curvature universals.

## 6. Cross-Branch Separation vs Shared Structure

Accepted shared structures:
- projector class shared by exact orthogonal, periodic Helmholtz/Leray, and Maxwell transverse (under compatible assumptions),
- fiber/row-space/collision geometry shared across constrained-observation and unified impossibility branches.

Rejected forced unifications:
- one universal scalar geometry across all branches,
- one universal threshold law,
- one universal detectability geometry.

Result:
- branch boundaries remain necessary and mathematically productive.

## 7. Required Output Mapping

Produced files:
- repo-wide geometry audit,
- branch-by-branch opportunity table,
- theorem candidate assessment,
- geometry falsification report,
- bounded-domain geometry report,
- constrained-observation/fiber report,
- gauge/quotient report,
- same-rank geometric-invariant report,
- final novelty/usefulness memo.

Directory:
- `docs/research-program/geometry-pass-2026-04-16/`

## 8. Novelty and Usefulness Classification

### Repo-new

- integrated anti-classifier theorem package with executable witnesses (`OCP-049` to `OCP-053` context),
- bounded-domain positive/negative theorem split packaging under one geometry-aware obstruction framework,
- explicit branch-boundary falsification discipline.

### Likely literature-known

- orthogonal projector exactness and overlap no-go basics,
- Helmholtz/Hodge and transverse projection foundations,
- abstract fiber-factorization exactness,
- basic row-space/kernel equivalences.

### Literature-unclear

- exact theorem-level packaging and stress-tested integration of fixed-library same-budget anti-classifier + family-enlargement false-positive + model-mismatch instability in this form.

### Plausibly literature-distinct

- the restricted theorem/falsification package as a coherent anti-universal recoverability-limits program with branch-safe scope control.

## 9. Final Answers (Direct)

1. Where does geometry strengthen the repo?
- strongest in bounded-domain geometry, constrained-observation/fiber geometry, asymptotic operator geometry.

2. Which branches gain real theorem power?
- constrained-observation/unified-impossibility, bounded-domain CFD/Hodge, asymptotic generator branch.

3. New invariant beyond rank/count/budget?
- yes: geometric alignment/inclusion defect with collision-gap quantitative obstruction, on supported restricted-linear classes.

4. Which open problems are more attackable?
- weighted-cost anti-classifier theorem,
- broader bounded-domain exactness/obstruction theorem,
- robust noisy/enlarged-family collision-gap extensions,
- perturbation fragility vs margin-protected stability boundary.

5. Which geometry directions should be rejected?
- universal amount-only/budget-only/rank-only stories,
- boundary-oblivious transplant stories,
- unsupported universal quotient/gauge/unification stories.

6. Any contribution strong enough for new paper lane?
- yes: restricted theorem/falsification lane around anti-classifier and false-positive geometry; bounded-domain lane is a second candidate if broader theorem extension succeeds.

## 10. Recommendation

Continue geometry work where it is theorem-bearing or obstruction-bearing:
- bounded-domain geometry,
- constrained-observation/fiber geometry,
- asymptotic operator geometry.

Demote geometry where it is only analogy, relabeling, or universal overreach.
