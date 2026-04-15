# Structural Discovery Studio

## Purpose

The Structural Discovery Studio is the main diagnosis and redesign surface in the repository.

It starts from a concrete system family and answers:

- what is protected
- what current record or architecture is being used
- why exact recovery fails or partially fails
- what weaker target is still recoverable
- what minimal supported fix should be tried next
- whether that fix actually changes the regime
- how strong the current evidence level actually is

## Main Workflow

1. Choose a validated demo scenario or configure a system manually.
2. Inspect the regime badge, blocker, and missing-structure panel.
3. Read the minimal-fix and redesign cards.
4. Apply a supported recommendation inside the studio.
5. Compare before versus after.
6. Export JSON, CSV, figure, report, or share link.

## Supported In-Studio Repair Patterns

- raise periodic cutoff on the tested modal family
- increase finite history on the tested diagonal control family
- weaken a stronger qubit target to a weaker exact one
- add candidate-library measurement rows on the restricted-linear template
- replace the bounded-domain periodic-projector transplant with the boundary-compatible finite-mode Hodge architecture

## Guided Versus Diagnostic Modes

`guided diagnosis` prioritizes:

- blocker summary
- missing structure
- next-step recommendations
- before/after repair evidence

`raw diagnostics` keeps the same computation but emphasizes:

- collapse values
- support / history / row-space diagnostics
- threshold series
- raw numerical outputs

## Export Paths

The studio now supports:

- share links
- JSON export
- CSV series export where relevant
- Markdown report export
- figure export

## Provenance Rule

Every recommendation shown in the studio is tagged as one of:

- theorem-backed
- restricted exact theorem-backed
- family-specific validated result
- benchmark-guided empirical result
- standard guidance outside the current theorem spine

That evidence split is part of the feature, not a disclaimer after the fact.
