# Protected-State Correction Workbench Overview

## What the Workbench Is For

The workbench is the repository’s operational layer: it translates theorem and no-go structure into concrete decisions about architecture choice, recoverability, and redesign. It is designed for disciplined use, not broad symbolic exploration. Every module is expected to map to one of four evidence types: proved theorem behavior, proved no-go behavior, validated family-specific behavior, or explicitly conditional comparison behavior.

## How to Use It

Most users should start with the same sequence:

1. define the protected target and available record,
2. run diagnosis to identify structural blockers,
3. compare exact, asymptotic, and impossible regimes,
4. test a supported redesign,
5. export evidence for reproducibility.

This flow is implemented across three linked surfaces rather than one monolithic dashboard.

## Core Surfaces and Their Roles

### Structural Discovery Studio
The studio is the diagnosis-and-repair surface. It explains *why* a configuration fails, not just that it fails. It can surface missing structure, suggest supported fixes, and compare before/after outcomes using theorem-backed or validated branch logic.

### Discovery Mixer / Structural Composition Lab
The mixer is the composition surface. It lets users construct supported systems from typed components and immediately checks compatibility, support boundaries, and branch status. It is intentionally narrow: unsupported symbolic or mixed-family setups are rejected instead of being silently approximated.

### Benchmark / Validation Console
The benchmark console is the trust surface. It exposes known cases, module-health checks, and reproducible exports so users can distinguish stable, validated behavior from exploratory use.

## Relationship to the Theory

The workbench does not replace the theorem documents. It operationalizes them. The design principle is simple: if the repository does not have theorem or validated family support for a claim, the interface should not present that claim as solved.

## What the Workbench Does Not Claim

The workbench does not claim universal minimal redesign laws, universal bounded-domain exactness, or automatic theorem status for every suggested fix. It is a guided decision system tied to the repository’s explicit branch limits.

## Canonical Companion Docs

- [Module-theory map](module-theory-map.md)
- [Benchmark / Validation Console](benchmark-validation-console.md)
- [Tool Qualification And Known-Results Verification Report](tool-qualification-report.md)
- [Professional Validation And Discovery Report](professional-validation-report.md)
- [Workbench Architecture](workbench-architecture.md)
