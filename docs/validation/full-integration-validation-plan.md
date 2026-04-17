# Full Integration Validation Plan (2026-04-16)

## Purpose

Validate the post-lens integrated repository state with claim-type-matched methods.

Acceptance rule:
- exact claims require exact algebraic or symbolic checks,
- asymptotic/rate claims require spectral or semigroup checks,
- bounded-domain claims require boundary/topology-aware witnesses,
- constrained-observation claims require fiber/row-space/collision witness checks,
- workbench claims require reproducible UI/export consistency checks.

## Validation Matrix

| Claim lane | Promoted claim families | Required test type | Why this is the right test | Falsifier |
| --- | --- | --- | --- | --- |
| Exact finite-dimensional | `OCP-002`, `OCP-003`, `OCP-016`, `OCP-019`, `OCP-021`, `OCP-031`, `OCP-045`, `OCP-047`, `OCP-049`, `OCP-050`, `OCP-052`, `OCP-053` | exact linear algebra, symbolic derivation, brute-force witness enumeration | theorem statements are finite-dimensional exact laws | one admissible counterexample with violated conclusion |
| Quantitative/stability/dynamic next-phase layer | `QR-*`, `STAB-*`, `DYN-*`, `MSC-*` branch-scoped package | deterministic artifact regeneration + recomputation consistency tests + perturbation/rate witness sweeps | promoted results are operationalized as computable invariants, envelopes, and rates | regenerated summary/artifacts mismatch independent recomputation |
| Bounded-domain / Hodge / topology | `OCP-023`, `OCP-028`, `OCP-029`, `OCP-044` | explicit bounded-family constructions, boundary-trace checks, Hodge-compatible decomposition checks | branch conclusions depend on boundary geometry and family restrictions | one bounded family with preserved assumptions and opposite verdict |
| Asymptotic generator / rate | `OCP-013`, `OCP-014`, `OCP-015`, `OCP-020` | spectral-gap and eigenvalue checks, semigroup/flow convergence checks | these claims are rate and finite-time impossibility statements | observed finite-time exactness or rate violation under stated assumptions |
| Constrained observation / recoverability | `OCP-030`–`OCP-047` plus fiber hierarchy `OCP-048`–`OCP-053` | fiber constancy checks, row-space/kernel inclusion checks, same-rank/same-budget anti-classifier scans, noise-separation checks | this branch is fundamentally factorization/fiber/alignment based | same family with contradiction to claimed regime boundary |
| Workbench / engineering | theorem-to-UI evidence labels, export/reload consistency, benchmark console integrity | static consistency tests, browser workflow replay, generated-artifact parity checks | product claims are operational and must be reproducible | mismatch between UI/report label and independent recomputation |

## Planned Execution

Primary gate:
- `bash scripts/validate/run_all.sh`

Focused rechecks:
- `PYTHONPATH=src uv run --with pytest python -m pytest -q tests/math/test_recoverability.py tests/math/test_unified_limits.py tests/math/test_cfd_projection.py tests/math/test_continuous_generators.py`
- `PYTHONPATH=src uv run --with pytest python -m pytest -q tests/math/test_next_phase.py tests/examples/test_next_phase_examples_consistency.py`
- `node --test tests/consistency/workbench_static.test.mjs`

## Promotion Guard

A promoted result remains promoted only if all are true:
1. matched validation type executed,
2. no contradiction found on stated families,
3. family restrictions are explicit,
4. evidence-level label is canonical (`theorem-backed`, `restricted theorem-backed`, `validated family-specific`, `benchmark empirical`, etc.),
5. no decorative or unsupported language is promoted in workbench exports.
