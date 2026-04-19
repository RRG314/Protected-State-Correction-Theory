# Missing-Pieces Closure Report (MP-1..MP-7)

Date: 2026-04-19  
Repo: `/Users/stevenreid/Documents/New project/repos/ocp-research-program`

Authoritative starting guides used:
- `docs/research-program/structural-information-theory/external-imports/structural_information_theory_comprehensive_report.md`
- `docs/research-program/structural-information-theory/external-imports/adversarial_originality_overlap_usefulness_audit.md`

Generated evidence used in this closure pass:
- `data/generated/structural-information-theory/unified_cross_domain_reduction_metrics.csv`
- `data/generated/structural-information-theory/out_of_family_anti_classifier.csv`
- `data/generated/structural-information-theory/decision_baseline_comparison.csv`
- `data/generated/structural-information-theory/coarse_graining_monotonicity.csv`
- `data/generated/structural-information-theory/stability_checks.csv`
- `data/generated/structural-information-theory/harness_summary.json`

## MP-1 Primitive structural object with explicit axioms

Previous state:
- Fiber/factorization objects existed but were distributed across branch docs; no explicit typed primitive object in code.

External material found:
- `data/imported/structural-information-theory/object_candidate_comparison.csv`
- completion report object proposal (`I=(A,M,T,Pi_M,Pi_T,C_{M,T})`).

Added in this pass:
- `src/ocp/structural_information.py`:
  - `StructuralInformationObject`
  - finite-fiber exactness checker
  - collision witness extraction
  - `collapse_modulus_zero` and `recoverability_defect_mse`.

Current status:
- `CONDITIONAL -> REDUCED GAP`.
- Primitive object now explicit and executable on finite/restricted families.
- Universal axiomatization beyond these family classes remains open.

Next exact closure target:
- Add a formal theorem file proving equivalence between object operations and OCP-030/OCP-031 for declared restricted-linear families.

## MP-2 Stability layer beyond exactness

Previous state:
- Stability language existed; theorem-grade continuity statement above factorization was marked open.

External material found:
- completion report ST-7 (OPEN)
- existing `restricted_linear_stability_report` in `src/ocp/recoverability.py`.

Added in this pass:
- `restricted_linear_stability_bound(...)` in `src/ocp/structural_information.py` with explicit perturbation bound.
- Validation artifact: `data/generated/structural-information-theory/stability_checks.csv`.
- Unit test: `tests/math/test_structural_information.py::test_restricted_linear_stability_bound_holds_on_vertex_box`.

Current status:
- `OPEN -> PROVED (restricted linear box families)`.
- Bound is theorem-grade only on declared finite-dimensional linear class with fixed decoder and bounded coefficient box.

Next exact closure target:
- Extend from vertex-box certification to norm-ball class and noisy estimator perturbations.

## MP-3 Dynamic irreversibility / coarse-graining law

Previous state:
- Mixed static exactness and empirical degradation trends; no explicit law boundary.

External material found:
- gravity surrogate degradation checks (`gravity_theorem_checks.json`)
- completion report ST-6 (validated trend).

Added in this pass:
- finite coarsening-flow operator in `src/ocp/structural_information.py`:
  - `recoverability_flow_defect`
  - `is_monotone`.
- Artifacts:
  - `data/generated/structural-information-theory/coarse_graining_monotonicity.csv`.

Current status:
- `OPEN -> PARTIAL`.
- `PROVED_SANITY`: finite coarsening monotonicity sanity chain.
- `VALIDATED_SURROGATE`: monotone defect growth in black-hole surrogate slices.
- Not promoted as universal dynamic law.

Next exact closure target:
- Prove branch-limited semigroup theorem for declared degradations (Markov/coarsening family class) with explicit assumptions.

## MP-4 Vector-valued quantification layer axioms

Previous state:
- Metrics existed (IDELB/DFMI/CL/ambiguity) but no explicit integrated vector profile and no hard anti-scalar boundary in current run state.

External material found:
- descriptor-fiber artifacts in OCP + imported completion ablations.

Added in this pass:
- Quantized descriptor-fiber metric operators in `src/ocp/structural_information.py`:
  - `descriptor_fiber_metrics`
  - `compatibility_lift`.
- Cross-domain metrics from new harness:
  - `data/generated/structural-information-theory/unified_cross_domain_reduction_metrics.csv`.

Current status:
- `CONDITIONAL -> VALIDATED (restricted diagnostic layer)`.
- Amount-only baseline IDELB remains positive on all scored lanes in this pass; augmented profile reduces obstruction in all scored lanes.
- Not a universal invariant claim.

Next exact closure target:
- Formal non-reducibility theorem: no single scalar of amount-only descriptors classifies exactness on enlarged independent witness classes.

## MP-5 Physics translation theorem boundary

Previous state:
- Some theorem-grade mappings existed; several statements remained interpretive.

External material found:
- imported overlap audit + gravity theorem/killer status files.

Added in this pass:
- explicit surrogate-theorem boundary codified in generated outputs:
  - monotonicity file with per-lane status labels (`PROVED_SANITY`, `VALIDATED_SURROGATE` only).
- citation hardening in formal docs and references.

Current status:
- `CONDITIONAL -> REDUCED GAP`.
- Boundary now explicit: theorem-grade only on declared map classes; Landauer-style content remains context, not promoted theorem.

Next exact closure target:
- Write explicit theorem templates in one physics-boundary doc with assumptions and no-claim clauses.

## MP-6 Unified cross-domain reduction harness

Previous state:
- no single executable harness combining OCP witnesses with imported hidden-state/gravity lanes and baseline comparisons.

External material found:
- imported real-system metrics and gravity metrics.

Added in this pass:
- New executable harness:
  - `scripts/research/run_structural_information_harness.py`.
- Outputs:
  - `unified_cross_domain_reduction_metrics.csv`
  - `out_of_family_anti_classifier.csv`
  - `decision_baseline_comparison.csv`
  - `coarse_graining_monotonicity.csv`
  - `stability_checks.csv`
  - `harness_summary.json`.

Current status:
- `OPEN -> CLOSED (for local restricted program requirements)`.
- Independent out-of-family survival detected (`information_real_system`).

Next exact closure target:
- Add at least one additional independently curated external dataset not generated in this workspace.

## MP-7 SDS boundary discipline / scope control

Previous state:
- prior audits flagged SDS drift risk into theorem-core language.

External material found:
- imported adversarial audit explicitly demotes SDS theorem-core status.

Added in this pass:
- This pass keeps SDS out of theorem-core additions.
- Scope and overlap notes added to core docs.

Current status:
- `OPEN -> PARTIAL`.
- Practical drift reduced, but a repo-wide SDS wording sweep is still needed.

Next exact closure target:
- Add a lint-like claim-status check that fails on SDS theorem-core phrasing without theorem mapping.

## Net Closure Summary

- Closed: MP-6.
- Substantially reduced with executable additions: MP-1, MP-2, MP-4, MP-5.
- Partial progress with explicit boundaries but still open theorem work: MP-3, MP-7.

No universal claims were promoted in this pass.
