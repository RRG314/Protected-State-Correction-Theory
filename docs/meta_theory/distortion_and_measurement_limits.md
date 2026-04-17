# Distortion and Measurement Limits

Date: 2026-04-17

## Purpose

Test whether a common “distinction-loss” mechanism explains exactness failure across branches without vague language.

## Formal Definitions

Let `(A, T, M)` be admissible family, target, and representation/record map.

- **Target-distinguishing collision:**
  `exists x1, x2 in A` with `M(x1)=M(x2)` and `T(x1)!=T(x2)`.

- **`T`-distorting map:**
  A map `M` that admits target-distinguishing collisions on `A`.

- **Compatibility-preserving representation:**
  A representation with no target-distinguishing collisions (equivalently, exact factorization possible).

These definitions are exact for static recoverability branches.

## Cross-Branch Tests

### 1. Fiber collisions (OCP recoverability)
- Mechanism: explicit target-distinguishing record collisions.
- Status: `PROVED` no-go (universal core form).
- Interpretation: direct evidence for `T`-distortion definition.

### 2. Symmetry-blind observations (soliton lane)
- Mechanism: symmetry-invariant observation collapses quotient distinctions.
- Status: symmetry no-go `PROVED`; broader injectivity claims `CONDITIONAL/VALIDATED`.
- Interpretation: same distinction-loss mechanism under quotient structure.

### 3. Family-enlargement false positives (restricted-linear)
- Mechanism: enlarged family introduces hidden kernel directions that collapse distinctions.
- Status: `PROVED` on supported class.
- Interpretation: distortion appears after family change, not necessarily in the original family.

### 4. Model-mismatch instability
- Mechanism: decoder representation is mismatched to true family, creating effective distortion of target distinctions.
- Status: canonical mismatch theorem `PROVED` on supported class.
- Interpretation: distinction-loss can come from wrong model class, not only raw sensor map.

### 5. Bounded-domain projection mismatch
- Mechanism: scalar divergence reduction fails to preserve target-relevant boundary-compatible structure.
- Status: no-go `PROVED`; restricted positive bounded class also exists.
- Interpretation: this is compatibility-loss beyond pure observation collapse.

### 6. Variable-resistivity MHD obstruction
- Mechanism: closure representation with variable `eta(r)` and domain class can obstruct exact closure.
- Status: `PROVED ON SUPPORTED FAMILY` package.
- Interpretation: best described as operator/profile/domain incompatibility, not measurement collapse alone.

### 7. SDS tool-layer analogues
- Mechanism: unsupported reductions and architecture mismatch are diagnosed explicitly.
- Status: `VALIDATED` tool behavior, not theorem-core.
- Interpretation: engineering reflection of theorem branches, not independent proof.

## Is distortion “just fiber collapse”?

- **Yes** for static record-based exactness (`A, T, M`) branches.
- **No** as a full cross-branch statement unless expanded to include operator/domain/evolution compatibility loss.

## Clean Abstract Statement (survives)

`Distinction-loss/compatibility-loss principle`:
- Exactness fails when the adopted representation/operator architecture does not preserve target-relevant distinctions on the declared admissible family.

Status: `CONDITIONAL` as a broad meta-statement; theorem-grade in multiple subcases.

## What is rejected

Rejected wording:
- “all failure is measurement distortion.”

Reason:
- Some failures are domain/operator compatibility obstructions rather than sensor-map collapse.
