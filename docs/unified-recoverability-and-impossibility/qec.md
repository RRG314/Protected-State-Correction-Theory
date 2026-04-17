# QEC Mapping

## Status

`CONDITIONAL` mapping note with a very strong exact anchor.

## Native field language

Quantum error correction distinguishes:
- logical information,
- admissible error family,
- syndrome sectors,
- exact correction conditions.

Classical anchor:
- Knill and Laflamme, *A Theory of Quantum Error-Correcting Codes* (1996/1997).

## Branch translation

- `F`: code states acted on by the admissible error family,
- `p`: logical information,
- `M`: syndrome or measurement-conditioned sector information,
- exact recoverability: logical state is determined up to the intended correction architecture,
- impossibility: syndrome sectors collide or logical distinctions leak into the same record.

## Exact match

QEC is the strongest exact field dictionary in the repo.
The Knill-Laflamme condition is exactly the right kind of protected-action / sector-separation statement.

## Strongest branch lesson

QEC shows especially clearly that:
- full physical-state inversion is the wrong question,
- logical recoverability is the right question,
- and sector distinguishability is the decisive structural issue.

That is one of the reasons this branch uses target maps rather than full-state invertibility language.

## What is not claimed

The repo does not claim a new QEC theorem.
It uses QEC as:
- an exact anchor,
- a field dictionary,
- and a strong example of detect/correct/impossible separation.
