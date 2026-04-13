# Maxwell / Coulomb-Gauge Projection

## Plain-Language Summary

This is the cleanest additional physics bridge that survives the audit.

The Maxwell-side interpretation is simple:
- the protected object is the transverse part of the field or vector potential,
- the disturbance is the longitudinal or pure-gradient part,
- and correction is a transverse projection.

That is a real operator-level fit to the exact branch. It is not a new theorem beyond the existing projection spine, but it is a legitimate physics extension.

## System Definition

On a projection-compatible domain such as a periodic box or a whole-space setting with the usual Fourier/Hodge decomposition,

```text
A = A_\perp + \nabla \chi,
```

with

```text
\nabla \cdot A_\perp = 0.
```

The protected object is `A_\perp`. The disturbance family is the longitudinal component `\nabla \chi`.

## Correction Architecture

The correction operator is the transverse projector

```text
P_\perp = I - \nabla \Delta^{-1} \nabla \cdot
```

on the compatible function class.

Then

```text
P_\perp A = A_\perp,
```

which is exactly the same operator structure as the periodic Helmholtz/Leray branch already proved in the repository.

## Exact Or Asymptotic?

This is an **exact** fit when the domain and function class support the projector cleanly.

It is not an asymptotic-damping architecture. It belongs on the exact side.

## What OCP Adds

What the repository adds here is not a new Maxwell theorem. It adds:
- a protected-object / disturbance-object interpretation,
- a direct comparison with QEC-style exact recovery,
- and a clean place for Maxwell projection inside the exact branch rather than inside vague gauge-language analogies.

## Fit Verdict

Verdict: **keep** as an exact physics extension.

Status inside the repo: **proved as a corollary-level fit**, not as a new standalone theorem.

## What To Cite

Useful outside anchors:
- [Abalos, "On constraint preservation and strong hyperbolicity" (Class. Quantum Grav. 39, 215004, 2022)](https://doi.org/10.1088/1361-6382/ac88af)
- [Berchenko-Kogan and Stern, "Constraint-preserving hybrid finite element methods for Maxwell's equations" (J. Comput. Phys. 409, 109340, 2020)](https://doi.org/10.1016/j.jcp.2019.109340)
- [Calabrese, "A remedy for constraint growth in numerical relativity: the Maxwell case" (Class. Quantum Grav. 21, 5735, 2005)](https://arxiv.org/abs/gr-qc/0404036)

## Limit

Do not overstate this bridge.

The exact fit is strongest when a real transverse projector exists on the chosen domain. Once the domain or boundary conditions change, the projector issue becomes more delicate and must be handled separately.
