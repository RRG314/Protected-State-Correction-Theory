# Universal Core Refinement Report

Date: 2026-04-17

Goal: test whether the universal core can be sharpened without crossing branch limits.

## Candidate UC-R1: Fiber Constancy Exactness

### Strongest possible statement
For all branches in scope, exactness is equivalent to fiber constancy under one uniform map structure.

### Weaker provable statement
For declared recoverability formulations `(A,T,M)`, exactness iff `T` is fiber-constant / factors through `M`.

### Proof status
- strongest form: `CONDITIONAL` (fails to map identically to all non-recoverability closure formulations).
- weaker form: `PROVED`.

### Promotion decision
Promote weaker statement into universal core.

## Candidate UC-R2: Indistinguishability / Collision No-Go

### Strongest possible statement
Any target-distinguishing collision forces impossibility across all in-scope branches.

### Weaker provable statement
If equal record values imply different target values on declared admissible family, exact recoverability is impossible.

### Proof status
- strongest form: `PROVED` when record/target map are explicit,
- broader process-level interpretation across non-record formulations: `CONDITIONAL`.

### Promotion decision
Promote map-level theorem form into universal core; keep process-level reinterpretations branch-limited.

## Candidate UC-R3: Detectable-only Through Target Coarsening

### Strongest possible statement
Whenever strong target fails, there always exists a meaningful weaker target that remains exact.

### Weaker provable statement
If strong target is exact then any coarsening is exact (forward monotonicity). Converse can fail.

### Proof status
- strongest form: `REJECTED` (existence of useful coarsening is not guaranteed universally),
- weaker monotonicity + converse-failure form: `PROVED`.

### Promotion decision
Promote forward monotonicity as universal-core-adjacent theorem; retain existential weaker-target claims as branch-limited.

## Candidate UC-R4: Exact Recoverability as Quotient/Factorization on Admissible Family

### Strongest possible statement
One quotient/factorization theorem uniformly captures all branch exactness and preservation claims.

### Weaker provable statement
Recoverability theorems require explicit admissible-family and nuisance-equivalence declarations; quotient/factorization is exact within that declared model.

### Proof status
- strongest form: `REJECTED` (preservation/closure branches have additional operator PDE structure not fully reduced),
- weaker form: `PROVED` as framework governance theorem.

### Promotion decision
Promote weaker form.

## Refinement Outcome

Universal core is sharpened to three explicit promoted items:
1. factorization/fiber exactness (`PROVED`),
2. collision no-go (`PROVED`),
3. coarsening monotonicity with converse-failure warning (`PROVED`, core-adjacent).

No stronger universal promotion survives for cross-branch preservation/emergence claims.
