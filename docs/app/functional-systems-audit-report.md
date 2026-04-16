# Functional Systems Audit Report

## Scope

This report is the **Lane 2** audit only.

It evaluates whether the system actually works in real use with:
- live workbench workflows
- real calculations
- known-answer cases
- exports
- share-state / reload behavior
- browser/UI truth checks
- benchmark and validation console behavior
- adversarial and unsupported cases

It does **not** treat clean code organization as proof the system works.
It does **not** treat passing tests alone as sufficient proof of correct module behavior.

## Executive Verdict

Current state: **functionally strong inside supported scope**.

The supported tool surface is now good enough for:
- known-case validation
- guided discovery inside supported families
- honest rejection of unsupported symbolic/nonlinear free exploration

It is **not** ready for unsupported free exploration.

## Module-by-Module Functional Status

| Module | Functional status | Real calculations | Export/report | Share/reload | Honest unsupported handling | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Exact Projection Lab | qualified-narrow | yes | report yes, CSV not offered | yes | n/a | Exact theorem anchor reproduces orthogonal exactness and overlap failure correctly. |
| QEC Sector Lab | qualified-narrow | yes | report yes, CSV not offered | yes | n/a | Exact tracked three-qubit sector case works and exports coherently. |
| MHD Projection Lab | qualified | yes | report yes, CSV not offered | yes | n/a | Exact projection vs short GLM split is live and numerically real. |
| CFD Projection Lab | qualified | yes | report yes, CSV not offered | yes | n/a | Periodic exact branch and bounded-domain limitation both survive UI and export checks. |
| Gauge / Maxwell Lab | qualified-narrow | yes | report yes, CSV not offered | yes | n/a | Transverse projection benchmark behaves correctly on the supported anchor case. |
| Continuous Generator Lab | qualified | yes | report yes, CSV not offered | yes | n/a | Finite-time exactness no-go remains separate from asymptotic suppression. |
| No-Go Explorer | qualified | yes | report yes, CSV not offered | yes | yes | Does not invent repairs for structurally rejected cases. |
| Structural Discovery Studio | qualified | yes | report, CSV, share-state all work | yes | yes | Strongest end-to-end diagnosis-to-repair workflow in the workbench. |
| Discovery Mixer / Structural Composition Lab | qualified | yes | report, CSV, JSON, share-state all work | yes | yes | Typed supported composition is real; unsupported nonlinear input is rejected honestly. |
| Benchmark / Validation Console | qualified | yes | report and CSV export work | yes | n/a | Trust surface is live and tied to generated validation snapshot. |

## Known-Answer Recovery Table

Professional known-answer matrix:
- `25/25` passing

Qualified tool matrix:
- `21/21` exact matches

### Major verified lanes

#### Exact / OCP branch
- orthogonal exact recovery: exact match
- overlap / indistinguishability no-go: exact match
- exact sector recovery: exact match

#### Constrained-observation / PVRT branch
- fiber collision exact no-go: exact match
- collapse-modulus lower-bound example: exact match after fixing delta-to-chart-bin drift
- restricted-linear exact no-go and minimal augmentation: exact match
- same-rank exactness / insufficiency split: exact match
- qubit phase-loss no-go and weaker-target exactness: exact match
- periodic cutoff threshold failure/repair: exact match
- diagonal history threshold failure/repair: exact match
- hidden protected direction no-go: exact match

#### Physics-supported lanes
- periodic Helmholtz / GLM split: exact match
- periodic incompressible velocity projection: exact match
- gauge / Maxwell transverse projection: exact match
- bounded-domain transplant failure: exact match
- restricted bounded-domain exact family: exact match
- divergence-only bounded no-go: exact match
- finite-time exactness failure for smooth linear flow: exact match

Reference artifacts:
- [professional_known_results_matrix.csv](../../data/generated/validations/professional_known_results_matrix.csv)
- [tool_known_results_matrix.csv](../../data/generated/validations/tool_known_results_matrix.csv)

## End-to-End Workflow Results

Live browser workflows passed:
- `10/10`
- console errors: `0`
- console warnings: `0`

Validated workflows:
1. exact recovery success workflow
2. guided benchmark route and export
3. failing setup -> diagnosis -> fix -> verified success
4. threshold failure -> cutoff augmentation -> verified exact recovery
5. stronger target fails / weaker target succeeds
6. structured linear mixer failure -> repair -> JSON export
7. unsupported custom input -> honest rejection
8. impossible setup -> no-go explanation -> no fake fix suggested
9. physics example workflow
10. exact impossible / asymptotic possible workflow

Reference:
- [browser_tool_qualification.json](../../data/generated/validations/browser_tool_qualification.json)

## Export / Report Verification Results

### Confirmed working
- JSON export: working on audited modules
- markdown report export: working on audited modules
- share-state encoding and reload: working across audited workflows
- CSV export: working where the lab exposes real series/table data
  - Structural Discovery / Recoverability
  - Benchmark / Validation Console
  - Discovery Mixer

### Important nuance
CSV export is **not** universally available. This is currently handled honestly by showing an alert rather than silently producing fake data.

That means:
- this is **not** fake functionality
- but it is a usability weakness because the global export button remains visible even on labs without CSV output

## Browser / UI Truth Checks

### What was checked
- displayed verdicts against backend calculations
- before/after comparison behavior
- export and reload preservation
- live workflow navigation
- supported vs unsupported case handling
- benchmark console trust surface

### Most important browser/UI finding
A real mismatch was found and fixed:
- the analytic recoverability view reported `selectedDelta = 0.25`
- but was using the nearest chart sample to compute `selectedKappa` and the lower bound
- this produced a quiet UI/backend mismatch

This has now been corrected so selected values are computed at the actual requested delta, not the nearest chart bin.

## Stale / Placeholder / Fake-Functionality Findings

### No confirmed fake functionality in audited supported lanes
The audited modules are using real calculations, not placeholder charts or stale hard-coded verdicts.

### Honest but still weak areas
- global CSV export remains a generic action even when the current lab has no CSV surface
- narrow anchor modules are real, but they are narrow; they should not be read as open-ended analyzers
- generated-artifact consistency checks remain useful for drift detection, but some are still partial/circular rather than fully independent truth validation

## Unsupported Cases That Need Clearer Handling

### Already handled correctly
- nonlinear custom mixer input: rejected explicitly
- out-of-basis custom variables: rejected explicitly
- unsupported free exploration: not promoted as safe

### Still needs clearer product-level affordance
- per-lab export capability is not exposed clearly enough in the UI before the user clicks export
- the workbench still relies on product prose and reports to explain scope limits rather than always making them obvious in the active module controls

## Fixes Applied In The Validation Baseline

- corrected analytic `selectedDelta` / `selectedKappa` / lower-bound drift in the workbench analysis path
- updated regression tests to lock the exact selected analytic values
- strengthened professional known-answer and adversarial audit outputs
- strengthened top-level report consistency with current validation results

## Remaining Failures

No blocking failures remain in the audited supported modules.

Remaining non-blocking limitations:
- unsupported free-form symbolic exploration remains outside safe scope
- CSV export is only partial across labs and should be surfaced more explicitly in the UI
- several artifact-consistency checks are still partial/circular by design and should stay labeled that way

## Final Operational Readiness Assessment

### Safe for known-case validation
- yes

### Safe for guided discovery inside supported families
- yes

### Safe for unsupported free exploration
- no

## Bottom-Line Lane 2 Classification

The workbench is **functionally real and trustworthy inside supported scope**.

Current classification:
- strong for theorem-backed and family-backed validation
- strong for guided discovery and repair workflows inside supported families
- not safe to oversell as an unrestricted symbolic or open-domain exploration engine
