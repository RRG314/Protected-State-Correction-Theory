# Live vs Current Repo Audit

Date: 2026-04-17  
Target live repo: `RRG314/Protected-State-Correction-Theory` (`origin/main`)  
Current working state: local branch `steven/fiber-based-recoverability-and-impossibility` + uncommitted serious-state updates

## Audit Method

Compared:
- live public main branch (`origin/main`),
- current local serious state (working tree canonical docs).

Classification labels:
- **Canonical**: required public entry or core theorem status doc.
- **Supporting**: useful technical depth for serious readers.
- **Archive**: historical/internal provenance; keep but demote.

## Snapshot Summary

1. Live public main branch is missing several current canonical artifacts (notably current paper set copies under `papers/*.md`, descriptor-fiber branch docs, and some reference/validation maps).
2. Current local state has significant branch/program additions that are real but not yet presented as a clean single public path.
3. Public front door required consolidation to prevent layered report clutter.

## Core File Matrix

| Area | File | Live main | Current local | Role | Action |
| --- | --- | --- | --- | --- | --- |
| Front door | `README.md` | present (stale identity emphasis) | present (rebuilt) | Canonical | keep canonical, push updated version |
| Front door | `RESEARCH_MAP.md` | present (stale map) | present (rewritten) | Canonical | keep canonical, push updated version |
| Front door | `STATUS.md` | present (stale scope) | present (rewritten) | Canonical | keep canonical, push updated version |
| System status | `SYSTEM_REPORT.md` | present | present (alignment addendum) | Canonical supporting | keep; add concise live-alignment section |
| System status | `FINAL_REPORT.md` | present | present (alignment addendum) | Canonical supporting | keep; add concise live-alignment section |
| Spine | `docs/finalization/architecture-final.md` | present | present | Canonical | keep |
| Spine | `docs/finalization/theorem-spine-final.md` | present | present | Canonical | keep |
| Spine | `docs/finalization/no-go-spine-final.md` | present | present | Canonical | keep |
| Status map | `docs/overview/proof-status-map.md` | present | present | Canonical | keep |
| Status map | `docs/overview/claim-registry.md` | present | present | Canonical supporting | keep |
| Workbench | `docs/workbench/index.html` | present | present | Canonical | keep |
| Workbench docs | `docs/app/workbench-overview.md` | present | present | Canonical | keep |
| Workbench docs | `docs/app/module-theory-map.md` | present | present | Canonical supporting | keep |
| Papers | `papers/recoverability_paper_final.md` | missing on live main | present | Canonical | promote to live main |
| Papers | `papers/ocp_core_paper.md` | missing on live main | present | Canonical | promote to live main |
| Papers | `papers/bridge_paper.md` | missing on live main | present | Canonical | promote to live main |
| Papers | `papers/mhd_paper_upgraded.md` | missing on live main | present | Canonical | promote to live main |
| Papers | `papers/unifying_theory_framework_final.md` | missing on live main | present | Canonical supporting | promote to live main |
| Branch docs | `docs/research-program/descriptor-fiber-anti-classifier-branch-overview.md` | missing on live main | present | Supporting (branch-limited) | promote with scoped status |
| Branch docs | `docs/research-program/descriptor-fiber-anti-classifier-branch-status.md` | missing on live main | present | Supporting | promote with scoped status |
| References | `docs/references/master_reference_map.md` | missing on live main | present | Canonical supporting | promote |
| Validation | `docs/validation/master_validation_report.md` | missing on live main | present | Canonical supporting | promote |
| Validation | `validation_summary.json` | missing on live main | present | Supporting machine-readable | promote if regenerated in same commit |

## Stale/Overlap Findings (Live-facing)

1. `RESEARCH_MAP.md` and `STATUS.md` were too narrow and not synchronized with branch-limited recoverability/anti-classifier reality.
2. Public identity text underemphasized the now-major constrained-observation and anti-classifier lanes.
3. Multiple deep pass reports were discoverable but not clearly demoted relative to canonical entry docs.

## Low-Value/Clutter Candidates

### Demote from front-facing (keep as archive/supporting)
- dated multi-pass reports in `docs/research-program/*2026-04-16*` bundles,
- exploratory `meta_theory` narrative files (keep only as historical provenance),
- overlapping integration summaries that restate canonical spines.

### Keep public-facing
- finalization spines,
- proof/claim maps,
- canonical papers,
- workbench overview + module map + benchmark console,
- validation/reference maps.

## Audit Conclusion

The current local state is stronger and more complete than live main. The required public alignment is primarily:
1. promote canonical files from current local state,
2. demote noisy exploratory/historical layers from front-door navigation,
3. preserve historical material via archive labeling rather than deletion.
