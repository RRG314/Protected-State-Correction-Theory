# Full Integration Validation Results (2026-04-16)

## Execution Summary

### Primary full gate

Command:
- `bash scripts/validate/run_all.sh`

Outcome:
- pass

Key completed stages:
- inventory + claim/proof map regeneration,
- operator/recoverability/fiber/decision/next-phase/design/discovery artifact regeneration,
- workbench example and validation summary regeneration,
- tool qualification + professional validation audit regeneration,
- Node consistency suite,
- markdown link check,
- naming consistency check,
- static workbench check,
- full Python test suite.

Observed pass counts from the full gate:
- Node consistency: `29 passed`
- Python suite: `158 passed in 50.42s`

### Focused rechecks

Command:
- `PYTHONPATH=src uv run --with pytest python -m pytest -q tests/math/test_recoverability.py tests/math/test_unified_limits.py tests/math/test_cfd_projection.py tests/math/test_continuous_generators.py`
- result: `66 passed in 19.51s`

Command:
- `PYTHONPATH=src uv run --with pytest python -m pytest -q tests/math/test_next_phase.py tests/examples/test_next_phase_examples_consistency.py`
- result: `10 passed in 2.13s`

Command:
- `node --test tests/consistency/workbench_static.test.mjs`
- result: `21 passed`

## Claim-Family Validation Matrix

| Claim family | Validation type used | Result | Scope that survived |
| --- | --- | --- | --- |
| Exact finite-dimensional and anti-classifier package (`OCP-031`, `OCP-045`, `OCP-047`, `OCP-049`, `OCP-050`, `OCP-052`, `OCP-053`) | exact row-space/kernel checks, witness enumeration, generated artifact checks | pass | restricted finite-dimensional linear classes |
| Next-phase quantitative/stability/dynamic package (`QR-*`, `STAB-*`, `DYN-*`, `MSC-*`) | deterministic artifact regeneration plus independent recomputation tests for profiles, perturbation sweeps, dynamics, and CFD deep dive | pass | explicit branch-supported finite/restricted-linear + bounded-domain witness families |
| Bounded-domain/Hodge lane (`OCP-023`, `OCP-028`, `OCP-029`, `OCP-044`) | bounded-family projector checks, boundary mismatch witnesses, finite-mode compatible exact checks | pass | explicit bounded tested families |
| Asymptotic generator lane (`OCP-013`, `OCP-014`, `OCP-015`, `OCP-020`) | generator/spectral checks and finite-time impossibility tests | pass | split-preserving linear-generator classes |
| Constrained observation/fiber hierarchy (`OCP-030`–`OCP-053`) | factorization/fiber checks, same-rank opposite-verdict scans, noise and mismatch witness checks | pass | branch-declared admissible families |
| Workbench consistency | static suite, qualification matrix, professional workflow replay | pass | supported labs/families and explicit unsupported boundaries |

## Evidence-Level Normalization Check

Post-regeneration outputs now use canonical evidence labels at source-generated artifacts (for example in `tool_known_results_matrix.csv` and `tool_qualification_summary.json`):
- `theorem-backed`
- `restricted theorem-backed (...)`
- `validated family-specific (...)`
- `benchmark empirical`

No stale old evidence strings remained in regenerated validation outputs.

## Falsifier Conditions and Outcome

Would have falsified promoted integration:
1. same-rank or same-budget examples contradicting anti-classifier claims,
2. bounded-domain example contradicting transplant no-go or finite-mode compatible exact result,
3. finite-time exact recovery appearing in the linear generator no-go class,
4. workbench reporting stronger evidence level than theorem/validation support,
5. regenerated claim/proof artifacts drifting from canonical theorem IDs.

Outcome:
- none occurred in this pass.

## Validation Verdict

Integration + cleanup + normalization pass is validated.

Surviving strength profile:
- strong: operator-theory + constrained/fiber anti-classifier package,
- strong: bounded-domain obstruction plus restricted exact bounded family,
- strong: asymptotic spectral/generator lane,
- explicit limit: no universal branch flattening; theory status remains branch-limited (`B`).
