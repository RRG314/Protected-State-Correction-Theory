# CFD Projection Results

## Plain-Language Summary

This file collects the narrow CFD results that survive honest testing.

The conclusion is not that the repository now explains all of CFD. The conclusion is that incompressible projection methods give a real application lane for the exact projector branch, and bounded-domain correction yields a useful limitation result.

## Corollary OCP-CFD-C1: Periodic Incompressible Projection Is An Exact Protected-State Correction Operator

Let the periodic velocity field satisfy

```text
u = u_df + ∇φ,
```

with `div(u_df)=0`, and let

```text
P_df u = u - ∇Δ^{-1}(div u)
```

be the periodic Helmholtz / Hodge projector.

Then

```text
P_df u = u_df,
```

and `P_df` is an exact protected-state correction operator for the divergence-free velocity class.

### Status

`PROVED` as a direct corollary of the exact projector branch and the periodic Helmholtz/Leray anchor.

### Proof Sketch

The decomposition is orthogonal on the compatible periodic `L^2` branch, and the gradient part lies in the disturbance image. The projector annihilates the disturbance component and preserves the divergence-free component.

## Criterion OCP-CFD-C2: Pressure Projection Is Exact Only When It Realizes The Correct Domain-Compatible Hodge Projector

A pressure-correction step belongs to the exact branch only when the correction operator coincides with the projector for the actual protected class being used.

That requires the operator to match:
- the divergence constraint,
- the admissible decomposition,
- and the relevant boundary conditions.

### Status

`CONDITIONAL`

### Why This Matters

This criterion is the clean way to say why periodic projection is exact, why a domain-compatible bounded projector may also be exact in principle, and why boundary-insensitive transplants fail.

## No-Go OCP-CFD-N1: Divergence-Only Recovery Is Insufficient On A Nontrivial Bounded Protected Class

See [Bounded Versus Periodic Projection](../cfd/bounded-vs-periodic-projection.md).

### Status

`PROVED`

### Significance

This is the strongest new CFD-facing limitation result in the repository.

It says that exact bounded recovery cannot be reduced to a scalar divergence-fixing rule once the protected class contains multiple distinct divergence-free states.
