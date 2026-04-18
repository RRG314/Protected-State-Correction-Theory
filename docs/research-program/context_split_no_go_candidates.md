# Context Split No-Go Candidates

Status: `EXPLORATION / NON-PROMOTED`

Main track A no-go set for conditioned-vs-invariant recoverability.

## NG-A1 — Local Exactness Is Not Globally Sufficient

Claim:
`(forall c, exact in context c)` does not imply `shared exact across all contexts`.

Status: `PROVED ON SUPPORTED FAMILY`.

Evidence:
`485` local-exact/global-fail families in the generated catalog.

## NG-A2 — Descriptor-Only Classification No-Go

Claim:
No classifier based only on stack rank, total budget, and context count can exactly classify shared exactness.

Status: `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `16` same-descriptor opposite shared verdict groups.
- rank-only and budget-only mismatches are substantial.

## NG-A3 — Family Enlargement Stability No-Go

Claim:
Shared exactness is not stable under family enlargement (adding one context).

Status: `VALIDATED / EMPIRICAL ONLY`.

Evidence:
- `107` enlargement flips (`shared_exact: 1 -> 0`) in `1800` families.
- Transition counts: `(1 -> 0): 107`, `(1 -> 1): 39`, `(0 -> 0): 1654`.

## NG-A4 — Context Drift Robustness No-Go

Claim:
Small context perturbations can flip shared exactness even when conditioned exactness remains common.

Status: `VALIDATED / EMPIRICAL ONLY` (supported by prior SFPR persistence lane plus current drift-prone families).

## NG-A5 — Universal Context-Split Law (Unscoped) No-Go

Claim:
A universal context split theorem without family restrictions is currently unsupported.

Status: `PROVED` as a methodological no-go for this pass.

Reason:
- all positive statements depend on linear/supported-family assumptions,
- broad claims collapse to known observability/fiber formulations without additional structure.
