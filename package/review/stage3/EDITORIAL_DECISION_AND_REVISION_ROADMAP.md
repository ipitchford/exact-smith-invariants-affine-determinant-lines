# Stage 3 Editorial Decision and Revision Roadmap

**Manuscript:** *Resultant-Character Lattices of Binary-Form Factorisations: An Affine Plücker Lift of the Classical Multiplication Jacobian*  
**Journal calibration:** *Linear Algebra and its Applications* (LAA)  
**Decision:** **Major Revision**  
**Process status:** Simulated/internal Stage 3 editorial synthesis; this is **not independent peer review**, external specialist validation, a priority determination, or an acceptance decision by LAA.

> **MANDATORY STAGE 3-to-4 CHECKPOINT:** This decision authorises no change to the manuscript, review package, or release artefacts. Revision must not begin unless and until the user explicitly approves crossing the Stage 3-to-4 checkpoint.

## 1. Evidence Boundary and Report Inventory

This synthesis uses the frozen field-analysis record and exactly five frozen Stage 3 reports. Consensus counts use only the four ordinary reports (EIC, R1, R2, and R3). The Devil's Advocate (DA) is tracked separately and has no consensus vote. Manuscript locations below are inherited from the reports; the synthesizer has not independently inspected or re-reviewed the manuscript.

### 1.1 Non-voting scope record

| Record | Function in this synthesis |
|---|---|
| `FIELD_ANALYSIS_AND_REVIEWER_PANEL.md` | Fixes the manuscript title, LAA calibration, reviewer remits, claim boundary, and mandatory Stage 3-to-4 checkpoint. It is not a review vote. |

### 1.2 Ordinary voting reports

| Report | Assigned remit | Recommendation read from report | Confidence | Principal strengths identified | Controlling concerns | Questions | Minor issues |
|---|---|---:|---:|---|---|---:|---:|
| `REVIEW_EIC.md` | LAA fit, contribution hierarchy, structure, submission path | **Major Revision** | **4/5** | Defensible contribution hierarchy; coherent determinant-to-lattice bridge; useful Smith/group-scheme consequences; responsible assurance language | \(h(\mathbf e)\) only partly evaluated; headline priority/context risk; classical machinery outweighs the arithmetic endpoint editorially; geometric payoff and submission metadata need strengthening | 4 | 5 |
| `REVIEW_R1_METHODOLOGY.md` | Integral proof rigour, scheme-theoretic precision, reproducibility boundary | **Minor Revision** | **4/5** | No fatal inference error found; integral composition, signs, modular-rank proof, and exact computation/proof boundary judged strong | Post-base-change multiplicity language; finite-locally-free/torsor presentation of Corollary 8.1; compressed descent; several sign/denominator conventions | 5 | 5 |
| `REVIEW_R2_DOMAIN.md` | Exact antecedents, resultant theory, contribution boundary | **Major Revision** | **4/5** | No fatal exact-object collision found beyond acknowledged antecedents; useful universal affine identity; substantive primitive cyclicity and prime-support result | Signed-graph and arithmetic-matroid context; partly definitional last Smith entry; formal-versus-specific content of Theorem 4.1; terminology; bounded rather than complete Smith theory | 7 | 12 |
| `REVIEW_R3_PERSPECTIVE.md` | Smith forms, lattice saturation, signed graphs, arithmetic matroids, group schemes | **Major Revision** | **4/5** | Sound arithmetic-combinatorial core; genuine primitive cyclicity; correct bad-prime support; scheme-aware group interpretation | \(h\) named rather than valued; missing standard framework; complete-edge versus square-chart conflation risk; proposed but unproved local \(p\)-adic presentation; critical-group boundary | 7 | 7 |

**Ordinary recommendation tally:** Major Revision 3; Minor Revision 1; Accept 0; Reject 0. All four ordinary reviewers report confidence 4/5, so no recommendation is down-weighted for low confidence. The majority is therefore decisive on revision severity, while subject-matter expertise controls issue-level arbitration.

### 1.3 Separate DA inventory

| Report | Consensus status | Confidence | Findings |
|---|---|---|---|
| `REVIEW_DA.md` | Non-voting adversarial track | No numerical confidence supplied | **0 CRITICAL**, **4 MAJOR**, **2 MINOR**. The report challenges the completeness/significance of the \(h\)-classification, the link between the rectangular complete-edge lattice and square normalisation charts, the intrinsic status of resultant normalisers, and the full-article significance case. |

## 2. Editorial Decision Letter

Dear Author(s),

Thank you for submitting *Resultant-Character Lattices of Binary-Form Factorisations: An Affine Plücker Lift of the Classical Multiplication Jacobian* for this simulated Stage 3 assessment calibrated to *Linear Algebra and its Applications*.

### Decision: Major Revision

The panel finds a credible LAA-facing paper in the arithmetic and combinatorial matrix content. In particular, the reports converge on the value of the integral determinant-to-character-lattice bridge, the proof that the primitive complete-edge cokernel is cyclic, and the exact bad-prime support criterion. The manuscript's careful separation of proof, producer-side symbolic checks, novelty evidence, and wider Keller/Hessian aspirations is also a material strength that must be preserved.

The present version is not yet ready for submission at this level. Three of four ordinary reviewers recommend Major Revision, all at 4/5 confidence. Their central concern is not a demonstrated fatal error: R1's methodology audit found the core proof architecture sound. The concern is that the paper's headline Smith claim currently ends with a determinantal gcd \(h(\mathbf e)\) whose valuations remain unevaluated, while the standard signed-graph, arithmetic-matroid, and toric-character context is not fully integrated. R3 proposes a potentially decisive \(p\)-local star presentation, but this is a reviewer-supplied theorem candidate, not an established manuscript result. It must be proved rigorously or rejected by a documented obstruction before it can affect the paper's claims. If it fails, the paper must explicitly fall back to the narrower theorem of primitive cyclicity, Smith shape, and exact prime support.

The revision must also separate the saturation index of the redundant complete-edge character list from determinants of selected square normalisation matrices, and it must make the scheme-level degree and multiplicity arguments as explicit as the integral determinant arguments. These are fixable matters, but together they change the main theorem framing, literature positioning, examples, and geometric interpretation. A point-by-point response and another Stage 3 verification review will therefore be required.

This decision is an internal simulation calibrated to LAA standards. It is not independent peer review, does not establish priority or correctness, and does not predict an LAA editorial outcome.

Sincerely,  
Stage 3 Editorial Synthesizer

## 3. Consensus and Disagreement Arbitration

### 3.1 Counting and weighting rules used

- `[CONSENSUS-4]` means all four ordinary reports agree on the point and action.
- `[CONSENSUS-3]` means three ordinary reports support the point/action; the fourth report's different view or non-participating remit is stated explicitly.
- `[SPLIT]` records a genuine severity/direction difference or a fragmented specialist issue without three affirmative votes. Silence is not converted into agreement. The editor resolves the split by evidence and assigned expertise.
- All ordinary confidence scores are 4/5 and receive full weight. Where the issue lies inside one reviewer's assigned specialty, expertise controls over raw vote count.
- DA findings never enter the four-report count. Corroboration by the DA may strengthen the risk assessment, but it cannot create ordinary consensus.

### 3.2 Points of agreement

#### [CONSENSUS-4] The established arithmetic core is real but narrower than a closed Smith classification

All four ordinary reports recognise substantive content in the proof that, after removing common content, the first \(k-2\) Smith factors are units/the primitive torsion cokernel is cyclic, and in Corollary 7.2's exact bad-prime support. The reports differ on whether more arithmetic is necessary for publication, but not on what the current nonformal achievement is.

**Binding editorial action:** State this content directly and consistently. Do not let the formally named top determinantal divisor obscure the cyclicity and support theorem actually proved.

#### [CONSENSUS-4] Preserve the manuscript's assurance and programme boundaries

EIC, R1, R2, and R3 all approve the separation between universal proof and producer-side exact checks, and all recognise the restraint concerning affine slices, Keller maps, Hessian consequences, independent reproduction, and priority.

**Binding editorial action:** Preserve these boundaries verbatim in substance. Neither successful revision nor simulated re-review may be described as independent verification, formalisation, priority resolution, or peer-reviewed acceptance.

#### [CONSENSUS-3] Major revision is the proportionate decision

EIC, R2, and R3 recommend Major Revision. R1 recommends Minor Revision because its proof audit found no major mathematical defect and regarded its requested scheme-theoretic changes as fuller exposition rather than new ideas.

**Disagreement type:** Severity disagreement.  
**Arbitration:** **Major Revision.** All confidence scores are equal, and the three Major recommendations concern the paper's headline contribution, literature position, and theorem framing rather than a proof error within R1's narrower remit. The decision does not overrule R1's positive proof assessment; it gives publication-level weight to the matrix-theoretic contribution question assigned to EIC, R2, and R3.

#### [CONSENSUS-3] The \(h(\mathbf e)\) endpoint and headline require a substantive resolution

EIC, R2, and R3 agree that defining \(h\) as the gcd of maximal minors leaves the final invariant partly unevaluated and makes phrases such as "complete Smith calculation" vulnerable. R1 does not request a stronger theorem; it finds the existing determinantal-divisor proof valid and notes that the manuscript correctly limits Corollary 7.2 to prime support.

**Disagreement type:** Severity and action disagreement.  
**Arbitration:** Require a theorem-level investigation of exact valuations. If the proposed local presentation is proved, promote the resulting local Smith theorem. If it is not proved, narrow the headline everywhere to primitive cyclicity/Smith shape plus exact bad-prime support and give an honest effective-computation statement. No unproved reviewer formula may enter the manuscript as fact.

#### [CONSENSUS-3] The graph/lattice antecedent framework must be strengthened

EIC requires a direct comparison with known weighted-incidence/critical-group/toric formulations; R2 and R3 specifically require signed-graph, arithmetic-matroid, and toric-arrangement context. R1 is the fourth report but expressly excludes priority and literature completeness from its remit; it neither corroborates nor opposes this finding.

**Disagreement type:** Coverage difference, not substantive opposition.  
**Arbitration:** Required. The revision must identify which parts are standard representable arithmetic-matroid multiplicity/GCD formalism, which are classical all-negative signed-incidence facts, and which are manuscript-specific modular and factorisation results. This is contextualisation, not a priority certificate.

#### [CONSENSUS-3] The manuscript architecture should make the arithmetic result visibly primary

EIC, R2, and R3 ask for the character-lattice problem, cyclicity/support theorem, and standard context to lead the contribution story. R1 considers the existing proof ordering effective and methodologically coherent.

**Disagreement type:** Direction and degree of restructuring.  
**Arbitration:** Reframe the introduction, theorem-status summary, abstract, and conclusion around the arithmetic endpoint, while retaining a rigorous proof chain. Compress or relocate only material whose detail obscures that hierarchy; do not sacrifice reproducible orientations or integral hypotheses.

### 3.3 Split and specialist findings

#### [SPLIT] R3's proposed local \(p\)-adic star presentation

R3 alone proposes the displayed local cyclic presentation and valuation formula. EIC and R2 ask whether valuations can be computed but do not supply or validate this proof; R1 does not assess it. R3 is, however, the assigned Smith/lattice specialist and reports 4/5 confidence.

**Arbitration:** Treat this as a **high-value required theorem investigation**, not as an accepted correction. The authors must prove the presentation over \(\mathbb Z_{(p)}\), including all edge cases and independence of choices, or provide a counterexample/precise obstruction. Only the proved branch may determine the revised theorem and title.

#### [SPLIT] Scheme-theoretic precision in multiplicity and generic degree

R1 identifies under-specified post-base-change multiplicity language and requests an fpqc-local Cartesian diagram and finite-locally-free proof for Corollary 8.1. R2 and R3 describe the result as sound/scheme-aware within its stated hypotheses; EIC values its characteristic sensitivity but defers technical proof detail.

**Arbitration:** R1's methodology expertise controls. The requested local hypotheses, torsor descent, and finite-locally-free diagram are required. This is an exposition/proof-precision repair, not a finding that Corollary 8.1 is false.

#### [SPLIT] Complete-edge saturation versus square polynomial charts

R3 explicitly distinguishes the redundant full-edge lattice index \(h\) from determinants of selected \((k-1)\)-edge matrices and from Laurent or arbitrary semi-invariant normalisers. The other ordinary reports do not make this an objection: R1 and R2 judge Corollary 8.1 sound on its own square-matrix hypotheses, while EIC asks for a clearer geometric payoff. DA Major findings 2 and 4 independently corroborate the interpretive risk but do not vote.

**Arbitration:** Require the distinction, without asserting that Corollary 8.1 is wrong. The revised paper must say exactly which lattice datum each geometric claim uses and must qualify the residual group as resultant-list-relative unless a universal property is actually proved.

#### [SPLIT] How much of the affine Plücker machinery should remain in the foreground

EIC and R2 regard much of the affine lift and contraction as formal once the scalar, kernel, and orientation are fixed, and request clearer separation or compression. R1 finds the integral proof architecture strong and R3 does not claim specialist authority over the resultant geometry.

**Arbitration:** This is a suggested rather than theorem-blocking revision. Add a general exterior-algebra/cofactor lemma or an explicit formal-versus-specific statement if it shortens and clarifies the contribution boundary; retain enough detail to audit the integral sign and base-change claims.

## 4. Traceable Revision Roadmap

### 4.1 Required P1 revisions

| ID | Required revision | Traceable sources | Deliverable and acceptance test | Estimated effort |
|---|---|---|---|---:|
| **P1-1** | **Resolve the exact arithmetic endpoint through a proof-level local investigation.** | EIC Weakness 1 and Questions 1-2; R2 Weakness 2 and Questions 3-4; R3 Weaknesses 1 and 4, stress test 4, Questions 1-2; DA Major 1 and Minor 2 | Prove or refute R3's proposed \(p\)-local star presentation. A successful proof must establish the module isomorphism, not merely matching orders; justify the use of a \(p\)-unit vertex; handle \(p=2\), \(k=3\), vanishing relation coefficients, and \(v_p(0)=\infty\); show independence of the chosen vertex; and derive the valuation formula and global Smith statement. Exact computations may test examples but are not proof. If the proposal fails, document the obstruction/counterexample and revise every headline to the proved fallback: primitive cyclicity/Smith shape plus exact bad-prime support. | **8-12 working days** |
| **P1-2** | **Reposition the main theorem in signed-graph, arithmetic-matroid, toric-character, and exact antecedent context, then restructure the contribution hierarchy.** | EIC Weaknesses 1-3 and Journal Fit/Originality; R2 Weaknesses 1-3 and 5, Literature Review, Missing Key References; R3 Weaknesses 1-2 and 5, Cross-Disciplinary Connections; DA Major 1 and 3 | Add direct comparison with all-negative signed incidence/frame-matroid theory, representable arithmetic matroids and (m(E)), toric arrangements, and adjacent Smith literature. State what is standard, formal, manuscript-specific, and unresolved. Include an introduction-level theorem-status table and move the complete-edge character problem and actual arithmetic conclusion earlier. Calibrate "complete Smith calculation" to the outcome of P1-1. Give exact antecedent locators and do not turn a bounded search into a priority claim. | **5-8 working days** |
| **P1-3** | **Repair the lattice-to-geometry interface and scheme-level degree/multiplicity presentation.** | R1 Weaknesses 1-3 and Questions 1-5; EIC Weakness 4 and Question 3; R3 Weakness 3, stress tests 5-6, Assumption Audit, Questions 3-4 and 7; DA Major 2 and 4, Minor 1 | Distinguish (i) the full redundant resultant-character lattice and \(h=m(E)\), (ii) a selected square edge matrix and \(|\det W_H|\), (iii) nonnegative polynomial monomials, (iv) Laurent units on the coprime open, and (v) arbitrary semi-invariants. Independently verify and, if correct, include the diagnostic \(\mathbf e=(1,2,2)\) example. State the base of the diagonalizable group scheme and make every residual-group claim resultant-relative unless a universal property is proved. Replace ambiguous post-base-change multiplicity wording by a localized ideal/order-one or Cartier-divisor statement with explicit hypotheses. Give the fpqc torsor/descent lemma and Cartesian finite-locally-free diagram showing the \(\nu\) étale branches and the total, separable, and inseparable degrees. The abstract must inherit all square-matrix and generic-finiteness qualifiers. | **6-10 working days** |

**Estimated P1 total:** 19-30 working days. The tasks overlap, but the main-theorem branch in P1-1 must be settled before finalising P1-2 wording and examples.

### 4.2 Suggested P2 revisions

| ID | Suggested revision | Traceable sources | Checkable result | Estimated effort |
|---|---|---|---|---:|
| **P2-1** | Isolate the formal exterior-algebra step and reduce editorial weight on derived machinery. | EIC Weakness 2 and Question 4; R2 Weakness 3 and Question 1; R3 Summary/Contribution wording | A general cofactor/Grassmann-duality lemma or a concise formal-versus-specific proposition separates scalar resultant input, kernel line, orientation chart, and Plücker completion. Orientation-heavy derivations are retained in a suitable proof location or supplement rather than deleted. | 3-5 days |
| **P2-2** | Tighten terminology and lattice conventions. | R2 Weakness 4, Terminology Precision, Questions 5-6; R3 Assumption Audit and Minor Issues; R1 Minor Issues | Define "pairwise inter-factor collision divisor," replace or formally define "normaliser," define residual group scheme and its base, state row/column and cokernel conventions, and reserve "torus isogeny" for the square/full-rank setting or map to the scheme-theoretic image. | 1-2 days |
| **P2-3** | Make sign, denominator, and isolated-component conventions independently auditable. | R1 Weakness 4, Questions 4-5, Minor Issues; R2 Minor Issues; EIC Minor Issues | State Vandermonde orientation and sign cancellation; present the degree-factor identity without apparent division or explain isolated-vertex cancellation; define isolated-tree bipartitions; standardise \(\mu_{g h(\mathbf e)}\), field notation, and theorem labels. | 2-3 days |
| **P2-4** | Add a compact arithmetic/geometric example table. | EIC Weaknesses 1 and 4 and Minor Issues; R2 Theoretical Framework and Questions 3-4; R3 stress tests 4-6; DA Minor 2 | Table records \(\mathbf d\), primitive \(\mathbf e\), \(g\), proved \(h\) or proved local valuations, Smith entries, \(m(E)\), selected-basis determinant(s), residual group scheme, and bad primes. Include an odd bad prime and a higher-valuation case only after they have been proved/independently calculated. | 2-4 days |

### 4.3 Suggested P3 editorial and submission revisions

| ID | Suggested revision | Traceable sources | Checkable result | Estimated effort |
|---|---|---|---|---:|
| **P3-1** | Align title, abstract, introduction, and conclusion with the proved branch. | EIC Title & Abstract/Conclusion; R2 Positioning and Minor Issues; R3 Minor Issues; DA Minor 1 | The title leads with the actual Smith/cokernel result; the abstract states the exact scope of Corollary 8.1 and says whether valuations are or are not known; the conclusion states the operational payoff without Keller/Hessian extrapolation. | 1-2 days |
| **P3-2** | Complete administrative submission metadata. | EIC Weakness 5 and Minor Issues; R2 final Minor Issue; field-analysis maturity record | Replace author, affiliation, contributions, funding, conflict, and licence placeholders. Keep AI-assistance disclosure separate from proof verification and authorship responsibility. This is mandatory before any submission build even though it does not affect the mathematical decision. | 0.5-1 day |
| **P3-3** | Complete copyediting and journal-format cleanup. | EIC Minor Issues; R1 Minor Issues; R2 Minor Issues; R3 Minor Issues | Fix the Section 6 numbering gap, exact theorem locators, \(K/\Bbbk\) ambiguity, terminology on generic scheme degree/étaleness, keywords, bibliography integration, and decide whether the Traditional Chinese abstract belongs in an LAA submission. | 1-2 days |

### 4.4 Checkable revision list

#### Priority 1 — required before re-review

- [ ] **P1-1.1** State R3's local \(p\)-adic presentation as a proposition under investigation, without presuming it true.
- [ ] **P1-1.2** Supply a complete proof of the local module isomorphism or a documented counterexample/obstruction.
- [ ] **P1-1.3** If proved, derive choice-independent \(v_p(h)\), the \(2\)-adic case, and the global Smith conclusion; if not proved, activate the narrow-claim fallback everywhere.
- [ ] **P1-1.4** Separate proof from exact computational regression checks.
- [ ] **P1-2.1** Add signed-graph/frame-matroid, arithmetic-matroid, toric-arrangement, and adjacent Smith context with exact locators.
- [ ] **P1-2.2** Identify \(h\) as the standard full-list saturation multiplicity \(m(E)\) while isolating the manuscript-specific cyclicity/support or valuation theorem.
- [ ] **P1-2.3** Add a traceable theorem-status table: classical input / formal consequence / candidate distinct content / unresolved extension.
- [ ] **P1-2.4** Make the arithmetic character-lattice question primary in the abstract and introduction and retain bounded novelty language.
- [ ] **P1-3.1** Distinguish full-edge (m(E)), square-basis determinants, polynomial monomials, Laurent units, and arbitrary semi-invariants.
- [ ] **P1-3.2** Independently verify the \(\mathbf e=(1,2,2)\) diagnostic before using it.
- [ ] **P1-3.3** Qualify the residual group as attached to the chosen resultant-character list unless a universal property is proved.
- [ ] **P1-3.4** Replace the post-base-change multiplicity sentence with an exact localized ideal/divisor formulation and explicit order-one hypotheses.
- [ ] **P1-3.5** Prove the fpqc torsor/descent step and display the finite-locally-free Cartesian diagram for Corollary 8.1.
- [ ] **P1-3.6** State total scheme degree, separable degree, inseparable factor, geometric points, and étaleness from that diagram, not from point counting alone.
- [ ] **P1-3.7** Give at least one concrete chart-level consequence while keeping \(h\) distinct from \(\lvert\det W\rvert\).

#### Priority 2 — strongly recommended

- [ ] **P2-1** Add the exterior-algebra/cofactor separation and shorten or relocate derived bookkeeping where useful.
- [ ] **P2-2** Tighten collision, normalising semi-invariant, residual-group, isogeny, and matrix-orientation terminology.
- [ ] **P2-3** Add the Vandermonde/sign, isolated-vertex, denominator, and notation clarifications.
- [ ] **P2-4** Add the arithmetic/geometric example table, using only proved values.

#### Priority 3 — editorial and submission completion

- [ ] **P3-1** Align title, abstract, introduction, and conclusion with the proved theorem branch and all scope qualifiers.
- [ ] **P3-2** Resolve author, affiliation, contribution, funding, conflict, licence, and AI-assistance metadata before submission.
- [ ] **P3-3** Complete numbering, cross-reference, bibliography, keyword, notation, and target-journal language cleanup.

### 4.5 Response and re-review requirements

- Submit a point-by-point response keyed exactly to `P1-1` through `P3-3` and their checklist subitems.
- For every required item, give the revised theorem/claim, exact manuscript location, proof or counterexample status, and any remaining limitation.
- Distinguish responses that change mathematics from responses that only change exposition.
- Supply a clean revised manuscript and a marked comparison, but do not overwrite the frozen Stage 3 evidence.
- A revised version requires Stage 3' verification review. Completion of the checklist is not itself acceptance.
- **Recommended revision window:** 6-8 weeks after explicit user approval to begin.

## 5. Devil's Advocate Issue Disposition

The DA found no CRITICAL issue, so the DA rule does not independently prohibit acceptance. The ordinary panel nevertheless requires Major Revision. DA findings remain separate from the consensus calculation as follows.

| DA item | Ordinary corroboration | Editorial disposition | Roadmap link |
|---|---|---|---|
| **DA-MAJOR-1:** \(h\) is the top determinantal divisor by definition; valuations and full group order remain unevaluated. | Strongly corroborated by EIC, R2, and R3; R1 confirms correctness but does not require valuation closure. | **Adopted as a required significance/classification issue, not as a claim of falsehood.** Prove the proposed local formula or narrow the headline. | P1-1, P1-2 |
| **DA-MAJOR-2:** The rectangular complete-edge index need not equal the determinant of any selected square polynomial chart. | Explicitly corroborated by R3; R1/R2 consider Corollary 8.1 sound on its own square-matrix hypotheses. | **Adopted as a required distinction.** Do not infer a chart of degree \(h\) without construction. | P1-3 |
| **DA-MAJOR-3:** The synthesis may be too slight for a full article without a stronger endpoint or intrinsic application. | Corroborated in severity by EIC, R2, and R3. | **Adopted as the publication-significance test.** A proved exact local theorem is the preferred strengthening; otherwise shorten/narrow the claim and make the concrete utility explicit. No Keller, Hessian, or affine-slice claim is required. | P1-1, P1-2, P1-3, P2-4 |
| **DA-MAJOR-4:** The resultant-generated residual group is not intrinsic among all possible semi-invariants. | Explicitly corroborated by R3; EIC asks for clearer geometric significance. | **Adopted as an interpretation qualifier.** Use resultant-list-relative language unless a universal property is proved. | P1-3 |
| **DA-MINOR-1:** The abstract overstates the scope of generic scheme degree. | R1 requests a scheme-level finite-flat formulation; R2 states the fixed-hypothesis scope. | **Adopted.** Add labelled-degree, algebraically closed field, square full-rank semi-invariant matrix, dense-open, and generically finite qualifiers. | P1-3, P3-1 |
| **DA-MINOR-2:** Current examples do not exhibit odd bad primes or higher valuations. | EIC, R2, and R3 all request more diagnostic families/examples. | **Adopted subject to proof.** Include such examples only after P1-1 establishes or independently computes them exactly. | P1-1, P2-4 |

**DA-CRITICAL disposition:** None to disposition. No required author acknowledgement is triggered under the DA-CRITICAL rule.

## 6. Mandatory Checkpoint

**STOP AFTER STAGE 3. No manuscript revision, package mutation, response-letter drafting, new theorem insertion, or release change begins from this roadmap alone. The user must explicitly approve crossing the Stage 3-to-4 checkpoint. Until that approval is recorded, the frozen manuscript and all Stage 3 evidence remain read-only.**
