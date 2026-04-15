# Bounded Versus Periodic Projection

## Plain-Language Summary

This file is the main CFD scope-control document.

The periodic incompressible projection branch is a real exact fit. The bounded-domain branch is not automatically the same problem. The boundary conditions become part of the protected object, and that changes what an exact correction operator must preserve.

## The Periodic Branch

On the periodic branch, the protected class is:

```text
S = {u : div(u) = 0}.
```

The exact projector removes the gradient disturbance and returns the divergence-free component exactly.

## The Bounded-Domain Branch

On a bounded domain, the protected class is typically narrower. A more realistic protected class is something like:

```text
S_bc = {u : div(u)=0, u·n|_{∂Ω}=0}
```

or an analogous class with the correct boundary trace for the physical problem.

At that point, exact correction requires more than removing divergence. It must preserve the relevant boundary structure too.

## Stronger Positive Result

The bounded branch is no longer only negative.

The repo now proves a narrower exact result on an explicit finite-mode Hodge family:

```text
S_bc = span{ J ∇ψ_i },
G_0  = span{ ∇φ_j },
```

with boundary-compatible `ψ_i` and Dirichlet `φ_j`.

On that family the orthogonal projector onto `S_bc` is exact.

See:
- [Bounded-Domain Hodge Theorems](../theorem-candidates/bounded-domain-hodge-theorems.md)

## Sharper No-Go Result

### No-Go OCP-CFD-N1: Divergence-Only Recovery Is Insufficient On A Nontrivial Bounded Protected Class

Let `S_bc` be a protected class containing two distinct states `u_1`, `u_2` with the same divergence data. Suppose a candidate recovery architecture factors only through the divergence scalar field, so that

```text
R(u) = F(div u)
```

for some map `F`.

Then `R` cannot be an exact recovery operator on `S_bc`.

### Proof

Because `u_1` and `u_2` have the same divergence data,

```text
div u_1 = div u_2.
```

So a divergence-only architecture gives

```text
R(u_1) = F(div u_1) = F(div u_2) = R(u_2).
```

But exact recovery would require

```text
R(u_1) = u_1,
R(u_2) = u_2.
```

Since `u_1 ≠ u_2`, that is impossible.

### Consequence

For bounded incompressible correction, a scalar divergence field is not enough to recover the whole protected velocity class exactly. The correction architecture must carry enough information about the domain-compatible protected class, including the relevant boundary structure.

## Repository Counterexample

The repo also contains a direct numerical rejection of the naive transplant idea.

Applying the periodic FFT projector unchanged to a bounded-domain field can:
- drive divergence essentially to zero,
- while still producing the wrong boundary-normal trace.

So the operator stops being an exact correction operator for the bounded protected class.

## Honest Verdict

- periodic projection: **EXACT FIT**
- bounded-domain projection on the implemented boundary-compatible finite-mode Hodge family: **EXACT FIT**
- broader bounded-domain projection with the correct Hodge projector: **CONDITIONAL FIT**
- naive periodic reuse on bounded domains: **REJECTED**
- divergence-only bounded recovery: **PROVED NO-GO**

## Related Files

- [CFD System Matrix](cfd-system-matrix.md)
- [Kept Versus Rejected CFD Bridges](kept-vs-rejected-cfd-bridges.md)
- [Bounded-Domain Projection Limits](../physics/bounded-domain-projection-limits.md)
