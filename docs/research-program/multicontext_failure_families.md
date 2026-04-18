# Multi-Context Failure Families

Status: `EXPLORATION / NON-PROMOTED`

Main track C: opposite-verdict and failure-family package in multi-context settings.

## Data Sources

- `data/generated/context_sensitive_recoverability/multicontext_witness_catalog.csv` (`1800` families)
- `data/generated/context_sensitive_recoverability/multicontext_anomaly_catalog.csv` (`1890` anomalies)

## Core Failure Families

## F1) Conditioned-Exact / Invariant-Fail Families

Definition:
`local_exact_all=1` and `shared_exact=0`.

Count:
`506` families.

Status:
`PROVED ON SUPPORTED FAMILY` as a structural split family.

## F2) Same-Descriptor Opposite-Shared-Verdict Families

Definition:
same descriptor signature `(n,k,m,rank_stack,total_budget)` with opposite `shared_exact` outcomes.

Count:
`23` descriptor groups.

Status:
`PROVED ON SUPPORTED FAMILY` no-go witness class.

Representative signatures:
- `n7|k3|m2|r2|b6`
- `n5|k4|m2|r2|b8`
- `n4|k2|m2|r3|b4`

## F3) Family Enlargement Flip Families

Definition:
shared verdict changes after adding one extra context.

Count:
`94` flips total.

Transition pattern:
- `shared 1 -> 0`: `94`

Status:
`VALIDATED / EMPIRICAL ONLY`.

## F4) Positive Shared-Augmentation Families

Definition:
local exact/global fail families where a positive shared augmentation restores invariant exactness.

Count in anomaly catalog:
`1306` positive-threshold anomaly rows (includes repeated signatures across families).

Status:
`PROVED ON SUPPORTED FAMILY` for existence; exact law remains conditional.

## Amount-Only vs Context-Compatibility Separation

Amount-only failures:
- rank-only mismatch: `668/1800`
- budget-only mismatch: `1306/1800`

Context-compatibility failures:
- conditioned-exact/invariant-fail: `506`
- same-descriptor opposite verdict groups: `23`
- enlargement flips: `94`

Interpretation:
Descriptor insufficiency is present, but context-compatibility constraints are the direct mechanism for invariant failure.

## Fragility Notes

- Opposite-verdict groups persist across several descriptor signatures and are not one-off artifacts.
- Family enlargement introduces additional incompatibility even when prior shared exactness existed.

## Strongest Supported No-Go Statement

No descriptor-only classifier based on stack rank, total budget, and context count can classify context-invariant exactness across the supported multi-context family class.

Status: `PROVED ON SUPPORTED FAMILY`.
