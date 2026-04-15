# Structural Discovery

Structural Discovery is the repo's failure-analysis, redesign, and evidence-export layer.

It answers a practical question that the theorem spine alone does not answer in a user-facing way:

1. What is the protected object?
2. Why does the current record or correction architecture fail?
3. What exact structure is missing?
4. What is the smallest meaningful change that can repair the failure?
5. Does that change actually move the example into a better regime?
6. What evidence level supports the current recommendation?

The capability is built on top of the constrained-observation recoverability branch, the restricted-linear design branch, the periodic and control threshold results, the bounded-domain architecture results, and the repo's no-go layer.

## What It Does

Structural Discovery combines five layers:

- Problem specification: admissible family, protected variable, observation map, and current architecture.
- Failure analysis: exact failure, threshold failure, weaker-vs-stronger split, no-go triggers, and architecture mismatch.
- Discovery: missing support, missing history, missing row-space coverage, hidden direction, or incompatible boundary structure.
- Recommendation: augment the record, weaken the target, switch record family, or switch architecture.
- Validation: compare the current setup to the recommended setup and record the regime change.

## What Is Theorem-Backed Or Strongly Linked

- restricted-linear exactness and minimal augmentation logic
- restricted-linear nullspace / row-space insufficiency detection
- periodic protected-support threshold results on the tested finite modal family
- diagonal finite-history threshold results on the tested scalar-output family
- weaker-vs-stronger target split in the fixed-basis qubit toy model
- divergence-only no-go and related record-insufficiency witnesses
- bounded-domain projector-transplant failure
- restricted exact bounded-domain Hodge-compatible repair path on the finite-mode family

Heuristic or standard-but-not-proved-in-repo parts are explicitly marked in the studio and docs.

## Main Outputs

- generated summary: `data/generated/structural_discovery/structural_discovery_summary.json`
- demo table: `data/generated/structural_discovery/structural_discovery_demo_table.csv`
- before/after figure: `docs/assets/structural-discovery/structural-discovery-before-after.svg`
- workbench surfaces:
  - Structural Discovery Studio
  - Benchmark / Validation Console

## Relationship To The Theory Program

Structural Discovery is a subsystem, not a universal theory claim.

What it contributes:

- a practical way to use the repo's strongest recoverability results
- an explicit failure-to-repair workflow
- a reusable way to compare stronger and weaker protected targets
- a bridge between theorem-backed branch results and engineering decisions
- exportable evidence snapshots that preserve status and provenance

What it does not claim:

- a universal augmentation law across all systems
- a complete automated theorem prover for new architectures
- exact minimal augmentation beyond the branches where the repo has clean formulas or validated finite searches

## Main Entry Points

- [Formalism](formalism.md)
- [Algorithms](algorithms.md)
- [Theorem / no-go linkage](theorem-linkage.md)
- [Quickstart](quickstart.md)
- [Demo walkthroughs](demo-walkthroughs.md)
- [Export guide](export-guide.md)
- [Developer reference](developer-reference.md)
- [Validation](validation.md)
