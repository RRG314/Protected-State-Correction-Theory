# CFD / PDE Mapping

## Status

`CONDITIONAL` mapping note with real restricted positive and negative results.

## Native field language

Here the native questions are:
- which flow quantities are determined by sparse records?
- when does projection exactly preserve the protected field?
- when do bounded-domain conditions destroy naive reconstruction rules?

## Branch translation

- `F`: restricted flow family,
- `p`: protected velocity field or protected flow functional,
- `M`: retained vorticity, velocity samples, divergence, truncation, or boundary-compatible record,
- exact recoverability: the record determines the protected quantity on the restricted family,
- impossible: the record misses a protected distinction,
- detectable-only: a coarsened flow functional remains recoverable while the full field or stronger functional fails.

## Strongest kept examples

- divergence-only no-go,
- periodic exact projection anchor,
- bounded-vs-periodic transplant failure,
- restricted bounded-domain Hodge positive family,
- weaker-vs-stronger periodic functional split.

## Why this mapping matters

The CFD lane shows that the branch is not only about abstract toy channels.
It applies to real scientific mistakes:
- using the wrong projector,
- overtrusting divergence data,
- assuming sensor count alone is enough,
- confusing recovery of a summary statistic with recovery of the field itself.

## Limitation

This is still a restricted-family theory.
The branch does not solve general PDE inverse problems or general CFD state estimation.
