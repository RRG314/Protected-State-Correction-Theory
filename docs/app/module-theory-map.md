# Module To Theory Map

| Workbench module | Main result or use | Status | Source code |
| --- | --- | --- | --- |
| Recoverability / Correction Studio | constrained-observation branch, fiber-separation exactness, collapse-modulus classification, `κ(η)/2` lower bound, restricted-linear design logic, minimal augmentation suggestions, periodic functional-support thresholds, control finite-history versus observer split | active branch / proved core / family-level threshold results / design surface | `src/ocp/recoverability.py`, `src/ocp/design.py`, `docs/theory/advanced-directions/constrained-observation-*.md`, `docs/workbench/lib/compute.js` |
| Exact Projection Lab | OCP-T1, OCP-N1 | proved | `src/ocp/core.py`, `docs/workbench/lib/compute.js` |
| QEC Sector Lab | OCP-T5, QEC exact anchor | proved / conditional anchor | `src/ocp/sectors.py`, `src/ocp/qec.py`, `docs/workbench/lib/compute.js` |
| MHD Projection Lab | periodic exact continuous anchor, GLM asymptotic branch | proved / conditional | `src/ocp/mhd.py`, `docs/workbench/lib/compute.js` |
| CFD Projection Lab | periodic incompressible projection fit, divergence-only bounded no-go, bounded-domain limitation | proved / conditional / no-go | `src/ocp/cfd.py`, `docs/cfd/*.md`, `docs/workbench/lib/compute.js` |
| Gauge Projection Lab | Maxwell / Coulomb-gauge exact-fit extension | kept physics extension | `docs/physics/maxwell-coulomb-gauge.md`, `docs/workbench/lib/compute.js` |
| Continuous Generator Lab | OCP-T3, OCP-C2, OCP-N5, OCP-N7 | proved | `src/ocp/continuous.py`, `docs/workbench/lib/compute.js` |
| No-Go Explorer | OCP-N1, OCP-N5, OCP-N7, OCP-N8, bounded-domain transplant rejection | proved / rejected-bridge layer | `docs/impossibility-results/*.md`, `docs/physics/bounded-domain-projection-limits.md`, `docs/workbench/lib/compute.js` |

## App-To-Proof Rule

Every module must satisfy this rule:
- if the underlying result is proved, say so
- if the underlying branch is conditional, say so
- if the module is a family-level threshold example, say so
- if the module is a design surface built from standard-adjacent results, say so
- if the module is a kept physics extension rather than a new theorem, say so
- if the module is a rejected bridge or counterexample, say so
- and never imply a stronger status than the linked theorem or scope file supports
