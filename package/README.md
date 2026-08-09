# Exact Smith Invariants and Affine Determinant Lines of Binary-Form Factorisation

**Status:** public unrefereed candidate  
**Version:** `0.1.0-candidate`  
**Authors:** `Anonymous`  
**Licence:** original text and documentation CC0 1.0; original code MIT

This is a provenance-linked public child candidate extending the
immutable *Bordered Jacobian Foundations* candidate. It does not modify,
supersede, correct, or independently validate that parent.

## Mathematical result and contribution boundary

Classical monic and fixed-leading-coefficient calculations identify square
polynomial-multiplication Jacobians with Sylvester resultants, and earlier
projective and monic work gives the pairwise-coprime rank criterion. Building
on that exact prior art, the manuscript proves over the universal integer
coefficient ring that every signed maximal minor of labelled, non-monic
binary-form multiplication is

```text
(product of all pairwise resultants)
    x (the matching Plücker coordinate of the product-one scaling torus),
```

with an explicit orientation. This is an affine Plücker lift of the classical
square multiplication Jacobian, not a claim to have discovered the
Jacobian-resultant phenomenon. It yields the multi-border contraction and the
semi-invariant character-determinant formula.

The strongest candidate contribution is the arithmetic half. For primitive
degrees, a one-generator local presentation computes every prime-adic
valuation of the complete edge-character cokernel. It yields a symmetric
global formula, an `O(k^2)` gcd algorithm, equality between the full
maximal-minor gcd and the spanning-tree gcd, the complete nonprimitive Smith
form, and the connected/étale factors of the residual diagonalizable group
scheme. The generic normalised-factorisation degree is presented separately
as a synthesis of the classical root-partition count and the torus-isogeny
scheme order.

The durable programme-level conclusion is

```text
rank-one degree difference  ->  integer character matrix and Smith invariants.
```

No arbitrary polynomial-normaliser classification, affine-space slice, Keller
map classification, Hessian construction, or Jacobian-conjecture consequence
is proved.

## Package contents

- `manuscript/`: final Markdown and BibTeX sources, generated TeX and PDF,
  and the strict Pandoc/XeLaTeX build interface;
- `verification/`: four byte-frozen exact programs, eight baseline receipts,
  eight canonical regenerated receipts, eight environment receipts, and
  the normal/optimized runner;
- `integrity/`: seven-claim registry and JSON schemas; after the payload is
  frozen, the build creates its manifest, digest sidecar, and inventory;
- `provenance/`: immutable parent identity, Stage-1 hashes and reports,
  focused exact-object antecedent re-audit, literature/bibliography records,
  the current Stage-4 bibliography check, claim lineage, environment record,
  AI-use disclosure, and development records;
- `review/`: the first internal referee round, detailed proof revisions,
  geometry and arithmetic audits, response to reviewers, producer regression
  disposition, Stage-2.5 integrity audit, complete Stage 3-prime re-review, and
  fresh Stage-4.5 citation, originality, and computational audits;
- `formal/`: a detailed Lean blueprint and an explicit `planned` status; and
- `tools/`: claim, manifest, deterministic-archive, and safe
  fresh-extraction validators.

## Quick checks

Use Python 3.13 with the direct versions in `requirements.txt`. The producer
replay used CPython 3.13.5, SymPy 1.14.0, python-flint 0.9.0, and jsonschema
4.26.0.

```bash
make compare
make claims
make verify
make manuscript
make integrity
```

`make verify` runs all four exact suites in normal and `python -O` modes.
The expected combined result is 129,352 positive exact comparisons and all 18
deliberate mathematical mutations detected. `make manuscript` requires
Pandoc, XeLaTeX, and a Traditional Chinese font compatible with the supplied
build settings.

The direct dependency pins are not a wheel-hashed transitive lock. A successful
same-environment replay is therefore not described as verified clean-machine
environment reconstruction.

## Manifest, archive, and fresh extraction

Rebuild the manifest only after intentional payload changes:

```bash
make manifest
make integrity
```

Build a deterministic archive outside the package root and verify a fresh
extraction:

```bash
make archive ARCHIVE=/path/to/determinant-lines-character-lattices.zip
make fresh-extract ARCHIVE=/path/to/determinant-lines-character-lattices.zip EXPECTED_ARCHIVE_SHA256=<digest-from-archive-build> RECEIPT=/path/to/fresh-extraction-receipt.json
```

The expected archive digest is an out-of-band trust anchor; the tool hashes the
exact descriptor-bound bytes before ZIP parsing or extracted-code execution.
The fresh-extraction tool rejects unsafe paths, symlinks, unexpected modes,
timestamps, compression, metadata, and size excesses. It checks
`manifest.sha256` before executing extracted code, validates every manifested
artifact and claim reference, compares canonical receipts, reruns the full
exact suites, and rebuilds the manuscript. Its receipt is intentionally saved
outside the archive to avoid circular self-certification.

## Parent binding

The scientific dependency is fixed to:

- DOI `10.5281/zenodo.21855302`;
- tag `v0.3-candidate`;
- annotated tag object `6f400c15d9203f8ef6eb617a8c64a5dac66cd442`; and
- tagged commit `217f17d9f73e8b5a1bdb8d114bb1003dbed146bc`.

See `provenance/PARENT.md` for the exact boundary.

## Assurance boundary

This is producer-side mathematical work. The proof has received an internal
regression audit and the computations have exact negative controls. A focused
antecedent re-audit found exact classical square/monic Jacobian and rank-locus
predecessors and no exact statement of the simultaneous affine Plücker tensor
or degree-weighted complete-edge Smith result in the expanded bounded corpus.
The recorded Stage-2.5 integrity gate passed with notes after that remediation,
and the fresh Stage-4.5 gate passed after all 28 references, every citation
context, all seven registered claims, and 63.64% of eligible prose were checked.
A subsequent internal adversarial arithmetic audit found no counterexample in
its stated finite search. These findings are not absolute priority or
originality conclusions. Public release, hashes, DOI registration, and
producer replay do not make the package an independent reproduction,
completed Lean formalisation, specialist priority audit, external peer review,
or accepted manuscript.

The responsible human contributor authorised release on 9 August 2026 under
anonymous authorship, with original text and documentation dedicated under
CC0 1.0 and original code licensed under MIT. No affiliation, funding, or
conflict claim is made.
