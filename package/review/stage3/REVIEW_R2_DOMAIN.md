## Domain Review Report (Peer Reviewer 2)

### Reviewer Identity

Reviewer 2 is acting as a senior elimination theorist with expertise in classical resultants, binary forms, Sylvester and Koszul complexes, Jacobians of coefficient-product maps, multiplication singularities, and coincident-root loci. This review is independent: it uses only the frozen manuscript, its bibliography, the supplied field/reviewer brief, and selected primary or authoritative literature consulted to resolve exact-object questions. No other Stage 3 review report was consulted.

### Overall Recommendation

**Major Revision**

### Confidence Score

**4/5**

### Summary Assessment

This is a mathematically coherent and unusually candid manuscript whose best feature is not a new resultant formula, but a carefully coordinated passage from classical square Jacobians to an affine, non-monic, all-factor Plücker identity and then to character-lattice arithmetic. I found no fatal exact-object collision beyond the monic square-Jacobian, rank-locus, and incidence-matrix antecedents that the authors already acknowledge. Theorem 4.1 is useful and clean over \(\mathbf Z\), but, once the common resultant factor and torus kernel are known, its Plücker completion is close to formal determinant-line algebra; the manuscript generally states this honestly. Theorem 6.1 is likewise a weighted specialization of classical signless-incidence minor theory. The genuinely most distinctive part is Theorem 7.1 together with Corollary 7.2: cyclicity of the torsion cokernel after removing the common content, and an exact classification of the primes supporting its final invariant factor. However, the last factor \(h(\mathbf e)\) is defined as a gcd of maximal minors, so the displayed final Smith entry is partly definitional and no valuation formula is supplied. Corollary 8.1 is a sound synthesis of root partitions and a torus isogeny, not an independent degree theorem. Publication should follow a stronger signed-graph/arithmetic-matroid antecedent audit, sharper headline wording for the Smith result, and several terminology and framing corrections.

### Strengths (3-5 items)

1. **Excellent control of the exact claim boundary.** The introduction and Section 2 distinguish the classical monic square Jacobian from the affine non-monic maximal-minor tensor, and Section 10.1 explicitly labels Corollary 5.1 as a contraction consequence, Theorem 6.1 as a weighted application of classical incidence theory, and Corollary 8.1 as a synthesis (manuscript lines 94-115, 232-255, and 1244-1291). This is the correct hierarchy.

2. **A clean universal integral identity.** Theorem 4.1 packages all maximal minors of the multiplication differential into one coordinate-complete formula over \(\mathbf Z\), with an explicit orientation convention and arbitrary base change (lines 389-521). Even if its conceptual derivation is largely formal after the scalar and kernel inputs, this is a useful reusable statement.

3. **Good separation of three phenomena often conflated in this subject.** The paper distinguishes the inter-factor collision factor \(\Delta_{\mathbf d}\), the torus tangent directions, and the arithmetic index of chosen characters. This separation makes Corollaries 5.1 and 5.2 transparent and prevents the resultant from being credited with the character-lattice contribution (lines 590-664).

4. **Theorem 7.1/Corollary 7.2 contain a concrete nonformal arithmetic result.** The modular argument showing that the first \(k-2\) primitive Smith factors are all \(1\), hence that the residual torsion is cyclic, is substantive. The parity and odd-prime classification in Corollary 7.2 gives a useful exact support theorem (lines 890-993).

5. **The geometric degree statement is responsibly scheme-theoretic.** Corollary 8.1 counts root partitions separately from the finite diagonalizable kernel, and it distinguishes scheme length, geometric points, separability, and etaleness in positive characteristic (lines 1011-1181). The final limitation that this does not itself produce a Keller map is essential and correctly stated.

### Weaknesses (3-5 items)

1. **The signed-graph and arithmetic-lattice literature is not yet adequately integrated.** The unweighted rank/minor statements are cited to Grossman--Kulkarni--Schochetman and Hessert--Mallik, but the all-negative signed-graph interpretation goes back at least to Zaslavsky's foundational treatment of signed incidence matrices. More importantly, the gcds of maximal minors of an integral character list are precisely the multiplicities that arithmetic-matroid and toric-arrangement language was designed to encode. This omission directly affects the positioning of Theorem 7.1, not merely the bibliography.

2. **The stated Smith normal form contains a partly tautological last entry.** In Theorem 7.1, \(h(\mathbf e)\) is defined immediately beforehand as the gcd of the maximal minors (lines 866-918). Once the lower determinantal divisors are shown to be \(1\), the equality of the final invariant factor with that gcd is the definition of Smith determinantal divisors. The real theorem is therefore: primitive torsion is cyclic, together with Corollary 7.2's exact prime-support criterion. The abstract, conclusion, and contribution discussion should say this just as directly. A closed formula for \(h\), or at least formulas for \(v_p(h)\), would materially strengthen the paper.

3. **Theorem 4.1 needs a more explicit account of what is formal and what is not.** The difficult inputs are the scalar resultant factor, its multiplicity, the torus kernel, and the global sign/orientation. Once two decomposable determinant-line tensors have the same kernel line and one scalar chart is fixed, the Plucker coordinate completion is standard exterior algebra. Lines 425-431 acknowledge this, but a general cofactor/Grassmann-duality lemma would make the contribution boundary more rigorous and would show exactly which part is specific to multiplication of binary forms.

4. **Some terminology is liable to mislead specialists.** The phrase "collision divisor" can suggest the full discriminant of the product, including repeated roots within an individual factor, whereas \(\Delta_{\mathbf d}\) records only pairwise inter-factor collisions. "Normaliser" has established, unrelated meanings in invariant theory and algebraic groups; here it means a border function or normalising semi-invariant. Both terms should be defined more tightly and used consistently.

5. **The paper remains a bounded synthesis rather than a full Smith-normal-form theory.** It treats the complete edge-character list and gives only the support, not the valuations, of its final primitive invariant. It does not classify arbitrary subsets of resultant characters, minimal normalising sets, or general semi-invariant tuples. These limitations are honestly stated (lines 1293-1317), but they mean that broad phrases such as "Smith-normal-form principle" should be reserved for the programme, not presented as an achieved classification.

### Detailed Comments

#### Literature Review

- **Coverage.** The exact-object audit in Sections 1, 2.3, 10.1, and Appendix D is much better than is customary. Artin's Lemma 1.8.5, Basu--Pollack--Roy's coefficient-product Jacobian, Bhargava--Cremona--Fisher--Gajovic's Hensel Jacobian, Chipalkatti's tangent/rank statement, Chaperon--Lopez de Medrano's arbitrary-factor monic rank locus, Chardin's generalized Sylvester framework, Mahatab--Sampath's multifactor scalar resultant identity, and Stacks tag 00U0 are all pertinent. Stacks, Section 10.143, Example 10.143.12 is especially close: it identifies the two-factor monic coefficient-product Jacobian with the Sylvester resultant and derives etaleness on the coprime locus. The manuscript correctly treats these as antecedents rather than independent reproduction.

- **Integration quality.** The resultant-side literature is integrated well; the graph/arithmetic side is not. Grossman--Kulkarni--Schochetman is a suitable direct source for unoriented incidence minors and Smith form, but Zaslavsky's all-negative signed-graph incidence framework should appear before it. The weighted row/column rescaling in Theorem 6.1 is elementary, yet the paper should locate it relative to signed-graphic/root-system matrices, not only signless incidence matrices. For Theorem 7.1, an integral list of characters, its saturation index, and gcds of maximal minors are naturally an arithmetic matroid. D'Adderio--Moci provides the right vocabulary; Ardila--Castillo--Henley is adjacent for type \(D\)-like lists \(e_i+e_j\). Neither is evidence of an exact collision, but omitting them leaves the theoretical framing incomplete.

- **Research gap argument.** The defensible gap is narrow: I did not locate a prior source stating the non-monic affine all-factor identity
  \[
  p_I(Dm_{\mathbf d})=\pm\Delta_{\mathbf d}\det K_I
  \]
  as a complete Plucker tensor with the manuscript's integral conventions, nor the primitive cyclicity and exact bad-prime support theorem for the weighted complete edge-character matrix. That negative finding is bounded, not a priority certificate. The paper should not present Theorem 4.1 as a new resultant or a new rank-locus theorem; it currently does not. It should present Theorem 6.1 as a corollary in a signed-incidence framework. For Theorem 7.1/Corollary 7.2, it should explicitly distinguish (a) classical Smith determinantal-divisor formalism, (b) the new modular corank lemma, and (c) the support classification.

#### Theoretical Framework

- **Appropriateness.** The determinant-line/torus-character framework is exactly the right invariant explanation for the bordered formulas. In particular, Corollary 5.1 is best understood as contraction of the Plucker covector by the vertical differentials, not as another ad hoc determinant expansion. The choice of the codimension-one torus \(\prod\lambda_i=1\) is canonical for the affine multiplication map.

- **Application depth.** The framework is fully applied through the semi-invariant case, but the paper stops just where the arithmetic becomes most informative. In Theorem 7.1, the cokernel is identified up to the index \(h(\mathbf e)\), while Corollary 7.2 identifies only its prime support. A stronger application would compute valuations or relate \(h\) explicitly to the arithmetic-matroid multiplicity of the complete signed-graphic list. Even one family displaying nontrivial \(p^a\)-valuation would clarify why the unresolved part is mathematically substantial rather than merely computational.

- **Alternative frameworks.** Three should be acknowledged. First, exterior-algebra/Grassmann duality gives a general lemma for maximal minors versus a kernel Plucker vector; this would isolate the multiplication-specific scalar. Second, the all-negative signed-graph incidence matrix is the natural home for Theorem 6.1. Third, arithmetic matroids or toric arrangements provide a standard framework for the lattice index and residual diagonalizable group in Theorem 7.1. These frameworks complement, rather than replace, the current determinant-line narrative.

#### Academic Argument Quality

- **Factual accuracy.** I found no fatal factual error in the highlighted results. The multidegree balance in Theorem 4.1, the incidence support criterion in Theorem 6.1, the modular rank argument in Theorem 7.1, and the root-partition/isogeny product in Corollary 8.1 are mutually consistent. The positive-characteristic statement in Corollary 8.1 correctly uses scheme length \(|\det W|\) while allowing fewer geometric points when the character isogeny has an inseparable part.

- **Argument logic.** The induction for Theorem 4.1 is logically economical: Lemma 3.1 separates the last factor, and the two-factor identity supplies the new pairwise resultants. The proof should nevertheless identify a general exterior-algebra lemma, because otherwise the coordinate bookkeeping can obscure that the Plucker conclusion is forced once the scalar and kernel are known. Theorem 7.1's modular argument is the strongest concise proof in the paper. Corollary 8.1's two finite contributions should continue to be kept separate: ordered partitions contribute the multinomial coefficient, while torus normalization contributes the isogeny degree.

- **Terminology precision.** Replace or qualify "collision divisor" by "pairwise inter-factor collision divisor." Replace "normaliser" by "normalising semi-invariant," "border function," or a formally defined term. In Theorem 7.1, call \(h(\mathbf e)\) the saturation index/arithmetic multiplicity as well as a gcd of maximal minors. In Corollary 8.1, "bad characteristic" should always mean a characteristic in which the chosen character isogeny is inseparable or the normalized map is not etale, not a characteristic in which the determinant identities fail.

#### Contribution to the Field

- **Incremental contribution.** Theorem 4.1 is a useful affine coordinate completion of classical scalar and rank results. Corollaries 5.1 and 5.2 are formal but valuable consequences. Theorem 6.1 is a neat weighted incidence corollary. Theorem 7.1/Corollary 7.2 is the principal candidate for a genuinely distinct theorem: it proves cyclic primitive torsion and exactly identifies its supporting primes. Corollary 8.1 packages classical root partitions and torus isogenies into a clean normalized-factorization degree statement.

- **Positioning.** The manuscript's Section 10.1 is close to the right positioning, but the same hierarchy needs to govern the abstract and conclusion. In particular, "complete Smith shape" should be glossed immediately as "all primitive invariant factors but the last are \(1\), and the prime support of the last is explicit"; otherwise readers may reasonably expect a closed formula for every invariant factor.

- **Overclaiming.** There is little overt overclaiming, and the repeated assurance caveats are commendable. The risk lies in aggregate presentation: a succession of named theorems can make formal contractions and classical specializations appear coequal with the arithmetic result. I recommend an explicit theorem-status table in the main text with columns "classical input," "formal consequence," and "candidate new content." Appendix D already contains much of the raw material.

#### Missing Key References

- **Thomas Zaslavsky**, "Signed graphs," *Discrete Applied Mathematics* **4**(1) (1982), 47-74, [doi:10.1016/0166-218X(82)90033-6](https://doi.org/10.1016/0166-218X(82)90033-6), with the 1983 erratum at volume 5, page 248. This is the foundational signed-graph/matroid setting for all-negative (unoriented/signless) incidence matrices and should be cited in the framing of Theorem 6.1.

- **Michele D'Adderio and Luca Moci**, "Arithmetic matroids, the Tutte polynomial and toric arrangements," *Advances in Mathematics* **232**(1) (2013), 335-367, [doi:10.1016/j.aim.2012.09.001](https://doi.org/10.1016/j.aim.2012.09.001). This supplies the natural language for gcds of minors, saturation indices, and arithmetic multiplicities of integral character lists relevant to Theorem 7.1.

- **Federico Ardila, Federico Castillo, and Michael Henley**, "The Arithmetic Tutte Polynomials of the Classical Root Systems," *International Mathematics Research Notices* **2015**(12) (2015), 3830-3877, [doi:10.1093/imrn/rnu050](https://doi.org/10.1093/imrn/rnu050). This is adjacent rather than an exact antecedent, but it is relevant to the equal-weight \(e_i+e_j\), signed-graph, and type-\(D\) aspect of the edge-character list.

- **Winfried Bruns and Udo Vetter**, *Determinantal Rings*, Lecture Notes in Mathematics 1327, Springer, 1988, [doi:10.1007/BFb0080378](https://doi.org/10.1007/BFb0080378), or an equivalent standard source on maximal-minor ideals and determinantal divisors. This would strengthen the general determinant-ideal framing around Section 4.1; it is not an exact antecedent to Theorem 4.1.

- As adjacent context only, the authors may also consider **Fan R. K. Chung and Robert P. Langlands**, "A combinatorial Laplacian with vertex weights," *Journal of Combinatorial Theory, Series A* **75**(2) (1996), 316-327, [doi:10.1006/jcta.1996.0080](https://doi.org/10.1006/jcta.1996.0080), and **Dino J. Lorenzini**, "Arithmetical graphs," *Mathematische Annalen* **285** (1989), 481-501. These are not collisions with Theorem 6.1 or 7.1, but they help locate vertex-weighted graph arithmetic and cokernel invariants.

### Questions for Authors

1. Can the authors state and prove a general exterior-algebra lemma that separates Theorem 4.1 into (i) a classical/common scalar factor, (ii) identification of the kernel Plucker line, and (iii) one orientation chart? Precisely which of these three ingredients do they claim as new?

2. Have the authors searched the signed-graph literature using the all-negative signed-incidence formulation, rather than only "signless incidence matrix" terminology? How does Theorem 6.1 specialize or extend Zaslavsky's determinant/matroid framework and the later Grossman--Kulkarni--Schochetman formulas?

3. Can \(h(\mathbf e)\) be expressed in closed form, or can its valuations \(v_p(h)\) be computed? If not, can the authors give examples where the same prime support yields different valuations, thereby demonstrating the residual problem explicitly?

4. What is the arithmetic matroid represented by the primitive complete edge-character list? Is \(h(\mathbf e)\) exactly its full-rank multiplicity, and does arithmetic-matroid duality or a signed-graphic representation recover any part of Theorem 7.1 or Corollary 7.2?

5. Is "normaliser" intended as a new technical term? If so, please define it before first use and distinguish it from the normalizer of a subgroup/action. If not, would "normalising semi-invariant" be clearer?

6. In Corollary 8.1, can the authors cite a standard diagonalizable-group or torus-isogeny source for the identification of the kernel with the Cartier dual of \(\operatorname{coker} W\), rather than leaving this entirely implicit behind the Stacks etale reference?

7. Do the authors know whether the affine Plucker identity has appeared under the language of cofactors of generalized Sylvester/Koszul matrices, approximation complexes, or determinant-of-complexes constructions? The present bounded negative search is useful but not yet enough for a priority claim.

### Minor Issues

- At lines 146-159, keep the Sylvester/resultant sign convention visible when the two-factor input is invoked later. A short cross-reference at the induction step would help readers audit the global sign.

- At lines 172-175, "perfectness" is too compressed for readers outside commutative algebra. Say explicitly that the cited work concerns perfect Jacobian ideals and their resolutions, not the maximal-minor identity proved here.

- The Mahatab--Sampath paper title suggests a cyclotomic specialization, while the manuscript uses its appendix for a general multifactor resultant identity. Give the exact theorem locator each time it is invoked so that the scope is not misunderstood.

- In Theorem 6.1, if the unique tree component is an isolated vertex, the displayed product \(\prod_i d_i^{\deg_H(i)-1}\) contains \(d_i^{-1}\); the bipartition imbalance cancels it. Add a sentence noting this cancellation, or rewrite the formula componentwise so that integrality is manifest.

- In Corollary 6.2, state whether an isolated vertex is allowed as a tree and how its bipartition is chosen (one part empty).

- Around lines 890-918, move the definition of \(h(\mathbf e)\) into the theorem statement or call it the full-rank determinantal divisor. This will make clear at a glance which part of the displayed Smith form is computed and which part remains symbolic.

- At lines 991-993 and again in the conclusion, emphasize that Corollary 7.2 determines prime support only; it does not determine exponents in \(h\).

- At lines 1030-1032, "generic scheme degree" is understandable, but "degree of the dominant generically finite morphism (equivalently, generic fibre length)" is more standard.

- In Corollary 8.1, distinguish the finite constant root-partition cover from the diagonalizable kernel even more explicitly in positive characteristic; only the latter is responsible for the inseparable loss of geometric points described there.

- The term "residual group scheme" should be defined once as the kernel of the character isogeny, with character group \(\operatorname{coker} W\).

- Appendix D is useful, but a compact version should be moved into the introduction. The contribution boundary is central enough that it should not depend on an appendix.

- The author and affiliation placeholders (lines 3-8 and 1384 onward) must of course be resolved before submission; the AI-assistance statement should remain separate from mathematical verification and authorship responsibility.
