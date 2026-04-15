# Structural Discovery Formalism

Structural Discovery works with a problem tuple

\[
\mathcal{P} = (X, A, p, M, \mathcal{R}, \mathcal{U}, \Sigma)
\]

where:

- `X` is the ambient state space.
- `A \subseteq X` is the admissible family.
- `p : A 	o P` is the protected object or protected variable.
- `M : A 	o Y` is the current observation / record map.
- `\mathcal{R}` is the current recovery or correction architecture class.
- `\mathcal{U}` is the allowed augmentation class.
- `\Sigma` is the success criterion, usually exact, approximate, asymptotic, or impossible recovery.

## Regimes

Exact:

\[
\exists R : Y 	o P 	ext{ such that } R(M(x)) = p(x) \quad orall x \in A.
\]

Approximate:

\[
\exists R : Y 	o P 	ext{ with controlled error } d_P(R(M(x)), p(x)) \leq arepsilon
\]

on the chosen family or sampled family.

Asymptotic:

There is no one-shot exact recovery map in the current static architecture, but there exists an observer or generator architecture whose online estimate converges to the protected target.

Impossible:

No recovery map inside the chosen architecture can recover the protected variable on the admissible family.

## Structural Failure Modes

Structural Discovery promotes a small set of named failure modes.

- Fiber collision: different protected values share the same record.
- Row-space insufficiency: the protected rows do not lie in the active record row space.
- Missing support: the protected target uses modes absent from the retained record.
- Hidden functional: the protected functional does not lie in the finite-history or sensor-generated family.
- Architecture mismatch: the record family may be insufficient for exact recovery but still supports an observer or asymptotic design.
- Boundary incompatibility: the obvious projector is not compatible with the protected class on the chosen bounded domain.

## Discovery Map

The Structural Discovery engine computes a discovery report

\[
D(\mathcal{P}) = (F, W, U, C, V)
\]

where:

- `F` is the detected failure summary.
- `W` is the weaker-target set already recoverable.
- `U` is the candidate augmentation set.
- `C` is the chosen comparison path.
- `V` is the validation evidence for before versus after.

## Minimal Augmentation In The Restricted-Linear Case

On the restricted-linear branch with admissible family `A = {Fz : ||z||_\infty \leq B}` and protected map `p(x) = Lx`, exact recovery from record `M(x) = Ox` is controlled by the restricted row-space condition on `OF` and `LF`.

The unrestricted augmentation count is

\[
\delta(O, L; F) = \operatorname{rank}\!egin{bmatrix}OF \ LF\end{bmatrix} - \operatorname{rank}(OF).
\]

Inside a finite candidate library, Structural Discovery searches for the smallest subset of candidate rows whose addition makes the protected rows recoverable.

## Family-Specific Thresholds Used By The Studio

The studio currently uses validated family-specific thresholds in three places.

Periodic modal family:

- exact recovery begins when the retained cutoff contains the entire protected support on the tested family.

Diagonal control family:

- exact recovery begins when the finite history is long enough to interpolate the protected functional on the active sensor spectrum.

Fixed-basis qubit family:

- stronger phase-sensitive targets fail while the weaker `z` target remains exact.

These are deliberately scoped results, not universal laws.
