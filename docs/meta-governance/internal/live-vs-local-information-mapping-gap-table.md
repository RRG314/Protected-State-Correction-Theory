# Live vs Local Information-Mapping Gap Table

Decision classes:
- `include-now`
- `include-after-rewrite`
- `internal-only`
- `defer`
- `reject`

| Item | Local Source | Live Gap | Decision | Why |
|---|---|---|---|---|
| Primitive-object restricted closure (`OCP-054`) | `src/ocp/structural_information.py`, theorem/docs maps | not fully reflected on live theorem-facing package | include-now | Core to static arena completion and tied to executable tests. |
| Dynamic monotonicity + no-go package (`OCP-055`,`OCP-056`) | dynamic layer + theorem/no-go spines | partial on live | include-now | Defines dynamic survive/fail boundary with explicit assumptions. |
| Finite multivalued dynamic extension (`OCP-057`) | harness + dynamic docs | missing on live | include-now | Extends binary-only dynamic statements with bounded scope. |
| BSC semigroup envelope (`OCP-058`) | dynamic docs + code/tests | missing on live | include-now | Supplies explicit compositional law for declared class. |
| Primitive invariance (`OCP-059`) | code/tests + theorem maps | not explicit on live | include-now | Static arena strengthening with clear assumption boundary. |
| Perturbation threshold (`OCP-060`) | code/tests + theorem maps | weaker live presentation | include-now | Provides robustness threshold above exactness core. |
| Nonlinear post-composition boundary (`OCP-061`) | code/tests + no-go maps | partial on live | include-now | Nonlinear survive/fail boundary is central to regime map. |
| Finite amount-code boundary (`OCP-062`) | code/tests + theorem/no-go maps | missing on live | include-now | Tightens static scalar-no-go into exact finite criterion. |
| BSC horizon threshold law (`OCP-063`) | code/tests + dynamic docs + artifacts | missing on live | include-now | Completes dynamic horizon classification on declared semigroup class. |
| Four-arena regime-map docs | `docs/restricted-results/regime-maps/*` | absent on live | include-now | Needed for explicit arena-level mapping objective. |
| Canonical final map document | `docs/meta-governance/final-information-regime-map.md` | absent on live | include-now | Gives one reviewer-facing synthesis of works/fails/open. |
| Canonical physics translation boundary | `docs/physics-translation/canonical-physics-translation-boundary.md` | weaker/older on live | include-now | Separates theorem-grade mapping from conditional/analogy claims. |
| Scope-gate automation + tests | `scripts/validate/check_claim_scope.py`, `tests/examples/test_claim_scope_gate.py`, policy doc | less strict on live | include-now | Prevents scope inflation and SDS/theory drift regression. |
| Validation interpreter hardening | `scripts/validate/run_all.sh`, `scripts/compare/run_professional_validation_audit.py` | live can fail under non-venv interpreter split | include-now | Improves reproducibility and branch validation reliability. |
| Structural harness expansion | `scripts/research/run_structural_information_harness.py` | live harness narrower | include-now | Required to reproduce expanded regime-map evidence. |
| External datasets: wine/magic/ionosphere/spambase/sonar/wdbc | `data/imported/external/*` + provenance | several missing on live | include-now | Supports external validity and anti-overfitting pressure. |
| Structural generated artifacts (canonical) | `data/generated/structural-information-theory/*` | live missing newest regime artifacts | include-now | Required evidence layer for included claims. |
| Practical baseline + failure catalog artifacts | `decision_practical_comparison.csv`, `diagnostic_failure_catalog.csv` | missing on live | include-now | Explicitly records failures where scalar can outperform, improving credibility. |
| Decision baseline method note | `docs/methods-diagnostics/decision-baseline-pressure.md` | outdated live version | include-after-rewrite | Valuable, but should stay concise and research-grade; include cleaned local version only. |
| Deep pass work queues and attack plans | `docs/meta-governance/*deep-pass*`, `*work-queue*`, `*attack-plan*` | local only | internal-only | Process artifacts, not public theorem surface. |
| Theory completion change report | `docs/meta-governance/theory-completion-change-report.md` | local only | internal-only | Useful audit log, not needed in live-facing branch. |
| Massive namespace/archive visibility cleanup (`ccb8d29`) | archive and docs namespace move set | not on live | defer | Valuable but too broad for focused information-mapping update branch. |
| Internal governance migration logs | `archive/internal-governance/**` and process-heavy docs | many local changes | reject | High clutter risk; low public explanatory value. |
