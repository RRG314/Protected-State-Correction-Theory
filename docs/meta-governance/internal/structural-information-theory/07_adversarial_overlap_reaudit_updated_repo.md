# Adversarial Overlap and Usefulness Re-Audit (Updated Local OCP State)

Date: 2026-04-19  
Baseline audit: `external-imports/adversarial_originality_overlap_usefulness_audit.md`

## What changed materially in this pass

New additions that affect novelty/usefulness assessment:
1. Explicit primitive object implementation (`src/ocp/structural_information.py`).
2. Restricted perturbation stability theorem implementation + checks.
3. Unified cross-domain harness with out-of-family anti-classifier checks.
4. Decision-baseline compression-regret comparison output.
5. Scope-and-citation hardening in core theorem docs.

Supporting table artifact:
- `data/generated/structural-information-theory/overlap_novelty_table_updated.csv`

## 1) Still clearly known backbone

Unchanged as known/reformulation:
- exact recoverability via factorization/fiber constancy,
- linear row-space/kernel criterion form,
- basic coarsening logic,
- core observability/identifiability overlap structure.

Verdict: remains `KNOWN` / `KNOWN REFORMULATION` and must be stated as such.

## 2) Still primarily reformulation/new language

- Broad “information as structural distinctions” framing remains mostly a unifying lens unless tied to restricted theorem outputs.
- Physics-wide synthesis remains mostly interpretive unless attached to explicit declared map classes.

Verdict: `KNOWN WITH DIFFERENT LANGUAGE` at broad level.

## 3) Strengthened restricted results after updates

Now stronger than previous state:
- Restricted stability bound above factorization core (`ST-7`) moved from OPEN to restricted PROVED/checked.
- Unified out-of-family anti-classifier diagnostics now executable in one local harness.
- Decision-baseline proxy comparison now explicit and reproducible.

Novelty classification:
- `PLAUSIBLY DISTINCT RESTRICTED RESULT` for stability+harness package,
- `CLEARLY NEW ONLY ON DECLARED WITNESS CLASS` for anti-classifier diagnostics.

## 4) Remaining claim-scope risks

High-risk if overstated:
- calling the primitive object a new universal information ontology,
- presenting surrogate degradation trends as universal dynamic laws,
- presenting decision-regret proxy as full Blackwell deficiency theory,
- promoting SDS beyond analogy/engineering layer.

## 5) Remaining citation burden

Still mandatory:
- factorization/sufficiency lineage,
- experiment-comparison lineage,
- identifiability/observability lineage,
- Landauer and black-hole entropy context for physics framing.

This pass integrated those anchors in core docs and references, but repo-wide consistency still requires a broader wording sweep.

## 6) What remains too weak/derivative for prominence

Demote from primary claims:
- universal-theory language,
- universal scalar invariants,
- broad cross-domain law wording without declared class assumptions.

## 7) Did this pass materially improve originality/theorem strength/usefulness?

Yes, but narrowly:
- theorem strength improved in the restricted stability lane,
- usefulness improved via a single executable harness and explicit outputs,
- originality remains restricted and methods-centered, not foundationally universal.

## 8) Strongest publishable unit now

Best lane:
- restricted negative-result + methods/benchmark paper:
  - amount-only descriptors cannot exactly classify recoverability on declared classes,
  - compatibility-aware augmentation reduces irreducible lower bounds,
  - supported by OCP + independent out-of-family lane evidence.

Second lane:
- restricted theorem note on perturbation stability above exact factorization in linear classes.

Not recommended now:
- universal positive theory-of-information paper.

## Updated verdict

- Core backbone: still mostly known.
- Framework-level novelty: still mostly reinterpretation.
- Restricted novelty: stronger than before this pass, now with executable stability and cross-domain harness evidence.
- Usefulness: improved for methods/diagnostics audience; still not a replacement for foundational standard theory.
