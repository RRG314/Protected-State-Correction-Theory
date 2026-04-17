# Publication Figure Pipeline

Generate all paper figures (PNG + PDF):

```bash
python scripts/figures/generate_publication_figures.py
```

Validate generated assets and core numeric relationships:

```bash
python scripts/figures/validate_publication_figures.py
```

Reference URL validation for all paper manuscripts:

```bash
python scripts/validate/validate_paper_references.py
```

Outputs:
- `figures/recoverability/*`
- `figures/ocp/*`
- `figures/mhd/*`
- `figures/bridge/*`
- `data/generated/figures/publication_figure_metrics.json`
- `data/generated/figures/publication_figure_validation.json`
- `data/generated/validations/paper_reference_validation.json`
