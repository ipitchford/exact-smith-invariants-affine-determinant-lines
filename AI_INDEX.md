# AI index — exact-smith-invariants-affine-determinant-lines

## Identity and version

Documentation addendum: 2026-09-24. Indexes [source commit 4b1e2dcb3c05](https://github.com/ipitchford/exact-smith-invariants-affine-determinant-lines/tree/4b1e2dcb3c0565c650767625a953c843603806c4) and candidate tag `v0.1.0-candidate`. This index was added after that release: it is **not** part of the original tag, DOI archive or frozen manifest. Existing release files and checksums remain unchanged. For historical manifest/allow-list checks, use a clean checkout of that tag, not this documentation-enriched branch. The addendum is authenticated by Git history.

[Release identity and DOI](README.md) · [Evidence Press context](https://evidencepress.org/releases/exact-smith-invariants-affine-determinant-lines/)

## Exact scope

Candidate factorisation of maximal coefficient-differential minors for labelled binary-form multiplication, and exact Smith invariants of the complete pairwise-resultant character lattice. Includes local valuations, a global formula, an O(k²) gcd algorithm and a spanning-tree gcd theorem.

The linked manuscript and claim register control all hypotheses and quantifiers; this index is a navigation aid, not a substitute proof.

## Claim and evidence map

- [package/manuscript/determinant_lines_character_lattices.md](package/manuscript/determinant_lines_character_lattices.md) — Precise statement and proof.
- [package/integrity/claims.json](package/integrity/claims.json) — Claim map.
- [ASSURANCE.md](ASSURANCE.md) — Assurance.
- [package/provenance/PARENT.md](package/provenance/PARENT.md) — Immutable parent binding.
- [package/requirements.txt](package/requirements.txt) — Dependencies.
- [PROVENANCE.md](PROVENANCE.md) — Provenance.
- [LICENSES.md](LICENSES.md) — Rights.

## Reproduce

From the indexed release root, after inspecting the commands and installing the documented environment:

```sh
python3 -m pip install -r package/requirements.txt
make -C package compare
make -C package claims
make -C package verify
make -C package integrity
```

Producer environment: Python 3.13.5, SymPy 1.14.0, python-flint 0.9.0, jsonschema 4.26.0. Recorded expectation: 129,352 positive exact comparisons and all 18 negative controls detected in normal and optimized modes.

## Trust boundary and safe reuse

A separately versioned extension, not a correction or independent reproduction of Bordered Jacobian Foundations. No arbitrary normaliser/affine-slice classification or Keller/Hessian/Jacobian-conjecture consequence is claimed.

No new mathematical validation, formalisation, independent reproduction or novelty audit was performed for this documentation repair. Preserve the anonymous attribution and existing citation metadata. Distinguish producer checks, finite formal results, universal written arguments and external review. Before downstream reuse, match the exact statement and dependency scope and check subsequent corrections; a DOI or successful command alone is not proof of correctness.

## Licence and provenance

Use the rights/provenance sources linked above and [README](README.md); cited and third-party material retains its own terms. This new index is dedicated under CC0-1.0, without changing any existing licence or attribution.

