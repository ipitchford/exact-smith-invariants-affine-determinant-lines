# Reproducible child-package plan

## Resultant-Character Lattices of Binary-Form Factorisations

**Plan status:** architecture only; no repository, release, tag, deposit, or
deployment is authorised by this document  
**Prepared:** 9 August 2026  
**Package slug:** `determinant-lines-character-lattices`

The package is a new, provenance-linked child of *Bordered Jacobian
Foundations*. It must not revise the historical parent candidate. The package
combines a manuscript, exact producer-side checks, a Lean formalisation track,
and machine-readable claim/evidence records while keeping each assurance layer
distinct.

## 1. Bound parent and current evidence

### 1.1 Parent pointer

The child package should bind to the immutable public parent object, not to the
moving `main` branch:

| Field | Bound value |
|---|---|
| Parent title | *Bordered Jacobian Foundations* |
| Public DOI | `10.5281/zenodo.21855302` |
| Git tag | `v0.3-candidate` |
| Annotated tag object | `6f400c15d9203f8ef6eb617a8c64a5dac66cd442` |
| Tagged commit | `217f17d9f73e8b5a1bdb8d114bb1003dbed146bc` |
| Permitted use | Read-only theorem, convention, provenance, and literature context |

The local parent `main` commit observed during planning was
`8196203063f54d468e1d2a18922fde7185294d04`, but it is not the identity of the
historical candidate and should not appear as the scientific dependency.

### 1.2 Frozen Stage-1 inputs

The package-construction process should ingest copies of the following files
and verify their hashes before any adaptation:

| Input | SHA-256 |
|---|---|
| `stage1_research_report.md` | `ab33b402df71c24d48932b46631415a57b3b6c208a0cc24a7701cf55d8869ed1` |
| `explore_multifactor.py` | `3806a7c9b4bf38598cc31ef438783984792d7e58f15d5fcf0726b93dd1879ebe` |
| `verify_multifactor_flint.py` | `e7de053c910d800bbdc73dd15ebc7d42bf135e2853c97c84e58754557db98adb` |
| `verify_character_lattice.py` | `b91d2c7b0f11a5470fd1bf41964b579973ae6b15cb3cc18e6e5b4854225bd91a` |
| SymPy normal and `-O` receipt, each | `27d4ea5a3e89a95ffd31d426f8d4ae50ad37794652f5cc60bec324c7e09133e2` |
| FLINT normal and `-O` receipt, each | `f352edfd686e54fc5894839bcba05f9686aa36617a5563a1f73e53d5929588c4` |
| Character-lattice normal and `-O` receipt, each | `5efd7944b92cb8e9422d3ea33b17545a6e0b386489ce01c9578dc02e8997df51` |

These hashes describe the files inspected on 9 August 2026. They do not attest
to theorem truth or independence.

## 2. Proposed repository layout

```text
determinant-lines-character-lattices/
├── README.md
├── STATUS.md
├── ASSURANCE.md
├── CHANGELOG.md
├── LICENSE
├── CITATION.cff
├── Makefile
├── pyproject.toml
├── requirements.lock
├── manuscript/
│   ├── determinant_lines_character_lattices.tex
│   ├── determinant_lines_character_lattices.md
│   ├── references.bib
│   ├── figures/
│   └── appendices/
│       ├── conventions.tex
│       ├── verification.tex
│       ├── formalisation.tex
│       └── novelty_matrix.tex
├── formal/
│   ├── lakefile.lean
│   ├── lean-toolchain
│   ├── lake-manifest.json
│   └── DeterminantLines/
│       └── ...
├── verification/
│   ├── README.md
│   ├── run_all.py
│   ├── checks/
│   │   ├── verify_multifactor_sympy.py
│   │   ├── verify_multifactor_flint.py
│   │   └── verify_character_lattice.py
│   ├── fixtures/
│   │   ├── degree_cases.json
│   │   └── mutations.json
│   ├── receipts/
│   │   ├── baseline/
│   │   └── regenerated/
│   └── environment/
├── provenance/
│   ├── PARENT.md
│   ├── STAGE1_INPUTS.json
│   ├── CLAIM_LINEAGE.md
│   └── AI_USE.md
├── integrity/
│   ├── manifest.schema.json
│   ├── manifest.json
│   ├── manifest.sha256
│   ├── payload_inventory.txt
│   └── claims.json
├── tools/
│   ├── build_manifest.py
│   ├── check_manifest.py
│   ├── check_claims.py
│   └── fresh_extract.sh
└── tests/
    ├── test_manifest.py
    ├── test_receipt_schema.py
    └── test_negative_controls.py
```

The `LICENSE` and authorship fields are placeholders until the user supplies
or confirms them. Copied parent material must not silently impose or inherit a
licence that has not been checked.

## 3. Artifact roles

### 3.1 Manuscript

The manuscript contains the mathematical argument and bounded literature
claims. It cites receipts only as computational support. Its theorem numbering
must map one-to-one to stable claim IDs in `integrity/claims.json`.

Recommended IDs:

| Claim ID | Manuscript unit | Initial status |
|---|---|---|
| `DLCL-T1` | All-factor signed Plücker identity | proved in manuscript; producer checked |
| `DLCL-T2` | Multi-border contraction | proved in manuscript; producer checked |
| `DLCL-T3` | Weighted graph-minor theorem | proved in manuscript; producer checked |
| `DLCL-T4` | Full character-lattice Smith form | proved in manuscript; producer checked |
| `DLCL-C1` | Bad-prime support criterion | proved in manuscript; producer checked |
| `DLCL-C2` | Generic scheme-degree formula | proved subject to stated generic hypotheses |
| `DLCL-N1` | Exact statements not found in bounded search | bounded-search outcome only |

No claim may have status `formally_verified` until the Lean completion gates in
`FORMALIZATION_BLUEPRINT.md` pass.

### 3.2 Verification suites

Retain three conceptually separate implementations:

1. SymPy/Berkowitz construction of every Plücker coordinate;
2. separately written `python-flint`/Bareiss construction plus direct border
   determinants;
3. integer-matrix graph-minor, Smith, and modular-prime checks.

The word “independent” should describe implementation separation only when
qualified. All three originated in the same producer process and are not an
independent reproduction.

### 3.3 Formal sources

Lean sources certify encoded statements. They do not import generated facts
from Python receipts. Small fixtures may compare outputs, but main proofs must
not depend on those fixtures.

### 3.4 Provenance

`PARENT.md` records the parent DOI, tag object, tagged commit, theorem used, and
assurance boundary. `STAGE1_INPUTS.json` records input paths as logical names,
hashes, and acquisition date; it must not preserve private absolute paths.

## 4. Verification manifest

### 4.1 Canonicalisation

`integrity/manifest.json` should be UTF-8 JSON with:

* lexicographically sorted object keys;
* arrays sorted by stable `id` or normalized path where order has no semantic
  meaning;
* `/` path separators;
* no absolute paths;
* no timestamps, hostnames, usernames, process IDs, or transient runtime
  versions;
* one final newline.

Serialize with an explicit canonical routine such as
`json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)`
plus a newline. Runtime and dependency versions belong in a separate
environment receipt and are referenced by hash.

The manifest lists every payload file except:

* `integrity/manifest.json` itself;
* `integrity/manifest.sha256`, which contains the manifest digest;
* ephemeral build directories explicitly excluded by schema.

`payload_inventory.txt` is a sorted newline-delimited list of the same artifact
paths. A fresh-extraction check fails on missing, modified, or unexpected
payload files.

### 4.2 Minimum schema

```json
{
  "schema_version": "1.0",
  "package": {
    "slug": "determinant-lines-character-lattices",
    "version": "UNRELEASED",
    "status": "research-draft"
  },
  "parent": {
    "doi": "10.5281/zenodo.21855302",
    "git_tag": "v0.3-candidate",
    "tag_object": "6f400c15d9203f8ef6eb617a8c64a5dac66cd442",
    "commit": "217f17d9f73e8b5a1bdb8d114bb1003dbed146bc"
  },
  "artifacts": [
    {
      "id": "...",
      "path": "...",
      "media_type": "...",
      "bytes": 0,
      "sha256": "...",
      "role": "source|receipt|manuscript|formal-proof|provenance"
    }
  ],
  "evidence_sets": [
    {
      "id": "sympy-plucker",
      "producer": "project-authors",
      "independent_reproduction": false,
      "script_artifact": "...",
      "receipt_artifacts": ["..."],
      "commands": ["..."],
      "negative_controls": ["NC1", "NC2"]
    }
  ],
  "formalisation": {
    "status": "planned|partial|complete",
    "lean_toolchain_artifact": "...",
    "mathlib_commit": "1f0fbd1ad9ff6e4751ab4564fc70cc4f2a1fadf9",
    "build_receipt": null,
    "axiom_audit_receipt": null
  },
  "claim_registry": "integrity/claims.json",
  "excluded_assurances": [
    "independent reproduction",
    "peer review",
    "absolute novelty",
    "publication"
  ]
}
```

The production schema should require 64 lowercase hexadecimal characters for
every SHA-256 and reject unknown top-level keys.

### 4.3 Claim registry

Each `claims.json` record should contain:

```json
{
  "id": "DLCL-T1",
  "statement_digest": "sha256-of-normalized-statement",
  "manuscript_location": "theorem:all-factor",
  "proof_status": "manuscript-proof",
  "formal_declaration": null,
  "computational_evidence": ["sympy-plucker", "flint-plucker"],
  "independent_reproduction": false,
  "peer_reviewed": false,
  "novelty_status": "not-found-in-bounded-search",
  "scope_notes": ["universal integer coefficient ring"]
}
```

Status transitions are monotone only when supported by a new artifact. For
example, changing `proof_status` to `lean-kernel-checked` requires the formal
declaration, clean-build receipt, axiom audit, and their hashes.

## 5. Receipt design

### 5.1 Frozen versus regenerated receipts

Keep the present Stage-1 text receipts under
`verification/receipts/baseline/stage1/` without editing. Their embedded
Python/library versions are historical evidence.

For the child package, emit two outputs per run:

1. a canonical result receipt containing cases, counts, orientations, result
   status, and negative-control outcomes, but no runtime-varying fields;
2. an environment receipt containing Python version, dependency versions,
   operating system, architecture, command, and optional timestamp.

This permits byte equality between normal and `python -O` result receipts
without pretending that different runtime environments are byte-identical.

### 5.2 Required result fields

Every canonical receipt should include:

* receipt schema version;
* evidence-set ID;
* script SHA-256;
* normalized input case list;
* comparison count;
* per-case orientation or determinant summary;
* explicit negative-control IDs and `detected: true`;
* final `pass: true|false`;
* no field whose value is supplied only by `assert`.

Scripts must raise explicit exceptions or return a nonzero exit status when a
positive comparison fails or a mutation survives. The `python -O` run is a
required guard against assertion-only verification.

## 6. Reproduction interface

The package should expose the following stable commands:

```text
make setup          # create the pinned environment; network may be needed
make verify         # all exact suites in normal mode
make verify-opt     # all exact suites under python -O
make compare        # canonical normal/-O receipt byte comparison
make formal         # lake build plus axiom audit
make manuscript     # compile LaTeX and generate Markdown/PDF
make integrity      # inventory, schema, claim and hash checks
make fresh-extract  # archive, extract to a temporary directory, run core gates
make all            # verify, compare, formal, manuscript, integrity
```

The exact commands behind these targets belong in the manifest. Dependency
bootstrap is the only step permitted to require network access; verification
and builds should run offline once the pinned caches exist.

### 6.1 Dependency pins

The starting Python environment is:

* Python 3.13 series;
* SymPy `1.14.0`;
* python-flint `0.9.0`.

Use a lock file with hashes and record the exact interpreter in the environment
receipt. The Lean project pins Mathlib commit
`1f0fbd1ad9ff6e4751ab4564fc70cc4f2a1fadf9` and resolves Lean through that
revision's toolchain file.

The locally observed `Lean 4.32.1` is diagnostic context only, not a package
pin unless the audited Mathlib revision resolves to it.

## 7. Negative-control matrix

All existing mutations should survive package migration:

| Evidence set | Required mutations |
|---|---|
| SymPy Plücker | missing resultant; collision product squared; first torus row reversed; recursive orientation reversed; differential perturbed |
| FLINT Plücker/border | missing resultant; torus row reversed; orientation reversed; differential perturbed |
| Character lattice | total degree substituted for bipartite balance; odd-cycle factor 2 omitted; common gcd omitted from Smith form; rank-one equal-degree collapse falsely extrapolated to `k=3` |

Add package-level controls:

* alter one manifest byte and require hash failure;
* remove an artifact and require inventory failure;
* add an unlisted file and require inventory failure;
* set `independent_reproduction: true` without an external evidence artifact and
  require claim-schema failure;
* insert `sorry` into a fixture copy and require the formal source audit to
  fail.

Negative controls should execute against disposable fixture copies, never by
mutating the canonical payload.

## 8. Build and integrity sequence

### Gate P0 — Scaffold

* create a new repository or standalone directory;
* add `PARENT.md` bound to the tagged commit;
* copy Stage-1 inputs after hash verification;
* choose licence, author placeholders, and citation metadata;
* make no change to the parent repository.

### Gate P1 — Manuscript proof package

* complete LaTeX and Markdown sources;
* map every theorem to a claim ID;
* compile without undefined references or citations;
* include English and Traditional Chinese abstracts;
* include data/code, ethics, contribution, conflict, funding, and AI-use
  declarations;
* run an adversarial convention/sign review.

### Gate P2 — Exact verification package

* migrate the three suites without changing their mathematical fixtures;
* generate canonical and environment receipts;
* run normal and `python -O` modes;
* require byte-identical canonical receipts;
* require all 13 mathematical negative controls to be detected;
* reconcile reported counts with receipt contents rather than hard-coded prose.

### Gate P3 — Formalisation

Follow `FORMALIZATION_BLUEPRINT.md`. A partial Lean tree is welcome, but the
package status remains `formalisation: partial` until all core completion gates
pass.

### Gate P4 — Fresh-extraction integrity

1. build the intended archive;
2. create a new temporary extraction directory;
3. verify `manifest.sha256` before executing payload code;
4. validate manifest and claims against their schemas;
5. verify every artifact hash and exact inventory;
6. create environments from locks;
7. rerun exact checks in normal and optimized modes;
8. rebuild Lean and the manuscript;
9. compare canonical receipts and expected output hashes;
10. save the fresh-extraction receipt outside the archive and then add it only
    in a subsequent, newly manifested package version.

This avoids a circular manifest in which a receipt purports to certify the
archive that already contains it.

### Gate P5 — External scientific gates

Before stronger public language, obtain separately attributable artifacts for:

* independent mathematical reproduction;
* specialist priority/antecedent audit;
* proof or code review by a person outside the producer process;
* journal or community peer review if later pursued.

These artifacts must identify reviewer/reproducer scope and the exact payload
hash examined. Agreement by another model in the same workflow is not an
independent reproduction.

### Gate P6 — Optional release

Publication, Git tags, DOI deposition, Evidence Press deployment, and public
readback require explicit user authority in a later step. A successful P0–P5
run does not grant release authority.

## 9. Assurance-state vocabulary

Use only the strongest phrase supported by the corresponding gate:

| Phrase | Minimum evidence |
|---|---|
| `research draft` | manuscript or notes exist |
| `producer checked` | pinned exact suites and negative controls pass |
| `reproducible package` | P4 passes from a fresh extraction |
| `Lean kernel checked` | formal core compiles, source/axiom audit passes |
| `independently reproduced` | external reproducer examines the bound payload and supplies an attributable report |
| `specialist priority audited` | documented object/formula identity search by a relevant specialist |
| `peer reviewed` | identifiable review process has occurred; distinguish informal review from journal review |
| `released` | immutable public object, production deployment where applicable, and public readback all verified |

These properties are independent. For example, a Lean-checked theorem can
remain novelly unassessed and scientifically unreproduced.

## 10. Claim and scope checks

`tools/check_claims.py` should fail if any manuscript or metadata file uses an
unqualified protected phrase inconsistent with `claims.json`. Initial protected
phrases include:

* `independently verified` or `independently reproduced`;
* `formally verified` or `Lean verified`;
* `peer reviewed`;
* `novel`, `first`, or `unique` without the bounded-search qualifier;
* `released`, `published`, or `accepted`;
* `Keller map classification`, `Hessian result`, or `Jacobian conjecture
  consequence`.

The scanner is a guardrail, not semantic proof. Human review remains required
for context and negation.

## 11. Recommended immediate implementation order

1. scaffold the child directory and provenance pointer;
2. freeze the Stage-1 scripts and receipts by hash;
3. write the manuscript theorem statements and convention appendix;
4. create canonical receipt schemas and a single `run_all.py` orchestrator;
5. implement P2 and P4 integrity gates;
6. bootstrap Lean F0–F1;
7. formalise the two-factor base and all-factor induction (F2–F3);
8. formalise multi-bordering (F4);
9. add graph/Smith formalisation (F5–F6);
10. request external reproduction and priority review against the frozen
    payload;
11. consider a release only after the user reviews the resulting assurance
    record.

The highest-value scientific stopping point is a fresh-extraction package with
the full manuscript, the all-factor and multi-border Lean core, exact
producer-side checks, and an honest external-review gap. Graph/Smith
formalisation would elevate it to the programme-defining endpoint; affine-slice
or Keller claims should not be added merely to make the package appear broader.
