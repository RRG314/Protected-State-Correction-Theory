# Core Formalism

## Status

Core branch formalism.

Universal definitions are kept as lean as possible so that theorem statements, no-go statements, field dictionaries, and executable tests all point to the same objects.

## 1. Basic objects

Let:
- `X` be a state space,
- `F ⊂ X` an admissible family,
- `P` a target space,
- `Y` a record space,
- `p : F → P` the target map,
- `M : F → Y` the record / observation / information map.

Optional branch objects:
- `D` a disturbance class,
- `A` a decoder / controller / correction / estimator class,
- `M_{0:t}` a history record,
- `\widetilde M` an augmented record or redesigned architecture.

## 2. Exact recoverability

`p` is **exactly recoverable** from `M` on `F` if there exists `R : M(F) → P` such that

```text
R(M(x)) = p(x)    for all x ∈ F.
```

Equivalent universal form:

```text
p = R ∘ M    on F.
```

This is the clean factorization statement.

## 3. Approximate / stable recoverability

Given metrics `d_Y` and `d_P`, `p` is **stably approximately recoverable** if there exists `R` and a modulus `ω` with `ω(0)=0` such that

```text
d_P(R(y), p(x)) ≤ ω(d_Y(y, M(x)))
```

in the perturbation regime of interest.

## 4. Asymptotic recoverability

A target is **asymptotically recoverable** if there exists a history-based or observer-based rule `R_t` such that

```text
d_P(R_t(M_0(x), …, M_t(x)), p(x)) → 0
```

as `t → ∞`.

This is the correct branch notion for observers, continuous monitoring, and damping-style architectures.

## 5. Detectable-only regime

The branch uses a precise, modest notion.

A target `p` is in the **detectable-only** regime if:
- `p` is not exactly recoverable from `M`,
- but there exists a nonconstant coarsening `q = φ ∘ p` that is exactly recoverable from `M`.

This captures:
- detect-but-not-correct logic in coding,
- weaker-versus-stronger target splits,
- partial classification when full reconstruction fails.

It is **not identical** to classical control-theoretic detectability in full generality.
That control notion is treated separately in the control dictionary.

## 6. Impossibility / irrecoverability

`p` is **impossible** or **irrecoverable** from `M` on `F` if no exact recovery map exists.

The universal obstruction is a fiber collision:

```text
M(x) = M(x') but p(x) ≠ p(x').
```

## 7. Weaker and stronger targets

`q` is a **weaker target** than `p` if `q = φ ∘ p` for some map `φ`.

Interpretation:
- `p` distinguishes more states than `q` does,
- exact recovery of `p` implies exact recovery of `q`,
- but not conversely.

This is the formal core of the branch's weaker-versus-stronger target language.

## 8. Minimal augmentation / redesign

Given a nonexact pair `(M, p)`, a minimal augmentation problem asks for the smallest admissible redesign `\widetilde M` such that `p` factors through `\widetilde M`.

This is universal in statement, but only restricted theorem classes currently survive in the repo:
- unrestricted linear augmentation count on restricted linear families,
- periodic mode/cutoff enrichments,
- diagonal history extensions,
- bounded-domain architecture swaps.

## 9. Protected-action principle

When a decoder/controller/correction architecture acts directly on states rather than only on records, admissibility requires two things:

1. **target compatibility**

```text
p(C(x)) = p(x)
```

on the protected family whenever the architecture is claimed to preserve the target;

2. **disturbance separation or suppression**

The action must either:
- separate the admissible disturbance classes,
- or suppress them asymptotically without destroying the target.

This is a universal design rule, but not currently a universal theorem.
Its exact theorems in this repo are branch-specific:
- exact projectors,
- sector recovery,
- invariant-split generators,
- restricted recoverability operators.

## 10. Universal principles that survive

### URI-F1: Fiber-factorization exactness
`PROVED`, standard.

Exact recovery holds iff `p` is constant on fibers of `M`, equivalently iff `p` factors through `M` on `F`.

### URI-F2: Coarsening monotonicity
`PROVED`, standard-adjacent.

If `q = φ ∘ p` and `p` is exactly recoverable from `M`, then `q` is exactly recoverable from `M`.

### URI-F3: Detectable-only by coarsening
`PROVED`, standard-adjacent.

If some nonconstant coarsening `q = φ ∘ p` is exactly recoverable while `p` is not, the regime is detectable-only in the branch sense.

## 11. What fails above this level

The universal formalism does **not** produce:
- one cross-field threshold invariant,
- one scalar complexity number,
- one rank/count criterion,
- one universal augmentation formula.

That failure is not a defect of exposition.
It is one of the branch's main results.
