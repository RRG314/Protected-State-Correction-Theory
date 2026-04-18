# Branch 07 — CFD Bounded Domain

## What this branch is
Geometry-sensitive CFD lane separating periodic exactness from bounded-domain failure/obstruction behavior.

## Strongest results
- Exact periodic incompressible projection on supported classes.
- Bounded-domain transplantation failures and compatibility limits.
- Clear separation between projection success and domain-structure obstruction.

## Canonical documents
- [Incompressible projection](../../docs/cfd/incompressible-projection.md)
- [Bounded vs periodic projection](../../docs/cfd/bounded-vs-periodic-projection.md)
- [Helmholtz-Hodge velocity projection](../../docs/cfd/helmholtz-hodge-velocity-projection.md)
- [CFD projection theorem results](../../docs/theorem-candidates/cfd-projection-results.md)
- [Bounded-domain projection limits](../../docs/physics/bounded-domain-projection-limits.md)

## Key tests / artifacts
- `tests/math/test_cfd_projection.py`
- `data/generated/cfd/`

## Open items
- Extend bounded-domain compatibility characterization beyond current branch assumptions.

## Shared infrastructure
CFD branch uses the shared theorem/no-go and validation toolchain.
