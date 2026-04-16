# Workbench Refactor Report

## What moved
- domain metadata out of `app.js` into:
  - `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/domain/workbenchCatalog.js`
  - `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/domain/defaultState.js`
  - `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/domain/discoveryMixerCatalog.js`
- chart and matrix rendering out of `app.js` into:
  - `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/ui/charts.js`
- analysis dispatch out of `app.js` into:
  - `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/app/analysisDispatcher.js`
- scenario persistence/share-state/export plumbing out of `app.js` into:
  - `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/app/scenarioSerialization.js`
  - `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/app/scenarioExports.js`
  - `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/app/scenarioStore.js`
- engine logic out of the old monolithic compute path into focused engine modules under `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/engine`

## What was split
- `compute.js` -> thin public facade + engine modules
- `state.js` -> thin public facade + serialization/export/domain modules
- `discoveryMixer.js` -> thin public facade + domain catalog + engine module

## What was preserved intentionally
- `app.js` still owns lane-specific rendering and event binding
- stage renderers remain specialized because their UI requirements still differ materially by branch
- exported public interfaces for `compute.js`, `state.js`, and `discoveryMixer.js` were preserved to avoid breaking tests/scripts

## What behavior changed
No mathematical behavior was intentionally changed.

Behavioral plumbing changes:
- `app.js` now hydrates, persists, and routes scenario updates through `scenarioStore.js`
- chart rendering now comes from shared UI helpers rather than inline local helpers
- workbench catalog metadata now has a single shared source

## What was removed
- duplicated inline catalog constants in `app.js`
- duplicated inline chart helper implementations in `app.js`
- local scenario persistence and share-state logic from `app.js`
- monolithic compute-state-store ownership in a single page file

## Current remaining structural risks
- `app.js` is still the largest single frontend file and still mixes orchestration with lab-specific rendering
- result rendering helpers are not yet fully extracted into a shared presentation module
- lane-specific form generation is still specialized rather than schema-driven

## Why this refactor is still worth keeping now
- the core boundaries are real, not cosmetic
- engine logic is now reusable outside the page shell
- state/export/share-state plumbing is now testable as an application service
- chart generation is now reusable and no longer duplicated in the page entrypoint
