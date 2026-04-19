# Descriptor-Fiber Anti-Classifier Branch Overview

This branch extends the anti-classifier program with finite-catalog quantitative diagnostics. Its role is to measure how amount-only descriptors fail and how compatibility information repairs that failure on declared witness families.

The branch sits on top of restricted-linear no-go results (`OCP-049`, `OCP-050`) and family/mismatch fragility results (`OCP-052`, `OCP-053`). It adds three practical quantities: descriptor-fiber mixedness (`DFMI`), irreducible descriptor-only error lower bound (`IDELB`), and compatibility lift (`CL`).

The central contribution is scoped and concrete. On finite generated catalogs, the branch gives a purity criterion for perfect descriptor-only classification, a lower bound for unavoidable descriptor-only error, and an explicit quantitative measure of how compatibility side-information improves classification.

This branch does not replace the core OCP theorem spine, does not claim universal cross-domain invariants, and does not promote catalog-level behavior as unrestricted theorems. Its value is a disciplined quantitative layer attached to already-proved anti-classifier structure.

Canonical references:
- `papers/descriptor-fiber-anti-classifier-branch.md`
- `docs/research-program/descriptor-fiber-anti-classifier-branch-status.md`
- `docs/research-program/descriptor-fiber-anti-classifier-branch-integration-report.md`
- `data/generated/descriptor-fiber-anti-classifier/`
