# Benchmark / Validation Console

## Purpose

The Benchmark / Validation Console is the workbench surface for:

- replaying validated repair demos
- checking branch health at a glance
- exporting reproducible snapshots
- keeping the product surface tied to real evidence instead of memory or screenshots

## What It Shows

- built-in repair demos with before/after regime changes
- selected demo details
- module-health benchmark rows
- summary counts for demo coverage and successful regime changes
- report and CSV export hooks
- a direct path to the repo’s dedicated tool-qualification and known-results report

## Linked Qualification Layer

The console is now tied to a separate qualification pass:

- [Tool Qualification And Known-Results Verification Report](tool-qualification-report.md)
- [Professional Validation And Discovery Report](professional-validation-report.md)

That report checks:

- whether the tool itself behaves correctly in real workflows
- whether the tool reproduces known expected results
- whether export, share-state, and reload flows preserve the same conclusion
- whether the workbench is safe for guided discovery inside supported families
- where the validation layer is strong, partial, or circular
- which known-answer, adversarial, and workflow cases currently pass

## Current Demo Set

- Periodic modal augmentation
- Control/history augmentation
- Weaker-versus-stronger target split
- Boundary architecture repair
- Restricted-linear measurement repair

## Why It Exists

The workbench now includes real diagnosis and redesign logic. That makes a benchmark surface necessary.

Without a benchmark console, it becomes too easy for the UI to drift away from:

- theorem-backed logic
- generated artifacts
- reproducibility expectations
- branch-level validation status

## Scope

This console is a workbench-facing validation layer.
It is not a replacement for the full repository test gate.
