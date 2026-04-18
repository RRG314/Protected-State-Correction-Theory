# Invariant Global Falsification Report

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This report applies full-program counterattacks to the invariant theorem stack and to the positive-recoverability extension claims.

Primary evidence:
- `data/generated/invariants/deep_invariant_catalog.csv` (`2640` rows)
- `data/generated/invariants/deep_invariant_stress.csv` (`116` rows)
- prior invariant and positive-framework outputs in `docs/research-program/` and `discovery/`.

## Attack 1: “Everything is just row-space/fiber renamed”

Verdict: **PARTIALLY SURVIVES**.

What collapses:
- Any claim that replaces fiber/factorization or row-space exactness as core criteria.

What survives:
- `CID`/context-gap split (multi-context mergeability) is not captured by single-map rank descriptors.
- `delta_C` constrained-library no-go captures feasibility geometry beyond unconstrained row-space inclusion.

## Attack 2: “Only tiny synthetic examples”

Verdict: **PARTIALLY SURVIVES**.

Evidence for survival:
- multicontext + augmentation + agreement + invariant catalogs produce `2640` consolidated rows.

Boundary:
- still synthetic finite-family data; no non-synthetic benchmark transfer yet.

## Attack 3: “Fails under family enlargement”

Verdict: **SURVIVES** (as a real failure mechanism against overbroad claims).

Evidence:
- deep stress `family_enlargement` rows: `101`.
- fragility flags overall: `115/116`.

Implication:
- promotion-safe claims must stay family-scoped.

## Attack 4: “Fails under model mismatch”

Verdict: **PARTIALLY SURVIVES**.

Evidence:
- mismatch stress rows and target-mismatch shifts show exactness collapse behavior.

Boundary:
- theorem-quality mismatch constants are not yet established.

## Attack 5: “Coordinate dependence”

Verdict: **PARTIALLY SURVIVES**.

Survives:
- core fiber/row-space theorems are coordinate-invariant.

At risk:
- some quantitative diagnostics (proxy collision modes, branch-specific compatibility quantities) require explicit representation and mode labels.

## Attack 6: “No design value beyond old minimal augmentation law”

Verdict: **PARTIALLY SURVIVES**.

Why not full collapse:
- constrained-library layer (`delta_C`) yields explicit no-go cases where free-rank gain is insufficient (`14` anomalies).
- this is actionable for design/library selection.

## Attack 7: “Numerical correlation only, no theorem content”

Verdict: **PARTIALLY SURVIVES**.

Theorem-grade on supported classes:
- `CID=0 <=> shared exactness` (supported families)
- existence of local-exact/global-fail families
- positive `delta_free` thresholds
- `delta_C` no-go and gain-insufficiency witnesses

Numerical-only layers:
- fragility rates,
- mismatch slopes,
- high-null collision-gap proxies.

## Attack 8: “Breaks in candidate-library-constrained settings”

Verdict: **SURVIVES as a true boundary condition**.

Interpretation:
- this attack invalidates unconstrained-only optimism, but it strengthens the constrained-invariant package.

## Global falsification verdict

1. **Core exactness remains unchanged:** fiber/factorization and row-space criteria are still the theorem backbone.
2. **Additive survivor stack (supported-family):** `CID/context-gap + delta_free + delta_C + descriptor-lift metrics`.
3. **Demotions required:** broad universal-invariant claims, high-null exact collision-gap claims, and branch-transfer novelty claims.
4. **Promotion-safe shape:** restricted theorem package + explicit stress boundaries + design-layer interpretation.

## Final status labels after full counterattack

- `PROVED`: core factorization/row-space exactness criteria.
- `PROVED ON SUPPORTED FAMILY`: CID zero-test, context split, delta-free existence, delta-C no-go, descriptor-lift reductions.
- `VALIDATED / NUMERICAL ONLY`: fragility rates, mismatch amplification summaries, several branch transfer indicators.
- `CONDITIONAL`: broad context-coherence generalizations, universal descriptor-lift claims.
- `DISPROVED`: universal replacement-invariant and universal collision-gap exact-threshold claims.
