# Full Repository Inventory Report

Date: **2026-04-18**

## 1) Snapshot

- Branch: `main`
- HEAD: `8b831bf`
- Remote: `origin https://github.com/RRG314/Protected-State-Correction-Theory.git`
- Working-state note: this report is generated during the TSIT Option D integration pass (tracked updates + untracked additions pending commit).

## 2) Top-Level Inventory (file counts)

| Area | File Count |
|---|---:|
| `docs` | 546 |
| `papers` | 48 |
| `src` | 59 |
| `scripts` | 52 |
| `tests` | 86 |
| `data/generated` | 89 |
| `figures` | 42 |
| `theory` | 7 |
| `archive` | 8 |
| `discovery` | 6 |

## 3) Documentation Inventory Highlights

- `docs/research-program`: **62** markdown files
- `docs/fiber-based-recoverability-and-impossibility`: **52** markdown files
- `docs/unifying_theory`: **35** markdown files
- `docs/repo_cleanup`: **28** markdown files
- `docs/app`: **24** markdown files
- `docs/meta_theory`: **17** markdown files

Canonical front-door and architecture files remain:
- `README.md`
- `RESEARCH_MAP.md`
- `STATUS.md`
- `SYSTEM_REPORT.md`
- `FINAL_REPORT.md`
- `docs/finalization/*`

## 4) Code and Test Inventory

- `src/ocp` modules: **20**
- `tests/math`: **17** python test files
- `tests/examples`: **18** python test files
- `tests/consistency/*.mjs`: present for docs/workbench/static consistency checks

## 5) Generated Artifact Inventory

`data/generated` now includes **17** active subprogram folders and **89** files total.

Key active generated lanes:
- `recoverability/`
- `unified-recoverability/`
- `indistinguishability/`
- `descriptor-fiber-anti-classifier/`
- `falsification/`
- `discovery/`
- `discovery-portfolio/`
- `validations/`
- `tsit-extension/` (new Option D adjacent lane mirror)

TSIT extension mirror in this repo:
- `data/generated/tsit-extension/tsit_positioning_summary.json`
- `data/generated/tsit-extension/tsit_option_d_scorecard.csv`
- `data/generated/tsit-extension/tsit_positioning_expansion_witnesses.csv`
- `data/generated/tsit-extension/tsit_positioning_expansion_anomalies.csv`

## 6) Workbench + Visual Surface Inventory

- `docs/workbench`: **27** files
- `docs/visuals`: includes figure index (image center), gallery, visual guide, and full visual story
- `figures/`: **42** files across bridge, indistinguishability, MHD, OCP, and recoverability families

## 7) Expansion / Discovery Work Already Integrated

Integrated in current OCP repo history:
- cross-domain exploration package
- major expansion candidate package
- indistinguishability exploration lane
- descriptor-fiber quantitative branch package
- AI-writing cleanup/professionalization pass
- image center integration and link cleanup

Current pass adds Option D TSIT adjacent quantitative extension placement and mirrored TSIT artifact subset.

## 8) Work Still Not Fully Added (from recent expansion/discovery waves)

### A) Local sandbox in this repo (non-canonical; tracked as exploratory artifacts)
- `discovery/new_structures_report.md`
- `discovery/theory_candidates.md`
- `discovery/witness_catalog.csv`
- `discovery/anomaly_catalog.csv`
- `discovery/summary.json`
- `discovery/run_new_structure_exploration.py`
- `discovery/README.md`

These are exploratory outputs and should be kept labeled `EXPLORATION / NON-PROMOTED` if retained.

### B) TSIT full seed package in sibling workspace (not yet fully mirrored)
Location:
- `/Users/stevenreid/Documents/New project/repos/topological-adam/`

High-value TSIT source/support files there include:
- `TSIT_Breakout_Results_2026.docx`
- `discovery/tsit_source_map.md`
- `discovery/tsit_claim_extraction.md`
- `discovery/tsit_falsification_report.md`
- `discovery/tsit_reduction_attack_report.md`
- `docs/research-program/tsit_overview.md`
- `docs/research-program/tsit_theorem_candidates.md`
- `docs/research-program/tsit_no_go_candidates.md`
- `docs/research-program/tsit_validation_plan.md`
- `docs/research-program/tsit_major_expansion_report.md`
- `figures/tsit/*.png`
- `scripts/tsit/run_tsit_expansion.py`

Option D integration intentionally mirrored only the minimal artifact + status subset into OCP to avoid front-door clutter and over-promotion.

## 9) Canonical vs Pending Decision Summary

Canonical in OCP now:
- OCP foundation and branch-limited recoverability architecture
- descriptor-fiber quantitative branch
- TSIT as adjacent quantitative extension (`EXPLORATION / NON-PROMOTED`), with no theorem-spine edits

Pending/optional mirror work:
1. Decide whether to mirror the full TSIT source package from `topological-adam` into a supporting archive path under `docs/research-program/adjacent-directions/`.
2. Decide whether to track `discovery/` sandbox outputs in this repo or keep them local-only.
3. If `discovery/` is tracked, add schema/reproducibility checks for its catalogs/script.
