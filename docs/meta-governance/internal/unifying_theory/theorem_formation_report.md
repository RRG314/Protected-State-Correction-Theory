# Theorem Formation Report

Date: 2026-04-17

Method used for each candidate:
1. strongest plausible statement,
2. weakest provable version,
3. proof/disproof pressure,
4. final status.

## UTH-C1: Fiber-Factorization Exactness

### Strongest version
For any branch representable as `(A,T,M)`, exact recoverability holds iff `T` factors through `M` on `A`.

### Weaker provable version
Same statement for declared recoverability branches where record and target maps are explicit.

### Pressure
- Matches OCP `OCP-030` and restricted-linear `OCP-031`.
- Matches soliton recoverability formulation on declared quotient classes.
- MHD uses compatibility equations not always written as explicit record-map inversion; forced transfer would distort.

### Final status
`PROVED` as universal recoverability core theorem.

## UTH-C2: Abstract Anti-Classifier Theorem

### Strongest version
No amount-only summary (rank/count/budget/dimension/history length) can classify exactness in any branch.

### Weaker provable version
No rank-only and no fixed-library budget-only exact classifier on supported restricted-linear class; same-count opposite-verdict witnesses on supported soliton families.

### Pressure
- OCP gives theorem-grade negative package (`OCP-049`,`OCP-050`).
- Soliton gives `PROVED ON SUPPORTED FAMILY` + `CONDITIONAL` continuous extension.
- MHD and SDS not naturally amount-classifier problems in same formal sense.

### Final status
- strongest version: `REJECTED` / too broad,
- weaker version: `PROVED ON SUPPORTED FAMILY` (OCP), plus restricted analogue in soliton lane.

## UTH-C3: Family-Enlargement Fragility Theorem

### Strongest version
Exactness on a small class never guarantees exactness on enlarged class (universal statement across all branches).

### Weaker provable version
In declared restricted-linear setting, exactness on `A_s` can fail on `A_l` with explicit witness/lower-bound (`OCP-052`).

### Pressure
- OCP theorem strong.
- Soliton and MHD show matching pattern but not same universal formal theorem class.

### Final status
- strongest version: `CONDITIONAL` at best (not promoted universal),
- weaker version: `PROVED` in OCP supported family.

## UTH-C4: Model-Mismatch Instability Theorem

### Strongest version
Any exact decoder is unstable under any nonzero model mismatch.

### Weaker provable version
Canonical restricted-linear family theorem with explicit mismatch error floor (`OCP-053`).

### Pressure
- Explicit proved formula exists in canonical class.
- Broad universal instability for all branches unproved; some branches may be robust under structured mismatch.

### Final status
- strongest version: `REJECTED` as universal claim,
- weaker version: `PROVED` on canonical supported class.

## UTH-C5: Structural Compatibility Master Theorem (Recoverability + Preservation)

### Strongest version
Single compatibility law completely characterizes exactness/preservation/failure across OCP, soliton, MHD, SDS.

### Weaker provable version
Branch-limited schema: each branch has explicit compatibility equations and obstruction sets; exactness holds only when branch-specific compatibility conditions are satisfied.

### Pressure
- OCP and MHD have strong compatibility equations but different objects.
- SDS engineering layers are not theorem-complete characterizations.
- Emergence/self-organization not reducible to same static compatibility law.

### Final status
- strongest version: `REJECTED`,
- weaker schema: `CONDITIONAL` (useful organizational theorem-template, not promoted as one theorem).

## Promotion Summary

Promote:
- UTH-C1 (`PROVED` universal recoverability core),
- UTH-C2 weaker form (`PROVED ON SUPPORTED FAMILY`),
- UTH-C3 weaker form (`PROVED` in supported class),
- UTH-C4 weaker form (`PROVED` canonical supported class).

Do not promote:
- universal anti-classifier statement across all branch types,
- universal preservation/emergence compatibility theorem.
