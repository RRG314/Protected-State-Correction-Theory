# Operator Constructions

## Plain-Language Summary

The repository is only worth keeping if it builds real operators, not just descriptive language. This section records the strongest operator constructions currently available.

## 1. Finite-Dimensional Exact Projector

Given an inner-product space `H` with orthogonal splitting

```text
H = S ⊕ D,
```

the exact recovery operator is the orthogonal projector `P_S`.

Properties:
- `P_S(s) = s` for `s in S`,
- `P_S(d) = 0` for `d in D`,
- `P_S(s+d)=s` for all admissible states.

This is implemented in [core.py](../../src/ocp/core.py).

## 2. Complementary Disturbance Projector

The complementary projector is

```text
P_D = I - P_S
```

in the orthogonal exact setting.

This gives the decomposition rule

```text
x = P_S x + P_D x.
```

That is the cleanest algebraic realization of the “protected part plus disturbance part” language.

## 3. Continuous Damping Operator

For asymptotic correction, the simplest generator is

```text
K = k P_D,   k > 0.
```

Then

```text
x_dot = -Kx
```

has solution

```text
x(t) = P_S x(0) + e^{-kt} P_D x(0).
```

This gives exact preservation of `S` and exponential decay of `D`.

## 4. QEC Recovery Structure

The QEC branch requires a sector-based operator family rather than one global projector.

The relevant objects are:
- code projector `P_C`,
- error family `{E_a}`,
- sector projectors onto `E_a C`,
- recovery family `{R_a}` conditioned on syndrome sectors.

The executable code in [qec.py](../../src/ocp/qec.py) now does two concrete things for the 3-qubit bit-flip code:
- verifies the Knill-Laflamme condition numerically,
- and constructs a coherent sector-recovery family that maps each tested single-bit-flip sector back to the code space.

## 5. Helmholtz/Leray Projection

For divergence cleaning on a periodic domain, the exact continuous recovery operator is

```text
P_df B = B - ∇Δ^{-1}(div B).
```

This is implemented in [mhd.py](../../src/ocp/mhd.py) as `helmholtz_project_2d`.

Properties:
- returns the divergence-free component,
- removes the gradient contamination,
- provides the best exact continuous OCP example in the repo.

## 6. GLM Correction Law

GLM cleaning is represented in the repo by `glm_step_2d`.

This is not an exact projector. It is a correction evolution law:
- introduce auxiliary `ψ`,
- update `B` through gradients of `ψ`,
- damp the divergence error through the coupled dynamics.

It is useful precisely because it shows what an asymptotic correction operator looks like when exact projection is unavailable or undesirable.

## 7. Failure Conditions For Operator Construction

Operator construction fails, or becomes uninteresting, when:
- no valid protected/disturbance decomposition exists,
- the disturbance family is not distinguishable,
- the candidate correction operator acts nontrivially on `S`,
- or the target disturbance is outside the image reachable by the correction architecture.

Those failure cases are not bugs in the exposition. They are central outputs of the OCP program.
