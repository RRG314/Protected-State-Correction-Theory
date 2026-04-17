# Final Inverse / Observability Pass Report

## What new theorem-grade results survived?

### `OCP-052`
Restricted-linear family-enlargement false-positive theorem.

### `OCP-053`
Canonical model-mismatch instability theorem.

Clean content:
- on the canonical family `F_beta = span{e1, e2 + beta e3}` with record `M(x) = (x1, x2)` and target `p(x) = x3`, each fixed `beta` gives exact target identifiability,
- but a decoder exact on `beta0` incurs worst-case exact-data target error

```text
|beta - beta0| / sqrt(1 + beta^2)
```

on the true family `F_beta`.

That is a real inverse-problem result:
- the true family remains identifiable,
- but the wrong inverse map is measurably unstable under model mismatch.

## What claims failed under falsification?

Failed or refused:
- universal rank/count/budget classifiers,
- family-blind exactness claims,
- family-blind model-mismatch robustness,
- universal discretization-robust exactness,
- universal PDE-side observability laws.

## What outside problem classes does the branch now touch?

The branch now honestly touches:
- target identifiability under partial/coarse records,
- observability and sensor geometry,
- inverse-problem nonuniqueness and instability,
- model mismatch and false-positive inverse maps,
- bounded versus periodic reconstruction boundaries,
- exact versus asymptotic observability under limited history.

## Strongest current paper candidate

Best current paper candidate:
- a restricted theory/falsification paper on target identifiability and false-positive recovery claims under partial/coarse records,
- centered on `OCP-049` through `OCP-053`.

## Strongest realistic next theorem

Best next theorem target:
- weighted-cost or geometry-constrained anti-classifier theorems for sensor design,
- or a bounded-domain family-enlargement theorem on one richer PDE-side benchmark class.

## Where the branch is still too weak or too family-restricted

Still too weak:
- nonlinear extension,
- universal PDE inverse problems,
- universal robust inverse-map design,
- universal discretization stability.
