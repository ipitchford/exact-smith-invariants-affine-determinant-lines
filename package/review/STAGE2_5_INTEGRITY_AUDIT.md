# Stage-2.5 integrity audit

**Audit date:** 9 August 2026  
**Workflow:** producer-side academic-pipeline integrity gate  
**Independence:** internal adversarial audit, not independent reproduction,
specialist priority review, plagiarism-service certification, or peer review

## 1. Payload first inspected

The first integrity pass was bound to the following frozen Stage-2 payload:

| Object | Identity |
|---|---|
| Deterministic ZIP | SHA-256 `0cebce69d9e9e430a82be4c171e8ac528664875572f217a366ad009bfad04a7e`; 76 entries; 710,592 bytes |
| Package manifest | SHA-256 `dc83ab02c23748d297df35681d7ed513417c9efa4b54c4442bd2f11c2e1ac8ae` |
| Standalone Markdown | SHA-256 `dcb1e6b106abae6b248a53b60d69c116694a60fffb9ba89ea8a3a8674c4f5086` |
| Standalone PDF | SHA-256 `94c5a09ce04475f1385912058d8627af16d0abee9414e398423cbab5ef64d61b` |
| External fresh-extraction receipt | SHA-256 `c2bebb37e530bd3f4d3e3b4ca418725a880b8dbb1840e434adccd78c5c1053fd` |

The original ZIP and receipt are retained as superseded producer artefacts;
they are not treated as the identity of the remediated package.

## 2. First-pass result: blocked

The mathematical and computational audit found no contradiction, but the
integrity gate blocked on contribution framing and citation identity.

### 2.1 Claims, code, and data

The frozen package passed manifest and claim validation, deterministic archive
rebuild, fresh extraction, canonical receipt comparison, full normal and
`python -O` replay, and manuscript rebuild. The numerical ledger reconciled:

- 143 SymPy Plücker coordinates;
- 134 FLINT Plücker coordinates and two border determinants;
- 31,761 tree formulas, 52,741 general graph-minor formulas, and 351
  Smith/bad-prime cases;
- 85,132 positive exact comparisons in total; and
- 13 deliberate mathematical mutations detected.

Sixteen substantive theorem, corollary, scheme-degree, evidence, and assurance
statements were sampled against their proofs or executable records. No
mathematical or computational blocker was found. AI-failure modes concerning
implementation bugs, hallucinated numerical results, bugs promoted to
insights, and fabricated methodology were assessed clear within this
producer-side scope. Three claim-registry notes required correction: a stale
Theorem 4.1 status note, an overbroad description of the stated border theorem,
and a wrong section locator for the bounded-search claim.

### 2.2 Originality and shortcut checks

The text audit covered all 9,472 normalised manuscript tokens and sampled 29 of
83 eligible prose paragraphs (34.9%), spanning every main section and the
appendices. No public-source verbatim or close prose match was detected. The
small overlap with the immutable parent was formula-level; larger overlap with
Stage-1 and development records was disclosed internal derivational reuse.
This was a heuristic local/web comparison, not iThenticate or Turnitin, and
author-wide self-reuse could not be assessed because author names remain
unset.

The universal proof, all-index statements, negative controls, and explicit
generic/open-locus qualifications cleared the shortcut-reliance audit. The
frame-lock audit did not clear: exact searches found closer multiplication-map
antecedents absent from the frozen bibliography.

### 2.3 Citation defects and closer antecedents

All 15 frozen bibliography identities existed and all citation keys resolved,
but Stacks Project tag `0727` was inaccurately described as a finite-étale
quotient result. It is an eigensheaf lemma and was removed. The quotient proof
is instead supported by tags `07S7`, `02VO`, and `02VN`, with tags `023T` and
`04TW` retained for descent and torsor groupoids.

The first pass also located exact-object antecedents not represented in the
frozen contribution boundary:

1. Artin, *Algebraic Geometry: Notes on a Course* (2022), section 1.8,
   Lemma 1.8.5;
2. Basu--Pollack--Roy, *Algorithms in Real Algebraic Geometry*, second
   edition (2006), section 4.2.1;
3. Chaperon--López de Medrano, *Astérisque* 323 (2009), Theorems 1 and 3;
4. Chipalkatti, *Journal of Algebra* 267 (2003), Lemma 5.7 and Corollary 5.8;
5. Bhargava--Cremona--Fisher--Gajović, *Proceedings of the London
   Mathematical Society* 124 (2022), Lemma 2.6; and
6. Stacks Project tag `00U0`, Example 10.143.12 and Lemma 10.143.13.

These sources establish square monic or fixed-leading-coefficient
multiplication Jacobians equal to a resultant and monic/projective multifactor
rank criteria. Their omission made the initial novelty frame incomplete, so
the Stage-2.5 result was **BLOCKED** despite the clean theorem replay.

## 3. Focused Stage-1 return and remediation

The workflow returned to a bounded exact-object antecedent audit before
revising the manuscript. Its detailed ledger is preserved in
`provenance/STAGE1_ANTECEDENT_REAUDIT.md`.

No fatal exact collision was located for either:

- the simultaneous non-monic affine all-factor complementary-minor/Plücker
  tensor with universal integral orientation; or
- the degree-weighted complete-edge resultant-character Smith shape,
  residual diagonalizable group scheme, and bad-prime criterion.

The audit nevertheless narrowed the defensible contribution substantially:

- the multiplication-Jacobian/resultant phenomenon and multifactor
  coprimality rank criterion are established background;
- the affine Plücker tensor is an explicit coordinate-complete lift and its
  multi-border formula is a formal contraction;
- the graph engine is classical signless-incidence theory in a
  factorisation-specific weighted specialization;
- the generic degree is a synthesis of the classical root-partition count and
  torus-isogeny scheme order; and
- the strongest candidate substantive result is the complete-edge
  resultant-character Smith calculation and exact bad-prime support.

The manuscript, bibliography, literature matrix, claim registry, provenance,
and package status were revised to this boundary. The historical Stage-1
report and initially inspected archive identity remain recorded rather than
silently overwritten.

## 4. Second-pass result

**Status:** **PASS WITH NOTES** after focused remediation and re-audit.

The manuscript bytes audited in the second pass have SHA-256
`bedebb820b895f997eff86710b404ce5ca7a6a2ac745de31edefb9dd8f28b3fb`.
Both canonical manuscript copies matched. The revised manuscript has 8,299
whitespace-delimited words, compiles to 26 pages, and cites all 20 defined
bibliography entries.

### 4.1 Claims, data, and replay

The provisional revised manifest contained 60 artifacts and three evidence
sets. Manifest, claim, and canonical-receipt checks passed under normal Python
and `python -O`. All seven registry locations and theorem/corollary names
resolved in both Markdown and generated TeX. The numerical ledger again
reconciled to 85,132 positive comparisons and 13 detected mutations.

A deterministic provisional archive passed safe fresh extraction, full exact
replay, and manuscript rebuild. Two non-blocking claim-metadata notes found in
this pass were corrected before final freezing: Corollary 8.1 is now
machine-labelled `classical-antecedent-attributed`, and every bounded-search
claim links the manifested Stage-1 antecedent re-audit. The final manifest and
external fresh-extraction receipt must therefore be regenerated after this
report is included; the delivered standalone audit records those final
identities.

AI-failure modes 1, 3, 5, and 6 were assessed **CLEAR** within the stated
producer-side boundary: executable counts trace to canonical receipts;
normal/optimized parity and explicit negative controls are present; no bug or
unexpected output is promoted into a theorem; and the methods described in
Section 9 match the packaged code and environment records.

### 4.2 Citation audit

All 20 bibliography identities were reconciled against primary, publisher,
DOI, or authoritative technical records. All 20 keys are cited, with no
undefined, unused, duplicate, or ghost key. Eighteen of 52 mechanically
enumerated bracketed citation clusters were inspected in context (34.6%): all
18 were supported paraphrases, with zero suspected or verbatim cases.

The citation auditor confirmed that tag `0727` occurs only in six
review/provenance notes documenting its historical removal; it is absent from
the manuscript and BibTeX and supports no active inference. The active
Basu--Pollack--Roy citations use stable section locator 4.2.1 rather than the
proposition number that varies between posted typesettings. This slice was
assessed **CLEAR**.

### 4.3 Originality, shortcut reliance, and frame lock

The reproducible second-pass denominator contained 84 eligible top-level prose
paragraphs with at least 30 lexical Pandoc `Str` tokens, excluding headings,
display equations, tables, list-only blocks, and references. Thirty-six were
audited (42.9%), spanning the abstract, every main section, eligible
appendices, and seeded-random supplements; the title and short/list-only
appendices were inspected outside the denominator.

The 36 grades were 24 `ORIGINAL`, 11 attributed `PARAPHRASE`, one
`COMMON_KNOWLEDGE`, zero `CLOSE_MATCH`, and zero `VERBATIM`. Exact fragment
searches and whole-text comparisons against accessible close antecedents found
no relevant prose match of eight or more normalised words. Parent overlap at a
ten-token threshold was approximately 0.71% and formulaic; overlap with the
unpublished Stage-1 and proof-revision records was disclosed internal
derivational reuse.

AI Mode 4, shortcut reliance, was assessed **CLEAR**: the universal statements
rest on ring-level proofs, not finite examples, and the computations remain
explicitly subordinate regression evidence. AI Mode 7, frame lock, was
assessed **CLEAR after recorded remediation**: the title, abstract, Sections
2, 4--8 and 10, conclusion, and Appendices D/E now consistently separate
classical antecedents, the derived affine lift, formal corollaries, attributed
syntheses, and the complete-edge Smith result as the strongest distinct
candidate.

### 4.4 Protected classes and dual use

The work is abstract algebra and elimination theory. It contains no human
participant data, protected-class inference, operational targeting, hazardous
protocol, or material dual-use capability. No additional integrity escalation
was triggered on those grounds.

### 4.5 Disposition

The initial Stage-2.5 block was genuine and remains part of the record. The
focused return to Stage 1 and the revised second pass clear that block. The
payload may proceed to the explicit Stage-2.5-to-Stage-3 checkpoint as a
**research-proof draft**. It does not cross that checkpoint automatically.

## 5. Assurance boundary

Even after remediation, this gate can establish only producer-side structural
and scholarly-integrity checks within the recorded corpus. It cannot establish
absolute novelty, specialist priority resolution, independent reproduction,
formal verification, external peer review, author identity, or publication
readiness. The originality check was heuristic local/web comparison rather
than iThenticate or Turnitin; the Chinese abstract was framing-checked but not
independently similarity-searched; Artin's exact lemma was checked in the
official MIT text while AMS printed pagination was not independently reopened;
and author-wide self-reuse could not be assessed because author identity is
unset. No tag, DOI, public deployment, or release is authorised.
