# Quantum-OCP Test Validity Audit

Status: conceptual-audit layer for whether the implemented tests answer the intended quantum questions.

Primary artifacts audited:
- `data/generated/quantum_ocp/quantum_witness_catalog.csv`
- `data/generated/quantum_ocp/quantum_anomaly_catalog.csv`
- `scripts/compare/run_quantum_ocp_pass.py`

## TV1. Fixed-Basis Collision Test (`QW001`)

Question tested:
- Can a single fixed basis recover a phase-sensitive target on a family with phase variation?

Metric used:
- exact recoverability via record-collision check.

Validity assessment:
- Correct metric for exact decoder existence.
- Not merely attractive numerics; logical impossibility follows from collisions.

Risk:
- Family is discrete/sampled; does not by itself prove continuous-family statements.

Verdict:
- Test is conceptually valid for supported family.

## TV2. Basis-Sensitive Opposite-Verdict Pair (`QW001/QW002`)

Question tested:
- Does basis choice matter beyond setting count for a fixed target?

Metric used:
- same descriptor signature + opposite exactness.

Validity assessment:
- Correct for anti-classifier claim in this finite class.
- Not enough alone to claim broad new quantum theorem.

Verdict:
- Valid for scoped no-go/design split.

## TV3. Conditioned vs Invariant Split (`QW005-QW008`)

Question tested:
- Can each context be exact while no shared decoder exists?

Metric used:
- per-context exactness + explicit shared-decoder incompatibility.

Validity assessment:
- Directly measures intended property.
- Main caveat: contexts are modeled as gain-scaled channels (a simplified context model).

Verdict:
- Valid and mathematically sharp on supported family.

## TV4. One-Added-Measurement Restoration (`QW003/QW004`)

Question tested:
- Can adding one complementary setting restore full target recoverability?

Metric used:
- exact recoverability change from one-setting to two-setting record.

Validity assessment:
- Appropriate for finite sampled phase target.
- Not equivalent to global informational completeness claim for arbitrary state families.

Verdict:
- Valid for finite sampled theorem candidate; do not overgeneralize.

## TV5. Distributed Allocation Split (`QW009/QW010`)

Question tested:
- Does subsystem allocation geometry matter beyond total measurement budget?

Metric used:
- matched budget (`measurement_count=2`) with opposite target recoverability.

Validity assessment:
- Correct metric for allocation-sensitive target accessibility.
- Family is hand-constructed but nontrivial and interpretable.

Verdict:
- Valid for scoped distributed no-go.

## TV6. Dephasing Fragility Sweep (`QW011-QW017`)

Question tested:
- How does environment-induced dephasing affect target recoverability and Fisher sensitivity?

Metric used:
- exactness under fixed target pair and FI under dephasing parameter sweep.

Validity assessment:
- Correctly tied to selected target and channel model.
- Not a universal open-system law; channel and target are fixed.

Verdict:
- Valid as benchmark fragility lane.

## TV7. Fisher Design Split (`QW019-QW024`)

Question tested:
- Can same setting count hide major target sensitivity differences?

Metric used:
- target FI comparison under phase-blind vs phase-sensitive settings.

Validity assessment:
- Correct for local sensitivity question.
- Does not by itself prove exact recoverability theorem; should remain empirical/diagnostic.

Verdict:
- Valid diagnostic; keep status `VALIDATED / EMPIRICAL ONLY`.

## TV8. Robustness Checks

Implemented check:
- perturbation-based verdict persistence (`robustness_fraction`) in each witness row.

Assessment:
- Useful guard against knife-edge exactness artifacts.
- Does not replace symbolic proof for broader classes.

## Overall Validity Conclusion

- Core exactness/no-go tests are correctly aligned to decoder-existence questions.
- Most overreach risk comes from interpretation scope, not from metric mismatch.
- Safe boundary: claim finite-family theorem/no-go/design splits; avoid foundational or universal quantum claims.
