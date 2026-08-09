# Stage 3-prime package-assurance review

**Object reviewed:** `work/determinant-lines-character-lattices/stage4/package/`  
**Review mode:** read-only re-review of the revised child package  
**Date:** 9 August 2026  
**Recommendation:** **MINOR REVISION**  

This is an internal producer-side verification review. It is not external peer
review, independent reproduction, specialist priority certification, formal
verification, acceptance, publication, or release.

## 1. Bottom-line assessment

The Stage-4 package has a coherent mathematical and computational evidence
spine. The seven registered claims point to real manuscript units; the four
evidence sets have the advertised frozen hashes and totals; all 28 bibliography
keys are both defined and cited; the package manuscript rebuilds cleanly; and
the normal/optimized canonical receipts agree exactly. No stale theorem claim,
missing evidence set, broken build interface, or forbidden external-assurance
claim was found.

The package is not yet ready to freeze into a manifest, however. Three
package-facing records are materially out of synchronisation with the revised
payload: the bibliography audit still certifies the former 20-entry corpus,
the assurance table claims not-yet-generated integrity artifacts as a current
state, and the response letter names the pre-packaging source paths rather than
the included package paths. Two smaller consistency repairs are also needed:
the `DLCL-C1` evidence mapping differs between `claims.json` and
`CLAIM_LINEAGE.md`, and `STATUS.md` describes only the six Stage-1 raw receipts
while summarising four suites. These are documentation and traceability defects,
not failures of the revised theorems or exact checks, so the appropriate
recommendation is **MINOR REVISION**, with all repairs completed before manifest
generation.

## 2. Checks performed and results

| Check | Result | Evidence |
|---|---|---|
| Claim schema and protected-assurance scan | PASS, with manifest cross-check correctly skipped because no manifest exists yet | `tools/check_claims.py`: 7 claims, 0 protected assertions |
| Claim-to-manuscript locations | PASS | T1: Theorem 4.1; T2: Corollaries 5.1--5.2; T3: Theorem 6.1 and Corollary 6.2; T4: Theorems 7.1, 7.3--7.4 and Corollaries 7.2, 7.5; C2: Theorem 8.1 |
| Novelty artifact IDs | PASS | Both deterministic IDs in `claims.json` match the corresponding provenance paths |
| Independent-reproduction and peer-review flags | PASS | Every claim has `independent_reproduction: false`, `peer_reviewed: false`, and empty external-evidence fields |
| Frozen checker and baseline hashes | PASS | All four checker digests and all eight baseline-receipt digests match `verification/run_all.py` and `verification/README.md` |
| Canonical receipt parity | PASS | Normal and optimized canonical JSON are byte-identical for all four suites |
| Verification totals | PASS | 143 + 136 + 84,853 + 44,220 = 129,352 positive comparisons; 5 + 4 + 4 + 5 = 18 negative controls |
| Raw stdout binding | PASS | Each of the eight environment-receipt stdout digests matches its frozen baseline receipt |
| Bibliography key completeness | PASS mechanically | 28 definitions, 28 cited keys, no missing or unused key |
| BibTeX data model | PASS mechanically | Biber 2.21 tool-mode validation completed without warning or error |
| Manuscript build interface | PASS | Temporary-copy two-pass build succeeded; regenerated TeX was byte-identical to packaged TeX; PDF is 35 A4 pages |
| Python and shell interfaces | PASS statically | Runner and integrity-tool Python sources parse; manuscript build script passes `bash -n` |
| Stage-4 source-to-package copies | PASS | Proof note, adversarial audit, geometry note, literature audit, response, tracking record, checker, and two raw receipts are byte-identical to their Stage-4 source artifacts |
| Manifest/archive | NOT RUN, as required | No manifest or archive was generated during this review |

## 3. Revision-response traceability

The following table audits whether the response letter's substantive statements
have corresponding included artifacts. It does not reclassify those internal
artifacts as independent evidence.

| Roadmap block | Author response | Package verification | Status |
|---|---|---|---|
| P1-1 exact arithmetic endpoint | Claims a proved local module isomorphism, exact valuations, global formula, tree-gcd equality, scaled Smith form, and separate computation | Theorems 7.1, 7.3--7.4; Corollaries 7.2, 7.5; proof note; adversarial audit; `local-smith` suite with 44,220/5 | FULLY TRACEABLE within producer scope |
| P1-2 literature and contribution hierarchy | Claims signed-graph, arithmetic-matroid, toric, matroid-over-ring, root-list, and adjacent Smith context | Revised Sections 1, 6, 7, 10, Appendix D, and Stage-4 arithmetic literature audit are present | FULLY TRACEABLE, bounded-search status preserved |
| P1-3 lattice-to-geometry interface | Claims five categories, `(1,2,2)` diagnostic, regular-unit scope, exact base-change multiplicity, and fpqc finite-locally-free proof | Revised Sections 4.1, 7.1, 7.5, 8.1--8.2 and the geometry-interface note contain the stated changes | FULLY TRACEABLE within manuscript-proof scope |
| P2 formal/expository repairs | Claims terminology, signs, graph conventions, examples, and contribution hierarchy were repaired | The revised manuscript contains the stated terminology, tree dependency, prime-to-`p` terminology, examples, and status table | FULLY TRACEABLE |
| P3-1/P3-3 title, framing, copyediting, and build | Claims 28 cited references and a clean 35-page build | Mechanically confirmed | FULLY TRACEABLE |
| P3-2 administrative metadata | Deliberately unresolved | `UNSET`/placeholder fields remain and submission/release is expressly blocked | CORRECTLY UNRESOLVED |

The first-round response is therefore substantively faithful. The residual
problem is package-relative naming, described below.

## 4. Actionable findings

### A1. The bibliography audit certifies the former 20-entry corpus, not the revised 28-entry corpus

**Severity:** Minor, but blocking final payload freeze.  
**Locations:** `provenance/BIBLIOGRAPHY_AUDIT.md`, especially Sections 1, 2,
and 7; compare `STATUS.md` and the revised `references.bib`.

The included audit says that `references.bib` contains 20 entries and that
Biber validated a complete 20-entry file. The actual packaged bibliography has
28 entries, including eight Stage-4 signed-graph/arithmetic-matroid/Smith
sources. `STATUS.md` and the response letter correctly report 28/28, and this
review independently confirmed that count and Biber validation. The problem is
therefore stale provenance, not a broken bibliography.

**Required repair:** Preserve the historical Stage-1 audit as historical, but
either relabel it explicitly as a 20-entry Stage-1 audit and add a
Stage-4 bibliography delta audit, or issue a clearly versioned 28-entry
superseding audit. The new record should enumerate the eight added keys,
confirm 28 defined/28 cited/no missing/no unused, record the Biber result, and
retain the bounded novelty and metadata-only assurance boundary. Update
`README.md`/`STATUS.md` to name the current audit artifact.

### A2. `ASSURANCE.md` overstates the current payload-integrity state

**Severity:** Minor, but an assurance-boundary defect.  
**Location:** `ASSURANCE.md`, assurance-dimensions row “Payload integrity”.

The row currently lists a canonical manifest, SHA-256 sidecar, inventory, and
deterministic archive as the **current state**. At this review checkpoint none
of those generated objects exists, by deliberate design. The schemas and
builders exist; that is a different assurance state. An archive will also
normally live outside the package it contains.

**Required repair:** Before Stage 4.5, change the current state to “schemas and
deterministic manifest/archive/fresh-extraction interfaces prepared; generated
manifest, sidecar, inventory, archive, and external extraction receipt pending.”
After successful final generation, update only the objects that actually
exist and identify the archive/receipt as external where applicable. Do not
describe tool availability as a completed integrity result.

### A3. The response letter's artifact names do not resolve inside the child package

**Severity:** Minor traceability defect.  
**Location:** `review/STAGE4_RESPONSE_TO_REVIEWERS.md`, revision identity and
“Verification supplied with the revision”.

The response names `manuscript-revised.md`, `LOCAL_SMITH_THEOREM.md`,
`LOCAL_SMITH_ADVERSARIAL_AUDIT.md`, `ARITHMETIC_LITERATURE_AUDIT.md`,
`GEOMETRY_INTERFACE_REVISIONS.md`, root-level `verify_local_smith.py`, raw
`verification_receipts/...`, and `manuscript-revised.pdf`. Their byte-identical
contents are present, but under package-relative names such as
`manuscript/determinant_lines_character_lattices.md`,
`review/STAGE4_LOCAL_SMITH_THEOREM.md`,
`provenance/STAGE4_ARITHMETIC_LITERATURE_AUDIT.md`, and
`verification/checks/verify_local_smith.py`.

**Required repair:** Preserve the historical response if desired, but add an
explicit package-path map adjacent to it, or append package-relative paths to
each listed artifact. The map should state that renaming did not change bytes.
This will make later manifest-bound review navigable without relying on the
outside Stage-4 work directory.

### A4. `DLCL-C1` has inconsistent computational-evidence attribution

**Severity:** Minor.  
**Locations:** `integrity/claims.json` and `provenance/CLAIM_LINEAGE.md`.

`claims.json` attaches only `character-lattice` to `DLCL-C1`, while the lineage
table says “Local-Smith arithmetic checks.” The UFD regular-unit argument is a
manuscript proof and is not computationally checked; the residual quotient and
index are supported by both arithmetic suites at different levels.

**Required repair:** Use one precise mapping in both records. A defensible
choice is to attach both `character-lattice` and `local-smith` while stating
that those computations support the quotient/Smith arithmetic only, not the
UFD unit classification. Alternatively, remove the computational-evidence
claim from C1 and leave arithmetic evidence under T4. Avoid implying that a
finite matrix test proves the regular-unit theorem.

### A5. `STATUS.md` omits the two Stage-4 raw baseline receipts in its wording

**Severity:** Minor wording drift.  
**Location:** `STATUS.md`, four-suite verification bullet.

The bullet says that raw stdout hashes agree with the six Stage-1 receipts.
That is true for the first three suites, but the same bullet presents all four
suites. The last two hashes agree with the Stage-4 local-Smith baselines, as
`provenance/ENVIRONMENT.md` correctly explains.

**Required repair:** Say explicitly that the first six raw hashes match the
Stage-1 baselines and the final two match the Stage-4 baselines, or simply say
that all eight raw hashes match their frozen baseline receipts.

### A6. Replace ambiguous “independent internal” language before assurance freeze

**Severity:** Minor assurance-language repair.  
**Locations:** `review/STAGE4_RESPONSE_TO_REVIEWERS.md` and the copied
adversarial-audit wording.

The documents repeatedly and correctly disclaim independent reproduction and
external peer review. Nonetheless, phrases such as “independent internal
adversarial audit” and “Stage 3' should independently verify” can be detached
from their qualifiers and misread as an assurance upgrade.

**Required repair:** Prefer “separate internal adversarial audit,” “fresh
internal reconstruction,” and “Stage 3' should perform a fresh internal
verification pass.” Keep `independent_reproduction: false` and
`peer_reviewed: false` for every claim. The present Stage-3-prime reports must
remain labelled internal producer-side review artifacts.

## 5. Non-defects and calibrated boundaries

- The absence of a manifest is not a failure at this checkpoint; generating
  one during this review would have violated the requested sequence. It becomes
  a final-gate requirement after the above documentation repairs.
- The unset author, affiliation, contribution, funding, conflict, and licence
  fields are correctly treated as an explicit submission/release blocker, not
  silently filled or waived.
- `research-proof-draft`, null statement digests, and empty formal-evidence
  arrays are internally consistent. No claim is represented as a frozen
  manuscript proof or Lean-kernel theorem.
- The PDF build timestamp makes byte-for-byte PDF rebuilding inappropriate;
  the package correctly uses structural rebuild success and TeX/source parity
  instead.
- The novelty language remains bounded. The package identifies classical
  square, monic, signed-incidence, arithmetic-matroid, and root-partition
  antecedents and does not use “first”, “unique”, or “novel” as an unqualified
  priority claim.
- The internal adversarial computations are useful falsification evidence but
  remain part of the same producer process. They do not change the independent
  reproduction or external peer-review status.

## 6. Acceptance conditions for the package-assurance layer

After A1--A6 are repaired, the package-assurance layer can be marked **PASS**
provided the final integrity stage then:

1. generates the manifest, sidecar, and inventory from the repaired payload;
2. reruns `check_claims.py` with manifest cross-references enabled;
3. verifies all four frozen evidence sets and canonical receipt parity under
   normal and optimized Python;
4. rebuilds the manuscript from a fresh extraction;
5. checks the delivered archive against an out-of-band archive digest; and
6. records the extraction receipt outside the archive without calling that
   producer replay an independent reproduction.

No mathematical major-revision issue was discovered by this package-assurance
review. The decision is **MINOR REVISION** solely because the current
documentation does not yet describe the revised payload with manifest-grade
precision.
