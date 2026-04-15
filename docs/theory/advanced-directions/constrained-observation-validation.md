# Constrained-Observation Validation Summary

## Branch-Specific Code And Tests

Core implementation:

- [recoverability.py](../../../src/ocp/recoverability.py)
- [run_recoverability_examples.py](../../../scripts/compare/run_recoverability_examples.py)

Python tests:

- [test_recoverability.py](../../../tests/math/test_recoverability.py)

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
10. periodic protected-variable minimal-cutoff law on the three-mode family
11. discretization stability of the periodic protected-variable thresholds
12. one-step versus two-step versus observer-side control behavior
13. diagonal minimal-history threshold behavior on the three-state control family
14. interpolation-weight recovery against the independent pseudoinverse-based linear recovery operator

Workbench-side:

1. analytic exact-versus-impossible threshold behavior
2. qubit variable-sensitive recovery split
3. periodic exact / approximate / impossible split
4. periodic protected-variable cutoff thresholds
5. control finite-history versus observer asymptotics
6. diagonal minimal-history threshold behavior in the three-state control lane
7. existing exact / QEC / MHD / CFD / gauge / generator / no-go modules still pass
8. share-state encoding and decoding still round-trip correctly

## Current Validation Snapshot

Most recent targeted branch checks completed during this pass:

- `tests/math/test_recoverability.py`: `14 passed`
- `tests/consistency/workbench_static.test.mjs`: `16 passed`
- recoverability artifact build:
  - [recoverability_summary.json](../../../data/generated/recoverability/recoverability_summary.json)
  - CSV and SVG outputs generated successfully

Most recent full repository gate:

- `./scripts/validate/run_all.sh`: passed
- Python suite: `40 passed`
- Workbench / Node suite: `16 passed`
- markdown link check: passed
- naming consistency check: passed
- static workbench asset check: passed
- browser smoke check on the updated Recoverability Lab: completed locally during this pass

## Failures Found And Fixed In This Pass

1. early control collision estimates were too dependent on coarse state sampling and understated the horizon-1 obstruction
2. workbench chart rendering leaked `NaN` SVG coordinates when switching among some recoverability system families
3. the control threshold chart was wired to the wrong input shape and silently degraded into an unavailable placeholder

Fixes applied:

- replaced the control collision estimate with an exact nullspace-on-a-box calculation on the finite family
- hardened the workbench line-chart renderer against non-finite data
- corrected the control threshold chart wiring so the displayed figure is again a real chart, not scaffolding

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
