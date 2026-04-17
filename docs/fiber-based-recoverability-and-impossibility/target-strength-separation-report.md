# Target-Strength Separation Report

## Main point

The branch does not treat “recovery” as one binary notion.
It distinguishes:
- exact recovery of the selected target,
- exact recovery of a weaker/coarsened target,
- asymptotic recovery under continuing observation,
- and impossibility for the stronger target.

## Strongest theorem package

### `OCP-048`
A coarsened target can be exactly identifiable even when the stronger target is not.

### `OCP-051`
On the canonical restricted-linear class, the weaker target keeps the noise upper bound `||K||_2 η` while the stronger target keeps the impossibility floor `Γ/2`.

## Outside inverse-problem reading

This is target-specific identifiability.
The same data may support:
- one exactly identifiable functional,
- one only detectable/coarsened functional,
- and no exact recovery of the stronger target.

## Why this matters

False positives often happen when a successful weaker target is quietly narrated as if the stronger target were also recovered.
The branch now treats that as a structural error, not a wording preference.
