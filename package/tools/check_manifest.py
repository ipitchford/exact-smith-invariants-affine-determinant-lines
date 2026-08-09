#!/usr/bin/env python3
"""Validate a DLCL manifest, sidecars, inventory, and payload hashes."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError, ValidationError
except ImportError as exc:  # pragma: no cover - dependency failure path
    Draft202012Validator = None  # type: ignore[assignment]
    SchemaError = ValidationError = Exception  # type: ignore[misc,assignment]
    JSONSCHEMA_IMPORT_ERROR = exc
else:
    JSONSCHEMA_IMPORT_ERROR = None

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_manifest import (  # noqa: E402
    GENERATED_PATHS,
    PARENT,
    artifact_id,
    canonical_json_bytes,
    media_type_for,
    role_for,
    scan_payload,
    sha256_bytes,
    sha256_file,
)


class ManifestCheckError(RuntimeError):
    """Raised for integrity or semantic validation failures."""


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ManifestCheckError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> tuple[Any, bytes]:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise ManifestCheckError(f"cannot read {path}: {exc}") from exc
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=reject_duplicate_keys)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ManifestCheckError(f"invalid UTF-8 JSON in {path}: {exc}") from exc
    return value, raw


def format_json_path(path: Any) -> str:
    parts = [str(part) for part in path]
    return "$" if not parts else "$." + ".".join(parts)


def validate_schema(instance: Any, schema: Any) -> None:
    if Draft202012Validator is None:
        raise ManifestCheckError(
            "jsonschema is required for schema validation: "
            f"{JSONSCHEMA_IMPORT_ERROR}"
        )
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    errors = sorted(
        validator.iter_errors(instance),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if errors:
        details = "; ".join(
            f"{format_json_path(error.absolute_path)}: {error.message}"
            for error in errors
        )
        raise ManifestCheckError(f"manifest schema validation failed: {details}")


def verify_digest_sidecar(root: Path, manifest_raw: bytes) -> None:
    sidecar = root / "integrity/manifest.sha256"
    try:
        observed = sidecar.read_bytes()
    except OSError as exc:
        raise ManifestCheckError(f"cannot read digest sidecar: {exc}") from exc
    expected_digest = sha256_bytes(manifest_raw)
    expected = f"{expected_digest}  manifest.json\n".encode("ascii")
    if observed != expected:
        raise ManifestCheckError("manifest.sha256 does not match manifest.json")


def verify_inventory(root: Path, artifacts: list[dict[str, Any]]) -> None:
    inventory = root / "integrity/payload_inventory.txt"
    try:
        observed = inventory.read_bytes()
    except OSError as exc:
        raise ManifestCheckError(f"cannot read payload inventory: {exc}") from exc
    expected = "".join(f"{item['path']}\n" for item in artifacts).encode("utf-8")
    if observed != expected:
        raise ManifestCheckError("payload_inventory.txt is not the canonical artifact path list")


def verify_artifacts(root: Path, manifest: dict[str, Any]) -> None:
    artifacts = manifest["artifacts"]
    paths = [item["path"] for item in artifacts]
    identifiers = [item["id"] for item in artifacts]
    if paths != sorted(paths):
        raise ManifestCheckError("artifacts are not sorted by normalized path")
    if len(paths) != len(set(paths)):
        raise ManifestCheckError("manifest contains duplicate artifact paths")
    if len(identifiers) != len(set(identifiers)):
        raise ManifestCheckError("manifest contains duplicate artifact IDs")

    actual = scan_payload(root)
    actual_paths = [item["path"] for item in actual]
    if paths != actual_paths:
        missing = sorted(set(paths) - set(actual_paths))
        unexpected = sorted(set(actual_paths) - set(paths))
        raise ManifestCheckError(
            f"payload inventory mismatch; missing={missing}, unexpected={unexpected}"
        )

    for item in artifacts:
        relative = item["path"]
        if relative in GENERATED_PATHS:
            raise ManifestCheckError(f"generated sidecar listed as payload: {relative}")
        path = root / relative
        expected_id = artifact_id(relative)
        if item["id"] != expected_id:
            raise ManifestCheckError(f"noncanonical artifact ID for {relative}")
        if item["bytes"] != path.stat().st_size:
            raise ManifestCheckError(f"byte-size mismatch for {relative}")
        if item["sha256"] != sha256_file(path):
            raise ManifestCheckError(f"SHA-256 mismatch for {relative}")
        if item["media_type"] != media_type_for(relative):
            raise ManifestCheckError(f"noncanonical media type for {relative}")
        if item["role"] != role_for(relative):
            raise ManifestCheckError(f"noncanonical artifact role for {relative}")


def verify_references(manifest: dict[str, Any]) -> None:
    artifact_ids = {item["id"] for item in manifest["artifacts"]}
    artifact_paths = {item["path"] for item in manifest["artifacts"]}
    if manifest["claim_registry"] not in artifact_paths:
        raise ManifestCheckError("claim registry is not a manifested artifact")

    evidence_ids: set[str] = set()
    for evidence in manifest["evidence_sets"]:
        if evidence["id"] in evidence_ids:
            raise ManifestCheckError(f"duplicate evidence-set ID: {evidence['id']}")
        evidence_ids.add(evidence["id"])
        references = [
            evidence["script_artifact"],
            *evidence["receipt_artifacts"],
            *evidence["external_evidence_artifacts"],
        ]
        missing = [identifier for identifier in references if identifier not in artifact_ids]
        if missing:
            raise ManifestCheckError(
                f"evidence set {evidence['id']} references missing artifacts: {missing}"
            )
        if evidence["independent_reproduction"] and not evidence["external_evidence_artifacts"]:
            raise ManifestCheckError(
                f"evidence set {evidence['id']} claims independence without external evidence"
            )

    formal = manifest["formalisation"]
    formal_refs = [
        formal["lean_toolchain_artifact"],
        formal["build_receipt"],
        formal["axiom_audit_receipt"],
    ]
    missing_formal = [
        identifier
        for identifier in formal_refs
        if identifier is not None and identifier not in artifact_ids
    ]
    if missing_formal:
        raise ManifestCheckError(f"formalisation references missing artifacts: {missing_formal}")
    if formal["status"] == "complete" and any(value is None for value in formal_refs):
        raise ManifestCheckError("complete formalisation lacks toolchain, build, or axiom evidence")


def verify_semantics(manifest: dict[str, Any]) -> None:
    if manifest["parent"] != PARENT:
        raise ManifestCheckError("parent identity differs from the immutable bound candidate")
    package = manifest["package"]
    if package["status"] == "released" and package["version"] == "UNRELEASED":
        raise ManifestCheckError("released status cannot use the UNRELEASED version placeholder")
    required_exclusions = {
        "absolute novelty",
        "independent reproduction",
        "peer review",
        "publication",
    }
    if not required_exclusions.issubset(set(manifest["excluded_assurances"])):
        raise ManifestCheckError("manifest omits a required assurance exclusion")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--schema", type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        root = args.root.resolve(strict=True)
        manifest_path = (
            args.manifest.resolve(strict=True)
            if args.manifest
            else root / "integrity/manifest.json"
        )
        schema_path = (
            args.schema.resolve(strict=True)
            if args.schema
            else root / "integrity/manifest.schema.json"
        )

        manifest, manifest_raw = load_json(manifest_path)
        verify_digest_sidecar(root, manifest_raw)
        schema, _ = load_json(schema_path)
        validate_schema(manifest, schema)
        if manifest_raw != canonical_json_bytes(manifest):
            raise ManifestCheckError("manifest.json is not canonical package JSON")
        verify_inventory(root, manifest["artifacts"])
        verify_artifacts(root, manifest)
        verify_references(manifest)
        verify_semantics(manifest)
        print(
            "PASS manifest "
            f"artifacts={len(manifest['artifacts'])} "
            f"evidence_sets={len(manifest['evidence_sets'])}"
        )
        return 0
    except (ManifestCheckError, OSError, ValueError, SchemaError, ValidationError) as exc:
        print(f"FAIL manifest check: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

