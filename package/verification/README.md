# Exact verification layer

## Status and role

These checks are producer-side exact evidence for the research draft. They are
not an independent reproduction, Lean formalisation, peer review, or novelty
determination.

The first three scripts in `verification/checks/` are byte-for-byte copies of
the Stage-1 programs. The fourth is the frozen Stage-4 local/global Smith
verifier. `verification/run_all.py` refuses to execute if a copied script or
frozen baseline receipt has changed.

## Frozen inputs

| File | SHA-256 |
|---|---|
| `checks/verify_multifactor_sympy.py` | `3806a7c9b4bf38598cc31ef438783984792d7e58f15d5fcf0726b93dd1879ebe` |
| `checks/verify_multifactor_flint.py` | `e7de053c910d800bbdc73dd15ebc7d42bf135e2853c97c84e58754557db98adb` |
| `checks/verify_character_lattice.py` | `b91d2c7b0f11a5470fd1bf41964b579973ae6b15cb3cc18e6e5b4854225bd91a` |
| `checks/verify_local_smith.py` | `09ce5ad767d89dd03c29718da7f6b1c2dbce1b8aac9f9eb4566fdebb22a2906a` |
| SymPy Stage-1 receipt, normal and optimized | `27d4ea5a3e89a95ffd31d426f8d4ae50ad37794652f5cc60bec324c7e09133e2` |
| FLINT Stage-1 receipt, normal and optimized | `f352edfd686e54fc5894839bcba05f9686aa36617a5563a1f73e53d5929588c4` |
| Character-lattice Stage-1 receipt, normal and optimized | `5efd7944b92cb8e9422d3ea33b17545a6e0b386489ce01c9578dc02e8997df51` |
| Local-Smith Stage-4 receipt, normal and optimized | `4d437bf2a6c885cc71f69f365d966ccce055cc05ee505dedc4678618401f40c4` |

The baseline receipts are retained unchanged under
`receipts/baseline/stage1/`.

## Execution

Run all four suites in normal and `python -O` modes with a compatible
Python 3.13 environment:

```bash
python3 verification/run_all.py --root .
```

Or through `make`:

```bash
make verify
make compare
```

`make verify-opt` reruns only optimized mode and requires the existing normal
canonical receipts to match. The direct versions are pinned in
`requirements.txt`, while `provenance/ENVIRONMENT.md` and the environment
receipts identify the producer replay. The package does not claim a
wheel-hashed transitive lock or clean-machine reconstruction.

## Receipt separation

Each subprocess produces two logical records:

1. **Canonical mathematical result.** Exact expected output lines, structured
   comparison counts, negative-control results, and the frozen script hash.
   The `mode` and runtime versions are deliberately absent, so normal and
   optimized receipts must be byte-identical.
2. **Environment record.** Execution mode, interpreter and platform fields,
   raw runtime lines removed from the canonical output, and SHA-256 values for
   raw stdout and stderr. These records are expected to vary across modes or
   machines.

The runner strips only lines beginning with `python=` from canonical output.
Every remaining line must equal the frozen output contract in content and
order, and any stderr is an explicit failure.

## Required totals

| Evidence set | Positive comparisons | Negative controls |
|---|---:|---:|
| SymPy Plücker | 143 | 5 |
| FLINT Plücker plus direct borders | 136 | 4 |
| Character graph and Smith arithmetic | 84,853 | 4 |
| Exact local/global Smith and tree-gcd | 44,220 | 5 |
| **Total** | **129,352** | **18** |

The FLINT positive total comprises 134 Plücker coordinates and two direct
multi-border determinants.

## Failure policy

Execution fails with a nonzero status if:

* a frozen input hash changes;
* a subprocess times out or exits nonzero;
* stderr is nonempty;
* an environment line count differs from the contract;
* any expected result or negative-control line is missing, changed, duplicated,
  or reordered;
* parsed count summaries differ from the expected totals;
* normal and optimized canonical receipts differ; or
* a requested comparison receipt is missing or noncanonical.

The implementation uses explicit exceptions and return codes, not Python
`assert`, so optimized execution cannot disable the checks.
