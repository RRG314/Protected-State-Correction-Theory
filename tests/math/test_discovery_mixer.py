from __future__ import annotations

from ocp.discovery_mixer import (
    analyze_control_custom_case,
    analyze_linear_custom_case,
    analyze_periodic_custom_case,
    analyze_random_mixer_case,
    analyze_structured_mixer_case,
    discovery_mixer_demo_reports,
)


def test_custom_linear_mixer_detects_missing_row_and_repairs_it() -> None:
    report = analyze_linear_custom_case(
        dimension=3,
        observation_text='x1\nx2 + x3',
        protected_text='x3',
        candidate_text='x2\nx3\nx1 + x2',
        delta=1.0,
    )
    assert report.validity == 'supported'
    assert report.impossible is True
    assert report.chosen_recommendation is not None
    assert report.chosen_recommendation.action_kind == 'add_measurement'
    assert report.comparison is not None
    assert report.comparison.after_regime == 'exact'
    assert report.raw_details['minimal_added_rows'] == 1


def test_custom_linear_mixer_rejects_nonlinear_expression() -> None:
    report = analyze_linear_custom_case(
        dimension=3,
        observation_text='x1\nsin(x2)',
        protected_text='x3',
        candidate_text='x2',
        delta=1.0,
    )
    assert report.unsupported is True
    assert report.diagnostics[0].code == 'unsupported-custom-linear-input'


def test_custom_periodic_mixer_detects_hidden_support_and_fix() -> None:
    report = analyze_periodic_custom_case(
        functional_text='a1 + 2*a4',
        observation='cutoff_vorticity',
        cutoff=2,
        delta=2.0,
    )
    assert report.impossible is True
    assert report.chosen_recommendation is not None
    assert report.chosen_recommendation.action_kind == 'add_mode'
    assert report.comparison is not None
    assert report.comparison.after_regime == 'exact'
    assert report.raw_details['predicted_min_cutoff'] == 4


def test_custom_control_mixer_detects_history_threshold() -> None:
    report = analyze_control_custom_case(
        sensor_profile_text='1,0.4,0.2,0',
        target_text='x3',
        horizon=2,
        delta=0.5,
    )
    assert report.validity == 'supported'
    assert report.impossible is True
    assert report.chosen_recommendation is not None
    assert report.chosen_recommendation.action_kind == 'add_history'
    assert report.comparison is not None
    assert report.comparison.after_regime == 'exact'


def test_structured_boundary_mixer_detects_architecture_swap() -> None:
    report = analyze_structured_mixer_case(
        family='boundary',
        config={'boundaryArchitecture': 'periodic_transplant', 'boundaryProtected': 'bounded_velocity_class', 'boundaryGridSize': 17, 'boundaryDelta': 0.2},
    )
    assert report.impossible is True
    assert report.chosen_recommendation is not None
    assert report.chosen_recommendation.action_kind == 'switch_architecture'
    assert report.comparison is not None
    assert report.comparison.after_regime == 'exact'


def test_random_mixer_case_is_seed_reproducible() -> None:
    config_a, report_a = analyze_random_mixer_case(family='linear', seed=37)
    config_b, report_b = analyze_random_mixer_case(family='linear', seed=37)
    assert config_a == config_b
    assert report_a.regime == report_b.regime
    assert report_a.root_cause == report_b.root_cause


def test_discovery_mixer_demo_bundle_is_complete() -> None:
    bundle = discovery_mixer_demo_reports()
    assert bundle['summary']['demo_count'] == 5
    assert set(bundle['demos']) == {
        'periodic_user_builder',
        'control_history_builder',
        'weaker_stronger_split',
        'custom_matrix_builder',
        'random_discovery_case',
    }
