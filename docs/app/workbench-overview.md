# Workbench Overview

The workbench is the operational surface for the theorem program. It is used to test recoverability conditions, identify structural blockers, and apply supported repair operations on declared families.

The workflow is simple: define the target and record, run diagnosis, inspect exact/conditional/fail regime status, try a supported repair, and export reproducible evidence. The interface is designed to preserve branch scope, so unsupported mixed-family claims are rejected rather than silently approximated.

Three surfaces carry most of the work. The Structural Discovery Studio handles diagnosis and repair comparison. The Discovery Mixer handles typed composition and compatibility checks before interpretation. The Benchmark/Validation Console tracks known-answer behavior and export integrity.

The workbench does not replace theorem documents. It implements them. If a claim is not theorem-backed or benchmark-validated on a declared family, the interface is expected to label it as conditional or exploratory.

Companion docs:
- `docs/app/module-theory-map.md`
- `docs/app/benchmark-validation-console.md`
- `docs/app/tool-qualification-report.md`
- `docs/app/professional-validation-report.md`
