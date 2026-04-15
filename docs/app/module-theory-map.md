# Module To Theory Map

| Workbench module | Main result or use | Status | Source code |
| --- | --- | --- | --- |
| Structural Discovery Studio | constrained-observation branch, restricted PVRT spine, collision-gap diagnostics, minimal augmentation logic, weaker-versus-stronger target splits, periodic and control threshold laws, bounded-domain architecture diagnosis, before/after repair flow | active branch / theorem-backed restricted-linear core / family-level threshold and redesign surface | `src/ocp/recoverability.py`, `src/ocp/design.py`, `src/ocp/structural_discovery.py`, `docs/structural-discovery/*.md`, `docs/theory/advanced-directions/constrained-observation-*.md`, `docs/theory/advanced-directions/pvrt-*.md`, `docs/theorem-candidates/pvrt-theorem-spine.md`, `docs/workbench/lib/compute.js` |
| Discovery Mixer / Structural Composition Lab | typed composition across supported families, controlled custom input, compatibility diagnostics, augmentation discovery, random constrained search, before/after repair comparison | theorem-backed restricted-linear core / family-specific validated composition surface / explicit unsupported handling | `src/ocp/discovery_mixer.py`, `docs/discovery-mixer/*.md`, `docs/workbench/lib/discoveryMixer.js`, `docs/workbench/app.js`, `docs/workbench/lib/state.js` |
| Benchmark / Validation Console | validated repair demos, module-health checks, exportable reproducibility layer | validated benchmark and product surface | `scripts/compare/run_structural_discovery_examples.py`, `tests/consistency/workbench_static.test.mjs`, `docs/workbench/lib/compute.js`, `docs/workbench/lib/state.js` |
| Exact Projection Lab | OCP-T1, OCP-N1 | proved | `src/ocp/core.py`, `docs/workbench/lib/compute.js` |
| QEC Sector Lab | OCP-T5, QEC exact anchor | proved / conditional anchor | `src/ocp/sectors.py`, `src/ocp/qec.py`, `docs/workbench/lib/compute.js` |
| MHD Projection Lab | periodic exact continuous anchor, GLM asymptotic branch | proved / conditional | `src/ocp/mhd.py`, `docs/workbench/lib/compute.js` |
| CFD Projection Lab | periodic incompressible projection fit, restricted bounded Hodge exact subcase, divergence-only bounded no-go, bounded-domain transplant failure | proved / restricted exact / no-go | `src/ocp/cfd.py`, `docs/cfd/*.md`, `docs/workbench/lib/compute.js` |
| Gauge Projection Lab | Maxwell / Coulomb-gauge exact-fit extension | kept physics extension | `docs/physics/maxwell-coulomb-gauge.md`, `docs/workbench/lib/compute.js` |
| Continuous Generator Lab | OCP-T3, OCP-C2, OCP-N5, OCP-N7 | proved | `src/ocp/continuous.py`, `docs/workbench/lib/compute.js` |
| No-Go Explorer | overlap, sector ambiguity, mixing, finite-time exactness failure, divergence-only no-go, bounded transplant failure | proved / rejected-bridge layer | `docs/impossibility-results/*.md`, `docs/physics/bounded-domain-projection-limits.md`, `docs/workbench/lib/compute.js` |

## Interpretation Rule

Every module must state one of the following clearly:

- proved theorem-backed result
- restricted exact theorem-backed result
- family-specific validated result
- benchmark-guided empirical surface
- standard-anchor reinterpretation
- kept extension
- rejected bridge or counterexample

No workbench surface should imply a stronger status than the linked theorem or scope document supports.
