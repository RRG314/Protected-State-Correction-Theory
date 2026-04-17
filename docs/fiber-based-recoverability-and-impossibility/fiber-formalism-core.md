# Fiber Formalism Core

## Basic objects

- `X`: state space
- `F ⊂ X`: admissible family
- `M : F → Y`: record / observation map
- `p : F → P`: protected target
- `A`: admissible decoder / controller / correction architecture class when needed

## Fiber

For `y ∈ M(F)`, define the record fiber

```text
Fib_M(y) = { x ∈ F : M(x) = y }.
```

## Fiber compatibility

The target `p` is fiber-compatible with `M` on `F` if it is constant on every record fiber.
This is the branch's exactness backbone.

## Fiber separation

The record separates the target if distinct target values never remain in the same fiber.
This is equivalent to exact recoverability.

## Fiber collapse

Fiber collapse refers to the loss of distinctions caused by `M`:
- harmless collapse if the target stays constant on the collapsed states
- destructive collapse if the fiber mixes target values

## Exact recoverability

The target `p` is exactly recoverable from `M` on `F` if there exists `R : M(F) → P` such that

```text
p(x) = R(M(x))
```

for every `x ∈ F`.

Equivalent fiber form:
- `p` is constant on every fiber of `M`

## Impossible regime

Exact recovery is impossible if some fiber contains target variation:

```text
∃ y, x, x' ∈ Fib_M(y) with p(x) ≠ p(x').
```

## Approximate / stable recoverability

Approximate or stable recoverability asks whether the target varies only weakly on nearby or noisy fibers.
In this repo the main quantitative branch object is the collapse-modulus style lower-bound language rather than one universal stability metric.

## Asymptotic recoverability

Asymptotic recoverability means the present record does not give an exact static decoder, but a time-dependent or observer architecture can drive the target error to zero or to a controlled asymptotic regime.

## Detectable-only regime

Detectable-only means the full target is not constant on fibers, but a coarsening of the target is.
If `q = φ ∘ p`, then the branch detectable-only regime is:
- `q` exact on fibers of `M`
- `p` not exact on fibers of `M`

## Target coarsening

A weaker target `q` is a coarsening of `p` if `q = φ ∘ p` for some map `φ`.
Coarsening never asks for finer fiber separation than the original target.

## Weaker and stronger targets

A weaker target is a coarsening or projection of a stronger one.
The stronger target needs finer fiber separation.
The weaker target may survive on coarser fibers.

## Fiber refinement under augmentation

Adding measurements replaces `M` by an augmented map `M~`.
This refines fibers:

```text
Fib_M~(y~) ⊆ Fib_M(y).
```

Exact recovery becomes possible when the refined fibers stop mixing target values.

## Fiber size / complexity

What is supportable here:
- finite fibers in small explicit witnesses
- affine / linear fibers in the restricted-linear class
- nested fibers under added measurements
- target-constant versus target-mixed fibers
- coefficient-space fiber dimension in the restricted-linear class

What is not claimed:
- a universal nonlinear fiber geometry
- a universal scalar complexity that classifies exactness above the fiber-compatibility level

What is not promoted here:
- a universal geometric theory of curved fibers across all fields
