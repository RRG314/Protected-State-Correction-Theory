# Discovery Mixer Compatibility Rules

## Core Compatibility Checks

The composition engine checks at least the following.

### 1. Domain and codomain compatibility

Does each map accept the kind of object the previous map outputs?

### 2. Dimension compatibility

Do the row counts, coordinate counts, and basis sizes match?

### 3. Variable consistency

Are all symbolic variables declared and in-range for the chosen basis?

### 4. Family consistency

Does the composition stay inside one supported family, or is there a validated reduction step?

### 5. Target compatibility

Is the protected target compatible with the chosen record on the admissible family?

### 6. Architecture compatibility

Is the chosen architecture exact, asymptotic, family-specific, or unsupported for this task?

### 7. Known no-go checks

Does the composition trigger a stored obstruction such as:

- non-separating record fibers
- insufficient row-space support
- insufficient cutoff support
- insufficient history horizon
- bounded-domain projector transplant failure
- weaker-versus-stronger target split

## Example Diagnostic Messages

Typical messages include:

- `record map does not separate the target on the admissible family`
- `history horizon is below the proven exact threshold for this functional`
- `periodic projector transplant is incompatible with the bounded protected class`
- `custom equation cannot be reduced to a supported linear or modal family`
- `full target is impossible, but a weaker target is exact under the same record`

## Design Principle

The engine prefers explicit structural failure explanations over generic incompatibility messages.
