# Constrained-Observation Clean Results

## Purpose

This note isolates the branch results that survived repeated derivation, implementation, parameter variation, and validation.

It is the short clean-results spine for the branch.

## 1. Clean Formal Results

### CR-1: Exact Recoverability Through Fiber Separation

Exact recoverability holds if and only if the protected variable is constant on observation fibers.

Status:
- proved
- standard / foundational

### CR-2: Collapse-Modulus Exactness Criterion

```text
κ_{M,p}(0)=0
```

if and only if exact recoverability holds.

Status:
- proved
- standard-adjacent but central to the branch

### CR-3: Adversarial Lower Bound

For observation perturbation radius `η`, every estimator satisfies

```text
worst-case protected-variable error ≥ κ_{M,p}(η)/2.
```

Status:
- proved
- strongest operational theorem in the branch

### CR-4: Restricted Linear Recovery Criterion

On a finite-dimensional linear family `x=Fz`, exact linear protected-variable recovery is possible if and only if

```text
ker(O F) ⊂ ker(L F).
```

Status:
- proved
- standard linear algebra, but a clean bridge result

### CR-5: Restricted Observation Rank Lower Bound

Exact protected-variable recovery implies

```text
rank(O F) ≥ rank(L F).
```

Status:
- proved
- useful minimum-record lower bound

### CR-6: Nested Minimal-Complexity Criterion

For a nested finite-dimensional linear observation family, minimal exact record complexity is the first level where the protected row enters the observation row space.

Status:
- proved
- standard-adjacent but genuinely useful

### CR-7: Same-Record Variable Hierarchy

The same coarse record can exactly recover a weaker protected variable while exact recovery of a stronger one remains impossible.

Status:
- proved
- useful negative result

### CR-7b: Minimal Augmentation In The Restricted Linear Design Layer

On the finite-dimensional restricted linear families used in the design layer, exact recovery can be restored by adding the smallest candidate measurement set whose rows place every protected row inside the augmented record row space.

Status:
- proved in the restricted linear template setting
- standard-adjacent but practically useful

## 2. Clean No-Go Results

### CR-8: Divergence-Only No-Go

A divergence-only record cannot exactly recover a nonconstant protected variable on a nontrivial divergence-free family.

Status:
- proved
- useful negative result

### CR-9: Fixed-Basis Phase-Loss No-Go

A fixed-basis qubit record cannot exactly recover a phase-sensitive protected variable on a family with phase freedom.

Status:
- proved
- useful quantum-side no-go

### CR-10: Hidden-Mode No-Go

In the diagonal scalar-output family, if the protected functional has nonzero weight on a sensor-hidden coordinate, no finite observation horizon recovers it exactly.

Status:
- proved on the family
- useful control-side no-go

## 3. Clean Threshold Results

### CR-11: Qubit Phase-Window Law

For the fixed-basis qubit family with phase window `[-w,w]`, the full Bloch-vector ambiguity satisfies

```text
κ(0)=2 sin(min(w, π/2)).
```

Consequences:
- exact full recovery only at `w=0`
- exact `z` recovery across the sampled phase-window range

Status:
- proved on the family
- benchmark-grade, not a novelty claim

### CR-12: Periodic Two-Mode Cutoff Threshold

On the tested two-mode periodic incompressible family, exact recovery of the full velocity field from truncated vorticity occurs if and only if both active modes are retained.

First exact cutoff in the implemented normalization:
- `Q=2`

Status:
- proved on the family
- clean coarsening threshold

### CR-13: Periodic Functional Support Threshold

On the tested four-mode periodic modal family, the minimal exact cutoff equals the largest retained cutoff index among the Fourier modes used by the protected variable.

Implemented thresholds:
- first coefficient only: `1`
- first two coefficients: `2`
- low-mode sum: `2`
- bandlimited contrast: `3`
- full weighted sum: `4`
- full coefficient vector: `4`

Status:
- proved on the family
- strongest current minimal-record result in the periodic lane

### CR-14: Diagonal Functional Interpolation Threshold

On the tested diagonal scalar-output family with distinct active eigenvalues, the minimal exact observation horizon is the smallest history length whose observation rows interpolate the chosen protected functional on the active sensor spectrum.

Implemented thresholds:
- `three_active`:
  - `sensor_sum`: `1`
  - `first_moment`: `2`
  - `second_moment`: `3`
  - `protected_coordinate`: `3`
- `two_active`:
  - `sensor_sum`: `1`
  - `first_moment`: `2`
  - `second_moment`: `2`
  - `protected_coordinate`: `2`
- `protected_hidden`:
  - `sensor_sum`: `1`
  - `first_moment`: `2`
  - `second_moment`: `2`
  - `protected_coordinate`: impossible for all finite horizons

Status:
- proved on the family
- strongest current minimal-record result in the control lane

### CR-15: Coordinate Threshold As A Special Case

The older coordinate-recovery rule is still true on the diagonal family, but only as a special case of the functional interpolation law.

Status:
- proved
- demoted from headline to corollary

## 4. What To Promote Publicly

Promote carefully:
- the exact / approximate / asymptotic / impossible protected-variable classification
- the operational lower bound `κ(η)/2`
- the divergence-only and phase-loss no-go structure
- the restricted-linear minimal-complexity criterion
- the restricted-linear minimal-augmentation design logic
- the periodic and diagonal family-level threshold laws
- the weaker-versus-stronger split under the same coarse record

Do not promote as major new theory:
- fiber separation by itself
- `κ(0)=0` by itself
- broad “phase transition” language without family qualifiers

## 5. Current Honest Summary

The branch now has real clean results.

They are best described as:
- a useful formal and computational lane,
- with honest no-go structure,
- with narrow but real minimal-record threshold families,
- and with a clean same-record hierarchy split that survives in more than one conventional system lane.
