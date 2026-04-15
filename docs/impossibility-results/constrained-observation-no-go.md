# Constrained-Observation No-Go Results

## Status

Negative-results note for the **Constrained-Observation Recoverability** branch.

The point of this file is not to collect every obvious impossibility statement. The point is to keep only the no-go results that are structurally useful for the branch.

## 1. Fiber-Collision No-Go

### COR-N1

Let `A` be an admissible family, `M : A → Y` an observation map, and `p : A → P` a protected-variable map.

If there exist `x, x' ∈ A` such that

```text
M(x)=M(x')
```

but

```text
p(x) ≠ p(x'),
```

then exact recovery of `p` from `M` on `A` is impossible.

### Reason

Any candidate recovery map `R` would have to satisfy

```text
R(M(x)) = p(x),
R(M(x')) = p(x'),
```

but `M(x)=M(x')`, so the same record would have to map to two different protected values.

### Status

Proved and foundational.

### Standardness

Standard.

## 2. Divergence-Only No-Go

### COR-N2

Let `A` be a nontrivial family of divergence-free vector fields and let the record map be

```text
M(u)=∇·u.
```

If the protected variable is nonconstant on `A`, then exact recovery from divergence-only data is impossible.

### Minimal proof

For any `u,v ∈ A`,

```text
M(u)=0=M(v).
```

If `p(u)≠p(v)`, then `COR-N1` applies.

### Why it matters

This is the cleanest observation-side analog of the repo's broader correction-side warning: a scalar constraint record cannot generally determine the full protected object.

### Status

Proved.

### Standardness

Elementary, but worth keeping because it is a recurring design mistake in constrained-flow settings.

## 3. Fixed-Basis Phase-Loss No-Go

### COR-N3

For qubit pure states

```text
|ψ(θ,φ)⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩,
```

the fixed-basis record

```text
M_Z(θ,φ) = (cos²(θ/2), sin²(θ/2))
```

cannot exactly recover any protected variable that distinguishes the phase `φ`.

### Reason

`M_Z` depends only on `θ`. Therefore all states with the same `θ` but different `φ` share the same record.

### Surviving positive subcase

If the admissible family fixes `φ`, then the same record can exactly recover the full Bloch vector on that restricted family.

### Status

Proved for the toy model.

### Standardness

Standard quantum-measurement logic.

## 4. One-Step Protected-Functional No-Go in the Control Toy Model

### COR-N4

In the scalar-output model

```text
x_{t+1}=diag(a,b)x_t,
y_t=x_{t,1}+ε x_{t,2},
p(x_0)=x_{0,2},
```

one-step exact recovery of `p(x_0)` from `y_0` is impossible for any finite `ε`, because multiple initial states share the same scalar output.

### Comment

This is not interesting by itself. It is kept only because the same model becomes exactly recoverable from a two-step record and asymptotically recoverable by an observer. That makes it a good branch benchmark.

## 5. What Not To Promote

The following directions should not be promoted as branch-defining no-go results unless they sharpen substantially.

- “Noninvertible maps are not invertible.”
- “Measurement loses information.”
- “Coarse-graining can destroy phase information.”

All of those are true, but they are too generic to count as results.

## 6. Best Current No-Go Contribution

The strongest branch-specific negative lesson at the moment is not a grand impossibility theorem. It is the combination of:

- fiber-collision as the exact logical obstruction,
- divergence-only no-go as the PDE-side obstruction,
- and the qubit phase-loss example as the quantum-side obstruction.

Together they show that the branch is really about **recoverability of a chosen protected variable**, not about full-state inversion in the abstract.
