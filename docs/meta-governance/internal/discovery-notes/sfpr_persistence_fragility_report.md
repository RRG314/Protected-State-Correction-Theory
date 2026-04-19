# SFPR Persistence and Fragility Report

Status: `EXPLORATION / NON-PROMOTED`

Artifact reference: `data/generated/sfpr/persistence_anomalies.csv` (`607` anomalies).

## Core Question

When does target-relevant structure persist under context/representation changes, and when does it fail while local recoverability appears intact?

## Results Summary

Anomaly counts by type:
- `local_exact_global_fail`: `224`
- `context_drift_flip`: `223`
- `model_mismatch_instability`: `152`
- `noise_fragility_flip`: `8`

Supporting summary key:
- conditioned-vs-invariant split support: `224`
- threshold flips (all families): `390`

## Main Persistence Findings

### 1) Local persistence does not imply global persistence
- Many families remain contextwise exact but lose shared exactness.
- This is the strongest persistence-layer signal and links directly to `CID`.
- Status: `PROVED` on supported families.

### 2) Context drift is a dominant fragility mechanism
- Small context perturbations frequently flip global verdicts.
- Status: `VALIDATED / EMPIRICAL ONLY`.

### 3) Representation mismatch is a major failure mode
- Reparameterization/model mismatch increases residuals and can destroy previously exact recovery.
- Status: `VALIDATED / EMPIRICAL ONLY`.

### 4) Pure additive noise is weaker than context drift in this setup
- Noise-driven flips are fewer than context-driven flips.
- Status: `CONDITIONAL` (depends on synthetic family design).

## Persistence Layer Interpretation

Surviving structure:
- persistence should be defined relative to **shared decoder feasibility** and target-fiber stability, not only per-context exactness.

Rejected simplification:
- "if each context is exact then system is stable" is false in this corpus.

## Recommended Persistence Invariants for Next Pass

1. `CID(C, tau)` as primary global fragility indicator.
2. mismatch amplification index based on residual increase under representation change.
3. threshold fragility curves from `threshold_catalog.csv` restricted to context-varying families.
