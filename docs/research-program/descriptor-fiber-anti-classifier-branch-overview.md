# Descriptor-Fiber Anti-Classifier Branch Overview

This branch extends the anti-classifier program with finite-catalog quantitative diagnostics. The technical role is to measure failure of amount-only descriptors and quantify how compatibility information reduces that failure on declared witness families.

It builds on restricted-linear no-go results (`OCP-049`, `OCP-050`) and family/mismatch fragility results (`OCP-052`, `OCP-053`). The branch introduces three quantities: descriptor-fiber mixedness (`DFMI`), irreducible descriptor-only error lower bound (`IDELB`), and compatibility lift (`CL`).

On finite generated catalogs, the branch provides:

- a purity criterion for perfect descriptor-only classification,
- a lower bound for unavoidable descriptor-only error,
- a quantitative measure of improvement from compatibility side-information.

Scope boundaries:

- this branch supplements the OCP theorem spine and does not replace it,
- catalog-level behavior is not promoted as unrestricted theorem-level behavior,
- no universal cross-domain invariant is claimed.

Canonical references:

- `papers/descriptor-fiber-anti-classifier-branch.md`
- `docs/research-program/descriptor-fiber-anti-classifier-branch-status.md`
- `docs/research-program/descriptor-fiber-anti-classifier-branch-integration-report.md`
- `data/generated/descriptor-fiber-anti-classifier/`
