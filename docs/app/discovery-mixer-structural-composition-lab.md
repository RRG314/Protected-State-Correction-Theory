# Discovery Mixer / Structural Composition Lab

## Purpose

The Discovery Mixer is the advanced composition surface in the workbench.

It lets a user assemble supported system families, targets, records, and correction architectures, then asks:

- is this composition coherent?
- is the requested target compatible with the current record?
- what regime does the current setup support?
- what exact structure is missing?
- what is the smallest supported change that repairs it?

## Main Workflow

1. Choose mixer mode: structured, controlled custom input, random exploration, or demo.
2. Build the composition using supported family-specific controls.
3. Inspect the regime badge and compatibility diagnostics.
4. Read the root-cause and missing-structure panels.
5. Apply a supported recommendation when one is available.
6. Compare before versus after.
7. Export a report, JSON payload, or CSV summary.

## What Makes It Different From The Structural Discovery Studio

The Structural Discovery Studio starts from a prepared scenario family and routes the user toward diagnosis and repair.

The Discovery Mixer starts one level earlier.
It lets the user compose the objects themselves, including supported custom matrices and symbolic-linear functionals, and then asks whether the composition is valid before moving to redesign.

## Scope Discipline

The mixer is intentionally typed.
It does not claim general symbolic-math support.
Unsupported or mixed-family custom input is rejected explicitly.
