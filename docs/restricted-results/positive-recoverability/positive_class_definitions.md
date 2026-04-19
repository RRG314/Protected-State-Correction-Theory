# Positive Class Definitions

This file defines a restricted positive layer for finite-dimensional linear systems with context-indexed records.

## Scope

All classes in this file assume:
- finite-dimensional linear state space,
- explicit target map,
- explicit context-indexed observation maps,
- explicit declaration of whether shared augmentation is allowed.

Without those declarations these classes become ambiguous and should not be promoted.

## Common setup

We use:
- state `x in R^n`,
- target `tau(x) = Lx`,
- context records `y_c = M_c x` for contexts `c in {1,...,k}`,
- optional shared augmentation `Ux` appended to every context.

## C1: Compatibility-Organized Recoverable Systems (CORS)

A system is in CORS when one shared decoder `D` satisfies `D M_c = L` for every context `c`.

Equivalent criterion: `row(L)` is contained in the shared agreement row-space.

How to read this class:
- it captures exact shared recoverability,
- any positive compatibility defect means the system is outside CORS.

## C2: Augmentation-Completable Recoverability Systems (ACRS)

A system is in ACRS when baseline shared exactness may fail, but shared augmentation can restore exactness.

Free augmentation threshold:
- `r_free* = rank([G;L]) - rank(G)`.

Constrained library criterion:
- `delta_C = rank([G;C;L]) - rank([G;C])`.

Interpretation:
- `delta_C = 0` means the declared library can complete recovery,
- `delta_C > 0` means that library is insufficient.

## C3: Context-Consistent Recoverability Systems (CCRS)

A system is in CCRS when each context is locally exact and those local decoders can be replaced by one shared decoder.

Why this class matters:
- it separates local recoverability from global coherence,
- it captures the practical failure mode where each context looks solvable in isolation but no shared map exists.

## C4: Descriptor-Lift Recoverability Systems (DLRS)

DLRS is a diagnostic class, not a standalone theorem class.

It evaluates systems with a pair:
- amount descriptors,
- compatibility-lift descriptors (`CID`, `r_free*`, `delta_C` when a library is declared).

Purpose:
- detect opposite-verdict systems that amount-only descriptors miss.

## Quick example

Two systems can have the same observation rank and the same budget, but different compatibility defects. One is CORS and exact. The other needs augmentation and sits in ACRS.
