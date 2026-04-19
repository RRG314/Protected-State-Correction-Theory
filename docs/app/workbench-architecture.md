# Workbench Architecture

The workbench now follows a layered static-web architecture inside `docs/workbench`.

## Layer map

### Layer A — Domain model
Files:
- `docs/workbench/lib/domain/defaultState.js`
- `docs/workbench/lib/domain/resultModel.js`
- `docs/workbench/lib/domain/templates.js`
- `docs/workbench/lib/domain/workbenchCatalog.js`
- `docs/workbench/lib/domain/discoveryMixerCatalog.js`

Responsibilities:
- scenario defaults
- lab metadata
- template libraries
- typed mixer catalog entries
- export/result-envelope schema helpers

### Layer B — Engine layer
Files:
- `docs/workbench/lib/engine/core/linearAlgebra.js`
- `docs/workbench/lib/engine/exactLabs.js`
- `docs/workbench/lib/engine/recoverabilityEngine.js`
- `docs/workbench/lib/engine/benchmarkConsole.js`
- `docs/workbench/lib/engine/physicsEngine.js`
- `docs/workbench/lib/engine/continuousEngine.js`
- `docs/workbench/lib/engine/noGoEngine.js`
- `docs/workbench/lib/engine/discoveryMixerEngine.js`

Responsibilities:
- theorem-backed and family-specific calculations
- regime classification
- diagnostics and augmentation logic
- benchmark derivation
- discovery-mixer structural analysis

The public entrypoints remain thin facades:
- `docs/workbench/lib/compute.js`
- `docs/workbench/lib/discoveryMixer.js`

### Layer C — Data and artifact layer
Files:
- `docs/workbench/lib/data/validationSnapshot.js`
- `docs/workbench/lib/generatedValidationSnapshot.js`

Responsibilities:
- generated validation snapshot loading
- stable frontend-facing validation payloads
- bridge between generated repo artifacts and the live benchmark surface

### Layer D — Application and orchestration layer
Files:
- `docs/workbench/lib/app/analysisDispatcher.js`
- `docs/workbench/lib/app/scenarioSerialization.js`
- `docs/workbench/lib/app/scenarioExports.js`
- `docs/workbench/lib/app/scenarioStore.js`
- `docs/workbench/app.js`

Responsibilities:
- scenario persistence and share-state
- analysis dispatch by active lab
- export/report orchestration
- workbench shell orchestration and event wiring

`app.js` is still the largest single file in the workbench. After this refactor it is narrower: it no longer owns catalog constants, chart primitives, or scenario persistence logic, but it still owns lab-specific rendering and event hookup.

### Layer E — Presentation layer
Files:
- `docs/workbench/lib/ui/charts.js`
- `docs/workbench/styles.css`
- `docs/workbench/index.html`

Responsibilities:
- chart SVG generation
- heatmap rendering
- matrix tables
- layout and visual system

## Dependency rules
- Domain modules must not import UI.
- Engine modules must remain UI-agnostic.
- Data modules must expose structured payloads, not DOM fragments.
- App modules may depend on domain, engine, and data.
- UI modules may depend on shared formatting helpers but not on theorem logic.
- `app.js` may orchestrate across layers, but new mathematical logic should not be added there.

## What remains intentionally specialized
These parts stay in `app.js` for now because they are still highly lab-specific and coupled to the current static-page rendering model:
- lane-specific form rendering
- lane-specific narrative copy
- lane-specific event bindings
- time/playback toolbar behavior

Those are the next candidates for extraction only if the rendered lab surfaces continue to stabilize under the current result model.
