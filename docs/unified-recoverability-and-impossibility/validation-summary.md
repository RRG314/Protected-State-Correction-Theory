# Validation Summary

## Executable branch artifacts

Generated in:
- `data/generated/unified-recoverability/unified_recoverability_summary.json`
- `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv`
- `data/generated/unified-recoverability/coordinate_rank_enumeration.csv`
- `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv`
- `data/generated/unified-recoverability/noisy_restricted_linear_hierarchy.csv`
- `data/generated/unified-recoverability/periodic_same_record_target_hierarchy.csv`
- `data/generated/unified-recoverability/control_exact_vs_asymptotic_split.csv`
- `data/generated/unified-recoverability/control_regime_hierarchy.csv`

Built by:
- `scripts/compare/run_fiber_recoverability_examples.py` (legacy unified-name wrapper still preserved)

## Direct tests

Math tests:
- `tests/math/test_unified_limits.py`

Artifact consistency tests:
- `tests/examples/test_unified_recoverability_examples_consistency.py`

## What is checked

1. finite detectable-only witness
2. restricted-linear weaker-versus-stronger witness
3. no-rank-only classifier witness sweep across dimensions
4. exhaustive small-dimension coordinate enumeration showing exact and fail cases coexist at the same ranks
5. fixed-library same-budget enumeration showing exact and fail selections coexist at the same cost
6. noisy restricted-linear weaker-versus-stronger separation with brute-force noise-grid checks
7. periodic same-record target hierarchy consistency
8. exact-versus-asymptotic control split consistency
9. control regime hierarchy consistency
10. generated artifact reproduction from current code

## Evidence classification

- universal factorization exactness: `PROVED`
- coarsening detectability logic: `PROVED`
- no rank-only exact classifier theorem: `PROVED`
- fixed-library budget-only anti-classifier theorem: `PROVED`
- noisy weaker-versus-stronger separation theorem: `PROVED`
- periodic and control witnesses used as field instantiations: `VALIDATED` / branch-backed
- broad universal threshold unification: `DISPROVED` as a promoted claim
