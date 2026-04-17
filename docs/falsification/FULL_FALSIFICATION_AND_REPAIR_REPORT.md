# Full Falsification And Repair Report

Date: 2026-04-17
Repository: OCP / Protected-State-Correction-Theory
Pass: Full falsification / disproof / repair

## 1. What was attacked

A-K branch program executed:
- A: exact finite-dimensional projector branch
- B: exact sector / QEC branch
- C: periodic Helmholtz / Leray branch
- D: bounded-domain / Hodge / CFD branch
- E: asymptotic generator branch
- F: constrained-observation / PVRT branch
- G: restricted-linear augmentation / anti-classifier branch
- H: fiber-based recoverability / impossibility branch
- I: workbench / Structural Discovery / Discovery Mixer surfaces
- J: physics extension / Maxwell / damping bridges
- K: meta-theory / descriptor-fiber extraction

## 2. Audit artifacts produced

- `docs/falsification/full_claim_audit.md`
- `data/generated/falsification/full_claim_audit.csv`
- `docs/falsification/theorem_falsification_report.md`
- `docs/falsification/counterexample_catalog.md`
- `data/generated/falsification/counterexample_catalog.csv`
- `docs/falsification/falsification_validation_results.md`
- `docs/falsification/wolfram_verification_report.md`

## 3. Counterexample program results

Canonical regenerated witness families now indexed in counterexample catalog:
- same-rank opposite-verdict witnesses (`OCP-047/OCP-049`)
- same-budget opposite-verdict witnesses (`OCP-050`)
- family-enlargement false-positive witness (`OCP-052`)
- model-mismatch instability witnesses (`OCP-053`)
- periodic refinement false-positive witness (family-blind exactness overclaim)
- descriptor-fiber mixedness witnesses for meta-layer anti-classifier extraction

## 4. Claims narrowed/demoted/retracted in this pass

### Survived but narrowed (demoted to supported-family status)
- `OCP-022`: `PROVED` -> `PROVED ON SUPPORTED FAMILY`
- `OCP-027`: `PROVED` -> `PROVED ON SUPPORTED FAMILY`
- `OCP-044`: `PROVED` -> `PROVED ON SUPPORTED FAMILY`

### Previously disproved (reconfirmed)
- `OCP-023`: remains `DISPROVED`

### Newly retracted in this pass
- none.

## 5. Concrete defects found and repaired

1. Workbench benchmark console omitted/renamed module labels required by consistency checks.
   - file repaired: `docs/workbench/lib/engine/benchmarkConsole.js`

2. README lacked the required professional validation reference checked by consistency tests.
   - file repaired: `README.md`

3. Claim-status overreach in selected bridge/restricted-family rows.
   - files repaired: `docs/overview/claim-registry.md`, `docs/overview/proof-status-map.md`

4. System/final reports had stale status interpretation after normalization.
   - files repaired: `SYSTEM_REPORT.md`, `FINAL_REPORT.md`

## 6. Validation gate outcomes

- JS consistency: pass (`29/29`)
- Python math: pass (`153 passed`)
- Python examples: pass (`29 passed`)
- link integrity check: pass
- witness regeneration scripts: completed

See full command-level details in:
- `docs/falsification/falsification_validation_results.md`

## 7. Wolfram/symbolic status

- `wolframscript` unavailable locally.
- No Wolfram-backed claims are made.
- Python/NumPy/SymPy-equivalent checks were used.

## 8. Final status posture

The repository exits this pass with:
- stronger branch-scope honesty,
- explicit supported-family labeling where needed,
- repaired tool/report consistency,
- regenerated counterexample and witness artifacts,
- no new universal overclaim promoted.

## 9. Files changed in this pass (direct edits + new falsification artifacts)

Direct edits:
- `README.md`
- `SYSTEM_REPORT.md`
- `FINAL_REPORT.md`
- `docs/overview/claim-registry.md`
- `docs/overview/proof-status-map.md`
- `docs/workbench/lib/engine/benchmarkConsole.js`
- `docs/meta_theory/README.md`

New/updated falsification docs:
- `docs/falsification/full_claim_audit.md`
- `docs/falsification/theorem_falsification_report.md`
- `docs/falsification/counterexample_catalog.md`
- `docs/falsification/wolfram_verification_report.md`
- `docs/falsification/falsification_validation_results.md`
- `docs/falsification/FULL_FALSIFICATION_AND_REPAIR_REPORT.md`
- `docs/falsification/CHANGELOG_FALSIFICATION_PASS.md`

New scripts:
- `scripts/falsification/build_full_claim_audit.py`
- `scripts/falsification/build_counterexample_catalog.py`
- `scripts/falsification/apply_status_overrides.py`
- `scripts/falsification/build_falsification_summary.py`
- `scripts/report/compute_meta_theory_invariants.py`

Generated data artifacts:
- `data/generated/falsification/full_claim_audit.csv`
- `data/generated/falsification/counterexample_catalog.csv`
- `data/generated/falsification/falsification_summary.json`
- `data/generated/meta-theory/meta_classifier_invariants.csv`
- `data/generated/meta-theory/meta_classifier_invariants.json`
