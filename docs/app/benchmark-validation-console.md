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
