# Formation Deepening Report

Status: secondary track continuation (`EXPLORATION / NON-PROMOTED`).

Primary artifacts:
- `data/generated/sfpr/formation_deep_bridge_catalog.csv`
- `data/generated/sfpr/formation_deep_bridge_summary.json`

Run snapshot (current):
- bridge rows: `180`
- mechanisms: `5` (`36` each)
- post local-not-shared cases: `65`
- threshold worsened cases: `53`
- threshold improved cases: `0`

## What was tested

Controlled formation transforms were applied to source context families, then measured pre/post on:
1. local exactness,
2. invariant exactness,
3. agreement-lift residual,
4. free shared-augmentation threshold.

Mechanisms:
- `constraint_generation`
- `context_drift`
- `intervention_cleaning`
- `optimization_induced`
- `context_conditioned_differentiation`

## Mechanism-level outcomes

- `context_drift`: `18/36` threshold-worsened, no improvements.
- `context_conditioned_differentiation`: `18/36` threshold-worsened, no improvements.
- `optimization_induced`: `17/36` threshold-worsened, `33/36` post local-not-shared.
- `constraint_generation`: `16/36` post local-not-shared.
- `intervention_cleaning`: `16/36` post local-not-shared.

## Main outcomes

1. Formation repeatedly generates local-exact but shared-fail regimes (`65` post local-not-shared cases).
2. Formation frequently increases global augmentation burden (`53` worsened thresholds).
3. No tested mechanism reduced free-threshold burden in this run (`0` improvements).
4. No independent theorem bridge from formation to shared recoverability emerged.

## Interpretation

Formation remains useful as a fragility/stress source for the main theorem lane, but not yet as a promoted theorem package.
The strongest rigorous content remains in context-sensitive compatibility and augmentation laws.

## Status labels

- bridge effects: `VALIDATED / EMPIRICAL ONLY`
- theorem-grade formation bridge: `OPEN`
- broad formation promotion: `DISALLOWED` in current evidence state
