# Protected-State Correction Workbench Overview

## What It Is

The Protected-State Correction Workbench is a static, theorem-linked research and engineering surface for:

- exact protected-state correction
- asymptotic redesign
- explicit no-go inspection
- constrained-observation recoverability
- structural failure diagnosis
- typed structural composition
- minimal supported augmentation
- before/after validation
- benchmark-driven reproducibility

It is not a detached visualization layer.
Each module is kept only if it corresponds to a proved theorem, a sharp no-go, a validated family-specific result, a disciplined conditional lane, or a real benchmark surface.

## Main Entry Paths

The workbench now has a task-first front door:

- discover missing structure
- compose a supported system
- test recoverability
- compare exact versus asymptotic correction
- inspect no-go boundaries
- run built-in benchmarks
- open reusable templates

This is meant to reduce friction for serious non-expert users without hiding the theorem layer from expert users.

## Modules

- Structural Discovery Studio
- Discovery Mixer / Structural Composition Lab
- Benchmark / Validation Console
- Exact Projection Lab
- QEC Sector Lab
- MHD Projection Lab
- CFD Projection Lab
- Gauge Projection Lab
- Continuous Generator Lab
- No-Go Explorer

## Structural Discovery Studio

This is the main diagnosis-and-redesign surface.

It now supports:

- analytic conditioning / lower-bound checks
- fixed-basis qubit weaker-versus-stronger target analysis
- periodic support-threshold diagnosis and repair
- diagonal finite-history diagnosis and repair
- restricted-linear minimal augmentation logic
- bounded-domain architecture diagnosis
- before/after comparisons tied to theorem, no-go, or family-specific status
- JSON, CSV, figure, report, and share-link export

## Discovery Mixer / Structural Composition Lab

This is the advanced composition-and-diagnostics surface.

It now supports:

- structured composition across restricted-linear, periodic modal, diagonal/history, and bounded-domain benchmark families
- controlled custom matrix and symbolic-linear input inside supported classes only
- immediate compatibility diagnostics on typed objects
- structural verdicts for exact, approximate, asymptotic, impossible, and unsupported cases
- missing-structure detection and ranked augmentation or redesign cards
- seeded constrained random exploration with replayable cases
- before/after repair comparison and exportable evidence

The mixer is intentionally narrow.
Its value comes from making supported families composable without pretending to solve arbitrary symbolic problems.

## Benchmark / Validation Console

This is the trust surface for the workbench.

It exposes:

- validated built-in repair demos
- module-health benchmark rows
- reproducibility-oriented scenario selection
- exportable benchmark snapshots
- a clear split between theorem-backed, family-specific, and benchmark-guided surfaces

Its qualification layer now also has a dedicated report:

- [Tool Qualification And Known-Results Verification Report](tool-qualification-report.md)
- [Professional Validation And Discovery Report](professional-validation-report.md)

That report keeps three things separate on purpose:

- tool qualification
- known-result reproduction against expected answers
- post-qualification discovery use

## What The Workbench Can Do

- classify a setup as exact, approximate, asymptotic, or impossible
- classify a composition as exact, approximate, asymptotic, impossible, or unsupported
- identify structural blockers
- identify weaker targets that already survive
- compute theorem-backed minimal augmentation counts where available
- propose supported redesigns
- apply supported redesigns in the studio
- compare failing and repaired setups side by side
- export evidence snapshots with provenance metadata

## What It Does Not Claim

- universal augmentation laws across arbitrary systems
- exact minimal redesign outside the branches where the repo has a proved criterion or validated finite search
- broad bounded-domain exactness beyond the restricted compatible families already documented
- theorem status for every engineering suggestion shown in the UI

## Evidence Levels In The UI

Every promoted output should be read as one of:

- theorem-backed
- restricted exact theorem-backed
- family-specific validated result
- benchmark-guided empirical result
- standard guidance outside the current theorem spine

That evidence split is part of the feature, not an after-the-fact disclaimer.


## Architecture And Extension Docs

- [Workbench Architecture](workbench-architecture.md)
- [Workbench Data Flow](workbench-data-flow.md)
- [Workbench Extension Guide](workbench-extension-guide.md)
- [Workbench Export Plumbing](workbench-export-plumbing.md)
- [Workbench Validation Map](workbench-validation-map.md)
- [Workbench Refactor Report](workbench-refactor-report.md)
- [Workbench Refactor System Check](workbench-system-check-report.md)
