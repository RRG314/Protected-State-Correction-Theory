# Coding-Theory Mapping

## Status

`CONDITIONAL` mapping note with exact internal examples.

## Native field language

Coding theory distinguishes:
- detectability,
- correctability,
- and undecidable ambiguity.

Classical anchor:
- R. W. Hamming, *Error Detecting and Error Correcting Codes* (1950).

## Branch translation

- `F`: admissible codewords and admissible error family,
- `p`: original message or logical content,
- `M`: received word, parity record, or syndrome record,
- exact recoverability: the record determines the message,
- detectable-only: the record determines that an error occurred, or which error class occurred, but not the original message,
- impossibility: multiple message/error combinations share the same received record while carrying different protected content.

## Exact match

This is one of the branch's cleanest cross-field matches.
The branch's weaker-versus-stronger target formalism is exactly the right language for:
- detect vs correct,
- syndrome separation,
- and parity-only partial diagnosis.

## Strongest branch lesson

The same record may support:
- a weaker decision target such as “error present?” or “which syndrome sector?”
- while failing to determine the stronger target “which original message/logical state?”

That is not a loose analogy.
It is a direct instance of the detectable-only regime.

## What is not claimed

The repo does not rebuild classical code-distance theory.
It uses coding theory as a clean dictionary for:
- exact vs detectable-only,
- fiber collisions,
- and minimal extra structure.
