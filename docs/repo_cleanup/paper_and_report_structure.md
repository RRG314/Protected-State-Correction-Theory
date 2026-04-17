# Paper and Report Structure

Date: 2026-04-17

## Goal

Organize papers and report layers so they stop competing and start reading as one intentional package.

## Paper Layer (Canonical)

| Paper role | Canonical file | Notes |
| --- | --- | --- |
| Recoverability theorem-heavy core paper | `papers/recoverability_paper_final.md` | Main anti-classifier + minimal augmentation + thresholds paper |
| OCP foundation companion | `papers/ocp_core_paper.md` | Compact operator-level framing |
| Projection/bridge paper | `papers/bridge_paper.md` | PDE/projection comparison and failure mechanism |
| MHD domain paper | `papers/mhd_paper_upgraded.md` | Euler-potential closure/obstruction lane |
| Unifying framework paper | `papers/unifying_theory_framework_final.md` | Branch-limited integrative framing |
| Descriptor-fiber anti-classifier branch paper | `papers/descriptor-fiber-anti-classifier-branch.md` | Finite-class quantitative extraction layer above anti-classifier witnesses |

Supporting paper artifacts:
- `papers/*/completeness_checklist.md`
- `papers/*/positioning_note.md`
- `papers/style/*`

## Report Layer (Canonical vs Supporting)

| Report area | Canonical | Supporting / historical |
| --- | --- | --- |
| Repo-wide architecture/theory snapshot | `docs/finalization/architecture-final.md` | `SYSTEM_REPORT.md`, `FINAL_REPORT.md` |
| Theory status and branch status | `docs/overview/proof-status-map.md` | `docs/research-program/branch-audit.md` |
| Unifying-theory refinement | `docs/unifying_theory/final_theory_refinement_master_report.md` | other `docs/unifying_theory/*` analyses |
| Validation and trust layer | `docs/validation/master_validation_report.md` | `docs/app/tool-qualification-report.md`, `docs/app/professional-validation-report.md` |
| Discovery/falsification/novelty layer | `docs/discovery/master_discovery_portfolio.md`, `docs/falsification/master_falsification_report.md`, `docs/literature/master_novelty_pressure_report.md` | `docs/research-program/*` dated passes |

## Public-Facing vs Internal/Historical Labels

- Public-facing canonical:
  - README, overview, finalization spine docs, canonical papers, workbench overview.
- Public-facing supporting:
  - branch audits, validation reports, discovery reports.
- Historical/internal (keep, do not delete):
  - dated pass folders in `docs/research-program/`.

## Path Stability Policy

1. Preserve existing files where possible.
2. If overlap exists, designate one canonical file and keep others as supporting/historical.
3. If legacy paths exist (e.g., `soliton_branch`), keep them and add canonical pointer guidance.

## Structural Outcome of This Pass

- No theorem or paper files deleted.
- Canonical paper set remains stable and front-linked.
- Report purpose boundaries are explicit.
