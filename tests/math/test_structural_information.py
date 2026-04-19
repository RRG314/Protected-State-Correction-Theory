from __future__ import annotations

import numpy as np

from ocp.structural_information import (
    StructuralInformationObject,
    compatibility_lift,
    descriptor_fiber_metrics,
    experiment_regret_binary,
    is_monotone,
    recoverability_flow_defect,
    restricted_linear_stability_bound,
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
