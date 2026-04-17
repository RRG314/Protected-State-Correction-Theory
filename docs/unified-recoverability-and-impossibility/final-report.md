# Final Branch Report

## What this branch is

This branch is a theorem-first attempt to unify recoverability, detectability, and impossibility across several fields without pretending that they all obey one universal law.

It is built around a clean split:
- what survives universally,
- what survives only on restricted families,
- and what broader unification claims fail.

## What was successfully unified

Successfully unified at the exact formal level:
- exact recovery as factorization through the record map,
- impossibility as fiber collision,
- weaker-versus-stronger target logic through coarsenings,
- detectability-only as exact recovery of a nontrivial coarsening while the stronger target fails.

Successfully unified at the restricted theorem level:
- row-space exactness,
- same-rank opposite-verdict counterexamples,
- fixed-library same-budget opposite-verdict counterexamples,
- noisy weaker-versus-stronger separation on the restricted-linear class,
- exact-versus-asymptotic control splits,
- family-level weaker-versus-stronger witnesses.

## What could not be unified honestly

Could not be unified into one serious universal theorem:
- one scalar capacity,
- one threshold law,
- one amount-only exactness classifier,
- one universal detectability notion shared identically by coding, control, QEC, and PDE problems.

That failure is itself one of the branch's main results.

## Strongest surviving result

The strongest surviving result is:

> No rank-only exact classifier theorem:
> even on restricted finite-dimensional linear families, the same ambient dimension, protected rank, and observation rank can produce opposite exactness verdicts.

This means any theory stronger than fiber-factorization must depend on **structure**, not only on amount.

The strongest new strengthening in this deeper pass is:

> even in one fixed coordinate candidate library with unit costs, the same measurement count and the same total budget can produce opposite exactness verdicts.

And the strongest quantitative noisy theorem now kept is:

> a weaker target can remain stably recoverable with error `≤ ||K||_2 η` while the stronger target still carries a noise-independent impossibility floor `Γ/2`.

## What is standard

Standard or standard-adjacent:
- fiber exactness,
- fiber-collision impossibility,
- kernel/row-space exactness,
- much of the basic dictionary language.

## What is plausibly branch-new

Plausibly branch-new or at least repo-new in a meaningful way:
- the exact positioning of unification failure,
- the no-rank-only branch theorem as the clean anti-universal statement,
- the fixed-library same-budget anti-classifier strengthening,
- the noisy weaker-versus-stronger separation theorem,
- the executable branch artifact layer tying the theorem to explicit witnesses across multiple supported examples.

## Best next theorem targets

1. genuinely weighted-cost or geometry-constrained strengthening beyond the solved fixed-library unit-cost case
2. richer noisy weaker-versus-stronger theorems beyond the current single restricted-linear class
3. sharper detectability-only versus asymptotic observer comparison theorem

## Honest verdict

This branch did **not** discover a general theory of recovery across all fields.
What it did discover is where such a theory stops being honest:
- universal exactness is fiber compatibility,
- stronger positive structure is restricted,
- and amount-only unification fails earlier than tempting broad language suggests.
