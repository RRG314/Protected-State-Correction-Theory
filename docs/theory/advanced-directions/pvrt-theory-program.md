# Protected-Variable Recoverability Theory (PVRT)

## Status

This file records the strongest honest surviving theory candidate extracted from the constrained-observation branch.

It is **not** a claim of a broad new universal theory.
It is a restricted theorem-and-falsification program built from results that survived repeated derivation, implementation, counterexample search, and cross-checking.

## 1. Candidate Theory Statement

The strongest surviving PVRT statement is:

> Recoverability of a protected variable is governed by the interaction between the observation fibers, the protected-variable map, and the admissible family. In restricted finite-dimensional linear families this interaction becomes an exact theorem program based on row-space inclusion, structured collision gaps, and minimal augmentation counts. Observation amount alone does not determine recoverability.

This is the form that survived.

Broader slogans did **not** survive:
- record amount alone determines recoverability,
- one universal threshold law governs all branches,
- one universal scalar complexity or capacity invariant exists.

## 2. Scope

PVRT currently has three different status levels.

### Broad cross-domain level
- exact statement: recoverability is fiber-compatibility between `M` and `p` on `A`
- status: real, but mostly standard or standard-adjacent

### Restricted theorem level
- exact statement: on finite-dimensional restricted linear families, exactness, stable exact-regime bounds, minimal record thresholds, and augmentation counts are governed by row-space inclusion and collision-gap structure
- status: strongest real theory-level output

### Family-level corollary level
- periodic modal thresholds
- diagonal finite-history / interpolation thresholds
- fixed-basis qubit weaker-versus-stronger protected-variable split
- status: real and useful, but family-specific

## 3. Core Objects

Let

```text
X = state space,
A ⊂ X = admissible family,
p : A → P = protected-variable map,
M : A → Y = observation or record map,
R : M(A) → P = recovery map.
```

The recoverability question is:

```text
Can M(x) determine p(x) on A?
```

The repo uses four regimes.

### Exact
There exists `R` such that

```text
R(M(x)) = p(x)    for all x ∈ A.
```

### Approximate
There exists a modulus `ω` such that

```text
d_P(R(y), p(x)) ≤ ω(d_Y(y, M(x)))
```

for the record perturbations of interest.

### Asymptotic
A history-based or observer-based reconstruction converges:

```text
d_P(R_t(M_0(x), …, M_t(x)), p(x)) → 0.
```

### Impossible
No exact recovery exists on the chosen family.

## 4. Protected Degrees Of Freedom

PVRT does **not** support one scalar notion of “degrees of freedom of `p`” across all branches.

The strongest honest statement is branch-specific.

### General level
The protected degrees of freedom are the distinctions in `p(x)` that remain meaningful on `A`.

Exact recovery requires that `M` separate those distinctions.

### Restricted linear level
For

```text
x = F z,
M(x) = O x,
p(x) = L x,
```

the protected-variable structure is carried by `L F`.

The important object is not only `rank(LF)`.
It is the row space `row(LF)` relative to `row(OF)`.

### Periodic modal level
Protected complexity is carried by the Fourier modes actually used by the protected functional.

### Diagonal control level
Protected complexity is carried by the interpolation complexity of the protected functional on the active sensor spectrum.

### Quantum toy level
Protected complexity is carried by which state-family distinctions survive the chosen record. For fixed-basis measurement, phase-sensitive distinctions survive for the full Bloch vector but not for `z`.

## 5. Central Supported Results

### PVRT-P1: Fiber-compatibility exactness
Exact recovery holds iff `p` is constant on each observation fiber.

Status:
- proved
- foundational
- almost certainly standard

### PVRT-P2: Collapse-modulus exactness

```text
κ_{M,p}(0)=0
```

iff exact recovery holds.

Status:
- proved
- foundational
- standard-adjacent

### PVRT-P3: Adversarial lower bound
For record perturbation radius `η`, every estimator satisfies

```text
worst-case protected-variable error ≥ κ_{M,p}(η)/2.
```

Status:
- proved
- strongest operational `κ` result currently supported

### PVRT-P4: Restricted-linear exactness theorem
On a restricted linear family,

```text
ker(O F) ⊂ ker(L F)
```

iff exact protected-variable recovery exists.

Equivalent form:

```text
row(L F) ⊂ row(O F).
```

Status:
- proved
- standard-adjacent linear algebra

### PVRT-P5: Restricted-linear exact-regime stability envelope
If exact recovery holds and `K` satisfies

```text
K O F = L F,
```

then for Euclidean record and protected metrics,

```text
κ_{M,p}(δ) ≤ ||K||_2 δ.
```

Status:
- proved in the restricted-linear branch
- computationally checked against exact linear examples and a control-family threshold case

Meaning:
- exact recoverability automatically yields a stable approximate upper bound inside the same restricted exact branch
- the branch now has both a lower obstruction (`κ(η)/2`) and an upper envelope (`||K||_2 δ`) in the exact linear regime

### PVRT-P6: Nested collision-gap threshold law
On the bounded coefficient box

```text
A_B = {F z : ||z||_∞ ≤ B},
```

define

```text
Γ_r(B) = sup { ||L F h|| : ||h||_∞ ≤ 2B, O_r F h = 0 }.
```

Then:
- `Γ_r(B)` is monotone nonincreasing on nested record families
- exact recovery begins exactly where `Γ_r(B)=0`
- every zero-noise estimator below threshold obeys

```text
worst-case protected-variable error ≥ Γ_r(B)/2.
```

Status:
- proved
- strongest theorem-grade threshold result currently in the branch

### PVRT-P7: Same-rank insufficiency theorem
Let `rank(LF)=r` and let the admissible linear family dimension exceed `r`.
For every observation rank `k` with

```text
r ≤ k < dim(range(F)),
```

there exist observation families of the same rank `k` such that:
- one exactly recovers `p`,
- one fails to recover `p`.

Status:
- proved in the restricted-linear setting
- useful negative result

Meaning:
- information amount alone is not enough
- alignment between observation structure and protected-variable structure matters

### PVRT-P8: Minimal augmentation theorem
If unrestricted extra linear measurements are allowed, the minimum number needed to restore exact recovery is

```text
δ(O, L; F) = rank([O F; L F]) - rank(O F).
```

Status:
- proved
- strongest practical design theorem in the branch

## 6. What PVRT Predicts

PVRT predicts the following.

1. A coarser record can remain exact for one protected variable while becoming impossible for a stronger one.
2. Exactness thresholds are controlled by branch-specific protected structure, not by one universal scalar complexity count.
3. In the restricted-linear branch, exactness, stable exact-regime bounds, and augmentation counts are all determined by the same row-space compatibility structure.
4. Record rank is only a necessary condition, not a sufficient one.

## 7. What PVRT Rules Out

PVRT rules out the following broad claims.

- record amount alone determines recoverability
- support size alone determines thresholds
- protected rank alone determines thresholds
- one cross-domain phase-transition law governs all current benchmark systems
- one universal scalar recoverability invariant governs the repo

## 8. Main Falsification Criteria

PVRT in the current restricted form would fail if any of the following appeared.

1. A restricted-linear counterexample where

```text
row(LF) ⊂ row(OF)
```

but exact recovery still fails.

2. An exact restricted-linear example where the computed exact recovery operator `K` does not satisfy

```text
κ(δ) ≤ ||K||_2 δ.
```

3. A genuine same-rank counterexample to the same-rank insufficiency theorem.

4. A cross-domain example showing that the protected-variable threshold laws are actually determined by record amount alone once the admissible family is fixed.

None of those failures survived in the current pass.

## 9. Honest Limits

PVRT does **not** currently justify the following claims.

- a broad new theory replacing observability, sufficiency, inverse stability, or quantum recoverability
- a universal recoverability law across quantum, periodic-flow, control, and PDE branches
- a major theorem program outside the restricted-linear and family-level settings

The honest status is narrower:

- real theory candidate: yes
- broad standalone universal theory: no
- strongest surviving form: restricted, theorem-backed, branch-compatible PVRT

## 10. Best Next Target

The single strongest next theorem target is:

> a robust noisy extension of the restricted-linear PVRT spine that keeps the exact-regime upper envelope, the `κ(η)/2` lower bound, and the minimal augmentation logic under admissible-family enlargement or record perturbation.

That is the next place where PVRT could become materially stronger without bluffing.
