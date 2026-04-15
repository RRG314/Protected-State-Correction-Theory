# Discovery Mixer Limitations And Unsupported Cases

## The Main Limit

The mixer is intentionally typed and narrow.
It is designed to reject unsupported compositions rather than pretend to solve them.

## Current Unsupported Areas

- arbitrary nonlinear symbolic systems
- generic symbolic PDE composition
- arbitrary quantum circuit composition
- unrestricted bounded-domain basis synthesis
- general-purpose theorem proving on user-entered expressions
- automatic reduction of mixed-family symbolic problems into validated theorem branches

## Why These Limits Exist

The repository is trying to remain trustworthy.
Broad symbolic claims would quickly outgrow the branch-level theorems and validations the repo currently has.

## Interpretation For Users

Unsupported does not mean the underlying research question is meaningless.
It means the current workbench cannot analyze that case honestly without adding a new validated family reduction or theorem path first.
