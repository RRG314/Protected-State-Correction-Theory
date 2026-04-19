# Invariant Expansion Master

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

Primary expansion artifacts:
- `data/generated/invariants/deep_invariant_catalog.csv` (`2640` rows)
- `data/generated/invariants/deep_invariant_stress.csv` (`116` rows)

## 1) Delta-free tightening

Observed from deep catalog:
- nonempty `delta_free` counts:
  - `0`: `268`
  - `1`: `721`
  - `2`: `585`
  - `3`: `408`
  - `4`: `275`

Interpretation:
- positive completion cost is frequent in context-sensitive classes.
- distribution is nontrivial and supports threshold-law development.

Status:
- `PROVED ON SUPPORTED FAMILY` (existence and finite-threshold behavior).
- exact closed-form dependence on context geometry: `OPEN`.

## 2) Delta-C tightening

Observed:
- `delta_C > 0` rows in deep catalog: `26`.
- agreement-operator anomalies show:
  - `candidate_library_defect_impossibility`: `14`
  - `library_gain_not_sufficient`: `14`

Interpretation:
- constrained completion has a distinct geometry from free completion.

Status:
- `PROVED ON SUPPORTED FAMILY` for no-go role.
- full necessary/sufficient theorem over general libraries: `OPEN`.

## 3) CID / context-coherence tightening

Observed:
- deep catalog rows with `context_gap=1`: `1096`.
- supported family split is large and reproducible.

Interpretation:
- local decoder existence and shared decoder existence are structurally different objects.

Status:
- split theorem: `PROVED ON SUPPORTED FAMILY`.
- strongest exact coherence equivalence beyond CID zero-test: `CONDITIONAL`.

## 4) Descriptor-lift expansion

Observed:
- from meta descriptor rows:
  - amount-only DFMI/IDELB = `0.3478` / `0.25`
  - amount+lift DFMI/IDELB = `0.0` / `0.0`
  - CL = `0.25`
- legacy descriptor branch also shows stronger lift case (`0.5` IDELB reduction).

Interpretation:
- compatibility lift is a robust anti-classifier repair signal on supported catalogs.

Status:
- scoped theorem: `PROVED ON SUPPORTED FAMILY`.
- universal elimination claim: `CONDITIONAL`.

## 5) Stress and robustness expansion

Deep stress summary:
- total rows: `116`
- by type:
  - `family_enlargement`: `101`
  - `target_mismatch`: `6`
  - `observation_noise`: `6`
  - `model_mismatch`: `3`
- fragility flags: `115/116`

Interpretation:
- fragility is not a corner case in current catalogs.

Status:
- fragility existence: `PROVED ON SUPPORTED FAMILY`.
- quantitative robustness laws: `VALIDATED / NUMERICAL ONLY`.

## 6) Positive recoverability/design unification

Current best constructive unification:
1. feasibility check: CID zero-test,
2. unconstrained repair cost: `delta_free`,
3. constrained repair feasibility: `delta_C`,
4. descriptor ambiguity and lift: DFMI/IDELB/CL.

This supports a theorem-backed design workflow on supported classes.

Status:
- workflow-level claim: `PROVED ON SUPPORTED FAMILY` as a staged decision process.
- universal design optimality claim: `OPEN`.
