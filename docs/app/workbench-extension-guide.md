# Extending the Workbench

## Add a new system family
1. Add or extend domain defaults in `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/domain/defaultState.js`.
2. Add catalog metadata in `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/domain/workbenchCatalog.js` or `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/domain/discoveryMixerCatalog.js`.
3. Implement the analysis logic in a focused engine module under `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/engine`.
4. Expose the engine through the public facade in `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/compute.js` or `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/discoveryMixer.js`.
5. Route the lab in `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/app/analysisDispatcher.js` if it is a top-level workbench lane.
6. Add lab-specific rendering in `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/app.js`.
7. Add static and known-answer validation coverage.

## Add a new exportable result field
1. Add the field to the engine result object.
2. If the field belongs in the shared export envelope, extend `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/domain/resultModel.js`.
3. If the field belongs only to one export format, extend `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/app/scenarioExports.js`.
4. Add regression coverage for JSON/CSV/report output.

## Add a new benchmark or validation snapshot
1. Extend the repo-side generator script under `scripts/compare/`.
2. Regenerate artifacts.
3. Keep frontend loading code in `/Users/stevenreid/Documents/New project/repos/ocp-research-program/docs/workbench/lib/data/validationSnapshot.js` stable unless the artifact schema genuinely changes.
4. Add consistency tests so generated artifacts and frontend use the same truth source.
