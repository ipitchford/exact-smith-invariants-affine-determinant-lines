# Stage 4.5 final integrity decision before package freeze

**Manuscript:** *Exact Smith Invariants and Affine Determinant Lines of
Binary-Form Factorisation*  
**Date:** 9 August 2026  
**Decision:** **PASS**  
**Scope:** producer-side final integrity of the revised research draft

This decision permits the revised payload to be frozen and packaged. It is not
independent mathematical reproduction, completed formal verification,
specialist priority resolution, external peer review, journal acceptance,
submission authority, or release authority.

## Audited snapshot

| Object | SHA-256 |
|---|---|
| Package manuscript Markdown | `850f24306d6007d7d7eecbe55d0893a10f922d51062882def898b6ec750e46fa` |
| Package bibliography | `e26368824e47b1025359f78c4fa00ebc2967c226fb1967526ab27ee6a2beaff0` |
| Package manuscript PDF | `0895440ad5517c587bc454a0b9e0a7c5edfa9728bbd16e09adf96511bd929d4b` |
| Claims registry | `8899826f28e031adf0c56b974344dcbfc3f135a1f09f6a1fcac4b1ebc4f237e3` |

The development and package Markdown sources differ only in the bibliography
filename in YAML. The package PDF has 35 A4 pages; a fresh build reproduced the
generated TeX byte for byte and the extracted PDF text byte for byte.

## Gate results

| Gate | Coverage | Result |
|---|---:|---|
| Bibliography identities | 28/28 | PASS |
| Citation contexts | 67/67 clusters; 96/96 key occurrences | PASS |
| Ghost/orphan citations | 0/0 | PASS |
| Claims registry | 7/7 | PASS |
| Originality screen | 98/154 eligible paragraphs (63.64%) | PASS |
| Substantially revised prose | 70/70 paragraphs | PASS |
| Close/verbatim matches | 0/0 | PASS |
| Exact replay | 129,352 positives; 18 mutations detected | PASS |
| Normal versus `python -O` | all four suites | PASS |
| Source/build parity | Markdown, TeX, extracted PDF text | PASS |
| Disposable archive/fresh extraction | deterministic archive and full replay | PASS |

The originality classifications were 89 `ORIGINAL`, 9 attributed
`PARAPHRASE`, 0 `CLOSE_MATCH`, and 0 `VERBATIM`. The declared parent tag and
live parent explainer shared no exact 12- or 20-word prose shingle with the
audited manuscript.

## Correction made during the gate

Three citations to Mahatab--Sampath used a version-sensitive equation number.
The arXiv and indexed/published texts number the relevant determinant display
differently. The current manuscript now cites the stable `Theorem A.3` only in
all three contexts. The source, generated TeX, and PDF were rebuilt and the
citations reverified. This found-and-fixed locator issue is superseded in the
audited snapshot; historical Stage 3-prime reports remain unchanged as audit
history.

## Seven-mode AI research audit

| Mode | Final status | Basis |
|---|---|---|
| 1. Implementation bug passing self-review | CLEAR | explicit validators, normal/optimized replay, 18 mutations, independent ledgers and out-of-range fixtures |
| 2. Hallucinated citation | CLEAR | 28 identities and every citation context freshly verified |
| 3. Hallucinated result | CLEAR | every numerical statement traced to code and receipts |
| 4. Shortcut reliance | CLEAR | general results rest on proofs; finite checks are expressly subordinate |
| 5. Bug reframed as insight | CLEAR | the Smith theorem is proved algebraically before its regression evidence |
| 6. Methodology fabrication | CLEAR | methods, bounds, versions, algorithms, and counts match code and logs |
| 7. Early frame-lock | CLEAR | the earlier exact-object block caused a return to Stage 1, contribution reframing, and a second literature audit |

Mode 7 was suspected at the first integrity gate because the initial
determinant-complex frame missed exact monic and multiplication-Jacobian
antecedents. The workflow returned to Stage 1, added those sources, narrowed
the contribution boundary, and later incorporated signed-graph and
arithmetic-matroid antecedents. The final result is therefore centred on the
proved exact cross-weighted Smith calculation rather than the earlier scalar
resultant shadow.

## Nonblocking but material limitations

- The author field is unset, so an author-name-wide self-plagiarism search was
  not possible. The declared parent and supplied project lineage were checked.
- Web-search originality screening is not Turnitin, iThenticate, or a closed
  full-text database.
- The Python requirements are direct pins, not a hash-locked transitive
  environment; clean-machine portability is not established.
- The exact programs are producer-side regression evidence. They do not prove
  the quantified theorems and are not independent reproduction.
- The bounded literature search is not an absolute novelty or priority
  determination.
- Author, affiliation, contribution, funding, conflict, licence, and
  venue-specific disclosure metadata remain unset and block submission or
  release finality.

## Freeze authorisation

There is no unresolved Stage 4.5 integrity issue. The live payload may now
receive its canonical manifest, digest sidecar, and inventory. The final
deterministic archive must then be checked using an externally supplied digest,
with the fresh-extraction receipt stored outside the archive. Those delivery
objects close package transport integrity; they do not raise the assurance
level beyond the research-draft boundary stated above.
