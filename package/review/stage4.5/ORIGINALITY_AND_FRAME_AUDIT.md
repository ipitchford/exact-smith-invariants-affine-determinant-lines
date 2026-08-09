# Stage 4.5 originality and frame-lock audit

## Audit identity

- Mode: Phase D final-check, fresh read-only audit
- Executed: 2026-08-09, Europe/London
- Audited manuscript: work/determinant-lines-character-lattices/stage4/package/manuscript/determinant_lines_character_lattices.md
- Audited manuscript SHA-256: 850f24306d6007d7d7eecbe55d0893a10f922d51062882def898b6ec750e46fa
- Stage-2 comparison manuscript SHA-256: bedebb820b895f997eff86710b404ce5ca7a6a2ac745de31edefb9dd8f28b3fb
- Parent release: Bordered Jacobian Foundations, tag object 6f400c15d9203f8ef6eb617a8c64a5dac66cd442, peeled commit 217f17d9f73e8b5a1bdb8d114bb1003dbed146bc
- Mutation boundary: no manuscript or package file was edited by this audit

## Verdict

**PASS.**

| Gate | Result | Blocking issue |
|---|---|---|
| Phase D paragraph originality | PASS | None |
| Declared-parent and internal-lineage reuse | PASS WITH BOUNDED-AUTHORSHIP NOTE | None |
| AI research failure mode 4: shortcut reliance | CLEAR | None |
| AI research failure mode 7: early frame-lock | CLEAR | None |
| Overall originality/frame-lock gate | PASS | None |

No sampled paragraph was graded CLOSE_MATCH or VERBATIM. No exact prose shingle of 12 or 20 words was shared with the immutable parent tag or its live Evidence Press explainer. No failure mode was SUSPECTED.

The authorship field remains a placeholder. Consequently, an author-name-wide search across all publications could not be executed. This does not create a match or a misconduct finding; it bounds the D2 conclusion to the declared parent and supplied project lineage.

## 1. Reproducible denominator and revision classification

The eligible-prose denominator was generated from the audited Markdown as follows:

1. remove YAML front matter;
2. include the English Abstract, Sections 1–11, and Appendices A–E;
3. exclude the Chinese abstract, keywords, administrative declarations, References, headings, tables, fenced code, and pure display-math blocks;
4. split at Markdown blank-line paragraph boundaries; and
5. retain blocks containing at least 20 English lexical words after citations, code spans, and LaTeX control words are removed.

This yields **154 eligible prose paragraphs in 17 major sections**.

To identify the mandatory Stage-4 stratum, each final paragraph was normalised by lowercasing and removing citation markup, LaTeX control words, and non-alphanumeric separators. Its maximum Python SequenceMatcher ratio against all eligible Stage-2 paragraphs was computed. A final paragraph with maximum ratio below 0.85 was classified as newly added or substantially revised. This reproducible heuristic classified **70 paragraphs** in that stratum.

Sampling used seed label **stage4.5-phaseD-v2**:

1. include all 70 newly/substantially revised paragraphs;
2. within each major section, rank remaining paragraphs by SHA-256 of seed-label plus normalised paragraph; and
3. add lowest-hash paragraphs until that section independently reaches ceil(section-denominator / 2).

The final sample is **98/154 = 63.64%**, includes **70/70 = 100%** of the revision stratum, and reaches at least 50% in every major section.

| Major section | Eligible | Sampled | Rate |
|---|---:|---:|---:|
| Abstract | 4 | 4 | 100.0% |
| 1. Introduction | 11 | 6 | 54.5% |
| 2. Conventions and antecedents | 9 | 5 | 55.6% |
| 3. A determinant-line composition lemma | 9 | 5 | 55.6% |
| 4. Affine Plücker lift | 14 | 7 | 50.0% |
| 5. Multi-border contraction | 5 | 3 | 60.0% |
| 6. Resultant-character minors | 14 | 7 | 50.0% |
| 7. Exact Smith invariants | 23 | 23 | 100.0% |
| 8. Generic-degree synthesis | 23 | 14 | 60.9% |
| 9. Exact computational evidence | 8 | 4 | 50.0% |
| 10. Antecedents and limitations | 13 | 7 | 53.8% |
| 11. Conclusion | 4 | 3 | 75.0% |
| Appendix A | 1 | 1 | 100.0% |
| Appendix B | 1 | 1 | 100.0% |
| Appendix C | 2 | 1 | 50.0% |
| Appendix D | 2 | 1 | 50.0% |
| Appendix E | 11 | 6 | 54.5% |

## 2. Web-search originality screen

For each sampled paragraph, the audit removed inline/display mathematics, citations, URLs, and Markdown decoration, then selected an 8–10-word characteristic window by document-frequency rarity with a fixed stopword list. The complete final query list appears in Appendix A.

Every one of the 98 final-sample fragments received:

- one exact quoted web search; and
- one unquoted companion search for nearby wording.

The search execution also retained two discarded-seed controls. There were 100 unique fragments overall; four quoted fragments were repeated during a batch handoff. Thus the raw log contains 104 quoted fragment executions and 100 unquoted executions, while the reported denominator and grades use only the 98 final-sample paragraphs.

Results:

- complete 8–10-word fragment reproduced in returned search snippets: **0/98**;
- contiguous run of at least six query tokens in unquoted returned snippets: **0/98**;
- apparent topical results were unrelated pages or cited classical subject matter, not close wording.

Search engines can ignore quotation marks and do not index all paywalled text. These are therefore screening results, not a universal corpus comparison.

### D1 grade summary

| Grade | Count | Proportion |
|---|---:|---:|
| ORIGINAL | 89 | 90.82% |
| COMMON_KNOWLEDGE | 0 | 0.00% |
| PARAPHRASE | 9 | 9.18% |
| CLOSE_MATCH | 0 | 0.00% |
| VERBATIM | 0 | 0.00% |

The nine PARAPHRASE grades are the explicitly cited antecedent/signed-graph/toric-context paragraphs P017, P018, P023, P055, P064, P087, P123, P124, and P125. Their wording is not close to returned sources and attribution is present.

## 3. Exact local shingle comparison

The local comparison removed fenced code, display and inline mathematics, citation markup, and LaTeX control sequences, then lowercased English lexical tokens. The primary misconduct threshold was an exact **20-word** prose shingle; **12-word** shingles were also checked as a sensitivity control.

| Corpus | Scope | 20-word result | 12-word result | Interpretation |
|---|---|---:|---:|---|
| Parent v0.3 tag | All 27 tagged Markdown/TeX/TXT/JSON/CFF files; 18,632 normalised tokens | 0 sampled/current paragraphs; 0 shingles | 0 paragraphs; 0 shingles | No exact parent prose reuse detected |
| Live parent explainer | Evidence Press index.md fetched 2026-08-09 | 0 shared shingles | 0 shared shingles | Public-page readback agrees with tag comparison |
| Stage-1 records | Seven scoping/research/antecedent records; 14,795 tokens | 0 paragraphs; 0 shingles | 1 paragraph; 1 shingle | The 12-word shingle already occurs in Stage 2; no Stage-1-only carryover |
| Development records | Eight outline/proof/configuration/audit records; 11,446 tokens | 2 paragraphs; 14 shingle hits | 8 paragraphs; 41 hits | Every shared shingle also occurs in Stage 2; no development-only carryover |
| Stage-2 manuscript | Frozen predecessor; 6,835 normalised prose tokens | 80 paragraphs; 1,886 shingle hits | 99 paragraphs; 2,659 hits | Expected direct revision lineage, not an external source |

The two development-record 20-word paragraphs are P101 in the root-partition construction and P152 in Appendix E. Both passages were already present in the frozen Stage-2 manuscript. Subtracting the Stage-2 shingle set leaves **zero** Stage-1-only or development-only matches at either 12 or 20 words.

## 4. D2 self-reuse boundary

The manuscript names the parent release in the Introduction and Appendix E, states that the rank-one result is a base case, and distinguishes the parent candidate from the child theorem package. The parent release is anonymous and the present author field is still “[Author name to be supplied]”.

Accordingly:

- comparison against the declared parent manuscript, all tagged parent text, and live parent explainer was executed and found no 12- or 20-word exact prose overlap;
- comparison against Stage 1, development records, and the Stage-2 manuscript was executed and the overlap was correctly attributable to the draft lineage;
- an external author-name publication search was **not executable** because no author identity was supplied.

Verdict: **PASS within the supplied and declared lineage; global author-wide self-plagiarism clearance is not claimed.**

## 5. D3 writing-characteristic screen

This is only a stylistic alert screen, not an AI-authorship determination. The paper contains high mathematical specificity, varied theorem/proof/limitation structures, and explicit producer-side AI disclosure. Formulaic-transition counts were low: Furthermore 0, Moreover 2, It is worth noting that 0, Additionally 0, and In addition 0. Hedging counts were may 5, could 1, might 0. No D3 threshold alert was triggered.

## 6. AI research failure mode 4 — shortcut reliance

**Status: CLEAR.**

This is a theoretical mathematics paper, not a benchmark-performance study. Its general theorems are supported by algebraic proofs; bounded exact computation is expressly labelled producer-side regression evidence. Section 9 records distinct exact implementations, ordinary and optimised runs, and deliberate negative controls, while also stating that the programs share a producer specification and cannot prove all-degree statements.

The likely shortcut analogue here would be treating successful finite enumeration or shared-spec backend agreement as proof. The manuscript does the opposite: it places the proof before computation, reports 18 detected negative controls, distinguishes finite checks from quantifiers, and preserves independent-reproduction limitations. No result depends on an incidental dataset feature, weak baseline, or hidden benchmark shortcut.

## 7. AI research failure mode 7 — early frame-lock

**Status: CLEAR.**

Evidence against frame-lock:

1. Stage-1 scoping made the all-factor determinant line the primary question, made Smith invariants a separately gated secondary question, and explicitly excluded arbitrary normalisers, affine-slice recognition, Keller-map uniqueness, and Hessian/Jacobian consequences.
2. Stage-1 synthesis already recorded that determinant line plus Smith form does not imply a Keller map and that the monic scalar shadow had classical antecedents.
3. The Stage-3 Devil’s Advocate identified a genuine frame-lock risk: treating the full resultant-character family as intrinsic among all semi-invariants.
4. Stage 4 did not suppress that objection. It proved a narrower universal statement for regular units on the fixed pairwise-coprime open, distinguishes full-edge, square-edge, polynomial-monomial, Laurent-unit, and arbitrary semi-invariant categories, and renames the object the unit-character residual group of that open.
5. The revised title, abstracts, and conclusion move the centre of gravity to the exact local/global Smith theorem only after the stronger local presentation was proved. This is a substantive reframing from the initial determinant-line emphasis.
6. The manuscript contains none of the checklist’s frame tells: “in hindsight”, “we realized/realised”, “surprisingly”, “unexpectedly”, “counterintuitively”, or “contrary to our hypothesis”.
7. Keller and four-dimensional Hessian applications remain explicitly conditional future work.

The final contribution is therefore explained by the revised, evidence-supported framing, not despite an unrevisable early commitment.

## 8. Issue list and limitations

### Blocking issues

None.

### Non-blocking limitations

1. The author placeholder prevents a publication-list-wide D2 search.
2. Web-search screening is not Turnitin, iThenticate, or a closed full-text database.
3. Cross-language and paywalled copying may escape this method.
4. Search-result snippets change over time and search engines may relax quotation marks.
5. This audit evaluates textual originality and pipeline framing; it does not establish theorem correctness, novelty, priority, independent reproduction, or peer review.

## Appendix A. Final sample and query audit trail

For every row below, the quoted search returned no full fragment and the unquoted companion returned no contiguous run of six or more fragment tokens. Grades use the Phase-D taxonomy.

| ID | Section | Lines | Stage-4 class | Quoted fragment | Grade |
|---|---|---:|---|---|---|
| P001 | Abstract | 13–20 | new/substantial | “primitive Pairwise resultants of labelled binary-form factors have characters in” | ORIGINAL |
| P002 | Abstract | 29–35 | new/substantial | “gcd computation It also shows that spanning-tree minors already generate” | ORIGINAL |
| P003 | Abstract | 37–51 | new/substantial | “pairwise-coprime open pairwise resultants generate all regular units modulo constants” | ORIGINAL |
| P004 | Abstract | 53–59 | new/substantial | “FLINT checks are producer-side regression evidence rather than independent reproduction” | ORIGINAL |
| P010 | 1. Introduction | 163–165 | new/substantial | “principal arithmetic object is the complete edge-character list Put and” | ORIGINAL |
| P011 | 1. Introduction | 179–181 | new/substantial | “positive gcd of the maximal minors of Section proves that” | ORIGINAL |
| P012 | 1. Introduction | 183–187 | new/substantial | “symmetric factorisation-free expression For this yields the complete Smith form” | ORIGINAL |
| P013 | 1. Introduction | 194–206 | new/substantial | “multi-border formula semi-invariant borders contribute Third resultant characters reduce integrally” | ORIGINAL |
| P014 | 1. Introduction | 220–223 | new/substantial | “algebraically closed field we prove after restriction to an explicit” | ORIGINAL |
| P015 | 1. Introduction | 229–235 | new/substantial | “semi-invariants recognise level sets as affine spaces classify Keller maps” | ORIGINAL |
| P017 | 2. Conventions and antecedents | 254–263 | unchanged supplement | “developed through modern determinant-of complexes formalisms by Jouanolou Chardin Demazure” | PARAPHRASE |
| P018 | 2. Conventions and antecedents | 265–276 | unchanged supplement | “monic polynomials including arbitrary numbers of factors These sources establish” | PARAPHRASE |
| P022 | 2. Conventions and antecedents | 314–316 | unchanged supplement | “not shorthand for an unspecified orientation Write for the submatrix” | ORIGINAL |
| P023 | 2. Conventions and antecedents | 327–338 | unchanged supplement | “square Sylvester map Artin identifies this Jacobian directly Basu Pollack” | PARAPHRASE |
| P024 | 2. Conventions and antecedents | 340–350 | unchanged supplement | “refinement recorded below retains the full complementary-minor tensor which maximal” | ORIGINAL |
| P026 | 3. A determinant-line composition lemma | 375–376 | unchanged supplement | “Set Assume that and scalars satisfy” | ORIGINAL |
| P027 | 3. A determinant-line composition lemma | 387–388 | unchanged supplement | “Let be a lift with extend by zero columns to” | ORIGINAL |
| P029 | 3. A determinant-line composition lemma | 414–415 | unchanged supplement | “put so Cauchy Binet with the intermediate rows in increasing” | ORIGINAL |
| P030 | 3. A determinant-line composition lemma | 443–444 | unchanged supplement | “elements of larger than Move the last column into increasing” | ORIGINAL |
| P031 | 3. A determinant-line composition lemma | 456–457 | unchanged supplement | “occurrences of cancel modulo two On the other hand expansion” | ORIGINAL |
| P034 | 4. Affine Plücker lift of the multiplication Jacobian | 500–502 | unchanged supplement | “makes the inductive contribution of the inherited kernel directions transparent” | ORIGINAL |
| P039 | 4. Affine Plücker lift of the multiplication Jacobian | 613–615 | unchanged supplement | “scalar resultants combine to while the determinant-one row change gives” | ORIGINAL |
| P042 | 4. Affine Plücker lift of the multiplication Jacobian | 660–669 | new/substantial | “criterion identifies pairwise root collision as the generic rank-loss set” | ORIGINAL |
| P043 | 4. Affine Plücker lift of the multiplication Jacobian | 671–674 | new/substantial | “any ring map and put Polynomial base change gives unconditionally” | ORIGINAL |
| P044 | 4. Affine Plücker lift of the multiplication Jacobian | 691–692 | new/substantial | “generators Consequently the order is exactly one along provided that” | ORIGINAL |
| P045 | 4. Affine Plücker lift of the multiplication Jacobian | 694–696 | new/substantial | “every with is a unit at and some maximal minor” | ORIGINAL |
| P046 | 4. Affine Plücker lift of the multiplication Jacobian | 698–706 | new/substantial | “Intersections and zero-factor strata can therefore carry extra scheme structure” | ORIGINAL |
| P048 | 5. Multi-border contraction | 742–748 | unchanged supplement | “part of the Laplace sign depending on The remaining parity” | ORIGINAL |
| P049 | 5. Multi-border contraction | 755–758 | unchanged supplement | “Cauchy Binet identifies the sum with Transposing this final matrix” | ORIGINAL |
| P050 | 5. Multi-border contraction | 760–762 | unchanged supplement | “semi-invariant Relative to the cocharacter basis let its integer character” | ORIGINAL |
| P055 | 6. Resultant-character minors via weighted signless incidence | 823–835 | new/substantial | “defect counts bipartite components and an unbalanced unicyclic component contributes” | PARAPHRASE |
| P057 | 6. Resultant-character minors via weighted signless incidence | 852–856 | new/substantial | “balance cancels the apparent exponent Within the stated component pattern” | ORIGINAL |
| P060 | 6. Resultant-character minors via weighted signless incidence | 873–876 | new/substantial | “removed The last row becomes Comparing determinants before cancelling any” | ORIGINAL |
| P061 | 6. Resultant-character minors via weighted signless incidence | 901–905 | new/substantial | “unoriented edge vertex incidence matrix If the unique tree component” | ORIGINAL |
| P062 | 6. Resultant-character minors via weighted signless incidence | 907–909 | unchanged supplement | “component on vertices supplies independent incidence rows Appending the restricted” | ORIGINAL |
| P063 | 6. Resultant-character minors via weighted signless incidence | 915–923 | unchanged supplement | “while two tree components leave more than one missing incidence” | ORIGINAL |
| P064 | 6. Resultant-character minors via weighted signless incidence | 925–930 | unchanged supplement | “unoriented graph incidence matrices The odd-unicyclic invertibility criterion also appears” | PARAPHRASE |
| P067 | 7. Exact Smith invariants of the unit-character lattice | 1040–1044 | new/substantial | “the Valuations at the distinct height-one primes give uniqueness Over” | ORIGINAL |
| P068 | 7. Exact Smith invariants of the unit-character lattice | 1046–1051 | new/substantial | “and it can enlarge after deleting further divisors We call” | ORIGINAL |
| P069 | 7. Exact Smith invariants of the unit-character lattice | 1090–1095 | new/substantial | “standard GCD rule For the original list the full-list multiplicity” | ORIGINAL |
| P070 | 7. Exact Smith invariants of the unit-character lattice | 1109–1111 | new/substantial | “exact local Smith presentation Let let be primitive and choose” | ORIGINAL |
| P071 | 7. Exact Smith invariants of the unit-character lattice | 1141–1143 | new/substantial | “ambient relation becomes which is equivalent to Each remaining edge” | ORIGINAL |
| P072 | 7. Exact Smith invariants of the unit-character lattice | 1149–1152 | new/substantial | “Tietze elimination proves the module isomorphism not merely an equality” | ORIGINAL |
| P073 | 7. Exact Smith invariants of the unit-character lattice | 1154–1156 | new/substantial | “edge between the pivots changes the displayed cyclic generator by” | ORIGINAL |
| P074 | 7. Exact Smith invariants of the unit-character lattice | 1182–1190 | new/substantial | “finitely generated abelian group is therefore finite Its primary localisations” | ORIGINAL |
| P075 | 7. Exact Smith invariants of the unit-character lattice | 1192–1197 | new/substantial | “DVR frameworks retain its isomorphism type and local invariant sequence” | ORIGINAL |
| P076 | 7. Exact Smith invariants of the unit-character lattice | 1201–1203 | new/substantial | “odd prime is nonzero precisely when exactly two degrees say” | ORIGINAL |
| P077 | 7. Exact Smith invariants of the unit-character lattice | 1225–1229 | new/substantial | “last line Swapping and does not change the truncated valuation” | ORIGINAL |
| P078 | 7. Exact Smith invariants of the unit-character lattice | 1259–1264 | new/substantial | “other degrees compute every excluded-pair gcd in gcd operations repeating” | ORIGINAL |
| P079 | 7. Exact Smith invariants of the unit-character lattice | 1266–1273 | new/substantial | “divides It cannot divide or else it would divide every” | ORIGINAL |
| P080 | 7. Exact Smith invariants of the unit-character lattice | 1284–1286 | new/substantial | “After localising at choose any unit pivot The star centred” | ORIGINAL |
| P081 | 7. Exact Smith invariants of the unit-character lattice | 1288–1290 | new/substantial | “unit vertex the star centred at has determinant up to” | ORIGINAL |
| P082 | 7. Exact Smith invariants of the unit-character lattice | 1296–1298 | new/substantial | “distinct remove from the star and add The resulting bent” | ORIGINAL |
| P083 | 7. Exact Smith invariants of the unit-character lattice | 1304–1309 | new/substantial | “Subtracting yields Hence these tree minors contain the ideal Conversely” | ORIGINAL |
| P084 | 7. Exact Smith invariants of the unit-character lattice | 1311–1313 | new/substantial | “Odd-unicyclic bases remain relevant as individual arithmetic-matroid multiplicities and square-chart” | ORIGINAL |
| P085 | 7. Exact Smith invariants of the unit-character lattice | 1354–1357 | new/substantial | “characteristic write with Its connected diagonalizable factor and prime-to tale” | ORIGINAL |
| P086 | 7. Exact Smith invariants of the unit-character lattice | 1366–1369 | new/substantial | “algebraic closure is not its total scheme rank in bad” | ORIGINAL |
| P087 | 7. Exact Smith invariants of the unit-character lattice | 1371–1374 | new/substantial | “comparison with toric arrangements over the standard identity gives exactly” | PARAPHRASE |
| P088 | 7. Exact Smith invariants of the unit-character lattice | 1382–1388 | new/substantial | “claim about an unlabelled rectangular target containing every root-partition branch” | ORIGINAL |
| P089 | 7. Exact Smith invariants of the unit-character lattice | 1412–1414 | new/substantial | “realise arbitrary higher odd and two-adic valuations The vector separates” | ORIGINAL |
| P091 | 8. Generic-degree synthesis and étaleness | 1437–1440 | new/substantial | “induced finite extension of function fields The proof below constructs” | ORIGINAL |
| P093 | 8. Generic-degree synthesis and étaleness | 1447–1453 | new/substantial | “normalised factorisation cover Fix the labelled degrees let be algebraically” | ORIGINAL |
| P096 | 8. Generic-degree synthesis and étaleness | 1477–1480 | new/substantial | “the number of geometric points in an algebraic closure of” | ORIGINAL |
| P102 | 8. Generic-degree synthesis and étaleness | 1571–1574 | new/substantial | “Base-change by the fpqc cover The torsor identity identifies the” | ORIGINAL |
| P103 | 8. Generic-degree synthesis and étaleness | 1593–1596 | new/substantial | “square is Cartesian because two points in one fibre differ” | ORIGINAL |
| P104 | 8. Generic-degree synthesis and étaleness | 1603–1610 | new/substantial | “of rank proving total scheme degree without counting geometric points” | ORIGINAL |
| P105 | 8. Generic-degree synthesis and étaleness | 1612–1619 | new/substantial | “Scheme-theoretically has length while its geometric-point count is Finally Corollary” | ORIGINAL |
| P106 | 8. Generic-degree synthesis and étaleness | 1626–1628 | new/substantial | “criterion gives the asserted taleness condition equivalently taleness is fpqc-local” | ORIGINAL |
| P107 | 8. Generic-degree synthesis and étaleness | 1632–1634 | new/substantial | “complete regular-unit character lattice Expressing each as an integral combination” | ORIGINAL |
| P108 | 8. Generic-degree synthesis and étaleness | 1640–1642 | new/substantial | “character matrix has determinant Theorem therefore gives the Laurent-unit normalisation” | ORIGINAL |
| P109 | 8. Generic-degree synthesis and étaleness | 1649–1655 | new/substantial | “still larger category and may require deletion of additional divisors” | ORIGINAL |
| P110 | 8. Generic-degree synthesis and étaleness | 1667–1669 | new/substantial | “whose maximal minors have absolute values Hence but no pair” | ORIGINAL |
| P111 | 8. Generic-degree synthesis and étaleness | 1691–1695 | new/substantial | “polynomial monomial chart can outperform every edge basis It does” | ORIGINAL |
| P112 | 8. Generic-degree synthesis and étaleness | 1697–1702 | new/substantial | “polynomial Keller map global affine-slice recognition is an additional requirement” | ORIGINAL |
| P114 | 9. Exact computational evidence | 1711–1715 | unchanged supplement | “first multifactor implementation uses SymPy and Berkowitz determinants It constructs” | ORIGINAL |
| P115 | 9. Exact computational evidence | 1722–1725 | unchanged supplement | “cases comprise symbolic Pl cker coordinates Five deliberate mutations omit” | ORIGINAL |
| P118 | 9. Exact computational evidence | 1742–1752 | new/substantial | “separate tier enumerates actual spanning trees by Pr fer sequences” | ORIGINAL |
| P119 | 9. Exact computational evidence | 1764–1769 | new/substantial | “negative controls Each default tier was run under ordinary Python” | ORIGINAL |
| P123 | 10. Antecedents, limitations, and the remaining programme | 1802–1818 | new/substantial | “present list Graph critical groups provide useful Smith-form context but” | PARAPHRASE |
| P124 | 10. Antecedents, limitations, and the remaining programme | 1820–1826 | new/substantial | “local invariant sequence rather than only its order Accordingly neither” | PARAPHRASE |
| P125 | 10. Antecedents, limitations, and the remaining programme | 1828–1839 | new/substantial | “factorisation-specific cross-weighted application of classical signed-incidence theory The strongest candidate” | PARAPHRASE |
| P126 | 10. Antecedents, limitations, and the remaining programme | 1841–1848 | new/substantial | “determinant-complex signed-graphic arithmetic-matroid toric-arrangement weighted-incidence or representation language Independent specialist” | ORIGINAL |
| P127 | 10. Antecedents, limitations, and the remaining programme | 1852–1856 | new/substantial | “classified and they may become units after deleting additional coefficient” | ORIGINAL |
| P128 | 10. Antecedents, limitations, and the remaining programme | 1858–1865 | new/substantial | “onto each branch-labelled image possible identifications of different branch translates” | ORIGINAL |
| P132 | 10. Antecedents, limitations, and the remaining programme | 1898–1911 | new/substantial | “investigate arbitrary semi-invariant vertical Jacobians after additional divisor deletions Refine” | ORIGINAL |
| P134 | 11. Conclusion | 1921–1928 | new/substantial | “shows that spanning-tree minors already determine the full arithmetic-matroid multiplicity” | ORIGINAL |
| P136 | 11. Conclusion | 1940–1948 | new/substantial | “graph-minor formula follows Standard arithmetic-matroid language then identifies the complete-list” | ORIGINAL |
| P137 | 11. Conclusion | 1950–1958 | new/substantial | “proofs and strengthened literature position receive genuinely independent specialist review” | ORIGINAL |
| P138 | Appendix A. Orientation and indexing conventions | 2018–2026 | unchanged supplement | “later factor Deleted source columns use zero-based indices The Pl” | ORIGINAL |
| P139 | Appendix B. Verification boundary | 2033–2037 | unchanged supplement | “include deliberate negative controls Larger exploratory cases were also tested” | ORIGINAL |
| P140 | Appendix C. Formalisation outline | 2043–2049 | unchanged supplement | “all-factor induction Laplace expansion Cauchy Binet and multi-border contraction integer” | ORIGINAL |
| P143 | Appendix D. Bounded antecedent and claim matrix | 2077–2083 | new/substantial | “bounded search Specialist review could still identify an equivalent formulation” | ORIGINAL |
| P147 | Appendix E. Self-contained affine lift of the classical two-factor Jacobian identity | 2158–2161 | unchanged supplement | “completeness transpose the Sylvester matrix and view it as Evaluating” | ORIGINAL |
| P148 | Appendix E. Self-contained affine lift of the classical two-factor Jacobian identity | 2186–2187 | unchanged supplement | “Vandermonde in the displayed order At the evaluated Jacobian row” | ORIGINAL |
| P149 | Appendix E. Self-contained affine lift of the classical two-factor Jacobian identity | 2199–2201 | unchanged supplement | “block parts After one source column is deleted one summand” | ORIGINAL |
| P151 | Appendix E. Self-contained affine lift of the classical two-factor Jacobian identity | 2215–2218 | unchanged supplement | “Moving it past the beta rows contributes and block expansion” | ORIGINAL |
| P152 | Appendix E. Self-contained affine lift of the classical two-factor Jacobian identity | 2263–2265 | unchanged supplement | “block and the existing row order is already block compatible” | ORIGINAL |
| P154 | Appendix E. Self-contained affine lift of the classical two-factor Jacobian identity | 2299–2301 | new/substantial | “exponents of read modulo two This table records the cancellations” | ORIGINAL |

## Final determination

**PASS — zero CLOSE_MATCH, zero VERBATIM, no undisclosed parent-text reuse detected, mode 4 CLEAR, and mode 7 CLEAR.**

The result remains a bounded heuristic originality screen. It should not be represented as a professional plagiarism-certificate result or as global clearance against publications that cannot be linked without an author identity.
