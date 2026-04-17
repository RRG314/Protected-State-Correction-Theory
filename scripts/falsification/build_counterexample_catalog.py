#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNI = ROOT / 'data/generated/unified-recoverability'
META = ROOT / 'data/generated/descriptor-fiber-anti-classifier'
LEGACY_META = ROOT / 'data/generated/meta-theory'
OUT_CSV = ROOT / 'data/generated/falsification/counterexample_catalog.csv'
OUT_MD = ROOT / 'docs/falsification/counterexample_catalog.md'


def load_csv(path: Path):
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def main() -> None:
    rows = []

    rank_rows = load_csv(UNI / 'rank_only_classifier_witnesses.csv')
    for i, r in enumerate(rank_rows[:8], start=1):
        rows.append({
            'witness_id': f'CX-RANK-{i:03d}',
            'branch': 'G/H',
            'claim_attacked': 'OCP-047/OCP-049',
            'counterexample_type': 'same-rank opposite-verdict',
            'descriptor': f"(n,r,k)=({r['ambient_dimension']},{r['protected_rank']},{r['observation_rank']})",
            'evidence_key': f"rowspace_residual exact={r['exact_rowspace_residual']} fail={r['fail_rowspace_residual']}; collision_gap exact={r['exact_collision_gap']} fail={r['fail_collision_gap']}",
            'status': 'VALIDATED',
            'source_file': str(UNI / 'rank_only_classifier_witnesses.csv'),
        })

    budget_rows = load_csv(UNI / 'candidate_library_budget_witnesses.csv')
    keep = 0
    for r in budget_rows:
        if int(r['exact_count']) > 0 and int(r['fail_count']) > 0:
            keep += 1
            rows.append({
                'witness_id': f'CX-BUDGET-{keep:03d}',
                'branch': 'G/H',
                'claim_attacked': 'OCP-050',
                'counterexample_type': 'same-budget opposite-verdict',
                'descriptor': f"(n,r,k,c)=({r['ambient_dimension']},{r['protected_rank']},{r['selection_size']},{r['exact_total_cost']})",
                'evidence_key': f"exact_count={r['exact_count']} fail_count={r['fail_count']}",
                'status': 'VALIDATED',
                'source_file': str(UNI / 'candidate_library_budget_witnesses.csv'),
            })
            if keep >= 8:
                break

    fam = load_csv(UNI / 'family_enlargement_false_positive.csv')[0]
    rows.append({
        'witness_id': 'CX-FAMILY-001',
        'branch': 'G/H',
        'claim_attacked': 'OCP-052',
        'counterexample_type': 'exact-on-small fail-on-large',
        'descriptor': f"small_dim={fam['small_family_dimension']} large_dim={fam['large_family_dimension']}",
        'evidence_key': f"small_exact={fam['small_exact_recoverable']} large_exact={fam['large_exact_recoverable']} lower_bound={fam['larger_family_impossibility_lower_bound']}",
        'status': 'VALIDATED',
        'source_file': str(UNI / 'family_enlargement_false_positive.csv'),
    })

    mismatch = load_csv(UNI / 'canonical_model_mismatch.csv')
    j = 0
    for r in mismatch:
        if abs(float(r['subspace_distance'])) > 1e-12:
            j += 1
            rows.append({
                'witness_id': f'CX-MISMATCH-{j:03d}',
                'branch': 'G/H',
                'claim_attacked': 'OCP-053',
                'counterexample_type': 'mismatched-decoder instability',
                'descriptor': f"beta_true={r['beta_true']} beta_ref={r['beta_reference']}",
                'evidence_key': f"distance={r['subspace_distance']} formula={r['formula_max_error']} brute={r['brute_force_max_error']}",
                'status': 'VALIDATED',
                'source_file': str(UNI / 'canonical_model_mismatch.csv'),
            })

    periodic = load_csv(UNI / 'periodic_refinement_false_positive.csv')[0]
    rows.append({
        'witness_id': 'CX-PERIODIC-001',
        'branch': 'F/H',
        'claim_attacked': 'family-blind exactness overclaim',
        'counterexample_type': 'coarse exact but refined fail',
        'descriptor': f"cutoff={periodic['cutoff']}",
        'evidence_key': f"coarse_exact={periodic['coarse_exact_recoverable']} refined_exact={periodic['refined_exact_recoverable']} refined_lb={periodic['refined_family_impossibility_lower_bound']}",
        'status': 'VALIDATED',
        'source_file': str(UNI / 'periodic_refinement_false_positive.csv'),
    })

    meta_json = META / 'meta_classifier_invariants.json'
    if not meta_json.exists():
        meta_json = LEGACY_META / 'meta_classifier_invariants.json'

    with meta_json.open(encoding='utf-8') as f:
        meta = json.load(f)
    for item in meta['summary']:
        rows.append({
            'witness_id': f"CX-META-{item['descriptor']}",
            'branch': 'K',
            'claim_attacked': 'amount-only descriptor sufficiency',
            'counterexample_type': 'descriptor-fiber mixedness',
            'descriptor': item['descriptor'],
            'evidence_key': f"mixed={item['mixed_values']}/{item['descriptor_values']} IDELB={item['irreducible_error_lb']}",
            'status': 'VALIDATED',
            'source_file': str(meta_json),
        })

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        '# Counterexample Catalog',
        '',
        'Date: 2026-04-17',
        '',
        '| Witness ID | Branch | Claim Attacked | Type | Descriptor | Evidence | Status | Source |',
        '| --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    for r in rows:
        lines.append(
            f"| {r['witness_id']} | {r['branch']} | {r['claim_attacked']} | {r['counterexample_type']} | {r['descriptor']} | {r['evidence_key']} | {r['status']} | `{r['source_file']}` |"
        )
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    print(f'wrote {OUT_CSV}')
    print(f'wrote {OUT_MD}')


if __name__ == '__main__':
    main()
