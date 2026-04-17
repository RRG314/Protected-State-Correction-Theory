# Lens Integration Validation Plan (2026-04-16)

## Purpose

Validate lens-derived promotions with claim-type-matched tests.

No promoted result is accepted from numerical fit alone if the claim is exact.

## Validation Grid By Claim Type

| Claim type | Promoted claim family | Required validation type | Why this test is appropriate | What falsifies |
| --- | --- | --- | --- | --- |
| Exact theorem claims | row-space/kernel exactness (`OCP-031`), same-rank insufficiency (`OCP-047`), anti-classifier theorems (`OCP-049`, `OCP-050`), family-enlargement false-positive (`OCP-052`), model-mismatch instability (`OCP-053`) | symbolic/linear-algebra derivation + exhaustive finite witness search + exact residual checks | these are finite-dimensional exact statements; exact algebra and explicit witnesses are decisive | one admissible exact counterexample violating theorem conditions/conclusions |
| Asymptotic/rate claims | invariant-split generator and spectral-rate interpretations (`OCP-013`, `OCP-014`, `OCP-015`, `OCP-020`) | spectral computation + semigroup/decay checks + perturbation stress in supported classes | claims are rate/convergence statements, so spectral/semigroup tests match statement type | observed violation of predicted decay/no-go under stated assumptions |
| Bounded-domain/PDE/topology claims | periodic-transplant failure (`OCP-023`), divergence-only bounded no-go (`OCP-028`), bounded finite-mode Hodge exactness (`OCP-044`), conditional bounded classification (`OCP-029`) | explicit bounded-family constructions + boundary-normal/tangential checks + Hodge-compatible decomposition checks | these claims depend on boundary/domain structure; domain-aware examples are required | bounded witness that preserves hypotheses but flips exact/no-go verdict |
| Recoverability/constrained-observation claims | collision-gap thresholds (`OCP-043`), exact-regime upper envelope (`OCP-046`), weaker-vs-stronger hierarchy (`OCP-041`, `OCP-051`) | brute-force finite-family scans + nullspace/row-space checks + ambiguity witness generation + noise stress | claims depend on constrained records and admissible families; witness scans and nullspace tests are direct falsifiers | same-family opposite behavior not predicted by theorem |
| Engineering/workbench claims | theorem-to-tool consistency and evidence labels | reproducible scenario replay + export/recompute consistency + static/browser checks | tool claims are operational and must be reproducible end-to-end | mismatch between UI claim and independent recomputation or test failure |

## Lens-Specific Validation Targets

### Operator-theory promotions
- validate alignment/kernel language against same-rank/same-budget witness suites.
- validate spectral-rate phrasing only on split-preserving generator classes already supported.

### Functional-analysis promotions
- validate bounded-domain obstruction statements only on explicit bounded families with boundary checks.
- avoid promoting topological obstruction as universal until broader domain families are proven.

### Geometry support promotions
- validate principal-angle/alignment diagnostics against operator-theory decisions.
- reject any geometry phrase not tied to a computable invariant used by a theorem/no-go.

## Command Plan

Primary full run:
- `bash scripts/validate/run_all.sh`

Focused branch-matched checks:
- `PYTHONPATH=src uv run --with pytest python -m pytest -q tests/math/test_recoverability.py tests/math/test_unified_limits.py tests/math/test_cfd_projection.py tests/math/test_continuous_generators.py`
- `node --test tests/consistency/workbench_static.test.mjs`

## Promotion Gate

A lens-derived result is promoted only if all are true:
- matched test type executed,
- no contradiction found under stated assumptions,
- branch scope documented,
- literature-status label assigned,
- workbench/doc wording does not overclaim.
