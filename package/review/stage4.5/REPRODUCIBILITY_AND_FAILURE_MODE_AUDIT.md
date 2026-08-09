# Stage 4.5 computational reproducibility and package audit

**Audit mode:** fresh, read-only audit of the live Stage-4 package, with all
mutating replay and archive tests performed on a disposable copy  
**Audit time:** 2026-08-09T13:26:32+0100  
**Auditor role:** internal computational/reproducibility auditor, separate
agent turn within the same producer workflow  
**Scope verdict:** **PASS**  
**AI failure modes 1, 3, 5, and 6:** **CLEAR within the stated producer-side
computational scope**  
**Final-delivery closure:** **PENDING BY DESIGN** until the live payload is
frozen and its canonical manifest, archive, and external fresh-extraction
receipt are generated.

This report is not an independent mathematical reproduction, external code
review, clean-machine reconstruction, formal verification, novelty audit, or
peer review. It audits whether the package accurately preserves and reruns the
computations it claims, whether the manuscript's computational account matches
the code, and whether the integrity/archive interfaces behave as specified.

## 1. Snapshot identity and source parity

The refreshed audit snapshot was taken after the concurrent bibliography
locator review had completed. An earlier disposable copy was discarded and no
finding from that superseded copy is used below.

| Object | SHA-256 |
|---|---|
| Development manuscript Markdown | `13924b3f02d112fbdde85179d6ca708512061053bfedbd7cb252c108cf8c0ba3` |
| Package manuscript Markdown | `850f24306d6007d7d7eecbe55d0893a10f922d51062882def898b6ec750e46fa` |
| Package generated TeX | `1f2ef53684010fdced1042908a06f9308a18d30756d164500818f7302e20711d` |
| Package PDF | `0895440ad5517c587bc454a0b9e0a7c5edfa9728bbd16e09adf96511bd929d4b` |
| Development and package bibliography | `e26368824e47b1025359f78c4fa00ebc2967c226fb1967526ab27ee6a2beaff0` |

The two Markdown sources differ in exactly one intentional YAML field:
`references-revised.bib` in the development tree versus `references.bib` in
the self-contained package. Their mathematical and prose contents otherwise
match.

A fresh build in the disposable copy passed the strict two-pass XeLaTeX gate:

- generated TeX was byte-for-byte identical to the packaged TeX;
- extracted PDF text was byte-for-byte identical to the packaged PDF text;
- the rebuilt output had 35 A4 pages; and
- the build emitted no unresolved-citation, unresolved-reference, font, or
  overfull-box failure covered by `manuscript/build.sh`.

The rebuilt PDF itself was not expected to be byte-identical because PDF build
metadata is time-sensitive. The package states this limitation correctly.

## 2. Static validator audit

The following code was inspected directly:

- all four files under `verification/checks/`;
- `verification/run_all.py`;
- `tools/check_claims.py`;
- `tools/build_manifest.py` and `tools/check_manifest.py`;
- `tools/build_archive.py` and `tools/fresh_extract.py`; and
- `manuscript/build.sh` and the package `Makefile`.

### 2.1 Optimized execution cannot erase the proof checks

No verifier or integrity tool contains a Python `assert` statement. The exact
checkers use explicit conditional branches followed by exceptions, including
explicit `raise AssertionError(...)`; those operations survive `python -O`.
The runner itself uses explicit exceptions and nonzero return codes.

### 2.2 Frozen-input and output contracts

`verification/run_all.py`:

1. verifies the SHA-256 of all four checker scripts and all eight raw baseline
   receipts before execution;
2. rejects nonzero exits, timeouts, any stderr, non-UTF-8 output, missing or
   reordered result lines, duplicate or changed result lines, wrong parsed
   totals, and changed negative-control lines;
3. separates canonical mathematical receipts from environment receipts;
4. requires canonical normal and optimized outputs to be byte-identical; and
5. postpones receipt writes until every requested suite has passed.

The runner SHA-256 was
`597e802059b210bff6198e7b90a7a1856ecba584d8e533104a50d418f05a7756`.

### 2.3 Claim, manifest, and archive controls

The claim checker validates the seven-claim registry against its JSON Schema,
rejects duplicate JSON keys, requires evidence artifacts for elevated
independence/peer-review/formalisation statuses, and scans package prose for
unqualified protected assurance assertions.

The manifest builder normalises and sorts paths, rejects symlinks and
non-regular files, assigns deterministic artifact identities, excludes only
the three circular generated integrity files and declared transient paths, and
refuses to write if claim evidence references are unresolved. The manifest
checker independently recomputes the inventory, bytes, hashes, media types,
roles, references, and required assurance exclusions.

The archive builder takes a descriptor-bound, no-follow snapshot; refuses
symlinks, output inside the package, and overwrite; preflights the manifest,
claims, and canonical receipts; and fixes member order, timestamp, mode,
compression, comments, and extra fields. The fresh extractor:

- hashes descriptor-bound archive bytes and compares an externally supplied
  digest before ZIP parsing;
- rejects unsafe, duplicate, case-colliding, encrypted, compressed,
  over-limit, noncanonical, or symlink members;
- verifies the extracted manifest digest before executing extracted code; and
- records manifest, claim, receipt, full-replay, and manuscript-build results
  in an external no-overwrite receipt.

No integrity-bypass defect was found in this bounded source inspection.

## 3. Fresh exact replay

All mutation-producing operations were confined to a disposable package copy.
The live package under review was not changed.

The four frozen suites were rerun under CPython 3.13.5 in ordinary and
optimized mode using SymPy 1.14.0 and python-flint 0.9.0. All subprocesses
exited zero with empty stderr.

| Evidence set | Positive comparisons | Negative controls | Canonical receipt SHA-256 |
|---|---:|---:|---|
| SymPy Pluecker | 143 | 5 | `23c41555057d0ca1bc0f21594b64b0b660c4be7351d63b1653c1187049d5a007` |
| FLINT Pluecker and borders | 136 | 4 | `40c2c0c6e7bcccd005a69df645a7cc14c924f4c901d60ea7a25b20ff05d5c2d3` |
| Character lattice | 84,853 | 4 | `532b638bbb9695b18d29561b8743c0256510e215b3eee0d297fbcdd0a9686e5f` |
| Local/global Smith | 44,220 | 5 | `fa28c357b1f06e6f8319f0a537fecb2e306eb0299e7e50291468321c99164325` |
| **Total** | **129,352** | **18** | -- |

For every evidence set, the ordinary and optimized canonical receipts were
byte-identical. The regenerated raw stdout hashes also matched the frozen
Stage-1 or Stage-4 baseline stdout bytes for both modes.

The negative controls execute genuine mutated computations rather than merely
printing labels. Together they cover omitted/squared resultants, kernel and
orientation errors, a perturbed differential, a wrong tree balance, an
omitted odd-cycle factor two, omitted common content, the false rank-one
equal-degree extrapolation, support-versus-valuation errors, basis-versus-full
saturation, and nonprimitive-content omission.

## 4. Independent ledger reconstruction and out-of-range checks

The published comparison counts were recomputed without importing the runner's
declared totals.

### 4.1 Loop-domain ledgers

Direct combinatorial reconstruction gave:

- tree determinants:
  \(\sum_{k=2}^{5} k^{k-2}3^k=31{,}761\), with the usual one-tree
  convention for \(k=2\);
- general graph minors:
  \(\sum_{k=2}^{5}\binom{\binom{k}{2}}{k-1}3^k+1=52{,}741\);
- Smith/bad-prime cases: \(3^3+3^4+3^5=351\);
- primitive tree-gcd vectors across the stated domains: 1,485; and
- local/global Smith ledger: 3,758 primitive vectors, 7,516 base comparisons,
  and 35,211 admissible prime-pivot comparisons, totalling 42,727.

These independently derived ledgers exactly match the manuscript, README, and
receipts.

### 4.2 New deterministic fixtures

To reduce the risk that the closed formula merely fits the frozen default
range, a separate audit program, not saved into the package and not importing
the verification modules, checked:

- 17 new primitive and nonprimitive degree vectors outside one or more default
  bounds, comparing the full SymPy Smith form against the closed global
  formula and nonprimitive scaling law;
- 50 admissible prime-pivot local-valuation comparisons on those new fixtures;
  and
- all 1,296 spanning trees of \((1,2,3,5,8,13)\), a six-factor tree-gcd case
  beyond the frozen tree-gcd verifier's \(k\le5\) range.

All passed. The six-factor tree-gcd was 2, equal to the closed full-list
index. These are still same-workflow audit calculations, not an independent
reproduction.

## 5. Claims and methodology correspondence

The seven-claim registry validates in ordinary and optimized execution. A
fresh manifest preview contained four computational evidence sets, and all
claim-to-evidence and novelty-artifact references resolved. The protected
assurance scan found zero unqualified assertions.

The entire computational-evidence section of the manuscript was matched to
the code:

- all seven SymPy default degree vectors and their 143-coordinate total;
- all five FLINT Pluecker cases, two direct border cases, and 136-positive
  total;
- character-lattice bounds of five vertices and degree at most three;
- the 31,761, 52,741, 351, 42,727, 1,485, 8, 44,220, 129,352, and 18
  numerical ledgers;
- the stated SymPy/Berkowitz and FLINT/Bareiss backend split; and
- execution in both ordinary and optimized Python.

No numerical or procedural statement in that section lacked a corresponding
code path and fresh run.

## 6. Disposable manifest/archive test

Because the live payload had not yet been finally frozen, canonical integrity
files were not generated during this audit. The complete interface was instead
exercised on the disposable refreshed copy.

The disposable manifest contained 84 payload artifacts and four evidence sets.
Two independent archive builds produced byte-identical 104-entry, 1,253,827
byte ZIPs with SHA-256
`fdfa57d00c2e594292920778dc3010f90d19dab83cffac9ef103e1731344f857`.
This digest is an audit fixture, **not the final package digest**.

Additional controls passed:

- an attempted overwrite of the first archive was rejected;
- a fresh-extraction attempt with an all-zero expected digest was rejected
  before receipt creation;
- the correct digest passed archive and manifest gates;
- manifest, claim, and receipt checks passed after extraction;
- the full ordinary/optimized exact replay passed after extraction; and
- the manuscript rebuilt successfully after extraction.

The disposable external receipt had SHA-256
`c44a4c7fa944eaa682f76f7350e040034e05c2974d7f05e4b2470f1aa139f928`.
It is not a delivery artifact and must not be substituted for the later
receipt bound to the final live archive.

## 7. AI research failure-mode audit

The statuses below use the Stage-4.5 meanings: `CLEAR`, `SUSPECTED`, or
`INSUFFICIENT EVIDENCE`.

### Mode 1: implementation bug passing AI self-review — CLEAR

Every reported computational number has a saved baseline and canonical
receipt, the exact suites were freshly rerun in two Python modes, the two
polynomial implementations use different expression engines and determinant
algorithms, all 18 deliberate mutations were detected, the ledgers were
recomputed independently, and additional out-of-range fixtures passed. Static
inspection found no optimization-disabled assertion path or silent stderr/exit
acceptance.

This clears the failure mode for the reported finite computational evidence.
It does not rule out a theorem-level specification error shared by the proof
and producer-written programs; the package correctly withholds independent
reproduction and formal-verification claims.

### Mode 3: hallucinated experimental result — CLEAR

This is a theoretical paper with exact regression calculations, not an
empirical experiment. Every count and pass claim in Section 9 was regenerated
from executable code and reconciled to saved raw receipts. No percentage,
stochastic run, seed count, benchmark result, or unsourced experimental table
is reported.

### Mode 5: implementation bug reframed as novel insight — CLEAR

The central Smith formula is stated and proved algebraically before its finite
verification evidence is described. The manuscript does not narrate a
surprising computational anomaly as a discovery, and it repeatedly separates
bounded exact checks from proof, novelty, and independence. New fixtures beyond
the frozen ranges gave no sign of a range-specific artifact.

### Mode 6: methodology fabrication — CLEAR

The manuscript's descriptions of software, determinant algorithms, degree
vectors, bounds, comparison counts, negative controls, and ordinary/optimized
execution agree with the inspected code and fresh logs. The producer runtime
also matches the environment record: CPython 3.13.5, SymPy 1.14.0,
python-flint 0.9.0, and jsonschema 4.26.0. Pandoc 3.9 and XeTeX from TeX Live
2026 completed the fresh manuscript build.

## 8. Limitations and final blockers

### Nonblocking, accurately disclosed limitations

- The Python dependencies are direct version pins, not a wheel-hashed
  transitive lock. Clean-machine or cross-platform reconstruction is
  **INSUFFICIENT EVIDENCE**, but the package makes no contrary claim.
- SymPy and FLINT agreement remains producer-side cross-implementation
  evidence, not independent reproduction.
- The finite checks do not prove the general theorems, novelty, or correctness
  of the prose proof.
- PDF bytes are not reproducible because build metadata varies; source-to-TeX
  and extracted-text parity were verified instead.

### Required final-delivery actions

The following objects did not yet exist in the live package at this audit
timestamp and therefore remain **PENDING**, not failed:

1. copy all accepted Stage-3-prime and Stage-4.5 review records into the live
   payload;
2. freeze the payload and generate the canonical manifest, sidecar, and sorted
   inventory;
3. run live manifest, claims, and canonical-receipt integrity checks;
4. build the final deterministic archive twice or otherwise confirm its
   deterministic digest; and
5. perform full fresh extraction from the final archive using an externally
   supplied digest, retaining the external receipt.

No computational or package-interface defect blocks those actions. Stage-4.5
finalisation should not be declared complete until their final hashes and
receipt are recorded outside this pre-freeze audit.

## 9. Final determination

**Computational reproducibility:** PASS for exact same-environment replay.  
**Source/generated parity:** PASS.  
**Claim and method traceability:** PASS.  
**Normal versus optimized execution:** PASS.  
**Negative-control adequacy in the stated mutation classes:** PASS.  
**Manifest/archive/fresh-extraction interface:** PASS on a disposable copy.  
**Clean-machine portability:** INSUFFICIENT EVIDENCE, explicitly excluded.  
**Independent reproduction / formal proof / external review:** NOT
ESTABLISHED, explicitly excluded.  
**Live final package closure:** PENDING the five freeze actions above.

Subject to that mechanical final freeze and fresh-extraction closeout, this
audit finds no computational-reproducibility blocker to preserving the work as
an unreleased producer-side research draft.
