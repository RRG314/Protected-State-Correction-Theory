# Soliton Branch Theorem Candidates

Date: 2026-04-17

## TC-SOL-1: Symmetry Non-Identifiability No-Go

Statement:
If observation map `M` is invariant under a nontrivial subgroup of `G`, full parameter recovery on `P` is impossible; only quotient recovery on `P/G` can be injective.

Status: `PROVED` on declared family/observation setup.

## TC-SOL-2: Restricted Injectivity for Selected Observation Families

Statement (current form):
On declared finite Family B scans, `local_complex_2` and `fourier_magnitudes_4` are injective on quotient target `(eta,v)`.

Status: `CONDITIONAL` + `VALIDATED`.

Needed for upgrade:
- continuous-domain injectivity theorem with explicit nondegeneracy assumptions.

## TC-SOL-3: Same-Count Opposite-Verdict Criterion (Candidate)

Statement (current form):
Equal observation dimension does not determine quotient identifiability on restricted one-soliton families.

Witness:
- `obs_dim = 4`
- `local_complex_2`: `true_nonident_pairs = 0`
- `local_magnitude_4`: `true_nonident_pairs = 145152`

Status: `VALIDATED` on tested family; continuous theorem `CONDITIONAL`.

## TC-SOL-4: Noise-Aware Ambiguity Floor

Statement (restricted):
For quotient-noninjective observation families, ambiguity remains bounded away from zero as noise level tends to zero.

Current support:
- magnitude-only family exhibits nonzero floor in declared scans.

Status: `PROVED ON SUPPORTED FAMILY` + `VALIDATED`; broader theorem `CONDITIONAL`.

## TC-SOL-5 (Secondary Lane): Projection/Reduction Preservation Split

Statement (restricted benchmark):
There exist reduction operators on the same NLS family with opposite one-soliton manifold preservation verdicts.

Current support:
- `lowpass_k18pct` near-preserving on single-soliton case,
- `subsample_interp_x8` no-go failure.

Status: `VALIDATED` + `CONDITIONAL`.
