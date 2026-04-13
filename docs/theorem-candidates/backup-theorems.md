# Backup Theorems And Supporting Propositions

## Plain-Language Summary

The repository has one clean central theorem and a few narrower supporting results. These are important because they show the framework is not just a definition package.

## Theorem OCP-T2: Continuous Damping On The Disturbance Space

Let `H = S ⊕ D` with `S ⟂ D`, and let `P_D` be the orthogonal projector onto `D`. Fix `k > 0` and consider

```text
x_dot = -k P_D x.
```

Then the solution with initial condition `x(0)=x_0` is

```text
x(t) = P_S x_0 + e^{-kt} P_D x_0.
```

In particular:
- the protected component is preserved exactly,
- the disturbance component decays exponentially,
- and `x(t) -> P_S x_0` as `t -> ∞`.

### Proof Sketch

Because `P_D` is a projector and commutes with `P_S = I - P_D`, decompose `x = s + d` with `s = P_S x`, `d = P_D x`. Then

```text
s_dot = 0,
 d_dot = -k d.
```

So `s(t)=s(0)` and `d(t)=e^{-kt} d(0)`.

## Proposition OCP-P1: Any Exact Recovery Must Preserve S And Kill D

If a linear operator `R` is an exact recovery on `S ⊕ D`, then necessarily

```text
R|_S = I_S,   R|_D = 0.
```

This is immediate by testing `R` on states of the form `s+0` and `0+d`.

## Proposition OCP-P2: Helmholtz Projection Is An Exact Continuous OCP Operator

On a periodic domain with the standard `L^2` pairing and admissible regularity assumptions, the Helmholtz/Leray projector `P_df` exactly recovers the divergence-free component of a field `B = B_df + ∇φ`.

This is the continuous analogue of OCP-T1.

## Proposition OCP-P3: GLM Cleaning Defines An Asymptotic Correction Architecture

Under stable parameter choices and on the tested examples in this repository, repeated GLM updates reduce the divergence norm, making GLM a practical asymptotic OCP-style correction architecture.

Status note:
- this proposition is intentionally weaker than a full theorem,
- because the repo currently validates it by structural derivation plus local numerical behavior rather than by a full PDE proof.
