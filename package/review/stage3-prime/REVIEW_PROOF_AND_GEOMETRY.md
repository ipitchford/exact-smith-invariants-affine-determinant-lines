# Stage 3-prime proof and geometry review

**Manuscript:** *Exact Smith Invariants and Affine Determinant Lines of
Binary-Form Factorisation*  
**Review remit:** Theorems 6.1, 7.1, 7.3, 7.4, and 8.1; Corollaries 6.2,
7.2, and 7.5; the local-to-global Smith passage; the residual diagonalizable
group; and the finite-locally-free normalised factorisation cover  
**Recommendation:** **Minor Revision**  
**Mathematical-core verdict:** **verified in this internal read-only review; no
critical or major mathematical defect found**

## 1. Assurance boundary

This is a supporting internal Stage-3-prime referee pass. I reconstructed the
module, valuation, tree-minor, group-scheme, and torsor arguments directly from
the revised manuscript. I also ran a fresh read-only exact counterexample hunt.
The computation is regression evidence only: it is not a proof, external
specialist reproduction, second-software validation, formal verification,
priority resolution, or external peer review.

The recommendation is conditional on the hypotheses actually stated in the
paper: \(k\geq3\) for the Smith package, positive integral degrees, primitive

\[
 \mathbf e=\mathbf d/\gcd(d_1,\ldots,d_k)
\]

for the local theorem, and the previously proved character-minor formula in
Theorem 6.1/Corollary 6.2 for the tree-gcd result. Theorem 8.1 separately assumes
an algebraically closed field, labelled factor degrees, and a square full-rank
semi-invariant character matrix.

## 2. Severity-ranked findings

### Critical findings

None.

### Major findings

None.

### Minor finding M1 — \(g\) and \(h(\mathbf e)\) are used before they are defined

**Location:** Abstract, Chinese abstract, and Introduction, especially the
displayed Smith forms before Section 7.1.

The revised front matter writes

\[
 \operatorname{diag}(g,\ldots,g,g h(\mathbf e))
\]

without explicitly saying there that \(g=\gcd(d_1,\ldots,d_k)\), that
\(\mathbf e=\mathbf d/g\) is primitive, or that \(h(\mathbf e)\) is the positive
gcd of the maximal character minors (equivalently \(|C_{\mathbf e}|\)). These
definitions do appear in Section 7, so this is not a mathematical ambiguity in
the proofs. It is nevertheless a residual traceability defect: the prior
adversarial audit specifically requested that \(h\) be defined before its first
use, while the response says all of that audit's minor clarifications were
incorporated.

**Required correction:** add one compact definition at the first displayed
Smith form, for example

\[
 g=\gcd_i d_i,\qquad \mathbf e=\mathbf d/g,\qquad
 h(\mathbf e)=\gcd_{|H|=k-1}|\det W_H(\mathbf e)|.
\]

It would also be useful to state that zeros do not affect this gcd and that
Section 7 proves it is positive.

### Minor finding M2 — make the local pivot explicit in Theorem 7.4's generator sentence

**Location:** Theorem 7.4, final sentence of the statement.

The proof correctly chooses a \(p\)-unit vertex \(a\), then uses the star centred
at \(a\) and one bent star for every unordered pair \(i,j\ne a\). The theorem
statement says only that “one star and \(\binom{k-1}{2}\) bent stars” generate
after localisation. This is true, but the precise family depends on the chosen
\(p\)-unit pivot.

**Suggested correction:** say “for any \(p\)-unit pivot \(a\), the star centred
at \(a\) and the associated \(\binom{k-1}{2}\) bent stars generate the local
maximal-minor ideal.” No proof change is needed.

### Minor finding M3 — justify the \(O(k^2)\) gcd-operation claim

**Location:** Theorem 7.3 and the Abstract.

The formula has \(O(k^2)\) pair factors, but computing each excluded-pair gcd
\(G_{ab}\) naively would take \(O(k)\) gcd operations and therefore \(O(k^3)\)
overall. The claimed \(O(k^2)\) bound is correct, but the implementation idea is
not stated.

**Suggested correction:** add that, for each fixed \(a\), prefix/suffix gcds of
the \(k-1\) remaining entries compute all \(G_{ab}\) in \(O(k)\) gcd operations.
Repeating over \(a\) gives \(O(k^2)\). This is an arithmetic-operation count, not
a unit-cost bit-complexity claim.

## 3. Reconstruction of the arithmetic proof

### 3.1 Theorem 6.1 and Corollary 6.2 — verified

Before the torus constraint is eliminated, the edge row for \(ij\) has
\(d_j\) in column \(i\) and \(d_i\) in column \(j\). Appending the all-ones row
and applying the stated unimodular column basis

\[
 e_1-e_k,\ldots,e_{k-1}-e_k,e_k
\]

produces an upper block-triangular matrix with \(W_H\) and final diagonal entry
one. Thus no hidden factor of \(k\) is introduced.

Multiplying column \(i\) by \(d_i\) converts every edge row, after extracting
\(d_id_j\), into the ordinary signless incidence row. The uncancelled identity
(6.1) is integral and handles an isolated tree vertex correctly. A signless
incidence component contributes:

- rank \(v-1\) for a tree or any connected bipartite component;
- absolute determinant two for an odd-unicyclic component; and
- zero for an even-unicyclic component.

Because \(H\) has \(k-1\) edges, full rank after one appended degree row requires
exactly one tree component and only odd-unicyclic remaining components. The
kernel vector of the tree incidence rows is the signed bipartition vector, so
the appended row contributes

\[
 \sum_{i\in P}d_i-\sum_{j\in Q}d_j.
\]

This gives Theorem 6.1 and its spanning-tree specialisation exactly as stated.

### 3.2 Theorem 7.1 — the Tietze elimination proves the module isomorphism

Write \(M=\mathbb Z^k/\mathbb Z\mathbf1\), with generators \(x_i\), ambient
relation \(\sum_i x_i=0\), and edge relations

\[
 q_{ij}=e_jx_i+e_ix_j.
\]

For every prime \(p\), primitivity supplies a pivot \(a\) for which \(e_a\) is a
unit in \(R_p=\mathbb Z_{(p)}\). Each star relation is then a valid presentation
elimination:

\[
 x_i=-\frac{e_i}{e_a}x_a\qquad(i\ne a).
\]

After these eliminations, the ambient relation has coefficient \(D_a/e_a\),
and a non-star edge \(ij\) has coefficient \(-2e_ie_j/e_a\). Multiplying by the
unit \(e_a\) gives precisely

\[
 C_{\mathbf e}\otimes R_p
 \cong R_p/(D_a,2e_ie_j:i<j,\ i,j\ne a).
\]

Every original generator and relation is accounted for. The calculation does
not merely match orders and does not divide by \(2\), \(D_a\), or a nonunit
degree. It remains valid at \(p=2\), for \(k=3\), and when \(D_a=0\). If two
pivots are admissible, the edge joining them identifies the two displayed
cyclic generators up to a unit, proving pivot independence.

### 3.3 Corollary 7.2 — Fitting ideals, zero conventions, and global cyclicity

The zeroth Fitting ideal of the cyclic local module is its annihilator
\(I_{p,a}\). Fitting ideals commute with localisation, and the global
presentation matrix is \(W_E^{\mathsf T}\), so its zeroth Fitting ideal is
generated by the maximal minors of \(W_E\). In the DVR \(R_p\), the generator
has the least of the displayed valuations. This proves

\[
 v_p(h)=\min\left(v_p(D_a),
   \min_{i<j,\ i,j\ne a}
   \{v_p(2)+v_p(e_i)+v_p(e_j)\}\right).
\]

The stated convention \(v_p(0)=\infty\) handles \(D_a=0\). The other
coefficients are nonzero because all degrees are positive and \(k\geq3\), so
the minimum is finite. Thus every primary localisation is cyclic. The module
has rank zero, and the direct sum of its cyclic primary components is cyclic
because their orders are pairwise coprime. Therefore

\[
 C_{\mathbf e}\cong\mathbb Z/h(\mathbf e)\mathbb Z.
\]

No computation is needed for this passage.

### 3.4 Theorem 7.3 — odd primes, \(p=2\), and the global product

For an odd prime, positivity of the local exponent forces exactly two unit
degrees \(e_a,e_b\), with \(e_a\equiv e_b\pmod p\). If

\[
 q=\min_{c\notin\{a,b\}}v_p(e_c),
\]

then \(D_a=(e_a-e_b)-\sum_c e_c\) and the second term has valuation at least
\(q\). Hence

\[
 \min(v_p(D_a),q)=\min(v_p(e_a-e_b),q),
\]

including the zero case. This is exactly \(v_p(Q_{ab})\).

At \(p=2\), with \(s\) odd degrees:

- odd \(s\) makes \(D_a\) odd;
- even \(s\geq4\) leaves two odd non-pivot degrees, producing valuation one;
- \(s=2\) gives the truncated minimum of \(v_2(D_a)\) and
  \(1+v_2(G_{ab})\).

The identity \(D_a+D_b=-2\sum_{c\notin\{a,b\}}e_c\) proves that the last
truncated value is independent of the odd pivot.

For odd primes, primitivity also implies that a prime dividing \(Q_{ab}\) cannot
divide either \(e_a\) or \(e_b\); consequently the unit pair is unique. Thus the
odd parts of distinct \(Q_{ab}\) are pairwise coprime, and the product in
Theorem 7.3 assembles the local valuations without double counting. The
standard convention \(\gcd(0,n)=n\) covers equal degree pairs; the excluded-pair
gcd is always positive because \(k\geq3\) and all degrees are positive.

### 3.5 Theorem 7.4 — tree minors generate the full local Fitting ideal

For a \(p\)-unit pivot \(a\), Corollary 6.2 gives the star determinant

\[
 \pm e_a^{k-2}D_a.
\]

The power of \(e_a\) is a local unit, so the tree-minor ideal contains \(D_a\).
Replacing edge \(aj\) by \(ij\), for \(i,j\ne a\), gives a bent star with
determinant

\[
 \pm e_a^{k-3}e_i(D_a+2e_j).
\]

After removing the unit power and subtracting \(e_iD_a\), the tree-minor ideal
contains \(2e_ie_j\). It therefore contains \(I_{p,a}\). The reverse inclusion
holds because every tree determinant is a maximal minor and the full
maximal-minor ideal is \(I_{p,a}\). Equality at every prime gives equality of
the positive global gcds. Odd-unicyclic bases may still have important
individual multiplicities; they simply do not reduce the full-list gcd.

### 3.6 Corollary 7.5 and the residual group scheme — verified

The primitive cokernel is cyclic of order \(h\), so the primitive Smith form is

\[
 \operatorname{diag}(1,\ldots,1,h).
\]

Since \(W_E(\mathbf d)=gW_E(\mathbf e)\), the same unimodular operations give

\[
 \operatorname{diag}(g,\ldots,g,gh),
\]

which already satisfies the divisibility chain. Consequently

\[
 D(X^*(T)/L)\cong\mu_g^{k-2}\times\mu_{gh}
\]

noncanonically, with finite locally free rank \(g^{k-1}h\). In characteristic
\(p\), the \(p\)-power factors are connected and the prime-to-\(p\) factors are
finite étale. The stated connected length, étale rank, geometric-point count,
and criterion \(p\nmid gh\) for étaleness follow directly.

The rectangular character map is also correctly scoped: the inclusion
\(L\hookrightarrow X^*(T)\) gives a finite free group-algebra inclusion with a
basis indexed by cosets. Its degree is the degree onto \(D(L)\), its
scheme-theoretic image, rather than a claim about the full ambient rectangular
torus or unlabelled root-partition branches.

## 4. Reconstruction of Theorem 8.1

### 4.1 Root-partition cover and common good open

Over the squarefree locus, a labelled projective factorisation is exactly a
partition of the \(D\) distinct roots into blocks of sizes \(d_i\). The resulting
cover has degree

\[
 \nu=\frac{D!}{\prod_i d_i!}
\]

and is finite étale, including in characteristics dividing \(\nu\): the relevant
constant symmetric-group action remains étale and free on the distinct-root
configuration space.

The affine frame space over this cover is a torsor under the product-one torus
\(T\). A semi-invariant principal ideal is \(T\)-stable and therefore descends
along the fpqc torsor. Because the squarefree source is dense and each \(g_a\)
is a nonzero polynomial, its descended zero locus is proper. The factorisation
cover is irreducible, so the finite image of that proper closed locus is a
proper closed subset of coefficient space. Removing the finitely many images
produces a common dense target open on which every \(g_a\) is nonzero on every
labelled branch.

### 4.2 Cartesian torsor diagram and finite local freeness

After base change by the torsor, the map

\[
 \theta=(q,g):P_0\longrightarrow Z_0\times(\mathbb G_m)^t
\]

becomes

\[
 \beta(x,\lambda)=\bigl(x,g(x)\chi_W(\lambda)\bigr).
\]

The square in (8.3) is Cartesian: two points over one projective
factorisation differ by a unique product-one scaling, and equivariance gives
\(g(\lambda x)=\chi_W(\lambda)g(x)\). Smith normal form changes source and target
torus coordinates by integral torus automorphisms and reduces \(\chi_W\) to the
coordinate power maps \(z_i\mapsto z_i^{s_i}\). Each is finite free of rank
\(s_i\) on coordinate rings. Hence \(\beta\), then \(\theta\) by fpqc descent,
is finite locally free of rank \(|\det W|\). Composition with the finite étale
root-partition cover proves rank

\[
 |\det W|\frac{D!}{\prod_i d_i!}.
\]

This is a scheme-length argument, not a point count. In characteristic \(p\),
writing \(s_i=p^{a_i}s_i'\) gives separable degree

\[
 \left(\prod_i s_i'\right)\nu,
\]

inseparable factor \(p^{\sum_i a_i}\), and the same formula for the number of
geometric points. Since the root-partition cover is étale, no additional
inseparable factor comes from a possible divisibility \(p\mid\nu\). Finally,
the bordered determinant formula shows that the restriction to \(X^\circ\) is
étale exactly when \(p\nmid\det W\).

I found no gap in the finite-locally-free descent or in the distinction among
total degree, separable degree, inseparable degree, and geometric-point count.

## 5. Examples and fresh falsification attempt

The displayed diagnostic examples agree with the theorems:

- \((1,1,9)\) has primitive Smith form \((1,9)\), retaining the full
  \(3\)-adic valuation;
- \((1,5,4)\) has Smith form \((1,8)\), exercising the higher two-adic branch;
- \((1,2,2)\) is saturated although its three square edge minors have absolute
  values \(3,2,2\); the displayed two nonnegative monomial rows multiply the
  complete character matrix to \(I_2\);
- \((1,1,1,1)\) has Smith form \((1,1,2)\), detecting the odd-cycle factor two;
- \((2,2,18)\) has Smith form \((2,18)\), correctly retaining nonprimitive
  content.

A fresh read-only checker reconstructed character rows from the eliminated
cocharacter basis rather than importing the project verifier. With seed
20260809, it found no discrepancy in:

- 720 random primitive Smith/global-index comparisons for \(3\leq k\leq8\)
  and entries up to 80;
- 18,536 admissible pivot/prime local-valuation comparisons; and
- 43,200 random \((k-1)\)-edge graph-minor comparisons against the full
  tree-plus-odd-unicyclic formula.

These finite checks support convention control only. The decision above rests
on the reconstructed proofs.

## 6. Decision recommendation

The required Stage-3 arithmetic and geometry repairs are substantively
successful. Theorems 7.1, 7.3, 7.4, and 8.1 and Corollaries 7.2 and 7.5 survive
this review, including the \(p=2\), \(D_a=0\), nonprimitive, bad-characteristic,
and finite-flat edge cases. The proof chain is strong enough for the internal
pipeline to move forward without another theorem-development cycle.

I recommend **Minor Revision**, limited to the three presentation corrections
in Section 2—most importantly defining \(g\), \(\mathbf e\), and \(h(\mathbf e)\)
before their first front-matter use. After those corrections, my proof-and-
geometry recommendation would be **Accept for the internal research-draft
pipeline**, while retaining every stated assurance limitation and the separate
submission metadata/licence blocker.
