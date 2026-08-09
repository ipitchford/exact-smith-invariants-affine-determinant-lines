# Stage 4 bibliography and citation-key check

**Date:** 9 August 2026  
**Scope:** revised research-draft manuscript only  
**Assurance:** producer-side mechanical and provenance check; not a specialist
priority review or independent source reproduction

## Bound inputs

| File | SHA-256 at this check |
|---|---|
| `manuscript/determinant_lines_character_lattices.md` | `850f24306d6007d7d7eecbe55d0893a10f922d51062882def898b6ec750e46fa` |
| `manuscript/references.bib` | `e26368824e47b1025359f78c4fa00ebc2967c226fb1967526ab27ee6a2beaff0` |
| `manuscript/determinant_lines_character_lattices.pdf` | `0895440ad5517c587bc454a0b9e0a7c5edfa9728bbd16e09adf96511bd929d4b` |

The PDF digest is build-instance-specific because the generated PDF embeds a
creation timestamp. The Markdown and BibTeX digests identify the checked
scholarly content.

## Mechanical results

- 28 distinct citation keys occur in the Markdown source.
- 28 distinct entries are defined in the BibTeX database.
- Every cited key is defined; no bibliography entry is unused.
- The database contains 24 DOI fields and all 24 DOI values are distinct after
  case normalisation.
- Biber 2.21 completed `--tool --validate-datamodel` with exit status zero.
- The package-local Pandoc/citeproc and two-pass XeLaTeX build completed with
  no undefined citation, unresolved reference, overfull-box, or font warning.
- The resulting PDF has 35 pages and embeds all listed fonts.

## Source-support records

Mechanical reconciliation is not a content audit. The supporting records are:

1. `BIBLIOGRAPHY_AUDIT.md`, which records the earlier 20-entry identity and
   metadata check;
2. `STAGE1_ANTECEDENT_REAUDIT.md`, which records the focused exact-object return
   prompted by the first integrity gate; and
3. `STAGE4_ARITHMETIC_LITERATURE_AUDIT.md`, which checks the eight-source
   arithmetic-matroid, signed-graph, toric, and adjacent Smith expansion and
   records the Zaslavsky erratum boundary; and
4. `review/stage4.5/CITATION_AND_CLAIM_AUDIT.md`, which freshly verifies all
   28 identities, all 67 citation clusters and all 96 cited-key occurrences.

Together these records support the current bounded contribution framing. They
do not establish exhaustive novelty, priority, external peer review, or
independent reproduction. Author and licence placeholders remain deliberate
release blockers rather than bibliography defects.

## Stage-4 bibliography delta

The 20-entry audit is retained unchanged as the Stage-1/Stage-2 historical
record. The revised bibliography adds exactly these eight keys:

| Added key | Role in the revised paper |
|---|---|
| `Zaslavsky1982` | all-negative signed-graph rank, support, and determinant structure |
| `Zaslavsky1983Erratum` | correction boundary for the 1982 signed-graph paper |
| `Moci2012` | representable arithmetic multiplicity and toric component count |
| `DAdderioMoci2013` | arithmetic-matroid GCD rule and toric-arrangement setting |
| `FinkMoci2016` | matroids over rings and DVR-sensitive quotient modules |
| `ArdilaCastilloHenley2015` | adjacent equal-weight signed-root-list arithmetic |
| `Lorenzini2008` | Smith/Laplacian comparison and critical-group boundary |
| `HanusaZaslavsky2011` | closest complete-incidence minor-lcm comparison |

Their primary-source locators and exact collision/non-collision adjudications
are recorded in `STAGE4_ARITHMETIC_LITERATURE_AUDIT.md`.

During Stage 4.5, a version-sensitive Mahatab--Sampath equation locator was
replaced in all three current contexts by the stable `Theorem A.3` locator.
The source and PDF digests above bind the repaired, reverified text.
