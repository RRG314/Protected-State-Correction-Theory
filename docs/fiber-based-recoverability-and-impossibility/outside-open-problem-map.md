# Outside Open-Problem Map

This note maps the branch to recognized outside problem classes instead of repo-internal slogans.

## Partial-observation identifiability

Current branch contact:
- `OCP-030`, `OCP-048`, `OCP-051`

What is already handled:
- exact target identifiability fails as soon as the target varies on one active fiber,
- weaker targets can remain exactly identifiable under the same coarse record.

Realistic next theorem target:
- target hierarchy theorems on richer supported families.

Dangerous false-positive mode:
- narrating weaker-target success as if the stronger target were recovered.

## Observability / sensor placement

Current branch contact:
- `OCP-047`, `OCP-049`, `OCP-050`

What is already handled:
- same rank, same count, and same unit-budget can still give opposite exactness verdicts.

Realistic next theorem target:
- weighted-cost or geometry-constrained anti-classifier theorems.

Dangerous false-positive mode:
- treating sensor amount as sufficient without checking fiber geometry.

## Inverse problems with nonuniqueness

Current branch contact:
- `OCP-030`, `OCP-052`

What is already handled:
- exact-data collisions already kill exact recovery,
- exactness on a narrow family can fail under honest family enlargement.

Realistic next theorem target:
- stronger lower bounds under structured family enlargement on supported PDE-side classes.

Dangerous false-positive mode:
- reporting exact recovery without declaring the admissible family.

## Model mismatch / false inverse maps

Current branch contact:
- `OCP-053`,
- validated model mismatch stress suite.

What is already handled:
- true-family exact identifiability does not make a mismatched inverse map exact,
- and the mismatch error can be stated in closed form on a canonical restricted-linear class.

Realistic next theorem target:
- broader model-mismatch error laws on richer supported linear families.

Dangerous false-positive mode:
- evaluating a decoder only on the training family and calling that a robust inverse result.

## PDE / CFD / bounded-domain recovery

Current branch contact:
- periodic support thresholds,
- bounded-domain projector mismatch,
- periodic refinement false-positive witness.

What is already handled:
- bounded versus periodic architecture mismatch,
- coarse modal truncation can hide hidden target-changing directions.

Realistic next theorem target:
- one bounded-domain family-enlargement theorem on a richer supported class.

Dangerous false-positive mode:
- coarse discretization or wrong projector making exactness look broader than it is.

## Control-side observability

Current branch contact:
- finite-history versus observer asymptotics,
- diagonal history thresholds.

What is already handled:
- exact and asymptotic recovery are genuinely distinct,
- selected functionals can become exact before full-state-style recovery is available.

Realistic next theorem target:
- one restricted equivalence theorem linking exact target observability, coarsened detectability, and observer asymptotics.

Dangerous false-positive mode:
- narrating asymptotic observer convergence as if it were finite-record exact identifiability.
