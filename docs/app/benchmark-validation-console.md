# Benchmark and Validation Console

The benchmark console is the trust surface for the workbench. It exists so users can replay known cases, verify module behavior, and export reproducible snapshots without relying on informal interpretation.

The console tracks demo outcomes, module-health checks, and export consistency. Its purpose is not broad exploration; it is to make sure the interface stays aligned with theorem-backed and validated behavior.

Current demo coverage includes periodic modal augmentation, control/history augmentation, weak-vs-strong target splits, bounded-domain architecture repair, and restricted-linear measurement repair. These cases are maintained because they connect directly to branch claims and failure boundaries.

Use this console with the qualification reports in `docs/app/tool-qualification-report.md` and `docs/app/professional-validation-report.md`. Together they define what can be trusted as stable, what is partial, and what is still exploratory.
