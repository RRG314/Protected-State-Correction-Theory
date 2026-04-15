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

## 8. Periodic Modal Minimal-Cutoff Theorem

Consider the finite periodic incompressible modal family

```text
ω = \sum_{j=1}^m c_j ω_j,
```

where each `ω_j` is a single Fourier-supported vorticity mode with cutoff level `q_j`, and let the protected variable be the selected coefficient vector

```text
p(c) = S c,
```

for a selector matrix `S`.

Let the observation map be low-pass truncated vorticity at cutoff `Q`.

### Proposition 8.1

Exact recovery of `p` is possible if and only if every selected coefficient corresponds to a retained mode, i.e.

```text
Q ≥ max { q_j : ||S e_j|| > 0 }.
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

By Proposition 5.1, exact recovery of `S c` holds exactly when

```text
ker(D_Q) ⊂ ker(S).
```

This is equivalent to requiring that every protected coefficient index `j` survive the truncation.

### Implemented family

For the three-mode family with cutoff levels `(1,2,3)`:

- `mode_1_coefficient`: threshold `1`
- `modes_1_2_coefficients`: threshold `2`
- `full_modal_coefficients`: threshold `3`

### Cross-checking

This proposition was checked by:

1. direct kernel-inclusion reasoning,
2. pseudoinverse-based recovery on the basis states,
3. finite-family collision scans across two discretizations.

## 9. Diagonal Minimal-History Theorem

Consider

```text
x_{t+1} = diag(λ_1, …, λ_n) x_t,
y_t = \sum_{j=1}^n c_j x_{t,j},
p(x_0)=x_{0,k},
```

with distinct active eigenvalues among the indices where `c_j ≠ 0`.

Let `A_H` denote the record map built from the first `H` observations.

### Proposition 9.1

Let `m` be the number of active sensor modes.

1. If `c_k = 0`, exact recovery of `x_{0,k}` is impossible for every finite horizon.
2. If `c_k ≠ 0` and `H < m`, exact recovery is impossible.
3. If `c_k ≠ 0` and `H = m`, exact recovery is possible, hence also for every `H ≥ m`.

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

- If `H < m`, the active restriction has nontrivial nullspace, so there exists an active state difference invisible to the record. Because the protected coordinate is active, one can choose that difference to change `x_{0,k}`.
- If `H = m`, the active restriction is square Vandermonde and invertible. Hence the active coordinates, and therefore `x_{0,k}`, are determined exactly.
- If `c_k = 0`, the protected coordinate never enters the record, so a fiber collision persists for every horizon.

### Explicit recovery weights

For `H = m`, the exact recovery weights are the coefficients of the interpolation polynomial that equals `1/c_k` at `λ_k` and `0` at the other active eigenvalues.

### Cross-checking

This theorem was checked by:

1. explicit interpolation weights,
2. pseudoinverse recovery from the record matrix,
3. nullspace-on-a-box collision computation,
4. horizon sweeps on three active-profile families.

## 10. What Stayed Strong And What Did Not

### Clean and retained

- exactness through fiber separation,
- `κ(0)=0` exactness,
- adversarial lower bound `κ(η)/2`,
- restricted linear kernel criterion,
- periodic modal minimal-cutoff theorem,
- diagonal minimal-history theorem.

### Useful but standard-adjacent

- qubit phase-loss law,
- divergence-only no-go in bare logical form,
- two-step control recovery formula.

### Still open

- a genuinely nontrivial cross-domain threshold theorem beyond the family-specific modal and diagonal cases,
- a stronger `κ` theorem that does more than organize exactness and minimax obstruction,
- a general minimal-record complexity theory that is not just family-specific linear algebra.
