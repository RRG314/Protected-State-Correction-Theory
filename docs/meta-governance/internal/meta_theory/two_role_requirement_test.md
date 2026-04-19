# Two-Role Requirement Test

Date: 2026-04-17

## Goal

Make the intuition “you need two interacting parts” precise, then attempt to falsify it.

## Version W (Weak Form)

### Statement
In nontrivial recoverability/correction tasks, exactness requires:
1. a target role `T`, and
2. at least one interacting non-target structure (`M`, `C`, `E`, domain/symmetry constraint),
with verdict controlled by a compatibility condition.

### Falsification attempts
- **Attempt W1:** Exactness determined by target alone.
  - Result: failed in tested branches; changing observation/operator/domain changes verdict at fixed target.
- **Attempt W2:** Interacting role is artificial.
  - Result: failed in OCP (row-space/fiber), soliton (symmetry-invariant maps), MHD (profile/domain obstruction).

### Classification
`SURVIVES` (branch-limited, nontrivial contexts).

---

## Version M (Medium Form)

### Statement
Exact recoverability/correction is equivalent to compatibility between at least two distinct structures.

### Falsification attempts
- **Attempt M1:** find branch where exactness is independent of compatibility.
  - Result: not found in promoted branches.
- **Attempt M2:** show compatibility condition reduces to trivial identity.
  - Result: false in key branches; compatibility is restrictive (fiber constancy, kernel inclusion, boundary compatibility, symmetry-aware injectivity).

### Caveat
Equivalence is exact in some branches (OCP recoverability core), and only restricted/conditional in others (soliton continuous extension, broader MHD generalization).

### Classification
`SURVIVES ONLY WEAKLY TO MODERATELY` at cross-branch level; exact equivalence remains branch-dependent.

---

## Version S (Strong Form)

### Statement
Every meaningful system requires multiple interacting roles.

### Falsification attempts
- **Attempt S1:** single-object trivial identities (`T=M`, identity maps) already classify exactness in trivial settings.
- **Attempt S2:** some standalone equations are meaningful without recoverability/correction decomposition.

### Result
This version either:
- becomes tautological (“meaningful” redefined to force multiple roles), or
- becomes false in broad mathematical usage.

### Classification
`TAUTOLOGICAL OR FALSE` (not promotable).

## Additional attack: “Is second role always nontrivial?”

Not always. In trivial identity setups the second role can collapse into the first, and the thesis loses informative content.

Therefore the thesis must be scoped to **nontrivial recoverability/correction problems**.

## Final outcome
- Weak form: keep.
- Medium form: keep as branch-limited meta-pattern.
- Strong form: reject.
