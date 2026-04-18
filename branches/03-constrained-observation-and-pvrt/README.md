# Branch 03 — Constrained Observation and PVRT

## What this branch is
Target recoverability under coarse/constrained observation, including restricted-linear exactness and threshold laws.

## Strongest results
- Fiber/factorization exactness formulation for protected-variable recovery.
- Restricted-linear kernel/row-space exactness criteria.
- Collision-gap and threshold laws on supported families.

## Canonical documents
- [Constrained-observation theorems](../../docs/theorem-candidates/constrained-observation-theorems.md)
- [PVRT theorem spine](../../docs/theorem-candidates/pvrt-theorem-spine.md)
- [Constrained-observation no-go](../../docs/impossibility-results/constrained-observation-no-go.md)
- [Formal core definitions](../../docs/research-program/formal_core_definitions.md)

## Key tests / artifacts
- `tests/math/test_recoverability.py`
- `tests/examples/test_generated_artifact_consistency.py`
- `data/generated/recoverability/`

## Open items
- Extend supported-family theorems to broader structured families without losing exact scope labels.

## Shared infrastructure
Use shared simulation and catalog scripts in `scripts/compare/` and `scripts/context_sensitive/`.
