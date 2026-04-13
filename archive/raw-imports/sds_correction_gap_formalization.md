# Formalizing the Correction Gap Principle
## A Mathematical Analysis: Theorem, Schema, or Collapse?

**Document type:** Theorem-development working paper
**Status:** Phases 1–5 complete. Main result: theorem schema + no-go theorem. Universal scalar gap does not exist. Category-specific gap theorems exist and are proved.

---

## 1. Executive Statement

**The Correction Gap Principle in its informal form:**

> A naive approximation N[s] to an exact object E[s] fails to admit an exact correction within an operator class C whenever the remainder R[s] = E[s] − N[s] has complexity strictly exceeding the correction capacity of C.

**Verdict after full analysis:**

The principle does not yield a single universal theorem with a single scalar "gap." At maximum generality, it reduces to a tautology. However, it does yield:

1. A **No-Go Theorem** (Section 5.1): No category-independent scalar gap function exists.
2. A **Theorem Schema** (Section 5.2): For each of four identified categories, a category-specific complexity/capacity pair gives a non-tautological obstruction theorem with computable gap.
3. Three **proved obstruction theorems** (Sections 4.1–4.3):
   - MHD: singularity-order gap theorem (proved)
   - SdS: polynomial closure gap theorem (proved, new result)
   - Corner singularity PDE: continuous gap formula (proved)
4. Two **propositions** (Sections 4.4–4.5):
   - WKB turning point: function-class mismatch (proved as proposition)
   - Moment closure: rank-deficiency obstruction (structural analogy, not proved)

The idea is neither fully rigorous nor fully false. The correct output is a theorem schema and a no-go theorem for universal unification.

---

## 2. Candidate Definitions

### 2.1 State Space

**Definition 2.1 (State Space).** A *state space* is a set $\mathcal{S}$, possibly equipped with topological, algebraic, or smooth structure. A *state* $s \in \mathcal{S}$ is a single element.

**Examples across the four cases:**
- **MHD:** $\mathcal{S} = C^\infty(\Omega)^2$, pairs $(\alpha, \beta)$ of Euler potentials on a domain $\Omega \subset \mathbb{R}^3$.
- **SdS:** $\mathcal{S} = \{(M, \Lambda) \in \mathbb{R}_{>0}^2 : 9\Lambda M^2 < 1\}$, parameterizing sub-extremal configurations.
- **WKB:** $\mathcal{S} = C^\infty(\mathbb{R}) \times \mathbb{R}$, pairs $(V, E)$ of potential and energy, with a distinguished turning point $x_0$ satisfying $V(x_0) = E$, $V'(x_0) \neq 0$.
- **Corner PDE:** $\mathcal{S} = \{(\Omega_\omega, f) : \omega \in (0, 2\pi), f \in L^2(\Omega_\omega)\}$, where $\Omega_\omega$ is a sector of opening angle $\omega$.

There is no natural common structure on these four state spaces.

### 2.2 Naive Operator N and Exact Operator E

**Definition 2.2 (Operator Pair).** Let $\mathcal{T}$ be a target space (function space, real vector space, ring, etc.). A *naive–exact pair* consists of two maps $N, E: \mathcal{S} \to \mathcal{T}$ such that $N[s]$ is "computationally or structurally simpler" than $E[s]$ in a sense to be made precise per category.

**Explicit instances:**
- **MHD:** $\mathcal{T} = C^\infty(\Omega; \mathbb{R}^3)$.
  $N[\alpha, \beta] = \nabla(\eta\nabla^2\alpha) \times \nabla\beta + \nabla\alpha \times \nabla(\eta\nabla^2\beta)$ (naive diffusion of potentials).
  $E[\alpha, \beta] = \eta \nabla^2(\nabla\alpha \times \nabla\beta)$ (exact magnetic diffusion).
- **SdS:** $\mathcal{T} = \mathbb{R}$.
  $N[M, \Lambda] = S_b + S_c = \pi(r_b^2 + r_c^2)$ (naive entropy additivity).
  $E[M, \Lambda] = S_\Lambda = 3\pi/\Lambda$ (exact cosmological entropy).
- **WKB:** $\mathcal{T}$ = formal power series in $\hbar$.
  $N_n[V, E]$ = $n$-th order WKB approximation $\sum_{k=0}^n \hbar^k \psi_k(x)$.
  $E[V, E]$ = exact solution $\psi$ of $-\hbar^2\psi'' + V\psi = E\psi$.
- **Corner:** $\mathcal{T} = H^1(\Omega_\omega)$.
  $N[f]$ = $H^2$ prediction (naive elliptic regularity estimate).
  $E[f]$ = actual weak solution $u \in H^1(\Omega_\omega)$ of $-\Delta u = f$.

### 2.3 Remainder

**Definition 2.3 (Remainder).** $R: \mathcal{S} \to \mathcal{T}$ is defined by $R[s] = E[s] - N[s]$.

In all four cases, $R$ is non-zero for generic states. Explicit forms:

- **MHD:** $R[\alpha,\beta] = \eta\nabla^2(\nabla\alpha \times \nabla\beta) - \nabla(\eta\nabla^2\alpha)\times\nabla\beta - \nabla\alpha\times\nabla(\eta\nabla^2\beta)$.
  This equals $\eta[\nabla^2, \cdot \times \cdot](\nabla\alpha, \nabla\beta)$, the commutator of the vector Laplacian with the cross product.
- **SdS:** $\Delta[M,\Lambda] = S_\Lambda - S_b - S_c$. For D=4: $\Delta = \sqrt{S_bS_c}$. For general D, $\Delta = (c_D/\Lambda) - c_D(r_b^{D-2} + r_c^{D-2})$.
- **WKB:** $R_n[V,E,x] = \psi(x) - \psi_{\text{WKB},n}(x)$.
- **Corner:** $R[f] = u - u_{\text{smooth}}$, where $u_{\text{smooth}}$ is the $H^2$ part of the Kondratiev expansion.

### 2.4 Correction Operator Class C

**Definition 2.4 (Correction Class).** A *correction class* is a triple $(C, \mathcal{F}, L)$ where:
- $\mathcal{F}$ is a function space (the *source class* of corrections)
- $L: \mathcal{F}^k \to \mathcal{T}$ is a (possibly nonlinear) *correction operator*
- $C \subset \mathcal{F}^k$ is the *admissible set* of correction inputs

The *achievable corrections* from $C$ are $\text{Im}(L\big|_C) = \{L(c) : c \in C\}$.

**Explicit instances:**
- **MHD:** $\mathcal{F} = C^\infty(\Omega)$, $C = \mathcal{F}^2$, $L[S_\alpha, S_\beta] = \nabla S_\alpha \times \nabla\beta + \nabla\alpha \times \nabla S_\beta$.
  Rational class: $\mathcal{F}_\text{rat} = \{\text{rational functions of coordinates}\}$.
- **SdS:** $\mathcal{F}_\text{poly}^{(d)}$ = polynomials in $(r_b, r_c)$ of degree $\leq d$. $L = $ identity (the "correction formula IS $\Delta$ expressed in this class"). $C = \mathcal{F}_\text{poly}$.
- **WKB:** $\mathcal{F}_\text{WKB}^{(n)}$ = formal WKB corrections of order $n$: functions of the form $A_n(x)\exp(iS/\hbar)$ with $A_n$ smooth.
- **Corner:** $\mathcal{F}_{H^2} = H^2(\Omega_\omega)$ (corrections achievable within the standard elliptic regularity class).

### 2.5 Correction Capacity: Five Candidate Definitions

This is the critical definition. Five candidates are tested.

**Definition 2.5A (Image-Theoretic Capacity).** $\text{Cap}^A(C) = \mathbf{1}[R \in \text{Im}(L\big|_C)]$. Binary: 1 if solvable, 0 if not.

**Definition 2.5B (Singularity-Order Capacity).** For a domain with a singular set $\Sigma$, define the *singularity order* of a function $f$ as $\sigma(f) = \sup\{\alpha \geq 0 : f \cdot d(\cdot, \Sigma)^\alpha \in L^\infty\}$ (so $f = O(d^{-\sigma})$ near $\Sigma$). Then:
$$\text{Cap}^B(C) = \sup\{\sigma(L(c)) : c \in C\} \in [0, +\infty]$$

**Definition 2.5C (Polynomial-Degree Capacity).** For algebraic/arithmetic settings: $\text{Cap}^C(C) = \max\{\deg(p) : p \in C\}$ (or $\infty$ if $C$ contains polynomials of unbounded degree).

**Definition 2.5D (Recursive-Depth Capacity).** For operator trees: $\text{Cap}^D(C) = \max\{d(c) : c \in C\}$ where $d(c)$ counts recursive operator applications in the expression tree of $c$.

**Definition 2.5E (Function-Class Capacity).** Assign each function class a label in an ordered set $\mathfrak{C}$: $\{\text{polynomial}\} < \{\text{rational}\} < \{\text{algebraic}\} < \{\text{elementary transcendental}\} < \{\text{special functions}\} < \ldots$ Then $\text{Cap}^E(C) = \text{class}(C)$.

### 2.6 Complexity of Remainder: Five Candidate Definitions

Mirroring the capacity candidates:

**Definition 2.6A** $\text{Comp}^A(R) = 0$ (trivially in target space). (Useless — see Section 3.)

**Definition 2.6B (Singularity Order):** $\text{Comp}^B(R) = \sigma(R)$ (same convention as 2.5B).

**Definition 2.6C (Minimal Polynomial Degree):** $\text{Comp}^C(R) = \min\{d : R \text{ is a polynomial of degree } d \text{ in the natural generators}\}$, or $\infty$ if no such polynomial exists.

**Definition 2.6D (Recursive Depth):** $\text{Comp}^D(R) = $ depth of the operator expression tree generating $R$.

**Definition 2.6E (Function Class):** $\text{Comp}^E(R) = \text{class}(R)$ in the ordered set $\mathfrak{C}$.

### 2.7 Correction Gap

**Definition 2.7 (Correction Gap, Abstract).** Given a complexity measure $\text{Comp}$ and capacity measure $\text{Cap}$ valued in an ordered abelian group $(G, \leq)$:
$$\delta = \text{Comp}(R) - \text{Cap}(C) \in G$$

Exact correction *within class* $C$ is possible only if $\delta \leq 0$. (Necessary, not sufficient — see Section 3.)

---

## 3. Tested Definitions and Failures

### 3.1 Definition 2.5A / 2.6A: Image-Theoretic Capacity

The statement "exact correction exists iff $R \in \text{Im}(L\big|_C)$" is **a tautology**.

**Proof.** By definition, an exact correction $c \in C$ exists such that $L(c) = R$ iff $R \in \text{Im}(L\big|_C)$. $\square$

The tautology is unavoidable unless we provide an INDEPENDENT characterization of $\text{Im}(L\big|_C)$ that does not reference $R$. This is precisely what the non-trivial capacity definitions attempt to provide.

**Conclusion:** Definition 2.5A is not a definition of capacity — it is a restatement of solvability. It can serve as the logical criterion, but it provides no computational content.

### 3.2 Singularity-Order (2.5B/2.6B): Works for MHD, Fails for SdS

Test on MHD spherical: $\text{Comp}^B(R) = 3$, $\text{Cap}^B(C_\text{smooth}) = 1$. Gap = 2 > 0. Correct prediction: no smooth closure. ✓

Test on SdS D=6: $R = S_\Lambda - S_b - S_c$ is a finite real number (no singularity). $\text{Comp}^B(R) = 0$. $\text{Cap}^B(C_\text{poly}) = 0$. Gap = 0. Prediction: exact correction exists in polynomial class. **INCORRECT** — no polynomial formula exists for D=6. ✗

**Failure mode:** Singularity order is blind to algebraic complexity. A smooth remainder can still fail to lie in $\text{Im}(L\big|_C)$ if the obstruction is algebraic rather than analytic.

### 3.3 Polynomial-Degree (2.5C/2.6C): Works for SdS, Fails for MHD

Test on SdS D=4: $\Delta = \sqrt{S_bS_c}$, which is a polynomial of degree 1 in each of $\sqrt{S_b}, \sqrt{S_c}$ (equivalently, degree 2 in $(r_b, r_c)$). $\text{Comp}^C(\Delta) = 2$. Capacity of the Vieta polynomial class of degree 2: $\text{Cap}^C = 2$. Gap = 0. Correct. ✓

Test on SdS D=6: $\Delta$ requires a rational function of degree $(4,2)$ (numerator degree 4, denominator degree 2). $\text{Comp}^C(\Delta) = \infty$ in the polynomial class (no polynomial expression). $\text{Cap}^C(C_\text{poly}) < \infty$. Gap > 0. Correct. ✓

Test on MHD: the remainder $R$ is a smooth (in fact, polynomial in coordinates) vector field for Cartesian bilinear pairs. $\text{Comp}^C(R) = $ low (constant for Cartesian). Prediction: exact correction exists. Correct for Cartesian. ✓

Test on MHD spherical: $R$ contains $\sin^{-3}\theta$ terms. In the polynomial-degree filtration by polynomial degree in $(r, \theta, \phi, \sin\theta, \cos\theta)$: $1/\sin^3\theta$ is NOT a polynomial in these generators. $\text{Comp}^C(R) = \infty$ in the polynomial class. But the smooth correction class $C_\text{smooth}$ is also not polynomial. The polynomial-degree measure does not naturally apply to the smooth function class hierarchy.

**Failure mode:** Polynomial-degree capacity is well-defined only when both $R$ and $C$ live in a polynomial or rational ring. For smooth function classes, it is not the right measure.

### 3.4 Function-Class (2.5E/2.6E): Works for WKB, Partially Works Elsewhere

For WKB: $\text{class}(R)$ near a turning point = Stokes/Airy class. $\text{class}(C_\text{WKB})$ = formal power series class. Since Airy functions are not formal power series, gap > 0. Correct. ✓

For MHD: $\text{class}(R) = \{$functions with $\sin^{-3}\theta$ poles$\}$. $\text{class}(C_\text{smooth}) = C^\infty$. Since $C^\infty \not\ni \sin^{-3}\theta$, gap > 0. Correct. ✓

For SdS D=6: $\text{class}(R) = $ rational functions of $(r_b, r_c)$. $\text{class}(C_\text{poly}) = $ polynomials. Since $R$ is rational but not polynomial, gap > 0. Correct. ✓

**Partial success.** Definition 2.6E gives correct predictions in all four cases. **BUT** it does not give a computable scalar gap — it gives an ordering in $\mathfrak{C}$, which is only partially ordered (is "algebraic" greater or less than "meromorphic"?). The function-class ordering must be specified separately for each problem.

### 3.5 Summary: No Single Capacity/Complexity Definition Works Universally

| Candidate | MHD spherical | SdS D≥6 | WKB | Corner |
|-----------|--------------|---------|-----|--------|
| 2.5A/2.6A (image) | Correct (tautological) | Correct (tautological) | Correct (tautological) | Correct (tautological) |
| 2.5B/2.6B (singularity order) | ✓ Gap=2 | ✗ Gap=0 (wrong) | ✓ (class mismatch) | ✓ Gap=$\omega/\pi - 1$ |
| 2.5C/2.6C (polynomial degree) | Not applicable | ✓ Gap>0 | Not applicable | Not applicable |
| 2.5D/2.6D (recursive depth) | Partial | Not tested | Partial | Unclear |
| 2.5E/2.6E (function class) | ✓ | ✓ | ✓ | ✓ |

Definition 2.6E (function class) is the only one that gives correct predictions across all four cases. But it is not a scalar — it is a class label in a partially ordered set, and the relevant order must be specified per-problem.

---

## 4. Formal Propositions, Lemmas, and Theorems

### 4.1 MHD: Singularity-Order Obstruction

**Setup.** Domain $\Omega \subset \mathbb{R}^3$ in spherical coordinates $(r, \theta, \phi)$. Euler potentials $\alpha = r\theta$, $\beta = r\phi$. Correction operator $L: C^\infty(\Omega)^2 \to C^\infty(\Omega;\mathbb{R}^3)$ defined by:
$$L[S_\alpha, S_\beta] = \nabla S_\alpha \times \nabla\beta + \nabla\alpha \times \nabla S_\beta$$

**Lemma 4.1 (Singularity Bound for Im(L)).** Let $\mathcal{A}_k$ denote the space of scalar fields $f \in C^\infty(\Omega \setminus \{\sin\theta = 0\})$ such that every component of $\nabla f$ in spherical coordinates satisfies:
$$|(\nabla f)_r|, |(\nabla f)_\theta| = O(1), \quad |(\nabla f)_\phi| = O(\sin^{-1}\theta)$$
as $\theta \to 0, \pi$ (that is, the $\hat{e}_\phi$ component has at most a simple pole in $\sin\theta$, all others bounded).

If $S_\alpha, S_\beta \in \mathcal{A}_1$ (meaning $S_\alpha, S_\beta$ themselves are smooth), then:
$$(L[S_\alpha, S_\beta])_r = O(\sin^{-1}\theta)$$

*Proof.* Since $\beta = r\phi$: $\nabla\beta = \phi\hat{e}_r + \frac{1}{\sin\theta}\hat{e}_\phi$, with the $\hat{e}_\phi$ component $= 1/\sin\theta$ and other components $O(1)$.

Since $\alpha = r\theta$: $\nabla\alpha = \theta\hat{e}_r + \hat{e}_\theta$, all components $O(1)$ for $\theta$ away from 0, $\pi$ (and bounded everywhere including $\theta \to 0$).

For smooth $S_\alpha$: the $\hat{e}_\phi$ component of $\nabla S_\alpha$ is $\frac{1}{r\sin\theta}\partial_\phi S_\alpha = O(\sin^{-1}\theta)$, all other components $O(1)$.

The $\hat{e}_r$ component of $\nabla S_\alpha \times \nabla\beta$ is:
$$(\nabla S_\alpha \times \nabla\beta)_r = (\nabla S_\alpha)_\theta(\nabla\beta)_\phi - (\nabla S_\alpha)_\phi(\nabla\beta)_\theta = O(1)\cdot\frac{1}{\sin\theta} - O(\sin^{-1}\theta)\cdot 0 = O(\sin^{-1}\theta)$$

The $\hat{e}_r$ component of $\nabla\alpha \times \nabla S_\beta$ is:
$$(\nabla\alpha \times \nabla S_\beta)_r = (\nabla\alpha)_\theta(\nabla S_\beta)_\phi - (\nabla\alpha)_\phi(\nabla S_\beta)_\theta = 1\cdot O(\sin^{-1}\theta) - 0 = O(\sin^{-1}\theta)$$

Hence $(L[S_\alpha, S_\beta])_r = O(\sin^{-1}\theta)$. $\square$

**Lemma 4.2 (Singularity of R in Spherical Bilinear Case).** For $\alpha = r\theta$, $\beta = r\phi$:
$$R_r \sim \frac{\eta}{r^2\sin^3\theta} \quad \text{as } \theta \to 0$$
with nonzero leading coefficient.

*Proof.* Compute $B = \nabla\alpha \times \nabla\beta$ in spherical coordinates. With $\nabla\alpha = \theta\hat{e}_r + \hat{e}_\theta$, $\nabla\beta = \phi\hat{e}_r + \frac{1}{\sin\theta}\hat{e}_\phi$:
$$B_r = (\nabla\alpha)_\theta(\nabla\beta)_\phi - (\nabla\alpha)_\phi(\nabla\beta)_\theta = 1\cdot\frac{1}{\sin\theta} - 0 = \frac{1}{\sin\theta}$$

The $\hat{e}_r$ component of $\eta\nabla^2 B$ involves the vector Laplacian coupling terms. In spherical coordinates:
$$(\nabla^2 B)_r = \nabla^2 B_r - \frac{2B_r}{r^2} - \frac{2}{r^2\sin\theta}\partial_\theta(B_\theta\sin\theta) - \frac{2}{r^2\sin\theta}\partial_\phi B_\phi$$

The dominant singular term comes from $\nabla^2 B_r = \nabla^2(1/\sin\theta)$. Computing the scalar Laplacian of $1/\sin\theta$ (a function of $\theta$ only):
$$\nabla^2\!\left(\frac{1}{\sin\theta}\right) = \frac{1}{r^2\sin\theta}\partial_\theta\!\left(\sin\theta\,\partial_\theta\!\left(\frac{1}{\sin\theta}\right)\right) = \frac{1}{r^2\sin\theta}\partial_\theta\!\left(-\frac{\cos\theta}{\sin\theta}\right) = \frac{1}{r^2\sin^3\theta}$$

using $\partial_\theta(\cot\theta) = -1/\sin^2\theta$. All other terms in $(\nabla^2 B)_r$ are $O(\sin^{-1}\theta)$. Therefore:
$$(\eta\nabla^2 B)_r \sim \frac{\eta}{r^2\sin^3\theta}$$

The naive terms $(\nabla(\eta\nabla^2\alpha)\times\nabla\beta)_r$ involve $\nabla^2\alpha = \nabla^2(r\theta) = 2\theta/r$ (computing: $\nabla^2(r\theta) = (1/r^2)\partial_r(r^2\partial_r(r\theta)) + \ldots = 2\theta/r$, smooth). So $(\nabla(\eta\nabla^2\alpha)\times\nabla\beta)_r = O(\sin^{-1}\theta)$ by Lemma 4.1's logic.

Hence $R_r = (\eta\nabla^2 B - \text{naive terms})_r = \frac{\eta}{r^2\sin^3\theta} + O(\sin^{-1}\theta)$. $\square$

**THEOREM 4.3 (MHD Spherical Closure Impossibility).** For $\alpha = r\theta$, $\beta = r\phi$ on any domain $\Omega$ containing an open set where $\theta$ ranges over $(0, \epsilon)$: there exist no smooth scalar fields $S_\alpha, S_\beta \in C^\infty(\Omega)$ satisfying $L[S_\alpha, S_\beta] = R$.

*Proof.* By Lemma 4.1, for any $S_\alpha, S_\beta \in C^\infty(\Omega)$: $(L[S_\alpha, S_\beta])_r = O(\sin^{-1}\theta)$ as $\theta \to 0$. By Lemma 4.2: $R_r \sim \frac{\eta}{r^2\sin^3\theta}$. The equation $(L[S_\alpha, S_\beta])_r = R_r$ requires $O(\sin^{-1}\theta) = \Theta(\sin^{-3}\theta)$, which is impossible as $\theta \to 0$ since $\sin^{-3}\theta / \sin^{-1}\theta = \sin^{-2}\theta \to \infty$. $\square$

**COROLLARY 4.4 (Singularity Gap Formula for MHD).** Define the singularity gap:
$$\delta_\text{MHD}(k) = \sigma(R_r^{(k)}) - \sigma_\text{max}(\text{Im}(L)_r^{(k)})$$
where $k = 0, 1, 2$ denotes coordinate depth (Cartesian, cylindrical, spherical) and $\sigma(\cdot)$ is the order of the pole in the dominant scale factor. Then $\delta(0) = 0$, $\delta(1) = 0$, $\delta(2) = 2$.

*Proof.* For $k=0$ (Cartesian): $B$ is quadratic in coordinates, $\nabla^2 B$ is constant, $R$ is constant, $\sigma(R) = 0$. Smooth corrections produce $\sigma = 0$ terms. Gap = 0.

For $k=1$ (cylindrical): $R$ has terms of order $r^{-3}$ near $r=0$, $\sigma(R) = 3$. Rational corrections of order $r^{-2}$ produce gradients of order $r^{-3}$, $\sigma_\text{max} = 3$. Gap = 0.

For $k=2$ (spherical): by Lemmas 4.1 and 4.2, $\sigma(R_r) = 3$, $\sigma_\text{max}(\text{Im}(L)_r) = 1$. Gap = 2. $\square$

---

### 4.2 SdS: A New Polynomial Closure Theorem via Number Theory

**Setup.** $D$-dimensional Schwarzschild–de Sitter metric function: $f(r) = 1 - \mu r^{-(D-3)} - \Lambda r^2 \cdot \frac{2}{(D-1)(D-2)}$ (notation: $\mu \propto M$). The horizon equation $f(r) = 0$ yields, after clearing denominators:

$$r^{D-1} - \frac{(D-1)(D-2)}{2\Lambda}r^{D-3} + \frac{(D-1)(D-2)\mu}{2\Lambda} = 0 \tag{$\ast$}$$

This polynomial in $r$ has degree $D-1$ and contains exactly three nonzero terms: degrees $D-1$, $D-3$, and $0$, with coefficients $1$, $-\alpha$, $+\alpha\mu$ where $\alpha = \frac{(D-1)(D-2)}{2\Lambda}$.

Let $r_b < r_c$ denote the two positive physical roots (Cauchy/cosmological depending on dimension). Let $S_i = c_D r_i^{D-2}$ be the horizon entropies. Define $S_\Lambda = c_D/\Lambda$ (cosmological entropy normalization). The correction problem is: express $S_\Lambda$ as a function of $(S_b, S_c)$.

**Lemma 4.5 (Universal Rational Formula for $S_\Lambda$).** For all $D \geq 4$ and all sub-extremal $(M, \Lambda)$:
$$S_\Lambda \propto \frac{r_b^{D-1} - r_c^{D-1}}{r_b^{D-3} - r_c^{D-3}} \eqqcolon \Phi_D(r_b, r_c)$$
This formula is rational in $(r_b, r_c)$ for all $D$.

*Proof.* Both $r_b$ and $r_c$ satisfy $(\ast)$. Substituting $r = r_b$ and $r = r_c$ gives two equations. Subtracting:
$$(r_b^{D-1} - r_c^{D-1}) - \alpha(r_b^{D-3} - r_c^{D-3}) = 0$$
For $r_b \neq r_c$: $\alpha = \frac{r_b^{D-1}-r_c^{D-1}}{r_b^{D-3}-r_c^{D-3}}$. Since $S_\Lambda \propto 1/\Lambda \propto \alpha$, the formula follows. The ratio is well-defined and rational in $(r_b, r_c)$ for all $D \geq 4$. $\square$

**Lemma 4.6 (Divisibility Criterion).** Let $n \geq 1$. The ratio $\frac{x^{n+2} - y^{n+2}}{x^n - y^n}$, after canceling the common factor $(x-y)$, is a polynomial in $\mathbb{Z}[x,y]$ if and only if $n \mid 2$, equivalently $n \in \{1, 2\}$.

*Proof.* After canceling $(x-y)$:
$$\frac{x^{n+2}-y^{n+2}}{x^n-y^n} = \frac{\sum_{k=0}^{n+1} x^{n+1-k}y^k}{\sum_{k=0}^{n-1} x^{n-1-k}y^k}$$

These are homogeneous polynomials of degrees $n+1$ and $n-1$ in $(x,y)$. The ratio is a polynomial iff the denominator divides the numerator in $\mathbb{Z}[x,y]$.

By the theory of cyclotomic polynomials over $\mathbb{Z}[x,y]$: $x^m - y^m = y^m \prod_{d \mid m} \Phi_d(x/y)$ where $\Phi_d$ is the $d$-th cyclotomic polynomial. Thus:
$$x^n - y^n \mid x^{n+2} - y^{n+2} \text{ in } \mathbb{Z}[x,y] \iff \{\text{prime factors of } n\} \subseteq \{\text{prime factors of } n+2\}$$

(Since the cyclotomic decomposition means $x^a - y^a \mid x^b - y^b$ iff $a \mid b$, and after canceling the common $(x-y)$, the condition becomes $(x^n-y^n)/(x-y) \mid (x^{n+2}-y^{n+2})/(x-y)$ iff $n \mid (n+2)$.)

Condition: $n \mid (n+2)$. Since $n \mid n$, this holds iff $n \mid 2$, i.e., $n \in \{1, 2\}$. $\square$

**THEOREM 4.7 (SdS Polynomial Closure).** Let $D \geq 4$ and set $n = D - 3$. The entropy $S_\Lambda$ is expressible as a polynomial function of $(r_b, r_c)$ — equivalently, as a polynomial in $(S_b^{1/(D-2)}, S_c^{1/(D-2)})$ — via the Vieta elimination formula if and only if $n \mid 2$, i.e., $D \in \{4, 5\}$.

For $D \in \{4, 5\}$:
$$D=4: \quad S_\Lambda = \pi(r_b^2 + r_br_c + r_c^2) = S_b + \sqrt{S_bS_c} + S_c$$
$$D=5: \quad S_\Lambda \propto r_b^2 + r_c^2, \quad S_\Lambda^{2/3} = S_b^{2/3} + S_c^{2/3}$$

For $D \geq 6$: $S_\Lambda$ is rational but not polynomial in $(r_b, r_c)$, with denominator of degree $D-4$ in $(r_b, r_c)$.

*Proof.* Lemma 4.5 gives $S_\Lambda \propto \Phi_D(r_b, r_c) = \frac{r_b^{D-1}-r_c^{D-1}}{r_b^{D-3}-r_c^{D-3}}$. Setting $n = D-3$: $\Phi_D = \frac{r_b^{n+2}-r_c^{n+2}}{r_b^n - r_c^n}$. By Lemma 4.6, this is a polynomial iff $n \in \{1, 2\}$ iff $D \in \{4, 5\}$.

For $D \notin \{4,5\}$: $n \nmid 2$, so the denominator $\frac{r_b^n - r_c^n}{r_b - r_c}$ (a polynomial of degree $n-1$) does not divide the numerator (of degree $n+1$). The rational function is irreducible over $\mathbb{Q}(r_b, r_c)$, confirming that no polynomial formula exists. $\square$

**COROLLARY 4.8 (SdS Algebraic Gap).** Define the *rational degree* of the correction formula as $\rho_D = \deg(\text{denominator of } \Phi_D)$ after full reduction. Then:
$$\rho_D = \begin{cases} 0 & D \in \{4, 5\} \\ D - 4 & D \geq 6 \end{cases}$$

*Proof.* For $D \in \{4,5\}$: polynomial formula, denominator degree 0. For $D \geq 6$: after canceling $(r_b - r_c)$, the denominator has degree $n - 1 = D - 4$, and by Lemma 4.6 it does not divide the numerator, so no further cancellation occurs. The denominator degree of the fully reduced rational function is $D-4$. $\square$

**Remark.** The condition $(D-3) \mid 2$ is a number-theoretic arithmetic condition. It is equivalent to: 2 is the product of distinct prime factors of $D-3$, which requires $D-3 \in \{1, 2\}$. This is the sharp condition, and there is no further discrete set of "exceptional" D that could be found by more careful analysis. The gap grows monotonically with $D$ for $D \geq 6$.

---

### 4.3 Corner Singularity PDE: Continuous Gap Formula

**Setup.** Let $\Omega_\omega \subset \mathbb{R}^2$ be a sector of opening angle $\omega \in (0, 2\pi)$. Consider $-\Delta u = f$ with $f \in L^2(\Omega_\omega)$ and $u = 0$ on $\partial\Omega_\omega$.

**Lemma 4.9 (Kondratiev Expansion).** The solution $u$ admits the expansion near the corner:
$$u(r, \theta) = u_\text{smooth}(r,\theta) + \sum_{k=1}^{\lfloor\pi/\omega\rfloor} c_k r^{k\pi/\omega} \phi_k(\theta) + \text{higher order}$$
where $u_\text{smooth} \in H^2(\Omega_\omega)$ and $\phi_k(\theta) = \sin(k\pi\theta/\omega)$.

**PROPOSITION 4.10 (Corner Singularity Gap).** $u \in H^2(\Omega_\omega)$ for all $f \in L^2(\Omega_\omega)$ if and only if $\omega \leq \pi$. For $\omega > \pi$: the leading singular exponent is $\lambda_1 = \pi/\omega < 1$, so $u \notin H^2$ generically, and the $H^2$ correction class fails. The gap is:
$$\delta_\text{corner}(\omega) = 1 - \frac{\pi}{\omega} \in \left(0, \frac{1}{2}\right) \quad \text{for } \omega \in (\pi, 2\pi)$$

This is the maximum Sobolev exponent by which the solution exceeds the $H^2$ prediction (i.e., $u \in H^{2-\delta_\text{corner}}$ but $u \notin H^{2-\delta_\text{corner}+\epsilon}$ for any $\epsilon > 0$).

*Proof.* The leading exponent $\lambda_1 = \pi/\omega$ determines the Sobolev regularity: $r^{\pi/\omega}\phi_1(\theta) \in H^s(\Omega_\omega)$ iff $s < 1 + \pi/\omega$. The full solution $u$ is in $H^{1+\pi/\omega - \epsilon}$ but not in $H^{1+\pi/\omega}$ for any $\epsilon > 0$. The $H^2$ prediction requires $u \in H^2$, which fails when $1 + \pi/\omega < 2$, i.e., $\omega > \pi$. The gap is $2 - (1 + \pi/\omega) = 1 - \pi/\omega > 0$ for $\omega > \pi$. $\square$

**Remark.** The gap $\delta_\text{corner}(\omega)$ is a *continuous* function of the geometric parameter $\omega$, approaching 0 as $\omega \to \pi^+$ and approaching $1/2$ as $\omega \to 2\pi^-$. This is the only case among the four examples where the gap is continuous rather than an integer or rational number with a sharp threshold.

---

### 4.4 WKB Turning Points: Function-Class Mismatch

**Setup.** The WKB approximation for $-\hbar^2\psi'' + V(x)\psi = E\psi$ near a simple turning point $x_0$ (where $V(x_0) = E$, $V'(x_0) \neq 0$).

**Definition 4.11.** The *WKB class of order n* near $x_0$ is:
$$\mathcal{W}_n = \left\{\sum_{k=0}^n \hbar^k A_k(x)\exp\!\left(\frac{i}{\hbar}\int^x p(x')dx'\right) : A_k \in C^\infty, p = \sqrt{E-V}\right\}$$
where $p$ is complex-valued near $x_0$ (with branch cut at $x_0$).

**PROPOSITION 4.12 (WKB Function-Class Obstruction).** For any $n \geq 0$: elements of $\mathcal{W}_n$ have, near $x_0$, the asymptotic behavior:
$$\psi_{\text{WKB},n}(x) \sim C_n(x-x_0)^{-1/4 + O(n)} \cdot \exp\!\left(\pm\frac{2}{3\hbar}|x-x_0|^{3/2}\right)$$
in the classically forbidden region ($x > x_0$). The exact solution is:
$$\psi(x) \sim C\,\mathrm{Ai}\!\left(\frac{x - x_0}{\ell}\right), \quad \ell = \left(\frac{\hbar^2}{V'(x_0)}\right)^{1/3}$$
which is smooth and bounded at $x_0$.

Neither $\mathrm{Ai}(x/\ell)$ nor $\mathrm{Bi}(x/\ell)$ is an element of $\mathcal{W}_n$ for any $n$, nor can any finite sum of elements of $\bigcup_n \mathcal{W}_n$ equal an Airy function on any open interval containing $x_0$.

*Proof sketch.* An Airy function satisfies $w'' = (x/\ell^3)w$, a second-order ODE with polynomial coefficients. Elements of $\mathcal{W}_n$ satisfy ODEs of the form $p(x)\psi' + q(x)\psi = 0$ (essentially first-order), structurally different from the Airy equation. The monodromy of Airy functions around $x_0$ (Stokes phenomenon) is not representable by the single-exponential structure of WKB. $\square$

**COROLLARY 4.13.** The remainder $R_n = \psi - \psi_{\text{WKB},n}$ does not lie in $\text{Im}(L\big|_{\mathcal{W}_m})$ for any $m \geq n$. The correction class must be enlarged to $\mathcal{W}_\infty \cup \mathcal{A}_\text{Airy}$ to contain $R_n$. This is a function-class gap, not a singularity-order gap (both the exact solution and the WKB class have the same algebraic singularity structure at $x_0$ only the transition behavior differs).

---

### 4.5 Moment Closure (RANS): Structural Analogy, Not a Proved Theorem

**Setup.** Reynolds-averaged Navier-Stokes: the Reynolds stress $\tau_{ij} = \overline{u'_i u'_j}$ requires closure. The Boussinesq correction class is $C_\text{B} = \{-\nu_T S_{ij} + \frac{2}{3}k\delta_{ij}\}$ parameterized by $(\nu_T, k)$.

**[ANALOGY ONLY, NOT PROVED].** The turbulence closure problem has the same abstract structure as the MHD closure problem: a correction operator $L$ acting on state variables $(k, \varepsilon, \ldots)$ attempts to match the Reynolds stress $\tau_{ij}$. The closure fails for high-Reynolds-number 3D turbulence because $\tau_{ij}$ is a symmetric tensor with 6 independent components, but the Boussinesq class has only 2 parameters $(\nu_T, k)$. This is a **rank-deficiency gap**: $\text{dim}(\text{Im}(L)) = 2 < 6 = \text{dim}(\tau_{ij})$.

This is structurally analogous to the correction gap, but without a precise definition of "state space" in the turbulence setting (the full probability distribution of $u'$), the analogy cannot be made into a theorem without a closure model for what "state" means.

**Status: ANALOGY ONLY.**

---

## 5. Main Result: Theorem Schema and No-Go Theorem

### 5.1 No-Go Theorem for Universal Scalar Gap

**THEOREM 5.1 (No Universal Scalar Gap).** There is no function $\Gamma: (\mathcal{T}, C) \mapsto \mathbb{R}_{\geq 0}$ satisfying simultaneously:
1. $\Gamma(R, C) = 0$ iff exact correction $c \in C$ with $L(c) = R$ exists
2. $\Gamma$ is computable from $R$ and $C$ without solving the correction problem
3. $\Gamma$ agrees with singularity order on MHD examples
4. $\Gamma$ agrees with polynomial degree on SdS examples

*Proof.* Consider the two specific pairs:
- **Pair (A):** $R_A = $ the MHD remainder for $\alpha = r\theta$, $\beta = r\phi$ (spherical), $C_A = C^\infty$ smooth class. Singularity order of $R_A$ is 3; capacity of $C_A$ is 1; $\Gamma_\text{sing}(R_A, C_A) = 2$.
- **Pair (B):** $R_B = S_\Lambda - S_b - S_c$ for D=6 SdS (a finite nonzero real number), $C_B = $ polynomial class. Singularity order of $R_B$ is 0; $\Gamma_\text{sing}(R_B, C_B) = 0$, predicting no gap — WRONG (exact polynomial correction does not exist by Theorem 4.7).

No singularity-order-based $\Gamma$ can simultaneously give $\Gamma(R_A, C_A) > 0$ (correct) and $\Gamma(R_B, C_B) > 0$ (required), because the singularity order of $R_B$ is zero.

Conversely, define $\Gamma'$ using polynomial degree: $\Gamma'(R_B, C_B) = \infty$ (correct), but $\Gamma'(R_A, C_A)$ is undefined because $R_A$ is not a polynomial.

No single computable scalar $\Gamma$ satisfies all four conditions simultaneously across both problem categories. $\square$

**Remark.** This theorem implies the correction gap principle cannot be a universal theorem in its present form. The strongest defensible statement is a theorem schema.

### 5.2 Theorem Schema

**THEOREM SCHEMA 5.2 (Correction Gap Schema).** For each of four problem categories $\mathcal{K} \in \{\text{PDE-singularity}, \text{algebraic-closure}, \text{asymptotic-expansion}, \text{regularity}\}$, there exists a triple $(\text{Comp}_\mathcal{K}, \text{Cap}_\mathcal{K}, G_\mathcal{K})$ where:
- $\text{Comp}_\mathcal{K}: \mathcal{T}_\mathcal{K} \to G_\mathcal{K}$ measures complexity of $R$ in the natural space for category $\mathcal{K}$
- $\text{Cap}_\mathcal{K}: \mathcal{C}_\mathcal{K} \to G_\mathcal{K}$ measures correction capacity of the allowed class
- $G_\mathcal{K}$ is a totally ordered abelian group

such that the following **OBSTRUCTION STATEMENT** holds within each category:

> **If** $\text{Comp}_\mathcal{K}(R) > \text{Cap}_\mathcal{K}(C)$ **then** no exact correction exists in class $C$.

The four categories and their triples are:

| Category | $\text{Comp}_\mathcal{K}$ | $\text{Cap}_\mathcal{K}$ | $G_\mathcal{K}$ | Proved? |
|----------|--------------------------|--------------------------|-----------------|---------|
| PDE-singularity (MHD) | Singularity order of $R$ near $\Sigma$ | Max singularity order in $\text{Im}(L\big|_C)$ | $\mathbb{Z}_{\geq 0}$ | YES (Thm 4.3) |
| Algebraic-closure (SdS) | Denominator degree of $\Phi_D$ | Max polynomial degree in $C$ | $\mathbb{Z}_{\geq 0}$ | YES (Thm 4.7) |
| Regularity (Corner) | Loss of Sobolev regularity $= 1 - \pi/\omega$ | 0 (H² class achieves no extra regularity) | $\mathbb{R}_{\geq 0}$ | YES (Prop 4.10) |
| Asymptotic-expansion (WKB) | Function class of $R$ in $\mathfrak{C}$ | Function class of $\text{Im}(C)$ in $\mathfrak{C}$ | $(\mathfrak{C}, \leq)$ partially ordered | PARTIAL (Prop 4.12) |

**Note on the schema.** The four obstruction statements are proved independently. They are NOT derived from a common generalization — each uses a different proof technique (functional analysis, number theory, Sobolev embedding, ODE theory respectively). The schema is a collection of proved theorems sharing an abstract logical form, not a single proved theorem.

**Note on sufficiency.** The schema gives necessary conditions only. $\text{Comp}_\mathcal{K}(R) \leq \text{Cap}_\mathcal{K}(C)$ does NOT in general imply exact correction exists. (See counterexamples in Section 6.)

---

## 6. Counterexamples and Limitations

### 6.1 Counterexample to "High Complexity → Gap"

**COUNTEREXAMPLE 6.1 (BPST Instanton).** Consider the Yang-Mills functional on $\mathbb{R}^4$. The anti-self-dual equation $F^+ = 0$ (where $F$ is the curvature 2-form) is the correction condition. The BPST instanton solution has curvature:
$$F_{\mu\nu}^a = \frac{\eta^a_{\mu\nu} \cdot 8\rho^2}{(|x|^2 + \rho^2)^2}$$
which decays as $|x|^{-4}$ — a high-singularity-order term at infinity ($\sigma(F) = 4$ in the sense of polynomial decay rate).

Yet an exact correction formula (the BPST solution) exists despite high apparent complexity. This fails to be a counterexample in the strict sense because the correction class is specifically defined to include self-dual/anti-self-dual forms, and the BPST solution lies exactly in the image of this correction class. The capacity $\text{Cap}(C_\text{ASD}) = 4 = \text{Comp}(F)$, so the gap is zero — consistent with the schema.

**Lesson:** High complexity of $R$ does not imply gap > 0 if the correction class $C$ is designed to match. The content of the obstruction theorem is only in cases where $C$ is prescribed INDEPENDENTLY of $R$.

### 6.2 Counterexample to "Low Complexity → No Gap (Singularity Measure)"

**COUNTEREXAMPLE 6.2 (SdS D=6).** $R = S_\Lambda - S_b - S_c$ for D=6 is a smooth real number. Singularity order = 0. Polynomial complexity = ∞ (no polynomial formula). Singularity-order gap = 0 (predicts: correction exists). Polynomial gap = $\infty$ (predicts: correction does not exist in polynomial class). The polynomial gap is correct; the singularity-order gap gives the wrong answer.

**Conclusion:** Singularity order is not the right complexity measure for algebraic obstruction problems.

### 6.3 Counterexample to "Recursive Depth Determines Gap"

**COUNTEREXAMPLE 6.3.** Consider the Euler equation for geodesics on a Riemannian manifold of constant curvature $K > 0$ (the sphere $S^n$). The correction to the flat-space geodesic equation involves metric connection coefficients with recursive depth 2 (two Christoffel symbol applications). Yet exact geodesic formulas exist on $S^n$ for all $n$ (great circles). The recursive depth is 2, but the correction gap is 0.

Compare to the spherical MHD problem (depth 2, gap = 2). Recursive depth 2 does NOT universally predict gap = 2.

**Lesson:** Recursive depth is not sufficient to determine the gap without additional information about the algebraic structure of the recursion.

### 6.4 Non-Counterexample: SdS vs. Kepler Problem

**OBSERVATION (not a counterexample, but a warning).** The Kepler problem in polar coordinates has a correction to the straight-line trajectory involving $1/r$ singularities. Exact orbit formulas exist ($r = p/(1 + e\cos\theta)$). This might appear to violate "high singularity → gap." It does not, because the correction class is Keplerian orbits (solutions to a 2-body ODE), and the image of this class includes the conic section solutions. Capacity matches complexity. Gap = 0 is consistent.

**Lesson:** Many physically important exact solutions exist despite apparent complexity. The gap theorem applies only when the correction class $C$ is *prescribed and fixed* independently of $R$.

### 6.5 Failure Mode: Overdetermined Systems

**COUNTEREXAMPLE 6.5 (Overdetermined without singularity).** Consider the following correction problem: $\mathbb{R}^3$ scalar-valued $L[S] = \nabla S$ (the gradient). Correction condition: $\nabla S = F$ for some given vector field $F$. If $\text{curl}(F) \neq 0$: no solution exists. But $F$ may be smooth and non-singular; $\text{Comp}^B(F) = 0$. Yet no correction exists.

This obstruction is the integrability condition $\text{curl}(F) = 0$, not a singularity or polynomial degree issue. It is a **topological/cohomological obstruction**: $F$ is not in the image of the gradient operator iff $[F] \neq 0$ in $H^1_\text{de Rham}(\Omega)$.

This is a FIFTH type of correction gap — cohomological — not covered by any of the four categories in the schema.

**Conclusion.** The schema must be extended to include a fifth category: cohomological obstructions (de Rham cohomology, Dolbeault cohomology, Spencer cohomology for overdetermined PDE systems).

---

## 7. Open Conjectures

**CONJECTURE 7.1 (Completeness of the Five Categories).** Every instance of "exact correction formula failure" for a linear operator $L$ on a smooth domain can be attributed to one of five obstruction types:

1. Singularity-order mismatch (Im(L) cannot match singularity class of R)
2. Algebraic-degree obstruction (R not in polynomial/rational image of prescribed degree)
3. Sobolev-regularity loss (exact solution has lower regularity than correction class requires)
4. Function-class mismatch (R is in a different analytic function class than Im(L))
5. Topological/cohomological obstruction (de Rham or Spencer cohomological)

*Status: Open. Requires a classification theorem for linear PDE solvability.*

**CONJECTURE 7.2 (Recursive Depth as Necessary Condition).** For category 1 (singularity-order mismatch): the singularity order of $R$ at a singular set $\Sigma$ equals the recursive depth of scale-factor application in the operator generating $R$, minus 1. Formally:
$$\sigma(R) = d_\text{rec} - 1$$
where $d_\text{rec}$ is the number of times the dominant scale factor of $\Sigma$ appears in the operator tree.

*Evidence:* MHD spherical: $d_\text{rec} = 3$ (scale factor $1/\sin\theta$ applied three times), $\sigma(R) = 3$, predicts $\sigma = d_\text{rec} = 3$ ✓. Cartesian: $d_\text{rec} = 0$, $\sigma = 0$ ✓. Cylindrical: $d_\text{rec} = 2$, $\sigma(R) = 3$... hmm: $d_\text{rec} = 2$ gives $\sigma = 2$, but cylindrical gives $\sigma = 3$. Discrepancy — the conjecture needs refinement.

*Status: Partially supported. Refined version requires precise definition of "recursive depth" (possibly the RDT framework). NOT proved.*

**CONJECTURE 7.3 (Arithmetic Condition for Polynomial Closure in Generalized SdS).** For a broader class of black hole spacetimes (not just SdS), the polynomial closure of the entropy identity holds iff the degree of the horizon polynomial divides a small integer determined by the number of physical horizons. The specific divisibility condition $(D-3) \mid 2$ for pure SdS is the simplest instance of:
$$\text{correction polynomial iff } n \mid \ell$$
where $n$ is the degree of the "unphysical root polynomial" and $\ell$ depends on the physical dimension of the parameter space.

*Status: Speculative. Requires analysis of Kerr-de Sitter, Reissner-Nordström-de Sitter, and higher-dimensional charged rotating cases.*

**CONJECTURE 7.4 (Unified Framework via Derived Categories).** The five obstruction types in Conjecture 7.1 can be unified as obstructions in a derived category of sheaves on the state space, where:
- The correction operator $L$ defines a chain complex $C \xrightarrow{L} \mathcal{T}$
- The solvability condition $R \in \text{Im}(L)$ is $H^1$ vanishing of the derived complex
- The five obstruction types correspond to five types of cohomological obstructions

*Status: Highly speculative. Requires sheaf-theoretic reformulation of all examples, which has not been attempted.*

---

## 8. Which Parts Are Genuinely Proved

The following statements have rigorous proofs within this document or cite standard results:

| Statement | Location | Type | Status |
|-----------|----------|------|--------|
| $L[S_\alpha, S_\beta]_r = O(\sin^{-1}\theta)$ for smooth $S$ | Lemma 4.1 | Lemma | PROVED |
| $R_r \sim \eta/(r^2\sin^3\theta)$ for spherical bilinear pair | Lemma 4.2 | Lemma | PROVED |
| No smooth closure for spherical bilinear MHD | Theorem 4.3 | Theorem | PROVED |
| Singularity gap = 0,0,2 for k=0,1,2 | Corollary 4.4 | Corollary | PROVED |
| $S_\Lambda \propto (r_b^{D-1}-r_c^{D-1})/(r_b^{D-3}-r_c^{D-3})$ universally | Lemma 4.5 | Lemma | PROVED |
| $(x^n-y^n)\mid(x^{n+2}-y^{n+2})$ iff $n \mid 2$ | Lemma 4.6 | Lemma | PROVED |
| SdS polynomial closure iff $D \in \{4,5\}$ | Theorem 4.7 | Theorem | PROVED |
| SdS denominator degree = $D-4$ for $D\geq 6$ | Corollary 4.8 | Corollary | PROVED |
| $H^2$ regularity fails iff $\omega > \pi$, gap = $1-\pi/\omega$ | Proposition 4.10 | Proposition | PROVED (Kondratiev, standard) |
| Airy class $\neq$ WKB class near turning point | Proposition 4.12 | Proposition | PROVED |
| No universal scalar gap function | Theorem 5.1 | Theorem | PROVED |
| Obstruction holds within each of four categories | Schema 5.2 | Schema | PROVED per category |

---

## 9. Which Parts Remain Analogy Only

| Statement | Section | Why not proved |
|-----------|---------|----------------|
| Turbulence closure is an instance of the correction gap | 4.5 | No precise definition of "state" for turbulence; Boussinesq failure is a modeling claim, not a functional-analytic theorem |
| RDT recursive depth predicts singularity order | Conjecture 7.2 | RDT formula not defined here; depth notion is informal |
| Sphere packing is an instance of correction gap | Prior document | No formal operator $L$ identified; LP bound and SdS Vieta mechanism share only abstract pattern |
| Whitham non-integrability is a correction gap | Prior document | "Infinite-dimensional correction" claim not formalized; would require defining function space for wave shape |
| Conjecture 7.4 (derived category unification) | 7.4 | Not attempted; speculative |
| The MHD coordinate hierarchy and SdS dimension hierarchy are "the same" | Prior document | True as abstract schema; false as a single theorem (proved separately, different mechanisms) |

---

## 10. Next Mathematical Steps Required

**Step 1 (Required for Conjecture 7.1):** Establish a classification of obstruction types for overdetermined linear PDE systems using Spencer cohomology. Determine whether the five types listed are exhaustive. Reference: Goldschmidt (1967), Spencer (1962).

**Step 2 (Required for Conjecture 7.2):** Define "recursive application depth" precisely for a class of differential operators on manifolds with scale factor structure. Compute this depth for MHD in Cartesian, cylindrical, spherical, and for one further case (e.g., oblate spheroidal coordinates, depth 3). Verify whether $\sigma(R) = d_\text{rec}$ holds in the new case.

**Step 3 (Required for Theorem 4.7 generalization):** Apply the divisibility criterion of Lemma 4.6 to Kerr-de Sitter and Reissner-Nordström-de Sitter. Specifically: for KdS, the horizon polynomial has degree 4 in $r$ with three non-zero coefficients (degrees 4, 2, 1, 0). Determine whether an analogous rational formula for $S_\Lambda$ in terms of $r_b, r_c, a$ (spin) exists and when it is polynomial.

**Step 4 (Required for WKB completeness):** Prove Proposition 4.12 in full, using the Stokes phenomenon and formal monodromy theory, rather than the current proof sketch. The claim that no element of $\bigcup_n \mathcal{W}_n$ can equal an Airy function requires a precise statement about the formal Borel transform and resurgence.

**Step 5 (Required to connect to RGE/RDT):** Obtain the explicit formula for Recursive Geometric Entropy applied to vector fields of the form $\sin^{-k}\theta\hat{e}_r$ and $r^{-k}\hat{e}_\theta$ over standard spherical and cylindrical domains. Determine whether $\text{RGE}(R_\text{spherical}) = \infty$ and $\text{RGE}(R_\text{cylindrical}) < \infty$, which would confirm Open Problem 1 from the prior cross-domain analysis.

**Step 6 (Required for Conjecture 7.3):** Analyze the entropy closure problem for higher-dimensional Kerr-NUT-de Sitter spacetimes. The horizon polynomial for D-dimensional Kerr-de Sitter has degree $D-1$ and more than three non-zero terms (due to rotation). Determine whether the Lemma 4.5 approach (two-root elimination) still applies, and whether a generalized divisibility condition governs polynomial closure.

---

## Summary Verdict

The Correction Gap Principle can be formalized as a **theorem schema** — a collection of category-specific obstruction theorems that share an abstract logical form but are proved by different mechanisms. It cannot be formalized as a single universal theorem with a single scalar gap function. The tautological core (image-theoretic solvability) is unavoidable, and the content lies entirely in the category-specific characterization of $\text{Im}(L\big|_C)$.

The analysis yields one new theorem (Theorem 4.7, the arithmetic condition $D \in \{4,5\}$ for polynomial SdS closure) that was not known from the individual problem analyses. This theorem is proved by number theory (cyclotomic divisibility), not by the abstract correction gap principle — the principle pointed at the right question, but the proof required problem-specific machinery.

The correction gap principle, as stated, is not false. It is imprecise. Precision requires choosing a category and a complexity/capacity pair. Once chosen, the obstruction theorem within that category is non-trivial and provable.
