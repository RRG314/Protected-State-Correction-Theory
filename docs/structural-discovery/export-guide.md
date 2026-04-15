# Structural Discovery Export Guide

The workbench now supports four export paths directly from the UI:

- share link
- JSON snapshot
- CSV series export where relevant
- Markdown report
- figure export

## Share Link

Use this when you want someone else to open the same workbench state directly.

## JSON Snapshot

Use this when you need:

- exact parameter replay
- raw analysis values
- scenario archiving
- downstream scripting

## CSV Export

Use this when you need the plotted series in tabular form.

Current supported CSV surfaces include:

- recoverability-collapse curves
- threshold series where available
- boundary architecture comparison series
- benchmark demo tables

## Report Export

Use this when you need a readable record of:

- current configuration
- evidence level
- blocker and missing structure
- recommendations
- before/after comparison
- reproducibility notes

## Figure Export

Use this for quick visual inclusion in notes, slides, or internal discussions.

## Interpretation Rule

Exports preserve the current workbench evidence split, but they do not upgrade the underlying status of a result.
A report that mentions a family-specific threshold remains family-specific.
