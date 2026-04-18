# Invariant Scope Corrections

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This file records scope corrections needed to keep invariant claims mathematically honest.

## 1. Collision Gap Scope Correction

Previous drift risk:
- Treating collision-gap numerics as uniformly exact across synthetic sweeps.

Correction:
- Collision-gap is exact where nullspace dimension is small and exhaustive boundary search is tractable.
- For high-null synthetic sweeps in `data/generated/invariants/invariant_witness_catalog.csv`, values marked with `collision_gap_mode=proxy_rowspace_residual` are diagnostic proxies, not exact collision-gap theorems.

Final status:
- `PROVED ON SUPPORTED FAMILY` (exact low-null regime)
- `VALIDATED / NUMERICAL ONLY` (high-null proxy regime)

## 2. Descriptor-Lift Scope Correction

Previous drift risk:
- Presenting CL (compatibility lift) as a universal invariant improvement.

Correction:
- CL is currently proved on finite descriptor catalogs and supported synthetic families.
- It is a lower-bound improvement on descriptor ambiguity/error in those catalogs, not a universal finite-sample guarantee.

Final status:
- `PROVED ON SUPPORTED FAMILY`
- broader distributional claims: `CONDITIONAL`

## 3. Augmentation Deficiency Scope Correction

Previous drift risk:
- Interpreting observed threshold histograms as a closed-form global law.

Correction:
- Positive thresholds are robustly observed and reproducible in current supported classes.
- Closed-form dependence on context geometry, candidate-library choice, and admissible augmentation sets remains open.

Final status:
- existence: `PROVED ON SUPPORTED FAMILY`
- closed-form global law: `OPEN`

## 4. Context Gap Scope Correction

Previous drift risk:
- Treating context gap (`local exact` minus `shared exact`) as fully characterized by amount descriptors.

Correction:
- Amount descriptors fail repeatedly (large opposite-verdict families exist).
- Context gap requires compatibility/coherence information (agreement-lift or equivalent structural data).

Final status:
- amount-only classification no-go: `PROVED ON SUPPORTED FAMILY`
- universal coherence characterization: `OPEN`

## 5. Alignment/Compatibility Invariant Scope Correction

Previous drift risk:
- Treating compatibility/alignment scores as distinct new invariant class without reduction testing.

Correction:
- Some alignment scores reduce to row-space/fiber logic in restricted classes.
- Keep alignment invariants where they add operational decision power (`delta_C`, library-gain insufficiency).

Final status:
- `delta_C` no-go signal: `PROVED ON SUPPORTED FAMILY`
- generic alignment novelty claim: `CONDITIONAL`

## 6. Branch Spillover Correction (Quantum/PDE)

Previous drift risk:
- importing branch-specific invariants into core claims.

Correction:
- Quantum and PDE invariants remain branch-limited and non-canonical until cross-branch theorem coupling is established.

Final status:
- branch diagnostics: `VALIDATED / NUMERICAL ONLY` or `PROVED ON RESTRICTED CLASS`
- core invariant promotion: `OPEN`

## 7. Stress-Result Interpretation Correction

Previous drift risk:
- reading stress flips as universal rates.

Correction:
- Stress flips establish existence and constructive fragility families.
- Rate claims require larger randomized and benchmark-backed studies.

Final status:
- existence: `PROVED ON SUPPORTED FAMILY`
- rate law: `VALIDATED / NUMERICAL ONLY`
