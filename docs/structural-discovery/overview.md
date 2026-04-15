# Structural Discovery

Structural Discovery is the repo's failure-analysis and redesign layer.

It answers a practical question that the theorem spine alone does not answer in a user-facing way:

1. What is the protected object?
2. Why does the current record or correction architecture fail?
3. What exact structure is missing?
4. What is the smallest meaningful change that can repair the failure?
5. Does that change actually move the example into a better regime?

The capability is built on top of the constrained-observation recoverability branch, the restricted-linear design branch, the periodic and control threshold results, and the repo's no-go layer.

## What It Does

Structural Discovery combines five layers:

- Problem specification: admissible family, protected variable, observation map, and current architecture.
- Failure analysis: exact failure, threshold failure, weaker-vs-stronger split, and explicit no-go triggers.
- Discovery: missing support, missing history, missing row-space coverage, hidden direction, or incompatible architecture.
- Recommendation: augment the record, weaken the target, switch record family, or switch from exact to asymptotic design.
- Validation: compare the current setup to the recommended setup and record the regime change.

## What Is Theorem-Backed

The Structural Discovery engine is not a separate theory. It is a practical layer built on theorem-backed or experiment-backed branch results already present in the repo.

Theorem-backed or theorem-linked parts:

- restricted-linear exactness and minimal augmentation logic
- restricted-linear nullspace / row-space insufficiency detection
- periodic protected-support threshold results on the tested finite modal family
- diagonal finite-history threshold results on the tested scalar-output family
- weaker-vs-stronger target split in the fixed-basis qubit toy model
- divergence-only no-go and related record-insufficiency witnesses

Heuristic or standard-but-not-proved-in-repo parts are explicitly marked in the studio and docs.

## Main Outputs

- generated summary: `data/generated/structural_discovery/structural_discovery_summary.json`
- demo table: `data/generated/structural_discovery/structural_discovery_demo_table.csv`
- before/after figure: `docs/assets/structural-discovery/structural-discovery-before-after.svg`
- workbench surface: `docs/workbench/` via the Structural Discovery Studio

## Relationship To The Theory Program

Structural Discovery is a subsystem, not a universal theory claim.

What it contributes:

- a practical way to use the repo's strongest recoverability results
- an explicit failure-to-repair workflow
- a reusable way to compare stronger and weaker protected targets
- a bridge between theorem-backed branch results and design decisions

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
- [Developer reference](developer-reference.md)
- [Validation](validation.md)
