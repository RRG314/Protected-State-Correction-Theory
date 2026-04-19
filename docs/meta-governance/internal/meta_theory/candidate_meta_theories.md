# Candidate Meta-Theories

Date: 2026-04-17
Pass: New theory-exploration (falsification-first)

## Purpose

Formalize and test candidate higher-level principles behind observed recoverability/unification failures across OCP, soliton, MHD, and SDS layers.

This document proposes candidates only; it does not promote them.

## Shared Setup

Use an explicit system tuple
`S = (A, T, M, C, E, D, ~)` where:
- `A`: admissible family,
- `T`: target/protected object,
- `M`: observation/representation map,
- `C`: correction architecture,
- `E`: evolution law (if dynamic),
- `D`: disturbance/ambiguity class,
- `~`: nuisance equivalence (symmetry quotient, if relevant).

Define compatibility relation `K` as the branch-specific condition that must hold for exactness (examples: fiber constancy, row-space inclusion, boundary-compatible Hodge structure, symmetry-aware identifiability).

---

## Candidate A — Interaction-Requirement Thesis

### Statement
For nontrivial recoverability/correction tasks, exactness requires at least two non-redundant roles:
1. a target role (`T`), and
2. an interacting non-target role (`M`, `C`, `E`, or domain/symmetry structure),
with exactness controlled by a compatibility condition `K(T, non-target role)`.

### Non-redundant (formalized)
Roles are non-redundant if one cannot be removed without changing exactness verdicts on `A`.

### What would count as evidence
- Branches where changing only the second role flips exact/impossible while `T` is fixed.
- Branches where exactness is equivalent to explicit compatibility between distinct roles.

### What would falsify
- A nontrivial branch where exactness is fully determined by `T` alone, independent of any second role.
- A branch where second-role changes never affect exactness.

### Initial status
`OPEN` (to be tested).

---

## Candidate B — Unification-Limit Thesis

### Statement
No amount-only compressed descriptor (rank-only, count-only, budget-only, single scalar capacity) can classify exact recoverability/correction across heterogeneous branches; branch-specific compatibility structure is required.

### Descriptor class
`phi(S)` built from amount metadata only (e.g., ranks, measurement count, budget count, residual magnitude alone) without structural compatibility information.

### What would count as evidence
- Same-rank or same-count opposite-verdict witness families.
- Theorem-grade anti-classifier results in supported classes.
- Domain/operator swaps that flip exactness at fixed amount.

### What would falsify
- A proven classifier using only amount metadata that is correct on all branches in scope.

### Initial status
`PROVED ON SUPPORTED FAMILY` for restricted-linear anti-classifier package; `CONDITIONAL` for broader cross-branch promotion.

---

## Candidate C — Representation-Distortion Thesis

### Statement
Exact global unification/recovery fails when the chosen representation or observation map collapses distinctions needed by the target; equivalently, target-distinguishing collisions obstruct exactness.

### Distortion (formalized)
A representation `M` is `T`-distorting on `A` if
`exists x1, x2 in A: M(x1)=M(x2) and T(x1)!=T(x2)`.

### What would count as evidence
- Fiber-collision no-go theorems.
- Symmetry-invariant observation no-go in quotient-identifiability settings.
- Family enlargement / model mismatch cases where hidden target-distinguishing directions appear.

### What would falsify
- A setting with persistent `T`-distortion but still exact recovery of `T` on the same `A`.

### Initial status
Core collision form `PROVED`; broader dynamic/closure interpretation `CONDITIONAL`.

---

## Candidate D — Strong “Everything Requires Multiple Interacting Roles” Thesis

### Statement
Every meaningful system description requires multiple interacting roles.

### Why included
This is a strong interpretation of the user intuition and must be stress-tested directly.

### Expected risk
High tautology/overreach risk due vague “meaningful system” quantifier.

### Initial status
`OPEN (high falsification priority)`.

## Next Step
All candidates are tested branch-by-branch in `cross_repo_meta_test.md` and then attacked directly in `two_role_requirement_test.md`.
