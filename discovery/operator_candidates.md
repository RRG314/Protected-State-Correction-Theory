# Operator Candidates

Status: discovery-track operator candidates with falsification labels.
Primary data: `data/generated/operator_discovery/operator_witness_catalog.csv` (1000 rows), `operator_anomaly_catalog.csv` (26 rows).
Continuation data: `data/generated/context_sensitive_recoverability/agreement_operator_witness_catalog.csv` (300 rows).

## O1. Shared Decoder Compatibility Operator (SDCO)

Definition:
`SDCO(F,t) = I(exists d_*: forall c, d_* M_c = t)`.
Equivalent computational form: solve lifted system `A d = b` and threshold residual.

Problem addressed:
- exact shared-decoder feasibility across contexts.

Observed utility:
- clean classifier for invariant exactness in supported family.

Reduction check:
- exactly equivalent to existing shared-decoder feasibility condition.

Status:
- Mathematical: `PROVED` equivalence.
- Novelty: `REDUCES TO EXISTING OCP LOGIC`.

## O2. Context Compatibility Defect Operator (CCD)

Definition:
`CCD(F,t) = CID(F,t) = min_d max_c ||d M_c - t||_2`.

Problem addressed:
- quantitative defect when invariant exactness fails.

Observed utility:
- in catalog, `CID` spans `[0, 8.2689]` and ranks local-exact/global-fail severity.

Reduction check:
- quantitative extension of the same lifted feasibility object.

Status:
- `VALIDATED / EMPIRICAL ONLY` as useful scalar diagnostic.
- `REDUCES TO EXISTING OCP LOGIC`.

## O3. Augmentation Gain Operator (AGO)

Definition:
For admissible augmentation class `A`:
`AGO(F,t;A) = CID_before - CID_after(U_*)`,
where `U_*` is best shared augmentation found in search class.

Problem addressed:
- quantify compatibility improvement from shared augmentation.

Observed utility:
- positive gain detected on `267` local-exact/global-fail cases in operator catalog.

Reduction check:
- depends strongly on augmentation admissibility; not invariant across augmentation classes.

Status:
- `PROVED ON SUPPORTED FAMILY` for positive-gain existence in declared search class.
- Novelty: `PLAUSIBLY DISTINCT` as computational operator package, theorem novelty still conditional.

## O4. Collapse Index Operator (CIO)

Definition:
`CIO(F,t) = fraction of target-disagreeing pairs among record-colliding pairs`.

Problem addressed:
- fiber-collision severity under finite witness sampling.

Observed utility:
- distinguishes severe collapse versus mild collapse in same rank classes.

Reduction check:
- direct finite-sample operationalization of fiber-collision logic.

Status:
- `VALIDATED / EMPIRICAL ONLY`.
- `REDUCES TO EXISTING OCP LOGIC` (useful diagnostic form).

## O5. Lift Conditioning Operator (LCO)

Definition:
`LCO(F) = sigma_min(A)` where `A=[M_1^T;...;M_k^T]`.

Problem addressed:
- numerical conditioning/stability margin of lifted equation.

Observed utility:
- nontrivial diagnostics for solver robustness.

Falsification:
- anomaly `lift_conditioning_not_sufficient` shows conditioning does not classify exactness on its own.

Status:
- `VALIDATED / EMPIRICAL ONLY`.
- `DISPROVED` as exact classifier.

## O6. Candidate-Library Defect Operator (CLDO)

Definition:
For agreement-lifted matrix `G`, target `L`, and admissible row library `C`:
`CLDO = delta_C = rank([G; C; L]) - rank([G; C])`.

Problem addressed:
- certify whether constrained augmentation libraries can, in principle, restore shared exactness.

Observed utility:
- exact full-library feasibility certificate in supported linear class,
- detects impossible libraries even when raw library rank gain is high.

Continuation evidence:
- `14` `delta_C > 0` impossibility cases,
- `14` cases with `library_rank_gain >= free_threshold` but still infeasible.

Reduction check:
- linear-algebraic rank inclusion test; not a broad standalone operator theory.

Status:
- Mathematical: `PROVED ON RESTRICTED CLASS`.
- Novelty: `PLAUSIBLY DISTINCT` as constrained-design no-go packaging.

## Operator Candidate Decision

Keep:
- AGO, CIO, CCD as practical diagnostics tied to theorem package,
- CLDO as a strict constrained augmentation feasibility/impossibility certificate.

Do not promote as novel math objects yet:
- SDCO, CCD, CIO (all largely reformulations of compatibility/fiber logic).

Needs second pass:
- AGO with proof-level lower/upper bounds under fixed admissibility class.
