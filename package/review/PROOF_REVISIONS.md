# Proof revisions for *Determinant Lines and Character Lattices*

**Purpose.** This file contains replacement mathematics prompted by the
proof audit. It is deliberately separate from the live manuscript. All index
sets below are zero-based and are always written in increasing order.

The results are proved under the hypotheses stated here. In particular, the
generic-degree proposition is a theorem over an algebraically closed field; no
uniform finite-flat theorem over an arbitrary base ring is asserted.

## 1. Complementary-minor composition with the exact sign

For an \(n\times(n+t)\) matrix \(A\) and a \(t\)-element set \(I\) of
column indices, put

\[
 p_I(A)=(-1)^{\sum_{i\in I}i}\det A_{\widehat I}.
\]

If \(K\) is a \(t\times(n+t)\) matrix whose rows lie in the right kernel
of \(A\), an identity

\[
 p_I(A)=c_A\det K_I \qquad (|I|=t)
\]

will be called a complementary-minor identity with scalar \(c_A\). No
division is implicit in this terminology.

### Lemma 1 (block-composition lemma)

Let \(R\) be a commutative ring, and fix integers \(r,q\geq1\) and
\(t\geq0\). Put

\[
 m=r+q-1,\qquad N=m+t+1=r+t+q.
\]

Suppose

\[
 P\in R^{r\times(r+t)},\qquad
 L\in R^{m\times(m+1)},\qquad
 S=\begin{pmatrix}P&0\\0&I_q\end{pmatrix}
   \in R^{(m+1)\times N},
\]

and set \(M=LS\). The column orders are the \(P\)-source followed by
the \(q\)-dimensional identity block, and the \(P\)-target followed by
that same identity block.

Assume the following data are given.

1. A matrix \(K_P\in R^{t\times(r+t)}\) and a scalar \(c_P\in R\)
   such that
   \[
   p_J(P)=c_P\det (K_P)_J\qquad (|J|=t).
   \]
2. A column vector \(\beta\in R^{m+1}\) and a scalar \(c_L\in R\)
   such that
   \[
   L\beta=0,\qquad
   p_{\{\ell\}}(L)=c_L\beta_\ell\quad(0\leq\ell\leq m).
   \]
3. A lift \(\lambda\in R^N\) satisfying \(S\lambda=\beta\).

Extend \(K_P\) by zero columns to

\[
 K_0=(K_P\;0)\in R^{t\times N},
\]

and order the rows of

\[
 K=\begin{pmatrix}K_0\\ \lambda^T\end{pmatrix}
   \in R^{(t+1)\times N}
\]

as the \(t\) inherited directions followed by the lifted outer
direction. Then, for every \((t+1)\)-element set \(I\),

\[
 \boxed{
 p_I(M)=(-1)^t c_Pc_L\det K_I.
 }
\]

#### Proof

First observe that \(S\) has the same complementary-minor scalar \(c_P\)
relative to \(K_0\). If a \(t\)-set \(J\) contains a column from the
identity block, then \(\det (K_0)_J=0\), and the complementary square
minor of \(S\) also vanishes by block rank. If \(J\) is contained in
the \(P\)-source, the complementary square matrix is block diagonal
with blocks \(P_{\widehat J}\) and \(I_q\). Hence

\[
 p_J(S)=c_P\det (K_0)_J
 \qquad (|J|=t).
\tag{1.1}
\]

Fix \(I=\{i_0<\cdots<i_t\}\subset\{0,\ldots,N-1\}\), and write
\(C=I^c\), so \(|C|=m\). Cauchy--Binet, with the intermediate rows
in their fixed increasing order, gives

\[
 \det M_C
 =\sum_{\ell=0}^{m}
   \det L_{\widehat\ell}\,\det S_{\widehat\ell,C}
 =c_L\sum_{\ell=0}^{m}
   (-1)^\ell\beta_\ell\det S_{\widehat\ell,C}.
\tag{1.2}
\]

Expanding the \((m+1)\times(m+1)\) matrix
\([S_C\mid\beta]\) along its last column shows that

\[
 \sum_{\ell=0}^{m}(-1)^\ell\beta_\ell
       \det S_{\widehat\ell,C}
 =(-1)^m\det[S_C\mid\beta].
\tag{1.3}
\]

Since \(\beta=S\lambda\), multilinearity in the last column yields

\[
 \det[S_C\mid\beta]
 =\sum_{a=0}^{t}\lambda_{i_a}\det[S_C\mid S_{i_a}].
\tag{1.4}
\]

There are \(m-i_a+a\) elements of \(C\) larger than \(i_a\).
Moving the final column \(S_{i_a}\) into its increasing position and
then applying (1.1) therefore gives

\[
 \begin{aligned}
 \det[S_C\mid S_{i_a}]
 &=(-1)^{m-i_a+a}\det S_{C\cup\{i_a\}}\\
 &=(-1)^{m+a+\sum I}\,
   c_P\det (K_0)_{I\setminus\{i_a\}}.
 \end{aligned}
\tag{1.5}
\]

Here the two occurrences of \(i_a\) cancel modulo two. Expanding
\(\det K_I\) along its last row gives

\[
 \det K_I
 =\sum_{a=0}^{t}(-1)^{t+a}\lambda_{i_a}
       \det (K_0)_{I\setminus\{i_a\}}.
\tag{1.6}
\]

Combining (1.4)--(1.6),

\[
 \det[S_C\mid\beta]
 =(-1)^{m+\sum I+t}c_P\det K_I.
\tag{1.7}
\]

Substitution into (1.2)--(1.3) gives

\[
 \det M_C=(-1)^{\sum I+t}c_Pc_L\det K_I.
\]

Multiplication by \((-1)^{\sum I}\) proves the formula. Every step is
a determinant identity over \(R\); no generic-rank or basis-change
argument is required. \(\square\)

### Application to factorisation

For the induction from \(k-1\) to \(k\), take

\[
 P=Dm_{d_1,\ldots,d_{k-1}},\qquad q=d_k+1,
\]

and let \(L=Dm_{D',d_k}\) at
\(B=A_1\cdots A_{k-1}\), \(A_k\), where
\(D'=\sum_{i<k}d_i\). The inherited kernel rank is \(t=k-2\).
The outer kernel column is \(\beta=(B,-A_k)^T\), and the explicit lift

\[
 \lambda=(0,\ldots,0,A_{k-1},-A_k)^T
\]

satisfies \(S\lambda=\beta\). Lemma 1 therefore supplies exactly the
factor \((-1)^{k-2}\). Replacing the ordered rows
\((\eta_1,\ldots,\eta_{k-2},\lambda)\) by
\((\kappa_1,\ldots,\kappa_{k-1})\), where
\(\kappa_b=\eta_b+\lambda\) and
\(\kappa_{k-1}=\lambda\), uses a unit upper-triangular row matrix and
introduces no further sign.

Unrolling the recurrence gives the particularly transparent exponent

\[
 E_0(\mathbf d)=
 \sum_{1\leq i<j\leq k}d_i(d_j+1)+\binom{k-1}{2}.
\tag{1.8}
\]

The exponent used in the research report,

\[
 E(\mathbf d)=
 \sum_{i<j}d_i(d_j+1)+\binom{k+1}{2}+1,
\]

satisfies \(E-E_0=2k\). Thus both expressions define the same sign.

## 2. Self-contained two-factor base lemma

This subsection is suitable for a proof appendix. It fixes the convention
rather than referring to an external sign computation.

### Lemma 2 (two-factor complementary minors over \(\mathbb Z\))

Let

\[
 A=\sum_{i=0}^{r}a_iX^{r-i}Y^i,\qquad
 B=\sum_{j=0}^{s}b_jX^{s-j}Y^j,
 \qquad r,s\geq1,
\]

and write \(AB=\sum_{h=0}^{r+s}c_hX^{r+s-h}Y^h\), where
\(c_h=\sum_{i+j=h}a_ib_j\). Order the source coordinates as

\[
 a_0,\ldots,a_r,b_0,\ldots,b_s
\]

and the target coordinates as \(c_0,\ldots,c_{r+s}\). Let \(M\) be
the coefficient Jacobian, so

\[
 M[h,i]=b_{h-i},\qquad
 M[h,r+1+j]=a_{h-j},
\]

with out-of-range subscripts equal to zero. Put

\[
 \kappa=(a_0,\ldots,a_r,-b_0,\ldots,-b_s).
\]

Define \(\operatorname{Res}(A,B)\) as the determinant of the Sylvester
matrix whose first \(s\) rows are the coefficient vectors of
\(t^ua(t)\), \(0\leq u<s\), and whose last \(r\) rows are those of
\(t^vb(t)\), \(0\leq v<r\), in the basis
\(1,t,\ldots,t^{r+s-1}\), where

\[
 a(t)=\sum_{i=0}^ra_it^i,\qquad
 b(t)=\sum_{j=0}^sb_jt^j.
\]

Then, in \(\mathbb Z[\mathbf a,\mathbf b]\),

\[
 \boxed{
 (-1)^\ell\det M_{\widehat\ell}
 =(-1)^{r(s+1)}\operatorname{Res}(A,B)\,\kappa_\ell,
 \qquad 0\leq\ell\leq r+s+1.
 }
\tag{2.1}
\]

#### Proof

Both sides of (2.1) are polynomials with integer coefficients. It is
therefore enough to prove their equality on a nonempty Zariski-open subset
over \(\mathbb C\). Work where \(a_rb_s\neq0\) and

\[
 a(t)=a_r\prod_{i=1}^{r}(t-\alpha_i),\qquad
 b(t)=b_s\prod_{j=1}^{s}(t-\beta_j),
\]

with all \(\alpha_i,\beta_j\) pairwise distinct. In the present Sylvester
convention,

\[
 \operatorname{Res}(A,B)
 =a_r^sb_s^r\prod_{i,j}(\beta_j-\alpha_i)
 =b_s^r\prod_j a(\beta_j)
 =(-1)^{rs}a_r^s\prod_i b(\alpha_i).
\tag{2.2}
\]

For completeness, (2.2) follows directly from the same evaluation
calculus used below. The transpose of the Sylvester matrix represents
\((u,w)\mapsto ua+wb\). Evaluate its output at
\((\alpha_1,\ldots,\alpha_r,\beta_1,\ldots,\beta_s)\). The evaluated
matrix is block anti-diagonal, with determinant

\[
 (-1)^{rs}
 \Bigl(\prod_i b(\alpha_i)\Bigr)\operatorname{Vand}(\alpha)
 \Bigl(\prod_j a(\beta_j)\Bigr)\operatorname{Vand}(\beta).
\]

Dividing by the determinant of the evaluation matrix,

\[
 \operatorname{Vand}(\alpha)\operatorname{Vand}(\beta)
 \prod_{i,j}(\beta_j-\alpha_i),
\]

gives (2.2). The specialization \((A,B)=(X^r,Y^s)\) fixes the
normalisation as \(+1\).

Choose \(\tau\in\mathbb C\) distinct from all roots and evaluate the
degree-\((r+s)\) target at

\[
 \alpha_1,\ldots,\alpha_r,
 \beta_1,\ldots,\beta_s,\tau.
\]

Let \(V\) be the resulting evaluation matrix. Its determinant is the
Vandermonde in this displayed order. At an \(\alpha_i\), the evaluated
Jacobian row is

\[
 b(\alpha_i)(1,\alpha_i,\ldots,\alpha_i^r\mid0),
\]

and at a \(\beta_j\) it is

\[
 a(\beta_j)(0\mid1,\beta_j,\ldots,\beta_j^s).
\]

The \(\tau\)-row is the sum of its \(A\)-block and \(B\)-block parts.
After a column is deleted, one of these two summands has deficient block
rank and vanishes. The other is evaluated as follows.

For \(m\) variables \(x_1,\ldots,x_m\), let \(W_{\widehat h}(x)\) be
the \(m\times m\) evaluation matrix with exponents
\(\{0,\ldots,m\}\setminus\{h\}\). Comparing coefficients of \(T^h\)
in the Vandermonde determinant on
\((x_1,\ldots,x_m,T)\) gives

\[
 \det W_{\widehat h}(x)
 =e_{m-h}(x)\operatorname{Vand}(x).
\tag{2.3}
\]

Suppose first that the deleted column is \(b_j\), whose global index is
\(\ell=r+1+j\). The surviving term places the \(\tau\)-row in the
\(A\)-block. Moving that row past the \(s\) beta rows contributes
\((-1)^s\), and block expansion gives

\[
 \begin{aligned}
 \det(VM_{\widehat\ell})
 ={}&(-1)^s
 \Bigl(\prod_i b(\alpha_i)\Bigr)b(\tau)
 \operatorname{Vand}(\alpha,\tau)\\
 &\quad\cdot
 \Bigl(\prod_j a(\beta_j)\Bigr)
 \det W_{\widehat j}(\beta).
 \end{aligned}
\tag{2.4}
\]

Use (2.2)--(2.3),

\[
 b(\tau)=b_s\prod_j(\tau-\beta_j),\qquad
 \prod_i b(\alpha_i)=(-1)^{rs}b_s^r
       \prod_{i,j}(\beta_j-\alpha_i),
\]

and divide (2.4) by \(\det V\). All Vandermonde and \(\tau\)-factors
cancel, leaving

\[
 \det M_{\widehat\ell}
 =(-1)^{s(r+1)}b_s e_{s-j}(\beta)\operatorname{Res}(A,B).
\tag{2.5}
\]

Since \(b_j=(-1)^{s-j}b_se_{s-j}(\beta)\),

\[
 \begin{aligned}
 (-1)^\ell\det M_{\widehat\ell}
 &=(-1)^{r+1+j+s(r+1)+s-j}
   b_j\operatorname{Res}(A,B)\\
 &=(-1)^{r(s+1)}(-b_j)\operatorname{Res}(A,B),
 \end{aligned}
\]

which is (2.1) in the \(B\)-block.

If the deleted column is \(a_i\), its global index is \(\ell=i\).
The surviving term places the \(\tau\)-row in the \(B\)-block, and the
existing row order is already block compatible. Thus

\[
 \begin{aligned}
 \det(VM_{\widehat i})
 ={}&\Bigl(\prod_i b(\alpha_i)\Bigr)
 \det W_{\widehat i}(\alpha)\\
 &\quad\cdot
 \Bigl(\prod_j a(\beta_j)\Bigr)a(\tau)
 \operatorname{Vand}(\beta,\tau).
 \end{aligned}
\tag{2.6}
\]

The same cancellations yield

\[
 \det M_{\widehat i}
 =(-1)^{rs}a_re_{r-i}(\alpha)\operatorname{Res}(A,B)
 =(-1)^{rs+r-i}a_i\operatorname{Res}(A,B).
\tag{2.7}
\]

Multiplying by \((-1)^i\) gives

\[
 (-1)^i\det M_{\widehat i}
 =(-1)^{r(s+1)}a_i\operatorname{Res}(A,B),
\]

which is (2.1) in the \(A\)-block. The equality holds on the chosen
dense open subset of \(\mathbb C^{r+s+2}\), hence as a polynomial
identity over \(\mathbb Z\). \(\square\)

### Corollary 2.1 (bordered sign)

For a row \(v=(v_0,\ldots,v_{r+s+1})\), expansion along the final row
and Lemma 2 give

\[
 \det\begin{pmatrix}M\\v\end{pmatrix}
 =(-1)^{s(r+1)+1}\operatorname{Res}(A,B)
   \langle v,\kappa\rangle.
\tag{2.8}
\]

This confirms that the multi-border sign reduces at \(k=2\) to the
base convention.

## 3. Generic degree, group scheme, and characteristic

### Proposition 3 (generic degree of a semi-invariant normalisation)

Let \(K\) be an algebraically closed field of characteristic
\(p\geq0\). Let \(k\geq2\) and \(d_i\geq1\), and put

\[
 D=\sum_{i=1}^k d_i,\qquad t=k-1,
\]

and let

\[
 X=\prod_{i=1}^k V_{d_i},\qquad
 T=\{(\lambda_1,\ldots,\lambda_k)\in\mathbb G_m^k:
        \prod_i\lambda_i=1\}.
\]

Suppose \(g_1,\ldots,g_t\in K[X]\) are nonzero
\(T\)-semi-invariants. Relative to the cocharacter basis
\(e_b-e_k\), write their characters as the rows of
\(W\in M_t(\mathbb Z)\), and assume \(\det W\neq0\) as an integer.
Set

\[
 \Phi=(m_{\mathbf d},g_1,\ldots,g_t):
 X\longrightarrow V_D\times\mathbb A^t
\]

and

\[
 X^\circ=D\!\left(\Delta_{\mathbf d}\prod_{a=1}^t g_a\right).
\]

Then the following hold.

1. The morphism \(\Phi\) is dominant and generically finite.
2. There is a dense open subset
   \(Y^\circ\subset V_D\times(\mathbb G_m)^t\), with its first
   coordinate squarefree, such that every geometric fibre over
   \(Y^\circ\) is the disjoint union of
   \[
   \nu=\frac{D!}{\prod_i d_i!}
   \]
   translates of the finite group scheme \(\ker\chi_W\), where
   \(\chi_W:T\to(\mathbb G_m)^t\) is the character isogeny defined by
   \(W\).
3. Consequently,
   \[
   \boxed{
   \deg_{\mathrm{gen}}\Phi
   =|\det W|\frac{D!}{\prod_i d_i!}.
   }
   \tag{3.1}
   \]
4. If the Smith form of \(W\) is
   \[
   \operatorname{diag}(s_1,\ldots,s_t),
   \qquad 1\leq s_1\mid\cdots\mid s_t,
   \]
   then
   \[
   \ker\chi_W\simeq\prod_{i=1}^t\mu_{s_i}
   \tag{3.2}
   \]
   as a finite diagonalizable group scheme. It has scheme order
   \(\prod_i s_i=|\det W|\).
5. If \(p=0\), the generic degree is separable. If \(p>0\), write
   \(s_i=p^{a_i}s_i'\) with \(p\nmid s_i'\). The reduced geometric
   point count and separable degree are
   \[
   \left(\prod_i s_i'\right)\frac{D!}{\prod_i d_i!},
   \tag{3.3}
   \]
   while the inseparable factor is
   \(p^{\sum_i a_i}=p^{v_p(\det W)}\).
6. On \(X^\circ\), the map \(\Phi\) is étale exactly when
   \(p\nmid\det W\), with the convention that every nonzero integer is
   invertible when \(p=0\).

#### Proof

Let \(V_D^{\mathrm{sf}}\) be the open set of nonzero binary forms with
\(D\) distinct geometric roots. Define

\[
 Z^{\mathrm{sf}}
 =V_D^{\mathrm{sf}}\times_{\mathbb P(V_D)}
   \left(\prod_i\mathbb P(V_{d_i})\right),
\tag{3.4}
\]

where the second map is projective multiplication and the first sends a
nonzero affine form to its projective class. The projective source is
understood to be restricted to the inverse image of the squarefree
locus. The projection

\[
 \pi:Z^{\mathrm{sf}}\longrightarrow V_D^{\mathrm{sf}}
\]

is finite étale. For \(F\in V_D^{\mathrm{sf}}(K)\), its fibre consists
of the projective factorisations obtained by partitioning the \(D\)
roots into labelled blocks of sizes \(d_i\). Thus its degree is

\[
 \nu=D!/\prod_i d_i!
\]

One may verify finite étaleness from the free symmetric-group action on
the ordered-root configuration space. Equivalently, projective
multiplication is finite, and its differential is an isomorphism over
the squarefree locus because the affine multiplication differential has
only the \(T\)-tangent kernel there.

Put \(U^{\mathrm{sf}}=m_{\mathbf d}^{-1}(V_D^{\mathrm{sf}})\). The map

\[
 q:U^{\mathrm{sf}}\longrightarrow Z^{\mathrm{sf}},\qquad
 (A_i)_i\longmapsto\bigl(\prod_iA_i,([A_i])_i\bigr),
\tag{3.5}
\]

is a \(T\)-torsor: two affine tuples with the same product and the same
projective factors differ by a unique product-one scaling.

For every \(a\), the principal ideal \((g_a)\) on
\(U^{\mathrm{sf}}\) is \(T\)-stable because \(g_a\) is a
semi-invariant. Its closed zero subscheme therefore descends along the
fpqc torsor \(q\) to a closed subscheme \(Z_a\subset Z^{\mathrm{sf}}\).
The open set \(U^{\mathrm{sf}}\) is dense in \(X\), so a nonzero
polynomial \(g_a\) does not vanish identically there. Faithful flatness
of \(q\) implies that \(Z_a\) is proper. Moreover,
\(Z^{\mathrm{sf}}\) is irreducible: it is the nonzero tautological-line
pullback over the irreducible squarefree open in
\(\prod_i\mathbb P(V_{d_i})\). Hence
\(\dim Z_a<\dim Z^{\mathrm{sf}}\). Since \(\pi\) is finite,
\(\pi(Z_a)\) is a proper closed subset of \(V_D^{\mathrm{sf}}\).
Consequently

\[
 V_D^{\mathrm{good}}
 =V_D^{\mathrm{sf}}\setminus\bigcup_{a=1}^t\pi(Z_a)
\tag{3.6}
\]

is dense and open, and every \(g_a\) is nonzero on every factorisation
branch above it.

Fix \(F\) and one of its projective factorisations. Choose an affine
representative \(A^0=(A_1^0,\ldots,A_k^0)\) with
\(\prod_iA_i^0=F\). Every affine representative with product exactly
\(F\) is uniquely of the form

\[
 \lambda\cdot A^0
 =(\lambda_1A_1^0,\ldots,\lambda_kA_k^0),
 \qquad \lambda\in T.
\tag{3.7}
\]

The semi-invariant equations become

\[
 g_a(\lambda\cdot A^0)
 =\chi_a(\lambda)g_a(A^0).
\tag{3.8}
\]

For \(F\in V_D^{\mathrm{good}}\) and
\(c=(c_1,\ldots,c_t)\in(K^*)^t\), equations
\(g_a=c_a\) on the branch (3.7) are precisely

\[
 \chi_W(\lambda)
 =\bigl(c_a/g_a(A^0)\bigr)_{a=1}^t.
\tag{3.9}
\]

Because \(\det W\neq0\), the homomorphism \(\chi_W\) is a finite
surjective isogeny. Every fibre of (3.9) is a translate of its kernel.
Thus the fibre of \(\Phi\) is a disjoint union of \(\nu\) such
translates and has length \(\nu|\det W|\). In particular, the image
contains the dense set
\(V_D^{\mathrm{good}}(K)\times(K^*)^t\), proving dominance, and its
fibres there are finite, proving generic finiteness. After a further
target shrinking, generic quasi-finiteness may equivalently be replaced
by finiteness. Thus one may take
\(Y^\circ=V_D^{\mathrm{good}}\times(\mathbb G_m)^t\), followed by that
optional further shrinking when an explicitly finite restriction is
desired.

Unimodular changes of the source and target character bases conjugate
\(\chi_W\) by torus automorphisms. Smith reduction therefore identifies
it with

\[
 (z_1,\ldots,z_t)\longmapsto
 (z_1^{s_1},\ldots,z_t^{s_t}),
\]

which proves (3.1)--(3.2). In characteristic \(p>0\), the reduced
subscheme of \(\mu_{p^{a_i}s_i'}\) has \(s_i'\) geometric points and
the local nonreduced factor has length \(p^{a_i}\). Since the
root-partition cover is étale, multiplication by \(\nu\) gives (3.3)
and the stated inseparable factor.

Finally, the multi-border identity gives on \(X^\circ\)

\[
 \det D\Phi
 =\pm\Delta_{\mathbf d}\det(W)\prod_a g_a.
\]

All factors except \(\det(W)\) are units there. The Jacobian criterion
therefore proves the final assertion. \(\square\)

### Scope note for Proposition 3

The proposition does **not** assert that \(\Phi\) is finite on all of
\(X\), nor that its source or any normalising level set is an affine
space. It does not cover a non-algebraically-closed base without an
additional descent statement. These are separate questions.

## 4. Exact replacement paragraphs for the graph and Smith sections

### 4.1 Quotient-lattice basis and weighted signless incidence

Let \(H\) be a set of \(k-1\) edges. Write \(C_H\) for the
\((k-1)\times k\) matrix whose row indexed by \(ij\) is

\[
 d_j e_i^*+d_i e_j^*.
\]

Let \(Q\in\mathbb Z^{k\times(k-1)}\) have columns
\(e_b-e_k\), \(1\leq b<k\). Then \(W_H=C_HQ\) is the character
matrix in the chosen cocharacter basis. The square matrix

\[
 T_0=[Q\mid e_k]
 =\begin{pmatrix}
 I_{k-1}&0\\
 -1\ \cdots\ -1&1
 \end{pmatrix}
\]

has determinant one. Therefore

\[
 \begin{pmatrix}C_H\\\mathbf1^T\end{pmatrix}T_0
 =\begin{pmatrix}W_H&C_He_k\\0&1\end{pmatrix},
\]

and hence, with no hidden factor of \(k\),

\[
 \det W_H=
 \det\begin{pmatrix}C_H\\\mathbf1^T\end{pmatrix}.
\tag{4.1}
\]

Multiplying column \(i\) in (4.1) by \(d_i\), and then factoring
\(d_id_j\) from edge row \(ij\), gives

\[
 |\det W_H|
 =\left(\prod_i d_i^{\deg_H(i)-1}\right)
 \left|\det\begin{pmatrix}B_H\\d_1\ \cdots\ d_k\end{pmatrix}\right|,
\tag{4.2}
\]

where \(B_H\) is the signless edge--vertex incidence matrix.

For a connected component on \(v\) vertices, the signless incidence
matrix has rank \(v-1\) when the component is bipartite and rank \(v\)
when it is nonbipartite. Since \(H\) has \(k-1\) edges, the bordered
matrix in (4.2) can be nonsingular only when there is exactly one
bipartite component. The identity

\[
 \sum_C(|E(C)|-|V(C)|+1)=|E(H)|-k+c=c-1
\]

then forces that component to be a tree and every other component to be
odd unicyclic. Each odd-unicyclic block has determinant of absolute
value \(2\). If \(P\sqcup Q\) is the bipartition of the tree component,
its incidence block bordered by the degree row has determinant, up to
row-order sign,

\[
 \sum_{i\in P}d_i-\sum_{j\in Q}d_j.
\]

Consequently

\[
 |\det W_H|
 =2^{c-1}
 \left|\sum_{i\in P}d_i-\sum_{j\in Q}d_j\right|
 \prod_i d_i^{\deg_H(i)-1}.
\tag{4.3}
\]

Thus the tree/odd-unicyclic component pattern is necessary; within that
pattern, the determinant is nonzero if and only if the displayed
bipartite degree balance is nonzero. If the unique tree component is an
isolated vertex \(i\), its balance \(d_i\) cancels the apparent factor
\(d_i^{-1}\) in (4.3), so the expression is integral.

### 4.2 Full rank and Smith form

Let \(g=\gcd(d_1,\ldots,d_k)\), put \(e_i=d_i/g\), and let
\(W_E(\mathbf e)\) be the complete-edge character matrix for the
primitive degree vector. It has full column rank \(k-1\) over
\(\mathbb Q\). Indeed, a kernel vector may be represented by
\((u_1,\ldots,u_k)\) with \(\sum_i u_i=0\), and the edge equations are

\[
 e_ju_i+e_iu_j=0.
\]

Since every \(e_i\neq0\) over \(\mathbb Q\), write \(v_i=u_i/e_i\).
For any three distinct indices,
\(v_i+v_j=v_i+v_\ell=v_j+v_\ell=0\); characteristic zero forces all
\(v_i=0\).

Fix a prime \(p\), and let
\(S=\{i:e_i\not\equiv0\pmod p\}\), which is nonempty by primitivity.
Coordinates outside \(S\) vanish because they pair in an edge equation
with an index in \(S\). If \(p\) is odd and \(|S|\geq3\), the same
three-index argument forces the kernel to vanish. If \(|S|=1\), the
sum equation forces the remaining coordinate to vanish. If
\(|S|=2\), at most one parameter survives. For \(p=2\), all ratios on
\(S\) agree, so again the kernel has dimension at most one. Hence

\[
 \operatorname{rank}_{\mathbb F_p}W_E(\mathbf e)\geq k-2
 \quad\text{for every prime }p.
\tag{4.4}
\]

No prime therefore divides the gcd of the \((k-2)\)-minors. The first
\(k-2\) primitive Smith entries are one. Since the matrix has full
column rank over \(\mathbb Q\), the last entry is the positive gcd

\[
 h(\mathbf e)=\gcd_{|H|=k-1}|\det W_H(\mathbf e)|.
\]

Scaling all degrees by \(g\) scales the entire character matrix by
\(g\), so the nonzero Smith entries of the original rectangular matrix
are

\[
 \boxed{
 g,\ldots,g,gh(\mathbf e),
 }
\tag{4.5}
\]

with \(k-2\) copies of \(g\). More precisely, the rectangular matrix
is unimodularly equivalent to a block consisting of this diagonal
matrix and zero rows.

### 4.3 Bad primes and the residual group scheme

For the primitive matrix, a prime \(p\) divides \(h(\mathbf e)\) exactly
when its modular kernel is nonzero. The case analysis above sharpens to

\[
 \begin{array}{ll}
 p=2:& \#\{i:e_i\text{ is odd}\}\text{ is even},\\[2mm]
 p\text{ odd}:&
 \text{exactly two }e_i\text{ are nonzero modulo }p,
 \text{ and those residues are equal}.
 \end{array}
\tag{4.6}
\]

Indeed, for odd \(p\) and \(S=\{a,b\}\), the sum equation gives
\(u_b=-u_a\), while the \(ab\)-edge equation becomes

\[
 (e_b-e_a)u_a=0.
\]

A nonzero kernel therefore survives exactly when the two nonzero
residues agree. For \(p=2\), every nonzero \(e_i\) is one and the edge
equations make all \(u_i\), \(i\in S\), equal to a parameter
\(\lambda\). The sum equation is \(|S|\lambda=0\), which has a nonzero
solution exactly when \(|S|\) is even.

For the unscaled degree vector, the complete bad-prime set is

\[
 \boxed{
 \{p:p\mid g\}\ \cup\ \{p:p\mid h(\mathbf e)\}.
 }
\tag{4.7}
\]

Let \(L\subset X^*(T)\) be the row lattice generated by the complete
edge-character matrix and put \(C=X^*(T)/L\). Equation (4.5) gives an
isomorphism of abstract finite abelian groups

\[
 C\simeq
 (\mathbb Z/g\mathbb Z)^{k-2}\oplus
 \mathbb Z/(gh(\mathbf e))\mathbb Z.
\tag{4.8}
\]

The residual subgroup of \(T\) is not merely this abstract cokernel: it
is the finite diagonalizable group scheme

\[
 D(C)=\operatorname{Spec}K[C].
\tag{4.9}
\]

Over a field of characteristic \(p\), this group scheme is étale if and
only if \(p\nmid gh(\mathbf e)\). When \(p\) divides an invariant
factor, the abstract cokernel remains the correct character group, but
the corresponding diagonalizable group scheme has a nonreduced
\(\mu_{p^a}\)-factor.

## 5. Multiplicity-one and divisor scope

Let

\[
 R=\mathbb Z[a_{i,j}:1\leq i\leq k,\ 0\leq j\leq d_i]
\]

be the universal coefficient ring. The universal pairwise resultant
\(R_{ij}=\operatorname{Res}(A_i,A_j)\) is primitive and irreducible in
\(R\), hence generates a height-one prime. Distinct \(R_{ij}\) are not
associates. The all-factor identity gives the exact ideal equality

\[
 I_{D+1}(Dm_{\mathbf d})
 =\left(\prod_{i<j}R_{ij}\right)I_{k-1}(K).
\tag{5.1}
\]

Localise (5.1) at the height-one prime \((R_{ij})\). Every other
pairwise resultant is a unit there. At the generic point of
\(R_{ij}=0\), no factor is the zero form, and the rows of \(K\) remain
linearly independent: a relation among the rows is already forced to
vanish by inspecting the separate nonzero factor blocks. Some
\((k-1)\)-minor of \(K\) is therefore a unit in this localisation.
Consequently

\[
 I_{D+1}(Dm_{\mathbf d})_{(R_{ij})}
 =(R_{ij})R_{(R_{ij})}.
\tag{5.2}
\]

Thus every pairwise-collision divisor occurs with valuation exactly
one in the maximal-minor ideal over the universal integer source.
Moreover, \(V(I_{k-1}(K))\) is contained in the union of zero-factor
strata; each such stratum has codimension \(d_i+1\geq2\). Hence
\(I_{k-1}(K)\) contributes no additional codimension-one component, and
the divisorial rank-loss cycle is

\[
 \sum_{i<j}\operatorname{div}(R_{ij}).
\tag{5.3}
\]

After base change to a field, the same valuation statement holds at
every generic collision component for which the other resultants and a
maximal minor of \(K\) remain nonzero. Intersections of collision
divisors and zero-factor strata may carry higher corank or additional
scheme structure; (5.2) makes no assertion about those higher-codimension
local rings.

## 6. Items deliberately not proved here

1. No closed formula for the \(p\)-adic valuations of
   \(h(\mathbf e)\) beyond the finite graph-minor gcd is supplied.
2. Proposition 3 is not promoted to a relative finite-flat theorem over
   \(\mathbb Z\) or an arbitrary base scheme.
3. No claim is made that arbitrary polynomial normalisers reduce to
   resultant semi-invariants.
4. No affine-space recognition, Keller-map classification, or Hessian
   conclusion follows from these local determinant and generic-degree
   statements.
5. The following standard inputs are used rather than reproved in full:
   primitive irreducibility of the universal resultant, finite étaleness
   of the squarefree root-partition cover, fpqc descent along a torus
   torsor, and the Smith classification of homomorphisms of split tori.
   A submission should cite each input at its first use.
