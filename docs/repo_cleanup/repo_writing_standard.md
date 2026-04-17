# Repository Writing Standard

Date: 2026-04-17

This standard defines the target prose style for canonical and high-visibility documents in this repository.

## Voice and Tone

Writing should be mathematically serious, direct, and calm. It should explain scope clearly without defensive over-qualification and without promotional language.

## Core Style Rules

1. Explain before listing.
2. Use lists only when they improve structure or scanability.
3. Keep hierarchy explicit: foundation, branch-limited strengthening, tooling/validation, companion boundaries.
4. Prefer concrete statements over abstract slogans.
5. State limits where they change interpretation; avoid repeating status labels as filler.
6. When introducing a system, answer: what it is, what problem it solves, how it works at a high level, what its limits are.
7. Public docs should optimize reader understanding, not process-history completeness.
8. Reports should read as analysis, not generated logs.
9. Preserve theorem/status honesty and avoid scope inflation.
10. Keep canonical phrasing consistent across README, status, system/final reports, and workbench overviews.

## Canonical Identity Wording

Use this framing consistently (adapted by context):

- The repository is a theorem-first OCP program with branch-limited recoverability strengthening.
- OCP is foundational, but recoverability/anti-classifier/bounded-domain lanes are major integrated branches.
- The workbench is theorem-linked and evidence-labeled, not a detached universal engine.

## Document Role Guidance

### README / Start Here / Research Map
Focus on orientation and hierarchy. Avoid deep inventories and process logs.

### Status / System / Final reports
Focus on program interpretation, branch roles, and scope boundaries. Move procedural detail into dedicated audit docs.

### Branch and theorem docs
Explain branch contribution to the whole program before enumerating branch-local claims.

### Workbench docs
Describe workflow and evidence model before module lists.

### Cleanup/audit docs
Keep process history factual, but avoid repeated narrative phrases copied from front-door docs.

## Anti-Patterns to Avoid

- Repeating “strongest current result” in multiple adjacent sections.
- Long stacked bullets where a short explanatory paragraph is clearer.
- Using status labels (`promoted/demoted/kept/rejected`) as a substitute for explanation.
- Rewriting the same repo identity sentence in every doc.
- Turning system docs into changelog dumps.
