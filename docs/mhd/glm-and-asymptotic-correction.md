# GLM And Asymptotic Correction

## Plain-Language Summary

GLM divergence cleaning is useful to OCP, but it should not be mislabeled as an exact projector. Its real value is as an **asymptotic correction architecture**.

It propagates and damps divergence error rather than removing it in one exact projection step.

## 1. Structural Role

In Dedner-style GLM cleaning, an auxiliary scalar field `ψ` is introduced and coupled to the magnetic field so that divergence error is transported and damped.

This gives a correction architecture with three important features:
- it targets the unphysical part of the field indirectly,
- it is continuous in time,
- and it is not exactly the same as applying `P_df`.

## 2. OCP Interpretation

The protected object is still the divergence-free physical field.
The disturbance is still the divergence-producing component.
The difference is in the recovery law:
- projection cleaning uses an exact projector,
- GLM uses an evolution law that reduces the disturbance over time.

That places GLM on the asymptotic OCP branch.

## 3. Why It Is Not Exact

GLM is not promoted as exact for several reasons:
- the disturbance component is not annihilated in one step,
- the correction is mediated through an auxiliary field,
- and the method depends on propagation and damping parameters.

So the right language is not “exact protected-state recovery.” It is “continuous asymptotic suppression of a constrained error mode.”

## 4. What The Repo Tests

The local test applies repeated `glm_step_2d` updates and checks that the `L^2` divergence norm decreases over the tested time window.

That supports the asymptotic-correction interpretation, but it does not upgrade GLM into an exact theorem.

## 5. Why GLM Still Matters

GLM is one of the most useful examples for OCP because it shows how the framework survives after exact projection is relaxed.

It supports a more realistic branch of the program:
- sometimes exact correction is available,
- sometimes only asymptotic suppression is available,
- and the theory should clearly distinguish those cases instead of forcing them into the same claim.
