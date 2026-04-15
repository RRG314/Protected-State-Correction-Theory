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

## Main Workflow

1. Choose a validated demo scenario or configure a system manually.
2. Inspect the failure analysis panel.
3. Read the minimal-fix cards.
4. Apply a recommendation inside the studio when the fix is supported locally.
5. Compare before versus after.
6. Export the scenario JSON or figure if the result is worth keeping.

## Supported In-Studio Repair Patterns

- raise periodic cutoff on the tested modal family
- increase finite history on the tested diagonal control family
- weaken a stronger qubit target to a weaker exact one
- add candidate-library measurement rows on the restricted-linear template

## Doc-Linked But Not Fully In-Studio Patterns

- richer qubit basis enrichment
- broader bounded-domain repair ideas outside the currently solved restricted subcases

These remain visible as guidance, but they are marked as outside the current theorem-backed or in-studio implementation layer.

## Provenance Rule

Every recommendation shown in the studio is tagged as one of:

- theorem-backed
- family-specific validated result
- empirical / benchmark-guided
- standard guidance outside the current theorem spine

That separation is part of the feature, not a disclaimer after the fact.
