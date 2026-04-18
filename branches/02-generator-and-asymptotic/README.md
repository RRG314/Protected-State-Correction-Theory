# Branch 02 — Generator and Asymptotic

## What this branch is
Asymptotic correction branch: generator-based suppression of disturbance while preserving protected structure.

## Strongest results
- Invariant-split generator theorem family.
- Mixing no-go for linear flows.
- Domain-specific asymptotic instantiations (GLM / damping style lanes).

## Canonical documents
- [Generator theorems](../../docs/theorem-candidates/generator-theorems.md)
- [No-go results](../../docs/impossibility-results/no-go-results.md)
- [GLM and asymptotic correction](../../docs/mhd/glm-and-asymptotic-correction.md)
- [Numerical relativity damping note](../../docs/physics/numerical-relativity-constraint-damping.md)

## Key tests / artifacts
- `tests/math/test_continuous_generators.py`
- `tests/examples/test_glm_decay.py`

## Open items
- Expand robustness constants and nonlinear stability boundaries with the same proof discipline.

## Shared infrastructure
Run branch computations from shared linear algebra and generated validation snapshot infrastructure.
