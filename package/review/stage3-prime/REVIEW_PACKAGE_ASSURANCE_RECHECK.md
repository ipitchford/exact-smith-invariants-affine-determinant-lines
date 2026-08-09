# Stage 3-prime package-assurance recheck

**Scope:** findings A1--A6 only  
**Date:** 9 August 2026  
**Decision:** **MINOR REVISION**  
**Manifest freeze:** **DO NOT PROCEED YET**

This is a fresh internal producer-side recheck, not external peer review or
independent reproduction.

| Finding | Status | Live verification |
|---|---|---|
| **A1: stale 20-entry bibliography audit** | **RESOLVED** | `provenance/STAGE4_BIBLIOGRAPHY_CHECK.md` binds the current Markdown, BibTeX, and PDF hashes; records 28 cited/28 defined/no missing/no unused; lists the eight-key Stage-4 delta; and preserves `BIBLIOGRAPHY_AUDIT.md` explicitly as historical. The three bound hashes match the live files. |
| **A2: premature payload-integrity claim** | **RESOLVED** | `ASSURANCE.md` now states that schemas and deterministic interfaces are prepared while the manifest, sidecar, inventory, archive, and external receipt remain pending. No generated manifest is currently present. |
| **A3: unresolved response-letter paths** | **RESOLVED** | `review/STAGE4_PACKAGE_PATH_MAP.md` maps every development name to a package-relative path. All eleven mapped targets exist, and the map states that it is navigation rather than an assurance upgrade. |
| **A4: inconsistent `DLCL-C1` evidence attribution** | **NOT RESOLVED** | `provenance/CLAIM_LINEAGE.md` now says “No direct computational evidence; the quotient arithmetic is registered under `DLCL-T4`,” but `integrity/claims.json` still assigns `DLCL-C1` the `character-lattice` evidence set. These two live records remain contradictory. |
| **A5: six-versus-eight receipt wording** | **RESOLVED** | `STATUS.md` now says that the first six raw stdout hashes match Stage-1 baselines and the final two match Stage-4 local-Smith baselines. |
| **A6: ambiguous internal-independence wording** | **RESOLVED** | The package-facing response now uses “separate internal adversarial reconstruction/audit” and asks Stage 3-prime for a “fresh internal verification.” The historical adversarial report still describes parts of its method as independently reconstructed/implemented, but immediately and explicitly classifies itself as an internal check, not independent specialist reproduction, formal verification, novelty resolution, or peer review. It therefore does not assert the prohibited assurance upgrade. |

`tools/check_claims.py` still passes its schema and protected-assertion scan, but
that validator does not compare `claims.json` with the prose lineage table.
Accordingly, A4 remains a real manifest-bound consistency defect despite the
mechanical PASS.

## Required final repair

Align `DLCL-C1` in the two records before freezing. Given the repaired lineage's
chosen boundary, the cleanest repair is to remove `character-lattice` from
`DLCL-C1.computational_evidence` and leave the quotient/Smith computations
registered under `DLCL-T4`. Alternatively, revise both records to the same
explicitly scoped support statement. Then rerun the claims check and proceed to
manifest generation.

With that single repair verified, this package-assurance recheck would become
**PASS** and the manifest freeze could proceed. At the current live state, the
decision remains **MINOR REVISION**.
