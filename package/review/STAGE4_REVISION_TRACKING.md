# Stage 4 revision tracking

Status vocabulary:

- `IN_PROGRESS`: active proof, literature, or manuscript work.
- `RESOLVED_MATH`: resolved by a mathematical change with a proof.
- `RESOLVED_EXPOSITION`: resolved by clarification, restructuring, or citation.
- `DELIBERATE_LIMITATION`: cannot be completed without information or authority
  not supplied; the limitation remains explicit.
- `REVIEWER_DISAGREE`: the requested change is declined with reasons and will be
  re-adjudicated at Stage 3'.
- `PENDING_REVIEW`: implemented but not yet accepted by the Stage 3' panel.
- `VERIFIED_STAGE3_PRIME`: checked and accepted within the internal
  producer-side research-draft review; not external peer review.

The frozen Stage 2.5 manuscript and Stage 3 reports are inputs only. This file
tracks a child revision and does not alter their evidential status.

## Priority 1

| Item | Type | Status | Planned or completed resolution | Evidence/location |
|---|---|---|---|---|
| P1-1.1 | Mathematics | VERIFIED_STAGE3_PRIME | Investigated without presumption, then proved the proposed local star presentation. | `LOCAL_SMITH_THEOREM.md`; revised Theorem 7.1 |
| P1-1.2 | Mathematics | VERIFIED_STAGE3_PRIME | Proved an actual local module isomorphism by unit Tietze elimination. | `LOCAL_SMITH_THEOREM.md`; `LOCAL_SMITH_ADVERSARIAL_AUDIT.md`; revised Theorem 7.1 |
| P1-1.3 | Mathematics | VERIFIED_STAGE3_PRIME | Derived pivot-independent valuations, the full 2-adic case, a symmetric global formula, tree-gcd equality, and the scaled Smith form. | revised Corollary 7.2, Theorems 7.3--7.4, Corollary 7.5 |
| P1-1.4 | Assurance | VERIFIED_STAGE3_PRIME | Kept proof independent of computation; added a separate exact tier under normal and optimized Python. | revised Sections 7 and 9; `verify_local_smith.py`; byte-identical receipts |
| P1-2.1 | Literature/framing | VERIFIED_STAGE3_PRIME | Added primary-source signed-graph, arithmetic-matroid, toric-arrangement, matroid-over-ring, root-list, and adjacent Smith context. | `ARITHMETIC_LITERATURE_AUDIT.md`; revised Sections 1, 6, 7, 10 and Appendix D |
| P1-2.2 | Framing | VERIFIED_STAGE3_PRIME | Identified primitive `h=m(E)` and unscaled `m_d(E)=g^(k-1)h`; isolated the evaluated cross-weighted module theorem. | revised Sections 1, 7, 10 |
| P1-2.3 | Exposition | VERIFIED_STAGE3_PRIME | Added a theorem-status table separating classical inputs, formal consequences, factorisation-specific steps, and candidate results. | revised Section 1 |
| P1-2.4 | Framing | VERIFIED_STAGE3_PRIME | Made the exact character-lattice theorem primary and retained bounded novelty language. | revised title, abstracts, Sections 1, 10, 11 |
| P1-3.1 | Geometry | VERIFIED_STAGE3_PRIME | Distinguished full-edge lattice, edge charts, polynomial monomials, Laurent units, and arbitrary semi-invariants. | `GEOMETRY_INTERFACE_REVISIONS.md`; revised Sections 7.1, 8.2 |
| P1-3.2 | Exact check | VERIFIED_STAGE3_PRIME | Verified `(1,2,2)` has full-edge Smith form `(1,1)` and edge determinants `3,2,2`; constructed an explicit nonnegative unimodular monomial chart. | revised Sections 7.5 and 8.2; exact verifier |
| P1-3.3 | Interpretation | VERIFIED_STAGE3_PRIME | Proved a scoped universal property and renamed the object the unit-character residual group of the fixed open `U`. | revised Sections 7.1, 7.4 |
| P1-3.4 | Scheme theory | VERIFIED_STAGE3_PRIME | Replaced reduced-component wording by unconditional base-changed ideal equality and exact DVR/Cartier order-one hypotheses. | revised Section 4.1 |
| P1-3.5 | Scheme theory | VERIFIED_STAGE3_PRIME | Proved the fpqc torsor/descent step and displayed the Cartesian translated-isogeny square. | revised proof of Theorem 8.1 |
| P1-3.6 | Scheme theory | VERIFIED_STAGE3_PRIME | Derived total, separable, inseparable, geometric-point, and étaleness data from the finite-locally-free factorisation. | revised Theorem 8.1 |
| P1-3.7 | Geometry | VERIFIED_STAGE3_PRIME | Gave edge, polynomial-monomial, and Laurent-unit chart consequences without conflating their determinants with `h`. | revised Section 8.2 |

## Priority 2

| Item | Type | Status | Planned or completed resolution | Evidence/location |
|---|---|---|---|---|
| P2-1 | Exposition | VERIFIED_STAGE3_PRIME | The status table and contribution boundary isolate formal determinant-line consequences while retaining the integral orientation proof. | revised Sections 1, 3--5, 10 |
| P2-2 | Terminology | VERIFIED_STAGE3_PRIME | Defined the scoped residual group, removed ambiguous `normaliser`, fixed cokernel/base conventions, and reserved isogeny language for square/image maps. | revised Sections 4, 7, 8 |
| P2-3 | Proof auditability | VERIFIED_STAGE3_PRIME | Repaired numbering; added cross-multiplied isolated-vertex handling, Vandermonde orientation, and a deleted-block parity table. | revised Section 6 and Appendix E |
| P2-4 | Examples | VERIFIED_STAGE3_PRIME | Added odd-prime, higher odd-adic, higher 2-adic, nonprimitive, and chart-separation examples. | revised Sections 7.5 and 8.2 |

## Priority 3

| Item | Type | Status | Planned or completed resolution | Evidence/location |
|---|---|---|---|---|
| P3-1 | Editorial | VERIFIED_STAGE3_PRIME | Aligned title, abstracts, introduction, and conclusion with the proved arithmetic endpoint and qualified geometric synthesis. | revised manuscript front and back matter |
| P3-2 | Administration | DELIBERATE_LIMITATION | Author identity, affiliation, contributions, funding, conflict, and licence cannot be invented. Preserve explicit placeholders and block submission/release finality until supplied by the responsible author. | revised declarations and release status |
| P3-3 | Copyediting | VERIFIED_STAGE3_PRIME | Repaired numbering, references, field notation, keywords, and terminology; retained the Chinese abstract as optional research-draft front matter. | revised manuscript; clean Pandoc/XeLaTeX build |

## Devil's-advocate findings

| Item | Status | Disposition |
|---|---|---|
| DA-MAJOR-1 | VERIFIED_STAGE3_PRIME | Exact local and global formulas now evaluate the top Smith divisor. |
| DA-MAJOR-2 | VERIFIED_STAGE3_PRIME | Full-list, edge-basis, monomial, and Laurent charts are explicitly separated. |
| DA-MAJOR-3 | VERIFIED_STAGE3_PRIME | The exact local theorem, global formula, tree-gcd theorem, and unit-group geometry materially strengthen the endpoint. |
| DA-MAJOR-4 | VERIFIED_STAGE3_PRIME | A scoped intrinsic interpretation is proved for regular units on `U`; no universality among arbitrary semi-invariants is claimed. |
| DA-MINOR-1 | VERIFIED_STAGE3_PRIME | Abstract hypotheses are explicit and the degree theorem is proved finite locally free on a dense open. |
| DA-MINOR-2 | VERIFIED_STAGE3_PRIME | Odd bad-prime and arbitrary higher-valuation examples are included. |

## Gate status

- Stage 4 revision: `VERIFIED_STAGE3_PRIME`.
- Stage 3' re-review: `ACCEPTED_RESEARCH_DRAFT_SCOPE`.
- Stage 4.5 final integrity: `PASS` after one version-sensitive citation
  locator was repaired and reverified; all seven AI-research failure modes are
  clear within the recorded producer-side scope.
- Submission/release readiness: blocked by P3-2 metadata and absent release
  authority, not by an unresolved manuscript-integrity issue.
