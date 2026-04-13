# Divergence Cleaning In OCP Language

## Plain-Language Summary

Projection-based divergence cleaning is the strongest continuous exact example in this repository.

What is protected is the physically admissible divergence-free part of the magnetic field. What is treated as disturbance is the gradient component that creates nonzero divergence. Helmholtz/Leray projection removes that unphysical component exactly on suitable domains.

## 1. Protected Object And Disturbance

On a periodic domain, a vector field admits a Helmholtz decomposition of the form

```text
B = B_df + ∇φ
```

where
- `div(B_df) = 0`,
- `∇φ` is the gradient part.

In OCP language:
- protected subspace `S`: divergence-free fields,
- disturbance space `D`: gradient fields,
- exact recovery operator: Leray projector `P_df`.

## 2. Exact Operator Construction

The exact correction operator is

```text
R(B) = P_df B = B - ∇Δ^{-1}(div B)
```

on the appropriate periodic or otherwise compatible domain.

This is the continuous analog of exact projector recovery in the finite-dimensional OCP model.

## 3. Why This Is A Strong OCP Anchor

This example is especially valuable because it provides all of the following in one place:
- an explicit protected space,
- an explicit disturbance space,
- an explicit decomposition rule,
- an explicit recovery operator,
- and an exact statement about what the operator does.

That is much stronger than a loose analogy.

## 4. Orthogonality

Under the `L^2` inner product on suitable domains, divergence-free fields and gradient fields are orthogonal after the usual boundary assumptions.

So this example is not merely “conceptually similar” to orthogonal correction. It is an actual projection-based orthogonal correction system.

## 5. Local Validation In This Repo

The local executable test constructs a field of the form

```text
B = B_phys + ∇φ
```

with `B_phys` divergence-free, applies `helmholtz_project_2d`, and checks that:
- the post-projection divergence is dramatically reduced,
- the recovered field matches the divergence-free component up to numerical tolerance,
- the `L^2` orthogonality residual is tiny.

## 6. What This Contributes Beyond QEC

QEC is the clean exact discrete anchor.
Projection-based divergence cleaning is the clean exact continuous anchor.

That matters because it shows that the OCP framework is not restricted to finite-dimensional logical code spaces. It can also describe exact protected-state correction in PDE-like settings when a real projection structure exists.
