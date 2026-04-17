# Theorem Falsification Report

Date: 2026-04-17
Pass type: Full falsification / disproof / repair

## Scope and method

This report records theorem-level and branch-level attacks across branches A-K using:
- exact linear algebra checks,
- brute-force witness regeneration,
- randomized/adversarial finite searches already encoded in tests,
- workbench consistency tests,
- claim/status consistency audits.

Wolfram tooling was checked and unavailable locally (`wolframscript: command not found`), so symbolic verification remained Python/SymPy/NumPy based.

## Branch A — Exact finite-dimensional projector

Claims attacked: `OCP-001`, `OCP-002`, `OCP-003`, `OCP-016`.

Checks:
- `tests/math/test_core_projectors.py`
- `tests/math/test_capacity.py`

Result:
- all attacked claims survived within declared assumptions.
- no new counterexample found inside stated linear-algebra assumptions.

Status changes:
- none.

## Branch B — Sector / QEC

Claims attacked: `OCP-005`, `OCP-017`, `OCP-019`, `OCP-021`.

Checks:
- `tests/math/test_qec_knill_laflamme.py`
- `tests/math/test_sector_recovery.py`

Result:
- exact sector recovery survives on declared orthogonal/compatibility hypotheses.
- overlap no-go survives.
- QEC bridge remains conditional by design; no unjustified promotion.

Status changes:
- none.

## Branch C — Periodic Helmholtz / Leray

Claims attacked: `OCP-006`, `OCP-027`.

Checks:
- `tests/math/test_mhd_projection.py`
- `tests/math/test_cfd_projection.py`

Result:
- periodic exact projector anchor survives.
- narrow CFD periodic fit survives but is family-scoped.

Status changes:
- `OCP-027` demoted from `PROVED` to `PROVED ON SUPPORTED FAMILY`.

## Branch D — Bounded-domain / Hodge / CFD

Claims attacked: `OCP-023`, `OCP-028`, `OCP-029`, `OCP-044`.

Checks:
- `tests/examples/test_bounded_domain_projection_limit.py`
- `tests/math/test_cfd_projection.py`
- generated witness recomputation through compare scripts

Result:
- bounded-domain transplant failure (`OCP-023`) re-confirmed.
- divergence-only no-go (`OCP-028`) survives.
- finite-mode Hodge exactness survives only on explicit supported family.

Status changes:
- `OCP-044` demoted from `PROVED` to `PROVED ON SUPPORTED FAMILY`.

## Branch E — Asymptotic generator

Claims attacked: `OCP-004`, `OCP-013`, `OCP-014`, `OCP-015`, `OCP-020`.

Checks:
- `tests/math/test_continuous_generators.py`

Result:
- invariant-split generator theorem, PSD corollary, mixing no-go, and finite-time exact-recovery no-go all survive in stated linear setting.

Status changes:
- none.

## Branch F — Constrained-observation / PVRT

Claims attacked: `OCP-030..043`.

Checks:
- `tests/math/test_recoverability.py`
- `scripts/compare/run_recoverability_examples.py`
- regenerated recoverability artifacts and threshold figures.

Result:
- core fiber/factorization criterion and threshold package survive on declared classes.
- no universal extension promoted beyond supported classes.

Status changes:
- none.

## Branch G — Restricted-linear anti-classifier / augmentation

Claims attacked: `OCP-045`, `OCP-046`, `OCP-047`.

Checks:
- `tests/math/test_design.py`
- `tests/math/test_recoverability.py`
- `scripts/compare/run_design_examples.py`

Result:
- minimal augmentation theorem survives.
- same-rank insufficiency survives.
- exact-regime envelope survives under explicit exactness assumptions.

Status changes:
- none.

## Branch H — Fiber-based recoverability / impossibility

Claims attacked: `OCP-048..053`.

Checks:
- `tests/math/test_unified_limits.py`
- `scripts/compare/run_fiber_recoverability_examples.py`
- counterexample extraction in `data/generated/falsification/counterexample_catalog.csv`

Result:
- no rank-only and no fixed-budget-only classifier failures survive.
- family-enlargement false-positive and model-mismatch instability witnesses survive.
- universal framing remained branch-limited.

Status changes:
- none.

## Branch I — Workbench / Structural Discovery / Discovery Mixer

Claims attacked: `WB-001` and module-label/status consistency claims.

Checks:
- `node --test tests/consistency/*.mjs`
- `tests/examples/test_validation_consistency.py`
- `scripts/compare/run_professional_validation_audit.py`

Failures found and repaired:
1. Benchmark console missing required `Recoverability / Observation Studio` module row.
2. Benchmark console label mismatch for `Structural Discovery Studio`.
3. README missing required professional validation link used by consistency checks.

Repair actions:
- updated `docs/workbench/lib/engine/benchmarkConsole.js`
- updated `README.md`

Post-repair result:
- JS consistency tests pass.
- validation-consistency examples pass.

## Branch J — Physics extension / bridges

Claims attacked: `OCP-022`, `OCP-024`, `OCP-025`, `OCP-026`, plus alignment of bridge wording.

Checks:
- theorem-vs-bridge scope audit against claim registry and proof-status map.

Result:
- conditional bridges remain conditional.
- generic constrained Hamiltonian remains analogy-only.
- gauge projection fit survives but is explicitly domain-support scoped.

Status changes:
- `OCP-022` demoted from `PROVED` to `PROVED ON SUPPORTED FAMILY`.

## Branch K — Meta-theory / descriptor-fiber extraction

Claims attacked: `META-001` and meta-layer promotion language.

Checks:
- `scripts/report/compute_meta_theory_invariants.py`
- regenerated `data/generated/meta-theory/meta_classifier_invariants.{csv,json}`
- overlap audit and quantitative extraction docs.

Result:
- broad meta-language is interpretive.
- quantitative descriptor-fiber layer survives as finite-class branch-limited math.

Status changes:
- no additional demotion beyond explicit branch-limited labeling already applied.

## Summary of theorem-grade outcomes

- Survived unchanged: majority of theorem backbone.
- Survived but narrowed: `OCP-022`, `OCP-027`, `OCP-044`.
- Disproved remains disproved: `OCP-023`.
- Tool-layer defects: 3 found and repaired.
