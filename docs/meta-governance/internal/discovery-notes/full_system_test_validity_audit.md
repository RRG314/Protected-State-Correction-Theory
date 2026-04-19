# Full System Test Validity Audit

Status: conceptual audit of whether existing computational tests answer the mathematical claims they are used to support.

## Method

For each major lane, I checked:
1. Intended mathematical question.
2. Metric/test actually used.
3. Whether metric is sufficient for the claim.
4. Artifact/trivialization risks.
5. Whether claim wording should be narrowed.

## Audit Table

| Lane | Mathematical question | Current metric/test | Validity assessment | Main risk | Action |
|---|---|---|---|---|---|
| OCP anti-classifier | Can rank/budget classify exactness? | Exhaustive finite witness catalogs (`rank_only`, `budget_only`) | Strong for scoped finite class. | Scope over-extension beyond class. | Keep “PROVED ON SUPPORTED FAMILY” wording. |
| OCP family enlargement | Does exactness persist under family enlargement? | Explicit small->large witness tables | Strong for exhibited constructions. | Could be mistaken for prevalence law. | Keep existential/no-go wording only. |
| Context-sensitive split | Does local exactness imply shared exactness? | Generated context-family catalog + exactness checks | Strong for supported synthetic class. | Generator bias toward split forms. | Add non-synthetic benchmark families before promotion. |
| Shared augmentation threshold | Is positive shared augmentation required? | Catalog search over restricted augmentation library | Strong existence evidence; weak universality evidence. | Threshold depends on allowed augmentation class. | Always specify augmentation admissibility constraints. |
| Indistinguishability DLS | Does DLS add signal beyond rank? | DLS vs rank/kappa/gamma correlations + anomaly flags | Good diagnostic evidence, not theorem proof. | Correlation can be construction-driven. | Keep exploratory-only label; add adversarial random families. |
| TSIT design failure | Can D-optimal be target-blind? | Adversarial sensor-pool sweeps (high anomaly rates) | Strong empirical no-go package. | Structured pool bias inflates rates. | Report existential and benchmark rates; avoid prevalence claims. |
| TSIT alpha novelty | Is alpha fundamentally new in linear class? | Reduction tests against row-space criterion | Strong reduction evidence. | None; reduction is direct. | Keep as normalized interface metric only. |
| CFD sensor geometry | Does geometry matter beyond rank/count? | Paired same-count/same-rank explicit cases | Strong scoped theorem witness. | Low dimensionality (4-mode basis). | Extend to richer finite catalogs; keep current scope explicit. |
| CFD ROM failure | Is energy capture enough for branch-sensitive recovery? | Rank sweep with wake proxy metrics | Good validated counterexample. | Single benchmark family. | Keep validated status, not theorem status. |
| MHD variable-eta obstruction | Does nonconstant eta break smooth exactness? | Symbolic residual derivations + theorem tests | Strong theorem-grade within family assumptions. | Family ansatz boundary. | Continue explicit “supported families” boundary language. |
| MHD reconnection scaling | Does sheet thinning concentrate defect? | `delta` sweep and localization ratio | Good benchmark pattern. | Could be mistaken for universal reconnection theorem. | Keep “validated benchmark signal” wording. |
| Soliton same-count split | Can same observation dimension split identifiability? | Finite-state collision catalogs | Strong for supported families. | Continuous extension gap. | Keep conditional extension label. |
| Soliton CGL superiority | Is random self-organization superiority robust? | Deep artifact checks and repeatability | Test correctly falsifies overclaim. | Metric dependence if interpreted broadly. | Keep `ARTIFACT RISK`; no promotion. |
| RGE package tests | Are generators statistically sane in repo scope? | cycle + small-stat + package tests | Valid for package sanity, not proof of strong RNG theory. | Over-interpretation as cryptographic/statistical theorem. | Keep validation-only framing. |
| TorchRGE counter-mode | Is counter-mode path production-ready? | Validation note + maturity split docs | Adequate for branch-status decision. | Lack of comprehensive CI tests in this pass. | Add explicit tests or keep experimental label. |

## Cross-Corpus Validity Findings

1. **Strongest test correctness:** OCP finite witness counterexamples, CFD finite sensor-geometry witness, MHD symbolic derivations.
2. **Most scope-sensitive tests:** context-sensitive augmentation thresholds, TSIT adversarial design rates, reconnection scaling benchmarks.
3. **Most overclaim-prone zone:** exploratory extracted thermodynamic/holography text without canonical proof harness.

## Redesigns Required Before Promotion

1. Add non-synthetic benchmark families for context-sensitive theorem package.
2. Add perturbation robustness panels for TSIT design conflicts.
3. Add broader finite-catalog CFD sensor tests beyond 4-mode basis.
4. Add explicit cross-check tests for TorchRGE counter-mode branch if maturity claims are to change.
5. Keep exploratory black-hole/holography material outside promoted theorem map until formalized and tested.

## Validity Audit Verdict

Current test stack is mostly aligned with its scoped questions, but multiple high-value branches still rely on **supported-family** evidence rather than generalized theorem conditions. Promotion should follow scope-tightening, not narrative broadening.
