# Lens Integration Validation Results (2026-04-16)

## Execution Summary

Primary full validation run:
- command: `bash scripts/validate/run_all.sh`
- status: passed
- key outcomes:
  - Node consistency suite: `29 passed`
  - Python theorem/operator/example suite: `148 passed`
  - generated inventories, claim registry, proof map, recoverability/unified/decision/design/discovery artifacts regenerated successfully

Focused branch-matched rechecks:
- command: `PYTHONPATH=src uv run --with pytest python -m pytest -q tests/math/test_recoverability.py tests/math/test_unified_limits.py tests/math/test_cfd_projection.py tests/math/test_continuous_generators.py`
- status: passed
- outcome: `66 passed in 9.54s`

- command: `node --test tests/consistency/workbench_static.test.mjs`
- status: passed
- outcome: `21 passed`

## Result Matrix by Claim Family

| Claim family | Validation mode used | Result | Survived scope |
| --- | --- | --- | --- |
| Exact recoverability and anti-classifier package (`OCP-031`, `OCP-047`, `OCP-049`, `OCP-050`, `OCP-052`, `OCP-053`) | exact algebra + finite witness suites + generated artifacts via `test_recoverability.py` and `test_unified_limits.py` | pass | restricted finite-dimensional linear classes (explicitly scoped) |
| Asymptotic generator and no-go boundaries (`OCP-013`, `OCP-014`, `OCP-015`, `OCP-020`) | spectral/flow checks via `test_continuous_generators.py` | pass | split-preserving linear generator classes in repo |
| Bounded-domain/Hodge/CFD branch (`OCP-023`, `OCP-028`, `OCP-029`, `OCP-044`) | bounded-domain explicit-family checks via `test_cfd_projection.py` and generated examples | pass | explicit bounded families and tested boundary-compatible constructions |
| Tool/workbench evidence consistency | static + scenario replay + export checks via Node consistency suites | pass | supported modules and typed families only |

## What Would Have Falsified Promotions

- a same-rank or same-budget witness with opposite verdict from the promoted alignment/kernel invariant explanation,
- a bounded-domain family violating the current boundary/topology obstruction framing,
- an asymptotic-rate claim failure on a class where assumptions are explicitly satisfied,
- a workbench claim not reproducible by independent scripted recomputation.

None of the above occurred in this pass.

## Surviving Promotions After Validation

- operator-theory alignment/kernel invariant as stronger-than-rank explanatory spine in constrained/fiber branches,
- spectral-rate sharpening in asymptotic branches under current assumptions,
- bounded-domain boundary/topology obstruction framing as primary no-go/exactness gate,
- geometry retained as supporting computable diagnostics (principal-angle/alignment), not as foundation.

## Failures and Demotions Confirmed

- entropy-language inflation for exact branches remains demoted,
- inverse-problem framing on exact projector/QEC/Helmholtz remains demoted,
- universal one-lens or one-language unification remains falsified.

## Artifacts Used

- `data/generated/validations/claim_registry.csv`
- `data/generated/validations/system_summary.json`
- `data/generated/validations/workbench_examples.json`
- `data/generated/recoverability/recoverability_summary.json`
- `data/generated/unified-recoverability/unified_recoverability_summary.json`
- `data/generated/unified-recoverability/decision_layer_summary.json`

## Validation Verdict

Lens integration survived as a **selective promotion**:
- strong in operator + functional-analysis lanes,
- supporting in geometry lane,
- secondary/archived in inverse-problem, information, and dynamical lanes outside their narrow valid scopes.
