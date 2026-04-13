# Incompressible Projection In Protected-State Language

## Plain-Language Summary

This is the strongest narrow CFD fit in the repository.

In projection-based incompressible CFD, the protected object is the divergence-free velocity field. The unwanted part is the non-solenoidal contamination, often introduced by an intermediate predictor step or by explicit gradient contamination. The correction operator is the Helmholtz / Hodge projector, or equivalently the pressure-projection step when it realizes that projector.

That is a real operator-level fit to Protected-State Correction Theory.

## Governing Setting

Take a periodic velocity field written as

```text
u = u_df + ∇φ,
```

with

```text
div(u_df) = 0.
```

Then the incompressible projection operator is

```text
P_df u = u - ∇Δ^{-1}(div u).
```

In the repo's language:
- protected object: divergence-free velocity component `u_df`
- disturbance family: gradient contamination `∇φ`
- correction operator: exact projector `P_df`
- classification: exact

## Exact Fit Verdict

Verdict: **EXACT FIT** on the periodic branch.

This is not a loose analogy. The operator is explicit, idempotent, and orthogonal under the standard `L^2` pairing on the compatible domain. The corrected field is exactly the protected component.

## What Is Standard Known CFD Structure

Standard incompressible projection methods already use this structure.

The repo is not claiming to invent pressure projection, Helmholtz decomposition, or Chorin-style fractional-step correction. Those belong to the established CFD literature.

## What Protected-State Correction Adds

The value added here is not a new CFD algorithm. It is a cleaner formal classification:
- what is protected,
- what counts as disturbance,
- what the exact correction operator is,
- and why exactness depends on the decomposition actually matching the protected class.

That classification becomes useful later when the bounded-domain branch stops behaving like the periodic branch.

## Theorem Links

- [Backup Theorems And Supporting Propositions](../theorem-candidates/backup-theorems.md)
- [CFD Projection Results](../theorem-candidates/cfd-projection-results.md)
- [Divergence Cleaning In OCP Language](../mhd/divergence-cleaning-in-ocp.md)

## Validation In This Repo

The executable periodic report checks that:
- divergence drops from a large pre-projection value to machine-scale,
- the projected velocity matches the known divergence-free component,
- the projection is idempotent,
- the orthogonality residual is tiny.

Relevant files:
- `src/ocp/cfd.py`
- `tests/math/test_cfd_projection.py`

## Outside Research

Useful anchors:
- [Chorin, "Numerical solution of the Navier-Stokes equations"](https://doi.org/10.1090/S0025-5718-1968-0242392-2)
- [Brown, Cortez, and Minion, "Accurate Projection Methods for the Incompressible Navier-Stokes Equations"](https://www.sciencedirect.com/science/article/pii/S0021999101967154)
- [Guermond, Minev, and Shen, "An overview of projection methods for incompressible flows"](https://doi.org/10.1016/j.cma.2005.10.010)
