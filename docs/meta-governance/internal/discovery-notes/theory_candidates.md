# Theory Candidates (Discovery Sandbox)

Status: exploration-only, non-integrated.

## Top candidate structures

### Context-Invariance Defect (CID)

Definition: CID = inf_D max_c ||D O_c - L||_F over shared decoder D.

Novelty test: Descriptor-matched opposite verdict contexts and CID separation check.

Filter result: **KEPT**

Reason: CID separates invariant exact vs fail on descriptor-matched context families; captures architecture constraint absent from amount-only descriptors.

### Partition Synergy Index (PSI)

Definition: PSI = min_i DLS(single terminal i) - DLS(joint terminals).

Novelty test: Same total rank/count partition families with opposite exactness.

Filter result: **KEPT**

Reason: Distributed partition anomalies detected; positive-PSI exactness rate=0.300.

### Intervention Lift (IL)

Definition: IL = residual(observational) - residual(interventional) at matched measurement count.

Novelty test: Matched-count observational-vs-interventional opposite verdict frequency.

Filter result: **KEPT**

Reason: Intervention lifted recoverability in 18 matched-count families.

### Target Sensitivity Floor (TSF)

Definition: TSF = min_theta I_F(theta) for target parameter under fixed measurement family.

Novelty test: Same-count sensitivity families with opposite recoverability labels.

Filter result: **KEPT**

Reason: TSF cleanly separates sensitivity-blind vs sensitivity-resolving families at fixed count.

### Recovery Frontier Size (RFS)

Definition: RFS(O) = number of weak targets recoverable under O before strong-target failure.

Novelty test: Weak-vs-strong target split under fixed observation map.

Filter result: **KEPT**

Reason: Reveals partial-recovery lattice structure (weak recoverable, strong impossible).

## Strongest theorem / no-go candidates

### Context-architecture incompatibility theorem (supported family)

Statement: There exist context families with identical rank/count descriptors where every context is exactly recoverable, yet no single decoder is exact across contexts.

Status: `PROVED`

Evidence: found 11 fail and 11 exact descriptor-matched context witnesses

Failure mode / limit: fails only if architecture constraint (shared decoder) is removed

### Distributed arrangement anti-classifier theorem (supported family)

Statement: In two-terminal linear partition families, total measurement count and joint rank do not determine exact recoverability; terminal arrangement can flip the verdict.

Status: `PROVED`

Evidence: descriptor groups with opposite verdicts: 1

Failure mode / limit: disproves amount-only distributed classification

### CID separation conjecture

Statement: Context-Invariance Defect threshold separates invariant exact/fail classes in generated multi-context families.

Status: `CONDITIONAL`

Evidence: CID threshold accuracy=22/22

Failure mode / limit: may collapse under broader nonlinear/contextual families

### Sensitivity-floor no-go

Statement: At fixed measurement count, zero Fisher sensitivity floor implies no finite-variance unbiased local estimator for the target parameter (Cramér-Rao no-go).

Status: `PROVED`

Evidence: zero-floor models=1, nonzero-floor models=4

Failure mode / limit: applies to local unbiased estimation regime

### Naive amount-only claim

Statement: Same rank and same count imply same exact-recovery verdict.

Status: `DISPROVED`

Evidence: counterexamples found in causal, multi-terminal, and Willems lanes

Failure mode / limit: same-descriptor opposite-verdict anomalies

