# Supplementary Stage 3 Spot Check: Proposed Local Valuation Formula

**Status:** Internal editorial spot check of a theorem candidate proposed by Reviewer 3. This is not part of the frozen manuscript, not a proof, not an independent reproduction, and not evidence that Stage 4 revision has begun.

## Formula checked

For a primitive positive degree vector \(\mathbf e=(e_1,\ldots,e_k)\), let \(C_{\mathbf e}\) be the cokernel of the complete resultant-character lattice. Fix a prime \(p\) and an index \(a\) with \(p\nmid e_a\). Reviewer 3 proposed

\[
C_{\mathbf e}\otimes\mathbb Z_{(p)}
\cong
\mathbb Z_{(p)}\Big/
\left(e_a-\sum_{i\ne a}e_i,
      \;2e_i e_j\ (i<j,\ i,j\ne a)\right),
\]

and hence

\[
v_p(h(\mathbf e))=
\min\left\{
v_p\!\left(e_a-\sum_{i\ne a}e_i\right),
\min_{\substack{i<j\\ i,j\ne a}}
\bigl(v_p(2)+v_p(e_i)+v_p(e_j)\bigr)
\right\},
\]

with \(v_p(0)=\infty\).

The checks below compared this predicted valuation with the final nonzero Smith entry of the complete edge-character matrix computed directly over \(\mathbb Z\).

## Environment

- Python 3.14.6
- SymPy 1.14.0
- Exact integer matrices and **smith_normal_form(..., domain=ZZ)**
- No floating-point arithmetic

## Checks

1. **Seeded random check:** 1,000 primitive vectors, 250 for each \(k=3,4,5,6\), entries sampled uniformly from \(1,\ldots,15\) with seed **20260809**. Each vector was tested at every prime divisor of the computed \(h\) and at \(2,3,5,7,11,13\).

   Result: **PASS random_primitive_vectors=1000 k=3..6 primes=divisors(h)+2,3,5,7,11,13**

2. **Exhaustive bounded check:** every primitive vector in the following boxes:

   | \(k\) | Entry range | Primitive vectors |
   |---:|---:|---:|
   | 3 | \(1,\ldots,12\) | 1,447 |
   | 4 | \(1,\ldots,8\) | 3,823 |
   | 5 | \(1,\ldots,5\) | 3,091 |
   | 6 | \(1,\ldots,4\) | 4,031 |
   | **Total** |  | **12,392** |

   Result: **PASS exhaustive_local_valuation_formula {3: 1447, 4: 3823, 5: 3091, 6: 4031} total 12392**

3. **Pivot-independence check:** 6,235 primitive vectors across \(k=3,4,5\), testing every admissible choice of \(a\) for each checked prime. Every admissible pivot produced the same valuation, equal to the valuation of the computed final Smith entry.

   Result: **PASS all_admissible_pivot_choices vectors 6235**

## Interpretation

No counterexample was found. These checks materially increase confidence that the proposed local presentation is worth proving, and they show that it recovers more than the existing prime-support corollary. They do **not** establish the module isomorphism, arbitrary-degree validity, choice independence in general, novelty, or publication priority. The Stage 3 roadmap therefore correctly treats the formula as the highest-value required theorem investigation for Stage 4, conditional on explicit user approval.

