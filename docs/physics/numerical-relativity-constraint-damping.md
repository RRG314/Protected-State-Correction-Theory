# Numerical-Relativity Constraint Damping

## Plain-Language Summary

Numerical relativity gives a good additional physics lane for the **asymptotic** side of the theory.

The protected object is the constraint-satisfying sector of the evolution system. The disturbance is the constraint-violating component. The correction architecture is not a one-shot projector; it is a damped evolution law added to the equations.

That makes this a meaningful OCP-style branch, but only on the asymptotic side.

## System Definition

In free-evolution formulations of general relativity, one evolves the main fields while requiring the constraints to remain satisfied. Constraint-violating modes are the disturbance family.

The relevant question is:

> does the modified evolution law preserve the physical sector while damping the constraint-violating modes?

## Correction Architecture

The relevant architectures add lower-order or damping terms so that the constraint subsystem decays under the flow.

In OCP language:
- protected object: constraint-satisfying states,
- disturbance: constraint-violating modes,
- correction operator: the added damping generator or constraint-preserving evolution structure.

## Exact Or Asymptotic?

This is an **asymptotic** fit.

It should not be promoted as an exact branch unless one has an actual projector or one-shot recovery map.

## What OCP Adds

OCP helps here by making two distinctions explicit:
- exact projection is different from damping or free-evolution stabilization,
- and structural failure can come either from insufficient damping or from a correction architecture that does not preserve the protected sector cleanly.

## Fit Verdict

Verdict: **keep** as a conditional asymptotic physics extension.

It is worth keeping because the operator/generator language is real and citable. It is not a new theorem branch in the repo yet.

## What To Cite

Useful outside anchors:
- [Gundlach et al., "Constraint damping in the Z4 formulation and harmonic gauge" (Class. Quantum Grav. 22, 3767, 2005)](https://arxiv.org/abs/gr-qc/0504114)
- [Weyhausen, Bernuzzi, and Hilditch, "Constraint damping for the Z4c formulation of general relativity" (Phys. Rev. D 85, 024038, 2012)](https://doi.org/10.1103/PhysRevD.85.024038)
- [Abalos, "On constraint preservation and strong hyperbolicity" (Class. Quantum Grav. 39, 215004, 2022)](https://doi.org/10.1088/1361-6382/ac88af)

## Limit

This direction stays conditional until the repo contains a sharper constraint-subsystem theorem in a genuine PDE setting rather than only linear-generator analogs.
