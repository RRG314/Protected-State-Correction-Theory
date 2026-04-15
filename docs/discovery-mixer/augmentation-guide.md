# Discovery Mixer Augmentation Guide

## Purpose

The augmentation layer answers:
- what exact structure is missing?
- what is the smallest supported change that repairs the task?

## Supported Augmentation Types

- add measurement / observation row
- add retained mode or raise cutoff
- extend history horizon
- switch architecture
- weaken target
- restrict admissible family

## Ranking Logic

Recommendations are ranked using the strongest available structural information, including:

- smallest structural change
- expected regime improvement
- theorem-backed certainty when available
- interpretability of the change
- whether the fix can be tested directly in the studio

## Exact Count Versus Best-Effort Search

### Exact where theorem-backed

The mixer can return exact minimal augmentation counts on the restricted-linear branch where the repo already has a proved minimal augmentation theorem.

### Best-effort where family-specific

The mixer can also return family-specific repairs such as cutoff increases or horizon extensions on tracked finite families.
Those are validated on the family, but not promoted as universal redesign laws.

## Before / After Rule

A recommendation should not be treated as successful until the mixer applies the change and re-runs the analysis.
