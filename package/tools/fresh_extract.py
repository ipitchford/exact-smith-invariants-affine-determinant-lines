#!/usr/bin/env python3
"""Safely extract and verify a deterministic DLCL package archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any


PACKAGE_SLUG = "determinant-lines-character-lattices"
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
FILE_MODE = stat.S_IFREG | 0o644
DIRECTORY_MODE = stat.S_IFDIR | 0o755
REQUIRED_ARCHIVE_PATHS = {
    f"{PACKAGE_SLUG}/integrity/manifest.json",
    f"{PACKAGE_SLUG}/integrity/manifest.sha256",
    f"{PACKAGE_SLUG}/integrity/payload_inventory.txt",
}


class FreshExtractError(RuntimeError):
    """Raised when archive safety, integrity, or replay checks fail."""


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        + "\n"
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized_sha256(value: str) -> str:
    if re.fullmatch(r"[0-9a-fA-F]{64}", value) is None:
        raise FreshExtractError("expected archive SHA-256 must be exactly 64 hex digits")
    return value.lower()


def snapshot_archive(
    source_path: Path, destination: Path, max_archive_bytes: int
) -> dict[str, Any]:
    nofollow = getattr(os, "O_NOFOLLOW", None)
    if nofollow is None:
        raise FreshExtractError("no-follow archive reads are unavailable on this platform")
    flags = os.O_RDONLY | nofollow | getattr(os, "O_CLOEXEC", 0)
    source_descriptor: int | None = None
    try:
        source_descriptor = os.open(source_path, flags)
        before = os.fstat(source_descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise FreshExtractError(f"archive is not a regular file: {source_path}")
        if before.st_size > max_archive_bytes:
            raise FreshExtractError("archive exceeds compressed-size limit")
        digest = hashlib.sha256()
        total = 0
        with destination.open("xb") as target:
            while True:
                block = os.read(source_descriptor, 1024 * 1024)
                if not block:
                    break
                total += len(block)
                if total > max_archive_bytes:
                    raise FreshExtractError("archive exceeds compressed-size limit")
                digest.update(block)
                written = target.write(block)
                if written != len(block):
                    raise FreshExtractError("short write while snapshotting archive")
            target.flush()
            os.fsync(target.fileno())
        after = os.fstat(source_descriptor)
        before_identity = (
            before.st_dev,
            before.st_ino,
            before.st_size,
            before.st_mtime_ns,
            before.st_ctime_ns,
        )
        after_identity = (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mtime_ns,
            after.st_ctime_ns,
        )
        if before_identity != after_identity or total != after.st_size:
            raise FreshExtractError("archive changed while being snapshotted")
        os.chmod(destination, 0o600)
        return {"bytes": total, "sha256": digest.hexdigest()}
    except OSError as exc:
        raise FreshExtractError(f"cannot safely snapshot archive: {exc}") from exc
    finally:
        if source_descriptor is not None:
            os.close(source_descriptor)


def normalized_member_name(info: zipfile.ZipInfo) -> tuple[str, tuple[str, ...]]:
    raw = info.filename
    if not raw or "\x00" in raw or "\\" in raw or raw.startswith("/"):
        raise FreshExtractError(f"unsafe ZIP path: {raw!r}")
    if info.is_dir():
        if not raw.endswith("/"):
            raise FreshExtractError(f"directory entry lacks trailing slash: {raw!r}")
        trimmed = raw[:-1]
    else:
        if raw.endswith("/"):
            raise FreshExtractError(f"file entry has trailing slash: {raw!r}")
        trimmed = raw
    if not trimmed:
        raise FreshExtractError("empty ZIP member path")
    pure = PurePosixPath(trimmed)
    parts = pure.parts
    if any(part in {"", ".", ".."} for part in parts):
        raise FreshExtractError(f"unsafe ZIP path component: {raw!r}")
    if pure.as_posix() != trimmed:
        raise FreshExtractError(f"nonnormalized ZIP path: {raw!r}")
    if parts[0] != PACKAGE_SLUG:
        raise FreshExtractError(f"unexpected top-level path: {raw!r}")
    return trimmed, parts


def inspect_archive(
    archive: zipfile.ZipFile,
    max_total_bytes: int,
    max_file_bytes: int,
    max_entries: int,
) -> list[zipfile.ZipInfo]:
    if archive.comment != b"":
        raise FreshExtractError("archive comment must be empty")
    infos = archive.infolist()
    if not infos:
        raise FreshExtractError("archive is empty")
    if len(infos) > max_entries:
        raise FreshExtractError("archive exceeds member-count limit")
    names = [info.filename for info in infos]
    if names != sorted(names):
        raise FreshExtractError("archive entries are not sorted")
    if len(names) != len(set(names)):
        raise FreshExtractError("archive contains duplicate member names")
    if len({name.casefold() for name in names}) != len(names):
        raise FreshExtractError("archive contains a case-insensitive path collision")

    normalized_files: set[str] = set()
    normalized_directories: set[str] = set()
    total_bytes = 0
    for info in infos:
        trimmed, parts = normalized_member_name(info)
        if info.flag_bits & 0x1:
            raise FreshExtractError(f"encrypted ZIP member is not permitted: {info.filename}")
        if info.create_system != 3:
            raise FreshExtractError(f"non-Unix ZIP metadata: {info.filename}")
        mode = (info.external_attr >> 16) & 0xFFFF
        if stat.S_ISLNK(mode):
            raise FreshExtractError(f"symbolic-link member is not permitted: {info.filename}")
        expected_mode = DIRECTORY_MODE if info.is_dir() else FILE_MODE
        if mode != expected_mode:
            raise FreshExtractError(f"unexpected member mode: {info.filename}")
        if info.date_time != FIXED_TIMESTAMP:
            raise FreshExtractError(f"nonfixed member timestamp: {info.filename}")
        if info.compress_type != zipfile.ZIP_STORED:
            raise FreshExtractError(f"unexpected member compression: {info.filename}")
        if info.extra or info.comment:
            raise FreshExtractError(f"unexpected member metadata: {info.filename}")
        if info.file_size != info.compress_size:
            raise FreshExtractError(f"stored member size mismatch: {info.filename}")

        if info.is_dir():
            if info.file_size != 0:
                raise FreshExtractError(
                    f"directory member contains a data payload: {info.filename}"
                )
            normalized_directories.add(trimmed)
        else:
            if info.file_size > max_file_bytes:
                raise FreshExtractError(f"member exceeds file-size limit: {info.filename}")
            total_bytes += info.file_size
            if total_bytes > max_total_bytes:
                raise FreshExtractError("archive exceeds total uncompressed-size limit")
            normalized_files.add(trimmed)
            for length in range(1, len(parts)):
                prefix = "/".join(parts[:length])
                if prefix in normalized_files:
                    raise FreshExtractError(
                        f"file/directory prefix collision at {info.filename}"
                    )

    if f"{PACKAGE_SLUG}/" not in names:
        raise FreshExtractError("archive lacks its explicit top-level directory")
    overlaps = sorted(normalized_files & normalized_directories)
    if overlaps:
        raise FreshExtractError(f"file/directory path collision: {overlaps}")
    missing = sorted(REQUIRED_ARCHIVE_PATHS - set(names))
    if missing:
        raise FreshExtractError(f"archive lacks required integrity files: {missing}")
    for file_name in normalized_files:
        parts = PurePosixPath(file_name).parts
        for length in range(1, len(parts)):
            prefix = "/".join(parts[:length])
            if prefix in normalized_files:
                raise FreshExtractError(f"file prefix collision: {file_name}")
    bad_member = archive.testzip()
    if bad_member is not None:
        raise FreshExtractError(f"CRC failure in ZIP member: {bad_member}")
    return infos


def contained_destination(root: Path, parts: tuple[str, ...]) -> Path:
    destination = root.joinpath(*parts)
    resolved_root = root.resolve(strict=True)
    resolved_destination = destination.resolve(strict=False)
    try:
        resolved_destination.relative_to(resolved_root)
    except ValueError as exc:
        raise FreshExtractError(f"extraction destination escapes root: {parts}") from exc
    return destination


def extract_members(
    archive: zipfile.ZipFile, infos: list[zipfile.ZipInfo], extraction_root: Path
) -> None:
    for info in infos:
        _, parts = normalized_member_name(info)
        destination = contained_destination(extraction_root, parts)
        if info.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            os.chmod(destination, 0o755)
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        written = 0
        try:
            with archive.open(info, "r") as source, destination.open("xb") as target:
                while True:
                    block = source.read(1024 * 1024)
                    if not block:
                        break
                    target.write(block)
                    written += len(block)
                target.flush()
                os.fsync(target.fileno())
        except OSError as exc:
            raise FreshExtractError(f"cannot extract {info.filename}: {exc}") from exc
        if written != info.file_size:
            raise FreshExtractError(f"extracted byte count differs: {info.filename}")
        os.chmod(destination, 0o644)


def verify_manifest_digest(package_root: Path) -> str:
    manifest_path = package_root / "integrity/manifest.json"
    sidecar_path = package_root / "integrity/manifest.sha256"
    try:
        manifest_bytes = manifest_path.read_bytes()
        sidecar_bytes = sidecar_path.read_bytes()
    except OSError as exc:
        raise FreshExtractError(f"cannot read extracted manifest integrity files: {exc}") from exc
    digest = sha256_bytes(manifest_bytes)
    expected = f"{digest}  manifest.json\n".encode("ascii")
    if sidecar_bytes != expected:
        raise FreshExtractError("manifest.sha256 does not match extracted manifest.json")
    return digest


def run_check(
    identifier: str,
    actual_command: list[str],
    logical_command: list[str],
    package_root: Path,
    timeout_seconds: int,
) -> dict[str, Any]:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    try:
        completed = subprocess.run(
            actual_command,
            cwd=package_root,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        raise FreshExtractError(
            f"fresh-extraction check {identifier} timed out after {timeout_seconds} seconds"
        ) from exc
    except OSError as exc:
        raise FreshExtractError(f"cannot run fresh-extraction check {identifier}: {exc}") from exc
    if completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace")
        raise FreshExtractError(
            f"fresh-extraction check {identifier} failed with exit "
            f"{completed.returncode}: {stderr!r}"
        )
    if completed.stderr:
        stderr = completed.stderr.decode("utf-8", errors="replace")
        raise FreshExtractError(
            f"fresh-extraction check {identifier} emitted stderr: {stderr!r}"
        )
    try:
        stdout_lines = completed.stdout.decode("utf-8", errors="strict").splitlines()
    except UnicodeDecodeError as exc:
        raise FreshExtractError(f"check {identifier} stdout is not UTF-8") from exc
    print(f"PASS fresh-extract check={identifier}", flush=True)
    return {
        "command": logical_command,
        "id": identifier,
        "pass": True,
        "stderr_sha256": sha256_bytes(completed.stderr),
        "stdout_lines": stdout_lines,
        "stdout_sha256": sha256_bytes(completed.stdout),
    }


def standard_checks(
    package_root: Path,
    timeout_seconds: int,
    full_replay: bool,
    manuscript_build: bool,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    commands = (
        (
            "manifest",
            [sys.executable, "tools/check_manifest.py", "--root", "."],
            ["python3", "tools/check_manifest.py", "--root", "."],
        ),
        (
            "claims",
            [sys.executable, "tools/check_claims.py", "--root", "."],
            ["python3", "tools/check_claims.py", "--root", "."],
        ),
        (
            "receipt-compare",
            [sys.executable, "verification/run_all.py", "--root", ".", "--compare-only"],
            ["python3", "verification/run_all.py", "--root", ".", "--compare-only"],
        ),
    )
    for identifier, actual, logical in commands:
        checks.append(
            run_check(identifier, actual, logical, package_root, timeout_seconds)
        )
    if full_replay:
        checks.append(
            run_check(
                "full-exact-replay",
                [sys.executable, "verification/run_all.py", "--root", ".", "--mode", "both"],
                ["python3", "verification/run_all.py", "--root", ".", "--mode", "both"],
                package_root,
                timeout_seconds,
            )
        )
    if manuscript_build:
        make_path = shutil.which("make")
        if make_path is None:
            raise FreshExtractError("make executable is unavailable for manuscript build")
        checks.append(
            run_check(
                "manuscript-build",
                [make_path, "manuscript"],
                ["make", "manuscript"],
                package_root,
                timeout_seconds,
            )
        )
    return checks


def receipt_record(
    archive_identity: dict[str, Any],
    expected_archive_digest: str,
    entry_count: int,
    manifest_digest: str,
    checks: list[dict[str, Any]],
    full_replay: bool,
    manuscript_build: bool,
) -> dict[str, Any]:
    return {
        "archive": {
            "bytes": archive_identity["bytes"],
            "entry_count": entry_count,
            "expected_sha256": expected_archive_digest,
            "sha256": archive_identity["sha256"],
            "top_level_slug": PACKAGE_SLUG,
        },
        "checks": checks,
        "environment": {
            "machine": platform.machine(),
            "platform": platform.platform(),
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "system": platform.system(),
        },
        "manifest_sha256": manifest_digest,
        "options": {
            "full_exact_replay": full_replay,
            "manuscript_build": manuscript_build,
        },
        "pass": True,
        "schema_version": "1.0",
    }


def write_external_receipt(path: Path, data: bytes) -> None:
    if path.exists():
        raise FreshExtractError(f"refusing to overwrite external receipt: {path}")
    if not path.parent.is_dir():
        raise FreshExtractError(f"receipt parent does not exist: {path.parent}")
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent, prefix=f".{path.name}.", suffix=".tmp"
    )
    try:
        with os.fdopen(descriptor, "wb") as handle:
            written = handle.write(data)
            if written != len(data):
                raise FreshExtractError("short write while creating external receipt")
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary_name, 0o644)
        try:
            os.link(temporary_name, path)
        except FileExistsError as exc:
            raise FreshExtractError(
                f"refusing to overwrite concurrently created external receipt: {path}"
            ) from exc
        os.unlink(temporary_name)
    except OSError as exc:
        raise FreshExtractError(f"cannot write external receipt: {exc}") from exc
    finally:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--expected-archive-sha256", required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--full-replay", action="store_true")
    parser.add_argument("--manuscript-build", action="store_true")
    parser.add_argument("--timeout-seconds", type=int, default=900)
    parser.add_argument("--max-total-bytes", type=int, default=1024 * 1024 * 1024)
    parser.add_argument("--max-file-bytes", type=int, default=256 * 1024 * 1024)
    parser.add_argument("--max-archive-bytes", type=int, default=1024 * 1024 * 1024)
    parser.add_argument("--max-entries", type=int, default=10_000)
    parser.add_argument("--temp-parent", type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.timeout_seconds <= 0:
            raise FreshExtractError("timeout must be positive")
        if (
            args.max_total_bytes <= 0
            or args.max_file_bytes <= 0
            or args.max_archive_bytes <= 0
            or args.max_entries <= 0
        ):
            raise FreshExtractError("archive size limits must be positive")
        expected_archive_digest = normalized_sha256(args.expected_archive_sha256)
        archive_path = args.archive.resolve(strict=True)
        if not archive_path.is_file():
            raise FreshExtractError(f"archive is not a file: {archive_path}")
        receipt_path = args.receipt.resolve(strict=False)
        if receipt_path == archive_path:
            raise FreshExtractError("external receipt cannot overwrite the archive")
        if receipt_path.exists():
            raise FreshExtractError(f"external receipt already exists: {receipt_path}")
        temp_parent = None
        if args.temp_parent is not None:
            temp_parent = args.temp_parent.resolve(strict=True)
            if not temp_parent.is_dir():
                raise FreshExtractError(f"temp parent is not a directory: {temp_parent}")

        with tempfile.TemporaryDirectory(
            prefix="dlcl-fresh-extract.", dir=temp_parent
        ) as temporary:
            extraction_root = Path(temporary)
            archive_snapshot = extraction_root / "archive.snapshot.zip"
            archive_identity = snapshot_archive(
                archive_path, archive_snapshot, args.max_archive_bytes
            )
            if archive_identity["sha256"] != expected_archive_digest:
                raise FreshExtractError(
                    "archive SHA-256 does not match externally supplied expected digest"
                )
            print("PASS fresh-extract archive-digest", flush=True)
            try:
                archive = zipfile.ZipFile(archive_snapshot, mode="r")
            except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile) as exc:
                raise FreshExtractError(f"cannot open archive: {exc}") from exc
            with archive:
                infos = inspect_archive(
                    archive,
                    args.max_total_bytes,
                    args.max_file_bytes,
                    args.max_entries,
                )
                extract_members(archive, infos, extraction_root)
            package_root = extraction_root / PACKAGE_SLUG

            # Both digest gates are intentionally before any extracted code runs.
            manifest_digest = verify_manifest_digest(package_root)
            print("PASS fresh-extract manifest-digest", flush=True)
            checks = standard_checks(
                package_root,
                args.timeout_seconds,
                args.full_replay,
                args.manuscript_build,
            )
            record = receipt_record(
                archive_identity,
                expected_archive_digest,
                len(infos),
                manifest_digest,
                checks,
                args.full_replay,
                args.manuscript_build,
            )
            receipt_bytes = canonical_json_bytes(record)
            write_external_receipt(receipt_path, receipt_bytes)
            print(
                f"PASS fresh-extract receipt_sha256={sha256_bytes(receipt_bytes)} "
                f"receipt={receipt_path}",
                flush=True,
            )
        return 0
    except (
        FreshExtractError,
        OSError,
        ValueError,
        zipfile.BadZipFile,
        zipfile.LargeZipFile,
    ) as exc:
        print(f"FAIL fresh extract: {exc}", file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
