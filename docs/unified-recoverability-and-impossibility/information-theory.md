# Information-Theory Mapping

## Status

`CONDITIONAL` mapping note.

## Native field language

Classical information theory studies:
- messages,
- channels,
- lossy or noisy encoding,
- distinguishability limits,
- recovery or decoding boundaries.

Classical anchor:
- Claude Shannon, *A Mathematical Theory of Communication* (1948), available through Bell Labs / IEEE reprints.

## Branch translation

- admissible family `F`: allowed message family or structured state family,
- target `p`: message feature or protected content of interest,
- record map `M`: channel output or retained statistic,
- exact recoverability: the output determines the protected content,
- impossibility: distinct protected messages collide at the same output,
- detectable-only: the output determines a coarsened label but not the full message feature.

## Exact match

At the fiber level the match is exact.
If two admissible inputs produce the same retained record but different protected content, exact recovery fails.

## What is kept

Kept branch lesson:
- the universal exactness condition is not invertibility of the whole state;
- it is factorization of the chosen target through the retained record on the chosen admissible family.

That is the right level of generality for:
- lossy summaries,
- sufficient-statistic questions,
- and partial-information recovery.

## What is not claimed

This repo does **not** claim:
- a new Shannon-style capacity theory,
- a replacement for rate-distortion theory,
- or a universal channel theorem.

The branch only borrows the clean structural lesson:
- information loss is target-relative,
- not every lost distinction matters for the chosen task.
