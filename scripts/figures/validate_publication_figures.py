#!/usr/bin/env python3
"""Lightweight validation checks for publication figure generation."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIG_ROOT = ROOT / "figures"
METRICS = ROOT / "data/generated/figures/publication_figure_metrics.json"
REPORT = ROOT / "data/generated/figures/publication_figure_validation.json"

EXPECTED = [
    "recoverability/recoverability_rowspace_inclusion",
    "recoverability/recoverability_same_rank_insufficiency",
    "recoverability/recoverability_collision_gap_threshold",
    "recoverability/recoverability_regime_transition",
    "mhd/mhd_remainder_constant_vs_variable_eta",
    "mhd/mhd_singularity_near_axis",
    "mhd/mhd_sheet_thinning_scaling",
    "mhd/mhd_axis_vs_annular_behavior",
    "bridge/bridge_divergence_vs_recovery",
    "bridge/bridge_projection_success_vs_failure",
    "bridge/bridge_operator_component_diagram",
]


def main() -> None:
    missing = []
    for stem in EXPECTED:
        for ext in (".png", ".pdf"):
            p = FIG_ROOT / f"{stem}{ext}"
            if not p.exists():
                missing.append(str(p))

    with METRICS.open("r", encoding="utf-8") as f:
        m = json.load(f)

    checks = {
        "rowspace_exact_zero": abs(m["recoverability_residuals"]["exact"]) < 1e-10,
        "rowspace_fail_positive": m["recoverability_residuals"]["fail"] > 0.5,
        "gamma_monotone": all(
            m["recoverability_gamma"]["values"][i] >= m["recoverability_gamma"]["values"][i + 1] - 1e-9
            for i in range(len(m["recoverability_gamma"]["values"]) - 1)
        ),
        "gamma_hits_zero": m["recoverability_gamma"]["values"][-1] < 1e-9,
        "sheet_scaling_slope_positive": m["mhd_sheet_scaling"]["fit_slope"] > 0,
        "bridge_periodic_beats_bounded_error": m["bridge_errors"]["mean_error_periodic"] < m["bridge_errors"]["mean_error_bounded"],
        "bridge_divergence_reduced_both": m["bridge_errors"]["mean_div_after_periodic"] < 1e-10 and m["bridge_errors"]["mean_div_after_bounded"] < 1e-10,
    }

    report = {
        "missing_assets": missing,
        "checks": checks,
        "all_passed": (len(missing) == 0) and all(checks.values()),
    }

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
