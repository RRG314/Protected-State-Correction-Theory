# Projection Candidates

Status: projection-method discovery and reduction analysis.
Primary data: `data/generated/operator_discovery/operator_witness_catalog.csv`.

## P1. Stack Row-Space Projection (Baseline)

Definition:
Project target row `t` onto rowspace of `M_stack` and use residual
`rho_stack = ||t - Proj_row(M_stack)(t)||_2`.

Role:
- baseline exactness proxy for stacked representation.

Observed behavior:
- many cases with near-zero stack residual but invariant exactness failure (`491` cases in operator catalog).

Conclusion:
- useful baseline but insufficient for context-invariant exactness.

Status:
- `PROVED ON SUPPORTED FAMILY` insufficiency witness.
- Novelty: `ALREADY KNOWN IN SUBSTANCE`.

## P2. Mean-Context Projection Residual

Definition:
`rho_ctx_mean = mean_c ||t - Proj_row(M_c)(t)||_2`.

Role:
- summarizes local/contextwise projection quality.

Observed behavior:
- captures local exactness trends but cannot enforce shared decoder constraints.

Conclusion:
- helpful descriptive metric; not a theorem classifier.

Status:
- `VALIDATED / EMPIRICAL ONLY`.
- `REDUCES TO EXISTING OCP LOGIC`.

## P3. Projection Gain Functional

Definition:
`PG = rho_ctx_mean - rho_stack`.

Role:
- measures benefit from context stacking.

Observed behavior:
- mean `PG ~ 0.8075` in operator catalog, but high gain does not imply shared exactness.

Conclusion:
- computationally useful, theorem-insufficient alone.

Status:
- `VALIDATED / EMPIRICAL ONLY`.
- `CLOSE PRIOR ART / REPACKAGED`.

## P4. Context-Intersection Projection (Candidate)

Proposed form:
Project onto intersection-compatible decoder set induced by all contexts (implemented implicitly via CID/CLE rather than explicit projector matrix in this pass).

Role:
- enforce shared compatibility rather than stacked span only.

Reduction check:
- collapses to lifted feasibility/CID computation in linear core.

Status:
- `REDUCES TO EXISTING OCP LOGIC`.
- no distinct projection theorem found.

## Projection Discovery Verdict

- No genuinely new projection method survived as mathematically distinct.
- Strong negative result: projection of stacked rows is not enough for shared recoverability.
- Practical outcome: keep projection diagnostics as support, push decoder-compatibility equations for theorem work.
