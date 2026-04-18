# Branch 01 — Exact Projector and Sector

## What this branch is
Exact correction architecture for projector-compatible settings and sector-conditioned recovery structures.

## Strongest results
- Exact projector theorem family.
- Sector-conditioned exact recovery theorem package.
- Sector-overlap detection impossibility boundary.

## Canonical documents
- [Central theorem](../../docs/theorem-candidates/central-theorem.md)
- [Sector recovery theorems](../../docs/theorem-candidates/sector-recovery-theorems.md)
- [Capacity and structure bounds](../../docs/theorem-candidates/capacity-theorems.md)
- [Advanced no-go results](../../docs/impossibility-results/advanced-no-go-results.md)

## Key tests / artifacts
- `tests/math/test_sector_recovery.py`
- `tests/math/test_capacity.py`

## Open items
- Extend exact-sector guarantees beyond current declared compatibility assumptions.

## Shared infrastructure
Use centralized math kernels and theorem-linked tests from `src/ocp` and `tests/math`.
