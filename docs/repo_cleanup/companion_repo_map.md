# Companion Repository Map

Date: 2026-04-17

## Purpose

Clarify what stays in this repository and what belongs in companion programs.

## Ecosystem Map

| Program | Home | Why separate | How it connects | When to go there |
| --- | --- | --- | --- | --- |
| OCP / Protected-State Correction Theory (this repo) | <https://github.com/RRG314/Protected-State-Correction-Theory> | Core theorem/no-go/recoverability framework + workbench | Canonical theory and integration hub | Start here for theory, workbench, and paper set |
| Soliton geometry research | <https://github.com/RRG314/soliton-geometry-research> | Nonlinear-wave discovery and self-organization are primary there | OCP keeps only bounded overlap branch | Go there for direct soliton experiments/anomalies/theorem attempts |
| MHD closure research | <https://github.com/RRG314/MagnetoHydroDynamic-research> | Domain-specific Euler-potential closure/obstruction development | OCP tracks aligned bridge/paper artifacts | Go there for direct MHD implementation and domain-deep material |
| CFD companion lane | companion lane currently referenced without a stable public URL in this repo | Boundary/projection domain program may evolve independently | OCP keeps bridge-layer conclusions only | Use OCP bridge docs unless/ until public CFD repo URL is declared |
| SDS / Structural Discovery tooling layer | in this repo (`docs/workbench/`, `docs/app/`, `src/ocp/*`) | Integrated product layer tied to OCP formalism | Implements theorem-linked diagnostics and repair workflows | Stay in this repo for SDS/workbench usage |

## Boundary Rules

1. Do not duplicate full nonlinear discovery outputs into OCP.
2. Do not treat companion repository results as OCP-core theorems without explicit branch admission.
3. Keep cross-links explicit in availability sections and integration docs.

## Canonical Cross-References

- `docs/integration/repo_scope_statement.md`
- `docs/integration/cross_repo_audit.md`
- `docs/soliton-branch/final_branch_decision.md`
