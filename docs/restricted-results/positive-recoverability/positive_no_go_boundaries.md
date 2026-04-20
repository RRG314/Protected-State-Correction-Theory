# Positive No-Go Boundaries

Purpose:
Define failure/minimality boundaries for positive recoverability architectures.

Primary counterexample data:
- `data/generated/positive_framework/positive_counterexample_catalog.csv` (`152` rows)

## PN-1 Descriptor-Only Positive Classifier No-Go

Statement:
Amount-only descriptor signatures do not classify shared exactness.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `45` descriptor-only failures (same amount signature, opposite invariant verdict).

Boundary lesson:
- any positive framework without compatibility lift is incomplete.
- finite amount-code exact-classifier boundary is now explicit in `OCP-062`.

## PN-2 Model-Mismatch Boundary

Statement:
Exactness certificates are target-relative; changing target outside compatibility rowspace breaks exactness.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `50` mismatch failures,
- `49` with positive constrained-library defect (`delta_C > 0`).

## PN-3 Family-Enlargement Fragility Boundary

Statement:
Exactness on a base context family does not imply exactness on enlarged family.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `53` enlargement failures with local exactness preserved but shared exactness lost.

## PN-4 Library-Gain Insufficiency No-Go

Statement:
Raw candidate-library rank gain is not sufficient for constrained exact repair.

Status:
- `PROVED ON RESTRICTED CLASS`.

Reason:
- direction/alignment defect (`delta_C`) matters, not amount alone.

## PN-5 Nonlinear Extension Boundary

Statement:
Linear positive architecture theorems do not automatically transfer to nonlinear measurement maps.

Status:
- `PROVED` as a boundary no-go via explicit nonlinear counterexample family,
- restricted positive subclass survives for injective record post-compositions,
- extension to broad nonlinear theorem classes remains `OPEN`.

Evidence:
- `4` nonlinear sign-collision rows (`y=x^2`, target `x`).
- injective-postcomposition finite-family equivalence checks (`y -> y^3`) in structural-information tests.

## PN-6 Trivial-Class Prevention Boundary

Statement:
If class definitions bake recoverability directly into admissibility without independent testable conditions, positive framework becomes trivial and non-informative.

Status:
- `PROVED` as methodological no-go.

## Boundary summary

The strongest positive package survives only with explicit boundaries:
1. class scope fixed (finite linear context families),
2. compatibility lift included,
3. augmentation admissibility declared,
4. mismatch and enlargement failure explicitly tracked.
