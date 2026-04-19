# Promoted Unifying Theorems

Date: 2026-04-17

## UTH-1 (Universal Recoverability Core)

Let `A` be an admissible family, `T : A -> Z` a target, and `M : A -> Y` an observation map.
The following are equivalent:
1. `T` is exactly recoverable from `M` on `A`.
2. `T` is constant on fibers of `M` over `A`.
3. `T` factors through `M` on `A`.

Status: `PROVED`.

Primary anchors:
- OCP fiber exactness (`OCP-030`),
- restricted-linear specialization (`OCP-031`).

## UTH-2 (Universal Collision No-Go Corollary)

If there exist `x,x' in A` with `M(x)=M(x')` and `T(x) != T(x')`, then no exact recovery map from `M(A)` to `Z` exists for `T` on `A`.

Status: `PROVED`.

Primary anchors:
- overlap/no-go and fiber-collision logic across OCP and soliton quotient lanes.

## UTH-3 (Branch-Limited Anti-Classifier Theorem Package)

Within the supported restricted-linear class:
- rank tuple alone does not classify exactness (`OCP-049`),
- fixed-library budget alone does not classify exactness (`OCP-050`).

Status: `PROVED` (supported class).
Soliton analogue: same-count opposite-verdict witnesses are `PROVED ON SUPPORTED FAMILY` + `CONDITIONAL` continuous extension.

## UTH-4 (Branch-Limited Fragility Package)

Within the supported OCP restricted-linear class:
- exactness can fail under admissible-family enlargement (`OCP-052`),
- exact-data mismatch can induce explicit decoder error floors (`OCP-053`).

Status: `PROVED` (declared classes).

## Promotion Guardrail

These promoted theorems define a branch-limited unifying framework. They are not promoted as one universal theorem for all nonlinear branches or emergence dynamics.
