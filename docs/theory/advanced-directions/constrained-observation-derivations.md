# Constrained-Observation Recoverability Derivations

## Status

This note records the strongest derivations currently supporting the **Constrained-Observation Recoverability** branch.

It is meant to be read together with:

- [constrained-observation-recoverability.md](constrained-observation-recoverability.md)
- [constrained-observation-formalism.md](constrained-observation-formalism.md)
- [constrained-observation-theorems.md](../../theorem-candidates/constrained-observation-theorems.md)
- [constrained-observation-no-go.md](../../impossibility-results/constrained-observation-no-go.md)
- [constrained-observation-results-report.md](constrained-observation-results-report.md)

The branch goal here is narrow:

> determine when a coarse record preserves enough structure to recover a protected variable exactly, approximately, asymptotically, or not at all.

The note is deliberately conservative. Several statements below are clean but likely standard in spirit. They remain because they support the computational tests and define the branch's honest scope.

## 1. Core Setup

Let

```text
X  = state space,
A ⊂ X = admissible family,
p : A → P = protected-variable map,
M : A → Y = observation map.
```

A recovery map is any map

```text
R : M(A) → P.
```

Exact recoverability means

```text
R(M(x)) = p(x)    for all x ∈ A.
```

The branch obstruction is a **fiber collision**:

```text
M(x) = M(x')  but  p(x) ≠ p(x').
```

## 2. Exact Recoverability and Fiber Separation

### Proposition 2.1

Exact recoverability of `p` from `M` on `A` holds if and only if `p` is constant on each fiber of `M`.

### Derivation

If exact recoverability holds, then for `M(x)=M(x')` we have

```text
p(x) = R(M(x)) = R(M(x')) = p(x').
```

Conversely, if `p` is constant on every fiber, define `R(y)` by choosing any `x ∈ A` with `M(x)=y` and setting `R(y)=p(x)`. The fiber-constancy assumption makes this well-defined.

### Status

Almost certainly standard. Still the correct exact branch backbone.

## 3. Collapse Modulus and Exactness

Define the collapse modulus

```text
κ_{M,p}(δ) = sup { d_P(p(x), p(x')) : d_Y(M(x), M(x')) ≤ δ }.
```

### Immediate properties

For any metrics `(Y,d_Y)` and `(P,d_P)`:

```text
κ_{M,p}(δ) ≥ 0,
κ_{M,p}(δ₁) ≤ κ_{M,p}(δ₂)    if δ₁ ≤ δ₂.
```

### Proposition 3.1

```text
κ_{M,p}(0) = 0
```

if and only if exact recoverability holds.

### Derivation

At `δ=0`,

```text
κ_{M,p}(0) = sup { d_P(p(x), p(x')) : M(x)=M(x') }.
```

Because `d_P` is a metric, this supremum vanishes exactly when `p(x)=p(x')` on every observation fiber, which is Proposition 2.1.

### Status

Clean and fully supported, but likely standard.

## 4. Operational Meaning of `κ`: Adversarial Lower Bound

Assume the estimator receives a noisy record `y` with

```text
d_Y(y, M(x)) ≤ η.
```

### Proposition 4.1

For any estimator `\widehat p : Y → P`, the worst-case protected-variable error satisfies

```text
sup_{x ∈ A} sup_{d_Y(y,M(x))≤η} d_P(\widehat p(y), p(x))  ≥  κ_{M,p}(η) / 2.
```

### Derivation

Take any `x,x' ∈ A` with

```text
d_Y(M(x), M(x')) ≤ η.
```

Choose the admissible noisy record `y = M(x')`. Then `y` is compatible with

- state `x'` with zero noise,
- state `x` with observation perturbation at most `η`.

Any single estimate `\widehat p(y)` must therefore approximate both `p(x)` and `p(x')`. By the triangle inequality,

```text
max(d_P(\widehat p(y), p(x)), d_P(\widehat p(y), p(x'))) ≥ d_P(p(x), p(x')) / 2.
```

Taking the supremum over all such pairs yields the bound.

### Interpretation

This is the strongest current reason to keep `κ` in the branch:

- `κ(0)` controls exactness,
- `κ(η)/2` gives a minimax obstruction under record perturbations of size `η`.

### Cross-checking

This statement was checked three ways in the branch:

1. direct derivation from the triangle inequality,
2. closed-form analytic benchmark `M_ε(u,v)=(u, εv)`,
3. generated numeric lower-bound curves in `analytic_noise_lower_bound.csv`.

## 5. Restricted Linear Recovery Criterion

Let the admissible family be a finite-dimensional linear family

```text
x = F z,
```

and let

```text
M(x) = O x,
p(x) = L x.
```

Then on coefficient space the problem reduces to

```text
record = O F z,
protected = L F z.
```

### Proposition 5.1

There exists a linear recovery map `K` with

```text
K O x = L x    for all x ∈ range(F)
```

if and only if

```text
ker(O F) ⊂ ker(L F).
```

### Derivation

If `K O F = L F`, then for any `z ∈ ker(O F)`,

```text
L F z = K O F z = 0.
```

So `ker(O F) ⊂ ker(L F)`.

Conversely, if the kernel inclusion holds, define a map on `im(O F)` by

```text
T(O F z) = L F z.
```

This is well-defined: if `O F z = O F z'`, then `O F(z-z')=0`, hence `L F(z-z')=0`, so `L F z = L F z'`. Extend `T` linearly to the ambient record space and call the extension `K`.

### Corollary 5.2

If exact recovery holds, then

```text
rank(O F) ≥ rank(L F).
```

### Derivation

From kernel inclusion,

```text
nullity(O F) ≤ nullity(L F),
```

so rank-nullity gives the rank lower bound.

### Proposition 5.3: Nested Minimal-Complexity Criterion

Let `(O_r)_r` be a nested observation family satisfying

```text
row(O_1 F) ⊂ row(O_2 F) ⊂ ··· ⊂ row(O_R F).
```

Then exact recovery of `Lx` from `O_r x` holds if and only if

```text
row(L F) ⊂ row(O_r F).
```

Consequently the minimal exact record complexity is

```text
r_* = min { r : row(L F) ⊂ row(O_r F) }.
```

### Derivation

By Proposition 5.1, exact recovery at level `r` holds if and only if

```text
ker(O_r F) ⊂ ker(L F).
```

For finite-dimensional matrices this kernel inclusion is equivalent to row-space inclusion

```text
row(L F) ⊂ row(O_r F).
```

The minimal exact level is therefore the first `r` at which the protected row enters the observation row space.

### Consequence

This is the cleanest general statement currently supporting the periodic and diagonal threshold laws. It is standard-adjacent linear algebra, but it is the branch’s strongest honest generalization.

### Proposition 5.4: Same-Record Variable Hierarchy

If a fixed record level `r` satisfies

```text
row(L_1 F) ⊂ row(O_r F)
```

but

```text
row(L_2 F) ⊄ row(O_r F),
```

then `L_1 x` is exactly recoverable while `L_2 x` is not.

### Derivation

Apply Proposition 5.3 separately to `L_1` and `L_2`.

### Proposition 5.5: Exact-Regime Stability Envelope

Assume exact recovery holds and choose any linear operator `K` satisfying

```text
K O F = L F.
```

Then for Euclidean record and protected metrics,

```text
κ_{M,p}(δ) ≤ ||K||_2 δ.
```

### Derivation

Take any two admissible coefficient vectors `z,z'`. Then

```text
L F(z-z') = K O F(z-z').
```

Hence

```text
||L F(z-z')|| ≤ ||K||_2 ||O F(z-z')||.
```

Now take the supremum over all pairs with record discrepancy at most `δ`.

### Why this matters

This gives the strongest current upper bound attached to the branch’s collapse modulus.
The exact restricted-linear branch is therefore not just exact; it is quantitatively stable under record perturbation with a computable linear envelope.

### Proposition 5.6: Same-Rank Insufficiency

Let `rank(LF)=r` and assume the restricted family dimension is larger than `r`.
For any observation rank `k` with

```text
r ≤ k < dim(range(F)),
```

there exist observation matrices `O_exact` and `O_fail` such that

```text
rank(O_exact F) = rank(O_fail F) = k,
```

but exact recovery holds for `O_exact` and fails for `O_fail`.

### Derivation

Choose coordinates on the family so that

```text
L F = [I_r  0].
```

Then:

- choose a `k`-dimensional row space containing `row(LF)` to get `O_exact`,
- choose a `k`-dimensional row space omitting at least one protected row direction to get `O_fail`.

Because `k < dim(range(F))`, both choices exist.
By Proposition 5.3, the first case is exact and the second is not.

### Consequence

This kills the broad “record amount alone determines recoverability” shortcut even inside the best-behaved restricted-linear branch.

### Proposition 5.7: Nested Restricted-Linear Collision-Gap Threshold Law

Fix `B > 0` and consider the admissible coefficient box

```text
A_B = { F z : ||z||_∞ ≤ B }.
```

For a nested record family `M_r(x)=O_r x`, define the structured collision gap

```text
Γ_r(B) = sup { ||L F h|| : ||h||_∞ ≤ 2B, O_r F h = 0 }.
```

Then:

1. `Γ_r(B)` is nonincreasing in `r`;
2. exact recovery at level `r` holds if and only if `Γ_r(B)=0`;
3. the minimal exact complexity is

```text
r_* = min { r : Γ_r(B)=0 } = min { r : row(L F) ⊂ row(O_r F) };
```

4. any estimator fed exact records from `A_B` satisfies the zero-noise lower bound

```text
sup_{x ∈ A_B} d_P(\widehat p(M_r(x)), p(x)) ≥ Γ_r(B) / 2.
```

### Derivation

**Monotonicity.**

Nested row-space inclusion is equivalent to reverse kernel inclusion:

```text
ker(O_{r+1} F) ⊂ ker(O_r F).
```

So the feasible set defining `Γ_{r+1}(B)` is a subset of the feasible set defining `Γ_r(B)`, and therefore

```text
Γ_{r+1}(B) ≤ Γ_r(B).
```

**Exactness implies `Γ_r(B)=0`.**

If exact recovery holds, Proposition 5.1 gives

```text
ker(O_r F) ⊂ ker(L F).
```

Hence every feasible `h` in the definition of `Γ_r(B)` also satisfies `L F h = 0`, so the supremum vanishes.

**`Γ_r(B)=0` implies exactness.**

Assume `Γ_r(B)=0`. Let `h` be any vector in `ker(O_r F)`. If `h=0`, there is nothing to prove. If `h ≠ 0`, choose

```text
t = min(1, 2B / ||h||_∞).
```

Then `t h ∈ ker(O_r F)` and `||t h||_∞ ≤ 2B`, so `t h` is feasible for `Γ_r(B)`. The assumption `Γ_r(B)=0` gives

```text
L F (t h) = 0.
```

Since `t > 0`, homogeneity implies `L F h = 0`. Therefore

```text
ker(O_r F) ⊂ ker(L F),
```

and Proposition 5.1 yields exact recovery.

**Minimal-complexity identity.**

The previous equivalence shows

```text
Γ_r(B)=0    if and only if    row(L F) ⊂ row(O_r F),
```

so the first exact level is exactly the first zero-gap level.

**Zero-noise lower bound.**

Take any feasible `h` with `||h||_∞ ≤ 2B` and `O_r F h = 0`. Write `h = z - z'` with `z, z' ∈ [-B,B]^d`. Then

```text
O_r F z = O_r F z'
```

while the protected-variable gap equals `||L F h||`. Any estimator given the shared exact record must approximate both protected values at once, so the triangle inequality gives a worst-case error at least `||L F h|| / 2`. Taking the supremum yields

```text
sup_{x ∈ A_B} d_P(\widehat p(M_r(x)), p(x)) ≥ Γ_r(B) / 2.
```

### Interpretation

This is the strongest current theorem-grade statement in the branch:

- the exact threshold is the first level where the structured collision gap vanishes;
- below that threshold the branch gets an explicit positive no-go quantity, not just a boolean failure flag;
- periodic cutoff laws and diagonal finite-history laws are corollaries, not isolated curiosities.

### What It Does Not Say

It does **not** give a universal scalar complexity law across every branch system.

The theorem only controls finite-dimensional restricted linear families with a nested observation family. That restriction is part of why it survives falsification.

## 6. Qubit Fixed-Basis Phase-Loss Law

Consider the pure qubit family

```text
|ψ(θ,φ)⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩
```

with computational-basis record

```text
M_Z(θ,φ) = (cos²(θ/2), sin²(θ/2)).
```

Take the protected variable to be the Bloch vector

```text
p(θ,φ) = (sin θ cos φ, sin θ sin φ, cos θ),
```

and restrict to the phase-window family

```text
φ ∈ [-w, w].
```

### Proposition 6.1

The full Bloch-vector fiber ambiguity satisfies

```text
κ_{M_Z,p}(0) = 2 sin(min(w, π/2)).
```

### Derivation

Holding `θ` fixed keeps the record fixed. The Bloch-vector distance between phases `φ` and `φ'` at the same polar angle is

```text
||p(θ,φ) - p(θ,φ')|| = 2 sin(θ) |sin((φ-φ')/2)|.
```

The maximum over the admissible window occurs at `θ = π/2` and maximal phase separation `|φ-φ'| = 2w`, giving

```text
κ_{M_Z,p}(0) = 2 sin(min(w, π/2)).
```

### Cross-checking

Checked against the computational sweep with refined `θ` and `φ` sampling.

### Consequence

The weaker protected variable `z = cos θ` stays exactly recoverable because the record already determines `θ`.

## 7. Divergence-Only No-Go

Let `A` be a nontrivial family of divergence-free vector fields and let

```text
M(u) = ∇·u.
```

Take the protected variable to be any nonconstant map on `A`; the strongest version is `p(u)=u`.

### Proposition 7.1

Exact recovery from divergence-only data is impossible on `A`.

### Derivation

For any two distinct states `u,v ∈ A`,

```text
M(u) = 0 = M(v)
```

while `p(u) ≠ p(v)`. This is an immediate fiber collision.

### Status

Elementary but genuinely useful. It kills a tempting but underpowered recovery architecture.

## 8. Periodic Functional Threshold Law

Consider the finite periodic incompressible modal family

```text
ω = \sum_{j=1}^m c_j ω_j,
```

where each `ω_j` is a single Fourier-supported vorticity mode with cutoff level `q_j`, and let the protected variable be any linear functional

```text
p(c)=a \cdot c
```

or any finite list of such functionals. The selected-coefficient case is the special case in which the rows of `S` are canonical basis vectors.

Let the observation map be low-pass truncated vorticity at cutoff `Q`.

### Proposition 8.1

Exact recovery of `p` is possible if and only if every modal coefficient used by the protected variable survives the truncation, i.e.

```text
Q ≥ max { q_j : a_j ≠ 0 }.
```

### Derivation

In the modal basis, the observation map is diagonal:

```text
M_Q(c) = D_Q c,
```

where `(D_Q)_{jj}` is a nonzero scalar when `q_j ≤ Q` and zero otherwise.

Therefore

```text
ker(M_Q) = span { e_j : q_j > Q }.
```

By Proposition 5.3, exact recovery of `a \cdot c` holds exactly when the protected row lies in the row space of `D_Q`, which happens precisely when every index with `a_j ≠ 0` survives truncation. In the selected-coefficient language, exact recovery of `S c` holds exactly when

```text
ker(D_Q) ⊂ ker(S).
```

These are the same statement written in kernel and row-space language.

### Implemented family

For the four-mode family with cutoff levels `(1,2,3,4)`:

- `mode_1_coefficient`: threshold `1`
- `modes_1_2_coefficients`: threshold `2`
- `low_mode_sum`: threshold `2`
- `bandlimited_contrast`: threshold `3`
- `full_weighted_sum`: threshold `4`
- `full_modal_coefficients`: threshold `4`

### Cross-checking

This proposition was checked by:

1. direct kernel-inclusion reasoning,
2. row-space residual checks from the independent minimal-complexity routine,
3. pseudoinverse-based recovery on the coefficient grid,
4. finite-family collision scans across two discretizations.

## 9. Diagonal Functional Interpolation Law

Consider

```text
x_{t+1} = diag(λ_1, …, λ_n) x_t,
y_t = \sum_{j=1}^n c_j x_{t,j},
p(x_0)=g \cdot x_0,
```

with distinct active eigenvalues among the indices where `c_j ≠ 0`.

Let `A_H` denote the record map built from the first `H` observations and define the active index set

```text
J = { j : c_j ≠ 0 }.
```

### Proposition 9.1

Exact recovery of `g \cdot x_0` from the first `H` observations holds if and only if there exists a polynomial `P` of degree at most `H-1` such that

```text
g_j = c_j P(λ_j)    for j ∈ J,
```

and

```text
g_j = 0    for j ∉ J.
```

### Derivation

The record matrix is

```text
O_H =
\begin{bmatrix}
c_1 & \cdots & c_n \\
c_1 λ_1 & \cdots & c_n λ_n \\
\vdots & & \vdots \\
c_1 λ_1^{H-1} & \cdots & c_n λ_n^{H-1}
\end{bmatrix}.
```

Restrict to the active coordinates. Up to column scaling by `c_j`, this is a Vandermonde matrix in the active eigenvalues.

Any recovery weights `w_0, …, w_{H-1}` produce the estimator

```text
\sum_{t=0}^{H-1} w_t y_t
= \sum_{j=1}^n c_j \Big( \sum_{t=0}^{H-1} w_t λ_j^t \Big) x_{0,j}.
```

So exact recovery of `g \cdot x_0` is possible exactly when the polynomial

```text
P(λ)=\sum_{t=0}^{H-1} w_t λ^t
```

matches `g_j / c_j` on the active eigenvalues and kills every hidden protected direction.

### Explicit recovery weights

When the interpolation condition holds, the exact recovery weights are the polynomial coefficients of `P`.

### Special cases

1. **Coordinate recovery.**
   For `g=e_k`, exact recovery requires the Lagrange interpolant that equals `1/c_k` at `λ_k` and `0` on the other active eigenvalues. If `k ∈ J`, this has degree `|J|-1`, so the minimal exact horizon is `|J|`. If `k ∉ J`, exact recovery is impossible.
2. **Moment-type functionals.**
   If `g_j = c_j q(λ_j)` for a low-degree polynomial `q`, then the minimal exact horizon is at most `deg(q)+1`, even when the full active state dimension is larger.

### Cross-checking

This theorem was checked by:

1. explicit interpolation weights,
2. pseudoinverse recovery from the record matrix,
3. nullspace-on-a-box collision computation,
4. horizon sweeps on three active-profile families and four protected functionals,
5. direct comparison between predicted minimal horizons and exact-recovery classifications.

## 10. What Stayed Strong And What Did Not

### Clean and retained

- exactness through fiber separation,
- `κ(0)=0` exactness,
- adversarial lower bound `κ(η)/2`,
- restricted linear kernel criterion,
- nested minimal-complexity criterion,
- periodic functional support law,
- diagonal functional interpolation law.

### Useful but standard-adjacent

- qubit phase-loss law,
- divergence-only no-go in bare logical form,
- two-step control recovery formula.

### Still open

- a genuinely nontrivial cross-domain threshold theorem beyond the family-specific modal and diagonal cases,
- a stronger `κ` theorem that does more than organize exactness and minimax obstruction,
- a general minimal-record complexity theory that is not just family-specific linear algebra.
