from ocp.cfd import divergence_only_bounded_no_go_witness, periodic_incompressible_projection_report


def test_periodic_incompressible_projection_is_exact_on_the_periodic_branch() -> None:
    report = periodic_incompressible_projection_report(n=48, contamination=0.2)
    assert report.after_projection_l2_divergence < report.before_l2_divergence * 1e-10
    assert report.recovery_l2_error < 1e-10
    assert report.idempotence_l2_error < 1e-10
    assert report.orthogonality_residual < 1e-10


def test_divergence_only_bounded_no_go_witness_has_same_constraint_and_distinct_states() -> None:
    witness = divergence_only_bounded_no_go_witness(n=32)
    assert witness.first_state_divergence_rms < 1e-10
    assert witness.second_state_divergence_rms < 1e-10
    assert witness.state_separation_rms > 0.1
