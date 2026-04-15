import pytest

from ocp.cfd import (
    bounded_hodge_projection_report,
    divergence_only_bounded_no_go_witness,
    periodic_incompressible_projection_report,
)


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


def test_bounded_hodge_projection_is_exact_on_the_boundary_compatible_family() -> None:
    report = bounded_hodge_projection_report(n=41)
    assert report.protected_divergence_rms < 1e-8
    assert report.recovered_divergence_rms < 1e-8
    assert report.protected_boundary_normal_rms < 1e-8
    assert report.recovered_boundary_normal_rms < 1e-8
    assert report.orthogonality_residual < 1e-10
    assert report.recovery_l2_error < 1e-10
    assert report.idempotence_l2_error < 1e-10
    assert report.projector_construction_agreement < 1e-8


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


@pytest.mark.parametrize(
    ('n', 'protected_modes', 'disturbance_modes'),
    (
        (33, ((1, 1), (1, 2)), ((1, 1), (2, 1))),
        (41, ((1, 1), (2, 1), (2, 2)), ((1, 1), (1, 2), (2, 1))),
        (49, ((1, 1), (1, 3), (2, 2)), ((1, 1), (2, 1), (2, 2))),
    ),
)
def test_bounded_hodge_projection_persists_across_grids_and_mode_families(
    n: int,
    protected_modes: tuple[tuple[int, int], ...],
    disturbance_modes: tuple[tuple[int, int], ...],
) -> None:
    report = bounded_hodge_projection_report(
        n=n,
        protected_modes=protected_modes,
        disturbance_modes=disturbance_modes,
    )
    assert report.protected_divergence_rms < 1e-7
    assert report.recovered_divergence_rms < 1e-7
    assert report.protected_boundary_normal_rms < 1e-7
    assert report.recovered_boundary_normal_rms < 1e-7
    assert report.orthogonality_residual < 1e-9
    assert report.recovery_l2_error < 1e-9
    assert report.idempotence_l2_error < 1e-9
