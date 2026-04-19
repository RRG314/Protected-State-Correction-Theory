# Soliton Branch Claim Registry (OCP Integration Layer)

Date: 2026-04-17

## Scope

This registry tracks only OCP-integrated soliton-branch claims. IDs are local to this branch and do not alter existing OCP theorem IDs.

| ID | Claim | Status | Evidence type | Primary artifacts | Scope limitations |
| --- | --- | --- | --- | --- | --- |
| SOL-OCP-001 | Symmetry non-identifiability no-go under `G`-invariant observations | PROVED | formal argument + stress check | `theorem_candidates.md`, `proof_or_disproof_notes.md` (companion repo) | Restricted one-soliton manifold setup. |
| SOL-OCP-002 | Quotient recoverability formulation for fixed-time one-soliton family | PROVED (formalism) | definition-level formalization | `formalism.md` | Not a uniqueness theorem by itself. |
| SOL-OCP-003 | Injectivity of `local_complex_2` on quotient `(eta,v)` | CONDITIONAL + VALIDATED | exhaustive finite-grid scan | `observation_collision_summary.csv` | Continuous-domain theorem open. |
| SOL-OCP-004 | Injectivity of `fourier_magnitudes_4` on quotient `(eta,v)` | CONDITIONAL + VALIDATED | exhaustive finite-grid scan | `observation_collision_summary.csv` | Continuous-domain theorem open; sample design dependence. |
| SOL-OCP-005 | Same-count opposite verdict (dimension-4 witness) | VALIDATED + CONDITIONAL | explicit witness + exhaustive scan | `same_count_opposite_verdict.json` | Finite tested family only. |
| SOL-OCP-006 | Magnitude-only noninjectivity creates nonzero ambiguity floor at zero noise | PROVED ON SUPPORTED FAMILY + VALIDATED | structural argument + noise scan | `noise_ambiguity_scan.csv`, `observation_collision_witnesses.json` | Promoted only for declared magnitude-only fixed-time class. |
| SOL-OCP-007 | Lowpass reduction near-preserves single soliton while subsample-interp fails | VALIDATED + CONDITIONAL | explicit projection benchmark | `projection_preservation_summary.csv` | NLS class and tested operators only. |
| SOL-OCP-008 | Split-step baseline is structure-preserving vs forward Euler baseline drift | VALIDATED | baseline numerical comparison | `integrator_baseline_comparison.csv` | Numerical benchmark result, not theorem. |
| SOL-OCP-009 | Direct linear minimal-augmentation transfer to nonlinear soliton branch | DISPROVED (as immediate transfer) | explicit bridge rejection | `docs/research-program/soliton-geometry-discovery-2026-04-16/optional_existing_repo_bridge.md` | Could re-enter only with new nonlinear replacement theorem. |
| SOL-OCP-010 | Broad soliton-to-OCP universal bridge | ANALOGY ONLY | falsification audit | `stress_test_report.md`, `novelty_positioning.md` | Not promotable at present. |
