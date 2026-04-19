# Invariant Buildout Options

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

## Option A - Theorem Note (highest priority)

Target:
- Consolidate exact and supported-family invariant theorems into one invariant spine note.

Contents:
1. core exact pair: fiber/factorization + row-space criterion
2. context split theorem and CID zero-test
3. augmentation deficiency theorem (`delta_free`) and constrained no-go (`delta_C`)
4. descriptor anti-classifier lower-bound package (IDELB/DFMI/CL)

Readiness:
- `READY` for draft theorem note with strict scope labels.

## Option B - Quantitative Invariant Paper Candidate

Target:
- Publish a scoped quantitative package centered on CL + `delta_C` + context-gap anomalies.

Needs before submission:
1. tighter literature-difference statements
2. explicit confidence/robustness intervals across randomized families
3. one benchmark beyond synthetic generators

Readiness:
- `CONDITIONAL`.

## Option C - Design Framework Module

Target:
- Invariant-driven design checklist for recoverability planning.

Proposed checks:
1. amount descriptor check (cheap, non-decisive)
2. compatibility/CID check
3. free-threshold estimate (`delta_free`)
4. candidate-library defect check (`delta_C`)
5. fragility stress checks (mismatch/enlargement/noise)

Readiness:
- `READY` as internal design framework.

## Option D - Workbench Diagnostic Layer

Target:
- Add invariant dashboard outputs (CID, context gap, CL, `delta_free`, `delta_C`, stress flags).

Readiness:
- `READY` for exploratory workbench lane.

Caution:
- keep labels explicit: `EXPLORATION / NON-PROMOTED`.

## Option E - Archive-only candidates

Candidates:
- broad alignment-only descriptors without additive theorem power
- unnormalized mixedness-depth variants without robustness study

Readiness:
- `ARCHIVE / HOLD`.

## Recommended buildout sequence

1. Theorem note (Option A)
2. Design framework module (Option C)
3. Workbench diagnostic layer (Option D)
4. Quantitative paper candidate after stronger robustness and literature positioning (Option B)
