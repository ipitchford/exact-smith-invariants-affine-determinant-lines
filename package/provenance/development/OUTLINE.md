# Manuscript Architecture and Evidence Map

## Structure selection

The paper uses an adapted theoretical-mathematics structure.  It retains the
theoretical-paper pattern's background, extension, implications and limitations,
but replaces generic “critical analysis” sections with definitions,
theorem–proof sequences and exact arithmetic corollaries.

**Target main-text length:** 7,000–7,500 words, excluding references,
declarations and technical appendices.

## Proposed outline

### Front matter — approximately 400 words

- Title and anonymous author/affiliation placeholders.
- English abstract, 180–230 words.
- Traditional Chinese abstract, independently written, 300–500 characters.
- Six keywords in each language.
- Status note: research-stage preprint; producer checks only.

**Evidence:** final theorem package and assurance record.

### 1. Introduction — approximately 600 words

1. State the rectangular multiplication problem and the scaling-dimension gap.
2. State the two-factor determinant-line theorem and supply its root-evaluation
   proof in a self-contained appendix.
3. State the all-factor question and why scalar determinants are insufficient.
4. Give a numbered contributions list:
   - all-factor signed Plücker theorem over \(\mathbb Z\);
   - multi-border/character determinant;
   - weighted graph-minor theorem;
   - Smith form, bad primes and generic degree.
5. State assurance and scope exclusions.

**Evidence:** parent theorem; Stage-1 proof; bounded novelty audit.

**Transition:** from motivation to the exact coordinate and orientation choices
needed for a sign-sensitive theorem.

### 2. Conventions and classical antecedents — approximately 700 words

2.1 Binary-form coefficient convention and ascending Sylvester resultant.  
2.2 Source, target and determinant-line dimensions.  
2.3 Product-one scaling torus and its ordered infinitesimal basis.  
2.4 Signed complementary-minor convention.  
2.5 Classical scalar shadows: CRT determinant, Koszul/Sylvester divisibility,
projective multiplication.  
2.6 Precise novelty boundary.

**Evidence:** Mahatab–Sampath; Chardin; Jouanolou; Breiding–Kohn–Sturmfels;
Kurth; parent conventions.

**Transition:** the scalar antecedents do not retain the affine scaling kernel,
so an oriented composition lemma is required.

### 3. Determinant-line composition — approximately 700 words

3.1 Define the Plücker scalar of a full-row-rank matrix relative to an ordered
kernel basis.  
3.2 State the block-composition lemma.  
3.3 Prove the factor \((-1)^{t_1}\) on canonical adapted matrices.  
3.4 Prove invariance under basis changes.  
3.5 Record the determinant-one torus-basis transformation used in induction.

**Evidence:** self-contained proof; mixed-degree sign fixtures as non-proof
sanity checks.

**Negative control addressed:** a sign depending only on the unordered degree
multiset is false.

### 4. The all-factor Plücker theorem — approximately 1,050 words

4.1 State the theorem for all \(k\ge2\) over \(\mathbb Z\):

\[
 (-1)^{\sum I}\det(Dm)_{\widehat I}
 =\varepsilon_{\mathbf d}\Delta_{\mathbf d}\det K_I.
\]

4.2 Display the closed orientation exponent.  
4.3 Verify reduction to the two-factor theorem.  
4.4 Induct by factoring \(k\)-fold multiplication through \((k-1)\)-fold and
two-factor multiplication.  
4.5 Use exact resultant multiplicativity.  
4.6 Derive the sign recurrence and solve it.  
4.7 Give the explicit \(k=3\) theorem and mixed-order signs.  
4.8 Derive the maximal-minor/Fitting ideal and generic kernel description.

**Evidence:** integral induction; parent base; exact SymPy/FLINT receipts.

**Claim qualification:** multiplicity one is asserted at the generic point of
each collision divisor, not as a claim that the affine determinantal ideal is
globally principal.

### 5. Multi-border contraction — approximately 600 words

5.1 Append \(k-1\) gradient rows.  
5.2 Laplace-expand with the fixed zero-based sign convention.  
5.3 Apply Cauchy–Binet to \(KG^T\).  
5.4 State the vertical torus-Jacobian formula.  
5.5 Specialise to semi-invariants and the integer character determinant.  
5.6 Recover the rank-one degree-difference principle.

**Evidence:** determinant proof; two direct FLINT resultant-border checks with
\(\det W=1,2\).

### 6. Resultant characters and graph minors — approximately 900 words

6.1 Compute the edge character
\(\chi_{ij}(u)=d_ju_i+d_iu_j\).  
6.2 Append the all-ones row and eliminate the last cocharacter coordinate.  
6.3 Scale columns and edge rows to obtain a signless incidence matrix.  
6.4 State and prove the complete \((k-1)\)-edge minor theorem:
one tree component plus odd-unicyclic components.  
6.5 Derive the spanning-tree bipartite-balance formula and star corollary.  
6.6 Explain what is classical incidence theory and what is the weighted
factorisation-specific bridge.

**Evidence:** Grossman–Kulkarni–Schochetman; Hessert–Mallik; 84,502 exact tree
and general graph-minor checks.

### 7. Smith normal form and bad characteristics — approximately 850 words

7.1 Define the complete-edge character matrix, common gcd \(g\), primitive
degrees \(e_i\), and maximal-minor index \(h\).  
7.2 Prove modular kernel dimension at most one.  
7.3 Deduce primitive Smith form \(\operatorname{diag}(1,\ldots,1,h)\).  
7.4 Restore the common factor to obtain
\(\operatorname{diag}(g,\ldots,g,gh)\).  
7.5 Prove the exact bad-prime support criterion by the cases
\(|S|=1,2,\ge3\) and \(p=2\).  
7.6 Work examples \((1,1,1)\), \((1,1,2)\), and \((1,1,1,1)\).  
7.7 State that valuations are determined by the finite graph-minor gcd; no
shorter formula is claimed.

**Evidence:** self-contained modular proof; 351 exact Smith/bad-prime cases;
classical SNF/incidence context.

### 8. Normalised factorisation degree and étaleness — approximately 450 words

8.1 Work over an algebraically closed field with generic nonzero normaliser
values.  
8.2 Count labelled root partitions.  
8.3 Multiply by the torus-isogeny scheme order \(|\det W|\).  
8.4 State
\(|\det W|D!/\prod_i d_i!\).  
8.5 Separate scheme degree, reduced points and étaleness in bad
characteristic.

**Evidence:** root-factorisation argument; Breiding–Kohn–Sturmfels; Smith
arithmetic and multi-border theorem.

### 9. Exact computational evidence — approximately 400 words

9.1 Explain the independent implementation layers without calling them
independent reproduction.  
9.2 Tabulate cases, coordinate counts, negative controls and dependency
versions.  
9.3 Record script and normal/optimized receipt SHA-256 values.  
9.4 State the limitations of producer-side exact checking.

**Evidence:** frozen Stage-1 scripts and receipts.

### 10. Limitations and research programme — approximately 350 words

10.1 Parent and follow-up assurance status.  
10.2 Bounded-search and implicit-prior-art risk.  
10.3 Deferred kernel-presentation and \(p\)-adic valuation compression.  
10.4 Deeper collision strata/subresultants.  
10.5 Arbitrary normalisers and global affine-slice recognition.  
10.6 Keller/Hessian applications explicitly deferred.

**Evidence:** Stage-1 adversarial review and open-gap analysis.

### 11. Conclusion — approximately 200 words

- Restate the determinant-line factorisation.
- Explain the Smith-normal-form replacement for degree difference.
- Identify independent reproduction and specialist priority review as the next
  scientific gates.

### Declarations — excluded from main word count

- Data and code availability.
- Ethics declaration.
- Author contributions using CRediT placeholders.
- Conflict of interest.
- Funding acknowledgment.
- AI-use disclosure.

### Appendices — excluded from main word count

A. Orientation and indexing table.  
B. Verification matrix, negative controls and hashes.  
C. Formalisation blueprint for Lean.  
D. Full bounded novelty matrix.

## Evidence-flow summary

\[
 \text{two-factor base}
 \longrightarrow
 \text{composition sign}
 \longrightarrow
 \text{all-factor Plücker tensor}
 \longrightarrow
 \text{multi-border character determinant}
\]

\[
 \text{resultant edge characters}
 \longrightarrow
 \text{signless incidence minors}
 \longrightarrow
 \text{Smith invariants and arithmetic}
 \longrightarrow
 \text{generic degree/étaleness}.
\]

No arrow reaches affine-space recognition or Keller/Hessian conclusions; those
remain outside the manuscript's proved scope.
