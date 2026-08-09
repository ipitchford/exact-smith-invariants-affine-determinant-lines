## Methodology Review Report (Peer Reviewer 1)

### Reviewer Identity

A commutative algebraist specialising in resultants, determinantal ideals,
determinant-of-complexes arguments, and scheme-theoretic properties of
polynomial maps over arbitrary base rings. This report is an independent
proof-methodology audit of the frozen manuscript. It does not assess priority
or literature completeness, and it does not treat the producer-side symbolic
checks as an independent proof or reproduction.

### Overall Recommendation

**Minor Revision**

### Confidence Score

**4/5**

### Summary Assessment

The manuscript presents a coherent theoretical design: a universal
two-factor complementary-minor identity is composed integrally to obtain the
all-factor Plucker tensor; Laplace expansion and Cauchy--Binet then contract
that tensor against border gradients; weighted incidence matrices convert the
resultant characters into graph minors; and determinantal divisors convert a
uniform modular-rank bound into the asserted Smith shape. I checked the
dimension substitutions, complementary-minor signs, induction parity,
unitriangular torus-basis change, character-coordinate transformation, and
modular kernel analysis. I find no counterexample or fatal inference error in
these arguments. In particular, the proof of Theorem 7.1 is not computational:
the crucial step is the proof that every reduction of the primitive complete
edge matrix has rank at least \(k-2\), which forces its first \(k-2\)
determinantal divisors to be one.

The revisions I request are mainly scheme-theoretic precision at two
interfaces. First, the post-base-change multiplicity-one statement should be
formulated in terms of the local equation or order of the pulled-back
resultant, rather than the ambiguous phrase "the component is reduced."
Second, Corollary 8.1 should exhibit a finite-locally-free diagram over the
chosen dense open, making the scheme fibre, degree, separable degree, and
inseparable factor consequences of a base-changed torus isogeny rather than of
a primarily pointwise branch count. These repairs require fuller exposition,
not a new mathematical idea. The exact computations are unusually well
bounded and useful for detecting sign mistakes, but the paper correctly
identifies them as producer-side regression evidence only.

### Strengths

1. **Integral composition rather than generic division (Lemma 3.1, lines
   265--382):** The block-composition lemma works over an arbitrary
   commutative ring and avoids selecting and dividing by a generically nonzero
   minor. The Cauchy--Binet expansion, final-column expansion, and last-row
   expansion use compatible zero-based complementary-minor conventions. In
   particular, the count \(m-i_a+a\) in line 349 and the
   \((-1)^{t_1+a}\) cofactor in lines 365--369 produce the displayed
   \((-1)^{t_1}\) factor. The argument also remains valid in the base case
   \(t_1=0\).

2. **The all-factor induction closes with the correct kernel basis and parity
   (Theorem 4.1, lines 410--521):** Under the substitutions
   \(r=D'+1\), \(q=d_k+1\), and \(t_1=k-2\), the matrix dimensions in
   Lemma 3.1 match the factorisation of multiplication. The proposed lift
   \((0,\ldots,0,A_{k-1},-A_k)\) maps to the outer kernel
   \((B,-A_k)\), and the passage from the inherited rows to the standard
   \(e_b-e_k\) rows is unitriangular of determinant one. The recurrence in
   lines 508--519 agrees with the closed exponent modulo two. This establishes
   a polynomial identity over \(\mathbb Z\), so arbitrary base change is a
   genuine theorem consequence, not an extrapolation from characteristic
   zero.

3. **The border contraction is a formal and correctly signed consequence
   (Corollaries 5.1--5.2, lines 608--664):** The \(I\)-dependent part of the
   Laplace sign cancels the definition of \(p_I\); the remaining parity
   \(nt+\binom t2\) is consistent with the stated row order. Cauchy--Binet
   then gives \(\det(KG^{\mathsf T})\), and transposition reconciles the
   displayed \((a,b)\) indexing. The semi-invariant specialisation correctly
   retains the reduction of the integer character determinant in positive
   characteristic.

4. **The weighted incidence and Smith arguments are logically economical
   (Theorems 6.1 and 7.1, lines 703--770 and 890--961):** The matrix with
   columns \(e_b-e_k\) and \(e_k\) is unimodular, so no spurious factor of
   \(k\) enters when the torus constraint is eliminated. Column scaling yields
   the factor \(\prod_i d_i^{\deg_H(i)-1}\), while the classical component
   ranks leave precisely one tree component and odd-unicyclic remaining
   components. For primitive degrees, the modular kernel has dimension at most
   one for every prime. Hence some \((k-2)\)-minor survives modulo every prime,
   the \((k-2)\)-nd determinantal divisor is one, and the final invariant is
   exactly the gcd of maximal minors. Scaling every row by the common gcd
   multiplies every Smith invariant by that gcd. No finite computation is
   needed in this proof.

5. **Assurance boundaries are methodologically sound (lines 1183--1240,
   1319--1326, and 1445--1451):** The two polynomial backends, exact arithmetic,
   optimized-mode runs, and deliberate mutations are strong regression tests
   for convention errors. The manuscript nevertheless says explicitly that
   these are producer-written, cross-implementation checks and do not prove
   the universal claims, novelty, or independent reproducibility. That is the
   correct evidential hierarchy.

### Weaknesses

1. **The post-base-change multiplicity-one condition is under-specified
   (lines 566--583):** The universal-ring statement is sound: at the
   height-one prime \((R_{ij})\), a chosen \(K\)-minor is a unit and the other
   nonassociate resultants are units, so the localized maximal-minor ideal has
   valuation one. After an arbitrary base change, however, saying that "the
   component is reduced" does not by itself specify an order of vanishing or
   ensure that the pulled-back resultant is a uniformizer in a codimension-one
   local ring. Ramified pullback can change multiplicity, and a valuation is
   not available on an arbitrary nonnormal local ring without further
   qualification. **Why this matters:** this paragraph is the manuscript's
   stated scheme-theoretic refinement, so its hypotheses must support its exact
   multiplicity language. **Improvement:** state the unconditional localized
   ideal identity after base change, then give multiplicity one under an
   explicit hypothesis such as an integral normal (or regular in codimension
   one) base, a height-one collision prime at which a \(K\)-minor and all other
   resultants are units, and order one for the pulled-back \(R_{ij}\). An
   equivalent Cartier-divisor formulation would be even cleaner.

2. **Corollary 8.1 needs a scheme-level finite-cover diagram, not only a
   branchwise fibre count (lines 1030--1066 and 1068--1174):** The root-partition
   cover and torus-isogeny ingredients are appropriate, and the asserted
   degree is credible. The proof, however, moves from a finite etale
   projective cover and a \(T\)-torsor to equations on selected affine
   representatives, then concludes that a generic geometric fibre is a
   disjoint union of translates. **Why this matters:** in characteristic
   dividing \(\det W\), the relevant fibres are nonreduced; a pointwise branch
   description alone does not establish their scheme lengths, finite local
   freeness after shrinking, or the function-field inseparable degree.
   **Improvement:** after constructing \(V_D^{\mathrm{good}}\), display the
   Cartesian diagram over
   \(V_D^{\mathrm{good}}\times(\mathbb G_m)^t\) that identifies the restriction
   of \(\Phi\), fpqc-locally on the \(T\)-torsor, with the base change of
   \(\chi_W:T\to(\mathbb G_m)^t\). State explicitly that this restriction is
   finite locally free of rank \(|\det W|\) on each of the \(\nu\) etale
   branches. Smith normal form then proves, scheme-theoretically, the total,
   separable, and inseparable degrees.

3. **The torsor and descent step is correct in outline but too compressed
   (lines 1072--1130):** The map \(q\) should indeed be the product-one frame
   torsor, and a semi-invariant generator gives a descent datum on its principal
   ideal. These two assertions currently appear without an explicit local
   trivialisation or cocycle. **Why this matters:** the proper closed sets
   \(Z_a\) are used to find a single dense open on which every normaliser is
   nonzero on every factorisation branch. **Improvement:** add a short lemma
   proving that \(q\) is an fpqc \(T\)-torsor; show
   \(a^*(g_a)=\chi_a g_a\), so \((g_a)\) has the required descent datum; and
   spell out that finite morphisms preserve dimension of closed subsets, which
   makes \(\pi(Z_a)\) proper because \(Z^{\mathrm{sf}}\) is irreducible. This
   can be combined with the diagram requested above.

4. **Two sign- and denominator-sensitive proofs would benefit from one more
   explicit convention (lines 723--750 and Appendix E, lines 1540--1693):** In
   Theorem 6.1 the proof speaks of multiplying columns and then dividing by
   degree factors even though an isolated tree vertex produces the displayed
   exponent \(-1\). In Appendix E, the Vandermonde orientation is implicit and
   the cancellations between (E.4) and (E.5), and between (E.6) and (E.7), are
   condensed despite the theorem's emphasis on an exact global sign.
   **Why this matters:** neither point appears false, but both are likely fault
   lines for independent reproduction and later formalisation. **Improvement:**
   give the incidence identity first after cross-multiplication and handle the
   isolated-vertex cancellation explicitly; define
   \(\operatorname{Vand}(x)=\prod_{i<j}(x_j-x_i)\), and include a short parity
   table for the two deleted-column blocks in Lemma E.1.

### Detailed Comments

#### Research Questions & Hypotheses

- The mathematical questions are clear and answerable: determine the full
  complementary-minor tensor, contract it against torus-normalising borders,
  compute the resultant-character lattice, and translate the Smith data into
  residual group schemes and generic degrees.
- The conclusions are appropriately narrower than the surrounding Keller and
  Hessian programme. Lines 1176--1181 and 1293--1317 explicitly state that
  local determinant control does not recognise affine-space slices or produce
  a Keller map.
- There are no empirical hypotheses. The relevant standards are validity of
  universal polynomial identities, exact control of orientation, and
  scheme-theoretic validity in all stated characteristics.

#### Research Design

- This is a theoretical/conceptual design with exact symbolic falsification
  checks. The ordering is effective: prove an arbitrary-ring composition
  lemma; establish the universal determinant identity; derive formal border
  consequences; compute a discrete character matrix; and only then pass to
  geometry.
- The manuscript wisely formalises the polynomial identities before invoking
  divisor or etaleness language (Appendix C, lines 1453--1467). That ordering
  keeps the most reusable theorem independent of geometric regularity
  hypotheses.
- The design would be stronger if Section 8 adopted the same level of formal
  explicitness as Sections 3--5 through one torsor/isogeny proposition and a
  Cartesian diagram.

#### Sampling Strategy

- **Not applicable.** This is not an inferential study based on a sample. The
  finite degree vectors in Section 9 are test cases, not a sample from which
  theorems are inferred.
- The selected checks cover factor-order sign changes, multiple torus ranks,
  weighted degrees, graph types, and bad characteristics. That is an
  appropriate regression suite, but it has no proof-bearing role.

#### Data Collection

- **Not applicable in the empirical sense.** The mathematical data are
  universal coefficient matrices and exact integer character matrices.
- The manuscript describes the construction of each test object and the
  deliberate mutations sufficiently to explain what kinds of implementation
  error the receipts are designed to detect. I did not read or rerun those
  programs for this report, so I do not independently attest to the numerical
  totals in Section 9.

#### Analysis Methods

- **Lemma 3.1:** The complementary-minor convention and Cauchy--Binet indexing
  are consistent. Equation (3.5) correctly combines insertion of column
  \(i_a\) with \(p_{I\setminus\{i_a\}}(S)\), and equation (3.6) uses the
  correct last-row cofactor.
- **Theorem 4.1:** The inductive map and lift have the required dimensions;
  resultant multiplicativity is used without a block permutation; and the
  standard torus rows differ from the inherited rows by determinant-one row
  operations. The parity difference \(k-(k-2)=2\) closes the recurrence.
- **Section 4.1:** The exact ideal equality follows immediately from all the
  coordinate identities. The universal height-one argument is valid; only the
  formulation after general base change needs tightening.
- **Corollary 5.1:** The Laplace and Cauchy--Binet signs agree with Appendix E in
  the \(k=2\) specialisation. This is an important internal consistency check.
- **Theorem 6.1:** The unimodular augmentation correctly identifies the torus
  minor with an augmented signless-incidence determinant. The component-rank
  classification is complete for a graph with exactly \(k-1\) edges.
- **Theorem 7.1:** The modular analysis correctly handles vanishing degree
  residues. If an index is outside \(S\), its coordinate vanishes; on \(S\),
  the transformed coordinates have at most one parameter. This establishes
  the uniform rank lower bound needed for the determinantal-divisor argument.
- **Corollary 7.2:** For odd \(p\), only two equal nonzero residues leave a
  kernel; in characteristic two, the parity of the number of odd primitive
  degrees is exactly the survival condition. The corollary correctly claims
  prime support rather than exact valuations.
- **Corollary 8.1:** The formula combines the labelled root-partition degree
  with the scheme order of a torus isogeny. The mathematical mechanism is
  correct, but its scheme-level implementation should be made explicit as
  requested above.

#### Results Presentation

- The theorem/corollary hierarchy makes clear which statements are universal
  identities, formal contractions, matrix calculations, and geometric
  syntheses.
- The manuscript does not selectively suppress negative scope. It states that
  the Smith theorem gives prime support but not closed valuation formulas, and
  that the work does not classify arbitrary normalisers, higher collision
  schemes, affine slices, Keller maps, or Hessian constructions.
- The conclusions do not extend beyond the proofs once the two
  scheme-theoretic clarifications above are made. The strongest statement,
  Theorem 7.1 with Corollary 7.2, is proved by integer and modular linear
  algebra rather than inferred from checked cases.

#### Reproducibility

- The exact coefficient order, Sylvester order, zero-based deleted-column
  sign, torus basis, gradient-row order, and border sign are all recorded in
  Appendix A (lines 1430--1443). This is excellent practice for a
  sign-sensitive result.
- Appendix E makes the all-factor induction logically independent of the
  unrefereed parent candidate. Its dense-open proof over \(\mathbb C\) is a
  valid way to prove a universal integer polynomial identity.
- The computational evidence uses exact arithmetic, distinct algebra engines,
  normal and optimized execution, and negative controls. These features make
  it reproducible as software evidence but do not make it an independent
  mathematical reproduction. The paper states this distinction correctly.
- A formalisation following Appendix C would substantially improve assurance,
  especially for Lemma 3.1 and Appendix E, but formalisation is not necessary
  for the present theorem to be publishable.

#### Methodological Fallacies Detected

- No statistical or empirical fallacies apply.
- **Potential proof-by-computation fallacy:** explicitly avoided. The finite
  checks are never invoked to establish a universal theorem.
- **Potential over-generalisation after base change:** locally present in the
  wording of lines 576--580. This is repairable by stating the exact local
  hypotheses described in Weakness 1.
- **Potential set-points/scheme-fibres conflation:** the prose proof of
  Corollary 8.1 comes close to this in positive characteristic. The group-scheme
  language points in the correct direction, but the requested finite-flat
  diagram would remove the ambiguity.

### Robustness and Reproducibility Assessment

**Theoretical robustness: Strong, subject to minor scheme-theoretic
clarification.** The core identities are proved universally and do not rely on
irreducibility, generic smoothness, or characteristic-zero division. The graph
and Smith calculations are exact over \(\mathbb Z\).

**Computational reproducibility: Well specified but producer-side.** The
manuscript reports exact checks across two polynomial systems and a separate
integer-matrix implementation, with deliberate false formulas and
optimized-mode controls. Because these implementations were written within the
same research process and were not examined or rerun in this review, they
remain supporting receipts, not independent reproduction or validation of the
proof.

**Statistical reporting completeness:** Not applicable to a purely theoretical
mathematics paper.

### Questions for Authors

1. Can the post-base-change statement in lines 576--580 be replaced by an
   exact localized ideal statement, followed by a multiplicity-one corollary
   under normality/regular-codimension-one and order-one pullback hypotheses?
2. Can you exhibit the restriction of \(\Phi\) over
   \(V_D^{\mathrm{good}}\times(\mathbb G_m)^t\) as, fpqc-locally, the disjoint
   union of \(\nu\) base changes of \(\chi_W\), and thereby prove finite local
   freeness and fibre length without relying on geometric-point counting?
3. Is the map \(q:U^{\mathrm{sf}}\to Z^{\mathrm{sf}}\) Zariski locally trivial
   as a \(T\)-torsor in your model, or only asserted fpqc locally? Either is
   sufficient, but an explicit local trivialisation would make the descent of
   \((g_a)\) transparent.
4. Will you define the Vandermonde orientation explicitly and show one line of
   the sign cancellation leading to (E.5) and (E.7)? This seems especially
   valuable because the paper advertises an integral orientation, not merely
   equality up to sign.
5. In Corollary 8.1, can you state explicitly that the finite etale
   root-partition cover remains etale when the characteristic divides
   \(D!/\prod d_i!\), because it arises from a free action of a constant etale
   symmetric group scheme rather than from averaging by the group order?

### Minor Issues

- In Section 8, the algebraically closed field is denoted \(K\), while \(K\)
  already denotes the torus-kernel matrix throughout Sections 2--5. Renaming
  the field \(\Bbbk\) would reduce ambiguity.
- At lines 909--914, write \(\mu_{g h(\mathbf e)}\) rather than \(\mu_{gh}\)
  on first occurrence so that the dependence of \(h\) remains explicit.
- Clarify whether "On \(X^\circ\), the map is etale" means that every point of
  the restricted source is an etale point of \(\Phi\), or explicitly name the
  target open used for the finite-etale restriction. The Jacobian assertion is
  pointwise valid either way, but the two formulations serve different uses.
- The definition of generic scheme degree at lines 1030--1032 should say that
  after shrinking the target, the map is finite locally free; then geometric
  fibre length is visibly constant. This would align the definition with the
  requested Section 8 diagram.
- The heading calls the main border result "Corollary 5.1," whereas some
  surrounding programme descriptions call it "Theorem 5.1." Standardise the
  reference label in derivative materials.

### Final Methodological Judgment

The integral all-factor theorem, multi-border contraction, weighted graph
minor formula, Smith-shape theorem, and bad-prime criterion are supported by a
valid proof architecture. I found no major mathematical defect in those core
results. Publication-quality revision should make the codimension-one
multiplicity claim and the generic-degree/isogeny synthesis as precise at the
scheme level as the determinant identities already are at the polynomial
level. Subject to those focused revisions, the manuscript meets a strong
methodological standard for a theoretical algebra paper.
