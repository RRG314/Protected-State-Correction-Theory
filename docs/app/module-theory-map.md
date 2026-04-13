# Module To Theory Map

| Workbench module | Main theorem / result | Status | Source code |
| --- | --- | --- | --- |
| Exact Projection Lab | OCP-T1, OCP-N1 | proved | `src/ocp/core.py` and `docs/workbench/lib/compute.js` |
| QEC Sector Lab | OCP-T5, QEC exact anchor | proved / conditional anchor | `src/ocp/sectors.py`, `src/ocp/qec.py`, `docs/workbench/lib/compute.js` |
| MHD Projection Lab | periodic exact continuous anchor, GLM asymptotic branch | proved / conditional | `src/ocp/mhd.py`, `docs/workbench/lib/compute.js` |
| Continuous Generator Lab | OCP-T3, OCP-C2, OCP-N5, OCP-N7 | proved | `src/ocp/continuous.py`, `docs/workbench/lib/compute.js` |
| No-Go Explorer | OCP-N1, OCP-N5, OCP-N6, OCP-N7, OCP-N8 | proved / structural boundary | `docs/impossibility-results/*.md`, `docs/workbench/lib/compute.js` |

## App-To-Proof Rule

Every module must satisfy this rule:
- if the underlying result is proved, say so,
- if the underlying branch is conditional, say so,
- if the module is illustrative only, say so,
- and do not imply a stronger status than the linked theorem file supports.
