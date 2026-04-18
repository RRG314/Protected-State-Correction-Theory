# Protected-State Correction Theory

[![Release](https://img.shields.io/github/v/release/RRG314/Protected-State-Correction-Theory?display_name=tag)](https://github.com/RRG314/Protected-State-Correction-Theory/releases)
[![Workbench](https://img.shields.io/badge/Workbench-Live-0f8f82)](https://rrg314.github.io/Protected-State-Correction-Theory/docs/workbench/)
[![License: MIT](https://img.shields.io/badge/License-MIT-2f855a.svg)](LICENSE)

A theorem-first research program for **protected-state correction and constrained-observation recoverability**.

## What This Repository Is

This repository develops OCP (Orthogonal Correction Principle) as a formal framework for deciding when a protected object can be preserved or recovered in the presence of disturbance, ambiguity, or coarse observation. The work is organized around exact results, no-go results, and branch-limited extensions that are kept only when they remain mathematically honest.

OCP is the backbone, but it is not the entire story. The current program also includes constrained-observation recoverability, anti-classifier limits, bounded-domain obstruction analysis, and a theorem-linked workbench used for diagnosis, comparison, and reproducible validation.

## Program Structure

The program has a clear hierarchy.

- Foundation: exact projector/sector anchors, continuous asymptotic generator results, and the core no-go layer.
- Branch-limited strengthening: restricted-linear recoverability, anti-classifier/family-enlargement/mismatch theorems, and bounded-domain compatibility limits.
- Quantitative extraction: descriptor-fiber diagnostics on supported finite witness classes.
- Adjacent quantitative extensions: target-structured information diagnostics (TSIT) kept as exploration/non-promoted, with explicit overlap controls against core OCP/fiber math.
- Engineering surface: a workbench that exposes theorem-backed and validated branch behavior without claiming universal symbolic capability.

Current overall status remains branch-limited (`B`): the universal core is strong, but broader unification claims are not promoted.

## Where To Start

If you are new to the repository, start with these files in order:

1. [Start Here](docs/overview/start-here.md)
2. [Final Architecture](docs/finalization/architecture-final.md)
3. [Final Theorem Spine](docs/finalization/theorem-spine-final.md)
4. [Final No-Go Spine](docs/finalization/no-go-spine-final.md)
5. [Canonical Reading Paths](docs/repo_cleanup/canonical_reading_paths.md)

## Papers

The active paper set is:

- [Recoverability paper](papers/recoverability_paper_final.md)
- [OCP core companion](papers/ocp_core_paper.md)
- [Bridge paper](papers/bridge_paper.md)
- [MHD closure paper](papers/mhd_paper_upgraded.md)
- [Unifying framework paper](papers/unifying_theory_framework_final.md)
- [Descriptor-fiber anti-classifier branch paper](papers/descriptor-fiber-anti-classifier-branch.md)

## Adjacent Quantitative Extensions

The repository keeps one active adjacent extension lane for target-specific diagnostics where practical value survived falsification but core-theorem promotion did not.

- [TSIT quantitative extension (Option D, non-promoted)](docs/research-program/adjacent-directions/tsit_quantitative_extension.md)
- [TSIT claim status table](docs/research-program/adjacent-directions/tsit_claim_status_table.md)
- [TSIT witness catalog reference](docs/research-program/adjacent-directions/tsit_witness_catalog_reference.md)

## Workbench

The workbench is a theorem-linked research surface, not a detached UI demo.

- [Protected-State Correction Workbench](docs/workbench/index.html)
- [Workbench overview](docs/app/workbench-overview.md)
- [Module-theory map](docs/app/module-theory-map.md)
- [Benchmark / Validation Console](docs/app/benchmark-validation-console.md)

## Image / Figure Center

Visual artifacts are organized as a first-class supporting surface:

- [Figure Index (image center)](docs/visuals/figure-index.html)
- [Visual Gallery](docs/visuals/visual-gallery.html)
- [Visual Guide](docs/visuals/visual-guide.md)

## Validation and References

- [Master validation report](docs/validation/master_validation_report.md)
- [Professional validation report](docs/app/professional-validation-report.md)
- [Full falsification and repair report](docs/falsification/FULL_FALSIFICATION_AND_REPAIR_REPORT.md)
- [Master reference map](docs/references/master_reference_map.md)
- [BibTeX library](docs/references/protected-state-correction.bib)

## Companion Repositories

This repository keeps theorem-core OCP and its branch-limited recoverability program as the primary home of record. Companion repositories remain separate when they carry their own domain-first development cycle:

- OCP main repo (this repo): [RRG314/Protected-State-Correction-Theory](https://github.com/RRG314/Protected-State-Correction-Theory)
- Soliton companion: [RRG314/soliton-geometry-research](https://github.com/RRG314/soliton-geometry-research)
- MHD companion: [RRG314/MagnetoHydroDynamic-research](https://github.com/RRG314/MagnetoHydroDynamic-research)

## Scope Limits

This repository does not claim a universal correction law across all domains, a universal amount-only recoverability classifier, or a universal physics unification theorem.

## Author

Steven Reid  
ORCID: [0009-0003-9132-3410](https://orcid.org/0009-0003-9132-3410)  
Email: `sreid1118@gmail.com`
