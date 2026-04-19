# Theorem Dependency Map

Date: 2026-04-17

## 1) Dependency Graph (Logical)

```mermaid
graph TD
  U1["UCT-1 Factorization/Fiber Exactness"]
  U2["UCT-2 Collision No-Go"]
  U3["UCT-3 Coarsening Monotonicity"]

  B11["B1 Restricted-Linear Compatibility OCP-031"]
  B12["B1 Minimal Augmentation OCP-045"]
  B13["B1 Anti-Classifier OCP-049/050"]
  B14["B1 Family Enlargement OCP-052"]
  B15["B1 Model Mismatch OCP-053"]
  B16["B1 Bounded-Domain No-Go OCP-023/028"]
  B17["B1 Bounded Restricted Exactness OCP-044"]
  B18["B1 Soliton Quotient/Same-Count Package"]
  B19["B1 MHD Obstruction/Survivor Package"]

  E1["E Structural Discovery + Mixer"]

  U1 --> U2
  U1 --> U3
  U1 --> B11
  B11 --> B12
  B11 --> B13
  B11 --> B14
  B11 --> B15
  U2 --> B16
  B16 --> B17
  U1 --> B18
  U2 --> B18
  U2 --> B19

  B11 --> E1
  B13 --> E1
  B16 --> E1
  B17 --> E1
```

## 2) Dependency Notes

1. `UCT-1` is the primary abstract root for recoverability statements.
2. `UCT-2` is a no-go corollary of `UCT-1` and supports multiple branch obstruction packages.
3. Restricted-linear package (`OCP-031`,`045`,`049`,`050`,`052`,`053`) forms the densest theorem chain.
4. Bounded-domain positive theorem (`OCP-044`) depends on no-go boundary logic to prevent overpromotion.
5. Soliton and MHD packages map to root core via restricted translations, not full identity.
6. Engineering layers depend on theorem packages; they do not sit above them.

## 3) Governance Dependency Rule

A result may only be promoted upward in hierarchy if all of its parent assumptions/dependencies are satisfied in the target branch.
