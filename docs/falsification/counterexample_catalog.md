# Counterexample Catalog

Date: 2026-04-17

| Witness ID | Branch | Claim Attacked | Type | Descriptor | Evidence | Status | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CX-RANK-001 | G/H | OCP-047/OCP-049 | same-rank opposite-verdict | (n,r,k)=(3,1,1) | rowspace_residual exact=0.0 fail=1.0; collision_gap exact=0.0 fail=2.0 | VALIDATED | `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv` |
| CX-RANK-002 | G/H | OCP-047/OCP-049 | same-rank opposite-verdict | (n,r,k)=(3,1,2) | rowspace_residual exact=0.0 fail=1.0; collision_gap exact=0.0 fail=2.0 | VALIDATED | `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv` |
| CX-RANK-003 | G/H | OCP-047/OCP-049 | same-rank opposite-verdict | (n,r,k)=(3,2,2) | rowspace_residual exact=0.0 fail=1.0; collision_gap exact=0.0 fail=2.0 | VALIDATED | `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv` |
| CX-RANK-004 | G/H | OCP-047/OCP-049 | same-rank opposite-verdict | (n,r,k)=(4,1,1) | rowspace_residual exact=0.0 fail=1.0; collision_gap exact=0.0 fail=2.0 | VALIDATED | `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv` |
| CX-RANK-005 | G/H | OCP-047/OCP-049 | same-rank opposite-verdict | (n,r,k)=(4,1,2) | rowspace_residual exact=0.0 fail=1.0; collision_gap exact=0.0 fail=2.0 | VALIDATED | `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv` |
| CX-RANK-006 | G/H | OCP-047/OCP-049 | same-rank opposite-verdict | (n,r,k)=(4,1,3) | rowspace_residual exact=0.0 fail=1.0; collision_gap exact=0.0 fail=2.0 | VALIDATED | `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv` |
| CX-RANK-007 | G/H | OCP-047/OCP-049 | same-rank opposite-verdict | (n,r,k)=(4,2,2) | rowspace_residual exact=0.0 fail=1.0; collision_gap exact=0.0 fail=2.0 | VALIDATED | `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv` |
| CX-RANK-008 | G/H | OCP-047/OCP-049 | same-rank opposite-verdict | (n,r,k)=(4,2,3) | rowspace_residual exact=0.0 fail=1.0; collision_gap exact=0.0 fail=2.0 | VALIDATED | `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv` |
| CX-BUDGET-001 | G/H | OCP-050 | same-budget opposite-verdict | (n,r,k,c)=(3,1,1,1.0) | exact_count=1 fail_count=2 | VALIDATED | `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv` |
| CX-BUDGET-002 | G/H | OCP-050 | same-budget opposite-verdict | (n,r,k,c)=(3,1,2,2.0) | exact_count=2 fail_count=1 | VALIDATED | `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv` |
| CX-BUDGET-003 | G/H | OCP-050 | same-budget opposite-verdict | (n,r,k,c)=(3,2,2,2.0) | exact_count=1 fail_count=2 | VALIDATED | `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv` |
| CX-BUDGET-004 | G/H | OCP-050 | same-budget opposite-verdict | (n,r,k,c)=(4,1,1,1.0) | exact_count=1 fail_count=3 | VALIDATED | `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv` |
| CX-BUDGET-005 | G/H | OCP-050 | same-budget opposite-verdict | (n,r,k,c)=(4,1,2,2.0) | exact_count=3 fail_count=3 | VALIDATED | `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv` |
| CX-BUDGET-006 | G/H | OCP-050 | same-budget opposite-verdict | (n,r,k,c)=(4,1,3,3.0) | exact_count=3 fail_count=1 | VALIDATED | `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv` |
| CX-BUDGET-007 | G/H | OCP-050 | same-budget opposite-verdict | (n,r,k,c)=(4,2,2,2.0) | exact_count=1 fail_count=5 | VALIDATED | `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv` |
| CX-BUDGET-008 | G/H | OCP-050 | same-budget opposite-verdict | (n,r,k,c)=(4,2,3,3.0) | exact_count=2 fail_count=2 | VALIDATED | `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv` |
| CX-FAMILY-001 | G/H | OCP-052 | exact-on-small fail-on-large | small_dim=2 large_dim=3 | small_exact=True large_exact=False lower_bound=1.0 | VALIDATED | `data/generated/unified-recoverability/family_enlargement_false_positive.csv` |
| CX-MISMATCH-001 | G/H | OCP-053 | mismatched-decoder instability | beta_true=0.5 beta_ref=1.0 | distance=0.316227766016838 formula=0.4472135954999579 brute=0.44721359549995804 | VALIDATED | `data/generated/unified-recoverability/canonical_model_mismatch.csv` |
| CX-MISMATCH-002 | G/H | OCP-053 | mismatched-decoder instability | beta_true=2.0 beta_ref=1.0 | distance=0.31622776601683783 formula=0.4472135954999579 brute=0.44721359549995776 | VALIDATED | `data/generated/unified-recoverability/canonical_model_mismatch.csv` |
| CX-PERIODIC-001 | F/H | family-blind exactness overclaim | coarse exact but refined fail | cutoff=2 | coarse_exact=True refined_exact=False refined_lb=0.9999999999999999 | VALIDATED | `data/generated/unified-recoverability/periodic_refinement_false_positive.csv` |
| CX-META-rank_tuple_(n,r,k) | K | amount-only descriptor sufficiency | descriptor-fiber mixedness | rank_tuple_(n,r,k) | mixed=34/34 IDELB=0.5 | VALIDATED | `data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.json` |
| CX-META-rank_tuple_plus_rowspace_proxy | K | amount-only descriptor sufficiency | descriptor-fiber mixedness | rank_tuple_plus_rowspace_proxy | mixed=0/68 IDELB=0.0 | VALIDATED | `data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.json` |
| CX-META-budget_tuple_(n,r,selection,cost) | K | amount-only descriptor sufficiency | descriptor-fiber mixedness | budget_tuple_(n,r,selection,cost) | mixed=19/19 IDELB=0.2857142857142857 | VALIDATED | `data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.json` |
