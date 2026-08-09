# Bibliography Audit

Audit date: 9 August 2026  
Corpus: `references.bib`  
Scope: bibliographic identity, version selection, exact claim locators,
identifier resolution and source-to-entry consistency. This audit does not
establish priority, novelty, mathematical correctness, peer review beyond the
publication record, or independent reproduction.

## 1. Result

The bibliography contains 20 unique entries corresponding to every source in
`LITERATURE_MATRIX.md`. No duplicate DOI or citation key was retained. Where a
publisher, author repository, journal archive or stable technical reference
was available, its title, author list, year, venue, volume, issue, pages,
identifier and cited claim locator were reconciled against that record.

The focused antecedent re-audit made four material corrections to the earlier
ledger:

1. It added the direct coefficient-product Jacobian sources Artin (2022),
   Basu–Pollack–Roy (2006), and Bhargava–Cremona–Fisher–Gajović (2022).
2. It added the polynomial-multiplication singularity and projective tangent
   sources Chaperon–López de Medrano (2009) and Chipalkatti (2003).
3. It retained Hessert–Mallik as the 2023 version of record and the parent
   candidate under its exact Zenodo title and creator (`Anonymous`).
4. It added Stacks tag `00U0` for the universal monic multiplication/resultant
   chart and replaced the inapposite tag `0727` with tags `02VN` and `02VO`
   for fpqc locality of étaleness and finite locally free degree. Tags `023T`,
   `04TW`, and `07S7` remain for descent, torsors, and quotient existence.

## 2. Entry-level verification ledger

| Citation key | Verification route | Result and claim boundary |
|---|---|---|
| `Cayley1848` | Public-domain journal catalogue and the reprint in Cayley's collected papers | Author, title, journal, volume, year and pages verified. No DOI was found or inferred. |
| `Chardin1993` | Springer chapter DOI `10.1007/978-1-4612-2752-6_3`; author's article PDF; host-volume catalogues | Chapter title, author, pages, book title, series volume, publisher, year and editors verified. |
| `Jouanolou1991` | Elsevier/Crossref DOI `10.1016/0001-8708(91)90031-2` | Title, venue, volume 90(2), pages 117–263 and 1991 verified. |
| `Jouanolou1995` | Elsevier/Crossref DOI `10.1006/aima.1995.1042`; parent full-text audit | Author, venue, volume 114(1), pages 1–174 and 1995 verified. The DOI landing page indexes the English title *Invariant Aspects of Elimination*; the bibliography retains the original French title used in the article and mathematical catalogues. |
| `Jouanolou1997` | Elsevier/Crossref DOI `10.1006/aima.1996.1609` | Title, venue, volume 126(2), pages 119–250 and 1997 verified. |
| `Demazure2012` | EMS Press article record and DOI `10.4171/LEM/58-3-5` | Publisher record verifies volume 58, combined issue 3/4, pages 333–373 and publication date 31 December 2012. The combined issue from EMS is preferred to Crossref's shortened issue value `3`. |
| `GelfandKapranovZelevinsky1994` | Springer book record; original-edition library records | Authors, title, 1994 original publication, series, publisher and original ISBN verified. The DOI identifies Springer's electronic/reissued edition of the same work; this edition distinction remains explicit. |
| `DAndreaChipalkatti2007` | arXiv `math/0601705`; journal-repository record; printed article masthead | Principal authors, title, journal, volume 58, issue 2, pages 155–180 and appendix attribution verified. No journal DOI was located, so none is supplied. |
| `GrossmanKulkarniSchochetman1995` | Elsevier/Crossref DOI `10.1016/0024-3795(93)00173-W` | Full author names, title, journal, volume 218, pages 213–224 and 1995 verified. |
| `HessertMallik2023` | Taylor & Francis/Crossref DOI `10.1080/03081087.2022.2035307`; arXiv:2201.02580 | Version of record verified as volume 71(4), pages 513–527, print issue 2023; first published online 5 February 2022. The bibliography uses the print-year convention and retains the arXiv ID. |
| `BreidingKohnSturmfels2024` | Springer book DOI `10.1007/978-3-031-51462-3`; open-access book PDF | Authors, title, Oberwolfach Seminars 53, Birkhäuser Cham, 2024, eBook ISBN and DOI verified. Section 10.2, Proposition 10.7 and Corollary 10.8, p. 130 support the projective multiplication and degree use. |
| `Kurth1997` | Numdam version-of-record page and DOI `10.5802/aif.1574` | Author, exact mathematical title, journal, volume 47(2), pages 585–597 and 1997 verified. |
| `MahatabSampath2015` | Elsevier/Crossref DOI `10.1016/j.jalgebra.2015.04.006`; arXiv:1401.7696 | Full author names, title, *Journal of Algebra* 435, pages 223–262 and 2015 verified. No issue number is deposited, so none is invented. |
| `Artin2022` | AMS book DOI `10.1090/gsm/222`; AMS volume record; full-text §1.8 | Author, title, GSM volume 222, publisher, place and year verified. Lemma 1.8.5, p. 40 identifies the product-equation Jacobian with the transposed resultant matrix; Corollary 1.8.6 continues the singularity criterion on pp. 40–41. |
| `BasuPollackRoy2006` | Springer book DOI `10.1007/3-540-33099-2`; authors' second-edition PDF | Authors, title, second edition, series volume 10, publisher and year verified. The monic multiplication-Jacobian statement is §4.2.1, Proposition 4.20, pp. 109–110 in the standard second-edition posting; a later posted typesetting renumbers it Proposition 4.19, p. 122. |
| `ChaperonLopezDeMedrano2009` | NUMDAM version-of-record PDF and article record | Authors, title, *Astérisque* 323, pages 123–160 and 2009 verified. Theorem 1 is on pp. 126–127 and the arbitrary-factor monic criterion is Theorem 3 on pp. 132–133. No DOI was found or inferred. |
| `Chipalkatti2003` | Elsevier DOI `10.1016/S0021-8693(03)00336-3`; arXiv:math/0110224 | Author, title, *Journal of Algebra* 267(1), pages 246–271 and 2003 verified. Lemma 5.7, p. 268 and Corollary 5.8, p. 269 support the projective tangent and multiple-factor uses. |
| `BhargavaCremonaFisherGajovic2022` | Wiley version-of-record DOI `10.1112/plms.12438`; open-access publisher and author PDFs | Authors, title, *Proceedings of the London Mathematical Society* 124(5), pages 713–736 and 2022 verified. Lemma 2.6, p. 726 states both monic-by-monic and monic-by-arbitrary-formal-degree multiplication Jacobian formulas over an arbitrary ring. |
| `AnonymousBorderedJacobian2026` | Zenodo record 21855302 and DOI `10.5281/zenodo.21855302`; Evidence Press release page | Exact title, creator, release date, DOI and version `0.3-candidate` verified. The unrefereed producer-candidate boundary remains in the entry note. |
| `StacksProject2026` | Stacks tags `00U0`, `023T`, `04TW`, `07S7`, `02VN`, and `02VO`, read directly | `00U0`, Example 10.143.12 and Lemma 10.143.13 support the universal monic resultant chart and étale lifting; `023T` supports effective fpqc descent of quasi-coherent sheaves; `04TW` defines pseudo-torsors; `07S7` gives quotient existence and an fppf torsor for free finite locally free actions; `02VN` and `02VO` give fpqc locality of étaleness and finite locally free degree. Tag `0727` instead concerns a rank-one semi-invariant sheaf in an alternating Čech-complex setting and was removed from this claim mapping. |

## 3. Source-to-object adjudication

The metadata verification and the mathematical object match are separate
checks. The expanded ledger supports the following bounded conclusions:

- square, monic and one-factor-normalised two-factor multiplication-Jacobian
  identities are direct antecedents;
- arbitrary-factor monic corank and pairwise-coprimality criteria are direct
  antecedents;
- none of the added sources states the simultaneous non-monic all-factor
  complementary-minor/Plücker tensor, its orientation, the multi-border
  contraction, or the weighted complete-edge Smith calculation;
- the generic degree formula combines a classical projective root-partition
  degree with the standard scheme order of a torus-isogeny kernel and should
  be treated as synthesis rather than standalone novelty; and
- no fatal collision was located, but a bounded producer search cannot settle
  priority.

## 4. Normalisation decisions

- Citation keys follow `AuthorYear` or `AuthorAuthorYear`; existing parent keys
  were preserved where practical.
- Titles protect proper mathematical names and symbols (`Koszul`, `Smith`,
  `SL_2`, and `Z[X]`) against down-casing by journal styles.
- Page ranges use BibTeX's double-hyphen form.
- DOI fields contain bare DOI identifiers; URL fields contain resolvable links.
- Published versions are preferred over preprints. An arXiv identifier remains
  only when it gives provenance or open access without displacing the version
  of record.
- Original-language titles are retained for French sources, with TeX accents
  for compatibility with traditional BibTeX engines.
- Exact theorem, lemma, section and page locators are recorded in this audit
  even when the BibTeX entry itself appropriately remains at whole-object
  granularity.

## 5. Remaining caveats

1. **Basu–Pollack–Roy numbering drift.** The mathematical statement is stable,
   but proposition numbering differs between posted typesettings. Citations
   should include §4.2.1 and descriptive text rather than rely on the number
   alone.
2. **D'Andrea–Chipalkatti issue metadata.** Some catalogue output labels the
   item inconsistently, but the printed article masthead gives volume 58,
   number 2. The bibliography follows the printed item.
3. **GKZ edition identity.** The 1994 book and the later electronic/reprint DOI
   share content but have different ISBNs. An eventual house style may require
   a separately dated reprint citation.
4. **DOI absence.** No version-of-record DOI was verified for Cayley,
   Chaperon–López de Medrano, D'Andrea–Chipalkatti, or the continuously
   maintained Stacks Project. No DOI was invented.
5. **Parent candidate authorship.** Zenodo names the creator as `Anonymous` and
   does not deposit Evidence Press as a publisher. Evidence Press is release
   context, not substituted personal authorship.

## 6. Assurance boundary

This remains a producer-side Stage-1 metadata and exact-object audit. DOI
resolution and metadata agreement show that a cited object exists and that an
entry identifies it. Direct inspection of the cited pages shows what those
locators state. Neither establishes the truth of the present paper's theorem,
absolute priority, independent reproduction, formal verification, peer review,
or publication acceptance.

## 7. Mechanical validation

`biber` 2.21 accepted the complete 20-entry file in tool mode with data-model
validation enabled and emitted no warning or error. Separate read-only checks
confirmed 20 entry declarations, 20 distinct citation keys, 16 distinct DOI
fields, no duplicate DOI, and the four deliberate no-DOI exceptions documented
above.
