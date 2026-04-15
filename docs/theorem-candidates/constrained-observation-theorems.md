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

### COR-P6: Nested Linear Minimal-Complexity Criterion

Let `x = Fz` range over a finite-dimensional admissible linear family, let the protected variable be `p(x)=Lx`, and let observation levels be a nested family

```text
M_r(x)=O_r x
```

with

```text
row(O_1 F) ⊂ row(O_2 F) ⊂ ··· ⊂ row(O_R F).
```

Then exact protected-variable recovery at level `r` holds if and only if

```text
row(L F) ⊂ row(O_r F).
```

Consequently the minimal exact record complexity is

```text
r_* = min { r : row(L F) ⊂ row(O_r F) }.
```

**Status:** proved and implemented.

**Value:** strongest current generalization of the family-level threshold results.

**Standardness:** standard-adjacent linear algebra, but very useful for the branch.

### COR-P7: Same-Record Variable Hierarchy

Under the same setup, let two protected variables be

```text
p_1(x)=L_1 x,
p_2(x)=L_2 x.
```

If

```text
row(L_1 F) ⊂ row(O_r F)
```

but

```text
row(L_2 F) ⊄ row(O_r F),
```

then the same record level `r` exactly recovers `p_1` while exact recovery of `p_2` is impossible.

**Status:** proved and checked in both the periodic and diagonal control lanes.

**Value:** strongest clean weaker-versus-stronger split under a fixed coarse record.

**Standardness:** standard-adjacent, but one of the branch’s most useful organizing facts.

### COR-P8: Exact-Regime Stability Envelope

Let the restricted-linear setup be

```text
x = F z,
M(x) = O x,
p(x) = L x.
```

Assume exact recovery holds and let `K` satisfy

```text
K O F = L F.
```

Then for Euclidean record and protected metrics,

```text
κ_{M,p}(δ) ≤ ||K||_2 δ.
```

**Status:** proved and cross-checked on exact linear and control-threshold examples.

**Value:** strongest current upper bound attached to `κ`.

**Standardness:** standard-adjacent linear analysis.

### COR-P9: Same-Rank Insufficiency

Let `rank(L F)=r` and assume the restricted family dimension exceeds `r`.
Then for every observation rank `k` with

```text
r ≤ k < dim(range(F)),
```

there exist same-rank record families with opposite recoverability verdicts:
- one exact,
- one impossible.

**Status:** proved in the restricted-linear setting and stress-tested across dimensions.

**Value:** strongest negative theorem directly supporting the claim that recoverability depends on interaction, not only on information amount.

**Standardness:** standard-adjacent, but useful.

### COR-P10: Nested Restricted-Linear Collision-Gap Threshold Law

Let the admissible family be the coefficient box

```text
A_B = { F z : ||z||_∞ ≤ B }
```

with `B > 0`, let the protected variable be `p(x)=Lx`, and let the record family be nested observations

```text
M_r(x)=O_r x
```

with

```text
row(O_1 F) ⊂ row(O_2 F) ⊂ ··· ⊂ row(O_R F).
```

Define the structured collision gap

```text
Γ_r(B) = sup { ||L F h|| : ||h||_∞ ≤ 2B, O_r F h = 0 }.
```

Then:

1. `Γ_r(B)` is nonincreasing in `r`;
2. exact protected-variable recovery at level `r` holds if and only if `Γ_r(B)=0`;
3. the minimal exact record complexity is

```text
r_* = min { r : Γ_r(B)=0 } = min { r : row(L F) ⊂ row(O_r F) };
```

4. every estimator fed exact records from `A_B` obeys the zero-noise lower bound

```text
sup_{x ∈ A_B} d_P(\hat p(M_r(x)), p(x)) ≥ Γ_r(B) / 2.
```

**Status:** proved and implemented.

**Value:** strongest surviving threshold/no-go theorem in the branch.

**Standardness:** standard-adjacent convex linear algebra, but still the cleanest honest generalization currently supported.

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

### COR-T2: Periodic Functional Support Threshold

Consider the finite periodic incompressible modal family

```text
ω = \sum_{j=1}^m c_j ω_j,
```

where each mode `ω_j` is supported at a Fourier cutoff level `q_j`, and let the protected variable be any linear functional

```text
p(c)=a \cdot c
```

or any finite list of such functionals.

For truncated-vorticity observation at cutoff `Q`, exact recovery of the chosen protected variable is possible if and only if

```text
Q ≥ max { q_j : a_j ≠ 0 }.
```

Equivalently: exact recovery turns on exactly when the record retains every modal coefficient used by the protected variable.

In the implemented four-mode family this yields the exact thresholds:

- `mode_1_coefficient`: threshold `1`
- `modes_1_2_coefficients`: threshold `2`
- `low_mode_sum`: threshold `2`
- `bandlimited_contrast`: threshold `3`
- `full_weighted_sum`: threshold `4`
- `full_modal_coefficients`: threshold `4`

**Status:** proved for the finite modal family and checked across discretizations.

**Value:** strongest surviving minimal-record threshold law in the periodic-flow lane.

**Standardness:** family-specific and not a general CFD theorem.

### COR-T3: Diagonal Functional Interpolation Theorem

Consider the scalar-output diagonal family

```text
x_{t+1} = diag(λ_1, …, λ_n) x_t,
y_t = \sum_{j=1}^n c_j x_{t,j},
p(x_0) = g \cdot x_0,
```

with distinct active eigenvalues among the indices for which `c_j ≠ 0`.

Define the active index set

```text
J = { j : c_j ≠ 0 }.
```

Then exact recovery from the first `H` observations holds if and only if there exists a polynomial `P` of degree at most `H-1` such that

```text
g_j = c_j P(λ_j)    for every j ∈ J,
```

and

```text
g_j = 0    for every j ∉ J.
```

Consequences:

1. hidden protected directions with `g_j ≠ 0` and `c_j = 0` are impossible for every finite horizon;
2. weaker functionals such as constants or low-degree moments can be recovered at shorter horizons;
3. coordinate recovery is the special case obtained by interpolating a Kronecker delta on the active eigenvalues.

In the implemented three-state family this yields:

- `three_active`:
  - `sensor_sum`: threshold `1`
  - `first_moment`: threshold `2`
  - `second_moment`: threshold `3`
  - `protected_coordinate`: threshold `3`
- `two_active`:
  - `sensor_sum`: threshold `1`
  - `first_moment`: threshold `2`
  - `second_moment`: threshold `2`
  - `protected_coordinate`: threshold `2`
- `protected_hidden`:
  - `sensor_sum`: threshold `1`
  - `first_moment`: threshold `2`
  - `second_moment`: threshold `2`
  - `protected_coordinate`: impossible for all finite horizons

**Status:** proved for the family, with explicit reconstruction weights and computational cross-checks.

**Value:** cleanest minimal-history threshold law in the control lane.

**Standardness:** very likely standard or Vandermonde-interpolation-adjacent, but still a real, usable branch theorem.

### COR-C1: Coordinate-Recovery Corollary

Under the assumptions of `COR-T3`, if the protected variable is a visible coordinate

```text
p(x_0)=x_{0,k}
```

with `k ∈ J`, then the minimal exact history length is `|J|`; if `k ∉ J`, exact recovery is impossible for every finite horizon.

**Status:** proved as a special case of `COR-T3`.

**Value:** still useful, but no longer the most general control-side threshold statement.

**Standardness:** standard-adjacent.

### COR-P8: Two-Step Scalar-Output Recovery Formula

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

In the diagonal scalar-output family, if the protected functional has nonzero weight on a sensor-hidden coordinate, then no finite observation horizon recovers it exactly.

**Status:** proved for the family and checked computationally.

## 4. What Is Real Versus What Is Still Open

### Clean and worth keeping

- `COR-P2` exactness through `κ(0)`
- `COR-P3` adversarial lower bound `κ(η)/2`
- `COR-P4` restricted linear exactness criterion
- `COR-P6` nested linear minimal-complexity criterion
- `COR-P9` nested restricted-linear collision-gap threshold law
- `COR-P7` same-record variable hierarchy
- `COR-T2` periodic functional-support threshold on the implemented family
- `COR-T3` diagonal functional-interpolation theorem on the implemented family

### Useful but standard-adjacent

- fiber separation
- linear kernel inclusion
- two-step two-state recovery formula
- fixed-basis phase-loss logic
- the broad restricted-linear theorem spine itself

### Still open / not yet strong enough

- a genuinely nontrivial cross-domain threshold theorem beyond the family-specific examples
- a theorem turning `κ_{M,p}` into more than a clean exactness-and-robustness organizer outside the restricted-linear threshold setting
- a sharper minimal-record complexity theory that is not just family-specific linear algebra

## 5. Best Current Next Targets

1. Push `COR-P9` into a robust noisy-record theorem under admissible-family enlargement.
2. Strengthen `κ` beyond `κ(0)=0`, `κ(η)/2`, and the restricted-linear `Γ_r(B)` law.
3. Prefer a stronger no-go theorem over a vague cross-domain “phase transition” slogan.
