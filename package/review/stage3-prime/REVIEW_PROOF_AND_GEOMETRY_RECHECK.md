# Stage 3-prime proof and geometry recheck

**Scope:** Recheck of M1--M3 in REVIEW_PROOF_AND_GEOMETRY.md and rendered
readback of the rebuilt manuscript  
**Decision:** **PASS**  
**Residual blocker:** **None**

## Finding closure

| Finding | Source verification | Rebuilt-PDF verification | Status |
|---|---|---|---|
| M1: define \(g\), primitive \(\mathbf e\), and \(h(\mathbf e)\) before use | The English abstract now defines all three and identifies \(h\) as the positive gcd of maximal minors. The Chinese abstract gives the same definitions. The Introduction repeats them before the first displayed Smith form and states that Section 7 proves \(h=|C_{\mathbf e}|\). | The definitions appear on the first PDF page and the Introduction readback. | **CLOSED** |
| M2: identify the local pivot in Theorem 7.4 | The statement now says: after localising at \(p\), choose any \(p\)-unit pivot \(a\); the star centred at \(a\) and its associated \(\binom{k-1}{2}\) bent stars generate the full maximal-minor ideal. | The revised sentence and binomial coefficient render on PDF page 17. | **CLOSED** |
| M3: justify the \(O(k^2)\) gcd-operation bound | Theorem 7.3 now explains that, for each fixed \(a\), prefix/suffix gcds compute all excluded-pair \(G_{ab}\) values in \(O(k)\) operations, and repetition over \(a\) gives \(O(k^2)\). It also limits the claim to arithmetic-operation count, not unit-cost bit complexity. | The full explanation renders on PDF page 17. | **CLOSED** |

## Rebuilt-manuscript checks

- Revised Markdown SHA-256:
  `47120041d1050d1c512b19a7d86e86ff92cebd37ce68ac6e0070e25158462be2`.
- Rebuilt PDF SHA-256:
  `5012ed06fdfb342f6830265eb0dd8cfd23773ed27fc58bc63c8cb10b9d482c61`.
- The PDF is 35 pages, carries the revised title, and was created after the
  revised Markdown timestamp.
- PDF text readback contains the corrected M1--M3 language.
- The Section-8 base field is now \(\Bbbk\), which renders correctly and no
  longer collides with the earlier kernel matrix \(K\).
- The Mahatab--Sampath antecedent now carries the exact locator “Theorem A.3
  and eq. (A.17)” in the Introduction, Section 2.3, and Section 10.1; the
  locator is present in PDF readback.

## Recommendation

All three minor findings from the proof-and-geometry review are fully resolved.
No residual mathematical, expository, or build blocker was found within this
narrow recheck. The proof-and-geometry recommendation is therefore **PASS for
the internal research-draft pipeline**, subject to the manuscript's existing
assurance and submission-metadata limitations.
