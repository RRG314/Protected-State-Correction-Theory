# Fibers And Weaker-Vs-Stronger Targets

## Coarsening viewpoint

Let `q = φ ∘ p`.
Then every fiber that is constant for `p` is automatically constant for `q`.
The converse can fail.

That is why weaker targets can remain exact while stronger ones fail.

## Branch results in this language

- `OCP-041`: same-record weaker-versus-stronger split
  - same record fibers
  - weaker target constant on them
  - stronger target not constant on them
- `OCP-048`: detectable-only through target coarsening
  - exact coarsened recovery survives even when the full target fails
- `OCP-051`: noisy weaker-versus-stronger separation theorem
  - weaker target still has a controlled upper bound under record noise
  - stronger target retains a noise-independent impossibility floor

## Practical use

When the strong target fails, there are only a few honest options:
- refine the fibers by adding information
- restrict the admissible family
- or weaken the target until it becomes fiber-constant
