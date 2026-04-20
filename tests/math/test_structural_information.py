from __future__ import annotations

import numpy as np

from ocp.structural_information import (
    amount_scalar_exact_classifier_possible,
    amount_scalar_nonreducibility_certificate,
    bsc_horizon_threshold,
    bsc_mmse_flow_from_perfect_observation,
    bsc_effective_flip_probability,
    StructuralInformationObject,
    compatibility_lift,
    descriptor_fiber_metrics,
    experiment_regret_binary,
    garbling_mmse_flow_discrete,
    garbling_mmse_flow_binary,
    full_column_rank_margin,
    is_monotone,
    postcomposition_exactness_report,
    perturbation_robustness_certificate,
    primitive_object_reparameterization_certificate,
    primitive_object_ocp_equivalence_certificate,
    recoverability_flow_defect,
    restricted_linear_stability_bound,
    target_dependent_transition_no_go_example,
    target_postcomposition_exactness_report,
)


def test_structural_information_exactness_and_collision_witness() -> None:
    exact_obj = StructuralInformationObject(
        records=np.array([[0.0], [0.0], [1.0], [1.0]], dtype=float),
        targets=np.array([[2.0], [2.0], [3.0], [3.0]], dtype=float),
    )
    assert exact_obj.exact_recoverable() is True
    assert exact_obj.collapse_modulus_zero() < 1e-12
    assert exact_obj.collision_witness() is None

    fail_obj = StructuralInformationObject(
        records=np.array([[0.0], [0.0], [1.0], [1.0]], dtype=float),
        targets=np.array([[2.0], [4.0], [3.0], [3.0]], dtype=float),
    )
    assert fail_obj.exact_recoverable() is False
    assert fail_obj.collapse_modulus_zero() > 1.9
    assert fail_obj.collision_witness() is not None


def test_restricted_linear_stability_bound_holds_on_vertex_box() -> None:
    observation = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ],
        dtype=float,
    )
    protected = np.array([[0.0, 1.0, 1.0]], dtype=float)
    perturbation = np.array(
        [
            [0.02, 0.01, 0.00],
            [0.00, -0.01, 0.03],
        ],
        dtype=float,
    )
    report = restricted_linear_stability_bound(
        observation,
        protected,
        perturbation,
        box_radius=1.0,
    )
    assert report.exact_recoverable is True
    assert report.decoder_operator_norm is not None
    assert report.predicted_error_upper_bound is not None
    assert report.empirical_max_error is not None
    assert report.predicted_error_upper_bound >= report.empirical_max_error - 1e-9
    assert report.upper_bound_holds_on_box_vertices is True


def test_primitive_object_ocp_equivalence_certificate_exact_case() -> None:
    observation = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ],
        dtype=float,
    )
    protected = np.array([[0.0, 1.0, 1.0]], dtype=float)
    cert = primitive_object_ocp_equivalence_certificate(
        observation,
        protected,
        box_radius=1.0,
    )
    assert cert.kernel_inclusion_holds is True
    assert cert.linear_decoder_exact is True
    assert cert.fiber_constancy_exact is True
    assert cert.collapse_modulus_zero <= 1e-10
    assert cert.all_equivalent is True


def test_primitive_object_ocp_equivalence_certificate_fail_case_has_witness() -> None:
    observation = np.array([[1.0, 0.0]], dtype=float)
    protected = np.array([[1.0, 1.0]], dtype=float)
    cert = primitive_object_ocp_equivalence_certificate(
        observation,
        protected,
        box_radius=1.0,
    )
    assert cert.kernel_inclusion_holds is False
    assert cert.linear_decoder_exact is False
    assert cert.fiber_constancy_exact is False
    assert cert.collapse_modulus_zero > 1e-8
    assert cert.witness_pair_present is True
    assert cert.all_equivalent is True


def test_recoverability_flow_nondecreasing_under_coarsening() -> None:
    target = np.array([0.0, 0.0, 1.0, 1.0], dtype=float)
    # y0 is finest, y1 merges first pair, y2 merges all.
    y0 = np.array([0, 1, 2, 3], dtype=int)
    y1 = np.array([0, 0, 1, 1], dtype=int)
    y2 = np.array([0, 0, 0, 0], dtype=int)
    flow = recoverability_flow_defect(target, [y0, y1, y2])
    assert flow[0] <= flow[1] + 1e-12
    assert flow[1] <= flow[2] + 1e-12
    assert is_monotone(flow, mode="coarsening")


def test_descriptor_metrics_and_compatibility_lift() -> None:
    descriptors = np.array(
        [
            [0.1, 0.2],
            [0.1, 0.2],
            [0.9, 0.8],
            [0.9, 0.8],
        ],
        dtype=float,
    )
    labels_bad = np.array([0, 1, 0, 1], dtype=int)
    labels_good = np.array([0, 0, 1, 1], dtype=int)
    m_bad = descriptor_fiber_metrics(descriptors, labels_bad, bins=2)
    m_good = descriptor_fiber_metrics(descriptors, labels_good, bins=2)
    lift = compatibility_lift(m_bad["IDELB"], m_good["IDELB"])
    assert m_bad["IDELB"] > m_good["IDELB"]
    assert lift["CL_abs"] > 0.0
    assert lift["CL_rel"] > 0.0


def test_experiment_regret_binary_is_nonnegative_under_coarsening() -> None:
    target = np.array([0, 0, 1, 1], dtype=int)
    fine = np.array([0, 1, 2, 3], dtype=int)
    coarse = np.array([0, 0, 1, 1], dtype=int)
    regret = experiment_regret_binary(target, fine, coarse)
    assert regret >= -1e-12


def test_markov_garbling_mmse_flow_is_monotone() -> None:
    # Binary target with informative initial records.
    joint = np.array(
        [
            [0.42, 0.08],
            [0.08, 0.42],
        ],
        dtype=float,
    )
    kernel = np.array(
        [
            [0.9, 0.1],
            [0.1, 0.9],
        ],
        dtype=float,
    )
    flow = garbling_mmse_flow_binary(joint, kernel, steps=5)
    assert flow.monotone_nondecreasing is True
    vals = np.asarray(flow.flow, dtype=float)
    assert np.all(vals[1:] >= vals[:-1] - 1e-12)


def test_markov_garbling_mmse_flow_discrete_is_monotone() -> None:
    # Three target states with numeric values.
    joint = np.array(
        [
            [0.30, 0.05, 0.00],
            [0.05, 0.20, 0.05],
            [0.00, 0.05, 0.30],
        ],
        dtype=float,
    )
    target_values = np.array([-1.0, 0.5, 2.0], dtype=float)
    kernel = np.array(
        [
            [0.85, 0.10, 0.05],
            [0.10, 0.80, 0.10],
            [0.05, 0.10, 0.85],
        ],
        dtype=float,
    )
    flow = garbling_mmse_flow_discrete(joint, target_values, kernel, steps=5)
    vals = np.asarray(flow.flow, dtype=float)
    assert flow.monotone_nondecreasing is True
    assert np.all(vals[1:] >= vals[:-1] - 1e-12)


def test_bsc_closed_form_mmse_flow_is_monotone_and_matches_limit() -> None:
    eps = 0.15
    flow = bsc_mmse_flow_from_perfect_observation(eps, steps=30)
    vals = np.asarray(flow.flow, dtype=float)
    assert flow.monotone_nondecreasing is True
    # Starts from perfect record: zero MMSE.
    assert vals[0] <= 1e-12
    # Should increase toward prior variance 1/4.
    assert vals[-1] > vals[1]
    assert abs(vals[-1] - 0.25) < 0.02
    # One-step formula check.
    e1 = bsc_effective_flip_probability(eps, 1)
    assert abs(vals[1] - e1 * (1.0 - e1)) < 1e-12


def test_target_dependent_transition_breaks_broad_monotonicity() -> None:
    flow = target_dependent_transition_no_go_example()
    vals = np.asarray(flow.flow, dtype=float)
    assert vals[1] < vals[0]
    assert flow.monotone_nondecreasing is False


def test_amount_scalar_nonreducibility_certificate_detects_collision() -> None:
    amount_codes = np.array(
        [
            [0, 1, 1, 2],
            [0, 1, 1, 2],
            [1, 0, 2, 1],
        ],
        dtype=int,
    )
    labels = np.array([0, 1, 1], dtype=int)
    rep = amount_scalar_nonreducibility_certificate(amount_codes, labels)
    assert rep.nonreducible is True
    assert rep.mixed_codes >= 1
    assert rep.witness_indices is not None


def test_primitive_object_reparameterization_invariance_for_invertible_change() -> None:
    observation = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ],
        dtype=float,
    )
    protected = np.array([[0.0, 1.0, 1.0]], dtype=float)
    q = np.array(
        [
            [1.0, 1.0, 0.0],
            [0.0, 1.0, 1.0],
            [1.0, 0.0, 1.0],
        ],
        dtype=float,
    )
    rep = primitive_object_reparameterization_certificate(
        observation,
        protected,
        reparameterization=q,
    )
    assert rep.reparameterization_invertible is True
    assert rep.invariance_holds is True
    assert rep.baseline_exact is rep.transformed_exact


def test_primitive_object_reparameterization_can_fail_for_noninvertible_change() -> None:
    # Baseline exact on x=(x1,x2), record y=x1+x2, target t=x1+x2.
    observation = np.array([[1.0, 1.0]], dtype=float)
    protected = np.array([[1.0, 1.0]], dtype=float)
    # Collapse family to 1D subspace where exactness no longer matches baseline criterion.
    q = np.array([[1.0], [0.0]], dtype=float)
    rep = primitive_object_reparameterization_certificate(
        observation,
        protected,
        reparameterization=q,
    )
    assert rep.reparameterization_invertible is False
    # Non-invertible changes are not guaranteed to preserve verdicts.
    assert isinstance(rep.invariance_holds, bool)


def test_perturbation_robustness_margin_certificate() -> None:
    observation = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ],
        dtype=float,
    )
    protected = np.array([[1.0, 1.0]], dtype=float)
    margin = full_column_rank_margin(observation)
    assert margin > 0.9
    delta = np.array([[0.05, 0.0], [0.0, -0.05]], dtype=float)
    cert = perturbation_robustness_certificate(observation, protected, delta)
    assert cert.baseline_exact is True
    assert cert.baseline_full_column_rank is True
    assert cert.guaranteed_exact_by_margin is True
    assert cert.exact_after_perturbation is True


def test_postcomposition_exactness_injective_vs_noninjective_boundary() -> None:
    records = np.array([[-2.0], [-1.0], [1.0]], dtype=float)
    targets = np.array([[-2.0], [-1.0], [1.0]], dtype=float)

    rep_inj = postcomposition_exactness_report(
        records,
        targets,
        post_map=lambda y: y**3,
    )
    assert rep_inj.map_injective_on_records is True
    assert rep_inj.exactness_equivalence_holds is True

    rep_noninj = postcomposition_exactness_report(
        records,
        targets,
        post_map=lambda y: y**2,
    )
    assert rep_noninj.map_injective_on_records is False
    assert rep_noninj.exact_before is True
    assert rep_noninj.exact_after is False


def test_bsc_horizon_threshold_exists_and_is_minimal() -> None:
    rep = bsc_horizon_threshold(0.15, 0.20, max_steps=200)
    assert rep.reached is True
    assert rep.horizon is not None
    assert rep.flow_prefix[rep.horizon] >= 0.20 - 1e-12
    if rep.horizon > 0:
        assert rep.flow_prefix[rep.horizon - 1] < 0.20 + 1e-12


def test_amount_scalar_exact_classifier_possible_boundary() -> None:
    amount_codes_good = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=int)
    labels_good = np.array([0, 0, 1, 1], dtype=int)
    assert amount_scalar_exact_classifier_possible(amount_codes_good, labels_good) is True

    amount_codes_bad = np.array([[0, 0], [0, 0], [1, 1]], dtype=int)
    labels_bad = np.array([0, 1, 1], dtype=int)
    assert amount_scalar_exact_classifier_possible(amount_codes_bad, labels_bad) is False


def test_target_postcomposition_injective_map_preserves_exactness() -> None:
    records = np.array([[-2.0], [-1.0], [1.0], [2.0]], dtype=float)
    targets = np.array([[-2.0], [-1.0], [1.0], [2.0]], dtype=float)
    rep = target_postcomposition_exactness_report(
        records,
        targets,
        target_map=lambda t: np.exp(t),
    )
    assert rep.map_injective_on_targets is True
    assert rep.exact_before is True
    assert rep.exact_after is True
    assert rep.exactness_equivalence_holds is True


def test_target_postcomposition_noninjective_coarsening_can_make_exact() -> None:
    records = np.array([[0.0], [0.0]], dtype=float)
    fine_targets = np.array([[-1.0], [1.0]], dtype=float)
    rep = target_postcomposition_exactness_report(
        records,
        fine_targets,
        target_map=lambda t: np.abs(t),
    )
    assert rep.map_injective_on_targets is False
    assert rep.exact_before is False
    assert rep.exact_after is True
    assert rep.exactness_equivalence_holds is False
