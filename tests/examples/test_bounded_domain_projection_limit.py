from ocp.physics import bounded_domain_projection_counterexample


def test_periodic_projector_does_not_preserve_bounded_domain_boundary_class() -> None:
    report = bounded_domain_projection_counterexample(32)
    assert report.before_l2_divergence > 1.0
    assert report.after_periodic_projection_l2_divergence < 1e-10
    assert report.physical_boundary_normal_rms < 1e-10
    assert report.projected_boundary_normal_rms > 1e-2
