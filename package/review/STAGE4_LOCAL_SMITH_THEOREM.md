# Local Smith theorem for the complete resultant-character lattice

**Stage:** 4 theorem investigation  
**Status:** proved in this note, subject to incorporation audit and independent
specialist checking  
**Frozen inputs:** the Stage 3 manuscript, Reviewer 3's perspective report, the
Stage 3 editorial roadmap, and the supplementary producer-side spot checks  
**Scope boundary:** this note proves an integer-lattice theorem. It does not
establish novelty, priority, independent reproduction, peer review, or any
Keller/Hessian consequence.

## 1. Conventions and setup

Let $k\geq 3$, let

\[
 \mathbf e=(e_1,\ldots,e_k)\in\mathbb Z_{>0}^k,
 \qquad \gcd(e_1,\ldots,e_k)=1,
\]

and put

\[
 M=X^*(T)=\mathbb Z^k/\mathbb Z(1,\ldots,1).
\]

Write $x_i\in M$ for the image of the $i$-th standard basis vector. Thus
the single ambient relation is

\[
 x_1+\cdots+x_k=0.
\]

For every edge $ij$ of $K_k$, set

\[
 q_{ij}=e_jx_i+e_ix_j\in M,
\]

and define the complete resultant-character quotient

\[
 C_{\mathbf e}
 =M/\langle q_{ij}:1\leq i<j\leq k\rangle.
\]

Equivalently, if the complete character matrix $W_E(\mathbf e)$ lists the
$q_{ij}$ by rows in a basis of $M\cong\mathbb Z^{k-1}$, then

\[
 C_{\mathbf e}=\operatorname{coker}\bigl(W_E(\mathbf e)^{\mathsf T}\bigr).
\]

This transpose convention matters: the row lattice of $W_E$ is the
submodule being divided out of $M$. The maximal minors are unchanged by
transposition.

For a prime $p$, write

\[
 R_p=\mathbb Z_{(p)},\qquad v_p(0)=\infty.
\]

The ring $R_p$ is a discrete valuation ring with uniformiser $p$. Since
localisation is flat,

\[
 C_{\mathbf e}\otimes R_p
 \cong
 \frac{M\otimes R_p}
 {\langle q_{ij}:i<j\rangle_{R_p}}.
\]

## 2. Exact local presentation

### Theorem 2.1 (local star presentation)

Fix a prime $p$. Because $\mathbf e$ is primitive, there is an index $a$
such that $p\nmid e_a$. Define

\[
 D_a=e_a-\sum_{i\ne a}e_i=2e_a-\sum_{i=1}^k e_i
\]

and the ideal

\[
 I_{p,a}
 =\left(D_a,\;2e_ie_j\ (i<j,\ i,j\ne a)\right)R_p.
\]

Then the assignment $1\mapsto x_a$ induces an isomorphism of
$R_p$-modules

\[
 \boxed{
 C_{\mathbf e}\otimes R_p
 \ \cong\ 
 R_p/I_{p,a}.
 }
\]

This includes $p=2$ and $k=3$, without any change of statement.

#### Proof

Work over $R_p$. The chosen $e_a$ is a unit. For each $i\ne a$, the
star-edge relation is

\[
 q_{ai}=e_ix_a+e_ax_i=0.
\]

Its coefficient of $x_i$ is a unit, so this is a valid Tietze elimination:

\[
 x_i=-\frac{e_i}{e_a}x_a.
\]

After all $k-1$ such eliminations, $x_a$ is the only remaining generator.
The ambient relation becomes

\[
 0=\sum_i x_i
 =\left(1-\sum_{i\ne a}\frac{e_i}{e_a}\right)x_a
 =\frac{D_a}{e_a}x_a.
\]

Multiplication by the unit $e_a$ makes this precisely the relation
$D_ax_a=0$.

For a non-star edge $ij$, with $i,j\ne a$, substitution gives

\[
 q_{ij}
 =e_j\left(-\frac{e_i}{e_a}x_a\right)
  +e_i\left(-\frac{e_j}{e_a}x_a\right)
 =-\frac{2e_ie_j}{e_a}x_a.
\]

Multiplication by the unit $-e_a$ makes this precisely the relation
$2e_ie_jx_a=0$. There are no other generators or relations. Hence the
resulting one-generator presentation is $R_p/I_{p,a}$. This is an
isomorphism of modules, not merely an equality of orders. $\square$

### Edge cases explicitly covered

1. **Existence of a pivot.** Primitivity is equivalent to saying that for
   every prime $p$, at least one $e_a$ is a $p$-unit.
2. **The prime $2$.** No division by $2$ occurred. At $p=2$, the
   relations $2e_ie_j$ remain in the ideal and retain their full valuation.
3. **The case $k=3$.** Exactly two indices remain outside $a$, so there is
   exactly one non-star coefficient $2e_ie_j$. The proof is unchanged.
4. **A zero $D_a$.** The generator $D_a=0$ simply contributes the zero
   relation and has valuation $\infty$. Since $k\geq3$ and the degrees are
   positive, at least one coefficient $2e_ie_j$ occurs and is nonzero, so
   the local quotient still has finite length.
5. **Vanishing modulo $p$.** Some $e_i$, $D_a$, or $2e_ie_j$ may
   vanish modulo $p$. The presentation is over $R_p$, not only over
   $\mathbb F_p$, so these are measured by their exact valuations rather
   than discarded.

### Corollary 2.2 (choice independence)

If $a$ and $b$ are both $p$-unit indices, then

\[
 I_{p,a}=I_{p,b}.
\]

In particular, every admissible pivot produces the same valuation formula.

#### Proof

Theorem 2.1 identifies both ideals with the annihilator of the same canonical
module:

\[
 I_{p,a}=\operatorname{Ann}_{R_p}(C_{\mathbf e}\otimes R_p)=I_{p,b}.
\]

More concretely, the edge $ab$ gives
$x_b=-(e_b/e_a)x_a$, so the two displayed cyclic generators differ by a
unit. $\square$

## 3. Exact valuations and complete primitive Smith form

### Theorem 3.1 (exact local valuation)

For any $p$-unit pivot $a$, set

\[
 m_p(\mathbf e)=
 \min\left\{
 v_p(D_a),
 \min_{\substack{i<j\\i,j\ne a}}
 \bigl(v_p(2)+v_p(e_i)+v_p(e_j)\bigr)
 \right\}.
\]

Then

\[
 \boxed{
 C_{\mathbf e}\otimes R_p\cong R_p/(p^{m_p(\mathbf e)}),
 \qquad
 v_p(h(\mathbf e))=m_p(\mathbf e).
 }
\]

Here $R_p/(p^0)=0$, and $v_p(0)=\infty$. The value
$m_p(\mathbf e)$ is finite for every $p$.

#### Proof

Every finitely generated ideal of the DVR $R_p$ is generated by the member
of least valuation. Theorem 2.1 therefore gives the first isomorphism.

The zeroth Fitting ideal of $C_{\mathbf e}\otimes R_p$ is both
$I_{p,a}=(p^{m_p})$ and the localisation of the ideal generated by the
maximal minors of $W_E(\mathbf e)$. The positive generator of the latter
ideal over $\mathbb Z$ is $h(\mathbf e)$. Hence
$v_p(h)=m_p$.

The minimum is finite because, for $k\geq3$, there is at least one pair
$i<j$ outside $a$, and $2e_ie_j\ne0$. $\square$

### Corollary 3.2 (primitive cyclicity and global reconstruction)

The group $C_{\mathbf e}$ is finite cyclic and

\[
 \boxed{
 C_{\mathbf e}\cong\mathbb Z/h(\mathbf e)\mathbb Z,
 \qquad
 h(\mathbf e)=\prod_p p^{m_p(\mathbf e)}.
 }
\]

Only finitely many $m_p$ are nonzero.

#### Proof

Theorem 3.1 shows that every $p$-primary localisation is cyclic of order
$p^{m_p}$. The direct sum of cyclic primary groups of pairwise coprime orders
is cyclic. The order is the product displayed. Equivalently, this recovers the
primitive Smith form

\[
 \operatorname{diag}(1,\ldots,1,h(\mathbf e)).
\]

Finiteness also follows directly: for any prime, the local presentation has a
nonzero relation coefficient, so tensoring further with $\mathbb Q$ gives
zero. Thus the finitely generated abelian group $C_{\mathbf e}$ has rank
zero and is finite.
$\square$

## 4. Explicit odd- and $2$-adic cases

The uniform formula above is often shorter than a case split. The following
forms make the bad-prime support and higher valuations transparent.

### 4.1 Odd primes

Let $p$ be odd and let

\[
 S_p=\{i:p\nmid e_i\}.
\]

Then $m_p=0$ unless

\[
 S_p=\{a,b\},\qquad e_a\equiv e_b\pmod p.
\]

In that exceptional case,

\[
 \boxed{
 m_p(\mathbf e)
 =\min\left\{
 v_p(e_a-e_b),
 \min_{c\notin\{a,b\}}v_p(e_c)
 \right\}.
 }
\]

To justify the simplification, put
$q=\min_{c\notin\{a,b\}}v_p(e_c)$. With pivot $a$, the least non-star
valuation is $q$, because the pair $bc$ contributes $e_be_c$. Moreover

\[
 D_a=(e_a-e_b)-\sum_{c\notin\{a,b\}}e_c,
\]

and the sum on the right has valuation at least $q$. Therefore

\[
 \min(v_p(D_a),q)=\min(v_p(e_a-e_b),q).
\]

This proves both the old odd-prime support criterion and every higher
odd-prime valuation.

### 4.2 The prime $2$

Let

\[
 s=\#\{i:e_i\text{ is odd}\}.
\]

Primitivity gives $s\geq1$. Then:

\[
 \boxed{
 m_2(\mathbf e)=
 \begin{cases}
 0,&s\text{ odd},\\[2mm]
 1,&s\geq4\text{ and }s\text{ even},\\[2mm]
 \min\left(v_2(D_a),\ 1+\min_{c\notin\{a,b\}}v_2(e_c)\right),
 &s=2,
 \end{cases}
 }
\]

where $a,b$ are the two odd indices in the last case.

Indeed, for an odd pivot $a$, one has $D_a\equiv s\pmod2$. If $s$ is
odd, the ambient coefficient is a unit. If $s\geq4$ is even, $D_a$ is
even while two odd indices remain outside $a$, so a non-star coefficient
has valuation exactly one. If $s=2$, the least non-star coefficient pairs
the other odd index $b$ with an even index of least valuation.

The $s=2$ expression is independent of whether $a$ or $b$ is used. If
$E=\sum_{c\notin\{a,b\}}e_c$ and
$q=\min_{c\notin\{a,b\}}v_2(e_c)$, then

\[
 D_a+D_b=-2E\equiv0\pmod{2^{q+1}}.
\]

Thus $v_2(D_a)$ and $v_2(D_b)$, truncated at $q+1$, agree.

This recovers the old parity support criterion and shows that all higher
$2$-adic valuations occur only in the exactly-two-odd case.

## 5. A factorisation-free global formula

The primewise theorem can be assembled into a symmetric integer formula that
does not require factoring a trial maximal minor.

For every pair $a<b$, define

\[
 G_{ab}=\gcd\{e_c:c\notin\{a,b\}\},
 \qquad
 Q_{ab}=\gcd(|e_a-e_b|,G_{ab}),
\]

and write $Q_{ab}^{\mathrm{odd}}=Q_{ab}/2^{v_2(Q_{ab})}$. Since $k\geq3$,
the set defining $G_{ab}$ is nonempty.

Define $\eta_2(\mathbf e)$ as follows:

\[
 \eta_2(\mathbf e)=
 \begin{cases}
 0,&s\text{ odd},\\
 1,&s\geq4\text{ and }s\text{ even},\\
 \min\bigl(v_2(D_a),1+v_2(G_{ab})\bigr),&s=2,
 \end{cases}
\]

where $a,b$ are the two odd indices in the last line.

### Theorem 5.1 (closed global index formula)

\[
 \boxed{
 h(\mathbf e)
 =2^{\eta_2(\mathbf e)}
  \prod_{1\leq a<b\leq k}Q_{ab}^{\mathrm{odd}}.
 }
\]

The odd factors in the product are pairwise coprime.

#### Proof

Let $p$ be odd. If $p\mid Q_{ab}$, then $p$ divides every $e_c$ outside
${a,b}$ and divides $e_a-e_b$. It cannot divide $e_a$, because then it
would divide $e_b$ and hence every $e_i$, contrary to primitivity. Thus

\[
 S_p=\{a,b\},\qquad e_a\equiv e_b\not\equiv0\pmod p.
\]

Conversely, this exceptional support condition implies $p\mid Q_{ab}$.
It also shows that an odd prime can divide at most one of the $Q_{ab}$, so
their odd parts are pairwise coprime.

By Section 4.1,

\[
 v_p(h)=
 \min\left(v_p(e_a-e_b),\min_{c\notin\{a,b\}}v_p(e_c)\right)
 =v_p(Q_{ab}).
\]

For every other odd prime, both sides have valuation zero. Section 4.2 gives
the displayed exponent at $2$. Equality follows prime by prime. $\square$

### Computational consequence

The formula gives a canonical $O(k^2)$ arithmetic-operation computation of
$h$, rather than an exponential gcd over all $(k-1)$-edge subgraphs:

1. compute every pair-exclusion gcd $G_{ab}$;
2. compute $Q_{ab}$, strip its power of $2$, and multiply the odd parts;
3. compute $s$ and the single exponent $\eta_2$.

All $G_{ab}$ can be obtained in $O(k^2)$ gcd operations, for example by an
interval-gcd table (or a range-gcd sparse table) followed by constant-many
range queries per excluded pair. This is an arithmetic-operation statement;
it is not a claim of unit-cost bit complexity for arbitrarily large degrees.

## 6. Spanning trees already determine the full index

Let

\[
 \tau(\mathbf e)
 =\gcd_{T\text{ spanning tree of }K_k}|\det W_T(\mathbf e)|.
\]

The definition of $h$ also allows disconnected edge sets with odd-unicyclic
components. The next theorem shows that those additional bases never lower
the full-list gcd.

### Theorem 6.1 (tree-gcd equality)

\[
 \boxed{\tau(\mathbf e)=h(\mathbf e).}
\]

More strongly, after localising at a prime $p$ and choosing a $p$-unit
vertex $a$, one star and
$\binom{k-1}{2}$ bent stars generate the local maximal-minor ideal.

#### Proof

Fix $p$ and a $p$-unit vertex $a$. Let $J_{p,a}$ be the ideal generated
in $R_p$ by the following spanning-tree determinants.

First take the star $T_a$ centred at $a$. The manuscript's proved tree
formula gives, up to sign,

\[
 \det W_{T_a}=e_a^{k-2}D_a.
\]

Since $e_a$ is a unit, $D_a\in J_{p,a}$.

For each unordered pair of distinct indices outside $a$, choose either
ordering $(i,j)$ and form the bent star

\[
 T_{a;i,j}
 =\{a\ell:\ell\ne a,j\}\cup\{ij\}.
\]

Its bipartition is
${a,j}\sqcup(V\setminus\{a,j})$, its centre $a$ has degree $k-2$,
and $i$ has degree two. The same tree formula gives, up to sign,

\[
 \det W_{T_{a;i,j}}
 =e_a^{k-3}e_i(D_a+2e_j).
\]

The reverse ordering works equally well. After multiplying by units and
subtracting $e_iD_a$, the chosen ordering yields

\[
 2e_ie_j\in J_{p,a}.
\]

Therefore the ideal $I_{p,a}$ of Theorem 2.1 is contained in the ideal
generated by these tree determinants.

Conversely, every tree determinant is a maximal minor of $W_E$. The ideal
of all maximal minors is the zeroth Fitting ideal of
$C_{\mathbf e}\otimes R_p$, which Theorem 2.1 identifies with $I_{p,a}$.
Hence

\[
 I_{p,a}\subseteq J_{p,a}\subseteq
 \operatorname{Fitt}_0(C_{\mathbf e}\otimes R_p)=I_{p,a}.
\]

Thus the tree-minor ideal and full maximal-minor ideal agree after
localisation at every prime. Their positive integer generators have the same
valuation at every prime, so $\tau=h$. $\square$

### Interpretation

Odd-unicyclic minors remain relevant as individual arithmetic-matroid basis
multiplicities and as square chart determinants. They are redundant only for
the single full-list saturation index $m(E)=h$.

## 7. Nonprimitive degrees

Let

\[
 \mathbf d=g\mathbf e,
 \qquad g=\gcd(d_1,\ldots,d_k),
\]

with $\mathbf e$ primitive. Every resultant-character row scales by $g$:

\[
 W_E(\mathbf d)=gW_E(\mathbf e).
\]

### Corollary 7.1 (complete Smith form with content)

\[
 \boxed{
 \operatorname{SNF}(W_E(\mathbf d))
 =\operatorname{diag}
 \bigl(\underbrace{g,\ldots,g}_{k-2},\ gh(\mathbf e)\bigr).
 }
\]

Consequently

\[
 C_{\mathbf d}
 \cong
 (\mathbb Z/g\mathbb Z)^{k-2}
 \oplus\mathbb Z/(gh(\mathbf e))\mathbb Z.
\]

#### Proof

Take unimodular matrices that put $W_E(\mathbf e)$ into
$\operatorname{diag}(1,\ldots,1,h)$. The same matrices put
$gW_E(\mathbf e)$ into
$\operatorname{diag}(g,\ldots,g,gh)$, which already satisfies Smith
divisibility. $\square$

If $\gamma=v_p(g)$ and $m=m_p(\mathbf e)$, then the exact local form is

\[
 C_{\mathbf d}\otimes R_p
 \cong
 \bigl(R_p/(p^\gamma)\bigr)^{k-2}
 \oplus R_p/(p^{\gamma+m}).
\]

Thus normalising by the primitive vector before choosing a local pivot is
essential at primes dividing $g$.

## 8. Diagonalizable group-scheme consequences

Let

\[
 G_{\mathbf d}=D(C_{\mathbf d})
\]

be the diagonalizable group scheme over $\operatorname{Spec}\mathbb Z$ with
character group $C_{\mathbf d}$. Noncanonically, after choosing Smith
coordinates,

\[
 \boxed{
 G_{\mathbf d}
 \cong
 \mu_g^{\,k-2}\times\mu_{g h(\mathbf e)}.
 }
\]

It is finite locally free of rank

\[
 |C_{\mathbf d}|=g^{k-1}h(\mathbf e).
\]

Let $K$ be a field of characteristic $p>0$. Write

\[
 g=p^\gamma g',\qquad h=p^m h',
 \qquad p\nmid g'h'.
\]

After base change to $K$, its connected diagonalizable factor and maximal
étale factor are

\[
 G_{\mathbf d,K}^{\mathrm{conn}}
 \cong
 \mu_{p^\gamma}^{\,k-2}\times\mu_{p^{\gamma+m}},
\]

\[
 G_{\mathbf d,K}^{\mathrm{et}}
 \cong
 \mu_{g'}^{\,k-2}\times\mu_{g'h'}.
\]

Hence:

- the connected factor has length $p^{\gamma(k-1)+m}$;
- the étale factor has rank $(g')^{k-1}h'$;
- over an algebraic closure, the number of geometric points is
  $(g')^{k-1}h'$;
- the total scheme rank remains $g^{k-1}h$;
- the group scheme is étale (equivalently reduced after field base change)
  exactly when $p\nmid gh$.

For primitive degrees, $G_{\mathbf e}\cong\mu_h$, with connected factor
$\mu_{p^{m_p}}$. The local theorem therefore gives not merely the bad
characteristics but the exact infinitesimal length in each bad
characteristic.

These statements concern the residual group attached to the **complete
pairwise-resultant character list**. They do not assert that a selected square
set of polynomial resultant normalisers has determinant $h$, nor that this
group is intrinsic among all possible semi-invariants.

## 9. Diagnostic examples

All Smith forms below are for the row lattice in $X^*(T)$.

| Primitive $\mathbf e$ | Exact $h(\mathbf e)$ | Primitive Smith form | Diagnostic point |
|---|---:|---|---|
| $(1,1,3)$ | $3$ | $\operatorname{diag}(1,3)$ | Odd bad prime $3$ |
| $(1,1,9)$ | $9$ | $\operatorname{diag}(1,9)$ | $v_3(h)=2$ |
| $(1,1,4)$ | $4$ | $\operatorname{diag}(1,4)$ | $v_2(h)=2$ |
| $(1,3,2)$ | $4$ | $\operatorname{diag}(1,4)$ | Exactly two odd entries; the $2$-adic valuation rises above $v_2(G_{12})$ |
| $(1,5,4)$ | $8$ | $\operatorname{diag}(1,8)$ | $v_2(h)=3$ |
| $(1,2,2)$ | $1$ | $\operatorname{diag}(1,1)$ | Full list saturated although the three square minors have absolute values $3,2,2$ |
| $(1,1,1,1)$ | $2$ | $\operatorname{diag}(1,1,2)$ | Four odd entries force exactly one factor of $2$ |

Two infinite families expose arbitrary higher valuations:

\[
 h(1,1,N)=N\qquad(N\geq1),
\]

and, for $q\geq1$,

\[
 h(1,1+2^q,2^q)=2^{q+1}.
\]

The first family gives $v_p(h)=r$ from $N=p^r$, including arbitrary odd
valuations. The second family realises the upper $q+1$ branch of the
exactly-two-odd $2$-adic formula.

For a nonprimitive example, take

\[
 \mathbf d=(2,2,18)=2(1,1,9).
\]

Then $g=2$, $h=9$,

\[
 \operatorname{SNF}(W_E(\mathbf d))=\operatorname{diag}(2,18),
 \qquad
 G_{\mathbf d}\cong\mu_2\times\mu_{18}.
\]

## 10. Proof audit and hidden convention risks

### 10.1 Audited points

1. **Character versus cocharacter lattice.** The quotient
   $M=\mathbb Z^k/\mathbb Z(1,\ldots,1)$ is the character lattice of
   $T=\ker(\mathbb G_m^k\to\mathbb G_m)$. The edge vector
   $e_jx_i+e_ix_j$ pairs with a cocharacter
   $u\in\{\sum u_i=0\}$ as $e_ju_i+e_iu_j$, matching the manuscript.
2. **Row-lattice convention.** The quotient is the cokernel of
   $W_E^{\mathsf T}$, not of the rectangular row matrix viewed in the other
   direction. Smith entries and maximal minors are unchanged by transpose.
3. **No illegal division.** The only denominators are powers of $e_a$, a
   unit in $R_p$. No division by $2$, by another degree, or by $D_a$
   occurs.
4. **Fitting ideal versus order.** The equality
   $v_p(h)=m_p$ uses equality of zeroth Fitting ideals after localisation,
   not an assumption that matching cardinalities imply isomorphic modules.
   The module isomorphism was proved first.
5. **Absolute determinants.** Gcds use absolute values, whereas ideal
   manipulations use signed determinants. The missing signs are units
   $\pm1$, so they do not affect any ideal.
6. **The $k=3$ endpoint.** The bent-star exponent $e_a^{k-3}$ is then
   $e_a^0=1$; no negative exponent occurs.
7. **Positive-degree hypothesis.** It guarantees that the non-star products
   are nonzero. The algebraic elimination extends to nonzero signed degrees,
   but zero degrees require a separate finiteness statement and are outside
   binary-form factorisation.
8. **Primitive versus nonprimitive input.** A $p$-unit pivot need not exist
   for $\mathbf d$ when $p\mid g$. The theorem is correctly applied to the
   primitive vector $\mathbf e$, after which scalar multiplication gives the
   nonprimitive Smith form.
9. **Group-scheme base.** $D(C)$ is defined first over
   $\operatorname{Spec}\mathbb Z$; connected/étale assertions are made only
   after base change to a field of specified characteristic.
10. **Full list versus square chart.** The theorem computes the saturation
    index of the redundant complete edge list. It does not produce a
    $(k-1)$-edge basis of determinant $h$. The example $(1,2,2)$ proves
    that such an inference would be false.

### 10.2 Remaining assurance boundaries

- The proof has been developed and internally audited in this Stage 4 task;
  it has not yet received independent specialist reproduction.
- The earlier exact computations are consistent with the theorem but are not
  used in any proof step.
- The theorem's novelty relative to local presentations of signed-graphic or
  arithmetic-matroid modules requires a separate literature audit.
- Incorporating this theorem into the manuscript requires a full dependency
  check of the abstract, Theorem 7.1, Corollary 7.2, examples, conclusion,
  computation claims, and group-scheme wording.

## 11. Strongest conclusion

Reviewer 3's proposed local presentation is correct. It yields:

1. an actual cyclic $R_p$-module presentation for every prime;
2. every exact valuation $v_p(h)$, including $p=2$;
3. a factorisation-free symmetric global formula for $h$;
4. a canonical $O(k^2)$ arithmetic computation;
5. equality between the spanning-tree gcd and the full maximal-minor gcd;
6. the complete nonprimitive Smith form and exact connected/étale residual
   group-scheme decomposition.

No mathematical blocker remains for replacing the manuscript's implicit
top-divisor endpoint by this complete local and global Smith calculation.
The remaining blockers are assurance and integration tasks: specialist
re-review, antecedent checking for the strengthened result, and careful
manuscript revision without conflating the full edge list with a square
polynomial normalisation chart.
