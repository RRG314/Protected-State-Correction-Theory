# Public vs Internal Map (OCP)

Date: 2026-04-16/17

## Purpose

Prevent internal-only research process artifacts from being treated as public canonical outputs.

## Public-safe canonical classes

- top-level reports: `README.md`, `SYSTEM_REPORT.md`, `FINAL_REPORT.md` (after consistency pass).
- theorem/no-go branch docs under `docs/theorem-candidates`, `docs/finalization`, `docs/research-program` (curated subset).
- validated generated artifact summaries under `data/generated/validations/*`.
- workbench docs intended for external readers.
- soliton branch summary docs that are status-labeled and bounded.

## Internal-only / keep-private classes

- cross-program scratch memos and private audits in user-level workspace roots.
- temporary comparative notes and intermediate synthesis drafts.
- raw internal discussion dumps that are not status-normalized.

## Borderline / review before public push

- newly added long-form integration reports with date-stamped names.
- draft paper pipelines and private release planning notes.
- generated inventories that may include implementation-only paths.

## Soliton bridge publication rule

Public-facing OCP docs may reference:
- admitted branch decision,
- status registry,
- bounded analogue claims,
- rejection boundaries.

They should not expose:
- internal anomaly triage details from soliton repo,
- artifact-risk exploratory logs as if they were OCP theory outcomes.

## Action in this pass

- Keep OCP-facing soliton docs branch-bounded and status-labeled.
- Keep direct nonlinear discovery narrative in soliton repo docs.
- Maintain explicit companion-program split in cross-repo integration docs.

