# Constrained-Observation Recoverability Formalism

## Status

Formal branch note for the **Constrained-Observation Recoverability** lane inside **Protected-State Correction Theory**.

This document is intentionally narrower than the branch overview. It is meant to state the mathematical objects cleanly enough that theorem statements, no-go statements, and computational tests can all point to the same definitions.

## 1. Scope

The branch studies when a constrained record preserves enough information to recover a **protected variable**. The point is not to replace the repository's existing correction theorems. The point is to add an observation layer in front of them.

The central question is:

> Given a state family `A`, a protected variable `p`, and an observation map `M`, when does the record `M(x)` determine `p(x)` exactly, approximately, asymptotically, or not at all?

This is standard in spirit in several areas:

- sufficiency and approximate sufficiency,
- observability and functional observers,
- inverse-problem stability,
- restricted recovery,
- quantum recoverability.

The possible contribution here is not the existence of those literatures. The possible contribution is a disciplined protected-variable formulation tied directly to the repository's exact / asymptotic / no-go architecture.

## 2. Basic Setup

Let:

- `X` be a state space,
- `A ⊂ X` be an admissible family,
- `P` be a protected-variable space,
- `Y` be an observation space,
- `p : A → P` be the protected-variable map,
- `M : A → Y` be the observation or record map.

A recovery map is any map

```text
R : M(A) → P.
```

The branch does not assume that `M` is invertible on `A`. In fact, the interesting case is precisely when `M` is coarse.

## 3. Exact Recoverability

### Definition 3.1

The protected variable `p` is **exactly recoverable from `M` on `A`** if there exists a recovery map `R : M(A) → P` such that

```text
R(M(x)) = p(x)    for all x ∈ A.
```

### Proposition 3.2: Fiber-Separation Criterion

The following are equivalent.

1. `p` is exactly recoverable from `M` on `A`.
2. `p` is constant on every fiber of `M`, that is,

```text
M(x) = M(x')  ⇒  p(x) = p(x')
```

for all `x, x' ∈ A`.

### Proof sketch

- `1 ⇒ 2`: if `R(M(x)) = p(x)` and `M(x) = M(x')`, then

```text
p(x) = R(M(x)) = R(M(x')) = p(x').
```

- `2 ⇒ 1`: define `R(y)` by picking any `x ∈ A` such that `M(x)=y` and setting `R(y)=p(x)`. This is well-defined because `p` is constant on fibers.

### Status note

This criterion is likely standard. It is kept because it is the correct branch backbone and because all later no-go and stability statements reduce to it.

## 4. Approximate Recoverability

Let `d_Y` and `d_P` be metrics on `Y` and `P`.

### Definition 4.1

A family is **stably approximately recoverable** if there exists a function `ω : [0,∞) → [0,∞)` with `ω(0)=0` and a recovery rule `R` such that

```text
d_P(R(y), p(x)) ≤ ω(d_Y(y, M(x)))
```

for all admissible `x` and perturbed records `y` in the regime of interest.

The function `ω` is a modulus of recoverability. In inverse-problem language, this is a modulus of continuity for the protected variable through the observation map.

## 5. Collapse Modulus

### Definition 5.1

For `δ ≥ 0`, define the **collapse modulus**

```text
κ_{M,p}(δ) = sup { d_P(p(x), p(x')) : x,x' ∈ A, d_Y(M(x), M(x')) ≤ δ }.
```

This is the largest protected-variable ambiguity compatible with record discrepancy at most `δ`.

### Immediate properties

- `κ_{M,p}(δ)` is monotone nondecreasing in `δ`.
- `κ_{M,p}(δ) ≥ 0`.
- `κ_{M,p}(0)` is the exact fiber-collision quantity.

### Proposition 5.2

`p` is exactly recoverable from `M` on `A` if and only if

```text
κ_{M,p}(0) = 0.
```

### Proof sketch

By definition,

```text
κ_{M,p}(0) = sup { d_P(p(x), p(x')) : M(x)=M(x') }.
```

Since `d_P` is a metric, this supremum vanishes exactly when all equal-record pairs have equal protected value. Proposition 3.2 then gives exact recoverability.

### Interpretation

- `κ(0)=0`: exact recovery is at least logically possible.
- `κ(0)>0`: exact recovery is impossible.
- growth of `κ(δ)` for `δ>0`: measures stability loss under coarse observation or record noise.

### Status note

The metric itself is the strongest plausible candidate for a branch-specific contribution, but only if it proves useful across more than one conventional system family. The definition by itself is not enough.

## 6. Asymptotic Recoverability

The branch allows a dynamical form of recoverability.

### Definition 6.1

Suppose a system produces an observation history `M_t(x)` and an estimator or observer state `z_t`. A protected variable is **asymptotically recoverable** if there exists a reconstruction rule `R_t` such that

```text
d_P(R_t(M_0(x), …, M_t(x)), p(x)) → 0
```

as `t → ∞`.

This is the appropriate branch notion for observer-style systems and continuous measurement / feedback architectures. It is not an exact one-shot recovery claim.

## 7. Irrecoverability

### Definition 7.1

The protected variable is **irrecoverable from `M` on `A`** if no exact recovery map exists.

By Proposition 3.2 and Proposition 5.2, irrecoverability occurs whenever there exists a fiber collision, equivalently whenever

```text
κ_{M,p}(0) > 0.
```

## 8. Restricted Linear Recovery

Let `F` be a finite-dimensional linear family with coefficient space `ℝ^m`. Let

```text
x = Fz,
M(x) = O x,
p(x) = L x,
```

where `O` and `L` are linear maps.

### Proposition 8.1: Restricted Linear Criterion

There exists a linear recovery operator `K` such that

```text
K O x = L x    for all x ∈ range(F)
```

if and only if

```text
ker(O F) ⊂ ker(L F).
```

### Proof sketch

- If `K O F = L F`, then any `z` with `O F z = 0` must satisfy `L F z = K O F z = 0`.
- Conversely, if `ker(O F) ⊂ ker(L F)`, define a map on `im(O F)` by

```text
T(O F z) = L F z.
```

This is well-defined because equality of `O F z` values implies the difference lies in `ker(O F)`, hence also in `ker(L F)`. Extend `T` linearly to `K` on the ambient observation space.

### Stability margin

A useful restricted margin is

```text
α_{O,L,F} = inf { ||O F z|| / ||L F z|| : L F z ≠ 0 }.
```

If `α_{O,L,F} > 0`, then

```text
||L F z|| ≤ α_{O,L,F}^{-1} ||O F z||
```

and exact protected-variable recovery is stable on the restricted family.

### Status note

The criterion is linear-algebraically standard. It is still worth keeping because it is the cleanest precise bridge from the branch to functional observability and restricted recovery.

## 9. Record Complexity and Threshold Families

The branch also needs a disciplined way to talk about richer versus poorer records.

### Definition 9.1

Let `{M_λ}` be a parameterized family of observation maps ordered by record richness. The parameter `λ` may represent:

- retained Fourier cutoff,
- observation horizon,
- number of active sensors,
- retained basis information,
- quantization level,
- bandwidth,
- or another monotone coarsening parameter.

### Definition 9.2

For a fixed protected variable `p`, the **exact-recovery threshold set** is

```text
T_exact = { λ : p is exactly recoverable from M_λ on A }.
```

If there exists a least exact parameter `λ_*`, the branch calls it the **minimal exact record complexity** for that family.

### Definition 9.3

If `κ_{M_λ,p}(0)` changes from positive to zero at some parameter value, the branch treats that point as an **exact/no-go threshold** on the chosen family.

If no sharp jump appears but recovery errors or stability margins vary continuously, the branch classifies the family as **smooth degradation without a sharp exactness threshold**.

These notions are intentionally family-specific. The branch does not currently support a universal scalar record-complexity theory.

## 10. Divergence-Only No-Go

Let `A` be a family of divergence-free vector fields on a bounded or periodic domain, and let

```text
M(u) = ∇·u.
```

Let the protected variable be any nonconstant map `p(u)` on that family; in the strongest form one can take `p(u)=u` itself.

### Corollary 10.1

If `u, v ∈ A` are distinct divergence-free states, then

```text
M(u) = 0 = M(v)
```

while `p(u) ≠ p(v)`.

Therefore exact recovery from divergence-only data is impossible on any nontrivial divergence-free family.

### Proof

This is an immediate fiber-collision application.

### Status note

This result is elementary, but it is useful because it gives a precise statement of a recurring repository intuition: a scalar constraint record does not, by itself, determine the full protected field.

## 11. Fixed-Basis Phase-Loss No-Go

Consider pure qubit states

```text
|ψ(θ,φ)⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩.
```

Let the observation map be the fixed computational-basis measurement record

```text
M_Z(θ,φ) = (cos²(θ/2), sin²(θ/2)).
```

### Corollary 11.1

If the admissible family contains states with the same `θ` and different `φ`, then exact recovery of the full Bloch vector or the full pure state from `M_Z` is impossible.

### Proof

`M_Z` depends only on `θ`. Hence states `(θ,φ)` and `(θ,φ')` produce identical record maps but represent different protected values whenever the protected variable distinguishes phase.

### Meridian subcase

If the admissible family is restricted to a fixed meridian `φ=φ_0`, then the full Bloch vector on that restricted family is exactly recoverable from `M_Z` because `θ` is determined by the record and `φ` is fixed by the family definition.

## 12. What is Standard and What Is Being Tested

Likely standard or close to standard:

- fiber-separation / factorization for exact recoverability,
- the linear kernel criterion,
- the qubit phase-loss no-go,
- the divergence-only no-go in its bare logical form.

Being actively tested as a possible branch-level contribution:

- whether `κ_{M,p}` is a useful cross-domain organizing quantity rather than just a renamed modulus of continuity,
- whether a protected-variable exact / approximate / asymptotic / impossible classification is genuinely clearer across multiple conventional systems,
- whether the branch can produce at least one useful threshold or no-go statement that is not merely trivial restatement.
