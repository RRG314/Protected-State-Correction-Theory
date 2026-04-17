# Same-Rank / Same-Budget Anti-Classifier Report

## Purpose

This note collects the branch's cleanest sensor-design and observability falsifications.

## `OCP-047` same-rank insufficiency

Same observation rank does not determine exact target recoverability.
That already kills naive amount-only observability language.

## `OCP-049` no rank-only exact classifier theorem

For every supported dimension/rank pattern in the theorem statement, equal observation rank can still coexist with opposite exactness verdicts.

Artifact:
- [`rank_only_classifier_witnesses.csv`](../../data/generated/unified-recoverability/rank_only_classifier_witnesses.csv)

## `OCP-050` no fixed-library budget-only exact classifier theorem

Even inside one fixed candidate library with unit costs, equal sensor count and equal total budget can still coexist with opposite exactness verdicts.

Artifact:
- [`candidate_library_budget_witnesses.csv`](../../data/generated/unified-recoverability/candidate_library_budget_witnesses.csv)

## Why this matters outside the repo

These are direct warnings against:
- rank-only observability claims,
- count-only sensor placement claims,
- budget-only exactness claims,
- and any report that treats raw amount as a sufficient identifiability statistic.
