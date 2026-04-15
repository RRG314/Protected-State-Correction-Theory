# Discovery Mixer Demo Walkthroughs

## Demo 1 — User-built periodic failure and fix

Scenario:
- choose the periodic modal family
- choose a stronger functional with support beyond the retained cutoff
- choose cutoff vorticity with too small a cutoff

Expected diagnosis:
- exact recovery fails because hidden support lies outside the retained record
- the mixer reports the predicted minimum cutoff

Expected repair:
- raise the cutoff to the smallest value that covers the protected support
- re-run analysis
- exact recovery becomes available on the tracked family

## Demo 2 — User-built control history failure and fix

Scenario:
- choose the diagonal/history family
- choose a moment-type or protected-coordinate target
- set a history horizon below the tracked threshold

Expected diagnosis:
- the target is impossible under the current finite history
- the mixer reports horizon insufficiency

Expected repair:
- extend the horizon to the smallest supported value
- exact recovery becomes available on the tracked family

## Demo 3 — Weaker-versus-stronger target discovery

Scenario:
- keep the same record
- compare a stronger target with a weaker target

Expected diagnosis:
- stronger target remains impossible under the current record
- weaker target is exact under the same record

Expected redesign paths:
- weaken the target
- or enrich the record

## Demo 4 — Custom matrix / functional input

Scenario:
- enter a valid restricted-linear observation system and a protected functional
- provide candidate augmentation rows

Expected diagnosis:
- current record is structurally insufficient
- row-space logic identifies the missing protected direction

Expected repair:
- add one candidate row
- re-run analysis
- exact recovery becomes available

## Demo 5 — Structured randomized search

Scenario:
- run seeded random exploration inside a supported family

Expected behavior:
- the mixer returns a reproducible case
- the case includes a regime verdict, root cause, and repair path if found
- the exported case can be replayed using the same seed
