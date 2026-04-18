# Live Workbench and Asset Audit

Date: 2026-04-17

## Scope

Audited public-facing surfaces:
- workbench landing path and module docs,
- Structural Discovery Studio / Discovery Mixer / Benchmark Console documentation,
- image center / figure center surfaces,
- static asset and figure references,
- export/report path consistency,
- branch naming consistency in app-facing docs.

## Paths Checked

- `docs/workbench/index.html`
- `docs/app/workbench-overview.md`
- `docs/app/module-theory-map.md`
- `docs/app/benchmark-validation-console.md`
- `docs/workbench/lib/*`
- `docs/visuals/figure-index.html`
- `docs/visuals/visual-gallery.html`
- `docs/visuals/visual-guide.md`
- `docs/visuals/*`
- `figures/*`

## Validation Commands

1. `python3 scripts/validate/check_links.py`
2. `python3 scripts/validate/check_visual_gallery.py`
3. `python3 scripts/figures/validate_publication_figures.py`
4. `node --test tests/consistency/*.mjs`
5. `PYTHONPATH=src .venv/bin/pytest tests/examples/test_visual_gallery_integrity.py -q`

## Findings

### Pass

1. Workbench static consistency tests passed (`29/29`).
2. Visual gallery integrity checks passed.
3. Publication figure validation checks passed with no missing assets.
4. Markdown link checks passed.
5. Workbench docs now align with theorem-linked branch framing.
6. Figure Index (image center) and Visual Gallery paths resolve from canonical public docs.

### Naming/Status Consistency

1. No stale primary `meta theory` naming found in canonical workbench entry docs.
2. Descriptor-fiber branch is presented as branch-limited and non-standalone in module mapping, consistent with repo status discipline.
3. TSIT is presented as an adjacent quantitative extension (`EXPLORATION / NON-PROMOTED`) in docs and is not exposed as a promoted workbench theorem lane.

### Remaining Risk Notes

1. Historical app/report docs should stay demoted from front-door navigation.

## Conclusion

Live workbench, image center, and asset surfaces are consistent with current canonical branch identity and pass path/asset validation for public release.
