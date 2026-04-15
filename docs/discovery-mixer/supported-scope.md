# Discovery Mixer Supported Scope

## Supported Families

The mixer currently supports four typed family groups.

### 1. Restricted linear families

Supported objects:

- finite-dimensional state coordinates
- observation matrices or observation rows
- protected linear functionals or protected row blocks
- candidate augmentation rows
- bounded admissible coefficient families

Supported calculations:

- rank checks
- row-space residual checks
- nullspace / collision checks
- exact recoverability checks
- same-rank insufficiency diagnostics
- minimal augmentation count
- candidate augmentation search
- before/after regime comparison

Status:
- strongest theorem-backed branch inside the mixer

### 2. Periodic modal families

Supported objects:

- the repository's finite modal periodic basis
- supported modal functionals in `a1..a4`
- full vorticity, cutoff vorticity, or divergence-only observation choices
- cutoff augmentation on the tracked basis

Supported calculations:

- modal support analysis
- cutoff threshold checks
- exact / impossible classification on the tracked basis
- weaker-versus-stronger target comparison
- before/after cutoff repair comparison

Status:
- family-specific validated branch

### 3. Diagonal / history families

Supported objects:

- diagonal finite-history control family
- sensor profiles on the tracked diagonal spectrum
- moment-type or linear protected targets
- history-horizon changes
- observer-versus-finite-history interpretation

Supported calculations:

- minimal history threshold on supported diagonal families
- exact versus impossible finite-history split
- asymptotic architecture guidance where applicable
- before/after horizon repair comparison

Status:
- family-specific validated branch

### 4. Bounded-domain restricted family

Supported objects:

- boundary-compatible bounded family benchmark
- periodic transplant architecture
- boundary-compatible Hodge architecture
- bounded protected velocity class and divergence certificate targets

Supported calculations:

- architecture mismatch detection
- boundary-compatibility diagnostics
- restricted exact family support
- before/after architecture replacement comparison

Status:
- restricted exact bounded-domain branch plus explicit no-go benchmark

## Controlled Custom Input

Supported custom input is intentionally narrower than the structured mixer.

### Custom linear input

Allowed:

- numeric row matrices
- expressions in `x1..xn`
- linear protected functionals
- candidate augmentation rows

Rejected:

- nonlinear functions such as `sin(x2)` or `x1*x2`
- constant-offset functionals
- undeclared variables
- dimension mismatches

### Custom periodic input

Allowed:

- linear modal functionals in `a1..a4`
- supported periodic observation choice
- supported cutoff choice

Rejected:

- nonlinear modal expressions
- references outside the tracked four-mode basis
- mixed periodic and bounded-domain assumptions

### Custom control input

Allowed:

- explicit diagonal sensor profile vectors
- targets such as `x3`, `moment(2)`, or other supported linear functionals on `x1..xn`
- supported finite-history horizons

Rejected:

- unsupported nonlinear target syntax
- profiles or targets outside the tracked diagonal family size

## Unsupported Input Classes

The mixer currently does not support:

- arbitrary nonlinear state equations
- arbitrary symbolic PDEs
- arbitrary coupled operator algebras
- generic bounded-domain basis design outside the tracked benchmark family
- arbitrary quantum circuit or full symbolic QEC composition
- general-purpose CAS reduction

When the mixer rejects an input, it should also explain the nearest supported reformulation whenever one exists.

## Evidence-Level Meaning

- theorem-backed: supported by a proved repo theorem on the active family
- restricted exact theorem-backed: exact only on an explicit restricted family
- family-specific validated result: validated computationally on the tracked family, not promoted as broad theorem
- benchmark-guided empirical result: useful diagnostic or repair flow supported by benchmark results
- heuristic: suggestion only, not a promoted theorem or benchmarked guarantee
- unsupported: not analyzable by the current engine
