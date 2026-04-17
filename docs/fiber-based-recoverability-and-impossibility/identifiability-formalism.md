# Identifiability Formalism

## Core setup

Let:
- `X` be a state space,
- `F ⊂ X` an admissible family,
- `M : F → Y` a record or observation map,
- `p : F → P` a protected target map.

The observation fiber over `y` is

```text
Fib_M(y) = { x in F : M(x) = y }.
```

## Exact target identifiability

The target `p` is exactly identifiable from `M` on `F` if there exists `g : M(F) → P` such that

```text
p = g ∘ M on F.
```

Equivalent branch language:
- `p` is constant on every observation fiber.

## Non-identifiable target

The target `p` is non-identifiable on `F` if there exist `x, x' in F` with

```text
M(x) = M(x')
```

but

```text
p(x) != p(x').
```

That is exact-data nonuniqueness for the target.

## Detectable-only / coarsened identifiability

A coarsened target `q = φ ∘ p` is exactly identifiable even when `p` is not.
This is the branch's detectable-only regime.

Interpretation:
- the current fibers are too coarse for `p`,
- but already fine enough for `q`.

## Exact target observability on an admissible family

In this branch, exact target observability means exact identifiability of the chosen target from the chosen record on the declared family.

This is deliberately target-specific.
The branch does **not** assume that full state observability follows.

## Observation refinement

A refined observation `M~` is finer than `M` if every `M~`-fiber lies inside an `M`-fiber.
Equivalently, the refined record separates at least as many admissible distinctions.

## Identifiability defect

The exact-data identifiability defect of `p` under `M` on `F` is the amount of target variation that remains inside one active fiber.

In finite or restricted-linear branch settings this is represented by:
- `κ(0)`,
- collision gap,
- row-space residual,
- or explicit fiber witnesses depending on the family.

## Minimal measurement augmentation

A minimal exact augmentation is the smallest added record structure that refines the fibers enough to make the target constant on them.

## False-positive recoverability claim

A positive exact-recovery claim is a false positive if it is asserted outside the family, target, architecture, or discretization that actually makes the theorem true.

Main branch sources:
- amount-only false positives: `OCP-049`, `OCP-050`
- family-enlargement false positives: `OCP-052`
- model-mismatch false positives: `OCP-053` and the validated stress suites
- target-swap false positives: `OCP-048`, `OCP-051`

## Family-restricted identifiability

A target may be exactly identifiable on one admissible family and non-identifiable on a larger family.
This is not a contradiction.
It is a branch-central caution about inverse-problem scope.

## Model-mismatch instability

A decoder exact on one family may incur positive error on a nearby family even when the target remains exactly identifiable on the true family.
That is not failure of identifiability on the true family.
It is failure of the wrong inverse map.
