# Response to the Stage 3 editorial decision and reviewers

## Revision identity and boundary

This response concerns the Stage-4 child manuscript
`manuscript-revised.md`, titled *Exact Smith Invariants and Affine
Determinant Lines of Binary-Form Factorisation*. The frozen Stage-2.5
manuscript, frozen package, public outputs, and Stage-3 reports were not
overwritten.

The revision makes one substantive theorem-level advance: it proves the
proposed prime-local star presentation and derives an exact local/global Smith
calculation. It also repairs the literature framing and scheme-theoretic
geometry requested by the panel. These are producer-side revisions subject to
Stage 3' review. They are not independent verification, priority resolution,
external peer review, or acceptance.

## Executive summary of mathematical changes

1. The primitive complete-edge cokernel is now proved to have, for every prime
   and every admissible pivot, the local presentation

   \[
   C_{\mathbf e}\otimes\mathbb Z_{(p)}
   \cong
   \mathbb Z_{(p)}/
   (D_a,2e_ie_j:i<j, i,j\ne a).
   \]

2. The revision derives every valuation of `h`, a complete two-adic case
   split, a symmetric global pair-exclusion formula, an `O(k^2)` gcd
   computation, and equality of the spanning-tree gcd with the full
   maximal-minor gcd.
3. The complete nonprimitive Smith form remains
   `diag(g,...,g,g h(e))`, now with the final invariant explicitly evaluated.
4. Pairwise resultants are proved to generate all regular units modulo
   constants on the universal pairwise-coprime open. This supplies a scoped
   intrinsic meaning: the unit-character residual group of that open.
5. The generic-degree theorem is now proved by an fpqc-local Cartesian diagram
   and a finite-locally-free factorisation, rather than primarily by branchwise
   point counting.
6. Signed-graph, arithmetic-matroid, toric-arrangement, matroid-over-ring,
   root-system, and adjacent Smith antecedents are integrated with exact claim
   boundaries.

## Priority 1 responses

### P1-1 — exact arithmetic endpoint

**Disposition:** implemented; mathematical change; pending Stage 3' review.

#### P1-1.1 — investigate without presumption

The proposed statement was first treated as a conjectural target in
`LOCAL_SMITH_THEOREM.md`. The investigation found a proof rather than a
counterexample. The manuscript states the result only after the proof, in
Section 7.2, Theorem 7.1.

#### P1-1.2 — prove the module isomorphism

Section 7.2, Theorem 7.1 proves the actual module isomorphism by Tietze
elimination over `R_p=Z_(p)`. A `p`-unit star eliminates all generators except
`x_a`; the ambient relation yields `D_a`, and every non-star edge yields
`2e_i e_j`. The proof divides only by the unit `e_a`. It explicitly covers
`p=2`, `k=3`, `D_a=0`, and vanishing coefficients.

A separate internal adversarial reconstruction is recorded in
`LOCAL_SMITH_ADVERSARIAL_AUDIT.md`. It found no counterexample or major proof
error. This remains an internal check, not external reproduction.

#### P1-1.3 — valuations, choice independence, and global form

- Pivot independence is stated immediately after Theorem 7.1: each displayed
  ideal is the annihilator of the same canonical local module, and admissible
  cyclic generators differ by a unit.
- Corollary 7.2 gives the exact valuation as the minimum of the pivot imbalance
  and non-star product valuations.
- Equations (7.6)--(7.7) give the odd and two-adic cases, including the
  exactly-two-odd higher-valuation branch.
- Theorem 7.3 gives the symmetric global formula
  `h=2^eta_2 product Q_ab^odd`.
- Theorem 7.4 proves that spanning-tree minors already generate the full local
  Fitting ideal.
- Corollary 7.5 gives the complete nonprimitive Smith form and Section 7.4
  gives the connected and prime-to-`p` étale group-scheme factors.

#### P1-1.4 — proof/evidence separation

The proofs in Section 7 use no finite computation. Section 9 separately
describes `verify_local_smith.py`, which passed 44,220 positive comparisons and
five deliberate negative controls under ordinary and optimized Python. The
normal and optimized receipts are byte-identical. The manuscript labels this
producer-side regression evidence only.

**Remaining limitation:** no independent specialist reproduction or formal
proof has occurred.

### P1-2 — graph/lattice context and contribution hierarchy

**Disposition:** implemented; literature/framing change; pending Stage 3'
review.

#### P1-2.1 — signed-graph, arithmetic-matroid, toric, and Smith context

- Section 6.2 cites Zaslavsky's all-negative signed-graph rank/support results
  together with the 1983 erratum, and the direct unoriented-incidence work.
- Section 7.1 identifies the primitive index with the standard representable
  arithmetic-matroid multiplicity `m(E)` and cites the GCD rule.
- Section 7.2 relates the quotient module to matroids over `Z` and DVRs.
- Section 7.4 distinguishes the complex toric component count from the
  arbitrary-characteristic diagonalizable group scheme.
- Section 10.1 and Appendix D compare the equal-weight root-list case,
  Laplacian/critical-group context, and the Hanusa--Zaslavsky complete-incidence
  lcm result without claiming an exact collision.

The primary-source record is `ARITHMETIC_LITERATURE_AUDIT.md`.

#### P1-2.2 — standard `m(E)` versus manuscript-specific evaluation

Section 7.1 states

`h(e)=m_e(E)` and `m_d(E)=g^(k-1) h(e)`.

The manuscript no longer presents the gcd definition, GCD rule, or complex
toric component count as new. The candidate increment is the explicit local
module, exact evaluation, tree-gcd theorem, and factorisation-open
interpretation for the cross-weighted diagonal-quotient list.

#### P1-2.3 — theorem-status table

Section 1 contains a seven-row status table separating classical antecedents,
formal determinant-line consequences, factorisation-specific specialisations,
standard arithmetic-matroid data, the candidate exact theorem package, and the
generic-degree synthesis.

#### P1-2.4 — arithmetic result made primary

The title, English and Chinese abstracts, introduction, Section 10.1, and
conclusion now lead with the exact Smith calculation. Bounded-search language
is retained; no absolute novelty or priority claim is made.

**Remaining limitation:** the audit is bounded and producer-side.

### P1-3 — lattice-to-geometry and scheme precision

**Disposition:** implemented; mathematics and exposition; pending Stage 3'
review.

#### P1-3.1 — five character/function categories

Sections 7.1 and 8.2 distinguish:

1. the redundant full edge list and `m(E)`;
2. a selected square edge matrix and `m(H)=|det W_H|`;
3. nonnegative polynomial resultant monomials;
4. Laurent resultant units on `U=D(Delta)`; and
5. arbitrary polynomial semi-invariants.

#### P1-3.2 — the `(1,2,2)` diagnostic

Sections 7.5 and 8.2 verify that the full matrix has Smith form `(1,1)` while
the three edge-basis determinants have absolute values `3,2,2`. The revision
also constructs the nonnegative monomial tuple

`(R12 R13 R23, R12 R23)`

whose character matrix is the identity. The associated total generic degree is
30, compared with 90, 60, and 60 for the three edge charts.

#### P1-3.3 — scoped residual-group claim

Equation (7.1) proves that pairwise resultants generate every regular unit
modulo constants on the universal pairwise-coprime open. The paper therefore
uses the scoped phrase **unit-character residual group of `U`**. It does not
claim intrinsic universality among arbitrary semi-invariants or after further
shrinking.

#### P1-3.4 — exact multiplicity-one hypotheses

Section 4.1 now states the unconditional base-changed ideal identity (4.4),
the DVR valuation formula (4.5), and precise order-one hypotheses. It also
gives the Cartier-divisor formulation and explains why a ramified pullback can
raise multiplicity even if the support is reduced.

#### P1-3.5 — torsor/descent and Cartesian diagram

The proof of Theorem 8.1 constructs the root-partition cover, the product-one
frame torsor, a common dense good open, and the Cartesian square (8.3). After
fpqc trivialisation, the map is the translated torus isogeny

`beta(x,lambda)=(x,g(x) chi_W(lambda))`.

#### P1-3.6 — total, separable, inseparable, point, and étale data

Equation (8.2) factors the restricted map into a finite-locally-free morphism
of rank `|det W|` followed by a finite étale morphism of rank
`D!/product d_i!`. The proof derives total degree, separable degree,
inseparable factor, geometric-point count, and étaleness from this
factorisation and Smith form.

#### P1-3.7 — chart-level consequence without conflation

Section 8.2 proves that a square Laurent basis always realises the full-list
index on `U`, while the `(1,2,2)` table shows that individual edge determinants
and polynomial monomial determinants can differ from one another and from the
full redundant-list gcd.

**Remaining limitations:** arbitrary base change can split resultants or add
units; saturation does not prove existence of a nonnegative monomial basis in
general; different branch translates of the raw rectangular target are not
classified.

## Priority 2 responses

### P2-1 — formal exterior-algebra layer

**Disposition:** implemented in substance; expository change.

The Section-1 status table and Section 10.1 explicitly identify the Plücker
completion and border contraction as formal determinant-line consequences once
the scalar, kernel, and orientation are fixed. The existing arbitrary-ring
composition Lemma 3.1 is retained because it is stronger and more useful for
the integral orientation than an additional abstract cofactor lemma. A second
near-duplicate lemma was not added.

### P2-2 — terminology and conventions

**Disposition:** implemented.

- The paper uses “pairwise-collision product” and states what it detects.
- Ambiguous “normaliser” terminology was removed in favour of “normalising
  function” or “normalising semi-invariant.”
- Section 7.2 defines the row-lattice/cokernel convention.
- Section 7.4 states the base of the diagonalizable group scheme.
- “Isogeny” is used for a square full-rank map or for the map onto the
  scheme-theoretic image, not for the raw rectangular target.

### P2-3 — signs, denominators, and isolated components

**Disposition:** implemented.

- Section 6 now has contiguous subsection numbering.
- Equation (6.1) states the weighted incidence transformation before
  cancellation; the isolated tree vertex is handled explicitly.
- Appendix E defines the Vandermonde orientation.
- Appendix E adds a parity table for deleted `A`- and `B`-block columns.
- The residual group is consistently written `mu_g^(k-2) x mu_(g h(e))`.

### P2-4 — compact examples

**Disposition:** implemented.

Section 7.5 includes exact odd-prime, higher odd-adic, higher two-adic,
nonprimitive, and saturation-without-edge-basis examples. Section 8.2 adds the
associated chart-degree table.

## Priority 3 responses

### P3-1 — title, abstracts, introduction, conclusion

**Disposition:** implemented.

The title is changed from *Resultant-Character Lattices of Binary-Form
Factorisations: An Affine Plücker Lift of the Classical Multiplication
Jacobian* to *Exact Smith Invariants and Affine Determinant Lines of Binary-Form
Factorisation*. Both abstracts, Section 1, and Section 11 now state the exact
local/global theorem and all geometric qualifiers.

### P3-2 — administrative submission metadata

**Disposition:** deliberate limitation; unresolved submission blocker.

No author identity, affiliation, contribution allocation, final conflict
declaration, funding statement, or distribution licence was supplied. None was
invented. The manuscript adds a “Submission metadata and licence” section that
explicitly blocks submission or release until the responsible author supplies
and approves these fields. The AI-use disclosure remains separate from
authorship and verification.

### P3-3 — copyediting and build

**Disposition:** implemented pending final integrity.

Section numbering, citation keys, field notation, terminology, keywords, and
cross-references were revised. The Chinese abstract is retained as optional
research-draft front matter rather than represented as a target-journal
requirement. Pandoc citation processing passes with all 28 references cited,
and the two-pass XeLaTeX build reports no undefined citation/reference,
overfull-box, or font warning.

## Devil's Advocate dispositions

| Finding | Response |
|---|---|
| DA-MAJOR-1: top divisor unevaluated | Resolved mathematically by Theorem 7.1, Corollary 7.2, and Theorem 7.3. |
| DA-MAJOR-2: full list differs from square charts | Adopted and demonstrated in Sections 7.5 and 8.2. |
| DA-MAJOR-3: endpoint may be too slight | Strengthened by the exact local/global calculation, tree-gcd theorem, and regular-unit geometry; significance remains for Stage 3' judgement. |
| DA-MAJOR-4: resultants not intrinsic among all semi-invariants | Adopted in the broad category; answered positively only for regular units on the fixed open `U`. |
| DA-MINOR-1: abstract overstates generic degree | Repaired with fixed labelled degrees, algebraically closed base, square full-rank matrix, dense target open, and finite-locally-free qualifiers. |
| DA-MINOR-2: examples miss odd and higher valuations | Resolved by Section 7.5 and the new exact verifier. |

No DA-CRITICAL finding existed.

## Verification supplied with the revision

- `LOCAL_SMITH_THEOREM.md`: proof-development record.
- `LOCAL_SMITH_ADVERSARIAL_AUDIT.md`: separate internal adversarial audit;
  PASS WITH MINOR CLARIFICATIONS, all incorporated.
- `ARITHMETIC_LITERATURE_AUDIT.md`: bounded primary-source audit.
- `GEOMETRY_INTERFACE_REVISIONS.md`: unit-group and finite-flat proof record.
- `verify_local_smith.py`: exact producer-side regression tier.
- `verification_receipts/local_smith.normal.txt` and
  `local_smith.optimized.txt`: byte-identical receipts.
- `manuscript-revised.pdf`: clean 35-page two-pass XeLaTeX build at the first
  Stage-4 compilation checkpoint.

## Requested re-review

Stage 3' should perform a fresh internal verification of:

1. the local presentation and Fitting-ideal passage;
2. the global odd/two-adic formula and tree-gcd proof;
3. the exact arithmetic-matroid and signed-graph attribution boundary;
4. the regular-unit universal property;
5. the fpqc Cartesian diagram and finite-locally-free degree proof; and
6. the claim that the revised title and contribution hierarchy are
   proportionate.

Completion of this response is not acceptance. P3-2 remains a deliberate
release blocker even if the mathematical revision is accepted internally.
