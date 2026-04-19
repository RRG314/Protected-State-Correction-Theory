# Workbench Integration Audit

Date: 2026-04-17
Scope: `docs/workbench/*` + `docs/app/*`

## Objective

Keep the current workbench experience recognizable while ensuring naming, evidence labels, and doc links are consistent with the canonical theory/docs layer.

## Findings

1. Core workbench architecture is stable
- Entrypoint: `docs/workbench/index.html`
- Main runtime: `docs/workbench/app.js`
- Catalog/meta model: `docs/workbench/lib/domain/workbenchCatalog.js`

2. Link surfaces
- Workbench module references point to real docs and existing paths.
- Static asset references in `index.html` are valid.

3. Naming consistency issue detected
- Mixed use of `Recoverability / Observation Studio` and `Structural Discovery Studio` in benchmark-related outputs.
- This created avoidable module-label drift.

## Applied Corrections

Updated module labels to a consistent, mode-specific naming scheme:
- `Structural Discovery Studio (Threshold mode)`
- `Structural Discovery Studio (Boundary mode)`

Files updated:
- `docs/workbench/lib/engine/benchmarkConsole.js`
- `docs/workbench/lib/generatedValidationSnapshot.js`
- `docs/app/tool-qualification-report.md`
- `docs/app/module-theory-map.md`

## Evidence-Level Integration

Workbench status/evidence wording remains aligned with repo standards:
- theorem-backed
- restricted theorem-backed
- validated family-specific
- benchmark empirical
- unsupported

No changes were made to module behavior or computation logic in this pass.

## UX Preservation

Intentionally preserved:
- module layout and navigation,
- card hierarchy and controls,
- export/report flow,
- benchmark/demo workflow.

Only consistency-level copy refinements were applied.
