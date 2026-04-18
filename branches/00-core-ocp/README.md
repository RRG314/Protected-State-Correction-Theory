# Branch 00 — Core OCP

This branch contains the program’s foundational structure: exact correction anchors, asymptotic generator anchors, and the core no-go constraints that keep later branches scoped.

The central objects are a protected component, a disturbance component, and a correction map. In the exact finite-dimensional setting, correction is modeled by projector structure; in continuous settings, asymptotic suppression is modeled by generator structure. The branch is intentionally minimal, because these are the claims that every other branch inherits.

The strongest current references are `docs/finalization/architecture-final.md`, `docs/finalization/theorem-spine-final.md`, and `docs/finalization/no-go-spine-final.md`, together with `papers/ocp_core_paper.md`.

Use this branch first when you need the baseline theorem language and status labels before moving into recoverability, augmentation, or physics extensions.
