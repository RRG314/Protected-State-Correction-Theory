# Helmholtz-Hodge Velocity Projection

## Plain-Language Summary

Helmholtz / Hodge decomposition is the mathematical structure that makes the incompressible projection branch exact.

The decomposition matters because exact correction requires more than a low divergence number. It requires a real splitting of the ambient velocity field into:
- a protected divergence-free component,
- and a disturbance component that the correction operator can remove without touching the protected one.

## Protected Object And Disturbance Family

For the periodic branch, the decomposition is

```text
u = u_df + ∇φ,
```

with `u_df` divergence-free. Then:
- protected object: `u_df`
- disturbance family: `∇φ`
- correction operator: `P_df`

## Exact Recovery Rule

The exact recovery rule is

```text
R(u) = P_df u = u - ∇Δ^{-1}(div u).
```

This is a direct CFD realization of the exact projector branch already formalized elsewhere in the repository.

## Exactness Conditions

The fit stays exact only when all of the following remain true:
- the protected class really is the divergence-free subspace for the chosen domain and inner product,
- the contamination lies in the complementary gradient class,
- the projection operator is the correct Hodge projector for that same protected class,
- any boundary structure required by the protected class is built into the operator.

If these conditions fail, the fit drops from exact to conditional or rejected.

The repository now has a stronger bounded-domain positive result too:
- on an explicit finite-mode bounded family built from stream modes `J∇ψ` and Dirichlet gradient modes `∇φ`,
- the corresponding orthogonal projector is exact on that bounded family.

That result is recorded in:
- [Bounded-Domain Hodge Theorems](../theorem-candidates/bounded-domain-hodge-theorems.md)

## What This Adds Beyond Standard CFD Language

Standard CFD language often emphasizes the pressure Poisson solve or the fractional-step scheme. The protected-state language emphasizes the correction logic itself:
- what must be preserved,
- what is being removed,
- and what exact operator relation makes that removal legitimate.

That shift is small but useful. It helps explain why some projection steps are exact correction operators and others are only numerical surrogates.

## Repo Classification

- periodic exact projector branch: **PROVED exact fit**
- bounded-domain exact branch on the implemented boundary-compatible finite-mode Hodge family: **PROVED exact fit**
- broader bounded-domain exact branch with realistic discretizations and boundary treatments: **CONDITIONAL**
- boundary-insensitive transplant: **REJECTED**

## Related Files

- [Incompressible Projection In Protected-State Language](incompressible-projection.md)
- [Bounded Versus Periodic Projection](bounded-vs-periodic-projection.md)
- [CFD Versus MHD Correction Comparison](cfd-vs-mhd-correction-comparison.md)
