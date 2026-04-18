# Invariant Falsification Report

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This report applies the required counterattacks to existing and candidate invariants.

## Attack Matrix

## ATTACK 1: Invariant is rank/count/budget in disguise

Result:
- **SURVIVES** for DFMI/IDELB/CL, CID/context-gap, and `(delta_free, delta_C)`.
- **COLLAPSES** for pure amount-signature descriptors.

Evidence:
- amount-only ambiguity remains high (`rank` ambiguity rate `1.0`, budget ambiguity rate `1.0`).
- lifted descriptors remove ambiguity on supported catalogs.

## ATTACK 2: Invariant is row-space inclusion renamed

Result:
- **PARTIALLY SURVIVES**.

Interpretation:
- fiber/row-space remains the exact backbone.
- context-coherence and descriptor-lift invariants are additive only at multi-context/classifier layers.

## ATTACK 3: Works only on tiny hand-built examples

Result:
- **PARTIALLY SURVIVES**.

Evidence:
- strong support from large existing context-sensitive catalogs (`1800` rows), not only tiny synthetic sets.
- new invariant pass is compact (`32` systems) and should not be treated as sole evidence source.

## ATTACK 4: No theorem consequence, only weak correlation

Result:
- **PARTIALLY SURVIVES**.

Details:
- CID has exact zero-test consequence in supported class.
- CL gives explicit lower-bound reduction in descriptor ambiguity.
- MIS/FEFI candidates remain mostly diagnostic and conditional.

## ATTACK 5: Fails under enlargement or mismatch

Result:
- **SURVIVES** as falsification signal against weak invariants.

Details:
- fragility is real (`exact -> fail` under enlargement/mismatch/noise in stress catalogs).
- invariants that cannot encode fragility are insufficient.

## ATTACK 6: Coordinate dependence / representation fragility

Result:
- **PARTIALLY SURVIVES**.

Details:
- row-space and kernel criteria are representation-invariant.
- some quantitative descriptor choices need normalization and basis-robust definitions.

## ATTACK 7: Adds no value beyond minimal augmentation law

Result:
- **PARTIALLY SURVIVES**.

Details:
- `delta_free` alone is insufficient under candidate constraints.
- `delta_C` and CL add value by identifying constrained impossibility and classifier repair.

## Per-candidate verdicts

- Fiber/factorization exactness: **SURVIVES** (core exact invariant).
- Row-space residual/null-intersection: **SURVIVES** (core exact invariant).
- `delta_free`: **SURVIVES** (constructive threshold invariant, supported class).
- `delta_C`: **SURVIVES** (candidate-library no-go invariant, supported class).
- DFMI/IDELB/CL: **SURVIVES** on supported catalogs; broader universality remains conditional.
- CCD/CID: **SURVIVES** as supported-class zero-test.
- FEFI/MIS/MDDF: **PARTIALLY SURVIVES** (diagnostic candidates).
- Broad alignment novelty claim: **COLLAPSES** (many components reduce to known compatibility logic).

## Falsification conclusion

The strongest invariant program survives as a **restricted, theorem-backed core plus quantitative descriptor/context extensions**. Broad universal invariant claims do not survive.
