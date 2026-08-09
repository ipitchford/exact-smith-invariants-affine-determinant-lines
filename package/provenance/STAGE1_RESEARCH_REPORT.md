# Determinant Lines and Character Lattices of Binary-Form Factorisation Maps

> **Historical Stage-1 record.** This report records the initial research
> boundary and is retained unchanged below for provenance. The focused
> exact-object antecedent audit in `STAGE1_ANTECEDENT_REAUDIT.md` supersedes its
> literature and contribution-boundary assessment, but not its mathematical
> derivations or computational receipts.

## Final Stage-1 research report

**Date:** 9 August 2026  
**Status:** research-stage, producer-verified draft; not independently reproduced,
formally verified, peer reviewed, or released  
**Relationship to prior work:** separate follow-up to the immutable
*Bordered Jacobian Foundations* candidate.  The parent Evidence Press venue and
this follow-up share a producer/research process; public availability is not
independent scholarly endorsement.

## Abstract

Multiplication of two binary forms has a one-dimensional scaling kernel, and
the signed maximal minors of its coefficient Jacobian equal a resultant times
that kernel vector.  This report develops the corresponding theory for an
arbitrary number of factors.  For positive degrees
\(\mathbf d=(d_1,\ldots,d_k)\), every maximal minor of the differential of
\((A_1,\ldots,A_k)\mapsto\prod_iA_i\) is shown, over \(\mathbb Z\), to be
the product of all pairwise resultants multiplied by the corresponding
Plücker coordinate of the \((k-1)\)-dimensional product-one scaling torus.
An explicit orientation formula is obtained by induction.  Bordering by
\(k-1\) functions then yields a determinant equal to the collision divisor
times their vertical torus Jacobian.  For semi-invariants, this vertical
Jacobian is an integer character determinant.

For normalisers built from pairwise resultants, the character matrix reduces
to a weighted unoriented graph-incidence matrix.  This gives a spanning-tree
determinant formula, a more general tree/odd-unicyclic component formula, and
the Smith form of the full resultant-character lattice.  The latter identifies
the residual diagonalizable group and all primes at which the primitive
character lattice loses rank.  The generic scheme degree is
\(|\det W|D!/\prod_i d_i!\).

The scalar product-of-resultants determinant has classical antecedents in
polynomial Chinese remainder and generalized Sylvester theory.  The candidate
contribution is therefore the non-monic determinant-line refinement and its
character-lattice consequences, not the scalar alone.  Two exact symbolic
backends and a separate integer-matrix suite support the results, but remain
producer-side evidence.

## 1. Introduction

Let \(V_d\) denote the rank-\(d+1\) module of binary forms of degree \(d\).
For two factors, coefficient multiplication

\[
 m_{r,s}:V_r\times V_s\longrightarrow V_{r+s},\qquad (A,B)\longmapsto AB,
\]

has source dimension one greater than its target.  Its generic kernel is the
infinitesimal scaling direction \((A,-B)\).  The parent candidate proves that
the complete signed maximal-minor vector of \(Dm_{r,s}\) is a fixed sign times
\(\operatorname{Res}(A,B)(A,-B)\) (Evidence Press, 2026).  Bordering this
rectangular matrix by the differential of a bihomogeneous function pairs the
border with the missing scaling direction.  The familiar degree difference is
the resulting one-dimensional character.

The natural question is whether this is a rank-one accident.  For
\(k\) factors with degrees \(d_i\), the source exceeds the target by
\(k-1\), exactly the dimension of the torus

\[
 T=\{(\lambda_1,\ldots,\lambda_k):\lambda_1\cdots\lambda_k=1\}.
\]

Root collisions between distinct factors are detected by pairwise resultants.
These observations suggest a determinant-line factorisation into a collision
divisor and a torus Plücker tensor.  The present research asks:

1. Does that factorisation hold for all positive degree vectors over
   \(\mathbb Z\), with an explicit sign?
2. Does multi-bordering replace the scalar degree difference by a character
   determinant?
3. What lattice is generated when the borders are pairwise resultants?
4. Which parts of this picture are classical, and which exact statements were
   not located in a bounded source search?

The answer to the first three questions is affirmative.  The literature answer
is deliberately qualified.  Mahatab and Sampath (2015) prove a product of
pairwise resultants as the determinant of a canonical polynomial Chinese
remainder map for monic factors.  Chardin's generalized Sylvester analysis gives
resultant divisibility and gcd statements for relevant maximal minors (Chardin,
1993).  Projective polynomial multiplication and root-partition degrees are
also classical (Breiding et al., 2024).  The defensible candidate contribution
is the exact non-monic Plücker identity, its orientation and multi-border
contraction, and the weighted character-lattice synthesis.

The report stops before the programme's global affine-geometry stages.  An
étale factorisation chart is not automatically an affine-space slice or a
Keller map.  No classification of arbitrary normalisers, affine slices, Keller
maps, or Hessian constructions is claimed.

## 2. Method

### 2.1 Algebraic strategy

The primary method is proof over the universal integer coefficient ring.
The two-factor identity serves as the base case.  The \(k\)-factor map is
factored through multiplication of the first \(k-1\) factors followed by a
two-factor multiplication.  A complementary-minor composition lemma tracks the
kernel wedge and orientation.  Resultant multiplicativity supplies the new
pairwise collision factors.

The multi-border identity is then obtained by Laplace expansion and
Cauchy–Binet.  Character determinants follow from the Euler equations for torus
semi-invariants.

For the character lattice, each pairwise resultant is identified with an edge
of the complete graph.  Elementary row and column scalings reduce character
minors to bordered minors of the unoriented incidence matrix.  Classical graph
incidence results then determine all maximal minors.  Determinantal divisors and
a modular rank argument yield the Smith form.

### 2.2 Computational strategy

The proof predictions were checked by three exact programs:

1. a SymPy/Berkowitz implementation that constructs the multiplication
   differential, Sylvester resultants and torus kernel independently and checks
   every Plücker coordinate in seven default degree vectors;
2. a separate python-flint implementation using `fmpz_mpoly` and
   fraction-free Bareiss determinants for mixed three-factor cases, four linear
   factors and direct resultant-border determinants; and
3. an integer-matrix suite checking tree determinants, arbitrary maximal graph
   minors, Smith forms and modular bad-prime criteria.

All computations are deterministic and exact.  Normal and `python -O` receipts
are byte-identical, and deliberate negative controls must fail.  These are
structural producer checks, not statistical evidence, formal verification, or
independent reproduction.

### 2.3 Literature strategy

The search followed object identity rather than keyword similarity.  It covered
polynomial CRT determinants, resultants and generalized Sylvester matrices,
binary resultant Jacobian ideals, projective factorisation quotients, torus
normalisation, and incidence-matrix minors/Smith forms.  Primary papers,
publisher records and the parent full-text audit were preferred.  A negative
search finding is reported only as “not found in the bounded search.”  The
parent Evidence Press release is producer-supplied context, not an independent
source validating the theorem.

### 2.4 Validity criteria

The algebraic claims were required to satisfy:

* recovery of the parent formula when \(k=2\);
* exact agreement for every Plücker coordinate, including zero coordinates;
* mixed block-order tests that distinguish orientation laws;
* first-power, not merely divisibility, of every pairwise resultant;
* normal and optimized-mode receipt parity;
* negative controls for each structural factor; and
* explicit separation between proven local determinant statements and open
  global affine geometry.

## 3. The all-factor determinant line

### 3.1 Coordinates and torus kernel

Write

\[
 A_i=\sum_{j=0}^{d_i}a_{i,j}X^{d_i-j}Y^j,qquad
 D=\sum_i d_i.
\]

The multiplication map

\[
 m_{\mathbf d}:\prod_{i=1}^kV_{d_i}\longrightarrow V_D
\]

has source dimension \(N=D+k\), target dimension \(n=D+1\), and generic
kernel rank \(t=k-1\).  Source coordinates are ordered by factor and then by
coefficient.  Let \(M=Dm_{\mathbf d}\).

For \(b=1,\ldots,k-1\), let

\[
 \kappa_b=(0,\ldots,A_b,\ldots,0,-A_k),
\]

and let \(K\) be the matrix with rows \(\kappa_b\).  For a \(t\)-element
set \(I\) of zero-based source columns, define

\[
 p_I(M)=(-1)^{\sum_{i\in I}i}\det M_{\widehat I}.
\]

Finally, put

\[
 \Delta_{\mathbf d}=
 \prod_{1\le i<j\le k}\operatorname{Res}(A_i,A_j),
\]

using the ascending-coefficient Sylvester convention of the parent candidate.

### 3.2 Main theorem

**Theorem 1 (all-factor Plücker identity).** For all \(k\ge2\) and positive
degree vectors \(\mathbf d\), the following identities hold over
\(\mathbb Z\):

\[
 p_I(M)=\varepsilon_{\mathbf d}\Delta_{\mathbf d}\det K_I,
 \qquad |I|=k-1,
\]

where

\[
 \varepsilon_{\mathbf d}=(-1)^{E(\mathbf d)},\qquad
 E(\mathbf d)=
 \sum_{i<j}d_i(d_j+1)+\binom{k+1}{2}+1.
\]

Thus every maximal minor contains the same collision scalar, while its
remaining coordinate is exactly the corresponding coordinate of the torus
kernel wedge.

For \(k=3\), the sign is

\[
 (-1)^{d_1(d_2+1)+(d_1+d_2)(d_3+1)+1}.
\]

This predicts signs \(-,+,-\) for the ordered degree vectors
\((1,1,2)\), \((1,2,1)\), and \((2,1,1)\), respectively, as confirmed by
both symbolic implementations.

### 3.3 Composition sign lemma

The sign is the delicate part of the induction.  The required matrix lemma may
be audited on canonical adapted matrices.

Let an inner full-row-rank matrix have shape \(r\times(r+t_1)\), and extend it
by an identity block of width \(q\).  Compose this block map with an outer
full-row-rank matrix of corank one.  Order the composite kernel by the inherited
\(t_1\) directions followed by a lift of the outer direction.  Then the
composite Plücker scalar is

\[
 c_M=(-1)^{t_1}c_Pc_L.
\]

To see the sign explicitly, use bases in which

\[
 P=(I_r\;0_{r\times t_1})
\]

and the outer map is \((I_{r+q-1}\;0)\), with its kernel in the last outer
coordinate.  In the fixed block source order, the only nonzero inner Plücker
coordinate deletes columns
\(r,\ldots,r+t_1-1\), so

\[
 c_P=(-1)^{t_1r+\binom{t_1}{2}}.
\]

The only nonzero outer coordinate deletes column \(r+q-1\), so

\[
 c_L=(-1)^{r+q-1}.
\]

The composite deletes the inherited kernel columns and the final lifted
column.  Hence

\[
 c_M=(-1)^{t_1r+\binom{t_1}{2}+r+t_1+q-1}
     =(-1)^{t_1}c_Pc_L.
\]

Invertible changes to adapted source, intermediate and target bases multiply
both sides by the same determinant factors, so the ratio is invariant.  This
proves the composition sign for the general full-rank locus, and the resulting
universal polynomial identity extends over \(\mathbb Z\).

### 3.4 Inductive proof

Assume the theorem for the first \(k-1\) factors.  Put

\[
 D'=\sum_{i<k}d_i,qquad B=\prod_{i<k}A_i,
\]

and factor

\[
 \prod_iV_{d_i}
 \longrightarrow V_{D'}\times V_{d_k}
 \longrightarrow V_D.
\]

The outer two-factor theorem contributes

\[
 (-1)^{D'(d_k+1)}\operatorname{Res}(B,A_k).
\]

In the chosen Sylvester convention,

\[
 \operatorname{Res}(B,A_k)=
 \prod_{i<k}\operatorname{Res}(A_i,A_k).
\]

An inherited kernel basis is

\[
 \eta_b=(0,\ldots,A_b,\ldots,-A_{k-1},0),
 \quad b=1,\ldots,k-2,
\]

and a lift of the outer kernel is

\[
 \ell=(0,\ldots,A_{k-1},-A_k).
\]

The standard rows satisfy

\[
 \kappa_b=\eta_b+\ell\ (b<k-1),\qquad \kappa_{k-1}=\ell.
\]

This row change has determinant one.  The composition lemma gives

\[
 e_k\equiv e_{k-1}+D'(d_k+1)+(k-2)\pmod2.
\]

The stated exponent satisfies this recurrence because its increment is
\(D'(d_k+1)+k\), congruent to the displayed expression.  Resultant
multiplicativity completes the scalar induction.

### 3.5 Rank-loss divisor and Fitting ideal

The coordinate identities imply the exact ideal equality

\[
 I_{D+1}(Dm_{\mathbf d})
 =\Delta_{\mathbf d}I_{k-1}(K).
\]

On the locus of nonzero factors, \(K\) has full row rank.  On the
pairwise-coprime locus the kernel of \(Dm\) is precisely the torus tangent
space.  Indeed, if

\[
 \sum_iH_i\prod_{j\ne i}A_j=0,
\]

then reduction modulo \(A_i\) gives \(H_i=c_iA_i\), and the original
equation gives \(\sum_i c_i=0\).  Consequently, the divisorial rank-loss
locus is exactly \(\Delta=0\).  At the generic point of each pairwise-collision
divisor—where the remaining pairwise resultants are nonzero and \(K\) has full
rank—the corresponding resultant appears with multiplicity one.  Intersections
and zero-factor strata can carry additional scheme structure through the
nonprincipal factor \(I_{k-1}(K)\); the theorem does not erase that distinction.

## 4. Multi-bordering and character determinants

Let \(g_1,\ldots,g_t\) be source polynomials and let \(G\) be their gradient
matrix.  Define the torus derivations

\[
 \delta_b=\sum_jK_{b,j}\frac{\partial}{\partial x_j}.
\]

Laplace expansion along the \(n\) multiplication rows gives a sum over deleted
sets \(I\).  Substituting Theorem 1 and applying Cauchy–Binet to \(K G^T\)
gives the following.

**Theorem 2 (multi-border contraction).**

\[
 \det\begin{pmatrix}M\\G\end{pmatrix}
 =(-1)^{nt+\binom t2}\varepsilon_{\mathbf d}
   \Delta_{\mathbf d}\det(\delta_b g_a)_{a,b=1}^t.
\]

If \(g_a\) is a semi-invariant with character row \(W_{a*}\), then

\[
 \delta_bg_a=W_{ab}g_a
\]

and therefore

\[
 \det D(m_{\mathbf d},g_1,\ldots,g_t)
 =(-1)^{nt+\binom t2}\varepsilon_{\mathbf d}
   \Delta_{\mathbf d}\det(W)\prod_ag_a.
\]

For \(k=2\), \(W\) is a one-entry matrix.  Its entry is the difference of
the two scaling degrees, exactly recovering the parent degree-difference
principle.

## 5. The resultant-character graph

### 5.1 Edge characters

The pairwise resultant \(R_{ij}\) transforms as

\[
 R_{ij}\mapsto\lambda_i^{d_j}\lambda_j^{d_i}R_{ij}.
\]

Thus its character on \(\sum_i u_i=0\) is

\[
 \chi_{ij}(u)=d_ju_i+d_iu_j.
\]

Associate \(R_{ij}\) with edge \(ij\) of the complete graph.  For a set
\(H\) of \(k-1\) edges, let \(W_H\) be the square character matrix after
eliminating \(u_k\).

### 5.2 General graph-minor theorem

**Theorem 3 (weighted incidence formula).** The determinant of \(W_H\) is
nonzero only if \(H\) has exactly one tree component and every other component
is odd unicyclic.  If \(H\) has \(c\) components, if \(P\sqcup Q\) is the
bipartition of its tree component, and \(\deg_H(i)\) is vertex valence, then

\[
 |\det W_H|=
 2^{c-1}
 \left|\sum_{i\in P}d_i-\sum_{j\in Q}d_j\right|
 \prod_i d_i^{\deg_H(i)-1}.
\]

When \(H\) is a spanning tree, this reduces to

\[
 |\det W_H|=
 \left|\sum_{i\in P}d_i-\sum_{j\in Q}d_j\right|
 \prod_i d_i^{\deg_H(i)-1}.
\]

To prove the theorem, represent each edge character in the full
\(k\)-coordinate lattice and append an all-ones row.  Multiply column \(i\)
by \(d_i\), then factor \(d_id_j\) from edge row \(ij\).  This yields

\[
 |\det W_H|=
 \left(\prod_i d_i^{\deg_H(i)-1}\right)
 \left|\det\begin{pmatrix}B_H\\d_1\ \cdots\ d_k\end{pmatrix}\right|,
\]

where \(B_H\) is the signless incidence matrix.  An odd-unicyclic component
has incidence determinant of absolute value two; a tree bordered by the degree
row has determinant equal to its bipartite degree balance.  Other component
patterns have deficient rank.  This uses classical unoriented-incidence theory
(Grossman et al., 1995; Hessert & Mallik, 2022); the weighted character
reduction is the factorisation-specific step.

### 5.3 Full Smith form

Let \(W_E\) contain all pairwise-resultant characters.  Put

\[
 g=\gcd(d_1,\ldots,d_k),\qquad e_i=d_i/g,
\]

and define

\[
 h(\mathbf e)=
 \gcd_{|H|=k-1}|\det W_H(\mathbf e)|.
\]

The graph theorem is an explicit finite formula for this gcd.

**Theorem 4 (full character-lattice Smith form).** For \(k\ge3\), the
nonzero Smith entries of \(W_E\) are

\[
 \operatorname{diag}(\underbrace{g,\ldots,g}_{k-2},gh(\mathbf e)).
\]

Hence, for the lattice \(L\) generated by pairwise-resultant characters,

\[
 X^*(T)/L\cong
 (\mathbb Z/g\mathbb Z)^{k-2}\oplus
 \mathbb Z/(gh\mathbb Z).
\]

For primitive degrees the quotient is cyclic of order \(h\).  To prove the
Smith shape, reduce the primitive character equations modulo an arbitrary
prime \(p\):

\[
 e_ju_i+e_iu_j=0,qquad \sum_i u_i=0.
\]

Because not all \(e_i\) vanish, this system has kernel dimension at most one.
Thus the matrix has rank at least \(k-2\) modulo every prime, so the gcd of
its \((k-2)\)-minors is one.  The first \(k-2\) primitive Smith entries are
one, and the final entry is the gcd of maximal minors, \(h\).  Scaling every
degree by \(g\) scales every Smith entry by \(g\).

The same modular analysis gives a closed criterion for the prime support of
\(h\).  Let \(S=\{i:e_i\not\equiv0\pmod p\}\).  Coordinates outside
\(S\) vanish because they pair with a nonzero degree.  If \(p\) is odd and
\(|S|\ge3\), writing \(v_i=u_i/e_i\) gives \(v_i+v_j=0\) for all
\(i,j\in S\); three indices and invertibility of \(2\) force every \(v_i\)
to vanish.  If \(|S|=1\), the sum equation forces the sole coordinate to
vanish.  If \(|S|=2\), say \(S=\{a,b\}\), then \(u_b=-u_a\) and the edge
equation becomes \((e_b-e_a)u_a=0\).  A nonzero kernel exists exactly when
the two residues agree.

For \(p=2\), all nonzero degree residues equal one.  The edge equations make
all \(v_i\) on \(S\) equal, so \(u_i=\lambda e_i\); the sum equation is
\(\lambda|S|=0\).  A nonzero kernel exists exactly when \(|S|\) is even.
Therefore:

* \(2\mid h\) exactly when an even number of primitive degrees are odd;
* for odd \(p\), \(p\mid h\) exactly when precisely two primitive degrees are
  nonzero modulo \(p\) and those residues are equal.

The exact valuations \(v_p(h)\) are determined by the graph-minor gcd.  No
shorter closed valuation formula is claimed here.

Three examples show the qualitative change from rank one.  For degrees
\((1,1,1)\), a star has determinant one, so the full character lattice is
saturated.  For \((1,1,2)\), \(h=2\).  For four equal linear factors, the
Smith form is \(\operatorname{diag}(1,1,2)\).  Equal degrees therefore do not
force character-rank collapse once \(k\ge3\), although residual torsion can
remain.

## 6. Generic degree and étaleness

Let the base be an algebraically closed field, and let
\(g_1,\ldots,g_{k-1}\) be semi-invariants that are generically nonzero on the
pairwise-coprime locus and whose integer character matrix \(W\) has nonzero
determinant.  For generic squarefree product coefficients and generic nonzero
normaliser values, a degree-\(D\) binary form has \(D\) distinct roots.
Assigning these roots to labelled factor blocks gives

\[
 \frac{D!}{d_1!\cdots d_k!}
\]

projective factorizations.  On each, the normalisation equations define a
torus isogeny with kernel scheme order \(|\det W|\).  Thus

\[
 \deg_{\mathrm{gen}}(m_{\mathbf d},g_1,\ldots,g_{k-1})
 =|\det W|\frac{D!}{\prod_i d_i!}.
\]

This is a scheme-degree statement.  The multi-border formula shows that the map is étale on
\(D(\Delta\prod_ag_a)\) precisely when \(\det W\) is invertible in the base
field.  In a characteristic dividing \(\det W\), the kernel retains the same
finite scheme order but may be nonreduced; geometric point count and scheme
degree must not be conflated.

This result agrees with the classical finite root-partition fibres of
projective polynomial multiplication (Breiding et al., 2024) while adding the
normalising torus-isogeny factor.

## 7. Computational findings

The SymPy multifactor tier checks 143 complete Plücker coordinates for
\((1,1)\), \((1,2)\), \((1,1,1)\), \((1,1,2)\), \((1,2,1)\),
\((2,1,1)\), and \((1,1,1,1)\).  Five mutations omit a resultant, square
the collision product, reverse a torus basis row, reverse the recursive sign,
or perturb the differential; all are detected.

The separately written FLINT tier checks 134 Plücker coordinates for five
three- and four-factor cases.  It also directly checks the square Jacobian
bordered by \((R_{12},R_{23})\) for degrees \((1,1,1)\) and \((1,1,2)\),
where \(\det W=1\) and \(2\), respectively.  Four structural mutations are
detected.

The character-lattice tier checks 31,761 spanning-tree determinants, 52,741
general graph minors, and 351 Smith/bad-prime cases: 84,853 positive checks in
total, plus four negative controls.  In every tier the normal and optimized
receipts are byte-identical.

The frozen research-stage hashes are:

| Tier | Script SHA-256 | Normal/optimized receipt SHA-256 |
|---|---|---|
| SymPy multifactor | `3806a7c9b4bf38598cc31ef438783984792d7e58f15d5fcf0726b93dd1879ebe` | `27d4ea5a3e89a95ffd31d426f8d4ae50ad37794652f5cc60bec324c7e09133e2` |
| FLINT multifactor and borders | `e7de053c910d800bbdc73dd15ebc7d42bf135e2853c97c84e58754557db98adb` | `f352edfd686e54fc5894839bcba05f9686aa36617a5563a1f73e53d5929588c4` |
| Character lattice | `b91d2c7b0f11a5470fd1bf41964b579973ae6b15cb3cc18e6e5b4854225bd91a` | `5efd7944b92cb8e9422d3ea33b17545a6e0b386489ce01c9578dc02e8997df51` |

These figures describe executed symbolic comparisons, not independent
experiments.  They cannot establish novelty, replace the proof, or certify the
absence of a shared specification error.

## 8. Literature synthesis and claim adjudication

### 8.1 Scalar determinant antecedents

Mahatab and Sampath (2015, Theorem A.3) prove that the canonical CRT map for a
product of monic polynomials has determinant equal to the product of pairwise
resultants.  This is a direct antecedent for the scalar \(\Delta\) on monic
slices.  The scalar product-of-resultants result must therefore be attributed,
not claimed.

Chardin (1993) proves, in a generalized Sylvester/Koszul setting, that the
resultant divides the relevant maximal minors and is generically their gcd.
The parent theorem for two factors and Theorem 1 above identify the entire
signed minor tensor, not only its gcd.

### 8.2 Factorisation quotients and root partitions

Projective multiplication and its finite fibres are classical.  Breiding et al.
(2024) treat projective polynomial multiplication and its degree through Segre
geometry.  Kurth (1997) uses the quotient of ordered linear factors by a scaling
torus and the symmetric group in the binary-form setting.  These sources support
the geometric architecture but prevent novelty claims for root partitions or
scaling quotients themselves.

### 8.3 Resultant Jacobian ideals

D'Andrea and Chipalkatti (2007) prove perfectness and equivariant resolutions
for Jacobian ideals of binary discriminants and, in a range, resultants.  This
is adjacent differential resultant theory.  The exact all-factor multiplication
Plücker identity was not located there in the bounded search, but the paper is
part of the required specialist context.

### 8.4 Incidence matrices

Grossman et al. (1995) determine minors and Smith forms of unoriented incidence
matrices.  Hessert and Mallik (2022) discuss the unicyclic inverse problem and
state the odd-cycle invertibility criterion.  Theorem 3 should therefore be
described as a weighted reduction to classical incidence theory.

### 8.5 Bounded novelty outcome

The following units were **not found in the bounded search**:

1. the all-\(k\), non-monic, signed \(\Delta\)-times-Plücker identity;
2. its multi-border character-determinant corollary in this setting;
3. the exact weighted resultant-character graph formula; and
4. the stated weighted full-lattice Smith theorem and modular criterion.

This is not a proof that they are new.  A specialist audit of determinant
complexes, toric quotients, logarithmic derivations and relative invariants is
still required.

## 9. Discussion

The main conceptual outcome is a clean separation of three layers.

First, \(\Delta\) is the rank-loss divisor.  It is classical in scalar shadows
and forced geometrically by pairwise common roots.  Second, the torus kernel
provides the missing determinant-line directions.  This is the information
lost when one immediately makes all factors monic or projective.  Third,
normalisers pair with those directions through an integer character matrix.
Its Smith form, not just its determinant, records the arithmetic of the
normalised chart.

This viewpoint corrects an over-generalisation from the parent rank-one case.
For two equal-degree factors, a resultant border has zero character difference.
For three equal linear factors, a tree of resultants can have character
determinant one.  Equal degree is therefore not a universal obstruction.  The
collision factor \(\Delta\) remains, and global affine geometry remains hard.

The strongest immediate mathematical deliverable is a standalone paper proving
Theorems 1–4 over \(\mathbb Z\), with the \(k=3\) case made fully explicit.
The proof burden is controlled: the all-factor theorem is an induction from the
parent result; the multi-border theorem is determinantal algebra; and the
character arithmetic reduces to graph incidence.

The limitations are equally clear.  The full character-lattice theorem only
classifies normalisers generated by pairwise-resultant characters.  Arbitrary
polynomial normalisers require a vertical Jacobian classification and may have
nonlinear mechanisms.  Even a perfect normaliser does not recognise an affine
space.  Consequently, claims about uniqueness of a three-dimensional Keller
mechanism or implications for the Hessian conjecture remain aspirations, not
results.

## 10. Limitations and assurance

1. The parent two-factor theorem is an immutable unrefereed candidate.  Its
   supplied exact checks are not independent reproduction.  The parent Evidence
   Press venue and the present follow-up share a producer/research process.
2. The extension proof and all new programs were produced in the same research
   process and may share a specification error.
3. The source search was bounded.  Exact antecedents may exist under different
   determinant-of-complexes, toric or invariant-theory language.
4. The Smith index \(h\) has an exact finite gcd formula and a prime-support
   criterion, but no shorter valuation formula is proved.
5. Higher-corank collision strata are not classified by subresultants here.
6. No arbitrary normaliser, affine-slice, Keller-map or Hessian theorem is
   established.
7. No proof-assistant kernel, peer review, public release or production readback
   has been completed for this follow-up.

## 11. Conclusion and recommendations

The proposed \(k=3\) subcase not only survives; it extends by a short
determinant-line induction to every number of factors.  The resulting theorem
has a precise and useful form:

\[
 \boxed{\text{maximal-minor tensor}
 =\text{pairwise collision divisor}
 \times\text{torus Plücker tensor}.}
\]

Multi-bordering converts this into the master character-determinant identity,
and pairwise resultants turn the character problem into weighted graph
incidence.  The Smith form then replaces the scalar degree difference by a
complete residual-group invariant.

The next recommended stage is a separate manuscript and reproducible child
package, not a revision of the historical parent.  Its minimum theorem set
should contain the signed all-factor identity, the multi-border formula, the
general graph-minor formula, the Smith theorem, the bad-prime criterion and the
generic degree corollary.  Before any novelty claim or release, the work should
receive an independent mathematical reproduction, a specialist priority audit,
and an adversarial sign/convention review.  Formalisation is well suited to a
later Lean kernel because the central statements are universal polynomial and
exterior-algebra identities.

Research on arbitrary normalisers and affine slices should begin only after
that foundation is stabilised.  Keller and Hessian applications should remain
explicitly conditional on solving the separate global affine-slice problem.

## References

Breiding, P., Kohn, K., & Sturmfels, B. (2024). *Metric algebraic geometry*.
Birkhäuser. [https://doi.org/10.1007/978-3-031-51462-3](https://doi.org/10.1007/978-3-031-51462-3)

Chardin, M. (1993). The resultant via a Koszul complex. In F. Eyssette & A.
Galligo (Eds.), *Computational algebraic geometry* (Progress in Mathematics,
Vol. 109, pp. 29–39). Birkhäuser.

D'Andrea, C., & Chipalkatti, J. (2007). On the Jacobian ideal of the binary
discriminant (with an appendix by A. Abdesselam). *Collectanea Mathematica,
58*(2), 155–180. [https://arxiv.org/abs/math/0601705](https://arxiv.org/abs/math/0601705)

Evidence Press. (2026). *Bordered Jacobian foundations* [Research candidate].
[https://doi.org/10.5281/zenodo.21855302](https://doi.org/10.5281/zenodo.21855302)

Grossman, J. W., Kulkarni, D. M., & Schochetman, I. E. (1995). On the minors
of an incidence matrix and its Smith normal form. *Linear Algebra and Its
Applications, 218*, 213–224.
[https://doi.org/10.1016/0024-3795(93)00173-W](https://doi.org/10.1016/0024-3795(93)00173-W)

Hessert, R., & Mallik, S. (2022). *The inverse of the incidence matrix of a
unicyclic graph* [Preprint]. arXiv.
[https://arxiv.org/abs/2201.02580](https://arxiv.org/abs/2201.02580)

Kurth, A. (1997). \(SL_2\)-equivariant polynomial automorphisms of the binary
forms. *Annales de l'Institut Fourier, 47*(2), 585–597.
[https://doi.org/10.5802/aif.1574](https://doi.org/10.5802/aif.1574)

Mahatab, K., & Sampath, K. (2015). Chinese remainder theorem for cyclotomic
polynomials in \(\mathbb Z[X]\). *Journal of Algebra, 435*, 223–262.
[https://doi.org/10.1016/j.jalgebra.2015.04.006](https://doi.org/10.1016/j.jalgebra.2015.04.006)

## AI-use disclosure

AI assistance was used in source discovery, mathematical exploration, proof
development, exact-check implementation and drafting.  All citations in this
report were checked against primary or publisher records during this research
stage.  The checks are producer-side evidence and do not constitute independent
verification.  A public manuscript should preserve this disclosure and state
its exact review and reproduction status.
