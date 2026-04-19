# Context-Sensitive Recoverability Falsification Report

Status: `EXPLORATION / NON-PROMOTED`

This report records direct attacks on the three-package main track.

## Attack 1

Question:
Does the package collapse entirely into old row-space/fiber statements?

Verdict: `PARTIALLY SURVIVES`.

Reason:
- Core exactness logic is still row-space/fiber based.
- Additive piece that survives: explicit contextwise-vs-shared decoder split and shared-augmentation threshold packaging across context families.

## Attack 2

Question:
Are new quantities merely renamed existing OCP metrics?

Verdict: `PARTIALLY SURVIVES`.

Reason:
- `CID=0` equivalence is largely a reformulation of shared decoder feasibility.
- But context split and augmentation catalogs add nontrivial classification structure not captured by rank/budget summaries alone.

## Attack 3

Question:
Are witnesses too hand-built or fragile?

Verdict: `PARTIALLY SURVIVES`.

Reason:
- Generator includes constructive families (`shared_exact`, `local_only`) that intentionally realize the split.
- However, opposite-descriptor groups (`23`) and enlargement flips (`94`) indicate behavior is not limited to one handcrafted instance.

## Attack 4

Question:
Do opposite-verdict families disappear under perturbation?

Verdict: `SURVIVES`.

Evidence:
- opposite shared-verdict descriptor groups persist,
- agreement-operator continuation increased opposite groups to `59`,
- family enlargement induces additional flips instead of removing the effect.

Scope caveat:
- robustness still tested on synthetic families; non-synthetic transfer remains open.

## Attack 5

Question:
Does family enlargement destroy the clean split formulation?

Verdict: `SURVIVES` (as a fragility law, not as a collapse).

Evidence:
- `94` `1->0` shared-exactness flips after adding one context.

Interpretation:
- Enlargement is an expected failure mechanism and belongs in the no-go package.

## Attack 6

Question:
Are there false positives where the framework says "interesting" but adds no theorem power?

Verdict: `PARTIALLY SURVIVES`.

Reason:
- Some anomalies are re-encodings of known anti-classifier behavior.
- Strongest additive theorem power remains narrow (conditioned-vs-invariant split, shared-threshold packaging).

## Attack 7

Question:
Does constrained augmentation reduce to raw candidate-library amount (`library_rank_gain`)?

Verdict: `SURVIVES` (amount-only claim fails).

Reason:
- continuation pass produced `14` cases where `library_rank_gain >= free_threshold` but constrained repair still fails.
- positive candidate-library defect (`delta_C > 0`) provides exact impossibility certificate in those cases.

## Final Falsification Outcome

- Strongly surviving main-track core:
  1. conditioned-vs-invariant split on supported families,
  2. positive shared augmentation threshold existence,
  3. multi-context opposite-verdict no-go catalog,
  4. constrained candidate-library defect no-go (`delta_C > 0`).

- Collapsed/limited parts:
  1. claims of broad novelty beyond OCP row-space/fiber core,
  2. unscoped universal statements.

Conclusion:
Keep as a disciplined narrow package with explicit family scope and non-promotion labels.
