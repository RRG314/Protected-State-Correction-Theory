import pytest

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


@pytest.mark.parametrize(
    ('n', 'contamination'),
    (
        (24, 0.05),
        (32, 0.2),
        (48, 0.35),
    ),
)
def test_periodic_incompressible_projection_is_stable_across_grid_and_contamination(
    n: int, contamination: float
) -> None:
    report = periodic_incompressible_projection_report(n=n, contamination=contamination)
    assert report.after_projection_l2_divergence < report.before_l2_divergence * 1e-10
    assert report.recovery_l2_error < 1e-10
    assert report.idempotence_l2_error < 1e-10
    assert report.orthogonality_residual < 1e-10


@pytest.mark.parametrize('n', (16, 24, 32, 48))
def test_divergence_only_bounded_no_go_witness_persists_across_grid_sizes(n: int) -> None:
    witness = divergence_only_bounded_no_go_witness(n=n)
    assert witness.first_state_divergence_rms < 1e-8
    assert witness.second_state_divergence_rms < 1e-8
    assert witness.state_separation_rms > 0.05
