# Workbench Data Flow

## Primary flow
1. The user edits a scenario in `docs/workbench/app.js`.
2. `app.js` updates the scenario through `docs/workbench/lib/app/scenarioStore.js`.
3. `scenarioStore.js` sanitizes and persists the scenario through `docs/workbench/lib/app/scenarioSerialization.js`.
4. `scenarioStore.js` calls `docs/workbench/lib/app/analysisDispatcher.js`.
5. `analysisDispatcher.js` routes to the appropriate engine entrypoint in `docs/workbench/lib/compute.js` or `docs/workbench/lib/discoveryMixer.js`.
6. Engine modules return structured analysis objects.
7. `app.js` renders those results into lab-specific UI and shared context panels.
8. Export actions call `docs/workbench/lib/app/scenarioExports.js` so exports are based on structured results, not scraped UI text.

## Share-state flow
- Scenario state is encoded with `encodeShareState`.
- `scenarioStore.js` keeps the hash synchronized through `history.replaceState`.
- Reload and hash changes hydrate via `store.hydrateFromHash(...)`.

## Validation surface flow
- Generated repo-side validation data is loaded through `docs/workbench/lib/data/validationSnapshot.js`.
- The benchmark console consumes that structured snapshot through `docs/workbench/lib/engine/benchmarkConsole.js`.
- The UI reads the benchmark result object instead of reading raw generated files directly.

## Export flow
- JSON export: full scenario plus result envelope
- CSV export: lab-specific numeric series only where structurally meaningful
- report export: scenario plus structured result summary
- figure export: current exportable canvas or SVG surface

## Boundary between theorem-backed and UI logic
- theorem-backed and family-specific calculations live under `lib/engine`
- UI labels and layout live in `app.js` and `lib/ui`
- result-envelope shaping for exports lives in `lib/domain/resultModel.js` and `lib/app/scenarioExports.js`
