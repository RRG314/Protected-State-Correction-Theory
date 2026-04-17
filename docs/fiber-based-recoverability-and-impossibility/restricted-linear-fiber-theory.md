# Restricted-Linear Fiber Theory

## Setup

Take the restricted family

```text
x = F z,
y = O F z,
p(x) = L F z.
```

The coefficient-space fibers are affine slices:

```text
z + ker(O F).
```

Their dimension is

```text
dim ker(O F) = dim(z) - rank(O F).
```

## Exactness criterion

Exact recoverability holds if and only if the target is constant on each affine fiber.
In the restricted-linear class this is equivalent to:

```text
ker(O F) ⊆ ker(L F)
```

and therefore to row-space inclusion:

```text
row(L F) ⊆ row(O F).
```

## Fiber interpretation of key results

- `OCP-045`: minimal augmentation theorem
  - add enough new measurements to refine the fibers until `ker(O~ F) ⊆ ker(L F)`
- `OCP-046`: exact-regime upper envelope
  - once fibers are target-constant, the exact decoder lifts record noise to a controlled target bound
- `OCP-047`: same-rank observation insufficiency
  - two systems can have the same amount yet different fiber alignment with the target
- `OCP-049`: no rank-only exact classifier theorem
  - equal rank does not determine whether the fibers are target-constant
- `OCP-050`: no fixed-library budget-only exact classifier theorem
  - equal sensor budget in one fixed library still does not determine whether the fibers are target-constant
- `OCP-051`: noisy weaker-versus-stronger separation theorem
  - weak target fibers are already constant while strong target fibers remain mixed
- `OCP-052`: family-enlargement false-positive theorem
  - exactness on a smaller family can fail immediately when the enlarged family adds hidden target-changing directions inside the record kernel

## Fiber refinement under augmentation

Adding measurements shrinks `ker(O F)`.
Exactness arrives exactly when the refined kernel stops carrying target variation.
That is the fiber form of the design-engine story.

## New canonical geometry and false-positive reports

The local branch now stores executable restricted-linear witnesses through:
- [`src/ocp/fiber_limits.py`](../../src/ocp/fiber_limits.py)
- [`restricted_linear_fiber_geometry.csv`](../../data/generated/unified-recoverability/restricted_linear_fiber_geometry.csv)
- [`family_enlargement_false_positive.csv`](../../data/generated/unified-recoverability/family_enlargement_false_positive.csv)
- [`model_mismatch_stress.csv`](../../data/generated/unified-recoverability/model_mismatch_stress.csv)

These reports are intentionally narrow.
They classify or stress:
- coefficient dimension,
- observation rank,
- affine fiber dimension,
- exact versus target-mixed status,
- row-space residual,
- collision gap,
- decoder drift under family enlargement,
- decoder drift under nearby model mismatch.

They do **not** claim that fiber dimension alone classifies exactness.
