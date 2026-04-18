# Formal Core Definitions

Status: theorem-first canonical definitions for the current strongest narrow core.
Scope: finite-dimensional linear families with context-indexed observations and declared augmentation class.

## 1. Admissible Family

An admissible family is
`F = (X, C, T, M, A)`
with:
- `X = R^n` state space,
- `C = {1, ..., k}` finite context index set,
- `T = R` (or finite-dimensional target codomain),
- `M = {M_c}_{c in C}`, each `M_c: R^n -> R^m`,
- `A` augmentation class (allowed shared added rows/channels).

## 2. Target Map

A protected target map is `tau: X -> T`.
In the core supported class:
`tau(x) = t^T x` for fixed `t in R^n`.

## 3. Context Record Maps

Each context has a record map
`y_c = M_c x`.
The context stack is
`M_stack = [M_1; ...; M_k]`.

## 4. Conditioned Exactness

Conditioned exactness holds when each context separately has an exact linear decoder:
`forall c, exists d_c in R^m such that d_c M_c = t`.
Equivalent condition in the linear class:
`t` lies in the row space of every `M_c`.

## 5. Context-Invariant Exactness

Context-invariant exactness holds when one shared decoder works across all contexts:
`exists d_* in R^m such that forall c, d_* M_c = t`.

## 6. Shared Decoder Feasibility Equation (Context Lift)

Define the lifted system
`A d = b` with
`A = [M_1^T; ...; M_k^T]`,
`b = [t; ...; t]`.
Shared exactness holds iff the lifted system is consistent.

## 7. Context-Invariance Gap

Define
`G(F,t) = I(conditioned_exact) - I(invariant_exact)`.
`G=1` means local/contextwise exactness with shared-decoder failure.

## 8. Context Compatibility Defect

Define
`CID(F,t) = min_d max_{c in C} ||d M_c - t||_2`.
In this linear core, `CID=0` iff context-invariant exactness holds.

## 9. Shared Augmentation

A shared augmentation of size `r` is `U in R^{r x n}` added to all contexts:
`M'_c = [M_c; U]` for all `c`.

## 10. Shared Augmentation Threshold

Given augmentation class `A`, define
`r_*(F,t;A) = min r >= 0` such that there exists `U in A` with invariant exactness for `{M'_c}`.
If none exists in `A`, set `r_* = +infty`.

## 11. Opposite-Verdict Witness Family

A descriptor map `a: F -> D` is descriptor-only when it uses amount-like summaries (for example `rank(M_stack)`, total budget `k*m`, context count `k`).
An opposite-verdict witness pair is `(F_1,F_2)` such that:
- `a(F_1)=a(F_2)`,
- invariant exactness differs.

## 12. Amount-Only Descriptor Class

The base descriptor class used in this pass is:
`D_amt = (n, k, m, rank(M_stack), k*m)`.
No theorem in this pass assumes `D_amt` is complete.
It is tested as a potential classifier and often fails.

## 13. Domain-Geometry Variant (CFD/MHD-facing)

For domain-labeled families, include a geometry/domain tag `g` in the family metadata:
`F_g = (X_g, C, T, M_g, A_g)`.
Descriptor matches across distinct `g` do not imply equal exactness.

## 14. Exact Scope Boundaries

These definitions are canonical for the current theorem program only on declared supported families.
They do not imply unrestricted nonlinear/infinite-dimensional/global-physics claims.
