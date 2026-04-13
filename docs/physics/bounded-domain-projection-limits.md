# Bounded-Domain Projection Limits

## Plain-Language Summary

This file records one of the most useful physics-side negative results in the repository.

The periodic exact projector is a real exact correction operator on the periodic branch. But that does **not** mean it can be transplanted unchanged into bounded-domain physical problems.

## The Rejected Claim

Rejected claim:

> the periodic exact projector can be reused unchanged as an exact bounded-domain correction operator.

This claim is **disproved** in the repository by explicit counterexample.

## Counterexample Structure

The bounded-domain protected class is taken to be divergence-free fields with the intended boundary-normal condition.

We construct:
- a physical bounded-domain field from a stream function, so its boundary-normal trace is essentially zero,
- a nonperiodic gradient contamination,
- and then apply the periodic FFT-based projector anyway.

What happens:
- the periodic projector drives the divergence norm essentially to machine precision,
- but the projected field picks up a nonzero boundary-normal trace,
- so it is not an exact correction operator for the bounded-domain protected class.

## Validated Numbers

The current counterexample test gives, at `n = 32`:
- physical boundary-normal RMS: about `2.30e-32`
- projected boundary-normal RMS after the periodic projector: about `3.11e-2`
- post-projection divergence RMS: about `5e-15`

So the operator still fixes the periodic divergence constraint, but fails the bounded-domain protected-state requirement.

## Why This Matters

This is precisely the kind of physics boundary the theory needs.

It shows that:
- exactness is domain-dependent,
- removing one residual is not enough if the protected class includes boundary structure,
- and naive projector transplantation is not an honest physical extension.

## Fit Verdict

Verdict: **keep as a rejected bridge / no-go-style counterexample**.

This is one of the strongest outcomes of the physics extension pass because it sharpens the scope of the exact continuous branch.

## Relevant Literature

Useful outside anchors:
- [Abalos, "On constraint preservation and strong hyperbolicity" (Class. Quantum Grav. 39, 215004, 2022)](https://doi.org/10.1088/1361-6382/ac88af)
- [Calabrese, "A remedy for constraint growth in numerical relativity: the Maxwell case" (Class. Quantum Grav. 21, 5735, 2005)](https://arxiv.org/abs/gr-qc/0404036)
- [Chorin, "Numerical solution of the Navier-Stokes equations" (Math. Comp. 22, 745, 1968)](https://doi.org/10.1090/S0025-5718-1968-0242392-2)

## Status

Status in the claim registry: `DISPROVED` for the transplant claim.
