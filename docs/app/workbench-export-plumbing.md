# Workbench Export and Report Plumbing

## Shared export pipeline
The export path is now split into explicit layers:
- scenario state and share-state serialization: `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/app/scenarioSerialization.js`
- export builders: `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/app/scenarioExports.js`
- export envelope shaping: `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/domain/resultModel.js`
- UI triggers: `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/app.js`

## Export rules
- JSON exports include scenario state, active lab, result envelope, theorem/evidence level, and reproducibility metadata.
- CSV exports are opt-in by lab; unsupported labs return `null` instead of fake CSV.
- Markdown reports are generated from structured analysis, not from DOM text scraping.
- Share links encode sanitized scenario state only.
- Figure exports are intentionally UI-level because they reflect the current displayed visual surface.

## Current limits
- Figure export remains DOM-driven because it exports the visible stage rather than a backend artifact.
- CSV exports remain intentionally selective; not every lab has a meaningful one-row-or-series CSV model.
