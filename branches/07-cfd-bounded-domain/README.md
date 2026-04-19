# Branch 07 - CFD Bounded Domain

This branch studies projection-based recoverability in CFD with explicit separation between periodic and bounded domains. The distinction matters because boundary structure changes the protected class.

The periodic/Helmholtz lane gives exact projector behavior under compatible assumptions. The bounded-domain/Hodge lane includes both positive supported-family results and sharp failure boundaries when periodic logic is transplanted naively.

Canonical references are `docs/cfd/incompressible-projection.md`, `helmholtz-hodge-velocity-projection.md`, `bounded-vs-periodic-projection.md`, and `docs/theorem-candidates/cfd-projection-results.md`.

This branch is a primary example of geometry-sensitive recoverability: same information amount can still produce opposite outcomes when domain structure changes.
