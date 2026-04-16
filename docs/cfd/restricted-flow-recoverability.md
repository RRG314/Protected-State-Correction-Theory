# Restricted Flow Recoverability

This note states the cleanest CFD-facing lesson from the recoverability branch.

## Main point

On restricted modal or linear flow families, exact recoverability is not controlled by raw information amount alone.
It is controlled by whether the record resolves the protected flow quantity.

In the simplest restricted-linear form:
- state family: `x in A_B = {F z : ||z||_inf <= B}`
- record: `y = O F z`
- protected variable: `p(x) = L F z`

Exact recovery is possible iff

$$
\operatorname{row}(L F) \subseteq \operatorname{row}(O F).
$$

This is the clean row-space form of the same fact that appears as a support-threshold law on the periodic modal CFD family.

## What this does not mean

It does **not** mean that arbitrary CFD state estimation is solved by rank language.
The statement is restricted to explicit finite-dimensional admissible families.

## Why the new CFD repo exists

The standalone CFD repo takes this restricted theorem spine and re-expresses it in CFD-first language:
- periodic projection
- bounded-domain failure
- modal flow functionals
- sensor / observation sufficiency
- exact versus asymptotic cleaning
