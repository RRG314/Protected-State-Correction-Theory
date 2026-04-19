# Companion Repository Map

Date: 2026-04-17

This map clarifies how companion programs relate to this repository and when a reader should leave the OCP repo for domain-first development.

## Program boundaries

| Program | Primary home | Why separate | How it connects to this repo | When to use it |
| --- | --- | --- | --- | --- |
| OCP / Protected-State Correction Theory | <https://github.com/RRG314/Protected-State-Correction-Theory> | Core theorem/no-go/recoverability framework and theorem-linked workbench | Canonical integration hub | Start here for theory architecture, status map, and canonical papers |
| Soliton geometry research | <https://github.com/RRG314/soliton-geometry-research> | Nonlinear-wave discovery and self-organization are primary there | OCP keeps only bounded overlap claims with explicit status labels | Go there for direct soliton experiments, anomaly work, and soliton-first theorem attempts |
| MHD closure research | <https://github.com/RRG314/MagnetoHydroDynamic-research> | Domain-specific closure/obstruction development evolves independently | OCP keeps aligned bridge conclusions and references | Go there for domain-deep MHD modeling and implementation |
| CFD-focused extension lane | referenced in this repo; no stable standalone public repo declared here | Boundary/projection program may be split later | OCP keeps bridge-level bounded/periodic conclusions | Stay in OCP unless a dedicated CFD repo is published |
| SDS / structural discovery tooling | in this repo (`docs/workbench/`, `docs/app/`, `src/ocp/*`) | Tooling is tightly coupled to OCP theorem/status surfaces | Directly integrated | Stay here for workbench and reproducibility workflows |

## Integration rules

1. Companion results do not become OCP-core theorems without explicit branch-admission review.
2. Cross-repo references should state whether a claim is theorem-backed, validated, conditional, or companion-only.
3. Scope boundaries must remain visible in front-door docs.

## Canonical cross-reference docs

- `docs/integration/repo_scope_statement.md`
- `docs/integration/cross_repo_audit.md`
- `docs/meta-governance/internal/soliton-branch/final_branch_decision.md`
