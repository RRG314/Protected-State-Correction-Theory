# Rewrite-Needed Assessment

Date: 2026-04-19

## Decision

A larger architecture rewrite is recommended before additional broad content expansion.

This is not because theorem content is absent; it is because theorem content, methods content, exploratory content, and historical pass logs are interleaved in a way that creates persistent claim-scope risk.

## Why local edits alone are no longer enough

1. Too many parallel master reports with overlapping authority.
2. Known-backbone and restricted-novel claims are distributed across many folders and eras.
3. Citation-corrected language now exists in key files, but repo-wide consistency cannot be guaranteed without structural separation.
4. Methods/diagnostics and theorem-core artifacts are mixed in neighboring paths.

## Recommended target architecture

### A) `docs/theorem-core/`
- only formal statements, assumptions, status labels, proof sketches, and theorem dependencies.
- mandatory known-overlap notes at theorem entry level.

### B) `docs/methods-diagnostics/`
- anti-classifier metrics, harness definitions, ablations, and benchmarking protocols.
- explicit non-theorem labeling by default.

### C) `docs/physics-translation/`
- theorem-grade mappings vs validated surrogate mappings vs analogy-only maps in separate files.

### D) `docs/research-program/structural-information-theory/`
- keep as active synthesis lane only if every claim links to theorem-core or methods artifact.

### E) `docs/archive/structured-passes/`
- move one-off exploratory or superseded pass reports here to reduce authority confusion.

## Paper lane split recommendation

1. Paper A (strongest now): restricted no-go + diagnostics benchmark paper.
2. Paper B: restricted perturbation stability theorem note.
3. Paper C (only later): broader synthesis, after theorem-core and methods lanes are fully separated.

## Stop condition used in this pass

After urgent citation correction and core MP closure, no additional broad structural-content expansion was performed.
Further expansion should follow the architecture rewrite plan above.
