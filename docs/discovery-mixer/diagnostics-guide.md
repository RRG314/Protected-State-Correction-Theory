# Discovery Mixer Diagnostics Guide

## Diagnostic Classes

The mixer diagnostics are organized around structural causes rather than generic errors.

Main classes:

- compatibility failure
- recoverability failure
- threshold insufficiency
- architecture mismatch
- target-strength mismatch
- unsupported input reduction

## Severity Levels

- `success`: current structure supports the requested task
- `info`: explanatory structural detail
- `warning`: the current setup is coherent but structurally insufficient or only partially supported
- `error`: exact failure, impossibility, or unsupported composition

## Common Structural Causes

### Collision or fiber failure

Interpretation:
- the record does not separate the protected target on the admissible family

Typical fix:
- add measurements
- weaken the target
- restrict the admissible family

### Support or cutoff failure

Interpretation:
- the protected functional depends on modal content not present in the retained record

Typical fix:
- raise the cutoff
- choose a lower-support target

### History insufficiency

Interpretation:
- the finite observation horizon is shorter than the supported threshold for the chosen functional

Typical fix:
- extend horizon
- switch to observer/asymptotic architecture

### Boundary incompatibility

Interpretation:
- the chosen exact architecture is incompatible with the bounded protected class even if it works on the periodic branch

Typical fix:
- swap to a boundary-compatible architecture

### Unsupported custom reduction

Interpretation:
- the user input cannot be reduced into a supported typed family

Typical fix:
- restate the problem using a supported linear, modal, or diagonal template

## Credibility Rule

Diagnostics should always match the strongest available evidence class.
A theorem-backed obstruction should not be described as a heuristic guess, and a heuristic redesign hint should not be described as a theorem.
