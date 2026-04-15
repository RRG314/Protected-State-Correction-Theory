# Constrained-Observation Theorems and Candidates

## Status

This note collects the strongest theorem-grade statements currently supported by the **Constrained-Observation Recoverability** branch.

The branch is intentionally conservative. Statements are split into:

- clean propositions that are fully supported,
- family-level theorems that survive both derivation and computation,
- and larger candidates that remain open.

The note should be read with:

- [constrained-observation-formalism.md](../theory/advanced-directions/constrained-observation-formalism.md)
- [constrained-observation-derivations.md](../theory/advanced-directions/constrained-observation-derivations.md)
- [constrained-observation-no-go.md](../impossibility-results/constrained-observation-no-go.md)
- [constrained-observation-results-report.md](../theory/advanced-directions/constrained-observation-results-report.md)

## 1. Supported General Propositions

### COR-P1: Fiber-Separation Exactness

Let `A` be an admissible family, `M : A → Y` an observation map, and `p : A → P` a protected-variable map.

Then exact recoverability of `p` from `M` on `A` holds if and only if `p` is constant on each fiber of `M`.

**Status:** proved and clean.

**Value:** foundational branch backbone.

**Standardness:** almost certainly standard in spirit.

### COR-P2: Exactness Through `κ(0)`

With the collapse modulus

```text
κ_{M,p}(δ) = sup { d_P(p(x),p(x')) : d_Y(M(x),M(x')) ≤ δ },
```

exact recoverability holds if and only if

```text
κ_{M,p}(0) = 0.
```

**Status:** proved and clean.

**Value:** the branch's correct exact / impossible separator.

**Standardness:** likely standard or standard-adjacent.

### COR-P3: Adversarial-Noise Lower Bound

Assume an estimator receives a perturbed record `y` satisfying

```text
d_Y(y, M(x)) ≤ η.
```

Then every estimator `\hat p : Y → P` obeys

```text
sup_x sup_{d_Y(y,M(x))≤η} d_P(\hat p(y), p(x)) ≥ κ_{M,p}(η) / 2.
```

**Status:** proved and cross-checked analytically and computationally.

**Value:** this is the strongest operational theorem currently supporting the `κ` branch.

**Standardness:** likely inverse-stability-adjacent, but still worth keeping because it makes `κ` do real work beyond `κ(0)=0`.

### COR-P4: Exact Restricted Linear Recovery

Let `x = Fz` range over a finite-dimensional admissible linear family and let

```text
M(x)=Ox,
p(x)=Lx.
```

Then there exists a linear recovery map `K` such that

```text
K O x = L x
```

for all admissible `x` if and only if

```text
ker(O F) ⊂ ker(L F).
```

**Status:** proved and implemented.

**Value:** cleanest exact bridge to restricted observability and signal recovery.

**Standardness:** almost certainly standard linear algebra.

### COR-P5: Restricted Observation Rank Lower Bound

Under the same setup,

```text
rank(O F) ≥ rank(L F)
```

is necessary for exact protected-variable recovery.

**Status:** proved and tested.

**Value:** honest minimum-record lower bound.

**Standardness:** standard linear algebra.

## 2. Supported Family-Level Threshold Theorems

### COR-T1: Qubit Phase-Window Collision Law

For the fixed-basis qubit record on the phase-window family `φ ∈ [-w,w]`, the full Bloch-vector ambiguity satisfies

```text
κ_{M_Z,p}(0) = 2 sin(min(w, π/2)).
```

Consequences:

- exact full-Bloch recovery holds only at `w=0`,
- exact recovery of the weaker protected variable `z` survives on the full sampled phase-window family.

**Status:** proved for the toy family and checked numerically under refined sampling.

**Value:** cleanest quantum-side threshold law in the branch.

**Standardness:** likely standard in spirit, but a good benchmark-quality result.

### COR-T2: Periodic Modal Minimal-Cutoff Theorem

Consider the finite periodic incompressible modal family

```text
ω = \sum_{j=1}^m c_j ω_j,
```

where each mode `ω_j` is supported at a Fourier cutoff level `q_j`, and let the protected variable be any selected subset of the modal coefficients.

For truncated-vorticity observation at cutoff `Q`, exact recovery of the chosen protected coefficients is possible if and only if

```text
Q ≥ max { q_j : c_j \text{ appears in the protected variable} }.
```

In the implemented three-mode family this yields the exact thresholds:

- `mode_1_coefficient`: threshold `1`
- `modes_1_2_coefficients`: threshold `2`
- `full_modal_coefficients`: threshold `3`

**Status:** proved for the finite modal family and checked across discretizations.

**Value:** strongest surviving minimal-record threshold law in the periodic-flow lane.

**Standardness:** family-specific and not a general CFD theorem.

### COR-T3: Diagonal Minimal-History Theorem

Consider the scalar-output diagonal family

```text
x_{t+1} = diag(λ_1, …, λ_n) x_t,
y_t = \sum_{j=1}^n c_j x_{t,j},
p(x_0) = x_{0,k},
```

with distinct active eigenvalues among the indices for which `c_j ≠ 0`.

Let `m` be the number of active sensor modes.

Then:

1. if `c_k = 0`, exact recovery of `x_{0,k}` is impossible for every finite horizon;
2. if `c_k ≠ 0`, exact recovery is impossible for horizons `H < m`;
3. if `c_k ≠ 0`, exact recovery is possible at horizon `H = m`, and hence for every `H ≥ m`, by an explicit interpolation formula.

In the implemented three-state family this yields:

- `three_active`: exact threshold `H = 3`
- `two_active`: exact threshold `H = 2`
- `protected_hidden`: impossible for all tested horizons

**Status:** proved for the family, with explicit reconstruction weights and computational cross-checks.

**Value:** cleanest minimal-history threshold law in the control lane.

**Standardness:** very likely standard or Vandermonde-interpolation-adjacent, but still a real, usable branch theorem.

### COR-P6: Two-Step Scalar-Output Recovery Formula

For the two-state model

```text
x_{t+1} = diag(a,b)x_t,
y_t = x_{t,1} + ε x_{t,2},
p(x_0)=x_{0,2},
```

if `ε(a-b) ≠ 0`, then

```text
x_{0,2} = (a y_0 - y_1) / (ε(a-b)).
```

If `ε=0` or `a=b`, exact two-step recovery fails.

**Status:** proved and checked independently against the pseudoinverse-based recovery operator.

**Value:** useful concrete anchor for one-step failure versus finite-history exactness.

**Standardness:** very likely standard.

## 3. Supported No-Go Statements Kept Near Theorem Level

### COR-N1: Fixed-Basis Phase-Loss No-Go

A fixed computational-basis record cannot exactly recover a phase-sensitive protected variable on a qubit family that contains the same amplitudes with varying phase, even though weaker protected variables such as the `z` coordinate remain recoverable.

**Status:** proved for the toy family.

### COR-N2: Divergence-Only Protected-Variable No-Go

On any nontrivial divergence-free family, a recovery architecture that factors only through the divergence record cannot exactly recover a nonconstant protected variable.

**Status:** proved in the cleanest branch form.

### COR-N3: Hidden-Mode Finite-History No-Go

In the diagonal scalar-output family, if the protected coordinate has zero sensor coupling, then no finite observation horizon recovers it exactly.

**Status:** proved for the family and checked computationally.

## 4. What Is Real Versus What Is Still Open

### Clean and worth keeping

- `COR-P2` exactness through `κ(0)`
- `COR-P3` adversarial lower bound `κ(η)/2`
- `COR-P4` restricted linear exactness criterion
- `COR-T2` periodic modal minimal-cutoff theorem on the implemented family
- `COR-T3` diagonal minimal-history theorem on the implemented family

### Useful but standard-adjacent

- fiber separation
- linear kernel inclusion
- two-step two-state recovery formula
- fixed-basis phase-loss logic

### Still open / not yet strong enough

- a genuinely nontrivial cross-domain threshold theorem beyond the family-specific examples
- a theorem turning `κ_{M,p}` into more than a clean exactness-and-robustness organizer
- a sharper minimal-record complexity theory that is not just family-specific linear algebra

## 5. Best Current Next Targets

1. Strengthen `κ` beyond `κ(0)=0` and `κ(η)/2`.
2. Test whether the periodic and diagonal threshold laws admit one real common theorem schema.
3. Prefer a stronger no-go theorem over a vague cross-domain “phase transition” slogan.
