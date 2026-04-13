# Contributing Paths

This repository supports contributions, but it is structured around proof status and scope control. The easiest way to contribute well is to enter through one of the established lanes below.

## 1. Theorem and Proof Lane

Best for contributors who want to:

- tighten theorem statements
- make assumptions explicit
- close proof gaps
- sharpen lemmas and corollaries
- improve notation consistency

Best entry files:

1. [architecture-final.md](../finalization/architecture-final.md)
2. [theorem-spine-final.md](../finalization/theorem-spine-final.md)
3. [claim-registry.md](claim-registry.md)
4. [proof-status-map.md](proof-status-map.md)

Good contribution shape:

- one theorem or proposition at a time
- one precise change in scope or proof status
- direct explanation of what became stronger, narrower, or clearer

## 2. No-Go and Falsification Lane

Best for contributors who want to:

- add counterexamples
- sharpen impossibility statements
- show why a tempting bridge fails
- reduce overreach in existing language

Best entry files:

1. [no-go-spine-final.md](../finalization/no-go-spine-final.md)
2. [advanced-no-go-results.md](../impossibility-results/advanced-no-go-results.md)
3. [dead-ends-and-do-not-promote.md](../open-questions/dead-ends-and-do-not-promote.md)

This is one of the most valuable lanes in the repository. A clean rejection result is a strong contribution.

## 3. Physics and Application Lane

Best for contributors who want to test whether a known system really fits the framework.

Best entry files:

1. [physics-system-matrix.md](../physics/physics-system-matrix.md)
2. [cfd-system-matrix.md](../cfd/cfd-system-matrix.md)
3. [kept-vs-rejected-physics-bridges.md](../physics/kept-vs-rejected-physics-bridges.md)
4. [kept-vs-rejected-cfd-bridges.md](../cfd/kept-vs-rejected-cfd-bridges.md)

A strong contribution in this lane must answer:

- what is protected
- what is disturbance
- what is the correction operator
- exact, asymptotic, conditional, or rejected
- what is standard in the outside literature
- what this repo adds, if anything

## 4. Workbench Lane

Best for contributors who want to improve:

- interaction clarity
- state handling
- export behavior
- module explanations
- theorem-to-UI alignment

Best entry files:

1. [workbench-overview.md](../app/workbench-overview.md)
2. [module-theory-map.md](../app/module-theory-map.md)
3. [docs/workbench/index.html](../workbench/index.html)
4. [tests/consistency/workbench_static.test.mjs](../../tests/consistency/workbench_static.test.mjs)

Good workbench contributions make the theory easier to inspect without weakening precision.

## 5. Validation and Reproducibility Lane

Best for contributors who want to:

- add tests
- improve generated validation artifacts
- tighten regression safety
- make examples easier to reproduce

Best entry files:

1. [scripts/validate/run_all.sh](../../scripts/validate/run_all.sh)
2. [src/ocp](../../src/ocp)
3. [tests](../../tests)
4. [data/generated/validations](../../data/generated/validations)

## 6. Documentation and Reviewer Lane

Best for contributors who want to:

- improve readability for outside technical readers
- tighten reviewer-facing scope and novelty statements
- improve release notes and citation guidance
- fix pathing and reading order

Best entry files:

1. [README.md](../../README.md)
2. [how-to-read-this-repo.md](../peer_review/how-to-read-this-repo.md)
3. [what-this-theory-is.md](../peer_review/what-this-theory-is.md)
4. [novelty-and-limits-for-reviewers.md](../peer_review/novelty-and-limits-for-reviewers.md)

## Best Near-Term Contribution Targets

Right now the most useful contribution targets are:

1. sharpening branch-specific capacity language without drifting back into a universal scalar claim
2. improving boundary-sensitive continuous and bounded-domain projection handling
3. improving theorem-linked workbench clarity
4. tightening reviewer-facing proof status and scope documents

## Contribution Quality Standard

A contribution is especially helpful if it leaves the repository:

- more explicit about assumptions
- more honest about boundaries
- more reproducible
- easier for a technical outsider to review
- or more useful without becoming broader than the evidence supports
