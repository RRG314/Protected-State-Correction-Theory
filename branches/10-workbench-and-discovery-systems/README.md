# Branch 10 — Workbench and Discovery Systems

## What this branch is
Engineering and tooling layer for theorem-linked analysis, discovery workflows, and reproducible diagnostics.

## Strongest results
- Live workbench with theorem-aware analysis modules.
- Discovery mixer and structural discovery layers.
- Validation surfaces linking generated outputs to branch claims.

## Canonical documents
- [Workbench app](../../docs/workbench/index.html)
- [Workbench overview](../../docs/app/workbench-overview.md)
- [Module-theory map](../../docs/app/module-theory-map.md)
- [Benchmark / validation console](../../docs/app/benchmark-validation-console.md)
- [Tool qualification report](../../docs/app/tool-qualification-report.md)

## Key tests / artifacts
- `tests/consistency/`
- `tests/examples/test_workbench_examples_consistency.py`
- `tests/examples/test_generated_artifact_consistency.py`
- `data/generated/validations/`

## Open items
- Keep scope controls explicit: supported-family diagnostics, not free-form symbolic theorem proving.

## Shared infrastructure
Workbench code remains centralized in `docs/workbench/lib/` and shared compare/validate scripts.
