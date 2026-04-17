# Repository and Paper Naming Alignment Report

Date: 2026-04-16

## Objective
Ensure public-facing naming is consistent across paper titles, repository names, README labels, and code-availability statements.

## Canonical naming set

- Program label: `Protected-State Correction Theory` (OCP program)
- OCP repository: `Protected-State-Correction-Theory`
- MHD repository: `MagnetoHydroDynamic-research`
- Bridge/CFD local companion repo label: `cfd-research-program` (no public URL configured)

## Paper title alignment

- Recoverability paper:
  - Title: `Recoverability Under Constrained Observation: Fiber Factorization, Thresholds, and Minimal Augmentation`
  - Primary repo in paper: OCP repo
  - Alignment status: aligned

- OCP core paper:
  - Title: `On the Failure of Rank-Based Criteria for Exact Recovery in Restricted Linear Observation Systems`
  - Primary repo in paper: OCP repo
  - Alignment status: aligned

- Bridge paper:
  - Title: `Structure-Dependent Recoverability and Failure Modes in Projection-Based Correction Systems`
  - Primary repo in paper: OCP repo for release artifacts
  - CFD companion status: described as companion lane only, not listed as a public code URL
  - Alignment status: aligned

- MHD paper:
  - Title: `Exact Closure and Obstruction in Euler-Potential MHD Under Variable Resistivity`
  - Primary repo in paper: MHD repo
  - OCP repo listed as synchronized companion
  - Alignment status: aligned

## Author identity alignment

All release papers now use the same identity block:
- Author: Steven Reid
- Email: sreid1118@gmail.com
- Affiliation style: Independent Researcher (consistent across papers)

## Workbench reference alignment

- Workbench URL appears only in OCP-centered papers where it is directly relevant:
  - recoverability paper
  - OCP core paper
- Bridge and MHD papers avoid unnecessary workbench references.

## Remaining mismatch risks

1. CFD repo has no remote configured; avoid publishing/citing a non-public URL until remote is established.
2. If the OCP README/repo subtitle changes later, update paper code-availability text in lockstep.
