# Continuous Quantum Error Correction

## Plain-Language Summary

Continuous quantum error correction is one of the most promising citable expansion directions, but it is not yet a promoted theorem branch in this repository.

It matters because it sits near the exact QEC anchor while using continuous monitoring, feedback, or engineered dissipation rather than a single syndrome-and-recovery step.

## System Definition

The protected object is still the logical/code sector.
The disturbance family consists of correctable error channels together with the continuously monitored or continuously damped error coordinates.

## Correction Architecture

Depending on the setup, the correction architecture is one of:
- continuous measurement plus feedback,
- autonomous or engineered dissipation,
- or a hybrid monitored-feedback loop.

In OCP language, this makes it a bridge candidate between:
- exact sector recovery, and
- asymptotic continuous correction.

## Exact Or Asymptotic?

Usually **asymptotic** or **measurement-conditioned exact** rather than globally exact in one unconditional step.

That is why the repo keeps this direction as conditional.

## What OCP Adds

OCP helps separate three things that are easy to blur together:
- exact sector recovery in the standard discrete QEC picture,
- continuous suppression of error syndromes or violation coordinates,
- and the no-go question of when distinguishability is too weak for reliable recovery.

## Fit Verdict

Verdict: **keep** as a conditional bridge and citable future direction.

Do not promote it as a new theorem branch yet.

## What To Cite

Useful outside anchors:
- [Ahn, Doherty, and Landahl, "Continuous quantum error correction via quantum feedback control" (Phys. Rev. A 65, 042301, 2002)](https://doi.org/10.1103/PhysRevA.65.042301)
- [Knill and Laflamme, "A theory of quantum error-correcting codes" (foundational preprint)](https://arxiv.org/abs/quant-ph/9604034)

## Limit

The repository does not yet prove a new continuous-QEC theorem. This direction is kept because the operator language is real, the literature is strong, and the bridge could become mathematically meaningful if the continuous measurement and feedback structure is formalized more sharply.
