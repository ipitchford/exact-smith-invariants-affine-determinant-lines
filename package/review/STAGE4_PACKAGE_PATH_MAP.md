# Stage 4 response-to-package path map

The response letter was written against the Stage-4 development directory.
The final child package uses stable role-based paths. This map makes every
named revision artifact resolvable inside the package. Renaming does not
change the mathematical content; byte parity was checked before the
package-assurance review, except for the response letter's explicit
assurance-language clarification recorded after that review.

| Response-letter name | Package-relative path |
|---|---|
| `manuscript-revised.md` | `manuscript/determinant_lines_character_lattices.md` |
| `manuscript-revised.pdf` | `manuscript/determinant_lines_character_lattices.pdf` |
| `LOCAL_SMITH_THEOREM.md` | `review/STAGE4_LOCAL_SMITH_THEOREM.md` |
| `LOCAL_SMITH_ADVERSARIAL_AUDIT.md` | `review/STAGE4_LOCAL_SMITH_ADVERSARIAL_AUDIT.md` |
| `ARITHMETIC_LITERATURE_AUDIT.md` | `provenance/STAGE4_ARITHMETIC_LITERATURE_AUDIT.md` |
| `GEOMETRY_INTERFACE_REVISIONS.md` | `review/STAGE4_GEOMETRY_INTERFACE_REVISIONS.md` |
| `REVISION_TRACKING.md` | `review/STAGE4_REVISION_TRACKING.md` |
| `RESPONSE_TO_REVIEWERS.md` | `review/STAGE4_RESPONSE_TO_REVIEWERS.md` |
| `verify_local_smith.py` | `verification/checks/verify_local_smith.py` |
| `verification_receipts/local_smith.normal.txt` | `verification/receipts/baseline/stage4/local_smith_receipt.txt` |
| `verification_receipts/local_smith.optimized.txt` | `verification/receipts/baseline/stage4/local_smith_receipt_optimized.txt` |

The canonical regenerated receipts and environment records are under
`verification/receipts/regenerated/` and `verification/receipts/environment/`,
respectively. This map is a navigation aid, not an assurance upgrade.

The complete internal Stage 3-prime re-review is preserved under
`review/stage3-prime/`. Its `EDITORIAL_DECISION_STAGE3_PRIME.md` permits the
research draft to enter final integrity; it is an internal simulated editorial
decision, not external peer review or journal acceptance. Historical review
text is retained verbatim even where the later Stage 4.5 integrity pass records
a superseding citation correction.

The fresh final-integrity audits and their synthesis are preserved under
`review/stage4.5/`. They cover citations and claim contexts, originality and
frame-lock, computational replay and package assurance, and the pre-freeze
decision. Final archive and extraction hashes remain external delivery data.
