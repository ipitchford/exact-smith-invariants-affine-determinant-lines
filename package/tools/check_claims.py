#!/usr/bin/env python3
"""Validate the DLCL claim registry and its assurance dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError, ValidationError
except ImportError as exc:  # pragma: no cover - dependency failure path
    Draft202012Validator = None  # type: ignore[assignment]
    SchemaError = ValidationError = Exception  # type: ignore[misc,assignment]
    JSONSCHEMA_IMPORT_ERROR = exc
else:
    JSONSCHEMA_IMPORT_ERROR = None


POSITIVE_ASSURANCE_PATTERNS = (
    re.compile(
        r"\b(?:this (?:work|paper|package|result)|the (?:work|paper|package|result)|we)\s+"
        r"(?:is|are|was|were|has been|have been)\s+"
        r"(?:independently (?:verified|reproduced)|formally verified|lean verified|"
        r"peer reviewed|released|published|accepted)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:we (?:prove|establish|show)|this (?:paper|work) "
        r"(?:proves|establishes|shows))\s+(?:the\s+)?(?:first|unique)\b",
        re.IGNORECASE,
    ),
)


class ClaimsCheckError(RuntimeError):
    """Raised for claim-registry or assurance failures."""


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ClaimsCheckError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ClaimsCheckError(f"cannot read {path}: {exc}") from exc
    try:
        return json.loads(raw, object_pairs_hook=reject_duplicate_keys)
    except json.JSONDecodeError as exc:
        raise ClaimsCheckError(f"invalid JSON in {path}: {exc}") from exc


def format_json_path(path: Any) -> str:
    parts = [str(part) for part in path]
    return "$" if not parts else "$." + ".".join(parts)


def validate_schema(instance: Any, schema: Any) -> None:
    if Draft202012Validator is None:
        raise ClaimsCheckError(
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
        raise ClaimsCheckError(f"claims schema validation failed: {details}")


def verify_claim_semantics(registry: dict[str, Any]) -> None:
    claims = registry["claims"]
    identifiers = [claim["id"] for claim in claims]
    if len(identifiers) != len(set(identifiers)):
        duplicates = sorted(
            identifier for identifier in set(identifiers) if identifiers.count(identifier) > 1
        )
        raise ClaimsCheckError(f"duplicate claim IDs: {duplicates}")

    for claim in claims:
        claim_id = claim["id"]
        if claim["independent_reproduction"] and not claim["independent_evidence_artifacts"]:
            raise ClaimsCheckError(
                f"{claim_id}: independence claimed without an external evidence artifact"
            )
        if claim["peer_reviewed"] and not claim["peer_review_artifacts"]:
            raise ClaimsCheckError(f"{claim_id}: peer review claimed without a review artifact")
        if claim["proof_status"] == "lean-kernel-checked":
            if not claim["formal_declaration"]:
                raise ClaimsCheckError(f"{claim_id}: Lean status lacks a declaration")
            if not claim["formal_evidence_artifacts"]:
                raise ClaimsCheckError(f"{claim_id}: Lean status lacks build/axiom evidence")
        if claim["proof_status"] in {"manuscript-proof", "lean-kernel-checked"}:
            if claim["statement_digest"] is None:
                raise ClaimsCheckError(f"{claim_id}: frozen proof status lacks statement digest")
        if claim["novelty_status"] == "specialist-audited" and not claim["novelty_evidence_artifacts"]:
            raise ClaimsCheckError(f"{claim_id}: specialist audit lacks an evidence artifact")
        if claim["kind"] == "search-outcome" and claim["proof_status"] != "not-applicable":
            raise ClaimsCheckError(f"{claim_id}: search outcome must use not-applicable proof status")

    if registry["package_status"] == "released":
        unresolved = [
            claim["id"]
            for claim in claims
            if claim["proof_status"] in {"planned", "research-proof-draft"}
        ]
        if unresolved:
            raise ClaimsCheckError(
                f"released claim registry contains unresolved proof drafts: {unresolved}"
            )


def verify_manifest_cross_references(
    registry: dict[str, Any], manifest: dict[str, Any]
) -> None:
    evidence_ids = {item["id"] for item in manifest["evidence_sets"]}
    artifact_ids = {item["id"] for item in manifest["artifacts"]}
    for claim in registry["claims"]:
        missing_evidence = sorted(set(claim["computational_evidence"]) - evidence_ids)
        if missing_evidence:
            raise ClaimsCheckError(
                f"{claim['id']}: missing computational evidence sets {missing_evidence}"
            )
        artifact_references = (
            claim["formal_evidence_artifacts"]
            + claim["independent_evidence_artifacts"]
            + claim["peer_review_artifacts"]
            + claim["novelty_evidence_artifacts"]
        )
        missing_artifacts = sorted(set(artifact_references) - artifact_ids)
        if missing_artifacts:
            raise ClaimsCheckError(
                f"{claim['id']}: missing evidence artifacts {missing_artifacts}"
            )


def iter_prose_files(root: Path) -> Iterable[Path]:
    fixed = (root / "README.md", root / "STATUS.md", root / "ASSURANCE.md")
    for path in fixed:
        if path.is_file():
            yield path
    for directory in (root / "provenance", root / "manuscript"):
        if not directory.is_dir():
            continue
        for path in sorted(directory.rglob("*"), key=lambda item: item.as_posix()):
            if path.is_file() and path.suffix.lower() in {".md", ".tex"}:
                yield path


def prose_lines(path: Path) -> Iterable[tuple[int, str]]:
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if path.suffix.lower() == ".md" and stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if path.suffix.lower() == ".tex":
            line = line.split("%", 1)[0]
        yield number, line


def scan_protected_assertions(root: Path) -> int:
    findings: list[str] = []
    for path in iter_prose_files(root):
        relative = path.relative_to(root).as_posix()
        for number, line in prose_lines(path):
            for pattern in POSITIVE_ASSURANCE_PATTERNS:
                if pattern.search(line):
                    findings.append(f"{relative}:{number}: {line.strip()}")
    if findings:
        raise ClaimsCheckError(
            "unqualified protected assurance assertion(s): " + " | ".join(findings)
        )
    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--claims", type=Path)
    parser.add_argument("--schema", type=Path)
    parser.add_argument(
        "--manifest",
        type=Path,
        help="manifest for evidence cross-check; auto-detected when present",
    )
    parser.add_argument(
        "--skip-prose-scan",
        action="store_true",
        help="skip conservative protected-assurance phrase scanning",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        root = args.root.resolve(strict=True)
        claims_path = (
            args.claims.resolve(strict=True)
            if args.claims
            else root / "integrity/claims.json"
        )
        schema_path = (
            args.schema.resolve(strict=True)
            if args.schema
            else root / "integrity/claims.schema.json"
        )
        registry = load_json(claims_path)
        schema = load_json(schema_path)
        validate_schema(registry, schema)
        verify_claim_semantics(registry)

        manifest_path = args.manifest
        if manifest_path is None:
            candidate = root / "integrity/manifest.json"
            manifest_path = candidate if candidate.is_file() else None
        if manifest_path is not None:
            manifest = load_json(manifest_path.resolve(strict=True))
            verify_manifest_cross_references(registry, manifest)
            manifest_status = "checked"
        else:
            manifest_status = "skipped"

        protected_count = 0
        if not args.skip_prose_scan:
            protected_count = scan_protected_assertions(root)
        print(
            "PASS claims "
            f"claims={len(registry['claims'])} "
            f"protected_assertions={protected_count} "
            f"manifest_crosscheck={manifest_status}"
        )
        return 0
    except (ClaimsCheckError, OSError, ValueError, SchemaError, ValidationError) as exc:
        print(f"FAIL claims check: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

