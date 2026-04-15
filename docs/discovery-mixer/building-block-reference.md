# Discovery Mixer Building-Block Reference

## Typed Object Categories

Every composable object in the mixer carries structural metadata.

Core categories:

- state space
- admissible family
- protected variable / target
- observation / record map
- correction architecture
- generator or asymptotic law
- projection operator
- functional
- threshold or complexity condition
- augmentation candidate
- comparison scenario

## Required Metadata

Each object should be interpretable through at least the following fields:

- object type
- family
- domain
- codomain
- dimension
- basis or representation
- linear / nonlinear status
- support status
- theorem links
- compatibility requirements
- supported diagnostics
- supported augmentation paths

## Why The Typing Exists

The object model prevents misleading compositions such as:

- mixing periodic and bounded-domain basis assumptions without a reduction step
- requesting exact static recovery from an architecture only validated asymptotically
- applying observation rows with the wrong dimension
- attaching unsupported symbolic objects to a theorem-backed linear pipeline

## Reading The Typed Object Inventory

The studio's typed-object panel is meant to answer:

- what exactly did the mixer think the objects were?
- which family did the input reduce to?
- what assumptions were attached?
- what theorem or no-go documents apply?
