# No-Go And Impossibility Results

## Plain-Language Summary

The no-go side is one of the strongest parts of this program. It keeps OCP from collapsing into the empty claim that “good correction should be good.”

A correction framework only means something if it can also say when correction is impossible, ambiguous, or underpowered.

## No-Go OCP-N1: Overlap Kills Exact Recovery

Let `H` be a vector space and let `S` and `D` be subspaces with

```text
S ∩ D ≠ {0}.
```

Then there is no single-valued map `R` on the set of states `s+d` that satisfies

```text
R(s+d)=s
```

for all `s in S` and `d in D`.

### Proof

Pick `0 ≠ v in S ∩ D`.

Then the same ambient state can be written in two admissible ways:

```text
v = v + 0 = 0 + v.
```

If exact recovery held for all admissible decompositions, then we would need both

```text
R(v)=v
```

from the first decomposition and

```text
R(v)=0
```

from the second.

This is impossible. Therefore no such single-valued exact recovery map exists.

## No-Go OCP-N2: Non-Preserving Correction Cannot Be Exact

Suppose `R` is claimed to be an exact recovery map for protected subspace `S` and disturbance space `D`.

If there exists `s in S` such that `R(s) ≠ s`, then `R` cannot be an exact recovery map.

Likewise, if there exists `d in D` such that `R(d) ≠ 0`, then `R` cannot annihilate the disturbance family exactly.

This is elementary, but important: a candidate correction operator that damages the protected component is disqualified immediately.

## No-Go OCP-N3: Disturbance Outside The Reach Of The Correction Architecture

This is currently a theorem schema rather than a finished theorem.

Informal statement:

> If the admissible disturbance family contains directions outside the image that the correction architecture can detect or suppress, then exact correction is impossible for the full family and asymptotic correction is impossible for those unreachable directions.

This is the right general statement behind many failures:
- insufficient syndrome information,
- insufficient control authority,
- underresolved PDE correction structure,
- and underparameterized correction laws.

Current status:
- `THEOREM SCHEMA`, not promoted as a finished theorem.

## No-Go OCP-N4: No Universal Scalar Correction-Capacity Number

This is inherited structurally from the earlier correction-gap work and retained here as a program boundary.

The current repo does **not** support the claim that one scalar correction-capacity number nontrivially classifies QEC, projection-based PDE cleaning, GLM feedback cleaning, and control architectures all at once.

Why not:
- the exact objects differ too much across categories,
- the relevant disturbance families are encoded differently,
- and forcing one scalar measure too early collapses the theory into metaphor.

This no-go result is important because it protects the repo from inflated unification claims.


## No-Go OCP-N5: Mixing Into The Protected Coordinates Breaks OCP Correction

Let `H = S ⊕ D` and let `P_S` be the projector onto `S`. Consider the linear flow

```text
x_dot = -Kx.
```

If `P_S K P_D` is nonzero, then there exists `d in D` such that the protected component changes immediately:

```text
rac{d}{dt} P_S x(t)ig|_{t=0} = - P_S K d 
eq 0.
```

Therefore the flow does **not** preserve the protected component for all disturbed initial states, and it cannot serve as an OCP correction flow that leaves `S` fixed pointwise.

### Why This Matters

This is a useful practical failure test. It rejects correction architectures that appear stabilizing overall but only by leaking disturbance into the protected coordinates.

## Why The No-Go Program Matters

The best current use of OCP may be partly negative:
- identifying when a proposed correction architecture is structurally incapable of exact recovery,
- identifying when orthogonality or distinguishability is missing,
- and rejecting architectures that only appear to correct because the protected object was never defined carefully.
