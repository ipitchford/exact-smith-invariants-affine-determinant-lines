# Stage 3' Verification Review — EIC Traceability Report

**Manuscript:** *Exact Smith Invariants and Affine Determinant Lines of
Binary-Form Factorisation*  
**Mode:** Academic-paper-reviewer `re-review` / Pipeline Stage 3'  
**Journal calibration:** *Linear Algebra and its Applications*  
**Decision:** **Accept within the producer-side research-draft scope**  
**Confidence:** **4/5**  
**Process status:** This is an internal simulated verification review. It is
not external peer review, independent specialist reproduction, formal
verification, a priority determination, journal acceptance, or permission to
submit or release the artefact.

## 1. Scope and verification method

I read the complete Stage 3 editorial decision and roadmap, the complete
point-by-point response, the complete revised manuscript, all five relevant
first-round reports, the field-analysis record, and the supplementary local
valuation spot check. I then navigated from every Priority-1 and Priority-2
author claim to the corresponding passage in the revised manuscript and
checked the mathematical or editorial change itself. The author's response was
used as an index, not as evidence that a revision succeeded.

For the new arithmetic centrepiece I independently reconstructed, from the
manuscript text, the generator elimination, annihilator/Fitting-ideal passage,
odd and two-adic simplifications, global product formula, spanning-tree ideal,
and nonprimitive Smith scaling. For the geometric repair I checked the
torsor, descent, Cartesian base-change square, finite-locally-free ranks, and
separable/inseparable factorisation. This is an independent *internal reading
of the proof*, not an independently authored external reproduction. I did not
treat the producer-side programs, receipts, or adversarial audit as proof.

The research-draft scope matters to the decision. The manuscript deliberately
lacks approved author, affiliation, contribution, funding, conflict, and
licence metadata. Those remain submission and release blockers, but they do
not prevent completion of the mathematical Stage 3' re-review.

## 2. Decision

### Accept within research-draft scope

All Priority-1 requirements are fully addressed at their actual manuscript
locations. The strongest former objection has been removed rather than merely
rephrased: Theorem 7.1 proves a one-generator local module isomorphism, not an
order coincidence, and Corollary 7.2 plus Theorems 7.3--7.4 compute the missing
valuations and full-list gcd. The resulting title and contribution hierarchy
are proportionate to the theorem now proved.

The signed-graph, arithmetic-matroid, toric-character, and adjacent Smith
framework is now integrated with appropriately narrow novelty language. The
complete regular-unit lattice, square chart lattice, polynomial monomial
semigroup, Laurent-unit lattice, and arbitrary semi-invariants are separated.
The scheme-level degree theorem is supported by the requested fpqc-local
Cartesian square and finite-locally-free factorisation.

Three Priority-2 items are fully addressed. The fourth, the compact example
table, is mathematically addressed but does not reproduce every column
requested in the roadmap; this is a non-blocking presentation issue. All four
Priority-2 items received substantive responses, satisfying the re-review
protocol's 80% response threshold. No new major or critical issue was found.

This decision closes the internal Stage 3' mathematical revision cycle. It
does **not** convert the paper into an externally peer-reviewed, independently
reproduced, priority-resolved, submission-ready, or release-ready work.

## 3. Revision response checklist

### Priority 1 — required revisions

| ID | Original review requirement | Author's claim | Response status | Actual revised location | Verified? | Quality assessment |
|---|---|---|---|---|---|---|
| **P1-1.1** | Treat the proposed local formula as an investigation, without presuming it true. | The formula was investigated first and stated in the manuscript only after a proof was found. | **FULLY_ADDRESSED** | Section 7.2, especially lines 1093--1121 | Yes | The final paper does not appeal to the spot checks as establishing the formula. It states a theorem only after giving exact hypotheses and immediately supplies the proof. The historical sequencing is documented in the proof-development note; the publishable point is independently checkable in the manuscript. |
| **P1-1.2** | Prove the local module isomorphism, including (p=2), (k=3), zero (D_a), and vanishing coefficients; do not prove only equality of orders. | Theorem 7.1 performs Tietze elimination using only the unit (e_a). | **FULLY_ADDRESSED** | Theorem 7.1 and proof, lines 1096--1139 | Yes | Each star relation eliminates one (x_i) because (e_a\in\mathbb Z_{(p)}^\times). The ambient relation becomes (D_ax_a=0); every non-star relation becomes (2e_ie_jx_a=0), up to a unit. No relation is discarded and no nonunit is divided out. This proves (C_{\mathbf e}\otimes R_p\cong R_p/I_{p,a}), including all named edge cases. |
| **P1-1.3** | Derive pivot-independent valuations, the full two-adic case, the global Smith conclusion, and choice independence. | Corollary 7.2, equations (7.6)--(7.7), Theorems 7.3--7.4, and Corollary 7.5 provide the complete calculation. | **FULLY_ADDRESSED** | Lines 1141--1177, 1186--1291, and 1297--1356 | Yes | The pivot ideals are annihilators of the same local module, and two pivot generators differ by a unit. The DVR minimum is the local zeroth Fitting ideal; localisation of the maximal-minor ideal identifies it with (v_p(h)). The odd and (2)-adic cases follow from the exact minimum, the symmetric product reconstructs all primes, the tree ideal equals the full Fitting ideal locally, and scaling by (g) gives the stated Smith form. |
| **P1-1.4** | Keep proof and computation separate. | Section 7 is proof-only; Section 9 reports bounded exact regressions and negative controls. | **FULLY_ADDRESSED** | Section 7, lines 1005--1397; Section 9, lines 1686--1758; assurance boundary, lines 1866--1873 | Yes | No finite computation is used in a theorem proof. The receipts are expressly called producer-side regression evidence and are denied the status of proof, independent reproduction, formal verification, or peer review. The numerical totals were not used to reach this review decision. |
| **P1-2.1** | Add signed-graph/frame-matroid, arithmetic-matroid, toric-arrangement, matroid-over-ring, and adjacent Smith context with exact locators. | These frameworks and primary sources were integrated throughout Sections 6, 7, 10, and Appendix D. | **FULLY_ADDRESSED** | Lines 810--822, 912--917, 1069--1082, 1179--1184, 1353--1356, 1788--1808, and 2037--2065 | Yes | The all-negative signed-incidence support is labelled classical and tied to Zaslavsky with the erratum; (h=m(E)) and the GCD rule are attributed to arithmetic-matroid sources; the full quotient is located in matroids-over-rings/DVR language; toric component counts and the critical-group boundary are stated. The bounded literature audit remains producer-side and is not upgraded to a priority claim. |
| **P1-2.2** | Identify (h) as standard (m(E)) while isolating manuscript-specific content. | Section 7.1 distinguishes full-list multiplicity from the local/global evaluation. | **FULLY_ADDRESSED** | Lines 1060--1082 and 1802--1821 | Yes | The manuscript explicitly states (h(\mathbf e)=m(E)), (m(H)=|\det W_H|), and (m_{\mathbf d}(E)=g^{k-1}h(\mathbf e)). It disclaims novelty for the GCD rule and component count, then identifies the candidate increment as the exact local module, valuations, global formula, tree-gcd equality, and factorisation-open interpretation. |
| **P1-2.3** | Add an introduction-level theorem-status table. | A seven-row status table separates antecedents, formal consequences, standard arithmetic data, candidate results, and synthesis. | **FULLY_ADDRESSED** | Introduction, lines 196--206 | Yes | The table is in the main text and directly distinguishes classical, formal, factorisation-specific, standard arithmetic-matroid, candidate theorem, and synthesis layers. It resolves the former aggregate-presentation risk. |
| **P1-2.4** | Make the arithmetic theorem primary and retain bounded novelty language. | Title, abstracts, introduction, contribution boundary, and conclusion now lead with the exact Smith result. | **FULLY_ADDRESSED** | Title and abstracts, lines 1--56; Introduction, lines 157--223; Section 10.1, lines 1810--1830; Conclusion, lines 1901--1940 | Yes | The exact local/global Smith calculation is now the declared centre of gravity. The affine Plücker lift and generic-degree theorem are properly subordinated. The manuscript explicitly calls the literature search bounded and requests independent specialist review. |
| **P1-3.1** | Separate the full redundant list, square edge matrices, polynomial monomials, Laurent units, and arbitrary semi-invariants. | Sections 7.1 and 8.2 distinguish all five categories. | **FULLY_ADDRESSED** | Lines 1033--1044, 1069--1082, and 1612--1637 | Yes | The full list has (m(E)); a square sublist has (m(H)=|\det W_H|); nonnegative monomials form a semigroup; Laurent units realise the row lattice; arbitrary polynomial semi-invariants are a larger class. No Smith row operation is silently treated as preserving polynomiality. |
| **P1-3.2** | Verify the ((1,2,2)) diagnostic before using it. | The full matrix has minors (3,2,2), and a nonnegative monomial pair has identity character matrix. | **FULLY_ADDRESSED** | Lines 1374--1396 and 1639--1677 | Yes | Direct calculation confirms (W_E=\bigl(\begin{smallmatrix}2&1\\1&-1\\-2&0\end{smallmatrix}\bigr)), maximal-minor absolute values (3,2,2), and gcd (1). The displayed exponent matrix sends (W_E) to (I_2). The generic degrees (90,60,60,30) then follow from the root-partition factor (30). |
| **P1-3.3** | Make residual-group claims resultant-relative unless a genuine universal property is proved. | Equation (7.1) proves that resultants generate all regular units on the fixed universal coprime open, yielding the scoped “unit-character residual group of (U)”. | **FULLY_ADDRESSED** | Lines 1009--1044, 1325--1370, and 1832--1847 | Yes | UFD localisation proves every unit is a unique Laurent resultant monomial modulo constants. This supplies an intrinsic character lattice for **regular units on this fixed open**, while the text expressly excludes arbitrary semi-invariants, further shrinkings, and arbitrary base change. The rectangular degree is stated only onto the scheme-theoretic image. |
| **P1-3.4** | Replace ambiguous post-base-change multiplicity language with an exact ideal/valuation or Cartier-divisor statement. | Equations (4.4)--(4.5) give the base-changed ideal identity and exact DVR valuation with order-one hypotheses. | **FULLY_ADDRESSED** | Section 4.1, lines 658--693 | Yes | The unconditional identity survives arbitrary base change. The order-one conclusion now requires a normal-domain height-one DVR, order one for the selected resultant, units for all others, and a unit kernel minor. The Cartier formulation correctly records ramified pullback multiplicity (m). |
| **P1-3.5** | Prove the fpqc torsor/descent step and display a finite-locally-free Cartesian diagram. | Theorem 8.1 constructs the root-partition cover, product-one frame torsor, descended zero loci, common good open, and square (8.3). | **FULLY_ADDRESSED** | Lines 1464--1592, especially 1498--1526 and 1528--1588 | Yes | The map $q$ is a $T$-torsor; semi-invariance makes each zero ideal descend; finiteness of the root-partition cover makes the excluded image closed and proper. After fpqc base change, $\theta$ becomes the translated torus homomorphism $\beta(x,\lambda)=(x,g(x)\chi_W(\lambda))$. Smith form makes $\beta$ finite locally free of rank $|\det W|$, and this descends. |
| **P1-3.6** | Derive total, separable, inseparable, point, and étale data scheme-theoretically. | Theorem 8.1 factors the map into ranks (|\det W|) and (D!/\prod d_i!), then applies Smith form. | **FULLY_ADDRESSED** | Theorem statement, lines 1429--1462; proof, lines 1585--1610 | Yes | The finite-locally-free composition gives total generic degree without point counting. Diagonal power maps give separable degree (prod s_i'), inseparable factor (p^{v_p(\det W)}), and geometric-point count; the root-partition factor stays étale. Corollary 5.2 gives the exact étaleness condition on (X^\circ). |
| **P1-3.7** | Give a chart-level consequence without conflating (h) and (|\det W|). | A Laurent basis realises the full index; the ((1,2,2)) example contrasts full-list, edge, and polynomial-monomial charts. | **FULLY_ADDRESSED** | Lines 1612--1677 | Yes | Equation (8.5) uses the full regular-unit index, while the table uses the actual determinant of each selected square chart. The text explicitly says a Laurent basis may use negative exponents and does not assert a general nonnegative basis theorem. |

### Priority 2 — suggested revisions

| ID | Original review requirement | Author's claim | Response status | Actual revised location | Verified? | Quality assessment |
|---|---|---|---|---|---|---|
| **P2-1** | Isolate the formal exterior-algebra layer and reduce its editorial weight. | The contribution table and boundary discussion identify formal versus factorisation-specific content; Lemma 3.1 is retained instead of adding a near-duplicate cofactor lemma. | **FULLY_ADDRESSED IN SUBSTANCE** | Lines 327--337, 491--512, 196--206, and 1810--1821 | Yes | No new abstract lemma was added, but the roadmap allowed a concise formal-versus-specific separation. The revised text now says exactly what is classical/formal and what the coordinate lift contributes, while preserving the integral orientation proof needed for auditability. |
| **P2-2** | Tighten collision, normalising-function, residual-group, isogeny, and matrix conventions. | Ambiguous “normaliser” language was removed; the collision product, row lattice, group base, and square/image isogenies are defined. | **FULLY_ADDRESSED** | Lines 306--310, 747--769, 1033--1057, 1325--1370, and 1398--1417 | Yes | Search of the complete manuscript found no use of “normaliser”. The product is explicitly a product of pairwise inter-factor resultants, the row-lattice quotient convention is stated, the residual group is over (\operatorname{Spec}\mathbb Z), and the rectangular map is described via its scheme-theoretic image rather than called a raw isogeny. |
| **P2-3** | Make signs, denominator cancellation, isolated components, and group notation independently auditable. | Section 6 gives a cross-multiplied integral identity and isolated-vertex cancellation; Appendix E fixes Vandermonde orientation and gives a parity table. | **FULLY_ADDRESSED** | Lines 824--910; Appendix A, lines 1998--2011; Appendix E, lines 2121--2137 and 2274--2283; group notation, lines 1325--1351 | Yes | Equation (6.1) precedes cancellation and the isolated vertex is handled explicitly. The Vandermonde direction is defined, the deleted-block parity table is present, section numbering is contiguous, and the residual factors are consistently written (\mu_g^{k-2}\times\mu_{g h(\mathbf e)}). |
| **P2-4** | Add a compact table containing degree decomposition, (m(E)), Smith data, square-basis determinants, group scheme, and bad primes, with odd and higher-valuation examples. | Section 7.5 and Section 8.2 provide exact diagnostic and chart-degree tables. | **PARTIALLY_ADDRESSED** | Lines 1372--1396 and 1639--1677 | Partial | The mathematics requested is present: odd bad primes, higher odd and two-adic valuations, nonprimitive scaling, the ((1,2,2)) saturation/edge-basis distinction, and chart degrees. The Section 7.5 table does not, however, expose separate columns for primitive (\mathbf e), content (g), full (m(E)), residual group scheme, and bad primes as the roadmap specified. This is a presentation omission, not a mathematical gap. |

**Priority-2 response rate:** 4/4 items received substantive responses; 3 are
fully addressed and 1 is partially addressed. This exceeds the protocol's 80%
response threshold.

## 4. Direct checks of the new theorem package

### 4.1 Local presentation and Fitting ideal

The decisive step is valid. Present (C_{\mathbf e}\otimes R_p) by the
generators (x_i), the ambient relation (\sum_i x_i=0), and all edge
relations (e_jx_i+e_ix_j=0). A (p)-unit (e_a) permits legitimate Tietze
elimination of every (x_i), (i\ne a). Substitution produces exactly

\[
 (D_a,2e_ie_j:i<j,\ i,j\ne a),
\]

with no omitted relation. Because this is a module isomorphism, its zeroth
Fitting ideal is that ideal. Fitting ideals commute with localisation, while
the global zeroth Fitting ideal is generated by the maximal minors. The least
DVR valuation is therefore exactly (v_p(h)), rather than merely a number
that agrees with checked examples.

### 4.2 Odd, two-adic, and global formulas

For odd (p), positivity of the local exponent forces exactly two unit
degrees, with equal residues; the minimum reduces to equation (7.6). At
(p=2), parity of the number of odd degrees yields the three cases in (7.7),
and the truncated pivot valuation is independent of which odd pivot is used.
For an odd prime dividing (Q_{ab}), primitivity forces (a,b) to be the
unique unit pair, so a prime cannot occur in two different odd factors. This
justifies the pairwise-coprime product in Theorem 7.3.

### 4.3 Tree-gcd theorem

After choosing a local unit pivot (a), the star determinant is a unit times
(D_a). Replacing one star edge by a bent edge (ij) gives a unit times
(e_i(D_a+2e_j)); subtracting (e_iD_a) supplies (2e_ie_j). Thus tree
minors contain every generator of the local annihilator ideal. Since tree
minors are themselves maximal minors, the reverse containment is immediate.
The equality of local ideals at every prime proves equality of the two global
positive gcds.

### 4.4 Nonprimitive Smith form and group scheme

Multiplying the primitive matrix by (g) multiplies every nonzero Smith entry
by (g), and the divisibility chain remains valid. Cartier duality then gives
the displayed product of roots-of-unity group schemes. The connected and
prime-to-(p) étale factors in (7.12) have the stated ranks. The manuscript
correctly distinguishes total scheme rank from geometric points.

## 5. New or residual issues discovered during revision

| ID | Severity | Location | Finding | Required disposition |
|---|---|---|---|---|
| **NEW-1** | Minor / presentation | Section 7.5, lines 1372--1383 | The compact table does not include all fields promised by P2-4: separate (\mathbf d,\mathbf e,g,m(E)), selected-basis determinants, residual group scheme, and bad-prime columns. The surrounding prose and Section 8.2 contain the missing mathematics. | Optional final editorial expansion; no re-review required. |
| **NEW-2** | Minor / notation | Section 8.1, line 1402 | The algebraically closed field is still denoted (K), while (K) denotes the torus-kernel matrix in Sections 2--5. This was a first-round minor issue and the response's broad copyediting statement suggests it was repaired, but the collision remains. | Rename the field (\Bbbk) in a final copyedit. |
| **NEW-3** | Minor / exposition | Theorem 7.3, line 1247 | The (O(k^2)) gcd-operation conclusion is true with standard pair-exclusion/range-gcd preprocessing, but the manuscript does not state that algorithm. A naive evaluation of every (G_{ab}) would look cubic. | Add one sentence describing prefix/range-gcd preprocessing, or omit the complexity label. |
| **NEW-4** | Minor / citation locator | Section 2.3, line 325 | Mahatab--Sampath is cited here without the theorem/equation locator supplied elsewhere, despite a first-round request to keep that scope explicit at each invocation. | Add “Theorem A.3 and equation (A.17)” in final copyediting. |

No new critical or major issue was found. None of these points changes a
theorem statement, proof strategy, title, or contribution boundary.

## 6. Devil's Advocate disposition on re-review

The first-round Devil's Advocate found no CRITICAL issue. Its four major
challenges are now resolved as follows:

1. **Unevaluated (h):** resolved by Theorem 7.1, Corollary 7.2, Theorems
   7.3--7.4, and Corollary 7.5.
2. **Rectangular index versus square chart:** resolved by Sections 7.1 and 8.2,
   especially the ((1,2,2)) example.
3. **Full-article significance:** materially strengthened by the exact local
   module, closed global formula, and tree-gcd theorem. Within the LAA-calibrated
   research-draft scope, this is now proportionate to a full article.
4. **Nonintrinsic resultant normalisation:** resolved in the regular-unit
   category by equation (7.1), with explicit exclusions for arbitrary
   semi-invariants and further open-set shrinkage.

The two DA minor findings are also resolved in substance: the abstract carries
the square/full-rank/algebraically-closed/dense-open qualifiers, and Section 7.5
contains odd-prime and higher-valuation examples.

## 7. Final editorial boundary

The mathematical response is accepted for the purpose of the internal Stage
3' research-draft pipeline. The manuscript may proceed to final integrity
checking with the four minor observations above recorded as non-blocking
copyedit items.

This report must not be described as external peer review or journal
acceptance. The paper remains a producer-authored research draft. Independent
specialist proof reproduction, a wider priority audit, approved author and
licence metadata, and any actual journal review remain outstanding.
