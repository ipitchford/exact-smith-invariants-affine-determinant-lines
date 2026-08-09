# Argument Blueprint

## Central thesis

For multiplication of labelled binary forms, the complete determinant line of
the coefficient differential factors over \(\mathbb Z\) into the product of
the pairwise-collision resultant divisor and the Plücker line of the
product-one scaling torus.  Multi-bordering pairs this torus line with an
integer character matrix.  For resultant normalisers, weighted graph incidence
then determines the character minors, Smith invariants, residual group scheme,
bad characteristics and generic degree.

## Claim–evidence–reasoning chains

### C1. The all-factor maximal-minor tensor is
\(\varepsilon_{\mathbf d}\Delta_{\mathbf d}\operatorname{Pl}(K)\)

**Evidence**

- Self-contained two-factor signed maximal-minor theorem, with provenance to
  the parent candidate.
- Block-composition lemma with the explicit factor \((-1)^{k-2}\).
- Exact multiplicativity
  \(\operatorname{Res}(\prod_{i<k}A_i,A_k)=\prod_{i<k}R_{ik}\).
- Determinant-one change from inherited/lifted kernel rows to the standard
  product-one torus basis.
- Complete symbolic coordinates for ordered mixed-degree fixtures.

**Reasoning**

The determinant line is multiplicative under the factored multiplication map.
The inner scalar supplies previous pairwise resultants, the outer two-factor
scalar supplies all resultants involving \(A_k\), and the kernel wedge carries
the missing dimensions.  The orientation recurrence solves to the displayed
closed exponent.

**Rebuttal / failure condition**

A wrong block-order sign, resultant convention or kernel-basis determinant
would invalidate the formula.  The proof displays each term, and mixed ordered
degree cases discriminate a multiset-only sign rule.

### C2. The rank-loss divisor is exactly pairwise collision

**Evidence**

- Ideal identity
  \(I_{D+1}(Dm)=\Delta_{\mathbf d}I_{k-1}(K)\).
- On nonzero factors, \(K\) has full rank.
- On the pairwise-coprime locus, reduction modulo each \(A_i\) shows that every
  kernel vector is a torus scaling direction.

**Reasoning**

No extra generic divisor can occur because the complete maximal-minor vector is
known.  At the generic point of each resultant divisor, the other factors and
the kernel minors are units, so multiplicity is one.

**Qualification**

Intersections and zero-factor strata retain additional scheme structure through
\(I_{k-1}(K)\).  The affine determinantal ideal is not asserted to be globally
principal.

### C3. Multi-bordering replaces degree difference by a character determinant

**Evidence**

- Laplace expansion along multiplication rows.
- The all-factor complementary minors.
- Cauchy–Binet for \(KG^T\).
- Euler equations \(\delta_bg_a=W_{ab}g_a\) for semi-invariants.
- Direct FLINT checks with resultant borders and \(\det W=1,2\).

**Reasoning**

Every deleted-column set pairs a Plücker coordinate of the kernel with the
matching gradient minor.  Cauchy–Binet recombines the sum into the determinant
of the vertical torus Jacobian.  Semi-invariance diagonalises the functions and
leaves the integer character determinant.

**Rebuttal / failure condition**

If the vertical character matrix is singular, borders fail to recover every
missing torus direction.  Nonzero \(\det W\) is necessary but does not remove
the collision factor \(\Delta\).

### C4. Resultant-character minors are weighted incidence minors

**Evidence**

- Scaling law
  \(R_{ij}\mapsto\lambda_i^{d_j}\lambda_j^{d_i}R_{ij}\).
- Augmentation by the all-ones row.
- Column scaling by \(d_i\) and row extraction of \(d_id_j\).
- Classical signless-incidence minor theory.
- Exhaustive bounded exact graph checks.

**Reasoning**

The weighted edge row becomes an unweighted incidence row after diagonal
scaling.  A square incidence block is nonsingular for an odd-unicyclic
component and contributes absolute determinant two.  A tree requires the
bordering degree row and contributes its bipartite balance.  With \(k-1\)
edges, nonzero determinant forces exactly one tree component and all other
components odd unicyclic.

**Antecedent boundary**

Incidence minors are classical.  The candidate contribution is their weighted
identification with resultant characters and the ensuing factorisation
arithmetic.

### C5. The complete-edge character matrix has Smith form
\(\operatorname{diag}(g,\ldots,g,gh)\)

**Evidence**

- The explicit graph-minor gcd \(h\) for primitive degrees.
- Modular kernel analysis: rank at least \(k-2\) over every \(\mathbb F_p\).
- Determinantal-divisor characterisation of Smith invariants.
- Exact Smith calculations through five vertices and degrees at most three.

**Reasoning**

Rank at least \(k-2\) modulo every prime means no prime divides the gcd of all
\((k-2)\)-minors, hence the first \(k-2\) primitive Smith entries are one.
The final entry is the gcd of maximal minors.  A common degree factor multiplies
every matrix entry and therefore every Smith entry.

**Qualification**

The graph-minor gcd is an exact finite formula.  Only its prime support receives
a shorter residue criterion; no closed formula for all \(p\)-adic valuations is
claimed.

### C6. Smith data determines bad characteristics

**Evidence**

- For primitive degrees, the character matrix has a nonzero modular kernel
  precisely under the stated residue conditions.
- For odd \(p\): only a two-element nonzero support with equal residues
  survives.
- For \(p=2\): a kernel survives precisely when the number of odd degrees is
  even.

**Reasoning**

A prime divides the final primitive Smith invariant exactly when maximal rank
fails modulo that prime.  The edge equations reduce the kernel to at most one
parameter, making the residue classification exhaustive.

### C7. The generic scheme degree is
\(|\det W|D!/\prod_i d_i!\)

**Evidence**

- Classical labelled root-partition count.
- A full-rank character matrix defines a finite torus isogeny of scheme degree
  \(|\det W|\).
- The multi-border formula identifies the étale locus.

**Reasoning**

Each projective factorisation supports a torsor of affine scalings.  Generic
nonzero normaliser values intersect that torus in the kernel of the character
isogeny.  Root partitions and torus solutions multiply.

**Qualification**

This is a scheme degree over an algebraically closed field.  If the
characteristic divides \(\det W\), the kernel can be nonreduced, so reduced
geometric points need not equal the degree.

## Counterarguments and responses

### “The theorem is only polynomial CRT.”

CRT determines a monic square determinant and directly anticipates the scalar
\(\Delta\).  It removes the affine scaling directions.  The paper's exact
object is the rectangular non-monic Plücker tensor and its borders.  The scalar
antecedent is credited in the abstract, introduction and related-work section.

### “Multidegrees already force the answer.”

Degree matching can rule out an extra scalar once divisibility is established.
It does not identify the kernel tensor, prove the block-order sign, or yield the
multi-border contraction.  The determinant-line induction supplies those data.

### “Full-rank characters give a Keller map.”

They give a generically finite étale chart only off the collision and
normaliser-zero divisors.  A Keller map on affine space also requires a global
slice isomorphic to affine space.  That recognition problem is not solved here.

### “Two symbolic backends are independent reproduction.”

They use different polynomial and determinant engines but the same producer
specification.  They are cross-implementation checks, not independent
mathematical reproduction.

## Logical dependency order

1. Self-contained two-factor identity (the parent candidate supplies
   provenance, not an unproved dependency).
2. Composition sign lemma.
3. All-factor Plücker identity.
4. Determinantal ideal and generic kernel.
5. Multi-border contraction.
6. Character determinant.
7. Weighted graph-minor theorem.
8. Smith form and modular criterion.
9. Generic degree and étaleness.

The paper must not use a later item to justify an earlier one.
