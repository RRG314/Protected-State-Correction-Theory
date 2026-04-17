# Literature Anchors

## Purpose

The fiber language clarifies the branch, but it is not itself claimed as literature novelty.
This note records the minimum literature-shaped comparison plan needed to avoid both rediscovery and overclaiming.

## Standard background areas

### Information theory
- Shannon output ambiguity and many-to-one channel structure.

### Coding theory
- Hamming detect-versus-correct logic and syndrome ambiguity.

### Inverse problems
- ill-posedness: nonexistence, nonuniqueness, instability.
- anchor: [Springer survey volume on inverse problems](https://link.springer.com/book/10.1007/978-3-7091-6296-5)

### Control / observability
- Kalman-style observability tradition and partial-state reconstruction.
- structural identifiability / observability review anchor: [Villaverde 2018](https://arxiv.org/abs/1812.04525)
- sensor-placement / structural observability anchor: [Hu and Fan 2024](https://www.sciencedirect.com/science/article/pii/S0191261524001814)

### PDE-constrained inverse problems
- state-dependent parameter identification, data limitation, model-class dependence.
- anchor: [Bukshtynov 2026 survey](https://arxiv.org/abs/2601.10920)

## Strongest repo-local package to compare against the literature

The most important comparison cluster is now:
- `OCP-049` no rank-only exact classifier theorem,
- `OCP-050` no fixed-library budget-only exact classifier theorem,
- `OCP-051` noisy weaker-versus-stronger separation theorem,
- `OCP-052` restricted-linear family-enlargement false-positive theorem.

## Honest reading of novelty status

### Likely literature-known in spirit
- factorization / fiber exactness,
- generic collision impossibility,
- family restriction as a source of identifiability failure.

### Repo-new and potentially publishable in exact current form
- the anti-classifier theorem package on the supported restricted-linear class,
- the exact family-enlargement false-positive theorem as packaged with explicit decoder lower bounds and artifact-backed witnesses,
- the theorem-to-tool warning layer tying those results into the workbench.

### What future review must compare against
- structural identifiability literature,
- sensor placement / observability geometry,
- PDE inverse problems under partial data,
- model discrepancy / model misspecification literature,
- coarse-versus-refined discretization stability in inverse problems.
