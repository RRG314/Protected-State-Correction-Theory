# AI Writing Failure Audit

Date: 2026-04-17

This audit identifies recurring AI-style writing failures found in the repository and documents the rewrite priorities used in this pass.

## Failure Matrix

| Failure type | Representative locations | Severity | Rewrite priority | Action taken |
| --- | --- | --- | --- | --- |
| Repetition without added value | `README.md`, `SYSTEM_REPORT.md`, `FINAL_REPORT.md`, `docs/research-program/branch-audit.md` | High | P1 | Replaced repeated identity/process phrases with one canonical explanation per document role. |
| Bullet-list dumping | `README.md`, `docs/app/workbench-overview.md`, `docs/research-program/usefulness-by-branch.md`, `docs/finalization/*` | High | P1 | Converted inventory-style bullet stacks into explanatory prose with selective lists only where structurally useful. |
| Shallow abstraction language | `SYSTEM_REPORT.md`, `STATUS.md`, `docs/app/module-theory-map.md` | High | P1 | Added explicit “what it is, what problem it solves, what it does not claim” framing tied to branch evidence. |
| AI-sounding transition language | `FINAL_REPORT.md`, `SYSTEM_REPORT.md` | Medium | P1 | Removed canned pass-log transitions and rewrote as authored analytical narrative. |
| Status clutter/process-log tone | `SYSTEM_REPORT.md`, `FINAL_REPORT.md`, `docs/repo_cleanup/*alignment*` | High | P1 | Reduced repeated promoted/demoted phrasing; retained status labels only where they change interpretation. |
| Pseudo-clarity (clear syntax, weak meaning) | `docs/research-program/usefulness-by-branch.md`, `docs/app/workbench-overview.md` | Medium | P2 | Added concrete role and decision impact statements per branch/module. |
| Branch-isolation drift | `docs/research-program/branch-audit.md`, `docs/integration/repo_scope_statement.md` | Medium | P1 | Rewrote branch summaries to explicitly connect each lane to the whole program. |
| Front-door overload and weak hierarchy | `README.md`, `RESEARCH_MAP.md`, `docs/overview/start-here.md` | High | P1 | Rebuilt entry docs with a clear orientation → theory spine → branch lanes → tooling → references flow. |
| System under-explanation | `docs/app/workbench-overview.md`, `docs/app/module-theory-map.md` | High | P1 | Reframed modules as problem-solving components tied to theorem status rather than feature list dumps. |
| Formulaic sentence rhythm | multiple front-door and summary docs | Medium | P2 | Varied paragraph structure and reduced repetitive short declaratives. |

## Cross-Repo Clarity Risks Found

| Risk | Representative locations | Severity | Action taken |
| --- | --- | --- | --- |
| Companion boundary ambiguity | `README.md`, `docs/repo_cleanup/companion_repo_map.md`, `docs/integration/repo_scope_statement.md` | Medium | Clarified home-of-record split and admissible bridge scope. |
| Soliton/OCP over-interpretation risk | integration/branch docs | Medium | Kept overlap language bounded and status-labeled. |

## Audit Conclusion

Highest-impact failures were concentrated in front-door and system-summary documents. The rewrite pass therefore prioritized canonical docs first, then branch/workbench explanation docs, and finally cleanup/report surfaces.
