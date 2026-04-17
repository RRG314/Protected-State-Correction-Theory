# Theorem Candidates and Surviving Results

## 1. Universal exactness theorem

### URI-T1: Fiber-factorization exactness

Let `F ⊂ X`, `M : F → Y`, and `p : F → P`.
Then the following are equivalent:

1. `p` is exactly recoverable from `M` on `F`.
2. `p` is constant on every fiber of `M`.
3. `p` factors through `M` on `F`.

Status:
- `PROVED`
- standard

Value:
- this is the true universal backbone.

## 2. Coarsening theorem

### URI-T2: Coarsening monotonicity and detectable-only hierarchy

If `q = φ ∘ p` and `p` is exactly recoverable from `M`, then `q` is exactly recoverable from `M`.

Conversely, exact recovery of `q` does not imply exact recovery of `p`.
That failure already occurs:
- on finite fiber-collision examples,
- and on restricted finite-dimensional linear families.

Status:
- forward implication: `PROVED`, standard
- converse failure: `PROVED` by explicit counterexample in this repo

Value:
- formal basis for weaker-vs-stronger targets,
- direct home for detect-vs-correct language.

## 3. Significant surviving negative theorems

### URI-N1: No rank-only exact classifier theorem

For every triple of integers `n > r ≥ 1` and `r ≤ k < n`, there exist two restricted finite-dimensional linear recovery problems with the same:
- ambient family dimension `n`,
- protected rank `r`,
- observation rank `k`,

but opposite exactness verdicts:
- one is exactly recoverable,
- one is impossible.

Equivalently:
- no classifier depending only on `(n, rank(LF), rank(OF))`
  can correctly decide exact recoverability on all restricted finite-dimensional linear families.

Status:
- `PROVED`
- strongest branch-specific negative theorem

Why it matters:
- it kills amount-only language at a mathematically clean level,
- it explains why exact positive laws above the fiber level must be structural,
- and it is strong enough to travel across fields as a warning even where the proof itself is restricted-linear.

### URI-N2: No fixed-library budget-only exact classifier theorem

Fix the coordinate candidate library

```text
C = {e_1^T, …, e_n^T}
```

with unit measurement cost.
For every `n > r ≥ 1` and `r ≤ k < n`, there exist two selections from `C`
with the same:
- library,
- selection size `k`,
- and total cost `k`,

but opposite exactness verdicts on the restricted finite-dimensional linear class.

Equivalently:
- even in a fixed admissible sensor library,
- measurement count and budget alone do not classify exact recoverability.

Status:
- `PROVED`
- branch-new strengthening of `URI-N1`

Why it matters:
- it kills the stronger practical slogan that a fixed sensor budget should determine exactness,
- and it ties the anti-universal theorem directly to candidate-library design language rather than only to abstract ranks.

## 4. Quantitative noisy target-hierarchy theorem

### URI-T3: Noisy weaker-versus-stronger separation on the restricted-linear class

Let `x = F z` lie in a bounded coefficient family and let noisy records be

```text
y = O F z + e,  ||e||_2 ≤ η.
```

Assume:
- the weaker target `W F z` is exactly recoverable with `K O F = W F`,
- the stronger target `S F z` is not exact on the same family,
- and the stronger collision gap on the bounded family is `Γ > 0`.

Then:
1. the weaker target admits the uniform error upper bound

```text
||K y - W F z||_2 ≤ ||K||_2 η,
```

2. every decoder for the stronger target has worst-case error at least

```text
Γ / 2
```

for every noise radius `η ≥ 0`,
3. so the weak upper bound stays strictly below the stronger impossibility floor whenever

```text
η < Γ / (2 ||K||_2).
```

Status:
- `PROVED`
- strongest current noisy theorem in the branch

Why it matters:
- it turns weaker-versus-stronger language into a quantitative noisy separation theorem,
- and it shows that stable weak recovery and strong-target impossibility can coexist on the same record even after noise is admitted.

## 5. Corollary: where unification stops

### URI-C1: Universal exactness fragments above the fiber level

Universal exactness survives at the factorization/fiber level.
Any stronger exact classifier based only on amount-type invariants already fails on the restricted-linear class, and the failure survives even inside a fixed unit-cost candidate library.

Status:
- `PROVED` as a consequence of `URI-T1` and `URI-N1`

Interpretation:
- this is the branch's main honest unification result.

It does **not** say fields have nothing in common.
It says the common structure above the fiber level is not captured by amount alone.

## 6. Demoted candidates

### URI-X1: One universal threshold law
Verdict:
- `DISPROVED` as a serious branch claim

Reason:
- periodic support thresholds,
- diagonal interpolation thresholds,
- and qubit phase-window collisions
arise from genuinely different structural mechanisms.

### URI-X2: One universal augmentation formula
Verdict:
- `DISPROVED` as a universal claim

Reason:
- the unrestricted linear deficiency formula survives,
- but it does not extend honestly to every branch in the same form.

### URI-X3: One universal detectability definition across all fields
Verdict:
- `DISPROVED` / too broad

Reason:
- target-coarsening detectability,
- classical control detectability,
- and coding-theory detectability
match only partially.

## 7. Strongest open targets

1. admissible-family-enlarged or genuinely weighted-cost version of `URI-N2`
2. richer noisy weaker-versus-stronger theorems beyond the current single restricted-linear class
3. branch-specific detectability theorem connecting finite exactness, observer asymptotics, and target coarsenings on a richer restricted class

See also:
- [proof-sketches.md](proof-sketches.md)
