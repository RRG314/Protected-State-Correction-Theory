# External Dataset Provenance: UCI Wine Quality

Source institution: UCI Machine Learning Repository
Dataset page: https://archive.ics.uci.edu/ml/datasets/Wine+Quality

Downloaded files:
- `winequality-red.csv`
- `winequality-white.csv`

Download URL base:
- `https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/`

Downloaded on: 2026-04-19 (local completion pass)

Use in this repository:
- independent external validation lane for structural-information harness
- binary target used in harness: `quality >= 7`

Notes:
- This dataset is externally curated and not generated in this workspace.
- Integration logic is implemented in `scripts/research/run_structural_information_harness.py`.
