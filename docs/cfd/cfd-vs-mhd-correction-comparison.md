# CFD Versus MHD Correction Comparison

## Plain-Language Summary

CFD and MHD meet the framework in closely related but not identical ways.

The narrow exact connection is the projection operator. The asymptotic connection is the family of damping and cleaning methods used when exact projection is unavailable, too expensive, or not built into the architecture.

## Shared Exact Structure

In both settings, the cleanest exact branch is projector-based:

- CFD protected object: divergence-free velocity field
- MHD protected object: divergence-free magnetic field
- disturbance family: gradient contamination or non-solenoidal numerical error
- exact operator: Helmholtz / Leray projection

That shared structure is real and operator-level.

## Shared Asymptotic Structure

When the method is not an exact projector, the correction architecture can still fit the asymptotic branch:

- CFD-side example: pressure-relaxation, pseudo-compressibility, or other iterative / damped enforcement schemes
- MHD-side example: GLM divergence cleaning

These belong to the asymptotic lane only when they reduce constraint error over time rather than remove it exactly in one correction step.

## Important Difference

The repo should not flatten CFD and MHD into one thing.

The exact operator class can match while the physical interpretation differs:
- CFD cares about incompressible velocity and pressure projection
- MHD cares about magnetic divergence control and field admissibility

The protected-state language helps compare the architectures without pretending the underlying equations are the same.

## What OCP Adds Here

The useful comparison is not that CFD and MHD are secretly identical.

The useful comparison is that both can be sorted into:
- exact projection-based correction,
- asymptotic damping/cleaning,
- and rejected shortcuts that fix one residual while damaging the protected class.

## Repo Verdict

Keep this comparison because it is structurally honest and helps explain the exact versus asymptotic split.
Do not promote it as a new fluid-unification theorem.
