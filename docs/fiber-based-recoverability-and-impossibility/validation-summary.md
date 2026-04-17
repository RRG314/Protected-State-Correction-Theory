# Validation Summary

## Preserved assets

Still preserved under the legacy artifact path for migration safety:
- `data/generated/unified-recoverability/unified_recoverability_summary.json`
- `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv`
- `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv`
- `data/generated/unified-recoverability/noisy_restricted_linear_hierarchy.csv`
- `data/generated/unified-recoverability/control_regime_hierarchy.csv`
- `data/generated/unified-recoverability/restricted_linear_fiber_geometry.csv`
- `data/generated/unified-recoverability/family_enlargement_false_positive.csv`
- `data/generated/unified-recoverability/model_mismatch_stress.csv`
- `data/generated/unified-recoverability/canonical_model_mismatch.csv`
- `data/generated/unified-recoverability/periodic_refinement_false_positive.csv`

## Direct branch tests

- `tests/math/test_unified_limits.py`
- `tests/examples/test_unified_recoverability_examples_consistency.py`
- `tests/consistency/workbench_static.test.mjs`

## Migration safety checks

This branch still preserves:
- theorem IDs,
- proof-status tags,
- artifact generation,
- workbench integration,
- report consistency,
- canonical fiber-based docs plus unified-name compatibility shims.

## Current repo-wide gate state

- full repo gate: passed
- Python: `148 passed`
- Node/workbench: `29 passed`
- markdown link check: passed
- naming consistency: passed

## Current evidence classification

- universal fiber-constant exactness: `PROVED`
- fiber-collision impossibility: `PROVED`
- restricted-linear fiber criterion: `PROVED`
- no rank-only exact classifier theorem: `PROVED`
- fixed-library same-budget anti-classifier theorem: `PROVED`
- noisy weaker-versus-stronger separation theorem: `PROVED`
- family-enlargement false-positive theorem: `PROVED`
- canonical model-mismatch instability theorem: `PROVED`
- model-mismatch drift harness: `VALIDATED`
- periodic refinement false-positive harness: `VALIDATED`
- family-level fiber threshold laws: `PROVED` / `VALIDATED` according to their original branch status
