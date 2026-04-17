# Family-Restriction Risk Report

## Why this matters

A large fraction of exact branch results are intentionally family-restricted.
That is a strength when the family is explicit and honest, but it is also the main source of false positive risk if users silently enlarge the admissible class.

## Current branch boundary

The branch is safe to treat as theorem-backed for:
- the declared restricted-linear families,
- the supported periodic modal families,
- the supported diagonal/history families,
- the explicit bounded-domain compatible family,
- the explicit qubit phase family.

It is not safe to treat as universal for:
- arbitrary larger admissible families,
- arbitrary PDE state classes,
- arbitrary sensor libraries,
- arbitrary nonlinear perturbations.

## New strongest certificate

`OCP-052` is the current sharpest family-restriction result because it shows exactly how a positive exactness claim can fail under honest enlargement.

## Practical rule

When a result is exact, the next honest question is not only “is κ(0)=0?”
It is also:
- what family was used,
- what hidden directions were excluded,
- and whether a nearby or larger family would reintroduce target-mixed fibers.
