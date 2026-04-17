# Fibers And Impossibility

## Fiber-collision impossibility

If a fiber contains two admissible states with different target values, exact recovery is impossible.

This is the branch’s clean impossibility core.

## Fiber interpretation of key no-go results

- overlap / indistinguishability no-go:
  - protected variation survives inside one correction fiber
- qubit phase-loss no-go:
  - the fixed-basis record fibers contain states with the same z statistics but different phase-sensitive targets
- divergence-only bounded no-go:
  - the divergence record fiber contains distinct bounded incompressible states
- bounded-domain projector transplant failure:
  - divergence is removed, but the architecture still leaves fibers that mix boundary-normal structure
- same-rank insufficiency:
  - same rank does not mean the fibers align with the target in the same way
- no rank-only or budget-only anti-classifier theorems:
  - amount-only invariants do not determine whether fibers are target-constant
- family-enlargement false positives:
  - exactness on one restricted family can fail as soon as the enlarged family restores a target-changing hidden fiber direction

## Best negative lesson

The real obstruction is not “low amount” in the abstract.
The real obstruction is target-mixed fibers.

The strongest current negative package is now:
- `OCP-049`,
- `OCP-050`,
- `OCP-052`.
