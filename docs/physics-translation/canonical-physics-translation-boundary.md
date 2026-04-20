# Canonical Physics Translation Boundary

## Scope

This document is the canonical theorem-facing boundary for physics translation in this repository.

It classifies every physics-facing statement into one of three classes:
- theorem-grade mapping,
- validated branch-limited mapping,
- analogy-only mapping.

No statement in this file is an ontology claim. All mappings are branch-scoped.

## Status Classes

- `PROVED`: theorem on declared class with explicit assumptions.
- `VALIDATED`: numerical or model-grounded evidence on declared surrogate class.
- `CONDITIONAL`: mathematically plausible mapping not yet promoted as theorem.
- `ANALOGY ONLY`: interpretation aid with no theorem weight.
- `REJECTED`: outside accepted scope.

## Theorem-Grade Mapping Templates

### T-Phys-1 Measurement fiber template (`PROVED`)
Assumptions:
- admissible family `A`, record map `M`, target map `T`.
- exactness is judged by fiber constancy.

Statement:
- exact recoverability is equivalent to target constancy on record fibers.

Source anchors:
- `OCP-030`, `OCP-031`, `OCP-054`.

Translation use:
- any measurement system where hidden-state recovery is represented by declared records and targets.

### T-Phys-2 Coarse target hierarchy template (`PROVED`)
Assumptions:
- same record map, target pair `(p, q)` with `q = phi o p`.

Statement:
- exact recoverability of `p` implies exact recoverability of `q`; converse may fail.

Source anchor:
- `OCP-048`.

Translation use:
- coarse observables recoverable while finer structure remains irrecoverable.

### T-Phys-3 Target-independent dynamic garbling template (`PROVED`, restricted)
Assumptions:
- finite record process with binary target,
- target-independent Markov garbling from `Y_t` to `Y_{t+1}`.

Statement:
- optimal squared-loss defect is nondecreasing along the garbling semigroup.

Source anchor:
- `OCP-055`.

Non-extension note:
- does not cover target-dependent transition laws.

### T-Phys-4 Finite multivalued garbling template (`PROVED`, restricted)
Assumptions:
- finite-valued target with numeric values,
- squared-loss MMSE defect,
- target-independent Markov garbling.

Statement:
- MMSE defect is nondecreasing along the garbling chain.

Source anchor:
- `OCP-057` and `dynamic_garbling_law_checks.csv`.

### T-Phys-5 BSC horizon template (`PROVED`, restricted)
Assumptions:
- binary target with prior `0.5`,
- perfect initial observation,
- repeated target-independent `BSC(epsilon)` degradation.

Statement:
- defect flow is monotone and admits explicit horizon threshold crossings for any floor below `0.25`.

Source anchor:
- `OCP-063` and `dynamic_horizon_thresholds.csv`.

## Validated Branch-Limited Mapping Templates

### V-Phys-1 Surrogate degradation trend (`VALIDATED`)
- monotone defect growth under declared Hawking-like surrogate noise slices.
- source: `data/generated/structural-information-theory/coarse_graining_monotonicity.csv`.

### V-Phys-2 Hidden-mass ambiguity diagnostics (`VALIDATED`)
- latent-state ambiguity and compatibility defect diagnostics on declared hidden-mass surrogate lanes.
- source: `data/generated/structural-information-theory/unified_cross_domain_reduction_metrics.csv`.

## Counterexample / No-Go Translation Templates

### N-Phys-1 Broad dynamic monotonicity no-go (`PROVED`)
Assumptions broken:
- transition law allowed to depend on hidden target.

Statement:
- dynamic defect monotonicity can fail; broad law is false without garbling assumptions.

Source anchor:
- `OCP-056`.

### N-Phys-3 Non-injective measurement post-map boundary (`PROVED`, restricted)
Assumptions:
- measurement channel replaced by nonlinear post-map `phi o M`.

Statement:
- injective `phi` on recorded support preserves exactness class;
- non-injective `phi` can collapse distinct recoverable records and destroy exactness.

Use:
- blocks overreach from nonlinear sensor remapping without injectivity checks.

Source anchor:
- `OCP-061`.

### N-Phys-2 Universal gravity-information law (`REJECTED`)
- not supported by theorem package,
- outside accepted claim scope.

## Landauer and Irreversibility Boundary

Status: `CONDITIONAL`.

Allowed statement:
- logical erasure can be used as context for distinction collapse language under explicit map assumptions.

Forbidden statement:
- no promoted new thermodynamic theorem from this repository.

## Required Nonclaims

1. no gravity ontology claim,
2. no paradox-resolution claim,
3. no universal scalar invariant claim,
4. no branch-to-universal promotion without explicit theorem proof.

## Canonical References

- `docs/theorem-core/theorem-spine-final.md`
- `docs/theorem-core/no-go-spine-final.md`
- `docs/overview/proof-status-map.md`
- `docs/physics/kept-vs-rejected-physics-bridges.md`
