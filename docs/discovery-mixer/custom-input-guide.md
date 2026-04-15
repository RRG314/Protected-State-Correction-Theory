# Controlled Custom Input Guide

## Purpose

Custom input mode allows a user to go beyond built-in presets without pretending to support arbitrary symbolic mathematics.

The rule is simple:
- custom input is accepted only when it can be reduced to a supported typed family
- otherwise the system rejects it explicitly

## Supported Custom Input Forms

### Linear custom input

Use variable names `x1..xn`.

Examples of accepted expressions:
- `x1`
- `x2 + x3`
- `2*x1 - x3`

Examples of rejected expressions:
- `sin(x2)`
- `x1*x2`
- `x5` when the declared dimension is `3`
- constant offsets such as `x1 + 1`

### Periodic custom input

Use basis variables `a1..a4`.

Examples of accepted expressions:
- `a1 + a2 + a4`
- `2*a4 - a1`

Rejected examples:
- `a5`
- `sin(a1)`
- `a1*a2`

### Control custom input

Use sensor-profile rows and protected targets reducible to the tracked diagonal family.

Accepted targets include:
- `x3`
- `moment(2)`
- supported linear combinations in `x1..xn`

## Failure Messages Matter

If custom input fails, the mixer should never stop at “invalid input.”
It should say whether the issue is:

- unsupported syntax
- nonlinear structure
- undeclared variable
- basis mismatch
- dimension mismatch
- unsupported family reduction

## Interpretation Rule

Accepted custom input is not automatically broad theorem support.
It only means the custom input has been reduced into a family the engine already knows how to analyze.
