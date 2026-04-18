# SFPR No-Go Candidates

Status: `EXPLORATION / NON-PROMOTED`

This file records no-go statements tested in the SFPR pass and their disposition.

## NG-1: Collapse No-Go

Statement:
If observation collapses target-distinguishing states into one record fiber, exact target recovery is impossible.

Status: `PROVED` (supported family), `LITERATURE-KNOWN`.

## NG-2: Context-Invariance No-Go

Statement:
Contextwise exact recoverability does not imply existence of a single context-invariant decoder.

Status: `PROVED` (supported family), `PLAUSIBLY DISTINCT` packaging in this corpus.

Evidence:
- `224` local-exact/global-fail witnesses.

## NG-3: Descriptor-Only Classifier No-Go

Statement:
No classifier using only rank/count/budget can exactly classify target recoverability across tested families.

Status: `PROVED` (supported family), `CLOSE PRIOR ART / REPACKAGED`.

Evidence:
- rank mismatch `1347`, budget mismatch `2980`, descriptor-opposite anomalies `281`.

## NG-4: Design-Criterion Sufficiency No-Go

Statement:
Maximizing global information criteria alone does not guarantee exact target recovery.

Status: `VALIDATED / EMPIRICAL ONLY`.

Evidence:
- `38` D-style vs alignment conflicts.

## NG-5: Formation Implies Recoverability No-Go

Statement:
Improved structure-formation scores do not imply improved recoverability.

Status: `VALIDATED / EMPIRICAL ONLY`.

Evidence:
- `143` formation-without-recoverability anomalies.

## NG-6: Persistence Under Perturbation No-Go

Statement:
Small context/representation perturbations can destroy shared recoverability even when local recoverability remains high.

Status: `VALIDATED / EMPIRICAL ONLY`.

Evidence:
- `223` context-drift flips and `152` model-mismatch instability anomalies.

## NG-7: Universal SFPR Law No-Go (Current Pass)

Statement:
A single broad SFPR law covering formation, persistence, collapse, recoverability, and design without branch restrictions is not supported.

Status: `PROVED` as a methodological no-go for this pass.

Reason:
- Formation layer remains theorem-weak.
- Most collapse/recoverability statements reduce to existing OCP/fiber logic unless scoped.
- Literature overlap is high outside narrow context/design split laws.

## Keep / Drop Decision

Keep as strong no-go package:
- NG-1, NG-2, NG-3.

Keep as validated risk diagnostics:
- NG-4, NG-5, NG-6.

Use as scope constraint:
- NG-7.
