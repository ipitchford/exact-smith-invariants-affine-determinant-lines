#!/usr/bin/env python3
"""Build a deterministic payload manifest for the DLCL child package.

The default mode writes canonical JSON to stdout.  Files are changed only when
``--write`` is supplied.  The manifest, its digest sidecar, and the inventory
are excluded from the payload they describe to avoid circular hashes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


SCHEMA_VERSION = "1.0"
PACKAGE_SLUG = "determinant-lines-character-lattices"
MATHLIB_COMMIT = "1f0fbd1ad9ff6e4751ab4564fc70cc4f2a1fadf9"
PARENT = {
    "commit": "217f17d9f73e8b5a1bdb8d114bb1003dbed146bc",
    "doi": "10.5281/zenodo.21855302",
    "git_tag": "v0.3-candidate",
    "tag_object": "6f400c15d9203f8ef6eb617a8c64a5dac66cd442",
}

GENERATED_PATHS = {
    "integrity/manifest.json",
    "integrity/manifest.sha256",
    "integrity/payload_inventory.txt",
}
TRANSIENT_PARTS = {
    ".DS_Store",
    ".git",
    ".lake",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "venv",
}

MEDIA_TYPES = {
    ".bib": "application/x-bibtex",
    ".cff": "application/yaml",
    ".csv": "text/csv",
    ".json": "application/json",
    ".lean": "text/plain",
    ".lock": "text/plain",
    ".md": "text/markdown",
    ".pdf": "application/pdf",
    ".py": "text/x-python",
    ".sha256": "text/plain",
    ".sh": "text/x-shellscript",
    ".tex": "application/x-tex",
    ".txt": "text/plain",
    ".yaml": "application/yaml",
    ".yml": "application/yaml",
}

EVIDENCE_CONFIGS = (
    {
        "id": "sympy-plucker",
        "label": "SymPy all-factor Plucker coordinates",
        "script": "verification/checks/verify_multifactor_sympy.py",
        "receipts": (
            "verification/receipts/regenerated/sympy-plucker.normal.json",
            "verification/receipts/regenerated/sympy-plucker.optimized.json",
        ),
        "commands": (
            "python3 verification/checks/verify_multifactor_sympy.py",
            "python3 -O verification/checks/verify_multifactor_sympy.py",
        ),
        "negative_controls": (
            "nc1-missing-resultant",
            "nc2-squared-collision-product",
            "nc3-reversed-torus-row",
            "nc4-wrong-recursive-orientation",
            "nc5-perturbed-differential",
        ),
    },
    {
        "id": "flint-plucker-border",
        "label": "FLINT all-factor Plucker and border determinants",
        "script": "verification/checks/verify_multifactor_flint.py",
        "receipts": (
            "verification/receipts/regenerated/flint-plucker-border.normal.json",
            "verification/receipts/regenerated/flint-plucker-border.optimized.json",
        ),
        "commands": (
            "python3 verification/checks/verify_multifactor_flint.py",
            "python3 -O verification/checks/verify_multifactor_flint.py",
        ),
        "negative_controls": (
            "nc1-missing-resultant",
            "nc2-reversed-torus-row",
            "nc3-wrong-orientation",
            "nc4-perturbed-differential",
        ),
    },
    {
        "id": "character-lattice",
        "label": "Character graph minors, Smith form, and bad primes",
        "script": "verification/checks/verify_character_lattice.py",
        "receipts": (
            "verification/receipts/regenerated/character-lattice.normal.json",
            "verification/receipts/regenerated/character-lattice.optimized.json",
        ),
        "commands": (
            "python3 verification/checks/verify_character_lattice.py",
            "python3 -O verification/checks/verify_character_lattice.py",
        ),
        "negative_controls": (
            "nc1-total-sum-for-bipartite-balance",
            "nc2-odd-cycle-factor-two-omitted",
            "nc3-common-gcd-omitted",
            "nc4-rank-one-collapse-extrapolated",
        ),
    },
    {
        "id": "local-smith",
        "label": "Exact local/global Smith formula and tree-gcd checks",
        "script": "verification/checks/verify_local_smith.py",
        "receipts": (
            "verification/receipts/regenerated/local-smith.normal.json",
            "verification/receipts/regenerated/local-smith.optimized.json",
        ),
        "commands": (
            "python3 verification/checks/verify_local_smith.py",
            "python3 -O verification/checks/verify_local_smith.py",
        ),
        "negative_controls": (
            "nc1-factor-two-omitted",
            "nc2-odd-support-for-valuation",
            "nc3-two-adic-support-for-valuation",
            "nc4-full-list-gcd-replaced-by-edge-basis",
            "nc5-nonprimitive-content-omitted",
        ),
    },
)


class ManifestBuildError(RuntimeError):
    """Raised when the payload cannot be represented deterministically."""


def canonical_json_bytes(value: Any) -> bytes:
    """Return canonical package JSON: sorted compact UTF-8 plus one newline."""
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalized_relative_path(path: Path, root: Path) -> str:
    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise ManifestBuildError(f"path is outside package root: {path}") from exc
    text = PurePosixPath(*relative.parts).as_posix()
    if not text or text.startswith("/") or "\\" in text:
        raise ManifestBuildError(f"noncanonical relative path: {text!r}")
    if any(part in {"", ".", ".."} for part in PurePosixPath(text).parts):
        raise ManifestBuildError(f"unsafe relative path: {text!r}")
    return text


def is_excluded(relative: str) -> bool:
    if relative in GENERATED_PATHS:
        return True
    return any(part in TRANSIENT_PARTS for part in PurePosixPath(relative).parts)


def media_type_for(relative: str) -> str:
    name = PurePosixPath(relative).name
    if name in {"Makefile", "lean-toolchain"}:
        return "text/plain"
    return MEDIA_TYPES.get(PurePosixPath(relative).suffix.lower(), "application/octet-stream")


def role_for(relative: str) -> str:
    if relative == "integrity/claims.json":
        return "claim-registry"
    if relative.startswith("integrity/") and relative.endswith(".schema.json"):
        return "integrity-schema"
    if relative.startswith("provenance/"):
        return "provenance"
    if relative.startswith("manuscript/"):
        return "manuscript"
    if relative.startswith("formal/"):
        if relative.endswith(".lean") or PurePosixPath(relative).name in {
            "lakefile.lean",
            "lake-manifest.json",
            "lean-toolchain",
        }:
            return "formal-proof"
        return "documentation"
    if relative.startswith("verification/receipts/"):
        return "receipt"
    if relative.startswith("verification/fixtures/"):
        return "fixture"
    if relative.startswith("verification/checks/"):
        return "source"
    if relative.startswith("tools/"):
        return "tool"
    if relative in {"README.md", "STATUS.md", "ASSURANCE.md", "CHANGELOG.md"}:
        return "documentation"
    if relative in {
        "CITATION.cff",
        "LICENSE",
        "pyproject.toml",
        "requirements.lock",
        "requirements.txt",
    }:
        return "metadata"
    return "other"


def artifact_id(relative: str) -> str:
    readable = re.sub(r"[^a-z0-9]+", "-", relative.lower()).strip("-")
    suffix = hashlib.sha256(relative.encode("utf-8")).hexdigest()[:12]
    return f"artifact:{readable}:{suffix}"


def scan_payload(root: Path) -> list[dict[str, Any]]:
    if not root.is_dir():
        raise ManifestBuildError(f"package root is not a directory: {root}")

    artifacts: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        relative = normalized_relative_path(path, root)
        if is_excluded(relative):
            continue
        if path.is_symlink():
            raise ManifestBuildError(f"symbolic links are not permitted: {relative}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise ManifestBuildError(f"non-regular payload entry: {relative}")
        identifier = artifact_id(relative)
        if identifier in seen_ids:
            raise ManifestBuildError(f"artifact ID collision: {identifier}")
        seen_ids.add(identifier)
        artifacts.append(
            {
                "bytes": path.stat().st_size,
                "id": identifier,
                "media_type": media_type_for(relative),
                "path": relative,
                "role": role_for(relative),
                "sha256": sha256_file(path),
            }
        )

    artifacts.sort(key=lambda artifact: artifact["path"])
    return artifacts


def discover_evidence_sets(
    root: Path, artifacts: Iterable[dict[str, Any]]
) -> list[dict[str, Any]]:
    artifact_by_path = {artifact["path"]: artifact["id"] for artifact in artifacts}
    result: list[dict[str, Any]] = []
    for config in EVIDENCE_CONFIGS:
        required_paths = (config["script"], *config["receipts"])
        present = [path for path in required_paths if (root / path).is_file()]
        if not present:
            continue
        missing = [path for path in required_paths if path not in artifact_by_path]
        if missing:
            joined = ", ".join(missing)
            raise ManifestBuildError(
                f"incomplete evidence set {config['id']}: missing {joined}"
            )
        result.append(
            {
                "commands": list(config["commands"]),
                "external_evidence_artifacts": [],
                "id": config["id"],
                "independent_reproduction": False,
                "label": config["label"],
                "negative_controls": list(config["negative_controls"]),
                "producer": "project-producer-workflow",
                "receipt_artifacts": [
                    artifact_by_path[path] for path in config["receipts"]
                ],
                "script_artifact": artifact_by_path[config["script"]],
            }
        )
    return sorted(result, key=lambda item: item["id"])


def build_manifest(root: Path, version: str) -> dict[str, Any]:
    artifacts = scan_payload(root)
    by_path = {artifact["path"]: artifact["id"] for artifact in artifacts}
    claim_registry = "integrity/claims.json"
    if claim_registry not in by_path:
        raise ManifestBuildError(f"required claim registry is missing: {claim_registry}")

    toolchain_path = "formal/lean-toolchain"
    toolchain_artifact = by_path.get(toolchain_path)
    formal_status = "partial" if toolchain_artifact else "planned"

    return {
        "artifacts": artifacts,
        "claim_registry": claim_registry,
        "evidence_sets": discover_evidence_sets(root, artifacts),
        "excluded_assurances": [
            "absolute novelty",
            "independent reproduction",
            "peer review",
            "publication",
        ],
        "formalisation": {
            "axiom_audit_receipt": None,
            "build_receipt": None,
            "lean_toolchain_artifact": toolchain_artifact,
            "mathlib_commit": MATHLIB_COMMIT,
            "status": formal_status,
        },
        "package": {
            "authors": ["Anonymous"],
            "license": "CC0-1.0 AND MIT",
            "slug": PACKAGE_SLUG,
            "status": "candidate",
            "version": version,
        },
        "parent": dict(PARENT),
        "schema_version": SCHEMA_VERSION,
    }


def ensure_claim_references_resolved(root: Path, manifest: dict[str, Any]) -> None:
    """Refuse a written manifest while claim evidence is absent from payload."""
    claims_path = root / manifest["claim_registry"]
    try:
        registry = json.loads(claims_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ManifestBuildError(f"cannot load claim registry for write preflight: {exc}") from exc
    if not isinstance(registry, dict) or not isinstance(registry.get("claims"), list):
        raise ManifestBuildError("claim registry has no claims array")

    evidence_ids = {item["id"] for item in manifest["evidence_sets"]}
    artifact_ids = {item["id"] for item in manifest["artifacts"]}
    unresolved: list[str] = []
    for claim in registry["claims"]:
        if not isinstance(claim, dict) or not isinstance(claim.get("id"), str):
            raise ManifestBuildError("claim registry contains an invalid claim record")
        claim_id = claim["id"]
        computational = claim.get("computational_evidence", [])
        if not isinstance(computational, list):
            raise ManifestBuildError(f"{claim_id}: computational_evidence is not an array")
        missing_sets = sorted(set(computational) - evidence_ids)
        if missing_sets:
            unresolved.append(f"{claim_id}:evidence={missing_sets}")

        artifact_fields = (
            "formal_evidence_artifacts",
            "independent_evidence_artifacts",
            "peer_review_artifacts",
            "novelty_evidence_artifacts",
        )
        for field in artifact_fields:
            references = claim.get(field, [])
            if not isinstance(references, list):
                raise ManifestBuildError(f"{claim_id}: {field} is not an array")
            missing_artifacts = sorted(set(references) - artifact_ids)
            if missing_artifacts:
                unresolved.append(f"{claim_id}:{field}={missing_artifacts}")

    if unresolved:
        raise ManifestBuildError(
            "payload is incomplete for claim registry; " + "; ".join(unresolved)
        )


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent, prefix=f".{path.name}.", suffix=".tmp"
    )
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def write_manifest_bundle(root: Path, manifest: dict[str, Any]) -> None:
    manifest_bytes = canonical_json_bytes(manifest)
    manifest_path = root / "integrity/manifest.json"
    digest = sha256_bytes(manifest_bytes)
    digest_bytes = f"{digest}  manifest.json\n".encode("ascii")
    inventory_bytes = (
        "".join(f"{artifact['path']}\n" for artifact in manifest["artifacts"])
    ).encode("utf-8")

    atomic_write(manifest_path, manifest_bytes)
    atomic_write(root / "integrity/manifest.sha256", digest_bytes)
    atomic_write(root / "integrity/payload_inventory.txt", inventory_bytes)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help="package root (default: parent of tools directory)",
    )
    parser.add_argument(
        "--version",
        default="0.1.0-candidate",
        help="package version recorded in the preview or written manifest",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="write manifest.json, manifest.sha256, and payload_inventory.txt",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        root = args.root.resolve(strict=True)
        manifest = build_manifest(root, args.version)
        if args.write:
            ensure_claim_references_resolved(root, manifest)
            write_manifest_bundle(root, manifest)
            print(
                "PASS manifest written "
                f"artifacts={len(manifest['artifacts'])} "
                f"evidence_sets={len(manifest['evidence_sets'])}"
            )
        else:
            sys.stdout.buffer.write(canonical_json_bytes(manifest))
        return 0
    except (ManifestBuildError, OSError, ValueError) as exc:
        print(f"FAIL manifest build: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
