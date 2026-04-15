# Recoverability / Correction Studio

## Purpose

The Recoverability / Correction Studio is the most decision-oriented surface in the repository.

It is meant to answer a practical question before a user starts building a correction scheme:

- what protected variable am I actually trying to preserve?
- what record do I really have?
- does that record support exact recovery, only weaker recovery, only asymptotic recovery, or no recovery at all?
- what should I add or change next?

## Studio Workflow

1. Choose a system family.
2. Choose the protected variable.
3. Choose the available record or observation map.
4. Inspect `κ(0)`, `κ(δ)`, finite recovery error, and the branch classification.
5. Read the guidance layer:
   - blocker
   - missing structure
   - recommended architecture
   - weaker recoverable target if available
   - no-go label if a naive approach is blocked
6. Export or save the scenario if it is worth keeping.

## Supported Lanes

### Analytic benchmark
- use for explicit `κ(η)/2` lower-bound reading
- use for conditioning / robustness questions

### Qubit fixed-basis record
- use for phase-loss and weaker-variable recovery
- strongest lesson: weaker protected targets can remain exactly recoverable after stronger ones fail

### Periodic incompressible modal family
- use for cutoff / retained-information thresholds
- strongest lesson: exact recovery is tied to protected support in the retained modal record

### Functional observability / control family
- use for finite-history versus observer-style recovery
- strongest lesson: exact static recovery and asymptotic observer recovery are distinct design choices

### Reusable linear template
- use for static record sufficiency, minimal augmentation, and ambiguity witness generation
- strongest lesson: exact recovery is a row-space question on the restricted family

## Guidance Logic

The studio guidance is not generic filler.

It is driven by the current branch results.

Examples:
- if `κ(0) > 0`, the guidance reports that exact recovery is blocked and looks for the missing structure that would separate the observation fibers
- if a weaker protected target is already recoverable, the guidance says so directly instead of implying that the full target can be saved
- if asymptotic recovery exists but exact finite-history recovery fails, the guidance points toward observer-style architectures instead of pretending that a static inverse exists
- if the problem is impossible inside the current candidate record library, the guidance says that explicitly

## What The Studio Is Good For

- screening whether a design problem is structurally solvable
- deciding whether to enrich the record or weaken the target
- finding a minimal record change on restricted linear families
- seeing whether a threshold law is present on a tested family
- understanding why a naive recovery architecture fails

## What The Studio Is Not

- a black-box solver for arbitrary nonlinear systems
- a claim that every system has one clean scalar capacity number
- a substitute for the theorem or no-go documents
- a guarantee that a family-level threshold extends automatically outside its tested class
