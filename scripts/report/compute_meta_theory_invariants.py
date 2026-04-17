#!/usr/bin/env python3
"""Compute descriptor-fiber anti-classifier invariants from existing witness tables.

Canonical outputs:
- data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.csv
- data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.json

Legacy compatibility outputs (kept during naming transition):
- data/generated/meta-theory/meta_classifier_invariants.csv
- data/generated/meta-theory/meta_classifier_invariants.json
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, Tuple

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "generated" / "unified-recoverability"
OUT_DIR = ROOT / "data" / "generated" / "descriptor-fiber-anti-classifier"
LEGACY_OUT_DIR = ROOT / "data" / "generated" / "meta-theory"


def _stats_from_counts(counts: Dict[Tuple[str, ...], Tuple[int, int]]) -> dict:
    total_values = len(counts)
    mixed_values = sum(1 for e, f in counts.values() if e > 0 and f > 0)
    total_exact = sum(e for e, _ in counts.values())
    total_fail = sum(f for _, f in counts.values())
    total_systems = total_exact + total_fail
    irreducible_error_lb = (
        sum(min(e, f) for e, f in counts.values()) / total_systems if total_systems else 0.0
    )
    return {
        "descriptor_values": total_values,
        "mixed_values": mixed_values,
        "ambiguity_rate": (mixed_values / total_values if total_values else 0.0),
        "total_exact": total_exact,
        "total_fail": total_fail,
        "total_systems": total_systems,
        "irreducible_error_lb": irreducible_error_lb,
        "majority_accuracy_ub": 1.0 - irreducible_error_lb,
        "perfect_classifier_possible": mixed_values == 0,
    }


def rank_only_amount_counts() -> Dict[Tuple[str, ...], Tuple[int, int]]:
    path = DATA_DIR / "rank_only_classifier_witnesses.csv"
    counts: Dict[Tuple[str, ...], list[int]] = defaultdict(lambda: [0, 0])
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (
                row["ambient_dimension"],
                row["protected_rank"],
                row["observation_rank"],
            )
            # each row is an explicit exact/fail opposite-verdict witness pair
            counts[key][0] += 1
            counts[key][1] += 1
    return {k: (v[0], v[1]) for k, v in counts.items()}


def rank_with_compatibility_counts() -> Dict[Tuple[str, ...], Tuple[int, int]]:
    path = DATA_DIR / "rank_only_classifier_witnesses.csv"
    counts: Dict[Tuple[str, ...], list[int]] = defaultdict(lambda: [0, 0])
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            base = (
                row["ambient_dimension"],
                row["protected_rank"],
                row["observation_rank"],
            )
            # split witness pair by compatibility proxy (row-space residual)
            key_exact = base + ("residual=0",)
            key_fail = base + ("residual>0",)
            counts[key_exact][0] += 1
            counts[key_fail][1] += 1
    return {k: (v[0], v[1]) for k, v in counts.items()}


def budget_only_amount_counts() -> Dict[Tuple[str, ...], Tuple[int, int]]:
    path = DATA_DIR / "candidate_library_budget_witnesses.csv"
    counts: Dict[Tuple[str, ...], list[int]] = defaultdict(lambda: [0, 0])
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (
                row["ambient_dimension"],
                row["protected_rank"],
                row["selection_size"],
                row["exact_total_cost"],
            )
            counts[key][0] += int(row["exact_count"])
            counts[key][1] += int(row["fail_count"])
    return {k: (v[0], v[1]) for k, v in counts.items()}


def summarize(name: str, counts: Dict[Tuple[str, ...], Tuple[int, int]]) -> dict:
    out = {"descriptor": name}
    out.update(_stats_from_counts(counts))
    return out


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    LEGACY_OUT_DIR.mkdir(parents=True, exist_ok=True)

    rank_counts = rank_only_amount_counts()
    rank_plus_comp = rank_with_compatibility_counts()
    budget_counts = budget_only_amount_counts()

    summaries = [
        summarize("rank_tuple_(n,r,k)", rank_counts),
        summarize("rank_tuple_plus_rowspace_proxy", rank_plus_comp),
        summarize("budget_tuple_(n,r,selection,cost)", budget_counts),
    ]

    # add compatibility lift statistic for the rank witness program
    rank_err = summaries[0]["irreducible_error_lb"]
    rank_plus_err = summaries[1]["irreducible_error_lb"]
    lift = rank_err - rank_plus_err

    payload = {
        "source_files": [
            str(DATA_DIR / "rank_only_classifier_witnesses.csv"),
            str(DATA_DIR / "candidate_library_budget_witnesses.csv"),
        ],
        "summary": summaries,
        "derived": {
            "rank_to_rank_plus_compatibility_error_lift": lift,
            "interpretation": "Reduction in irreducible amount-only classification error when adding a compatibility proxy.",
        },
    }

    fieldnames = list(summaries[0].keys())

    def write_outputs(out_dir: Path) -> tuple[Path, Path]:
        csv_path = out_dir / "meta_classifier_invariants.csv"
        with csv_path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(summaries)

        json_path = out_dir / "meta_classifier_invariants.json"
        with json_path.open("w") as f:
            json.dump(payload, f, indent=2)
        return csv_path, json_path

    primary_csv, primary_json = write_outputs(OUT_DIR)
    legacy_csv, legacy_json = write_outputs(LEGACY_OUT_DIR)

    print(f"Wrote {primary_csv}")
    print(f"Wrote {primary_json}")
    print(f"Wrote {legacy_csv}")
    print(f"Wrote {legacy_json}")


if __name__ == "__main__":
    main()
