# Professional Validation And Discovery Report

## 1. What was tested

- validation architecture and circularity map
- professional known-answer recovery across exact, PVRT, and physics-supported lanes
- dependency and consistency audit across reports, generated artifacts, and workbench outputs
- real user workflows in the live browser
- adversarial red-team cases near thresholds, parser boundaries, and classification edges
- post-qualification discovery search inside supported families

## 2. Validation architecture review

- strong tests: **5**
- partial/circular checks: **3**
- pre-pass missing areas closed: **3**

### Strong tests

- `tests/math/test_core_projectors.py`: direct projector algebra with explicit exact/no-go cases
- `tests/math/test_recoverability.py`: independent collapse, threshold, and restricted-linear checks including naive reference paths
- `tests/math/test_discovery_mixer.py`: typed custom-input rejection and repair behavior on supported families
- `tests/consistency/workbench_static.test.mjs`: UI-side analyzer parity, export integrity, and benchmark/truth-surface regression coverage
- `scripts/compare/run_browser_tool_qualification.mjs`: real browser workflows, export, reload, share-state, and unsupported-case honesty

### Partial or circular checks

- `tests/examples/test_workbench_examples_consistency.py`: good for drift detection, but the generated examples come from the same analyzer family later being checked
- `tests/examples/test_generated_artifact_consistency.py`: recomputes artifacts from the same source modules; useful for stale-output detection, not fully independent truth validation
- `node scripts/compare/build_workbench_examples.mjs`: builds regression fixtures from current workbench analyzers; fixture presence alone does not validate correctness

### Gaps that were missing before this pass

- explicit validation architecture map marking circularity and trust limits
- professional known-answer matrix spanning all major lanes with independent answers
- adversarial red-team cases near thresholds and parser boundaries
- report-level consistency checks tying README/system/final reports to current validation counts
- truth-surface snapshot inside the benchmark console

## 3. Known-answer recovery matrix

- passing known-answer checks: **25/25**

| Case | Category | Expected | Tool | Independent check | Result | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Orthogonal exact recovery | Exact / OCP | exact | exact | exact | exact match | theorem-backed exact anchor |
| Overlap / indistinguishability no-go | Exact / OCP | impossible | impossible | impossible | exact match | theorem-backed no-go anchor |
| Exact sector recovery | Exact / OCP | exact | exact | exact | exact match | theorem-linked QEC anchor |
| Fiber collision exact no-go at analytic ε=0 | Constrained observation / PVRT | impossible | impossible | impossible | exact match | explicit analytic benchmark |
| Collapse-modulus lower-bound example | Constrained observation / PVRT | exact-with-positive-noise-lower-bound | exact-with-positive-noise-lower-bound | exact-with-positive-noise-lower-bound | exact match | analytic lower-bound formula |
| Restricted-linear exact no-go before augmentation | Constrained observation / PVRT | impossible | impossible | impossible | exact match | restricted-linear row-space check |
| Minimal augmentation theorem case | Constrained observation / PVRT | exact-min-1 | exact-min-1 | exact-min-1 | exact match | restricted-linear brute-force augmentation search |
| Weaker target exact on the same restricted-linear record | Constrained observation / PVRT | exact | exact | exact | exact match | restricted-linear weaker-versus-stronger split |
| Same-rank exact case | Constrained observation / PVRT | exact | exact | exact | exact match | restricted-linear capacity check |
| Same-rank insufficiency case | Constrained observation / PVRT | impossible | impossible | impossible | exact match | restricted-linear capacity counterexample |
| Qubit phase-loss no-go | Constrained observation / PVRT | impossible | impossible | impossible | exact match | family-specific analytic qubit formula |
| Qubit weaker target exactness | Constrained observation / PVRT | exact | exact | exact | exact match | family-specific weaker-target split |
| Periodic cutoff threshold failure | Constrained observation / PVRT | impossible | impossible | impossible | exact match | family-specific periodic support threshold |
| Periodic cutoff threshold repair | Constrained observation / PVRT | exact | exact | exact | exact match | family-specific periodic support threshold |
| Periodic lower-complexity functional exactness | Constrained observation / PVRT | exact | exact | exact | exact match | family-specific periodic weaker-target threshold |
| Diagonal history threshold failure | Constrained observation / PVRT | impossible | impossible | impossible | exact match | family-specific control threshold |
| Diagonal history threshold repair | Constrained observation / PVRT | exact | exact | exact | exact match | family-specific control threshold |
| Hidden protected direction remains impossible | Constrained observation / PVRT | impossible | impossible | impossible | exact match | control no-go by unsensed protected direction |
| Periodic Helmholtz / GLM split | Physics-supported lanes | exact-better-than-glm | exact-better-than-glm | exact-better-than-glm | exact match | periodic projection versus damping benchmark |
| Periodic incompressible velocity projection | Physics-supported lanes | exact | exact | exact | exact match | periodic CFD exact branch |
| Gauge / Maxwell transverse projection | Physics-supported lanes | exact-improves-transverse | exact-improves-transverse | exact-improves-transverse | exact match | gauge projection benchmark |
| Naive bounded-domain transplant failure | Physics-supported lanes | impossible | impossible | impossible | exact match | theorem-linked boundary counterexample |
| Restricted bounded-domain exact family | Physics-supported lanes | exact | exact | exact | exact match | restricted exact bounded-domain result |
| Divergence-only bounded no-go | Physics-supported lanes | impossible | impossible | impossible | exact match | bounded divergence-only no-go witness |
| Finite-time exactness failure for smooth linear flow | Physics-supported lanes | asymptotic-only | asymptotic-only | asymptotic-only | exact match | continuous-generator no-go benchmark |

## 4. Independent cross-check findings

- Workbench answers were checked against separate Python-side or direct algebraic calculations wherever the lane supported that split.
- Brute-force collision-gap scans were added for tracked restricted-linear cases so the row-space theorem was not grading itself only through one nullspace implementation.
- Periodic threshold checks were tied to explicit active-mode support rather than only to the workbench’s family labels.
- Diagonal/control threshold checks were cross-checked through direct interpolation solves rather than only through the workbench threshold helper.
- Browser workflows validated exports, share-state, and reload behavior on the live UI rather than on analyzer return values alone.

## 5. User workflow results

- passing live workflows: **10/10**

- `Exact recovery success workflow`: pass — Exact Projection Lab preserved the orthogonal exact-recovery anchor and exported the same verdict.
- `Guided benchmark route and export`: pass — Guided entry opened the benchmark console with 12 module rows and working CSV/report export.
- `Failing setup → diagnosis → fix → verified success`: pass — Boundary architecture repair moved from impossible to exact, and share-link/reload preserved the repaired result.
- `Threshold failure → cutoff augmentation → verified exact recovery`: pass — Periodic stronger-target threshold failure was diagnosed and repaired in the live studio.
- `Stronger target fails / weaker target succeeds`: pass — The qubit workflow correctly weakened the Bloch-vector target to the z coordinate and preserved the exact verdict after the change.
- `Structured linear mixer failure → repair → JSON export`: pass — Typed linear mixer case repaired cleanly and exported the repaired exact state.
- `Unsupported custom input → honest rejection`: pass — Custom nonlinear protected variable is rejected explicitly and no fake repair is offered.
- `Impossible setup → no-go explanation → no fake fix suggested`: pass — No-Go Explorer preserved the proved no-go without inventing a redesign path.
- `Physics example workflow`: pass — CFD Projection Lab preserved the periodic exact branch and the bounded-domain limitation in both UI and exported report.
- `Exact impossible / asymptotic possible workflow`: pass — Continuous generator lab preserved the finite-time exactness no-go and asymptotic-only interpretation.

## 6. Adversarial / red-team cases

- adversarial cases caught correctly: **7/7**

| Case | Intended failure mode | Outcome | Notes |
| --- | --- | --- | --- |
| Brute-force collision gap versus theorem formula | same logic grading itself on κ(0) gap | caught | Small-grid brute force agrees closely with the analytic nullspace-based gap on the tracked 3-state family. |
| Same support-size heuristic failure | support size mistaken for threshold invariant | caught | Two support-size-2 functionals require different cutoffs because the maximal active mode differs. |
| Naive active-sensor-count heuristic failure | active sensor count mistaken for exact history threshold | caught | The exact threshold is controlled by interpolation structure, not raw active-sensor count. |
| Unsupported nonlinear custom expression | unsupported symbolic term silently accepted | caught | Unsupported nonlinear syntax is rejected explicitly instead of being coerced into a false linear interpretation. |
| Out-of-basis variable rejection | undeclared variable accepted into the typed family | caught | Variables outside the declared basis size are rejected with an explicit unsupported verdict. |
| Asymptotic versus impossible split | finite-history impossibility misclassified as asymptotic or vice versa | caught | The workbench keeps observer-style asymptotics separate from finite-history impossibility. |
| Share-state roundtrip drift | state encoding or export changes the verdict after reload | caught | Encoded benchmark state round-trips back to the same sanitized configuration. |

## 7. Dependency and consistency audit

- `README links professional validation report`: pass
- `README links tool qualification report`: pass
- `FINAL_REPORT includes current tool qualification counts`: pass
- `SYSTEM_REPORT includes current tool qualification counts`: pass
- `Tool qualification report includes current module count`: pass

## 8. New results found after stronger qualification

### Periodic threshold follows highest active mode, not support count
- classification: `useful negative result`
- summary: Randomized and hand-built periodic functionals continue to falsify raw support-count heuristics; the tracked threshold is controlled by the highest active retained mode on the four-mode basis.
- support: family-specific support-threshold stress check

### Random restricted-linear search remains useful for repairable supported-family discovery
- classification: `survives and worth keeping`
- summary: 15 seeded random linear cases produced impossible-before/exact-after repairs inside the supported typed family.
- support: seeded typed discovery search only, not a new theorem claim

## 9. Failures found

- Several generated-artifact consistency tests remain partial/circular: they are good stale-output alarms, not independent truth validators.
- Narrow anchor labs are still qualified-narrow rather than universal; the workbench should not oversell them as open-ended analyzers.

## 10. Fixes applied

- Added professional known-answer and adversarial outputs with independent cross-check logic.
- Added a generated validation snapshot so the benchmark console exposes current trust counts and limitations.
- Extended the browser qualification into a stronger workflow-based acceptance surface.
- Added report-consistency checks so top-level repo claims stay tied to current validation counts.

## 11. Final readiness assessment

- safe for known-case validation: **yes**
- safe for guided discovery inside supported families: **yes**
- safe for unsupported free exploration: **no**

## 12. Remaining limits

- Unsupported free-form symbolic systems are still outside the validated scope and must be rejected rather than approximated.
- Some artifact-consistency checks remain intentionally marked as partial because they recompute outputs from the same implementation family.
- Family-specific thresholds remain family-specific; this pass does not convert them into universal theorems.
