# Control / Observability Mapping

## Status

`CONDITIONAL` mapping note with exact restricted-linear content.

## Native field language

Classical systems theory distinguishes:
- observability,
- detectability,
- reconstructability,
- and observer-based asymptotic recovery.

Classical anchor:
- Kalman / systems-theory observability language.

## Branch translation

- `F`: admissible initial-condition family,
- `M_{0:H}`: output history of length `H`,
- `p`: state or functional of the initial state,
- exact recoverability: finite-history exact reconstruction,
- asymptotic recoverability: observer convergence,
- impossible: hidden protected direction survives the entire allowed record.

## Exact match

The restricted-linear branch is a clean fit.
For finite-dimensional linear families:
- row-space inclusion is the exact finite-history condition,
- interpolation thresholds determine minimal horizon on the diagonal family,
- observer convergence realizes asymptotic recoverability without finite exactness.

## Important non-identity

The branch's **detectable-only** regime is not identical to classical detectability.

Classical detectability is a dynamical notion about unobservable modes being asymptotically stable.
The branch's detectable-only regime is a target hierarchy notion:
- a coarsened target is exactly recoverable,
- the stronger target is not.

The two ideas are related, but they should not be conflated.

## Strongest kept example

The control toy family in the repo shows all three behaviors cleanly:
- one-step exact recovery fails,
- two-step protected-variable recovery is exact,
- and observer-based recovery converges asymptotically.

That is one of the branch's best exact-vs-asymptotic anchor examples.
