# Live Deployed vs Local Audit Report

Date: 2026-04-19  
Repo: `RRG314/Protected-State-Correction-Theory`  
Local workspace: `/Users/stevenreid/Documents/New project/repos/ocp-research-program`

## Baseline

- Live deployed baseline: `origin/main` at `cf4e99ad4901edf3340f128c626dcd7fb0292f02` (`v1.1.0`)
- Local push-prep branch: `steven/push-cleanup-audit`
- Snapshot reference commit (pre-reporting checkpoint): `3da3b9bb79502bc44f4d72441629fe294a46a029`
- Divergence status: local branch is ahead of `origin/main` with no observed behind count during this audit pass

## Commit Delta (local ahead stack)

1. `db5bd95` phase1 integration of external structural-information artifacts
2. `0561a14` phase2 structural-information core module and harness additions
3. `1bb6612` overlap re-audit and citation/scope hardening
4. `660488a` architecture audit
5. `da7d976` six-layer architecture and canonical routing rewrite
6. `7c1744a` README and entry routing rewrite
7. `286af49` theorem/restricted-result language tightening
8. `fbf6445` diagnostics, validation, and physics translation clarifications
9. `791c5c3` style normalization pass
10. `c027857` architecture moves and internalization commit
11. `4fd61f6` canonical routing/public surface cleanup commit
12. `3da3b9b` writing normalization across active docs
13. reporting commit(s) that add and refresh live-vs-local and push-readiness documentation

## Diff Scale vs Live

`origin/main...HEAD` statistics:

- 485 files changed (audit snapshot range)
- 7361 insertions (audit snapshot range)
- 1282 deletions (audit snapshot range)
- status mix includes heavy rename volume (`R100=214`) plus additions and edits

Top touched areas (by changed path count):

- `docs/meta-governance` (302)
- `docs/archive` (45)
- `docs/methods-diagnostics` (20)
- `data/imported` (17)
- `docs/research-program` (11)
- `docs/restricted-results` (10)
- `data/generated` (10)

## Concrete Difference Examples

### Example 1: Root research framing

- Live file: `README.md` on `origin/main`
- Local file: `README.md` on `steven/push-cleanup-audit`

Difference:
- Local version replaces broad onboarding language with research scope, claim boundaries, and six-lane routing.
- Local version makes known-backbone vs restricted-results separation explicit in the entry page.

### Example 2: Canonical routing

- Live entry path: `docs/overview/start-here.md` with legacy routing dependencies
- Local entry path: `docs/overview/start-here.md` aligned to the new authority map and theorem-first reading order

Difference:
- Local routing is branch- and lane-structured.
- The strongest theorem/no-go path is surfaced earlier.

### Example 3: Structural internalization

- Live surface keeps more pass artifacts in externally visible locations.
- Local branch relocates large process-heavy sets to internal/archive governance lanes and introduces compatibility redirects.

Representative move pattern:
- `docs/meta-governance/structural-information-theory/*`
- -> `docs/meta-governance/internal/structural-information-theory/*`

### Example 4: New imported evidence lane

- Live baseline does not include the imported structural-information provenance package.
- Local branch adds:
  - `data/imported/structural-information-theory/provenance_manifest.csv`
  - `data/imported/structural-information-theory/missing_pieces_map.csv`
  - `data/imported/structural-information-theory/theory_completion_summary.json`

Difference:
- Local branch has explicit provenance/evidence traces for imported theory-completion artifacts.

## Current Push Readiness State

- Working tree status at audit completion: clean
- Generated artifact churn from validation was intentionally restored before staging
- No broad unstaged delete/add move chaos remains

## Remaining Gaps and Risks Before Push

1. Review size risk remains high.
   - The branch remains a large multi-commit stack over `origin/main`.
2. Internal governance volume is large.
   - `docs/meta-governance/internal/*` is extensive; review messaging must clarify why it exists.
3. Rename-heavy diff may still look noisy on GitHub in some sections.
   - Reviewer guidance should identify architecture moves vs substantive theorem edits.
4. Validation environment dependency.
   - `scripts/validate/run_all.sh` requires running inside the repo `.venv` to avoid `numpy` import failures from system Python.

## Recommended Push Path

1. Push branch `steven/push-cleanup-audit` to remote.
2. Open PR to `main` with a reviewer-oriented commit walkthrough:
   - architecture moves/internalization
   - canonical routing/public surface
   - writing normalization
3. In PR description, call out:
   - known-vs-new claim boundary tightening
   - no intentional generated-artifact churn included
   - validation command and environment used

This local branch is now in a state that supports a clean PR review flow.
