#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ocp.structural_information import (
    compatibility_lift,
    descriptor_fiber_metrics,
    experiment_regret_binary,
    recoverability_flow_defect,
    restricted_linear_stability_bound,
)

OUT = ROOT / "data" / "generated" / "structural-information-theory"

IMPORTED = ROOT / "data" / "imported" / "structural-information-theory"
OCP_UNIFIED = ROOT / "data" / "generated" / "unified-recoverability"


@dataclass(frozen=True)
class Row:
    dataset: str
    lane: str
    context_id: str
    target: str
    standard_entropy: float
    standard_mi_state: float
    standard_fisher_trace: float
    standard_rank: float
    compatibility_defect: float
    tfcd: float
    ambiguity_index: float
    recoverability_defect: float
    verdict_good: int


def _to_float(v: str | float | int | None) -> float:
    if v is None:
        return float("nan")
    if isinstance(v, (float, int)):
        return float(v)
    s = str(v).strip()
    if not s:
        return float("nan")
    try:
        return float(s)
    except ValueError:
        return float("nan")


def _safe_fill(values: np.ndarray) -> np.ndarray:
    vals = np.asarray(values, dtype=float)
    finite = vals[np.isfinite(vals)]
    fill = float(np.median(finite)) if finite.size else 0.0
    out = vals.copy()
    out[~np.isfinite(out)] = fill
    return out


def _rows_to_matrix(rows: list[Row], cols: list[str]) -> np.ndarray:
    mat = []
    for row in rows:
        r = []
        for c in cols:
            r.append(float(getattr(row, c)))
        mat.append(r)
    return np.asarray(mat, dtype=float)


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _load_ocp_rank_witness_rows() -> list[Row]:
    src = OCP_UNIFIED / "rank_only_classifier_witnesses.csv"
    out: list[Row] = []
    for idx, r in enumerate(_read_csv_rows(src)):
        n = _to_float(r.get("ambient_dimension"))
        pr = _to_float(r.get("protected_rank"))
        ork = _to_float(r.get("observation_rank"))
        # exact witness
        out.append(
            Row(
                dataset="ocp_rank_witness",
                lane="ocp_restricted_linear",
                context_id=f"rank_witness_{idx}_exact",
                target="exactness",
                standard_entropy=float(np.log2(max(1.0, ork + 1.0))),
                standard_mi_state=float(ork / max(n, 1.0)),
                standard_fisher_trace=float(ork),
                standard_rank=float(ork),
                compatibility_defect=0.0,
                tfcd=0.0,
                ambiguity_index=0.0,
                recoverability_defect=0.0,
                verdict_good=1,
            )
        )
        # fail witness, same amount-level descriptors
        out.append(
            Row(
                dataset="ocp_rank_witness",
                lane="ocp_restricted_linear",
                context_id=f"rank_witness_{idx}_fail",
                target="exactness",
                standard_entropy=float(np.log2(max(1.0, ork + 1.0))),
                standard_mi_state=float(ork / max(n, 1.0)),
                standard_fisher_trace=float(ork),
                standard_rank=float(ork),
                compatibility_defect=1.0,
                tfcd=1.0,
                ambiguity_index=float(_to_float(r.get("fail_collision_gap"))),
                recoverability_defect=float(_to_float(r.get("fail_collision_gap")) / 2.0),
                verdict_good=0,
            )
        )
    return out


def _load_information_real_rows() -> list[Row]:
    src = IMPORTED / "real_system_metrics.csv"
    out: list[Row] = []
    for r in _read_csv_rows(src):
        out.append(
            Row(
                dataset="information_real_system",
                lane=str(r.get("battlefield", "unknown")),
                context_id=str(r.get("context_id", "")),
                target=str(r.get("subdomain", "unknown")),
                standard_entropy=_to_float(r.get("standard_entropy")),
                standard_mi_state=_to_float(r.get("standard_mi_state")),
                standard_fisher_trace=_to_float(r.get("standard_fisher_trace")),
                standard_rank=_to_float(r.get("standard_rank")),
                compatibility_defect=_to_float(r.get("compatibility_defect")),
                tfcd=_to_float(r.get("tfcd")),
                ambiguity_index=_to_float(r.get("ambiguity_index")),
                recoverability_defect=_to_float(r.get("recoverability_defect")),
                verdict_good=int(_to_float(r.get("verdict_good"))),
            )
        )
    return out


def _load_gravity_rows() -> list[Row]:
    src = IMPORTED / "gravity_recoverability_metrics.csv"
    out: list[Row] = []
    for r in _read_csv_rows(src):
        out.append(
            Row(
                dataset="gravity_recoverability",
                lane=str(r.get("lane", "unknown")),
                context_id=str(r.get("context_id", "")),
                target=str(r.get("target", "unknown")),
                standard_entropy=_to_float(r.get("standard_entropy")),
                standard_mi_state=_to_float(r.get("standard_mi_state")),
                standard_fisher_trace=_to_float(r.get("standard_fisher_trace")),
                standard_rank=_to_float(r.get("standard_rank")),
                compatibility_defect=_to_float(r.get("compatibility_defect")),
                tfcd=_to_float(r.get("tfcd")),
                ambiguity_index=_to_float(r.get("ambiguity_index")),
                recoverability_defect=_to_float(r.get("recoverability_defect")),
                verdict_good=int(_to_float(r.get("verdict_good"))),
            )
        )
    return out


def _metrics_for_rows(rows: list[Row]) -> dict[str, float]:
    base_cols = ["standard_entropy", "standard_mi_state", "standard_fisher_trace", "standard_rank"]
    aug_cols = base_cols + ["compatibility_defect", "tfcd", "ambiguity_index"]
    y = np.asarray([r.verdict_good for r in rows], dtype=int)

    base = _safe_fill(_rows_to_matrix(rows, base_cols))
    aug = _safe_fill(_rows_to_matrix(rows, aug_cols))

    m_base = descriptor_fiber_metrics(base, y, bins=4 if len(rows) >= 40 else 3)
    m_aug = descriptor_fiber_metrics(aug, y, bins=4 if len(rows) >= 40 else 3)
    lift = compatibility_lift(m_base["IDELB"], m_aug["IDELB"])
    return {
        "n_samples": float(len(rows)),
        "baseline_DFMI": m_base["DFMI"],
        "baseline_IDELB": m_base["IDELB"],
        "augmented_DFMI": m_aug["DFMI"],
        "augmented_IDELB": m_aug["IDELB"],
        "CL_abs": lift["CL_abs"],
        "CL_rel": lift["CL_rel"],
    }


def _decision_regret_for_rows(rows: list[Row]) -> float:
    # Use full context label as the finer experiment and amount-only descriptor fibers
    # as compressed experiment; report binary target regret.
    y = np.asarray([r.verdict_good for r in rows], dtype=int)
    contexts = np.asarray([idx for idx, _ in enumerate(rows)], dtype=int)
    amount = _safe_fill(
        _rows_to_matrix(
            rows,
            ["standard_entropy", "standard_mi_state", "standard_fisher_trace", "standard_rank"],
        )
    )
    amount_bins = []
    for col in range(amount.shape[1]):
        col_vals = amount[:, col]
        q = np.quantile(col_vals, [0.0, 0.33, 0.66, 1.0])
        q = np.unique(q)
        if len(q) <= 2:
            amount_bins.append(np.zeros_like(col_vals, dtype=int))
        else:
            amount_bins.append(np.digitize(col_vals, q[1:-1]).astype(int))
    tuple_labels = [tuple(v) for v in zip(*amount_bins, strict=False)]
    label_to_id: dict[tuple[int, ...], int] = {}
    amount_ids: list[int] = []
    for key in tuple_labels:
        if key not in label_to_id:
            label_to_id[key] = len(label_to_id)
        amount_ids.append(label_to_id[key])
    amount_labels = np.asarray(amount_ids, dtype=int)
    return float(experiment_regret_binary(y, contexts, amount_labels))


def _noise_from_context_id(context_id: str) -> float | None:
    m = re.search(r"noise([0-9]+(?:\.[0-9]+)?)", context_id)
    if not m:
        return None
    return float(m.group(1))


def _build_monotonicity_rows(gravity_rows: list[Row]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    # Synthetic theorem sanity chain.
    target = np.asarray([0.0, 0.0, 1.0, 1.0], dtype=float)
    labels = [
        np.asarray([0, 1, 2, 3], dtype=int),
        np.asarray([0, 0, 1, 1], dtype=int),
        np.asarray([0, 0, 0, 0], dtype=int),
    ]
    syn_flow = recoverability_flow_defect(target, labels)
    out.append(
        {
            "lane": "synthetic_flow",
            "target": "binary",
            "flow_values": json.dumps([float(v) for v in syn_flow]),
            "monotone_nondecreasing": int(all(syn_flow[i + 1] >= syn_flow[i] - 1e-10 for i in range(len(syn_flow) - 1))),
            "status": "PROVED_SANITY",
        }
    )

    # Real/surrogate monotonic trend check by noise bins in gravity Hawking lane.
    grouped: dict[tuple[str, str], list[Row]] = {}
    for row in gravity_rows:
        if row.lane != "blackhole_hawking_surrogate":
            continue
        grouped.setdefault((row.lane, row.target), []).append(row)

    for key, rows in grouped.items():
        by_noise: dict[float, list[float]] = {}
        for row in rows:
            noise = _noise_from_context_id(row.context_id)
            if noise is None:
                continue
            by_noise.setdefault(noise, []).append(float(row.recoverability_defect))
        if len(by_noise) < 2:
            continue
        noise_levels = sorted(by_noise)
        mean_defects = [float(np.mean(by_noise[n])) for n in noise_levels]
        monotone = all(mean_defects[i + 1] >= mean_defects[i] - 1e-10 for i in range(len(mean_defects) - 1))
        out.append(
            {
                "lane": key[0],
                "target": key[1],
                "flow_values": json.dumps(
                    [{"noise": noise_levels[i], "mean_defect": mean_defects[i]} for i in range(len(noise_levels))]
                ),
                "monotone_nondecreasing": int(monotone),
                "status": "VALIDATED_SURROGATE" if monotone else "FAILED_SURROGATE",
            }
        )
    return out


def _build_stability_rows() -> list[dict[str, object]]:
    cases = [
        (
            "case_exact_weak_target",
            np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 1.0]], dtype=float),
            np.array([[0.0, 1.0, 1.0]], dtype=float),
        ),
        (
            "case_exact_alt_target",
            np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=float),
            np.array([[1.0, 0.0, 0.0]], dtype=float),
        ),
    ]
    perturb_scales = [0.01, 0.05, 0.1]
    out: list[dict[str, object]] = []
    for name, obs, prot in cases:
        for scale in perturb_scales:
            delta = np.array(
                [
                    [scale, 0.5 * scale, 0.0],
                    [0.0, -0.5 * scale, scale],
                ],
                dtype=float,
            )
            rep = restricted_linear_stability_bound(obs, prot, delta, box_radius=1.0)
            out.append(
                {
                    "case_id": name,
                    "perturbation_scale": float(scale),
                    "exact_recoverable": int(rep.exact_recoverable),
                    "decoder_operator_norm": float(rep.decoder_operator_norm or np.nan),
                    "perturbation_operator_norm": float(rep.perturbation_operator_norm),
                    "predicted_error_upper_bound": float(rep.predicted_error_upper_bound or np.nan),
                    "empirical_max_error": float(rep.empirical_max_error or np.nan),
                    "upper_bound_holds_on_box_vertices": int(bool(rep.upper_bound_holds_on_box_vertices)),
                }
            )
    return out


def _write_csv(path: Path, rows: Iterable[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    ocp_rows = _load_ocp_rank_witness_rows()
    info_rows = _load_information_real_rows()
    grav_rows = _load_gravity_rows()

    datasets = {
        "ocp_rank_witness": ocp_rows,
        "information_real_system": info_rows,
        "gravity_recoverability": grav_rows,
        "gravity_hidden_mass_only": [r for r in grav_rows if r.lane == "hidden_mass_inference"],
        "gravity_blackhole_only": [r for r in grav_rows if r.lane == "blackhole_hawking_surrogate"],
    }

    reduction_rows: list[dict[str, object]] = []
    anti_rows: list[dict[str, object]] = []
    regret_rows: list[dict[str, object]] = []
    for name, rows in datasets.items():
        if len(rows) < 2:
            continue
        m = _metrics_for_rows(rows)
        reduction_rows.append({"dataset": name, **m})
        anti_rows.append(
            {
                "dataset": name,
                "n_samples": int(m["n_samples"]),
                "baseline_IDELB": float(m["baseline_IDELB"]),
                "augmented_IDELB": float(m["augmented_IDELB"]),
                "CL_rel": float(m["CL_rel"]),
                "status": "SURVIVES" if m["baseline_IDELB"] > 0 else "COLLAPSES",
                "independent_out_of_family": int(name in {"information_real_system", "gravity_hidden_mass_only"}),
            }
        )
        regret_rows.append(
            {
                "dataset": name,
                "decision_regret_amount_vs_context": float(_decision_regret_for_rows(rows)),
            }
        )

    monotonicity_rows = _build_monotonicity_rows(grav_rows)
    stability_rows = _build_stability_rows()

    _write_csv(
        OUT / "unified_cross_domain_reduction_metrics.csv",
        reduction_rows,
        [
            "dataset",
            "n_samples",
            "baseline_DFMI",
            "baseline_IDELB",
            "augmented_DFMI",
            "augmented_IDELB",
            "CL_abs",
            "CL_rel",
        ],
    )
    _write_csv(
        OUT / "out_of_family_anti_classifier.csv",
        anti_rows,
        [
            "dataset",
            "n_samples",
            "baseline_IDELB",
            "augmented_IDELB",
            "CL_rel",
            "status",
            "independent_out_of_family",
        ],
    )
    _write_csv(
        OUT / "decision_baseline_comparison.csv",
        regret_rows,
        [
            "dataset",
            "decision_regret_amount_vs_context",
        ],
    )
    _write_csv(
        OUT / "coarse_graining_monotonicity.csv",
        monotonicity_rows,
        [
            "lane",
            "target",
            "flow_values",
            "monotone_nondecreasing",
            "status",
        ],
    )
    _write_csv(
        OUT / "stability_checks.csv",
        stability_rows,
        [
            "case_id",
            "perturbation_scale",
            "exact_recoverable",
            "decoder_operator_norm",
            "perturbation_operator_norm",
            "predicted_error_upper_bound",
            "empirical_max_error",
            "upper_bound_holds_on_box_vertices",
        ],
    )

    summary = {
        "datasets_scored": [r["dataset"] for r in reduction_rows],
        "anti_classifier_survivors": [r["dataset"] for r in anti_rows if r["status"] == "SURVIVES"],
        "independent_out_of_family_survivors": [
            r["dataset"] for r in anti_rows if r["status"] == "SURVIVES" and r["independent_out_of_family"] == 1
        ],
        "stability_all_bounds_hold": bool(all(int(r["upper_bound_holds_on_box_vertices"]) == 1 for r in stability_rows)),
        "monotonicity_failures": [
            f"{r['lane']}::{r['target']}" for r in monotonicity_rows if int(r["monotone_nondecreasing"]) == 0
        ],
        "notes": [
            "Decision regret is a restricted compression-regret proxy, not a full Blackwell deficiency computation.",
            "Coarse-graining monotonicity is theorem-grade for finite sigma-algebra coarsening and validated on surrogate trends where available.",
        ],
    }
    with (OUT / "harness_summary.json").open("w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2)

    print(f"wrote {OUT / 'unified_cross_domain_reduction_metrics.csv'}")
    print(f"wrote {OUT / 'out_of_family_anti_classifier.csv'}")
    print(f"wrote {OUT / 'decision_baseline_comparison.csv'}")
    print(f"wrote {OUT / 'coarse_graining_monotonicity.csv'}")
    print(f"wrote {OUT / 'stability_checks.csv'}")
    print(f"wrote {OUT / 'harness_summary.json'}")


if __name__ == "__main__":
    main()
