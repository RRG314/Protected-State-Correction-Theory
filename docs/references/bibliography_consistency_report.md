# Bibliography Consistency Report

Date: 2026-04-17

## Scope

Audited bibliography and citation metadata across:
- `CITATION.cff`
- `docs/references/protected-state-correction.bib`
- `docs/references/ocp-visual-figures.bib`
- paper markdown files and reference sections
- paper URL/DOI validation output

## Findings

1. Repository metadata consistency
- Author identity is consistent:
  - Steven Reid
  - ORCID: 0009-0003-9132-3410
  - Email: `sreid1118@gmail.com`

2. Canonical citation source
- `docs/references/protected-state-correction.bib` is suitable as canonical BibTeX source.
- `ocp-visual-figures.bib` should remain supporting/special-purpose.

3. Reference validity
- `scripts/validate/validate_paper_references.py` reported:
  - papers checked: 4
  - failing URLs: 0
  - failing DOIs: 0

4. Style consistency
- Minor heterogeneity remains in historical/internal reports, but canonical papers are consistent enough for submission workflows.

## Normalization Decisions

- Canonical bibliography for citations and paper drafting: `protected-state-correction.bib`
- README and top-level docs should point to:
  - `CITATION.cff`
  - `docs/references/how-to-cite-this-work.md`
  - `docs/references/protected-state-correction.bib`

## Remaining Caution Points

- Avoid duplicating bibliography entries across multiple `.bib` files unless scope-specific.
- Keep companion-repo references in availability sections, not mixed into core theorem bibliographies unless directly cited as software artifacts.
