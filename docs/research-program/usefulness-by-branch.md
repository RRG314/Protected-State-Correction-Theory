# Usefulness by Branch

This document explains the practical value of each major branch in the repository. The goal is to clarify decision value, not to repeat theorem titles.

## Foundational OCP branch

Use this branch when you need the cleanest exact-versus-no-go baseline. It tells you whether a protected/disturbance decomposition supports exact correction at all and provides the formal language used across the rest of the repository.

## Exact sector / QEC anchor

Use this branch when disturbance is sector-structured and sector distinguishability is central. It is the strongest exact anchor beyond the plain projector case and provides the right model for sector overlap failure.

## Continuous asymptotic branch

Use this branch when exact one-step correction is unavailable but invariant-split damping or observer-style asymptotic suppression is realistic. It gives architecture guidance: when to stop asking for finite-time exactness and switch to asymptotic design.

## Restricted-linear recoverability branch

Use this branch when records are constrained and you need explicit criteria for exactness, impossibility, or repair. This is the branch that most directly supports design questions such as “is this record enough?” and “what is the smallest augmentation that restores exactness?”

## Fiber-based anti-classifier branch

Use this branch when you need to prevent overclaiming from amount-only summaries. It is the main mechanism for showing why same-rank or same-budget systems can produce opposite exactness outcomes, and why family-enlargement or mismatch can create false confidence.

## Descriptor-fiber quantitative branch

Use this branch when you need finite-class diagnostics that quantify descriptor insufficiency rather than only naming it. It is particularly useful for comparing amount-only descriptors to compatibility-enriched descriptors under explicit witness sets.

## Adjacent TSIT quantitative extension lane

Use this lane when the decision problem is explicitly target-specific and you need to compare design/allocation/context choices under fixed information budgets. It is useful for diagnostic and benchmark leverage, but it does not replace core recoverability criteria and remains non-promoted.

## Bounded-domain / CFD obstruction branch

Use this branch when moving from periodic theory to bounded domains. It gives the strongest guardrails against naive projector transfer and identifies where restricted bounded exactness is actually supported.

## Structural Discovery and Discovery Mixer

Use these surfaces when converting theory into decisions. They are valuable because they enforce supported-family boundaries while still giving practical guidance: diagnose failure, test repairs, compare regimes, and export reproducible evidence.

## Practical takeaway

The repository is most useful when branches are used together with clear hierarchy: foundation first, branch-specific criteria second, tooling for decision support third. Skipping that hierarchy is the main way users overread results.
