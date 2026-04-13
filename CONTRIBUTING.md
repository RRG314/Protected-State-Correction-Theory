# Contributing to Protected-State Correction Theory

Thank you for taking this repository seriously enough to contribute to it.

This is a theorem-first research repository, not a general idea dump. Good contributions make the theory clearer, more reproducible, more falsifiable, or more useful. The best pull requests usually do one of four things:

- sharpen a theorem, proof, lemma, or no-go result
- improve a kept application lane without overclaiming it
- tighten the workbench so it explains the theory more faithfully
- improve validation, documentation, or reproducibility

## First Principles

Please keep these rules in mind before opening a pull request.

- Do not overclaim novelty.
- Do not upgrade a conditional or illustrative result to a proved result without a real proof.
- Do not force a bridge to a new system unless the operator-level fit is real.
- Do not hide counterexamples, failures, or limitations.
- Keep exact, asymptotic, conditional, rejected, and open material clearly separated.
- Prefer a narrow result with explicit assumptions over a broad claim with vague scope.

## Best Contribution Paths

The repository is especially open to contributions in these areas:

1. Theorem and proof refinement
   Add proof details, tighten assumptions, improve notation consistency, or sharpen statements already in the theorem spine.

2. No-go and falsification work
   Add counterexamples, impossibility witnesses, boundary cases, or better rejection criteria.

3. Physics and application extensions
   Only where the fit survives operator-level testing. Good examples are projection methods, constraint-preserving structures, or carefully delimited sector/recovery constructions.

4. Workbench and visualization improvements
   Improve clarity, state handling, export behavior, accessibility, or theorem-to-interface alignment.

5. Validation and reproducibility
   Add tests, strengthen validation examples, reduce ambiguity in generated outputs, or improve validation scripts.

6. Documentation
   Improve contributor guidance, reviewer-facing summaries, citations, and reading paths without diluting precision.

A more detailed map is available in [docs/overview/contributing-paths.md](docs/overview/contributing-paths.md).

## Before You Start

Please read these first:

1. [README.md](README.md)
2. [docs/finalization/architecture-final.md](docs/finalization/architecture-final.md)
3. [docs/finalization/theorem-spine-final.md](docs/finalization/theorem-spine-final.md)
4. [docs/finalization/no-go-spine-final.md](docs/finalization/no-go-spine-final.md)
5. [docs/overview/proof-status-map.md](docs/overview/proof-status-map.md)
6. [docs/peer_review/how-to-read-this-repo.md](docs/peer_review/how-to-read-this-repo.md)

If you are working on the workbench, also read:

- [docs/app/workbench-overview.md](docs/app/workbench-overview.md)
- [docs/app/module-theory-map.md](docs/app/module-theory-map.md)

## How to Contribute Well

### For theorem or proof contributions

Please include:

- the exact statement you are adding or changing
- assumptions written explicitly
- proof, proof sketch, or the exact gap being closed
- whether the result is proved, conditional, or still open
- the files and claim IDs affected

If a result depends on a narrower setting than the current text suggests, narrowing it is a valid contribution.

### For physics or application extensions

Please include:

- the protected object
- the disturbance family
- the correction operator or architecture
- whether the fit is exact, asymptotic, conditional, or rejected
- what is standard known structure in the outside field
- what this repository adds, if anything

Analogy-only proposals are welcome as discussion material, but they should not go into the kept theory path unless they survive formalization.

### For workbench contributions

Please keep the workbench tied to the math.

A workbench change should:

- improve visibility of what is being computed
- preserve the exact versus asymptotic distinction
- indicate whether the module is proved, conditional, or illustrative
- avoid adding UI clutter without explanatory gain
- match the corresponding theorem or no-go document

### For documentation contributions

Please write in a way that is:

- precise
- readable to a technical outsider
- conservative about novelty
- explicit about limits

## Development Setup

```bash
cd '/Users/stevenreid/Documents/New project/repos/ocp-research-program'
uv sync
```

If you are only working on documentation or the static workbench, a full Python environment may not be necessary, but please still run the validation script before you submit.

## Validation

Run the full validation suite before opening a pull request:

```bash
cd '/Users/stevenreid/Documents/New project/repos/ocp-research-program'
./scripts/validate/run_all.sh
```

This covers:

- generated inventory and claim outputs
- theorem and operator tests
- workbench consistency tests
- markdown link checks
- static workbench asset checks

If you changed only a narrow part of the repo, mention that in the pull request, but please still prefer a full validation run when practical.

## Pull Request Expectations

A good pull request should say:

- what changed
- why it changed
- whether anything was strengthened, narrowed, or rejected
- what validation you ran
- what remains open or unresolved

Please keep pull requests focused. Small, clean, well-scoped contributions are much easier to review than large mixed changes.

## What Not to Do

Please do not:

- submit large speculative rewrites without first anchoring them to the current theorem spine
- reintroduce demoted claims without new evidence
- convert rejected bridges into promoted paths without new operator-level structure
- turn the repo into a broad fluid, control, or ML theory repository
- remove limitations or negative results because they look inconvenient

## Questions and Proposal Quality

If you are unsure whether a direction fits, open an issue first.

The most helpful issue proposals usually include:

- the exact files involved
- the precise claim or system under discussion
- what part is already standard in the literature
- what you think is new, conditional, or doubtful
- what kind of evidence could settle it

## Code and Document Style

- Keep changes modular.
- Keep file names descriptive and stable.
- Keep equations and theorem statements consistent with existing notation unless there is a strong reason to refactor.
- Add comments only when they materially improve understanding.
- Prefer clarity over compression.

## Community Standards

Please follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

For reporting repository or workbench security issues, see [SECURITY.md](SECURITY.md).
