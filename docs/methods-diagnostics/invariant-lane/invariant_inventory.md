# Invariant Inventory

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This inventory normalizes invariant-like objects currently used across the OCP/recoverability ecosystem and labels maturity level.

## Scope Legend

- `Core`: restricted-linear/factorization recoverability spine.
- `Context`: context-sensitive recoverability (local vs shared decoder).
- `Descriptor`: anti-classifier descriptor-fiber analysis.
- `Stress`: enlargement/mismatch/perturbation fragility analysis.
- `Physics`: branch-limited invariants in quantum/PDE lanes.

## Invariants

| Invariant | Precise role | Scope | Type | Current status | Supporting artifacts | Missing work |
|---|---|---|---|---|---|---|
| Fiber constancy / factorization exactness | Exact recoverability iff target is constant on record fibers (equiv. factorization through record map) | Core | Exact characterization | `PROVED` | `src/ocp/recoverability.py`; core theorem docs | Stability margin formalization beyond exact setting |
| Row-space inclusion residual | `||L - L P_row(O)||` or equivalent null-intersection test for restricted-linear exactness | Core | Exact (zero-test), quantitative otherwise | `PROVED` | `restricted_linear_recoverability`, `restricted_linear_rowspace_residual`, `data/generated/recoverability/pvrt_same_rank_counterexample.csv` | Tight perturbation bounds with explicit constants |
| Kernel/null intersection dimension | Dimension of `ker(O) ∩ row(L)^*` (operationalized by null-intersection in report) | Core | Exact obstruction indicator | `PROVED` | `RestrictedLinearRecoverabilityReport.null_intersection_dimension` | Cleaner theorem statement for non-orthonormal family bases |
| Minimal augmentation deficiency (`delta`) | Minimal shared augmentation needed to restore exactness in class | Core+Context | Exact on supported class | `PROVED ON SUPPORTED FAMILY` | `data/generated/context_sensitive_recoverability/augmentation_threshold_catalog.csv` | Closed-form bounds beyond supported family |
| Collapse modulus / collision gap | Maximum protected separation under record collision | Core | Exact in low-null finite classes; diagnostic proxy in high-null sweeps | `PROVED ON SUPPORTED FAMILY` (exact regime), `VALIDATED / NUMERICAL ONLY` (proxy regime) | `restricted_linear_collision_gap`; `data/generated/invariants/invariant_witness_catalog.csv` (`collision_gap_mode`) | Scalable exact computation for high nullspace dimension |
| CID (context-invariance defect) | `min_d max_c ||dM_c - t||`; zero iff shared decoder exists | Context | Exact zero-test + quantitative defect | `PROVED ON SUPPORTED FAMILY` | `src/ocp/context_invariant.py`; `data/generated/context_sensitive_recoverability/multicontext_witness_catalog.csv` | Robust norm/conditioning variants |
| Agreement-lift residual / basis dimension | Agreement operator projects multi-context family into shared-decoder test space | Context | Exact equivalence diagnostic (in supported class) | `PROVED ON SUPPORTED FAMILY` | `agreement_operator_recoverability`; `agreement_operator_witness_catalog.csv` | Formal equivalence proof writeup at theorem-note level |
| Descriptor-Fiber Mixedness Invariant (DFMI) | Fraction of descriptor fibers containing both exact/fail verdicts | Descriptor | Quantitative anti-classifier invariant | `PROVED ON SUPPORTED FAMILY` (finite-catalog level) | `meta_classifier_invariants.json`, `data/generated/invariants/summary.json` | Confidence intervals under randomized sampling |
| Irreducible Descriptor Error Lower Bound (IDELB) | `sum_f min(exact_f, fail_f)/N`; lower bound on any descriptor-only classifier error | Descriptor | Quantitative lower bound | `PROVED ON SUPPORTED FAMILY` | `meta_classifier_invariants.json` | Generalization to weighted descriptor families |
| Compatibility Lift (CL) | Error-lift reduction when descriptor is augmented by compatibility information | Descriptor+Context | Quantitative improvement invariant | `PROVED ON SUPPORTED FAMILY` | `meta_classifier_invariants.json` (`0.5` lift), `data/generated/invariants/summary.json` (`0.25` lift) | Canonical normalization across branches |
| Library defect (`delta_C`) | Candidate-library defect after rank gain; certifies infeasibility if positive | Context+Design | Exact no-go in candidate library class | `PROVED ON SUPPORTED FAMILY` | `agreement_operator_anomaly_catalog.csv` (14 impossibility rows) | Necessary/sufficient conditions for general candidate libraries |
| Model-mismatch instability metric | Error induced by decoder trained on wrong family/subspace | Stress | Diagnostic instability invariant | `VALIDATED / NUMERICAL ONLY` | `data/generated/unified-recoverability/model_mismatch_stress.csv` | Broader witness families and theorem-level upper/lower bounds |
| Family-enlargement fragility indicator | Exactness on narrow family fails on enlarged family | Stress | No-go/fragility indicator | `PROVED ON SUPPORTED FAMILY` (existence), `VALIDATED` (rates) | `family_enlargement_false_positive.csv`; multicontext enlargement anomalies | Rate law vs enlargement geometry |
| Boundary/domain compatibility indicators | Domain/decomposition compatibility controls projection exactness | Physics (CFD/MHD) | Branch diagnostic / conditional invariant | `CONDITIONAL` | CFD/MHD branch docs and generated obstruction catalogs | Unified formal definition and cross-branch theorem test |
| Quantum alignment ratio (`alpha_Q`) | Branch-limited normalized classical-vs-quantum information alignment | Physics (quantum) | Restricted diagnostic identity | `PROVED ON RESTRICTED CLASS` and largely `KNOWN / REFRAMED` | `docs/physics/quantum_alignment_*` | Broad generalization and novelty-risk resolution |

## Inventory Findings

1. The mature exact invariants are still fiber/factorization and row-space/nullspace compatibility criteria.
2. The most mature quantitative invariants are DFMI/IDELB/CL and CID in context-sensitive classes.
3. Augmentation invariants (`delta`, `delta_C`) are the strongest constructive lane beyond pure no-go framing.
4. Collision-gap is mathematically meaningful but computationally expensive in high-null regimes; high-null sweeps now require explicit proxy labeling.
5. Quantum and PDE invariants should remain branch-limited until stronger formal coupling to core exactness is proved.
