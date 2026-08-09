PYTHON ?= python3
ARCHIVE ?= ../determinant-lines-character-lattices.zip
RECEIPT ?= ../determinant-lines-character-lattices.fresh-extraction.json
EXPECTED_ARCHIVE_SHA256 ?=

.PHONY: setup verify verify-opt compare claims manuscript manifest-preview manifest integrity archive fresh-extract all

setup:
	$(PYTHON) -m pip install -r requirements.txt

verify:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) verification/run_all.py --root . --mode both

verify-opt:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) verification/run_all.py --root . --mode optimized

compare:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) verification/run_all.py --root . --compare-only

claims:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) tools/check_claims.py --root .

manuscript:
	cd manuscript && bash build.sh

manifest-preview:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) tools/build_manifest.py --root .

manifest:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) tools/build_manifest.py --root . --write

integrity:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) tools/check_manifest.py --root .
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) tools/check_claims.py --root .
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) verification/run_all.py --root . --compare-only

archive: integrity
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) tools/build_archive.py --root . --output "$(ARCHIVE)"

fresh-extract:
	@test -n "$(EXPECTED_ARCHIVE_SHA256)" || { echo "EXPECTED_ARCHIVE_SHA256 is required" >&2; exit 2; }
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) tools/fresh_extract.py --archive "$(ARCHIVE)" --expected-archive-sha256 "$(EXPECTED_ARCHIVE_SHA256)" --receipt "$(RECEIPT)" --full-replay --manuscript-build

all: verify manuscript integrity
