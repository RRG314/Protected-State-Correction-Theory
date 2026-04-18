# Branch 06 — Invariants and Augmentation

This branch formalizes which invariants are exact, which are branch-limited quantitative diagnostics, and which collapse to existing core logic. It also develops augmentation-deficiency structure used for repair planning.

The stable core remains fiber/factorization and row-space/kernel compatibility. Additive value currently comes from context and augmentation quantities (`CID`, `delta_free`, `delta_C`) and descriptor-lift diagnostics (`DFMI`, `IDELB`, `CL`) on supported families.

Canonical references are `docs/research-program/invariant_formal_audit.md`, `invariant_theorem_spine_draft.md`, `invariant_no_go_spine_draft.md`, and `invariant_formalization_and_bh_placement_master_report.md`.

This branch is intentionally theorem-first and overlap-aware: if a candidate invariant is only renamed row-space/fiber logic, it is demoted.
