# Falsification Results: Soliton–Geometry Discovery Pass

Date: 2026-04-16  
Objective: kill weak directions early; retain only theorem-grade or benchmark-grade lanes

## Falsification protocol used

For each candidate direction we asked:
1. Is this already a standard theorem in disguise?
2. Does it rely on vague geometry language without computable structure?
3. Does it collapse outside a coordinate artifact or idealized setting?
4. Can failure be exhibited with explicit perturbations/counterexamples?

---

## Candidate-by-candidate falsification outcomes

### C1. Observation-limited recoverability on restricted soliton manifolds

- **Attempted kill**: “This is just ordinary inverse scattering.”
- **Finding**: not automatically. IST assumes richer/global scattering data than many constrained observation settings.
- **Attempted kill**: “It collapses to trivial linear algebra.”
- **Finding**: symmetry quotients (translation/phase) and nonlinear profile parameterization prevent trivial reduction in general.
- **Outcome**: **SURVIVES** with strict scope restrictions.
- **Status**: **OPEN**

### C2. Projection/reduction preservation theorem/no-go

- **Attempted kill**: “Numerical-analysis literature already settles this fully.”
- **Finding**: broad preservation theory exists, but soliton-manifold-specific exact/no-go criteria under explicit projection classes remain plausibly open in narrow settings.
- **Attempted kill**: “Only consistency-order restatement.”
- **Finding**: can avoid this by tying to manifold invariance or symmetry-respecting defects.
- **Outcome**: **SURVIVES (conditional)**
- **Status**: **OPEN / CONDITIONAL**

### C3. Integrability-defect threshold law

- **Attempted kill**: “Thresholds are purely empirical.”
- **Finding**: risk is real; many published thresholds are heuristic.
- **Counterbalance**: in restricted perturbation families, defect-growth bounds may be derivable and benchmarkable.
- **Outcome**: **PARTIAL SURVIVAL**
- **Status**: **CONDITIONAL**

### C4. Topological-vs-integrable stability comparison

- **Attempted kill**: “Incommensurate mechanisms make theorem comparison meaningless.”
- **Finding**: strong risk confirmed. Comparable perturbation metrics and matched state spaces are hard.
- **Outcome**: **WEAK SURVIVAL only as carefully constrained comparative study**
- **Status**: **OPEN (high risk)**

### C5. Geometry-aware MI localization diagnostics

- **Attempted kill**: “Just feature engineering without theorem content.”
- **Finding**: this failure mode is common; novelty risk is high.
- **Outcome**: **SURVIVES only if tied to provable diagnostic bounds or reproducible benchmark superiority**
- **Status**: **VALIDATION-HEAVY / CONDITIONAL**

### C6. Soliton-surface invariants for prediction

- **Attempted kill**: “Surface reconstructions are explanatory only.”
- **Finding**: often true; predictive gain not automatic.
- **Outcome**: **MOSTLY FAILS as a primary lane**
- **Status**: **ANALOGY ONLY unless a concrete predictive invariant is shown**

### C7. Universal geometry unification

- **Attempted kill**: mechanism mismatch test.
- **Finding**: fails immediately (integrable vs topological vs dissipative stability are structurally different).
- **Outcome**: **REJECTED**
- **Status**: **DISPROVED (as near-term research program)**

---

## Rejected directions (explicit)

1. “One-geometry-to-rule-all-solitons” framing  
   Reason: structural mechanism mismatch; no falsifiable core invariant.

2. Pure immersion-visualization program without predictive theorem target  
   Reason: explanatory but weak theorem leverage.

3. Broad cross-domain plasma/MHD unification claims from soliton analogies alone  
   Reason: high overreach risk and weak falsifiability.

## Surviving directions after falsification

1. **Restricted observation recoverability for soliton manifolds** (best)
2. **Projection-preservation/no-go on explicit manifold class**
3. **Perturbative integrability-defect thresholds in narrow coefficient families**

## Falsification verdict

- The broad/hype lanes were mostly eliminated.
- The most defensible program is narrow, explicit, and theorem-driven with reproducible numerics.
- The surviving program is strong enough to justify immediate scoped work, but not broad novelty claims yet.

## Status summary (required labels)

- PROVED: none new in this discovery pass
- CONDITIONAL: C2, C3, C5
- VALIDATED: literature-backed falsification outcomes and lane filtering
- OPEN: C1, C2, C3, C4
- DISPROVED: C7
- ANALOGY ONLY: C6 unless predictive theorem support appears
