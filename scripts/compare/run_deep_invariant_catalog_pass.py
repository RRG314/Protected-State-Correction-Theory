#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN = ROOT / "data" / "generated"
OUT = GEN / "invariants"
OUT.mkdir(parents=True, exist_ok=True)


def _read_csv(path: Path):
    if not path.exists():
        return []
    with path.open() as f:
        return list(csv.DictReader(f))


def _to_int(x: str | None):
    if x is None:
        return ""
    x = str(x).strip()
    if x == "":
        return ""
    try:
        return int(float(x))
    except Exception:
        return ""


def _to_float(x: str | None):
    if x is None:
        return ""
    x = str(x).strip()
    if x == "":
        return ""
    try:
        return float(x)
    except Exception:
        return ""


def build_deep_catalog() -> list[dict]:
    out: list[dict] = []
    rid = 0

    mc = _read_csv(GEN / "context_sensitive_recoverability" / "multicontext_witness_catalog.csv")
    for r in mc:
        local = _to_int(r.get("local_exact_all"))
        shared = _to_int(r.get("shared_exact"))
        gap = _to_int(r.get("context_invariance_gap"))
        if shared == 1:
            status = "PROVED ON SUPPORTED FAMILY"
        elif local == 1 and shared == 0:
            status = "PROVED ON SUPPORTED FAMILY"
        else:
            status = "VALIDATED / NUMERICAL ONLY"
        out.append(
            {
                "record_id": f"deep_{rid}",
                "source": "multicontext_witness",
                "family": r.get("mode", ""),
                "mode": r.get("mode", ""),
                "descriptor_signature": r.get("descriptor_signature", ""),
                "n": _to_int(r.get("n")),
                "p": _to_int(r.get("m_per_context")),
                "q": "",
                "k": _to_int(r.get("k_contexts")),
                "total_budget": _to_int(r.get("total_budget")),
                "stack_rank": _to_int(r.get("stack_rank")),
                "target_rank": "",
                "local_exact": local,
                "shared_exact": shared,
                "context_gap": gap,
                "cid": _to_float(r.get("cid")),
                "rowspace_residual": _to_float(r.get("stack_residual")),
                "collision_gap": "",
                "collision_gap_mode": "",
                "delta_free": _to_int(r.get("shared_aug_threshold")),
                "delta_c": "",
                "library_rank_gain": "",
                "library_full_feasible": "",
                "dfmi": "",
                "idelb": "",
                "cl": "",
                "status_label": status,
                "scope_note": "context-indexed supported family",
            }
        )
        rid += 1

    aug = _read_csv(GEN / "context_sensitive_recoverability" / "augmentation_threshold_catalog.csv")
    for r in aug:
        out.append(
            {
                "record_id": f"deep_{rid}",
                "source": "augmentation_threshold",
                "family": "local_exact_global_fail",
                "mode": r.get("mode", ""),
                "descriptor_signature": r.get("descriptor_signature", ""),
                "n": _to_int(r.get("n")),
                "p": _to_int(r.get("m_per_context")),
                "q": "",
                "k": _to_int(r.get("k_contexts")),
                "total_budget": _to_int(r.get("total_budget")),
                "stack_rank": _to_int(r.get("stack_rank")),
                "target_rank": "",
                "local_exact": _to_int(r.get("local_exact_all")),
                "shared_exact": _to_int(r.get("shared_exact")),
                "context_gap": _to_int(r.get("context_invariance_gap")),
                "cid": _to_float(r.get("cid")),
                "rowspace_residual": _to_float(r.get("stack_residual")),
                "collision_gap": "",
                "collision_gap_mode": "",
                "delta_free": _to_int(r.get("shared_aug_threshold")),
                "delta_c": "",
                "library_rank_gain": "",
                "library_full_feasible": "",
                "dfmi": "",
                "idelb": "",
                "cl": "",
                "status_label": "PROVED ON SUPPORTED FAMILY",
                "scope_note": "local-exact/global-fail augmentation catalog",
            }
        )
        rid += 1

    ao = _read_csv(GEN / "context_sensitive_recoverability" / "agreement_operator_witness_catalog.csv")
    for r in ao:
        local = _to_int(r.get("local_exact_all"))
        shared = _to_int(r.get("invariant_exact_direct"))
        status = "PROVED ON SUPPORTED FAMILY" if (local == 1 and (shared in (0, 1))) else "VALIDATED / NUMERICAL ONLY"
        out.append(
            {
                "record_id": f"deep_{rid}",
                "source": "agreement_operator_witness",
                "family": r.get("mode", ""),
                "mode": r.get("mode", ""),
                "descriptor_signature": r.get("descriptor_signature", ""),
                "n": _to_int(r.get("n")),
                "p": _to_int(r.get("p_record")),
                "q": _to_int(r.get("q_target")),
                "k": _to_int(r.get("k_contexts")),
                "total_budget": _to_int(_to_int(r.get("p_record")) * _to_int(r.get("k_contexts")) if r.get("p_record") and r.get("k_contexts") else ""),
                "stack_rank": _to_int(r.get("descriptor_signature", "").split("stackr")[-1]) if "stackr" in r.get("descriptor_signature", "") else "",
                "target_rank": _to_int(r.get("descriptor_signature", "").split("targetr")[-1]) if "targetr" in r.get("descriptor_signature", "") else "",
                "local_exact": local,
                "shared_exact": shared,
                "context_gap": 1 if local == 1 and shared == 0 else 0,
                "cid": _to_float(r.get("stack_residual_norm")),
                "rowspace_residual": _to_float(r.get("stack_residual_norm")),
                "collision_gap": "",
                "collision_gap_mode": "",
                "delta_free": _to_int(r.get("free_aug_threshold")),
                "delta_c": _to_int(r.get("library_target_defect")),
                "library_rank_gain": _to_int(r.get("library_rank_gain")),
                "library_full_feasible": _to_int(r.get("library_full_pool_feasible")),
                "dfmi": "",
                "idelb": "",
                "cl": "",
                "status_label": status,
                "scope_note": "agreement-lift and library-constrained recoverability",
            }
        )
        rid += 1

    inv = _read_csv(OUT / "invariant_witness_catalog.csv")
    for r in inv:
        if r.get("row_kind") == "system":
            out.append(
                {
                    "record_id": f"deep_{rid}",
                    "source": "invariant_witness",
                    "family": r.get("family", ""),
                    "mode": r.get("role", ""),
                    "descriptor_signature": r.get("amount_signature", ""),
                    "n": _to_int(r.get("n")),
                    "p": _to_int(r.get("p")),
                    "q": _to_int(r.get("q")),
                    "k": _to_int(r.get("k")),
                    "total_budget": _to_int(r.get("total_budget")),
                    "stack_rank": _to_int(r.get("stack_rank")),
                    "target_rank": _to_int(r.get("target_rank")),
                    "local_exact": _to_int(r.get("local_exact_all")),
                    "shared_exact": _to_int(r.get("invariant_exact")),
                    "context_gap": _to_int(r.get("context_gap")),
                    "cid": _to_float(r.get("cid")),
                    "rowspace_residual": _to_float(r.get("rowspace_residual")),
                    "collision_gap": _to_float(r.get("collision_gap")),
                    "collision_gap_mode": r.get("collision_gap_mode", ""),
                    "delta_free": _to_int(r.get("delta_free")),
                    "delta_c": _to_int(r.get("delta_c")),
                    "library_rank_gain": _to_int(r.get("library_rank_gain")),
                    "library_full_feasible": _to_int(r.get("library_full_feasible")),
                    "dfmi": "",
                    "idelb": "",
                    "cl": "",
                    "status_label": "PROVED ON SUPPORTED FAMILY" if _to_int(r.get("invariant_exact")) in (0, 1) else "VALIDATED / NUMERICAL ONLY",
                    "scope_note": "compact theorem-pressure witness set",
                }
            )
        elif r.get("row_kind") == "meta_descriptor":
            out.append(
                {
                    "record_id": f"deep_{rid}",
                    "source": "invariant_meta_descriptor",
                    "family": "descriptor_fiber",
                    "mode": r.get("role", ""),
                    "descriptor_signature": "meta",
                    "n": "",
                    "p": "",
                    "q": "",
                    "k": "",
                    "total_budget": "",
                    "stack_rank": "",
                    "target_rank": "",
                    "local_exact": "",
                    "shared_exact": "",
                    "context_gap": "",
                    "cid": "",
                    "rowspace_residual": "",
                    "collision_gap": "",
                    "collision_gap_mode": "",
                    "delta_free": "",
                    "delta_c": "",
                    "library_rank_gain": "",
                    "library_full_feasible": "",
                    "dfmi": _to_float(r.get("descriptor_dfmi")),
                    "idelb": _to_float(r.get("descriptor_idelb")),
                    "cl": _to_float(r.get("descriptor_cl")),
                    "status_label": "PROVED ON SUPPORTED FAMILY",
                    "scope_note": "descriptor-fiber ambiguity meta invariant",
                }
            )
        rid += 1

    return out


def build_deep_stress() -> list[dict]:
    out: list[dict] = []
    sid = 0

    invs = _read_csv(OUT / "invariant_stress_catalog.csv")
    for r in invs:
        out.append(
            {
                "stress_id": f"dst_{sid}",
                "source": "invariant_stress",
                "base_id": r.get("base_system_id", ""),
                "stress_type": r.get("stress_type", ""),
                "descriptor_signature": "",
                "before_local_exact": _to_int(r.get("base_local_exact")),
                "before_shared_exact": _to_int(r.get("base_invariant_exact")),
                "after_local_exact": _to_int(r.get("stressed_local_exact")),
                "after_shared_exact": _to_int(r.get("stressed_invariant_exact")),
                "before_cid": _to_float(r.get("base_cid")),
                "after_cid": _to_float(r.get("stressed_cid")),
                "before_delta_free": _to_int(r.get("base_delta_free")),
                "after_delta_free": _to_int(r.get("stressed_delta_free")),
                "fragility_flag": _to_int(r.get("fragility_flag")),
                "severity": "high" if _to_int(r.get("fragility_flag")) == 1 else "low",
                "status_label": "VALIDATED / NUMERICAL ONLY",
                "note": r.get("notes", ""),
            }
        )
        sid += 1

    mm = _read_csv(GEN / "unified-recoverability" / "model_mismatch_stress.csv")
    for r in mm:
        out.append(
            {
                "stress_id": f"dst_{sid}",
                "source": "model_mismatch_stress",
                "base_id": r.get("label", ""),
                "stress_type": "model_mismatch",
                "descriptor_signature": f"dim{r.get('family_dimension','')}|dist{r.get('subspace_distance','')}",
                "before_local_exact": 1,
                "before_shared_exact": 1 if str(r.get("exact_recoverable_under_true_family", "")).lower() == "true" else 0,
                "after_local_exact": "",
                "after_shared_exact": "",
                "before_cid": "",
                "after_cid": "",
                "before_delta_free": "",
                "after_delta_free": "",
                "fragility_flag": 1 if _to_float(r.get("reference_decoder_max_error")) and _to_float(r.get("reference_decoder_max_error")) > 0 else 0,
                "severity": "medium",
                "status_label": "VALIDATED / NUMERICAL ONLY",
                "note": "off-family decoder error under subspace mismatch",
            }
        )
        sid += 1

    fe = _read_csv(GEN / "unified-recoverability" / "family_enlargement_false_positive.csv")
    for r in fe:
        out.append(
            {
                "stress_id": f"dst_{sid}",
                "source": "family_enlargement_false_positive",
                "base_id": "family_enlargement_case",
                "stress_type": "family_enlargement",
                "descriptor_signature": f"small{r.get('small_family_dimension','')}|large{r.get('large_family_dimension','')}",
                "before_local_exact": "",
                "before_shared_exact": 1 if str(r.get("small_exact_recoverable", "")).lower() == "true" else 0,
                "after_local_exact": "",
                "after_shared_exact": 1 if str(r.get("large_exact_recoverable", "")).lower() == "true" else 0,
                "before_cid": "",
                "after_cid": "",
                "before_delta_free": "",
                "after_delta_free": "",
                "fragility_flag": 1 if str(r.get("false_positive_risk", "")).lower() == "true" else 0,
                "severity": "high",
                "status_label": "PROVED ON SUPPORTED FAMILY",
                "note": "narrow-family exactness fails on enlarged family",
            }
        )
        sid += 1

    mc = _read_csv(GEN / "context_sensitive_recoverability" / "multicontext_witness_catalog.csv")
    for r in mc:
        if _to_int(r.get("enlargement_flip")) != 1:
            continue
        out.append(
            {
                "stress_id": f"dst_{sid}",
                "source": "multicontext_enlargement_flip",
                "base_id": r.get("family_id", ""),
                "stress_type": "family_enlargement",
                "descriptor_signature": r.get("descriptor_signature", ""),
                "before_local_exact": _to_int(r.get("local_exact_all")),
                "before_shared_exact": _to_int(r.get("shared_exact")),
                "after_local_exact": _to_int(r.get("enlarged_local_exact_all")),
                "after_shared_exact": _to_int(r.get("enlarged_shared_exact")),
                "before_cid": _to_float(r.get("cid")),
                "after_cid": "",
                "before_delta_free": _to_int(r.get("shared_aug_threshold")),
                "after_delta_free": "",
                "fragility_flag": 1,
                "severity": "high",
                "status_label": "VALIDATED / NUMERICAL ONLY",
                "note": "context-family enlargement changed shared verdict",
            }
        )
        sid += 1

    return out


def main():
    cat = build_deep_catalog()
    stress = build_deep_stress()

    cat_fields = [
        "record_id","source","family","mode","descriptor_signature","n","p","q","k","total_budget","stack_rank","target_rank","local_exact","shared_exact","context_gap","cid","rowspace_residual","collision_gap","collision_gap_mode","delta_free","delta_c","library_rank_gain","library_full_feasible","dfmi","idelb","cl","status_label","scope_note"
    ]
    stress_fields = [
        "stress_id","source","base_id","stress_type","descriptor_signature","before_local_exact","before_shared_exact","after_local_exact","after_shared_exact","before_cid","after_cid","before_delta_free","after_delta_free","fragility_flag","severity","status_label","note"
    ]

    with (OUT / "deep_invariant_catalog.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cat_fields)
        w.writeheader()
        w.writerows(cat)

    with (OUT / "deep_invariant_stress.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=stress_fields)
        w.writeheader()
        w.writerows(stress)

    summary = {
        "deep_catalog_rows": len(cat),
        "deep_stress_rows": len(stress),
        "sources": sorted({r["source"] for r in cat}),
        "stress_sources": sorted({r["source"] for r in stress}),
        "status": "EXPLORATION / NON-PROMOTED",
    }
    with (OUT / "deep_invariant_summary.json").open("w") as f:
        json.dump(summary, f, indent=2)

    print("wrote", OUT / "deep_invariant_catalog.csv", len(cat))
    print("wrote", OUT / "deep_invariant_stress.csv", len(stress))
    print("wrote", OUT / "deep_invariant_summary.json")


if __name__ == "__main__":
    main()
