# SFPR Core Definitions

Status: `EXPLORATION / NON-PROMOTED`

This document defines the minimal object system tested for the candidate Structure Formation, Persistence, and Recoverability (SFPR) framework.

## Object Set

### 1) State Space `X`
- Definition: admissible state set for a branch, finite or measurable, with branch-specific constraints.
- Purpose: domain where structure and target are defined.
- Redundancy check: not redundant; needed for fibers, coarsening, and context dependence.
- Reduction test vs OCP: compatible with OCP state space assumptions.
- Theorem usability: high.

### 2) Structure Map `S: X -> ScriptS`
- Definition: map assigning each state a structural descriptor (pattern class, partition, or invariant tuple).
- Purpose: separates "state" from "target-relevant structure".
- Redundancy check: too broad unless `ScriptS` is constrained to target-relevant observables.
- Reduction test vs OCP: if `S = tau`, this collapses to standard target map language.
- Theorem usability: conditional (requires target relevance condition).

### 3) Target Map `tau: X -> T`
- Definition: quantity/property to be exactly recovered.
- Purpose: objective variable for recoverability claims.
- Redundancy check: essential; cannot be removed.
- Reduction test vs OCP: identical role to existing OCP/recoverability notation.
- Theorem usability: high.

### 4) Observation Map `M: X -> Y`
- Definition: record/measurement/coarsening map.
- Purpose: induces indistinguishability fibers and collapse modes.
- Redundancy check: essential.
- Reduction test vs OCP: identical role to constrained-observation core.
- Theorem usability: high.

### 5) Formation Mechanism `F`
- Definition: rule that changes state-structure pair over time or intervention index: `(x, c, u) -> x'` and induced map updates on `(S, tau, M)`.
- Purpose: make structure creation testable instead of narrative.
- Redundancy check: weak if treated as generic dynamics; useful only when tied to recoverability deltas.
- Reduction test vs OCP: partly outside current OCP core, but reducible when only `M` is changed.
- Theorem usability: currently conditional.

### 6) Context Family `C`
- Definition: indexed family `{M_c}` or `{(M_c, D_c)}` over environment/representation contexts.
- Purpose: distinguish contextwise exactness from context-invariant exactness.
- Redundancy check: not redundant; needed for persistence layer.
- Reduction test vs OCP: extends existing context-invariant package.
- Theorem usability: high on supported finite linear families.

### 7) Recovery Map `R`
- Definition: estimator/decoder family with either context-specific `R_c` or shared `R_*` constraints.
- Purpose: precise statement of what "recovered" means.
- Redundancy check: essential.
- Reduction test vs OCP: same object as correction/recovery operator.
- Theorem usability: high.

### 8) Disturbance/Ambiguity Object `D`
- Definition: perturbation, nuisance symmetry, model mismatch, or observation ambiguity operator.
- Purpose: unify fragility and collapse mechanisms.
- Redundancy check: broad; must be typed (`noise`, `coarsening`, `context drift`, `mismatch`) to avoid vagueness.
- Reduction test vs OCP: mostly aligns with nuisance/no-go objects.
- Theorem usability: conditional unless type-restricted.

### 9) Structure-Preserving Map
- Definition: transformation `P` such that target-relevant equivalence classes are unchanged (`tau(x)=tau(x')` implication structure preserved under `P`).
- Purpose: persistence notion stronger than raw state persistence.
- Redundancy check: not equivalent to norm stability.
- Reduction test vs OCP: compatible but not explicit in canonical notation.
- Theorem usability: conditional.

### 10) Structure-Collapsing Map
- Definition: transformation `K` that merges target-distinguishing classes under observation (`M(Kx)=M(Kx')` while `tau(Kx) != tau(Kx')` for some pair).
- Purpose: collapse/no-go object.
- Redundancy check: not redundant; directly tied to indistinguishability failures.
- Reduction test vs OCP: equivalent in substance to collision/fiber no-go in many branches.
- Theorem usability: high.

## Minimal Derived Quantities Used in This Pass

### Target Alignment `a(tau,M)`
- `a = 1 - ||tau - Pi_row(M) tau|| / ||tau||`.
- Role: target-specific measurement quality (linear supported class).
- Reduction test: equivalent to row-space residual normalization.
- Status: `REDUNDANT` with existing linear recoverability geometry; retained as interface quantity only.

### Context-Invariance Defect `CID(C, tau)`
- `CID = min_d max_c ||d M_c - tau||`.
- Role: gap between contextwise and shared-decoder recoverability.
- Reduction test: not reducible to single-context rank/count.
- Status: `PLAUSIBLY DISTINCT` on multi-context families.

### Partition Synergy Index `PSI`
- `PSI = min_i DLS(M_i) - DLS(stack_i M_i)`.
- Role: distributed-allocation gain/loss measure.
- Reduction test: not determined by total budget alone.
- Status: `PLAUSIBLY DISTINCT` (empirical support).

### Intervention Lift `IL`
- `IL = residual(obs) - residual(itv)` at matched measurement count.
- Role: quantifies intervention benefit beyond amount-only descriptors.
- Reduction test: compatible with context-cleaning interpretation.
- Status: `VALIDATED / EMPIRICAL ONLY`.

### Target Sensitivity Floor `TSF`
- `TSF = a(tau,M)^2` in this pass.
- Role: sensitivity proxy for local estimation regimes.
- Reduction test: partially redundant with alignment in linear settings.
- Status: `CONDITIONAL`.

## Definition Filter Outcome

Kept as core SFPR candidates:
- `X, tau, M, C, R`, structure-collapsing map.

Kept conditionally:
- `S`, `F`, typed disturbance object `D`, structure-preserving map.

Demoted as convenience quantities in supported linear classes:
- target alignment `a`, `TSF` (reparameterizations of row-space geometry unless extended beyond linear classes).
