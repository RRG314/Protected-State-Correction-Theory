# Structured Mixer Guide

## Purpose

Structured mode is the safest and most interpretable way to use the Discovery Mixer.
It limits the user to families already represented in the repository and therefore exposes the strongest current structural logic.

## Workflow

1. choose a family
2. choose the protected target
3. choose the observation or architecture
4. set the complexity or threshold parameter
5. inspect the regime verdict
6. inspect the structural blocker
7. apply a supported recommendation
8. compare before versus after

## Family-Specific Guidance

### Restricted-linear family

Use this when you want theorem-backed analysis of:

- exact recoverability
- row-space insufficiency
- same-rank ambiguity
- minimal augmentation count
- candidate measurement additions

Typical question:
- which extra observation row do I need to recover this protected functional exactly?

### Periodic modal family

Use this when the issue is hidden modal support.

Typical question:
- is the current cutoff too small for the protected modal functional?

### Diagonal/history family

Use this when the issue is finite-history insufficiency.

Typical question:
- how much observation horizon is needed for this functional?

### Bounded-domain family

Use this when the issue is not missing measurement count but wrong architecture.

Typical question:
- is this periodic transplant invalid on the bounded-domain protected class, and is there a boundary-compatible replacement?

## Reading The Verdict

The key outcomes are:

- `exact`: current structure supports the requested target as configured
- `approximate`: a weaker or quantitative recovery story is available, but exactness is not promoted
- `asymptotic`: the current architecture is better treated as observer-like or damping-like rather than exact
- `impossible`: the current target cannot be recovered on the chosen admissible family under the current record or architecture
- `unsupported`: the requested setup lies outside the validated engine scope

## Using Recommendation Cards

Each recommendation card explains:

- what to change
- why that change matters structurally
- what evidence level supports it
- whether the fix is testable directly in the studio

If a recommendation is marked as testable in the studio, the `Apply and compare` action updates the composition and re-runs the analysis.
