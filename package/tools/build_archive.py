#!/usr/bin/env python3
"""Create a deterministic, integrity-preflighted ZIP of the DLCL package."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import stat
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable


PACKAGE_SLUG = "determinant-lines-character-lattices"
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
FILE_MODE = stat.S_IFREG | 0o644
DIRECTORY_MODE = stat.S_IFDIR | 0o755
REQUIRED_INTEGRITY_FILES = {
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


class ArchiveBuildError(RuntimeError):
    """Raised when source or archive state violates the deterministic profile."""


@dataclass(frozen=True)
class ArchiveEntry:
    archive_name: str
    source_path: Path | None
    is_directory: bool


def require_safe_open_flags() -> tuple[int, int]:
    nofollow = getattr(os, "O_NOFOLLOW", None)
    directory = getattr(os, "O_DIRECTORY", None)
    if nofollow is None or directory is None:
        raise ArchiveBuildError(
            "descriptor-bound no-follow reads are unavailable on this platform"
        )
    common = os.O_RDONLY | nofollow | getattr(os, "O_CLOEXEC", 0)
    return common, common | directory


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalized_relative(path: Path, root: Path) -> str:
    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise ArchiveBuildError(f"path escapes package root: {path}") from exc
    text = PurePosixPath(*relative.parts).as_posix()
    if not text or text.startswith("/") or "\\" in text:
        raise ArchiveBuildError(f"noncanonical source path: {text!r}")
    if any(part in {"", ".", ".."} for part in PurePosixPath(text).parts):
        raise ArchiveBuildError(f"unsafe source path: {text!r}")
    return text


def is_transient(relative: str) -> bool:
    return any(part in TRANSIENT_PARTS for part in PurePosixPath(relative).parts)


def collect_source_files(root: Path) -> list[tuple[str, Path]]:
    files: list[tuple[str, Path]] = []
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        relative = normalized_relative(path, root)
        if is_transient(relative):
            continue
        if path.is_symlink():
            raise ArchiveBuildError(f"symbolic links are not permitted: {relative}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise ArchiveBuildError(f"non-regular source entry: {relative}")
        files.append((relative, path))

    return files


def collect_entries(root: Path) -> list[ArchiveEntry]:
    files = collect_source_files(root)

    file_paths = {relative for relative, _ in files}
    missing_integrity = sorted(REQUIRED_INTEGRITY_FILES - file_paths)
    if missing_integrity:
        raise ArchiveBuildError(
            f"package is not ready for archiving; missing {missing_integrity}"
        )

    directory_names = {f"{PACKAGE_SLUG}/"}
    for relative, _ in files:
        parts = PurePosixPath(relative).parts[:-1]
        for length in range(1, len(parts) + 1):
            directory_names.add(
                f"{PACKAGE_SLUG}/{'/'.join(parts[:length])}/"
            )

    entries = [
        ArchiveEntry(name, None, True) for name in sorted(directory_names)
    ]
    entries.extend(
        ArchiveEntry(f"{PACKAGE_SLUG}/{relative}", path, False)
        for relative, path in files
    )
    entries.sort(key=lambda entry: entry.archive_name)
    names = [entry.archive_name for entry in entries]
    if len(names) != len(set(names)):
        raise ArchiveBuildError("duplicate deterministic archive entry")
    if len({name.casefold() for name in names}) != len(names):
        raise ArchiveBuildError("case-insensitive archive-name collision")
    return entries


def read_regular_file_nofollow(root: Path, relative: str) -> bytes:
    file_flags, directory_flags = require_safe_open_flags()
    parts = PurePosixPath(relative).parts
    if not parts:
        raise ArchiveBuildError("cannot snapshot an empty relative path")
    descriptors: list[int] = []
    file_descriptor: int | None = None
    try:
        current = os.open(root, directory_flags)
        descriptors.append(current)
        for part in parts[:-1]:
            current = os.open(part, directory_flags, dir_fd=current)
            descriptors.append(current)
        file_descriptor = os.open(parts[-1], file_flags, dir_fd=current)
        before = os.fstat(file_descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise ArchiveBuildError(f"source entry is not a regular file: {relative}")
        chunks: list[bytes] = []
        while True:
            block = os.read(file_descriptor, 1024 * 1024)
            if not block:
                break
            chunks.append(block)
        after = os.fstat(file_descriptor)
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
        if before_identity != after_identity:
            raise ArchiveBuildError(f"source changed while being snapshotted: {relative}")
        data = b"".join(chunks)
        if len(data) != after.st_size:
            raise ArchiveBuildError(f"source byte count changed while reading: {relative}")
        return data
    except OSError as exc:
        raise ArchiveBuildError(f"cannot safely snapshot {relative}: {exc}") from exc
    finally:
        if file_descriptor is not None:
            os.close(file_descriptor)
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def snapshot_package(source_root: Path, snapshot_root: Path) -> None:
    snapshot_root.mkdir(mode=0o700)
    files = collect_source_files(source_root)
    file_paths = {relative for relative, _ in files}
    missing_integrity = sorted(REQUIRED_INTEGRITY_FILES - file_paths)
    if missing_integrity:
        raise ArchiveBuildError(
            f"package is not ready for archiving; missing {missing_integrity}"
        )
    for relative, _ in files:
        data = read_regular_file_nofollow(source_root, relative)
        destination = snapshot_root.joinpath(*PurePosixPath(relative).parts)
        destination.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
        try:
            with destination.open("xb") as handle:
                written = handle.write(data)
                if written != len(data):
                    raise ArchiveBuildError(f"short snapshot write: {relative}")
            os.chmod(destination, 0o644)
        except OSError as exc:
            raise ArchiveBuildError(f"cannot write package snapshot {relative}: {exc}") from exc


def run_preflight(root: Path, timeout_seconds: int) -> None:
    commands = (
        (
            "manifest",
            [sys.executable, str(root / "tools/check_manifest.py"), "--root", str(root)],
        ),
        (
            "claims",
            [sys.executable, str(root / "tools/check_claims.py"), "--root", str(root)],
        ),
        (
            "receipts",
            [
                sys.executable,
                str(root / "verification/run_all.py"),
                "--root",
                str(root),
                "--compare-only",
            ],
        ),
    )
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    for identifier, command in commands:
        try:
            completed = subprocess.run(
                command,
                cwd=root,
                env=environment,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired as exc:
            raise ArchiveBuildError(
                f"preflight {identifier} timed out after {timeout_seconds} seconds"
            ) from exc
        if completed.returncode != 0:
            stderr = completed.stderr.decode("utf-8", errors="replace")
            raise ArchiveBuildError(
                f"preflight {identifier} failed with exit {completed.returncode}: {stderr!r}"
            )
        if completed.stderr:
            stderr = completed.stderr.decode("utf-8", errors="replace")
            raise ArchiveBuildError(
                f"preflight {identifier} emitted stderr: {stderr!r}"
            )
        print(f"PASS archive preflight={identifier}", flush=True)


def zip_info(name: str, is_directory: bool) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(filename=name, date_time=FIXED_TIMESTAMP)
    info.create_system = 3
    info.create_version = 20
    info.extract_version = 20
    info.compress_type = zipfile.ZIP_STORED
    info.comment = b""
    info.extra = b""
    mode = DIRECTORY_MODE if is_directory else FILE_MODE
    info.external_attr = mode << 16
    if is_directory:
        info.external_attr |= 0x10
    return info


def write_archive_temporary(output: Path, entries: Iterable[ArchiveEntry]) -> Path:
    descriptor, temporary_name = tempfile.mkstemp(
        dir=output.parent, prefix=f".{output.name}.", suffix=".tmp"
    )
    os.close(descriptor)
    try:
        with zipfile.ZipFile(
            temporary_name,
            mode="w",
            compression=zipfile.ZIP_STORED,
            allowZip64=True,
            strict_timestamps=True,
        ) as archive:
            archive.comment = b""
            for entry in entries:
                info = zip_info(entry.archive_name, entry.is_directory)
                if entry.is_directory:
                    data = b""
                else:
                    if entry.source_path is None:
                        raise ArchiveBuildError(
                            f"file entry lacks source: {entry.archive_name}"
                        )
                    data = entry.source_path.read_bytes()
                archive.writestr(info, data, compress_type=zipfile.ZIP_STORED)
        with open(temporary_name, "rb") as handle:
            os.fsync(handle.fileno())
        os.chmod(temporary_name, 0o644)
        return Path(temporary_name)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def publish_archive(temporary_path: Path, output: Path) -> None:
    try:
        os.link(temporary_path, output)
    except FileExistsError as exc:
        raise ArchiveBuildError(
            f"refusing to overwrite concurrently created archive: {output}"
        ) from exc
    except OSError as exc:
        raise ArchiveBuildError(f"cannot publish verified archive: {exc}") from exc


def verify_written_archive(output: Path, expected_entries: list[ArchiveEntry]) -> None:
    expected_names = [entry.archive_name for entry in expected_entries]
    try:
        with zipfile.ZipFile(output, mode="r") as archive:
            if archive.comment != b"":
                raise ArchiveBuildError("archive comment is not empty")
            infos = archive.infolist()
            observed_names = [info.filename for info in infos]
            if observed_names != expected_names:
                raise ArchiveBuildError("written archive entry order or names differ")
            for info, entry in zip(infos, expected_entries, strict=True):
                if info.date_time != FIXED_TIMESTAMP:
                    raise ArchiveBuildError(f"timestamp drift: {info.filename}")
                if info.create_system != 3:
                    raise ArchiveBuildError(f"non-Unix ZIP metadata: {info.filename}")
                expected_mode = DIRECTORY_MODE if entry.is_directory else FILE_MODE
                observed_mode = (info.external_attr >> 16) & 0xFFFF
                if observed_mode != expected_mode:
                    raise ArchiveBuildError(f"permission drift: {info.filename}")
                if info.compress_type != zipfile.ZIP_STORED:
                    raise ArchiveBuildError(f"unexpected compression: {info.filename}")
                if info.extra or info.comment:
                    raise ArchiveBuildError(f"unexpected ZIP metadata: {info.filename}")
            bad_entry = archive.testzip()
            if bad_entry is not None:
                raise ArchiveBuildError(f"CRC failure after archive write: {bad_entry}")
    except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile) as exc:
        raise ArchiveBuildError(f"cannot verify written archive: {exc}") from exc


def validate_output_path(root: Path, output: Path) -> Path:
    if output.suffix.lower() != ".zip":
        raise ArchiveBuildError("output filename must end in .zip")
    if not output.parent.is_dir():
        raise ArchiveBuildError(f"output parent does not exist: {output.parent}")
    try:
        output.relative_to(root)
    except ValueError:
        pass
    else:
        raise ArchiveBuildError("archive output must be outside the package root")
    if output.exists():
        raise ArchiveBuildError(f"refusing to overwrite existing archive: {output}")
    return output


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--timeout-seconds", type=int, default=900)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.timeout_seconds <= 0:
            raise ArchiveBuildError("timeout must be positive")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", PACKAGE_SLUG):
            raise ArchiveBuildError("invalid fixed package slug")
        root = args.root.resolve(strict=True)
        if not root.is_dir():
            raise ArchiveBuildError(f"package root is not a directory: {root}")
        output = validate_output_path(root, args.output.resolve(strict=False))
        with tempfile.TemporaryDirectory(
            dir=output.parent, prefix=f".{PACKAGE_SLUG}.snapshot."
        ) as snapshot_parent:
            snapshot_root = Path(snapshot_parent) / PACKAGE_SLUG
            snapshot_package(root, snapshot_root)
            run_preflight(snapshot_root, args.timeout_seconds)
            entries = collect_entries(snapshot_root)
            temporary_archive = write_archive_temporary(output, entries)
            try:
                verify_written_archive(temporary_archive, entries)
                archive_bytes = temporary_archive.stat().st_size
                archive_digest = sha256_file(temporary_archive)
                publish_archive(temporary_archive, output)
            finally:
                try:
                    temporary_archive.unlink()
                except FileNotFoundError:
                    pass
        print(
            f"PASS archive entries={len(entries)} bytes={archive_bytes} "
            f"sha256={archive_digest} output={output}",
            flush=True,
        )
        return 0
    except (ArchiveBuildError, OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"FAIL archive build: {exc}", file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
