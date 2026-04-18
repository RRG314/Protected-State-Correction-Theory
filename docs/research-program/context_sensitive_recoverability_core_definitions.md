# Context-Sensitive Recoverability Core Definitions

Status: `EXPLORATION / NON-PROMOTED`
Scope class: finite/synthetic linear and context-structured families.

This file freezes notation for the main-track narrow theory pass.

## 1. Admissible Family

An admissible family is a tuple
`F = (X, T, C, A)`
where:
- `X` is the state space (finite or finite-dimensional linear in this pass),
- `T` is the target space,
- `C` is a finite context index set,
- `A` is the set of allowed observation/recovery constructions.

In the linear supported class used here:
- `X = R^n`,
- target is linear `tau(x) = t^T x`,
- each context `c in C` has observation map `M_c: R^n -> R^m`.

## 2. Target

`tau: X -> T` is the protected/desired quantity to be exactly recovered.

In the linear class, `tau` is represented by vector `t in R^n`.

## 3. Record / Observation Map

For each context `c`, observation is `M_c`.
The context family is `{M_c}_{c in C}`.

Contextwise record map: `x -> (M_c x)` for fixed `c`.
Shared record structure: all `{M_c}` considered jointly.

## 4. Conditioned Exactness

Conditioned exactness holds if every context admits an exact decoder:

`forall c in C, exists d_c such that d_c M_c = t`.

Equivalent supported-family condition:
`t` lies in the row space of each `M_c`.

## 5. Context-Invariant Exactness

Context-invariant exactness holds if one shared decoder works for all contexts:

`exists d_* such that forall c in C, d_* M_c = t`.

This is strictly stronger than conditioned exactness.

## 6. Context-Invariance Gap

Define the gap indicator:

`G_C(t) = I(conditioned exactness) - I(context-invariant exactness)`.

So `G_C(t) = 1` means local/contextwise exactness is present but shared exactness fails.

## 7. Context-Invariance Defect (CID)

For fixed family `{M_c}` and target `t`,

`CID_C(t) = min_d max_{c in C} ||d M_c - t||`.

`CID_C(t)=0` iff context-invariant exactness holds (in exact arithmetic).

## 8. Shared Augmentation

A shared augmentation of size `r` is a matrix `U in R^{r x n}` appended to every context map:

`M_c' = [M_c; U]` for all `c`.

## 9. Shared Augmentation Threshold

`r_*(C,t)` is the minimal `r >= 0` such that there exists shared augmentation `U` with context-invariant exactness for `{M_c'}`.

If no such augmentation exists in the allowed augmentation class, set `r_* = +infty`.

## 10. Descriptor-Only Summaries (for no-go tests)

Descriptor-only summaries used in this pass:
- stack rank `rank([M_c]_{c in C})`,
- total budget `sum_c m_c`,
- context count `|C|`.

These are treated as classifier candidates and explicitly tested for insufficiency.

## 11. Main-Track Scope Limits

This package does not claim these definitions are universal outside the supported families.
No promotion claim is made for nonlinear/infinite-dimensional/global physics settings in this pass.
