# Branch 06 — Invariants and Augmentation

## What this branch is
Invariant program for recoverability classification, repair thresholds, and anti-classifier quantitative lift.

## Strongest results
- Core invariants remain fiber/factorization + row-space/kernel criteria.
- Scoped additive stack: `CID`, `delta_free`, `delta_C`, and descriptor-lift diagnostics.
- Deep stress catalog establishes robust fragility boundaries for overbroad claims.

## Canonical documents
- [Invariant formal audit](../../docs/research-program/invariant_formal_audit.md)
- [Invariant theorem spine (draft)](../../docs/research-program/invariant_theorem_spine_draft.md)
- [Invariant no-go spine (draft)](../../docs/research-program/invariant_no_go_spine_draft.md)
- [Invariant expansion master](../../docs/research-program/invariant_expansion_master.md)
- [Invariant formalization + BH placement master report](../../docs/research-program/invariant_formalization_and_bh_placement_master_report.md)

## Key tests / artifacts
- `data/generated/invariants/deep_invariant_catalog.csv`
- `data/generated/invariants/deep_invariant_stress.csv`

## Open items
- Push formal bounds/theorems for `delta_free` and constrained-feasibility geometry (`delta_C`).

## Shared infrastructure
Common invariant sweeps are executed via `scripts/compare/run_invariant_discovery_pass.py` and `scripts/compare/run_deep_invariant_catalog_pass.py`.
