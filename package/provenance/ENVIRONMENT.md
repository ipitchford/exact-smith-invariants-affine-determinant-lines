# Producer replay environment

The regenerated receipts were produced on 9 August 2026 with:

- CPython 3.13.5;
- SymPy 1.14.0;
- python-flint 0.9.0; and
- jsonschema 4.26.0 for integrity-schema validation.

The eight environment receipts bind the executable path, platform fields, raw
stdout hash, and mode for each exact run. The first six raw stdout hashes match
the corresponding frozen Stage-1 receipts; the final two match the frozen
Stage-4 local-Smith baselines.

`requirements.txt` pins the direct Python dependencies by version but does not
contain wheel hashes or a transitive resolver lock. The producer replay is
therefore stronger than an unrecorded local run but weaker than verified
environment reconstruction on a clean machine. Pandoc, XeLaTeX, and the
Traditional Chinese font used for the PDF are recorded by the manuscript
build interface rather than installed by the Python requirements file.
