# Branch 00 — Core OCP

## What this branch is
Canonical theorem-first backbone for the Orthogonal Correction Principle (OCP): exact projection structure, asymptotic correction architecture, and core impossibility boundaries.

## Strongest results
- Exact orthogonal projection recovery on protected/disturbance splits.
- Core no-go when protected and disturbance structure overlap.
- Formal exact-vs-asymptotic separation.

## Canonical documents
- [Start Here](../../docs/overview/start-here.md)
- [Architecture (final)](../../docs/finalization/architecture-final.md)
- [Theorem spine (final)](../../docs/finalization/theorem-spine-final.md)
- [No-go spine (final)](../../docs/finalization/no-go-spine-final.md)
- [Core companion paper](../../papers/ocp_core_paper.md)

## Key tests / artifacts
- `tests/math/test_core_projectors.py`
- `tests/math/test_continuous_generators.py`
- `tests/math/test_capacity.py`

## Open items
- Keep core statements minimal and branch-stable; avoid universal extension claims without branch-specific proof.

## Shared infrastructure
Code, tests, scripts, and generated artifacts remain centralized in `src/`, `tests/`, `scripts/`, and `data/generated/`.
