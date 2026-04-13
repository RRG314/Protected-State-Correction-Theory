# Control-Theoretic Extension

## Plain-Language Summary

Control theory belongs in OCP only in a careful, conditional way.

The clean fit is not “all feedback is correction.” The clean fit is:
- there is a protected component we want to preserve,
- there is a disturbance component we want to suppress,
- the split is dynamically meaningful,
- and the controller or observer acts on the disturbance coordinates without damaging the protected part.

If those conditions are missing, the OCP analogy is too loose.

## 1. Candidate Setup

Consider a linear system

```text
x_dot = A x + B u + w
```

with a proposed decomposition

```text
x = s + d,   s in S,   d in D.
```

The control-theoretic OCP question is whether we can choose feedback or observer dynamics so that:
- the `S` component is preserved or tracked,
- the `D` component is contracted or rejected,
- and the correction mechanism does not itself corrupt `S`.

## 2. Conditional Exact/Asymptotic Split

In most control systems, exact one-step recovery is not the right target. The more natural target is asymptotic correction.

A useful OCP-style sufficient condition is:
- `S` is invariant under the protected dynamics,
- `D` is invariant under the correction dynamics,
- controller or observer feedback acts only on `D`,
- the closed-loop dynamics on `D` are contractive or Hurwitz.

Then the disturbance coordinates decay while the protected coordinates remain fixed or follow their intended law.

## 3. Separation Principle Connection

The separation principle is relevant but not identical to OCP.

It helps because it separates estimation and control under suitable assumptions. But OCP asks a different question:

> Does the correction structure act on the error component without corrupting the protected one?

That is closer to an invariant splitting problem than to a generic feedback-design statement.

## 4. A Useful Theorem Schema

A defensible theorem schema is:

> If `H = S ⊕ D`, both subspaces are invariant under the chosen decomposition of the closed-loop generator, and the `D` block is exponentially stable while the `S` block is untouched, then the closed-loop system is an asymptotic OCP system.

This is meaningful, but still narrower than a general control theorem.

## 5. Why This Branch Stays Conditional

The control branch is not promoted as exact for several reasons:
- many controllers mix coordinates rather than respecting a protected/disturbance split,
- the relevant split may depend on coordinates or modeling choices,
- measurement noise and unmodeled dynamics can blur distinguishability,
- and invariance of `S` is often the real hard part.

## 6. Practical Value

Even without a deep new control theorem, OCP gives a useful design checklist:
- identify the protected coordinates explicitly,
- identify the disturbance coordinates explicitly,
- check whether the proposed correction law acts only on the disturbance coordinates,
- and reject architectures that “correct” by also damaging the protected dynamics.

That is a real engineering use, even if the branch remains theorem-light for now.

## 7. Worked Example

A concrete finite-dimensional example now lives in [worked-linear-example.md](worked-linear-example.md). It realizes the conditional control picture in the cleanest invariant-split setting.
