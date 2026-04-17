#!/usr/bin/env python3
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLAIM_REGISTRY = ROOT / 'docs/overview/claim-registry.md'
OUT_CSV = ROOT / 'data/generated/falsification/full_claim_audit.csv'
OUT_MD = ROOT / 'docs/falsification/full_claim_audit.md'


@dataclass
class ClaimRow:
    claim_id: str
    short_statement: str
    branch: str
    current_status_label: str
    source_files: str
    claim_kind: str
    current_evidence_type: str
    test_method_to_use: str
    falsification_risk_level: str
    final_verdict: str


def parse_markdown_table(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding='utf-8')
    lines = [ln for ln in text.splitlines() if ln.strip().startswith('|')]
    header = [x.strip() for x in lines[0].strip('|').split('|')]
    rows = []
    for ln in lines[2:]:
        cells = [x.strip() for x in ln.strip('|').split('|')]
        if len(cells) != len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return rows


def branch_for_claim(cid: str, short: str) -> str:
    explicit = {
        'OCP-001': 'A', 'OCP-002': 'A', 'OCP-003': 'A', 'OCP-016': 'A',
        'OCP-005': 'B', 'OCP-017': 'B', 'OCP-019': 'B', 'OCP-021': 'B',
        'OCP-006': 'C', 'OCP-027': 'C',
        'OCP-023': 'D', 'OCP-028': 'D', 'OCP-029': 'D', 'OCP-044': 'D',
        'OCP-004': 'E', 'OCP-013': 'E', 'OCP-014': 'E', 'OCP-015': 'E', 'OCP-020': 'E',
        'OCP-030': 'F', 'OCP-031': 'F', 'OCP-032': 'F', 'OCP-033': 'F', 'OCP-034': 'F', 'OCP-035': 'F', 'OCP-036': 'F', 'OCP-037': 'F', 'OCP-038': 'F', 'OCP-039': 'F', 'OCP-040': 'F', 'OCP-041': 'F', 'OCP-042': 'F', 'OCP-043': 'F',
        'OCP-045': 'G', 'OCP-046': 'G', 'OCP-047': 'G',
        'OCP-048': 'H', 'OCP-049': 'H', 'OCP-050': 'H', 'OCP-051': 'H', 'OCP-052': 'H', 'OCP-053': 'H',
        'OCP-007': 'J', 'OCP-008': 'J', 'OCP-022': 'J', 'OCP-024': 'J', 'OCP-025': 'J', 'OCP-026': 'J',
        'OCP-009': 'K', 'OCP-010': 'K', 'OCP-018': 'K',
        'OCP-011': 'I', 'OCP-012': 'I',
    }
    if cid in explicit:
        return explicit[cid]
    low = short.lower()
    if 'workbench' in low or 'studio' in low:
        return 'I'
    return 'K'


def kind_for_claim(short: str, status: str) -> str:
    low = short.lower()
    if any(x in low for x in ('workbench', 'studio', 'engineering design')):
        return 'tool'
    if any(x in low for x in ('bridge', 'fit', 'extension')):
        return 'bridge'
    if status in {'ANALOGY ONLY'}:
        return 'interpretive'
    if status in {'VALIDATED'}:
        return 'empirical'
    return 'theorem'


def method_for_branch(branch: str) -> str:
    return {
        'A': 'exact linear algebra + projector witness search',
        'B': 'sector overlap witness + basis-invariant checks',
        'C': 'FFT/Helmholtz recomputation + idempotence tests',
        'D': 'bounded-domain counterexample generation + boundary diagnostics',
        'E': 'spectral decomposition + non-normal generator stress tests',
        'F': 'fiber/collision brute-force + threshold recomputation',
        'G': 'row-space/kernel automation + anti-classifier witness regeneration',
        'H': 'logical dependency audit + family-enlargement/mismatch stress',
        'I': 'workbench consistency tests + export/label checks',
        'J': 'bridge-scope check + theorem-vs-analogy separation',
        'K': 'meta-layer overlap and invariant reproducibility checks',
    }[branch]


def risk_for_claim(status: str, kind: str, branch: str) -> str:
    if status in {'OPEN', 'ANALOGY ONLY'}:
        return 'High'
    if status in {'DISPROVED', 'RETRACTED'}:
        return 'Low'
    if kind == 'bridge' or branch in {'J', 'K'}:
        return 'High'
    if status in {'CONDITIONAL', 'VALIDATED'}:
        return 'Medium'
    return 'Medium'


def main() -> None:
    registry_rows = parse_markdown_table(CLAIM_REGISTRY)
    out: list[ClaimRow] = []

    for row in registry_rows:
        cid = row['Claim ID'].strip()
        short = row['Short Name'].strip()
        status = row['Status'].strip().upper()
        evidence = row['Evidence'].strip()
        key_files = row['Key Files'].strip()
        branch = branch_for_claim(cid, short)
        kind = kind_for_claim(short, status)
        out.append(
            ClaimRow(
                claim_id=cid,
                short_statement=short,
                branch=branch,
                current_status_label=status,
                source_files=key_files,
                claim_kind=kind,
                current_evidence_type=evidence,
                test_method_to_use=method_for_branch(branch),
                falsification_risk_level=risk_for_claim(status, kind, branch),
                final_verdict=status,
            )
        )

    out.extend([
        ClaimRow(
            claim_id='WB-001',
            short_statement='Benchmark console module-health rows match validated workbench surfaces.',
            branch='I',
            current_status_label='VALIDATED',
            source_files='docs/workbench/lib/engine/benchmarkConsole.js; tests/consistency/workbench_static.test.mjs',
            claim_kind='tool',
            current_evidence_type='node consistency tests + generated validation snapshot',
            test_method_to_use=method_for_branch('I'),
            falsification_risk_level='High',
            final_verdict='VALIDATED',
        ),
        ClaimRow(
            claim_id='META-001',
            short_statement='Descriptor-fiber invariants (DFMI/IDELB/CL) quantify finite-class anti-classifier limits.',
            branch='K',
            current_status_label='PROVED ON SUPPORTED FAMILY',
            source_files='docs/research-program/descriptor-fiber-anti-classifier-branch-overview.md; data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.json',
            claim_kind='theorem',
            current_evidence_type='finite-class theorem + regenerated witness statistics',
            test_method_to_use=method_for_branch('K'),
            falsification_risk_level='Medium',
            final_verdict='PROVED ON SUPPORTED FAMILY',
        ),
    ])

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].__dict__.keys()))
        writer.writeheader()
        for r in out:
            writer.writerow(r.__dict__)

    lines = [
        '# Full Claim Audit',
        '',
        'Date: 2026-04-17',
        'Method: claim-registry extraction + branch mapping + explicit tool/meta additions.',
        '',
        '| Claim ID | Short Statement | Branch | Current Status | Claim Type | Evidence Type | Test Method | Risk | Final Verdict |',
        '| --- | --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    for r in out:
        lines.append(
            f"| {r.claim_id} | {r.short_statement} | {r.branch} | {r.current_status_label} | {r.claim_kind} | {r.current_evidence_type} | {r.test_method_to_use} | {r.falsification_risk_level} | {r.final_verdict} |"
        )

    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'wrote {OUT_CSV}')
    print(f'wrote {OUT_MD}')


if __name__ == '__main__':
    main()
