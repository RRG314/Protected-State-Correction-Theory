# Plain-Language Overview

The Orthogonal Correction Principle is about a simple question:

> When can we correct a system without damaging the part we are trying to preserve?

The answer is not just “when we have a correction term.” It depends on structure.

## The Core Picture

Imagine a state is made of two parts:
- the part you want to keep,
- and the part you want to remove.

If those two parts can be separated cleanly, then a correction rule can act on the unwanted part and leave the protected part untouched.

If they cannot be separated cleanly, then correction is either impossible, ambiguous, or only approximate.

## Why “Orthogonal” Matters

In the cleanest exact cases, the protected part and the disturbance part are orthogonal or at least directly decomposable. That means:
- the protected part can be projected out exactly,
- the disturbance part can be identified exactly,
- and the correction does not have to guess.

That is why QEC and Helmholtz projection matter so much here. They are not just metaphors. They are cases where correction is backed by an actual decomposition operator.

## The Three Main Branches

### 1. Exact correction
This is the strongest case. Recovery is exact in one step once the right syndrome, projector, or recovery operator is applied.

### 2. Asymptotic correction
This is weaker but still real. The disturbance is not removed in one shot, but it is driven toward zero over time while the protected part remains stable.

### 3. Impossible correction
Sometimes the protected and disturbance parts are not distinguishable. Sometimes the correction operator is too weak. Sometimes the architecture corrupts the thing it is supposed to preserve. In those cases, a no-go result is more useful than a forced positive theory.
