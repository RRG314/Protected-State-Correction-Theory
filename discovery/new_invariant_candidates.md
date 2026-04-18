# New Invariant Candidates

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This file lists candidate invariants tested in this pass and preliminary disposition.

## Candidate Set

1. **Context-Coherence Defect (CCD)**
- Idea: minimal disagreement residual among per-context decoder equations.
- Intended gain: classify local-exact/global-fail cases beyond amount-only descriptors.
- Preliminary status: `PLAUSIBLY DISTINCT` (context branch), `PROVED ON SUPPORTED FAMILY` for zero-test equivalence to shared exactness through CID relation.

2. **Augmentation Deficiency Pair `(delta_free, delta_C)`**
- Idea: split unconstrained augmentation need from candidate-library-constrained deficiency.
- Intended gain: distinguish “in-principle repairable” from “repair blocked by candidate set geometry”.
- Preliminary status: `PLAUSIBLY DISTINCT` + `PROVED ON SUPPORTED FAMILY` (candidate-library no-go signals).

3. **Descriptor-Lift Compatibility Invariant (CL)**
- Idea: reduction in irreducible descriptor error when compatibility channels are added to amount-only descriptors.
- Intended gain: quantifiable anti-classifier repair signal.
- Preliminary status: `PLAUSIBLY DISTINCT` (descriptor layer), `PROVED ON SUPPORTED FAMILY`.

4. **Mixedness-Depth by Descriptor Fiber (MDDF)**
- Idea: refine DFMI by weighted target-spread depth inside mixed fibers.
- Intended gain: distinguish mild vs severe descriptor ambiguity.
- Preliminary status: `CONDITIONAL`; definition proposed, limited testing so far.

5. **Family-Enlargement Fragility Index (FEFI)**
- Idea: minimal enlargement size (or fraction of added contexts) needed to flip exactness.
- Intended gain: convert enlargement counterexamples into a quantitative fragility invariant.
- Preliminary status: `VALIDATED / NUMERICAL ONLY`.

6. **Mismatch Instability Slope (MIS)**
- Idea: derivative-like error growth against subspace distance under decoder mismatch.
- Intended gain: predictive instability budget for off-family deployment.
- Preliminary status: `OPEN`; current mismatch data too small.

7. **Boundary-Compatibility Defect (BCD)**
- Idea: domain/decomposition incompatibility residual for bounded-domain projection recoverability.
- Intended gain: explain geometry/domain split beyond rank or budget.
- Preliminary status: `CONDITIONAL`; branch-specific evidence but no unified cross-branch theorem yet.

8. **Quantum Alignment Ratio (branch-limited)**
- Idea: target-specific classical-to-quantum information alignment ratio.
- Intended gain: measurement-design diagnostics in quantum sub-branch.
- Preliminary status: mostly `KNOWN / REFRAMED`, with narrow restricted identity results retained as `PROVED ON RESTRICTED CLASS`.

## Immediate keep/drop recommendation

- Keep for theorem pressure now:
  - `(delta_free, delta_C)` pair
  - CL
  - CCD (context-coherence variant)
- Keep as exploratory diagnostics:
  - FEFI
  - MIS
  - MDDF
- Keep branch-limited only:
  - BCD (PDE/physics branch)
  - quantum alignment ratio
