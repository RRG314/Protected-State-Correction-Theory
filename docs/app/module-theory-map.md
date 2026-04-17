# Module to Theory Map

This map shows how each workbench module is justified inside the theorem/validation structure. The point is not to inventory features; it is to make evidence boundaries visible.

| Module | Primary role | Evidence class | Key sources |
| --- | --- | --- | --- |
| Structural Discovery Studio | Diagnose structural failure and compare supported repairs | theorem-backed + family-validated | `src/ocp/structural_discovery.py`, constrained-observation and PVRT docs |
| Discovery Mixer / Structural Composition Lab | Compose supported families and check compatibility before interpretation | theorem-backed core + validated composition layer | `src/ocp/discovery_mixer.py`, `docs/discovery-mixer/*` |
| Benchmark / Validation Console | Reproduce known outcomes and export benchmark evidence | validated benchmark layer | `tests/consistency/workbench_static.test.mjs`, `docs/workbench/lib/compute.js` |
| Exact Projection Lab | Exact protected/disturbance projection anchor | proved | `src/ocp/core.py` |
| QEC Sector Lab | Sector-conditioned exact recovery anchor | proved / conditional anchor | `src/ocp/sectors.py`, `src/ocp/qec.py` |
| MHD Projection Lab | Periodic exact projection versus GLM asymptotic comparison | proved + conditional comparator | `src/ocp/mhd.py` |
| CFD Projection Lab | Periodic exactness and bounded-domain obstruction behavior | proved / proved-on-supported-family / no-go | `src/ocp/cfd.py`, `docs/cfd/*` |
| Gauge Projection Lab | Maxwell/Coulomb-gauge projector-compatible extension | conditional kept extension | `docs/physics/maxwell-coulomb-gauge.md` |
| Continuous Generator Lab | Asymptotic correction and finite-time limitation behavior | proved | `src/ocp/continuous.py` |
| No-Go Explorer | Surface canonical impossibility results across branches | proved no-go and rejected-bridge layer | `docs/impossibility-results/*`, `docs/physics/bounded-domain-projection-limits.md` |

## Evidence Rule

A module may expose only what its linked evidence supports. If a behavior is branch-limited or family-specific, the module must preserve that scope in its labels and exports.

## Fiber/Descriptor-Fiber Coverage

Fiber-based and descriptor-fiber results are intentionally integrated into existing modules rather than split into standalone dashboards. Their current role is to sharpen diagnosis and classification boundaries, not to advertise a universal symbolic engine.
