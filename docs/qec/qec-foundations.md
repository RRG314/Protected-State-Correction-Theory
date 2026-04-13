# QEC Foundations

## Plain-Language Summary

Quantum error correction is the cleanest exact anchor for OCP because it separates three things very clearly:
- the logical information we want to preserve,
- the physical disturbances that hit the encoded state,
- and the recovery process that diagnoses the disturbance and corrects it without destroying the logical state.

This section is a short foundation, not a full QEC textbook.

## 1. Code Space and Logical States

A quantum code selects a **code space** `C` inside a larger physical Hilbert space `H_phys`.

The code space plays the role of the protected object.

A logical state is not stored directly in one physical qubit or mode. It is stored in a redundant embedding so that certain physical errors move the state into distinguishable error sectors.

## 2. Error Set and Recoverability

Fix a collection of physical errors `E_a`.

The exact-correction question is:

> Can we recover every logical state after any error in the chosen set?

The standard answer is given by the Knill-Laflamme condition:

```text
P_C E_a^† E_b P_C = α_ab P_C
```

where `P_C` is the projector onto the code space.

This condition says, roughly, that the code does not let the relevant errors reveal or scramble logical information in a way that makes recovery ambiguous.

## 3. Stabilizer and Syndrome Language

In stabilizer QEC, the code space is defined as the common `+1` eigenspace of a commuting stabilizer set.

Errors push the state into sectors distinguished by syndrome outcomes. Recovery works because the syndrome tells us which correction to apply while preserving the logical information.

That is already extremely close to an OCP architecture:
- protected object: the logical state in the code space,
- disturbance sectors: syndrome-labeled error images,
- correction structure: syndrome extraction plus recovery map.

## 4. Why QEC Is the Best Exact Anchor

QEC gives the cleanest example of all the ingredients OCP needs:
- a protected subspace,
- a disturbance family,
- a distinguishability condition,
- a recovery operator,
- and a sharp line between correctable and uncorrectable architectures.

It also gives natural capacity questions:
- how many errors can be corrected,
- what redundancy is required,
- and when different error images remain distinguishable.

## 5. Important Limitation For OCP

QEC does **not** fit the narrow direct-sum projector model perfectly if we insist on one global additive decomposition `x = s + d` with one disturbance space `D`.

What it really gives is a **family of error sectors**

```text
D_a = E_a C
```

plus a recovery map that uses syndrome information.

That is why the OCP rewrite of QEC must allow a sector-based formulation, not just a single complementary subspace.

## 6. Minimal Example Used In This Repo

The executable code in this repository checks the 3-qubit bit-flip code.

It verifies, for the error set `{I, X_1, X_2, X_3}`, that the relevant Knill-Laflamme residual is numerically negligible.

This does not prove anything new in QEC. Its role is to anchor the OCP formalism in a clean exact example that can be tested locally.
