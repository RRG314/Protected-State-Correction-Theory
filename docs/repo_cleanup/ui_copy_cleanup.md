# UI Copy Cleanup

Date: 2026-04-17

## Scope

Copy-level cleanup for workbench-facing labels and supporting docs; no UI redesign.

## Changes Made

1. Module label normalization
- Replaced mixed legacy label usage with explicit mode labels:
  - `Structural Discovery Studio (Threshold mode)`
  - `Structural Discovery Studio (Boundary mode)`

2. Report-table consistency
- Updated qualification tables to use the normalized module names.

3. Theory-map consistency
- Updated module map notes so the same labels appear in docs and benchmark outputs.

## Why This Improves Trust

- Removes ambiguity about whether there are separate modules or modes.
- Aligns benchmark outputs with app/module documentation.
- Makes workbench and docs read like one system.

## Intentionally Not Changed

- Visual design language
- Module ordering
- Interaction model
- Export payload schema
- Computation engines

## Follow-Up Guidance

When adding new modules or modes:
1. register canonical label in `workbenchCatalog.js`,
2. reuse exact label in benchmark snapshots,
3. mirror the label in `docs/app/module-theory-map.md`.
