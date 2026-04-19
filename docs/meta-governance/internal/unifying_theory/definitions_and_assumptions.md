# Definitions and Assumptions

Date: 2026-04-17

## 1) Core Definitions

### D1. Admissible family
`A ⊆ X` is the set of states the claim is about. All exactness/no-go statements are relative to `A`.

### D2. Target map
`T : A -> Z` is the protected/desired object to recover or preserve.

### D3. Record map
`M : A -> Y` is the observation/measurement map available to recovery/correction architecture.

### D4. Exact recoverability
`T` is exactly recoverable from `M` on `A` iff there exists `R : M(A) -> Z` such that `R(M(x)) = T(x)` for all `x ∈ A`.

### D5. Fiber collision
A pair `(x,x')` with `M(x)=M(x')` and `T(x) != T(x')`.

### D6. Exact modulo symmetry
Given nuisance relation `~`, exact modulo symmetry means exactness of target classes on `A/~`.

### D7. Branch-limited theorem
A theorem valid only under declared branch hypotheses (e.g., restricted-linear class, supported one-soliton class, declared MHD ansatz family, compatible bounded-domain class).

### D8. Validated result
Reproducible computational evidence on declared tested families without full theorem promotion.

## 2) Assumption Blocks by Branch

### A-U (Universal core assumptions)
- explicit `(A,T,M)` map structure,
- exact recoverability semantics as D4,
- admissible-family declaration is part of statement.

### A-RL (Restricted-linear OCP assumptions)
- finite-dimensional family `A={Fz}`,
- linear record `OFz` and target `LFz`,
- exactness judged via `ker(OF) ⊆ ker(LF)`.

### A-BD (Bounded-domain assumptions)
- declared protected class includes boundary/domain compatibility,
- architecture must satisfy full compatibility, not scalar residual only.

### A-SOL (Soliton restricted-lane assumptions)
- declared one-soliton family,
- explicit observation families,
- declared nuisance symmetry action for quotient claims.

### A-MHD (MHD closure assumptions)
- Euler-potential representation with declared ansatz classes,
- declared coefficient class (`η` structure),
- declared domain class (axis-touching vs annular).

### A-ENG (Engineering-layer assumptions)
- tools inherit theorem structure from supported branches,
- tool outputs carry explicit evidence labels,
- no automatic theorem promotion from tool behavior.

## 3) Scope and Validity Rules

1. No theorem applies outside its assumption block unless explicitly re-proved.
2. No validated result is upgraded to theorem without proof closure.
3. If assumptions change, status must be re-evaluated.
4. All branch bridges require explicit map-level translation, not terminology similarity.
