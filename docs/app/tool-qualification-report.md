# Tool Qualification And Known-Results Verification Report

This report is intentionally split into three stages:
- Stage 1: tool qualification
- Stage 2: known-results verification
- Stage 3: post-qualification discovery use

## 1. What the tool is currently capable of validating

- exact known-case replay on the exact, QEC, MHD, CFD, gauge, continuous, and no-go anchor modules
- theorem-backed and family-backed recoverability diagnosis in the recoverability studio
- end-to-end diagnosis, repair suggestion, and before/after validation in the Structural Discovery Studio
- typed composition, controlled custom input, and supported repair search in the Discovery Mixer
- benchmark replay, module-health checks, and export validation in the Benchmark / Validation Console

## 2. What the tool cannot yet validate reliably

- arbitrary unsupported symbolic systems outside the typed family classes
- broad nonlinear architecture design outside the current theorem-backed or family-backed lanes
- universal threshold laws inferred from one module family and projected onto another
- unsupported free exploration without a supported family reduction

## 3. Tool qualification results

A live browser qualification pass was executed on the high-risk workbench surfaces. It covered 10 real workflows with 0 console errors and 0 warnings.

- qualified modules/workflows: **11**
- partial modules/workflows: **0**

| Module | Scenario | Verdict | Real calculations | Report export | CSV export | Share/reload | Before/after | Unsupported honesty | Qualification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Exact Projection Lab | orthogonal exact recovery | exact | yes | yes | yes | yes | n/a | n/a | qualified-narrow | Exact theorem anchor is working and export/report state is coherent, but this lab is intentionally narrow and does not expose unsupported free-form input. |
| QEC Sector Lab | three-qubit bit-flip exact sector recovery | exact | yes | yes | yes | yes | n/a | n/a | qualified-narrow | Known exact anchor reproduces correctly; this lab is trustworthy for the tracked sector example but not yet a broad QEC explorer. |
| MHD Projection Lab | periodic projection versus short GLM run | exact-vs-asymptotic split | yes | yes | yes | yes | n/a | n/a | qualified | Real numerical comparison is present and the exact-versus-GLM gap is preserved. |
| CFD Projection Lab | periodic exact branch plus bounded transplant failure | mixed exact and no-go | yes | yes | yes | yes | n/a | n/a | qualified | This lab is trustworthy for both the periodic exact anchor and the bounded-domain negative benchmark. |
| Gauge / Maxwell Lab | transverse projection fit | exact fit on compatible domain | yes | yes | yes | yes | n/a | n/a | qualified-narrow | The lab behaves correctly on the kept projection-compatible example, but it remains an anchor surface rather than a broad discovery tool. |
| Continuous Generator Lab | invariant-split asymptotic correction with finite-time no-go | asymptotic only | yes | yes | yes | yes | n/a | n/a | qualified | The lab correctly distinguishes asymptotic suppression from impossible finite-time exact recovery. |
| No-Go Explorer | bounded-domain transplant failure witness | COUNTEREXAMPLE / REJECTED BRIDGE | yes | yes | yes | yes | n/a | yes | qualified | No-Go Explorer is trustworthy for explicit counterexamples and does not invent fixes for structurally rejected setups. |
| Recoverability / Observation Studio | periodic stronger-target threshold failure | Impossible | yes | yes | yes | yes | yes | yes | qualified | The recoverability studio is trustworthy for theorem-backed and family-backed threshold cases and keeps fix cards tied to real comparisons. |
| Structural Discovery Studio | wrong architecture on bounded-domain protected class | Impossible | yes | yes | yes | yes | yes | yes | qualified | This is currently the strongest end-to-end diagnosis-to-repair workflow in the workbench. |
| Discovery Mixer / Structural Composition Lab | typed restricted-linear failure, repair, and unsupported nonlinear rejection | Impossible | yes | yes | yes | yes | yes | yes | qualified | The mixer is strong enough for supported typed composition and explicit unsupported handling; it is not a free symbolic sandbox. |
| Benchmark / Validation Console | validated demo replay and module-health export | Validated benchmark surface | yes | yes | yes | yes | yes | n/a | qualified | Benchmark console exports real demo rows and module-health summaries. |

## 4. Known-results verification matrix

- passing known-result checks: **21/21**

| Case | Category | Expected | Tool | Independent check | Result | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Orthogonal exact recovery | Exact / OCP | exact | exact | exact | exact match | theorem-backed or theorem-linked branch example | Exact projector anchor. |
| Overlap / indistinguishability no-go | Exact / OCP | impossible | impossible | impossible | exact match | theorem-backed or theorem-linked branch example | Non-orthogonal disturbance contaminates the protected projection. |
| Exact sector recovery | Exact / OCP | exact | exact | exact | exact match | theorem-backed or theorem-linked branch example | Bit-flip sector anchor. |
| Fiber-collision no-go at analytic ε=0 | Constrained observation | impossible | impossible | impossible | exact match | explicit analytic benchmark | Zero degeneracy closes the record on the protected scalar. |
| Restricted-linear exact no-go before augmentation | Constrained observation | impossible | impossible | impossible | exact match | theorem-backed restricted-linear result | The protected row is outside the active observation row space. |
| Minimal augmentation theorem case | Constrained observation | exact-min-1 | exact-min-1 | exact-min-1 | exact match | theorem-backed restricted-linear result | One added row is enough, and the tool surfaces candidate one-row repairs. |
| Same-rank exact case | Constrained observation | exact | exact | exact | exact match | theorem-backed restricted-linear result | Rank two record that already contains the protected row. |
| Same-rank insufficiency case | Constrained observation | impossible | impossible | impossible | exact match | theorem-backed restricted-linear result | Same row rank, opposite recoverability verdict. |
| Qubit phase-loss no-go | Constrained observation | impossible | impossible | impossible | exact match | family-specific result with standard external guidance | Full Bloch-vector target fails once phase freedom opens. |
| Qubit weaker target exactness | Constrained observation | exact | exact | exact | exact match | family-specific result with standard external guidance | z-only target survives under the same fixed-basis record. |
| Periodic cutoff threshold failure | Constrained observation | impossible | impossible | impossible | exact match | family-specific threshold result | Cutoff 3 hides mode 4 support of the weighted functional. |
| Periodic cutoff threshold repair | Constrained observation | exact | exact | exact | exact match | family-specific threshold result | Cutoff 4 recovers the full functional support on the tracked basis. |
| Diagonal history threshold failure | Constrained observation | impossible | impossible | impossible | exact match | family-specific threshold and asymptotic benchmark | History horizon 2 is below the proven threshold for the second moment. |
| Diagonal history threshold repair | Constrained observation | exact | exact | exact | exact match | family-specific threshold and asymptotic benchmark | Horizon 3 reaches the tracked exact threshold. |
| Periodic Helmholtz / GLM split | Physics-supported lanes | exact-better-than-glm | exact-better-than-glm | exact-better-than-glm | exact match | theorem-backed or theorem-linked branch example | Projection should beat short GLM cleaning on the tracked periodic case. |
| Periodic incompressible velocity projection | Physics-supported lanes | exact | exact | exact | exact match | validated theorem / no-go / empirical branch example | Periodic CFD branch should remain exact. |
| Gauge / Maxwell transverse projection | Physics-supported lanes | exact-improves-transverse | exact-improves-transverse | exact-improves-transverse | exact match | theorem-backed or theorem-linked branch example | Gauge lab stays aligned with the exact projection anchor. |
| Naive bounded-domain transplant failure | Physics-supported lanes | impossible | impossible | impossible | exact match | theorem-linked counterexample and family-specific redesign guidance | Transplanted periodic projector fails the bounded protected class. |
| Restricted bounded-domain exact family | Physics-supported lanes | exact | exact | exact | exact match | restricted exact bounded-domain result | Boundary-compatible Hodge family should remain exact on the tracked benchmark. |
| Divergence-only bounded no-go | Physics-supported lanes | impossible | impossible | impossible | exact match | validated theorem / no-go / empirical branch example | Distinct bounded incompressible states share the same divergence record. |
| Finite-time exactness failure for smooth linear flow | Physics-supported lanes | asymptotic-only | asymptotic-only | asymptotic-only | exact match | validated theorem / no-go / empirical branch example | Continuous generator lab should keep exact and asymptotic separate. |

## 5. Independent cross-check findings

- The exact/QEC/CFD/continuous anchors agreed with independent Python-side recomputation on the tracked known cases.
- The restricted-linear and periodic threshold stories matched independent row-space and support-based calculations.
- The tool did not get to grade itself on the main results: workbench answers were checked against separate Python/source-side computations or direct formulas.
- One repo-integrity issue was caught and fixed during this pass: the generated repo inventory was previously counting `.playwright-cli` smoke artifacts as product files.
- The browser qualification script exercised export, share-link, reload, fix-application, unsupported rejection, and guided routing on the live UI rather than only on the source-side analyzers.

## 6. User workflow results

| Workflow | Status | Notes |
| --- | --- | --- |
| Failing setup → diagnosis → fix → verified success | pass | Boundary architecture workflow moves from impossible to exact with the promoted Hodge replacement. |
| Impossible setup → no-go explanation → no fake fix suggested | pass | No-Go Explorer reports the obstruction without inventing a repair path. |
| Stronger target fails / weaker target succeeds | pass | The same fixed-basis record kills the full Bloch target but preserves the z-only target. |
| Exact impossible / asymptotic possible workflow | pass | Continuous generator lab correctly routes the example to asymptotic-only behavior rather than exact finite-time recovery. |
| Wrong architecture chosen → system recommends a better one | pass | The bounded-domain failure points to the boundary-compatible replacement instead of a cosmetic tweak. |
| Export and reload preserve the same conclusion | pass | Share-state roundtrip and report export stay aligned on the structured linear mixer case. |

## 7. New results found after qualification, if any

### Random periodic modal search supports the support-threshold rule
- Classification: `survives and worth keeping`
- Summary: Across 40 seeded random periodic mixer cases, the tool's predicted minimum cutoff matched the highest active modal support index every time on the tracked four-mode basis.
- Support: family-specific empirical extension of the periodic support-threshold story; independently checked by parsing the generated modal functional support.

### Naive active-sensor-count heuristic fails in the diagonal/history family
- Classification: `useful negative result`
- Summary: Seed 46 produced a control case where the naive active-sensor-count heuristic predicts horizon 4, but the tool and independent diagonal-family logic require horizon 1.
- Support: supports keeping the control threshold logic tied to interpolation structure rather than raw sensor-count language.

### Random linear mixer is usable for repairable counterexample discovery
- Classification: `survives and worth keeping`
- Summary: Seeded restricted-linear search continues to produce real repairable failures with exact after-fixes, making it suitable for guided discovery inside the supported family.
- Support: tool finding only; this is a validation of discovery usefulness, not a new theorem claim.

## 8. Failures found

- Several narrow anchor labs are reliable for their tracked examples but are not yet honest open-ended validators. They should be treated as qualified-narrow rather than universal tools.

## 9. Fixes applied

- Added a dedicated workbench query layer for repeatable tool-vs-source comparisons.
- Added a known-results verification program with independent Python-side recomputation.
- Added a reproducible browser qualification script for the high-risk workbench workflows.
- Added a tool-qualification and discovery-use report plus generated artifacts.
- Corrected repo inventory generation so Playwright smoke artifacts no longer pollute repo file counts.

## 10. Final readiness assessment

- safe for known-case validation: **yes**
- safe for guided discovery inside supported families: **yes, with scope discipline**
- safe for unsupported free exploration: **no**

The workbench is now strong enough to validate known cases and to support guided discovery inside the supported typed families. It is still not honest to treat it as a free symbolic exploration environment outside those lanes.
