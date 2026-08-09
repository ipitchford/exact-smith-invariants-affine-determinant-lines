# Producer proof-regression audit

**Audit date:** 9 August 2026  
**Status:** completed inside the producer workflow  
**Independence:** not independent reproduction or peer review

## Scope

A separate agent in the same research workflow checked the integrated
manuscript against the detailed replacements in `PROOF_REVISIONS.md`. The
audit covered the ring-level composition sign, the all-factor induction, the
multi-border Laplace sign, graph-minor dimensions, Smith determinantal
divisors, the bad-prime criterion, the two-factor Appendix E proof, and the
generic-degree argument.

## Defects found and repaired

1. Section 8 initially said that the zero locus of a torus semi-invariant
   descended to the raw product of projective factor spaces. Semi-invariance
   alone does not give that descent. The proof now constructs
   `Z^sf = V_D^sf x_{P(V_D)} product_i P(V_{d_i})`, identifies
   `U^sf -> Z^sf` as a `T`-torsor, descends the stable principal ideal fpqc,
   and uses irreducibility plus finiteness to remove a proper closed image.
2. Section 4 initially claimed multiplicity one after any base change on which
   the chosen resultant remained reduced prime. The text now also requires
   the other resultants and some maximal torus-kernel minor to remain nonzero
   at the generic collision component.
3. The formalisation outline referred to the parent theorem as its rank-one
   kernel even after Appendix E became self-contained. It now points to
   Lemma E.1.
4. Exact Stacks Project locators were added for free finite-group quotients,
   finite-locally-free degree, etaleness, torsor groupoids, and fpqc descent
   (tags 07S7, 02VO, 02VN, 04TW, and 023T). An initially cited tag 0727 was
   later removed during the citation-integrity audit because it concerns an
   eigensheaf lemma rather than finite etaleness.

## Disposition

After repair, the auditor found no remaining transcription, dimension,
orientation-sign, induction, multi-border, graph-minor, Smith-form,
bad-prime, or generic-degree defect in the audited scope. This clears the
producer draft for package freezing on those grounds. It is not an external
specialist proof review, an independent reproduction, or journal peer review.
