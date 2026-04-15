# Protected-State Correction Workbench Overview

## What It Is

The Protected-State Correction Workbench is a static scientific tool tied directly to the repository's theorem, no-go, and design layers.

It is not a detached visualization layer.
Each module is kept only if it maps to a proved result, a disciplined conditional lane, or an explicit rejection decision.

## Modules
- Recoverability / Correction Studio
- Exact Projection Lab
- QEC Sector Lab
- MHD Projection Lab
- CFD Projection Lab
- Gauge Projection Lab
- Continuous Generator Lab
- No-Go Explorer

## What It Can Do
- inspect exact projector recovery and overlap failure
- inspect sector-based exact recovery in the 3-qubit bit-flip anchor
- compare exact periodic projection with asymptotic GLM cleaning
- inspect periodic incompressible projection versus bounded-domain limits
- inspect invariant-split generator behavior and mixing failure
- inspect explicit no-go witnesses
- classify recoverability as exact, approximate, asymptotic, or impossible under constrained observation
- suggest next steps when recovery fails
- save scenarios, reload them, export JSON, export figures, and share state links

## Recoverability / Correction Studio Highlights

This is now the main product-like surface in the repo.

It supports:
- analytic conditioning / lower-bound checks
- fixed-basis qubit phase-loss checks
- periodic incompressible cutoff and protected-support thresholds
- finite-history versus observer routing in the control lane
- reusable linear design templates with minimal-augmentation suggestions

It exposes actual decision outputs:
- `κ(0)` and selected `κ(δ)`
- exact / approximate / asymptotic / impossible classification
- blocker and missing-structure summaries
- weaker recoverable targets where available
- minimal added measurements for the restricted-linear template
- no-go labels when a naive design is blocked

## What It Is For
- deciding whether a current record is sufficient
- identifying why recovery fails
- choosing between exact static recovery and observer-style recovery
- finding a minimal record upgrade on restricted linear families
- locating threshold behavior on the tested periodic and control families
- generating reusable scenarios before moving into the proof documents or code

## What It Is Not For
- replacing the proofs
- claiming new theorems where the repo only offers a family-level example
- making conditional or rejected bridges look stronger than they are
- pretending every module has a meaningful time-history animation when the underlying result is static
