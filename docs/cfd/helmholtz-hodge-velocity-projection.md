# Helmholtz-Hodge Velocity Projection

Helmholtz-Hodge decomposition is the mathematical mechanism behind exact projection-based incompressible correction. The key point is structural: exactness requires a real decomposition into a protected divergence-free part and a removable gradient part under a compatible domain/boundary setting.

On the periodic branch, `u = u_df + ∇φ` with `div(u_df)=0`, and the correction map

$$
R(u)=P_{df}u=u-\nabla\Delta^{-1}(\operatorname{div}u)
$$

is exact for the declared protected class.

On bounded branches, exactness depends on whether the protected class and decomposition are boundary-compatible. The repository now includes a narrow positive bounded-domain finite-mode Hodge result, but broad bounded-domain transfer remains conditional or false depending on architecture.

This note should be read together with `docs/cfd/bounded-vs-periodic-projection.md` and `docs/theorem-candidates/bounded-domain-hodge-theorems.md`.
