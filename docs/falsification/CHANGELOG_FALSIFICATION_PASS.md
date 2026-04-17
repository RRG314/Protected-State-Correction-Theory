# Changelog: Falsification Pass (2026-04-17)

## Status changes

- `OCP-022`: `PROVED` -> `PROVED ON SUPPORTED FAMILY`
- `OCP-027`: `PROVED` -> `PROVED ON SUPPORTED FAMILY`
- `OCP-044`: `PROVED` -> `PROVED ON SUPPORTED FAMILY`

## Tool/report repairs

- fixed benchmark module labels in `docs/workbench/lib/engine/benchmarkConsole.js`
- added professional-validation link in `README.md`
- added falsification addenda to `SYSTEM_REPORT.md` and `FINAL_REPORT.md`

## New scripts

- `scripts/falsification/build_full_claim_audit.py`
- `scripts/falsification/build_counterexample_catalog.py`
- `scripts/falsification/apply_status_overrides.py`

## New generated artifacts

- `data/generated/falsification/full_claim_audit.csv`
- `data/generated/falsification/counterexample_catalog.csv`
- `data/generated/meta-theory/meta_classifier_invariants.csv`
- `data/generated/meta-theory/meta_classifier_invariants.json`

## New falsification docs

- `docs/falsification/full_claim_audit.md`
- `docs/falsification/theorem_falsification_report.md`
- `docs/falsification/counterexample_catalog.md`
- `docs/falsification/wolfram_verification_report.md`
- `docs/falsification/falsification_validation_results.md`
- `docs/falsification/FULL_FALSIFICATION_AND_REPAIR_REPORT.md`
- `docs/falsification/CHANGELOG_FALSIFICATION_PASS.md`

## Existing claims reaffirmed via tests

- projector/no-go core (`OCP-002`, `OCP-003`)
- asymptotic generator package (`OCP-013`, `OCP-014`, `OCP-015`, `OCP-020`)
- constrained-observation theorem layer (`OCP-030..043`)
- anti-classifier and fragility/mismatch package (`OCP-045..053`)
