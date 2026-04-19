# Data Layout and Evidence Policy

This file defines canonical evidence tiers.

## Canonical promoted evidence

These folders are used directly by theorem/status and validation workflows:
- `data/generated/unified-recoverability/`
- `data/generated/structural-information-theory/`

## Exploratory generated evidence

Exploratory and non-promoted outputs remain in other `data/generated/*` folders unless explicitly promoted in a theorem/status document.

## Imported evidence

External imports are preserved with provenance and are not promoted automatically:
- `data/imported/structural-information-theory/`

## Promotion rule

A generated artifact is promoted only when:
1. it is linked from a theorem/status or validation anchor, and
2. its scope/status label is explicit.

Otherwise it remains exploratory/supporting.
