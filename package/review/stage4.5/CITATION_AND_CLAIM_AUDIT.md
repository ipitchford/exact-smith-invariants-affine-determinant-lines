# Stage 4.5 citation and claim-context audit

**Audit date:** 9 August 2026  
**Auditor posture:** fresh, read-only audit of the current Stage 4 package; no reliance on earlier citation audits  
**Standard:** zero unresolved citation, attribution, locator, factual-claim, priority-claim, ghost-citation, or claims-registry issue  
**Decision:** **PASS**

## 1. Scope and frozen source snapshot

The audit covered, in full:

- `package/manuscript/determinant_lines_character_lattices.md` (2,314 lines);
- `package/manuscript/references.bib` (28 records); and
- `package/integrity/claims.json` (7 claim records).

The files audited after the in-audit locator repair had these SHA-256 digests:

| File | SHA-256 |
|---|---|
| `determinant_lines_character_lattices.md` | `850f24306d6007d7d7eecbe55d0893a10f922d51062882def898b6ec750e46fa` |
| `references.bib` | `e26368824e47b1025359f78c4fa00ebc2967c226fb1967526ab27ee6a2beaff0` |
| `claims.json` | `8899826f28e031adf0c56b974344dcbfc3f135a1f09f6a1fcac4b1ebc4f237e3` |

Coverage was complete rather than sampled:

- 28/28 bibliography records were identity-checked;
- 24/24 DOI-bearing records were checked against DOI-registration metadata (23 Crossref, 1 DataCite), with publisher, author, repository, or full-text records used as additional checks;
- 28/28 bibliography keys are cited;
- 0 uncited bibliography entries and 0 undefined or ghost citation keys were found;
- all 67 citation clusters, comprising 96 individual cited-key occurrences, were read in manuscript context and checked for entailment;
- all explicit locators were checked against the cited source or an authoritative full-text copy;
- the full manuscript was screened for externally checkable factual assertions, attribution statements, and priority/novelty language; and
- 7/7 claims-registry records were reconciled with manuscript locations, evidence-set definitions, evidence artifacts, and assurance wording.

## 2. Zero-issue decision

The current source meets the Stage 4.5 zero-issue standard.

| Gate | Result |
|---|---|
| Bibliographic identities | **PASS — 28/28** |
| DOI/metadata accuracy | **PASS — 24/24 DOI records; 4/4 non-DOI records** |
| Citation existence and key integrity | **PASS — 28 cited keys; no ghosts; no orphan bibliography entries** |
| Citation-context entailment | **PASS — 67/67 clusters; 96/96 cited-key occurrences** |
| Explicit locators | **PASS — all current locators verified** |
| Factual and attribution claims | **PASS — full-manuscript screen; no unsupported external factual claim found** |
| Priority and novelty claims | **PASS — bounded and expressly non-absolute** |
| Claims registry | **PASS — 7/7 records coherent and schema-valid** |
| AI research failure mode 2 | **CLEAR — no nonexistent, miscited, misattributed, or context-inapt reference remains** |
| Unresolved issues | **0** |

## 3. In-audit repair and supersession record

One issue was found before the gate closed. Three current manuscript contexts had cited Mahatab--Sampath as “Theorem A.3 and eq. (A.17).” The theorem is stable, but the equation number is version-sensitive: the arXiv v3 text places the determinant identity at (A.17), while another indexed/published text numbers the corresponding display (A.18). Because the bibliography identifies the 2015 *Journal of Algebra* article, retaining a version-specific equation number was not zero-issue citation practice.

The current package was repaired during this audit. Lines 151, 338, and 1796 now cite only `MahatabSampath2015, Theorem A.3`; Appendix D already cited the work without an equation locator. Theorem A.3 was then rechecked in the source and still entails every current claim: the determinant of the polynomial Chinese-remainder map for monic factors is the product of the pairwise resultants. Thus:

- the substantive attribution is unchanged;
- the source-version ambiguity is removed;
- the current source has no remaining locator defect; and
- historical Stage 3-prime reports remain audit history and are not current manuscript source.

This repair supersedes the pre-gate observation. It is not an unresolved issue in the audited snapshot.

## 4. Bibliography identity audit: 28/28

The table records the authoritative identity source and the result. “Crossref + full text” means that registered metadata were checked and the cited mathematical content was also checked in a publisher, author, repository, or preprint copy.

| Key | Authoritative identity/source checked | Identity result | Cited-key occurrences |
|---|---|---|---:|
| `Cayley1848` | [Deutsche Digitale Bibliothek record](https://www.deutsche-digitale-bibliothek.de/item/BWTZ6SV3BZSX4RJUAWQFVZ6R277IQRIY) and primary scan | **PASS:** Arthur Cayley, “On the Theory of Elimination,” 1848, vol. 3, pp. 116--120 | 1 |
| `Chardin1993` | [Crossref DOI record](https://api.crossref.org/works/10.1007/978-1-4612-2752-6_3) and [author PDF](https://webusers.imj-prg.fr/~marc.chardin/publications/textes/06.MEGA92.pdf) | **PASS:** title, author, collection, volume, year, pages, DOI | 4 |
| `Jouanolou1991` | [Crossref DOI record](https://api.crossref.org/works/10.1016/0001-8708%2891%2990031-2), [publisher page](https://www.sciencedirect.com/science/article/pii/0001870891900312), and [author-uploaded full text](https://www.researchgate.net/profile/Jean-Pierre-Jouanolou/publication/243015856_Le_formalisme_du_rsultant/links/5a6984dea6fdcccd01a1d172/Le-formalisme-du-rsultant.pdf) | **PASS:** title, author, journal, volume/issue, year, pages, DOI | 5 |
| `Jouanolou1995` | [Crossref DOI record](https://api.crossref.org/works/10.1006/aima.1995.1042), [author-upload record](https://www.researchgate.net/publication/245506354_Aspects_invariants_de_l%27%27elimination) | **PASS:** French title in bibliography is the article title; Crossref also exposes an English translation; journal data and DOI agree | 1 |
| `Jouanolou1997` | [Crossref DOI record](https://api.crossref.org/works/10.1006/aima.1996.1609) and [author-uploaded full text](https://www.researchgate.net/profile/Jean-Pierre-Jouanolou/publication/256647087_Formes_d%27inertie_et_resultant_Un_formulaire/links/5a72db4c458515512076773e/Formes-dinertie-et-resultant-Un-formulaire.pdf) | **PASS:** title, author, journal, volume/issue, year, pages, DOI | 2 |
| `Demazure2012` | [Crossref DOI record](https://api.crossref.org/works/10.4171/LEM/58-3-5) and [EMS Press article](https://ems.press/journals/lem/articles/12104) | **PASS:** title, author, journal, volume/issue, year, pages, DOI | 3 |
| `GelfandKapranovZelevinsky1994` | [Crossref DOI record](https://api.crossref.org/works/10.1007/978-0-8176-4771-1) and Springer DOI landing record | **PASS:** authors, book title, series, publisher, year, ISBN/DOI identity | 3 |
| `DAndreaChipalkatti2007` | [arXiv primary record and text](https://arxiv.org/abs/math/0601705) and journal metadata | **PASS:** authors, title, journal, volume/issue, year, pages, appendix note | 2 |
| `GrossmanKulkarniSchochetman1995` | [Crossref DOI record](https://api.crossref.org/works/10.1016/0024-3795%2893%2900173-W) and [publisher record](https://www.sciencedirect.com/science/article/pii/002437959300173W) | **PASS:** authors, title, journal, volume, year, pages, DOI | 3 |
| `HessertMallik2023` | [Crossref DOI record](https://api.crossref.org/works/10.1080/03081087.2022.2035307) and [arXiv primary text](https://arxiv.org/abs/2201.02580) | **PASS:** authors, title, journal, volume/issue, year, pages, DOI/arXiv identity | 2 |
| `Zaslavsky1982` | [Crossref DOI record](https://api.crossref.org/works/10.1016/0166-218X%2882%2990033-6), [publisher record](https://www.sciencedirect.com/science/article/pii/0166218X82900336), and [full text](https://davinci.fmph.uniba.sk/~matok1/diplomovka/sources/Zaslavsky-former.pdf) | **PASS:** author, title, journal, volume/issue, year, pages, DOI | 3 |
| `Zaslavsky1983Erratum` | [Crossref DOI record](https://api.crossref.org/works/10.1016/0166-218X%2883%2990047-1), [SUNY authoritative record](https://researchconnect.suny.edu/en/publications/signed-graphs-to-t-zaslausky-discrete-appl-math-4-1982-47-74/), and [author publication list](https://people.math.binghamton.edu/zaslav/Tpapers/topical-pubs.html) | **PASS:** one-page 1983 correction to the 1982 article; descriptive bracketed title in bibliography is unambiguous; journal, volume/issue, page, DOI agree | 3 |
| `Moci2012` | [Crossref DOI record](https://api.crossref.org/works/10.1090/S0002-9947-2011-05491-7) and [arXiv primary text](https://arxiv.org/abs/0911.4823) | **PASS:** author, title, journal, volume/issue, year, pages, DOI | 4 |
| `DAdderioMoci2013` | [Crossref DOI record](https://api.crossref.org/works/10.1016/j.aim.2012.09.001) and [arXiv primary text](https://arxiv.org/abs/1105.3220) | **PASS:** authors, title, journal, volume/issue, year, pages, DOI | 4 |
| `FinkMoci2016` | [Crossref DOI record](https://api.crossref.org/works/10.4171/JEMS/600), [arXiv primary text](https://arxiv.org/abs/1209.6571), and [EMS Press article](https://ems.press/journals/jems/articles/13725) | **PASS:** authors, title, journal, volume/issue, year, pages, DOI | 3 |
| `ArdilaCastilloHenley2015` | [Crossref DOI record](https://api.crossref.org/works/10.1093/imrn/rnu050) and [arXiv primary text](https://arxiv.org/abs/1305.6621) | **PASS:** authors, title, journal, volume/issue, journal year, pages, DOI; 2014 online registration does not alter the 2015 volume year | 2 |
| `Lorenzini2008` | [Crossref DOI record](https://api.crossref.org/works/10.1016/j.jctb.2008.02.002) and [author accepted manuscript](https://dinolorenzini.franklinresearch.uga.edu/sites/default/files/inline-files/papers/PaperAccepted.pdf) | **PASS:** author, title, journal, volume/issue, year, pages, DOI | 1 |
| `HanusaZaslavsky2011` | [Crossref DOI record](https://api.crossref.org/works/10.1080/03081081003586852) and [arXiv primary text](https://arxiv.org/abs/0811.1930) | **PASS:** authors, title, journal, volume/issue, year, pages, DOI | 2 |
| `BreidingKohnSturmfels2024` | [Crossref DOI record](https://api.crossref.org/works/10.1007/978-3-031-51462-3) and [author full text](https://kathlenkohn.github.io/Papers/MFO_Seminar_MAG.pdf) | **PASS:** authors, title, series/volume, publisher, year, ISBN/DOI | 4 |
| `Kurth1997` | [Crossref DOI record](https://api.crossref.org/works/10.5802/aif.1574) and [Numdam primary text](https://www.numdam.org/item/AIF_1997__47_2_585_0.pdf) | **PASS:** author, title, journal, volume/issue, year, pages, DOI | 3 |
| `MahatabSampath2015` | [Crossref DOI record](https://api.crossref.org/works/10.1016/j.jalgebra.2015.04.006), [arXiv primary text](https://arxiv.org/abs/1401.7696), and [publisher page](https://www.sciencedirect.com/science/article/pii/S0021869315001830) | **PASS:** authors, title, journal, volume, year, pages, DOI | 4 |
| `Artin2022` | [Crossref DOI record](https://api.crossref.org/works/10.1090/gsm/222), [AMS DOI page](https://doi.org/10.1090/gsm/222), and [MIT author notes](https://math.mit.edu/classes/18.721/notes/ag-dec22-2021.pdf) | **PASS:** author, title, series/volume, publisher, year, DOI | 5 |
| `BasuPollackRoy2006` | [Crossref DOI record](https://api.crossref.org/works/10.1007/3-540-33099-2) and [full searchable text](https://paperzz.com/doc/8144640/algorithms-in-real-algebraic-geometry) | **PASS:** authors, title, edition, series/volume, publisher, year, DOI | 5 |
| `ChaperonLopezDeMedrano2009` | [Numdam primary record and text](https://www.numdam.org/item/AST_2009__323__123_0.pdf) | **PASS:** authors, title, Astérisque number, year, pages | 7 |
| `Chipalkatti2003` | [Crossref DOI record](https://api.crossref.org/works/10.1016/S0021-8693%2803%2900336-3) and [arXiv primary text](https://arxiv.org/abs/math/0110224) | **PASS:** author, title, journal, volume/issue, year, pages, DOI | 4 |
| `BhargavaCremonaFisherGajovic2022` | [Crossref DOI record](https://api.crossref.org/works/10.1112/plms.12438), [arXiv primary text](https://arxiv.org/abs/2101.09590), and [author PDF](https://www.dpmms.cam.ac.uk/~taf1000/papers/prob_roots.pdf) | **PASS:** authors, title, journal, volume/issue, year, pages, DOI | 5 |
| `AnonymousBorderedJacobian2026` | [DataCite DOI record](https://api.datacite.org/dois/10.5281/zenodo.21855302) and [Zenodo DOI landing page](https://doi.org/10.5281/zenodo.21855302) | **PASS:** exact title, Anonymous creator, Zenodo, issue date 8 August 2026, `0.3-candidate` status/version, DOI | 4 |
| `StacksProject2026` | [Stacks Project](https://stacks.math.columbia.edu) and the seven exact tags listed below | **PASS:** corporate author, online work, access year, and all cited tags | 7 |

## 5. Citation-context and locator audit: 67/67 clusters, 96/96 occurrences

Every citation cluster was read with its surrounding claim. Repeated citations were not assumed valid merely because an earlier occurrence was valid. The following matrix groups the checked occurrences by substantive claim while recording all cited sources and locators.

| Manuscript claim family and locations | Source/locator check | Verdict |
|---|---|---|
| Parent rank-one complementary-minor and bordered identities; lines 107--114, 1884--1890, Appendix D, Appendix E | DataCite/Zenodo identity and candidate status checked. The manuscript consistently labels the source unrefereed and producer-related; it does not launder the deposit into independent verification. | **PASS** |
| Two-factor coefficient-product Jacobian is Sylvester/resultant; lines 140--146, 325--338, 1782--1787, 2063, 2087--2089 | Artin §1.8 Lemma 1.8.5 explicitly says the Jacobian matrix is the transpose of the resultant matrix. Basu--Pollack--Roy §4.2.1, Proposition 4.19 explicitly says the Jacobian matrix of monic multiplication is the Sylvester matrix and its determinant is the resultant. Bhargava--Cremona--Fisher--Gajović Lemma 2.6 gives both monic--monic and monic--arbitrary identities over a ring. Stacks tag 00U0 gives the same monic chart and its étale/coprime condition. | **PASS** |
| Projective tangent injectivity and monic multifactor corank/pairwise-coprimality; lines 145--149, 268--276, 646--660, 1788--1792, 1867--1874, Appendix D | Chipalkatti Lemma 5.7 identifies tangent injectivity with coprimality and displays the Sylvester map. Chaperon--López de Medrano Theorems 1--4 include the arbitrary-factor corank formula; Theorem 3 gives local diffeomorphism iff factors are pairwise coprime. | **PASS** |
| Multifactor scalar determinant is the product of pairwise resultants; lines 149--151, 335--338, 1794--1796, Appendix D | Mahatab--Sampath Theorem A.3 gives the polynomial CRT determinant. Current citations use the stable theorem locator only. | **PASS** |
| Resultant divisibility and generic gcd of generalized Sylvester/Koszul minors; lines 152--155, 256--257, 1796--1798, Appendix D | Chardin §IV, Lemma 1 and Remark 1 state the resultant divisibility and valuation/generic-gcd conclusion for the relevant minors. | **PASS** |
| Classical elimination determinants and determinant-of-complexes context; lines 254--263, 1799--1800, Appendix D | Cayley primary scan is an elimination-determinant source. Jouanolou 1991 develops the resultant formalism; §§5.4.1--5.4.4 explicitly use complementary minors for generic linear forms and evaluate the resultant. Jouanolou 1997 explicitly develops Macaulay, Sylvester, Jacobian, and complex-boundary formulas. Chardin, Demazure, and GKZ are accurately used as broad framework references, not as claims that they contain the paper's exact affine tensor. | **PASS** |
| Binary discriminant/resultant Jacobian ideals; lines 265--267 and Appendix D | D'Andrea--Chipalkatti's abstract and body establish perfectness and explicit equivariant resolutions for the binary discriminant Jacobian ideal and the analogous resultant setting. The manuscript correctly distinguishes these gradient ideals from its rectangular multiplication differential. | **PASS** |
| Irreducibility/nonassociation of pairwise resultants; lines 660--666 and 1028--1044 | Jouanolou 1991, Proposition 2.3(iii), gives geometric irreducibility of the universal resultant. Pairwise nonassociation follows from the distinct coefficient-block multidegrees. The UFD unit argument is then self-contained. | **PASS** |
| Signed-incidence support, rank, odd-cycle factors, and erratum handling; lines 821--835 and 1806--1809, Appendix D | Zaslavsky Corollary 7D.1 identifies all-negative balance with bipartiteness; Corollary 7D.3(d),(j) gives dependence and rank; Lemmas 8A.2--8A.3 give determinants/powers of two. The manuscript does not rely on the corrected 7D.3(g) wording and cites the erratum. Grossman--Kulkarni--Schochetman and Hessert--Mallik support the incidence-minor/Smith and odd-unicyclic claims. | **PASS** |
| Arithmetic-matroid multiplicity, GCD rule, toric component count, and module-valued refinement; lines 1082--1095, 1192--1197, 1371--1374, 1820--1826, Appendix D | Moci §2.2 and D'Adderio--Moci §§1.4--1.5 define saturation multiplicity and the GCD rule; Moci Lemma 5.4 and D'Adderio--Moci Lemma 4.1 give the complex-toric connected-component count. Fink--Moci Definition 2.1, equation (2.1), §§5 and 6.1 retain the quotient module/local invariant sequence over rings and DVRs. | **PASS** |
| Adjacent equal-weight classical root lists, complete-incidence lcm result, and critical-group context; lines 1809--1817 and Appendix D | Ardila--Castillo--Henley §4.2 contains the classical signed-root vectors including equal-weight \(\varepsilon_i+\varepsilon_j\). Hanusa--Zaslavsky concerns the **lcm** of minors of a Kronecker-product complete-incidence matrix; the manuscript expressly distinguishes this from its gcd/Smith problem. Lorenzini supplies Laplacian/critical-group Smith context; the manuscript expressly denies a Laplacian-cokernel identification. | **PASS** |
| Projective multiplication fibres and labelled root-partition degree; lines 156--158, 1442--1509, 1802--1806, Appendix D | Breiding--Kohn--Sturmfels §10.2, Proposition 10.7 and Corollary 10.8, p. 130 establish finite projective polynomial multiplication and the generic factorisation/root-partition count. Chaperon Theorem 3 supports differential invertibility on the pairwise-coprime locus. Kurth pp. 585--597 represents binary forms via ordered linear factors modulo a scaling torus and symmetric group. | **PASS** |
| Scheme quotients, torsors, descent, finite local freeness, composition, and étaleness; lines 1509--1514, 1523--1529, 1571--1628 | Stacks tags [07S7](https://stacks.math.columbia.edu/tag/07S7), [04TW](https://stacks.math.columbia.edu/tag/04TW), [023T](https://stacks.math.columbia.edu/tag/023T), [02VO](https://stacks.math.columbia.edu/tag/02VO), [02VN](https://stacks.math.columbia.edu/tag/02VN), and [02K9](https://stacks.math.columbia.edu/tag/02K9) entail the specific quotient/torsor, fpqc descent, composition/base-change, and étale-locality uses. Tag [00U0](https://stacks.math.columbia.edu/tag/00U0) explicitly treats monic polynomial multiplication and the resultant Jacobian. | **PASS** |
| Contribution/priority boundary; abstract, Introduction, §10.1, Appendix D, Conclusion | Every classical ingredient named as classical has a supporting antecedent above. Candidate increments are described as “candidate,” “bounded-search,” “not located,” or “derived refinement.” The manuscript says equivalent results may exist and requires specialist search and independent proof reproduction. It makes no absolute priority claim. | **PASS** |

No citation is ornamental in a way that creates false support. Broad framework citations are used for broad framework claims; exact theorem claims carry exact locators; contrast citations accurately state what the cited work does **not** establish.

## 6. Factual and priority-claim audit

The full manuscript was screened, including abstracts, tables, theorem-introduction prose, §9 assurance statements, §10 contribution/limitations language, Appendix D, and Appendix E.

### External factual claims

All externally checkable factual claims were either:

1. directly supported by one of the verified citation families above;
2. an accurate description of the cited source's scope;
3. an internally checkable package fact (software/receipt/assurance status); or
4. explicitly presented as a mathematical assertion proved in the manuscript rather than as a literature fact.

No unsupported factual assertion requiring an external citation was found. In particular:

- the historical/source descriptions of Cayley, elimination complexes, signed graphs, arithmetic matroids, toric arrangements, and projective factorisation geometry are supported;
- the contrast claims concerning Hanusa--Zaslavsky, Lorenzini, D'Andrea--Chipalkatti, and the Jouanolou corpus are accurate and avoid false equivalence;
- the parent release date, version, repository identity, and unrefereed status agree with DataCite/Zenodo; and
- the manuscript's statements that its computations are producer-side, not independently reproduced, not formally verified, and not externally peer reviewed agree with the claims registry and package provenance.

### Priority and novelty claims

The priority language passes. The strongest originality statement is expressly a bounded negative search result: the exact cross-weighted local/global quotient calculation and related affine tensor were “not located in the bounded search.” The manuscript repeatedly adds that this is not proof of priority, that equivalent formulations may exist, and that specialist review remains necessary.

No sentence converts any of the following into priority evidence: a DOI, public deposit, exact computation, cross-engine agreement, package integrity, internal review, or producer reproduction. Classical ingredients are attributed as such. This is appropriately calibrated.

## 7. Claims-registry audit: 7/7

`claims.json` validates with zero errors against `claims.schema.json`. Every declared manuscript location exists, every computational evidence-set identifier is defined by the manifest builder and has normal and optimized receipts, and every novelty artifact identifier resolves deterministically to an existing package path. The artifact suffixes are path hashes, not content hashes:

- `artifact:provenance-stage1-antecedent-reaudit-md:f45348efe842` resolves to `provenance/STAGE1_ANTECEDENT_REAUDIT.md`;
- `artifact:provenance-stage4-arithmetic-literature-audit-md:19999f5d2110` resolves to `provenance/STAGE4_ARITHMETIC_LITERATURE_AUDIT.md`.

| Claim | Registry-to-manuscript/evidence reconciliation | Verdict |
|---|---|---|
| `DLCL-T1` | Theorem 4.1 exists. `sympy-plucker` and `flint-plucker-border` are defined and receipted. Status is `research-proof-draft`; independent/formal/peer evidence remains empty/false. Bounded novelty artifact exists. | **PASS** |
| `DLCL-T2` | Corollaries 5.1 and 5.2 exist. FLINT border evidence is appropriately narrower than a universal proof. Status and scope notes correctly distinguish the arbitrary stacked-row identity from the gradient/semi-invariant corollaries. | **PASS** |
| `DLCL-T3` | Theorem 6.1 and Corollary 6.2 exist. Character-lattice evidence is defined. `classical-antecedent-attributed` agrees with the signed-incidence framing and arithmetic-literature audit. | **PASS** |
| `DLCL-T4` | Theorems 7.1, 7.3, 7.4 and Corollaries 7.2, 7.5 exist. Character-lattice and local-Smith evidence are defined and receipted. The primitive/nonprimitive and characteristic scope notes match the theorem package. | **PASS** |
| `DLCL-C1` | §7.1, Corollary 7.5, and §8.2 exist. Scope correctly limits the unit claim to regular units on the fixed pairwise-coprime open and distinguishes labelled-image degree from an unlabelled target. | **PASS** |
| `DLCL-C2` | Theorem 8.1 exists. Registry correctly distinguishes scheme degree, separable degree, inseparable factor, and geometric point count and restricts finite local freeness to the constructed dense target open. | **PASS** |
| `DLCL-N1` | §10.1 and Appendix D exist. `not-found-in-bounded-search` and the scope notes match the manuscript's non-absolute priority language and both novelty-audit artifacts. | **PASS** |

The registry does not use computational checks as formal or independent evidence. All seven claims have `independent_reproduction: false` and `peer_reviewed: false`; formal declarations and formal evidence are null/empty. This is internally and externally consistent.

## 8. AI research failure mode 2 audit

The applicable failure mode is **non-existent, miscited, misattributed, or context-inapt citations**. The following adversarial checks were applied:

| Failure-mode-2 test | Result |
|---|---|
| Invented source, author, title, venue, or DOI | None found; 28/28 identities resolve |
| DOI points to a different work | None; 24/24 DOI records resolve to the intended item |
| Real source but wrong author/year/volume/pages | None found |
| Ghost cite key or undefined reference | None found |
| Bibliography entry never cited | None found |
| Exact locator absent or pointing to unrelated content | None in the current source; the sole version-sensitive equation locator was removed and superseded |
| Citation supports only a weaker/different claim | None found after in-context reading |
| Group citation masks a misattribution | None found; each member's role was checked, and contrast claims were checked separately |
| Secondary citation used to imply primary verification | None; primary/authoritative texts were opened for the high-risk theorem claims |
| Repository/deposit cited as peer review or independent reproduction | None; the parent is expressly labelled an unrefereed producer candidate |
| Priority claim inferred from failure to find a source | None; all negative-search language is bounded and expressly non-conclusive |

**Mode-2 result: CLEAR.**

## 9. Query and source log

Searches were run on 9 August 2026. Exact-title/DOI searches were used for identity resolution; theorem/section searches were used for entailment and locator checks. Representative query strings (punctuation variants and DOI case variants were also tried) were:

- `"On the Theory of Elimination" Cayley 1848 116 120`
- `"The Resultant via a Koszul Complex" Chardin DOI`
- `"Le formalisme du résultant" Jouanolou 1991 PDF`
- `"Le formalisme du résultant" "5.4.1"` and `"5.4.4"`
- `"Aspects invariants de l'élimination" Jouanolou PDF`
- `"Formes d'inertie et résultant" Jouanolou PDF Macaulay jacobien`
- `"Jacobian Ideal of the Binary Discriminant" D'Andrea Chipalkatti`
- `"Corollary 7D.1" "Corollary 7D.3" "Lemma 8A.2" Zaslavsky`
- `"Signed graphs" erratum 1983 248 DOI`
- `"Lemma 5.4" Moci toric arrangements components`
- `"Lemma 4.1" D'Adderio Moci toric arrangements`
- `"Definition 2.1" "Matroids over a Ring" Fink Moci`
- `"The Arithmetic Tutte Polynomials of the Classical Root Systems" section 4.2`
- `"Determinants in the Kronecker Product" lcm minors`
- `"Proposition 10.7" "Corollary 10.8" polynomial multiplication`
- `Kurth SL2 equivariant polynomial automorphisms binary forms quotient scaling torus`
- `"Theorem A.3" Mahatab Sampath determinant pairwise resultants`
- `"equation (A.17)" Mahatab Sampath` and `"equation (A.18)" Mahatab Sampath`
- `Artin Algebraic Geometry Lemma 1.8.5 Jacobian resultant matrix`
- `Basu Pollack Roy Proposition 4.19 Jacobian multiplication Sylvester resultant`
- `Chaperon López de Medrano Theorem 3 polynomial multiplication corank`
- `Chipalkatti Lemma 5.7 coincident root loci tangent multiplication`
- `Bhargava Cremona Fisher Gajović Lemma 2.6 multiplication Jacobian resultant`
- `Stacks tag 00U0 polynomial multiplication resultant Jacobian`
- exact-title plus DOI queries for every remaining DOI record.

Authoritative URL families and exact records used are listed in §4. DOI metadata queries used:

- `https://api.crossref.org/works/{DOI}` for each of the 23 Crossref DOI records;
- [DataCite JSON for the parent DOI](https://api.datacite.org/dois/10.5281/zenodo.21855302);
- direct arXiv records/full texts for `math/0601705`, `2201.02580`, `0911.4823`, `1105.3220`, `1209.6571`, `1305.6621`, `0811.1930`, `1401.7696`, `math/0110224`, and `2101.09590`;
- author or repository full texts linked in §4; and
- exact Stacks tags [00U0](https://stacks.math.columbia.edu/tag/00U0), [07S7](https://stacks.math.columbia.edu/tag/07S7), [02VO](https://stacks.math.columbia.edu/tag/02VO), [02VN](https://stacks.math.columbia.edu/tag/02VN), [023T](https://stacks.math.columbia.edu/tag/023T), [04TW](https://stacks.math.columbia.edu/tag/04TW), and [02K9](https://stacks.math.columbia.edu/tag/02K9).

## 10. Limitations

This is a citation, attribution, claim-context, metadata, and registry audit. It is not:

- an independent proof of the paper's mathematical theorems;
- an independent reproduction of the symbolic computations;
- a formal verification;
- external peer review;
- an exhaustive global novelty or priority search; or
- evidence that the manuscript will be accepted or influential.

Some publisher copies are access-controlled. In those cases identity was verified through Crossref and the publisher record, while claim content was checked in author-uploaded, arXiv, Numdam, MIT, EMS, Stacks, or other authoritative full-text copies. The 1995 Jouanolou item was identity-verified through DOI registration and its author-upload record; the grouped claim about the Jouanolou elimination corpus was independently entailed by the exact 1991 and 1997 full texts. This access limitation does not create an unresolved citation issue, but it is recorded so the audit is not mistaken for publisher-platform readback of every page.

The negative novelty result remains bounded by design. A later specialist may find a closer equivalent antecedent under different terminology without contradicting this audit; what this audit establishes is that the manuscript reports its present search boundary honestly.

## 11. Final Stage 4.5 judgement

**PASS.** In the frozen current snapshot, all 28 bibliography identities resolve, every bibliography item is used, every citation key is defined, all 67 citation clusters and 96 cited-key occurrences are contextually supported, all current locators are sound, factual and priority language is calibrated, the 7-record claims registry is coherent, and AI research failure mode 2 is clear. There are **zero unresolved Stage 4.5 citation or claim-context issues**.
