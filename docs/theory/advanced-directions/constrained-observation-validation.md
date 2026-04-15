# Constrained-Observation Validation Summary

## Branch-Specific Code And Tests

Core implementation:

- [recoverability.py](../../../src/ocp/recoverability.py)
- [run_recoverability_examples.py](../../../scripts/compare/run_recoverability_examples.py)

Python tests:

- [test_recoverability.py](../../../tests/math/test_recoverability.py)
- [test_generated_artifact_consistency.py](../../../tests/examples/test_generated_artifact_consistency.py)

Workbench / Node coverage:

- [workbench_static.test.mjs](../../../tests/consistency/workbench_static.test.mjs)

## What Is Tested

Python-side:

1. fiber-collision exactness versus exact recovery
2. vectorized collapse-modulus values against a naive nested-loop reference implementation
3. restricted linear recovery criterion and restricted-rank lower bound
4. analytic collapse-modulus threshold behavior and adversarial lower bound
5. analytic lower-bound sweep against its closed-form formula
6. qubit meridian exactness, phase-loss no-go, and closed-form collision law
7. refined qubit phase-window sampling against the analytic formula
8. periodic full / truncated / divergence-only separation
9. periodic cutoff-threshold behavior on the two-mode family
10. periodic functional-support thresholds on the modal family
11. discretization stability of the periodic functional thresholds
12. one-step versus two-step versus observer-side control behavior
13. diagonal minimal-history threshold behavior on the three-state control family
14. interpolation-weight recovery against the independent pseudoinverse-based linear recovery operator
15. nested minimal-complexity criterion against direct row-space residual checks
16. periodic functional-support thresholds for non-coordinate protected variables
17. weaker-versus-stronger protected-variable splits under the same periodic coarse record
18. diagonal functional interpolation thresholds for sensor sums and moment-type functionals
19. diagonal functional weights against the independent row-space solver
20. nested restricted-linear collision-gap profiles against exact recovery, monotonicity, and row-space residual decay
21. restricted-linear collision gaps against independent brute-force nullspace scans on small cases
22. rank-lower-bound insufficiency counterexample for exact recovery
23. periodic threshold stress sweeps on repeated-cutoff modal families
24. diagonal polynomial threshold sweeps on larger active sensor spectra
25. generated recoverability summary rows against independent recomputation of the threshold sweeps
26. generated operator-example artifacts against direct CFD and continuous-flow recomputation

Workbench-side:

1. analytic exact-versus-impossible threshold behavior
2. qubit variable-sensitive recovery split
3. periodic exact / approximate / impossible split
4. periodic functional-support cutoff thresholds
5. control finite-history versus observer asymptotics
6. diagonal minimal-history threshold behavior in the three-state control lane
7. generalized periodic functional thresholds in the Structural Discovery Studio
8. generalized diagonal functional thresholds in the Structural Discovery Studio
9. the studio still distinguishes weaker recoverable variables from stronger impossible ones after the tightened theorem pass
10. existing exact / QEC / MHD / CFD / gauge / generator / no-go modules still pass
11. share-state encoding and decoding still round-trip correctly

Browser smoke checks:

1. periodic `band-limited contrast functional` is impossible at cutoff `2` and exact at cutoff `3`
2. diagonal `second sensor moment` is impossible at horizon `2` and exact at horizon `3`
3. verdict text, predicted thresholds, and exact/no-go badges match the offline branch outputs

## Current Validation Snapshot

Most recent targeted branch checks completed during this pass:

- `tests/math/test_recoverability.py`: `33 passed`
- `tests/examples/test_generated_artifact_consistency.py`: `2 passed`
- `tests/consistency/workbench_static.test.mjs`: `18 passed`
- recoverability artifact build:
  - [recoverability_summary.json](../../../data/generated/recoverability/recoverability_summary.json)
  - CSV and SVG outputs generated successfully

New generated branch artifacts in this pass:

- [periodic_functional_complexity_sweep.csv](../../../data/generated/recoverability/periodic_functional_complexity_sweep.csv)
- [periodic_threshold_stress_sweep.csv](../../../data/generated/recoverability/periodic_threshold_stress_sweep.csv)
- [diagonal_functional_complexity_sweep.csv](../../../data/generated/recoverability/diagonal_functional_complexity_sweep.csv)
- [diagonal_polynomial_threshold_sweep.csv](../../../data/generated/recoverability/diagonal_polynomial_threshold_sweep.csv)
- [periodic-functional-threshold.svg](../../assets/recoverability/periodic-functional-threshold.svg)
- [diagonal-functional-threshold.svg](../../assets/recoverability/diagonal-functional-threshold.svg)
- [periodic-threshold-stress.svg](../../assets/recoverability/periodic-threshold-stress.svg)
- [diagonal-polynomial-threshold.svg](../../assets/recoverability/diagonal-polynomial-threshold.svg)
- [nested-linear-threshold.svg](../../assets/recoverability/nested-linear-threshold.svg)

Most recent full repository gate:

- `./scripts/validate/run_all.sh`: passed
- Python suite: `100 passed`
- Workbench / Node suite: `18 passed`
- markdown link check: passed
- naming consistency check: passed
- static workbench asset check: passed
- browser smoke check on the updated Structural Discovery Studio: passed locally across periodic repair, control repair, qubit weaker-vs-stronger, and restricted-linear repair flows
- broader randomized projector / generator / sector tests: passed
- multi-grid MHD / CFD falsification sweeps: passed

## Failures Found And Fixed In This Pass

1. early control collision estimates were too dependent on coarse state sampling and understated the horizon-1 obstruction
2. workbench chart rendering leaked `NaN` SVG coordinates when switching among some recoverability system families
3. the control threshold chart was wired to the wrong input shape and silently degraded into an unavailable placeholder
4. older control-branch wording incorrectly treated the coordinate threshold as the whole control-side story
5. broad support-size and raw protected-rank heuristics survived in wording longer than they should have

Fixes applied:

- replaced the control collision estimate with an exact nullspace-on-a-box calculation on the finite family
- hardened the workbench line-chart renderer against non-finite data
- corrected the control threshold chart wiring so the displayed figure is again a real chart, not scaffolding
- generalized the periodic and control threshold tooling to real protected-function choices rather than one fixed headline variable
- promoted the structured collision gap into an explicit restricted-linear theorem layer and used it to replace weaker threshold heuristics

## Final Status

The branch-specific implementation is now passing:

- dedicated mathematical tests,
- dedicated workbench tests,
- generated-artifact checks,
- browser interaction smoke checks,
- and the full repository validation gate.

At this point the branch is no longer just a design document with one experiment script. It is a real implemented research lane with:

- formal notes,
- theorem and no-go documents,
- stronger family-level threshold results,
- reproducible experiment artifacts,
- a live workbench module,
- and explicit records of the branch results that failed or were demoted.
