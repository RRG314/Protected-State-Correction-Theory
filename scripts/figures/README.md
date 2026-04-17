# Publication Figure Pipeline

Generate all paper figures (PNG + PDF):

```bash
./.venv/bin/python scripts/figures/generate_publication_figures.py
```

Validate generated assets and core numeric relationships:

```bash
./.venv/bin/python scripts/figures/validate_publication_figures.py
```

Reference URL validation for all paper manuscripts:

```bash
./.venv/bin/python scripts/validate/validate_paper_references.py
```

Outputs:
- `figures/recoverability/*`
- `figures/mhd/*`
- `figures/bridge/*`
- `data/generated/figures/publication_figure_metrics.json`
- `data/generated/figures/publication_figure_validation.json`
- `data/generated/validations/paper_reference_validation.json`
