# Incompressible Projection in Protected-State Language

This note gives the exact periodic CFD anchor in repository language.

For a periodic velocity field written as `u = u_df + ∇φ` with `div(u_df)=0`, the projector

$$
P_{df}u = u - \nabla\Delta^{-1}(\operatorname{div}u)
$$

recovers the divergence-free component exactly. In branch terms, `u_df` is the protected target, `∇φ` is disturbance, and `P_df` is the correction operator.

The result is standard CFD structure, not a new CFD algorithm. What the repository adds is a recoverability classification that makes explicit why this case is exact and why nearby bounded-domain cases are not automatically exact.

Validation in this repo checks divergence reduction, recovery of the known divergence-free component, and projector consistency on the tested periodic families.

Relevant files:
- `src/ocp/cfd.py`
- `tests/math/test_cfd_projection.py`
- `docs/cfd/bounded-vs-periodic-projection.md`
