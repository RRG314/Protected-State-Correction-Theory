# Fibers And Exact Recoverability

## Universal exactness theorem

Exact recoverability holds if and only if the target is constant on every record fiber.

Equivalent forms:
1. exact decoder exists
2. target is fiber-constant
3. target factors through the record map

This is the universal exact backbone of the branch.
It is standard, but it is also the cleanest organizing principle.

## Fiber interpretation of older branch results

- `OCP-030`: observation fiber exactness
  - exact recoverability means no target variation remains inside any record fiber
- `OCP-031`: restricted linear exactness
  - in the linear class, target-constant fibers become the kernel condition `ker(O F) ⊆ ker(L F)`
- `OCP-046`: exact-regime upper envelope
  - once fibers are target-constant and an exact linear decoder exists, record perturbations lift to a controlled upper bound on target ambiguity

## What exactness does not mean

Exactness does not mean:
- high rank by itself
- many sensors by itself
- small fiber dimension in some naive sense

It means: target constancy on the actual fibers that the chosen record induces on the admissible family.
