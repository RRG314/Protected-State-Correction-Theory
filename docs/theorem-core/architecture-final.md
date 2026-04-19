# Final Architecture

The repo is organized around one stable core and several branch-limited lanes.

The core gives the shared mathematical language: exact recovery, asymptotic recovery, and explicit no-go boundaries. Branches then add stronger results on narrower families.

Tooling and apps come after theorem status, not before it. Workbench output is evidence only when it links back to theorem or validation anchors.

## Layer 1: theorem backbone

This layer contains the promoted theorem and no-go spine:
- `docs/theorem-core/theorem-spine-final.md`
- `docs/theorem-core/no-go-spine-final.md`
- `papers/ocp_core_paper.md`

## Layer 2: restricted strengthening lanes

These lanes add branch-limited structure, such as constrained observation, fiber impossibility, augmentation design, context-sensitive diagnostics, and PDE-domain limits.

## Layer 3: methods and validation

Methods and diagnostics live in `docs/methods-diagnostics/`.
Validation and artifact trust paths live in `docs/validation-evidence/`.

## Practical reading order

1. theorem spine
2. no-go spine
3. one restricted branch you care about
4. corresponding methods and validation artifacts

## Nonclaims that shape this architecture

The architecture does not claim:
- one universal scalar recoverability invariant,
- one universal bounded-domain projector law,
- one cross-branch law that removes branch assumptions.

Those are either disproved, unsupported, or still open.
