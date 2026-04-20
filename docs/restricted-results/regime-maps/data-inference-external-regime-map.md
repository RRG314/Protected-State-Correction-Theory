# Data, Inference, and External Validity Regime Map

## External lanes currently integrated

Independent external datasets in harness:
- `external_uci_wine_quality` (UCI Wine Quality)
- `external_uci_magic_gamma` (UCI MAGIC Gamma Telescope)
- `external_uci_ionosphere` (UCI Ionosphere)
- `external_uci_spambase` (UCI Spambase)

Provenance is recorded under `data/imported/external/*/PROVENANCE.md`.

## Regime E1: Amount-scalar non-reducibility on external lanes

Setting:
- quantized amount-code descriptors with binary lane labels.

Assumptions:
- deterministic classification restricted to amount-code classes.

Claim:
- mixed amount-code collisions produce decisive no-go witnesses.

Status:
- `PROVED_RESTRICTED` on all integrated external lanes.

What survives:
- anti-scalar boundary across independent data sources.

What fails:
- exact deterministic amount-only classification on those lanes.

Boundary:
- deterministic code-class model.

Evidence / tests / artifacts:
- `amount_scalar_nonreducibility.csv`

Nonclaims:
- no claim about all statistical learners or unrestricted feature maps.

## Regime E2: Descriptor-profile lift

Setting:
- amount baseline versus augmented profile with compatibility/ambiguity coordinates.

Assumptions:
- same quantization protocol per lane.

Claim:
- augmented profile lowers IDELB obstruction versus amount baseline.

Status:
- `VALIDATED` on all scored lanes.

What survives:
- diagnostic lift on internal and external lanes.

What fails:
- universal guarantee of large effect size across all datasets.

Boundary:
- declared quantization and lane definitions.

Evidence / tests / artifacts:
- `unified_cross_domain_reduction_metrics.csv`
- `out_of_family_anti_classifier.csv`

Nonclaims:
- no universal invariant claim.

## Regime E3: Decision baseline pressure

Setting:
- amount-code experiment vs augmented-code experiment with binary Bayes error.

Assumptions:
- finite empirical joint tables and deterministic binning.

Claim:
- augmented experiment reduces Bayes error in all currently scored lanes.

Status:
- `VALIDATED`.

What survives:
- practical decision-theoretic gain over amount-only experiment in current lanes.

What fails:
- full Blackwell-deficiency ordering over unrestricted experiment classes.

Boundary:
- practical finite-sample surrogate baseline only.

Evidence / tests / artifacts:
- `decision_baseline_comparison.csv`
- `docs/methods-diagnostics/decision-baseline-pressure.md`

Nonclaims:
- this is not a full comparison-of-experiments theorem package.

## Data arena verdict

- Works: external anti-classifier and decision-risk improvements survive across diverse independent lanes.
- Fails: amount-only deterministic exactness remains blocked on all current external lanes.
- Open: stronger theoretical non-reducibility classes beyond finite coded experiments.
