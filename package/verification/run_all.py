#!/usr/bin/env python3
"""Run and validate the four exact DLCL verification suites.

Default execution runs every checker in normal and optimized (``python -O``)
modes.  Raw runtime lines are retained in separate environment receipts; the
canonical mathematical receipts omit only those configured lines and must be
byte-identical across modes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable


SCHEMA_VERSION = "1.0"


class VerificationError(RuntimeError):
    """Raised when a frozen input, subprocess, or output contract fails."""


@dataclass(frozen=True)
class FrozenFile:
    path: str
    sha256: str


@dataclass(frozen=True)
class Suite:
    evidence_id: str
    script: FrozenFile
    baselines: tuple[FrozenFile, FrozenFile]
    normal_receipt: str
    optimized_receipt: str
    normal_environment: str
    optimized_environment: str
    expected_result_lines: tuple[str, ...]
    expected_environment_lines: int
    negative_controls: tuple[tuple[str, str], ...]
    summary: dict[str, int]
    count_parser: Callable[[tuple[str, ...]], dict[str, int]]


def parse_sympy_counts(lines: tuple[str, ...]) -> dict[str, int]:
    case_pattern = re.compile(r"^PASS degrees=.* coordinates=([0-9]+) orientation=[+-][0-9]+$")
    coordinates: list[int] = []
    for line in lines:
        match = case_pattern.match(line)
        if match:
            coordinates.append(int(match.group(1)))
    if len(coordinates) != 7:
        raise VerificationError(f"SymPy case summary count is {len(coordinates)}, expected 7")
    return {
        "case_count": len(coordinates),
        "pluecker_coordinates": sum(coordinates),
        "positive_comparisons": sum(coordinates),
    }


def parse_flint_counts(lines: tuple[str, ...]) -> dict[str, int]:
    case_pattern = re.compile(
        r"^PASS FLINT degrees=.* coordinates=([0-9]+) orientation=[+-][0-9]+$"
    )
    total_pattern = re.compile(r"^PASS total symbolic Pluecker coordinates=([0-9]+)$")
    coordinates = [
        int(match.group(1))
        for line in lines
        if (match := case_pattern.match(line)) is not None
    ]
    totals = [
        int(match.group(1))
        for line in lines
        if (match := total_pattern.match(line)) is not None
    ]
    border_count = sum(line.startswith("PASS FLINT multiborder ") for line in lines)
    if len(coordinates) != 5:
        raise VerificationError(f"FLINT case summary count is {len(coordinates)}, expected 5")
    if totals != [sum(coordinates)]:
        raise VerificationError(
            f"FLINT total summary {totals} does not equal case sum {sum(coordinates)}"
        )
    if border_count != 2:
        raise VerificationError(f"FLINT border summary count is {border_count}, expected 2")
    return {
        "border_determinants": border_count,
        "case_count": len(coordinates),
        "pluecker_coordinates": sum(coordinates),
        "positive_comparisons": sum(coordinates) + border_count,
    }


def parse_character_counts(lines: tuple[str, ...]) -> dict[str, int]:
    patterns = {
        "tree_determinants": re.compile(r"^PASS tree determinant formula checks=([0-9]+)$"),
        "general_graph_minors": re.compile(
            r"^PASS general maximal-minor graph formula checks=([0-9]+)$"
        ),
        "smith_and_bad_prime_checks": re.compile(
            r"^PASS Smith structure and bad-prime checks=([0-9]+)$"
        ),
    }
    counts: dict[str, int] = {}
    for key, pattern in patterns.items():
        matches = [
            int(match.group(1))
            for line in lines
            if (match := pattern.match(line)) is not None
        ]
        if len(matches) != 1:
            raise VerificationError(f"character summary {key} appears {len(matches)} times")
        counts[key] = matches[0]
    counts["positive_comparisons"] = sum(counts.values())
    return counts


def parse_local_smith_counts(lines: tuple[str, ...]) -> dict[str, int]:
    patterns = {
        "local_global_smith": re.compile(r"^PASS local/global Smith checks=([0-9]+)$"),
        "tree_gcd": re.compile(r"^PASS tree-gcd checks=([0-9]+)$"),
        "displayed_examples": re.compile(r"^PASS displayed examples=([0-9]+)$"),
    }
    counts: dict[str, int] = {}
    for key, pattern in patterns.items():
        matches = [
            int(match.group(1))
            for line in lines
            if (match := pattern.match(line)) is not None
        ]
        if len(matches) != 1:
            raise VerificationError(f"local Smith summary {key} appears {len(matches)} times")
        counts[key] = matches[0]
    counts["positive_comparisons"] = sum(counts.values())
    summary_pattern = re.compile(
        r"^PASS summary positive=([0-9]+) negative_controls=([0-9]+)$"
    )
    summaries = [
        (int(match.group(1)), int(match.group(2)))
        for line in lines
        if (match := summary_pattern.match(line)) is not None
    ]
    if summaries != [(counts["positive_comparisons"], 5)]:
        raise VerificationError(
            f"local Smith final summary {summaries} does not match parsed counts"
        )
    return counts


SUITES = (
    Suite(
        evidence_id="sympy-plucker",
        script=FrozenFile(
            "verification/checks/verify_multifactor_sympy.py",
            "3806a7c9b4bf38598cc31ef438783984792d7e58f15d5fcf0726b93dd1879ebe",
        ),
        baselines=(
            FrozenFile(
                "verification/receipts/baseline/stage1/exploratory_receipt.txt",
                "27d4ea5a3e89a95ffd31d426f8d4ae50ad37794652f5cc60bec324c7e09133e2",
            ),
            FrozenFile(
                "verification/receipts/baseline/stage1/exploratory_receipt_optimized.txt",
                "27d4ea5a3e89a95ffd31d426f8d4ae50ad37794652f5cc60bec324c7e09133e2",
            ),
        ),
        normal_receipt="verification/receipts/regenerated/sympy-plucker.normal.json",
        optimized_receipt="verification/receipts/regenerated/sympy-plucker.optimized.json",
        normal_environment="verification/receipts/environment/sympy-plucker.normal.json",
        optimized_environment="verification/receipts/environment/sympy-plucker.optimized.json",
        expected_result_lines=(
            "PASS degrees=(1, 1) factors=2 coordinates=4 orientation=+1",
            "PASS degrees=(1, 2) factors=2 coordinates=5 orientation=-1",
            "PASS degrees=(1, 1, 1) factors=3 coordinates=15 orientation=-1",
            "PASS degrees=(1, 1, 2) factors=3 coordinates=21 orientation=-1",
            "PASS degrees=(1, 2, 1) factors=3 coordinates=21 orientation=+1",
            "PASS degrees=(2, 1, 1) factors=3 coordinates=21 orientation=-1",
            "PASS degrees=(1, 1, 1, 1) factors=4 coordinates=56 orientation=-1",
            "PASS NC1 missing pairwise resultant detected",
            "PASS NC2 squared collision product detected",
            "PASS NC3 reversed torus basis vector detected",
            "PASS NC4 omitted recursive orientation constant detected",
            "PASS NC5 perturbed convolution differential detected",
        ),
        expected_environment_lines=0,
        negative_controls=(
            ("nc1-missing-resultant", "PASS NC1 missing pairwise resultant detected"),
            ("nc2-squared-collision-product", "PASS NC2 squared collision product detected"),
            ("nc3-reversed-torus-row", "PASS NC3 reversed torus basis vector detected"),
            (
                "nc4-wrong-recursive-orientation",
                "PASS NC4 omitted recursive orientation constant detected",
            ),
            ("nc5-perturbed-differential", "PASS NC5 perturbed convolution differential detected"),
        ),
        summary={
            "case_count": 7,
            "pluecker_coordinates": 143,
            "positive_comparisons": 143,
        },
        count_parser=parse_sympy_counts,
    ),
    Suite(
        evidence_id="flint-plucker-border",
        script=FrozenFile(
            "verification/checks/verify_multifactor_flint.py",
            "e7de053c910d800bbdc73dd15ebc7d42bf135e2853c97c84e58754557db98adb",
        ),
        baselines=(
            FrozenFile(
                "verification/receipts/baseline/stage1/multifactor_flint_receipt.txt",
                "f352edfd686e54fc5894839bcba05f9686aa36617a5563a1f73e53d5929588c4",
            ),
            FrozenFile(
                "verification/receipts/baseline/stage1/multifactor_flint_receipt_optimized.txt",
                "f352edfd686e54fc5894839bcba05f9686aa36617a5563a1f73e53d5929588c4",
            ),
        ),
        normal_receipt="verification/receipts/regenerated/flint-plucker-border.normal.json",
        optimized_receipt="verification/receipts/regenerated/flint-plucker-border.optimized.json",
        normal_environment="verification/receipts/environment/flint-plucker-border.normal.json",
        optimized_environment="verification/receipts/environment/flint-plucker-border.optimized.json",
        expected_result_lines=(
            "multifactor Pluecker exact FLINT verification",
            "PASS FLINT degrees=(1, 1, 1) coordinates=15 orientation=-1",
            "PASS FLINT degrees=(1, 1, 2) coordinates=21 orientation=-1",
            "PASS FLINT degrees=(1, 2, 1) coordinates=21 orientation=+1",
            "PASS FLINT degrees=(2, 1, 1) coordinates=21 orientation=-1",
            "PASS FLINT degrees=(1, 1, 1, 1) coordinates=56 orientation=-1",
            "PASS FLINT multiborder degrees=(1, 1, 1) edges=((0, 1), (1, 2)) detW=+1",
            "PASS FLINT multiborder degrees=(1, 1, 2) edges=((0, 1), (1, 2)) detW=+2",
            "PASS FLINT NC1 missing pairwise resultant detected",
            "PASS FLINT NC2 reversed torus basis vector detected",
            "PASS FLINT NC3 wrong orientation detected",
            "PASS FLINT NC4 perturbed differential detected",
            "PASS total symbolic Pluecker coordinates=134",
        ),
        expected_environment_lines=1,
        negative_controls=(
            ("nc1-missing-resultant", "PASS FLINT NC1 missing pairwise resultant detected"),
            ("nc2-reversed-torus-row", "PASS FLINT NC2 reversed torus basis vector detected"),
            ("nc3-wrong-orientation", "PASS FLINT NC3 wrong orientation detected"),
            ("nc4-perturbed-differential", "PASS FLINT NC4 perturbed differential detected"),
        ),
        summary={
            "border_determinants": 2,
            "case_count": 5,
            "pluecker_coordinates": 134,
            "positive_comparisons": 136,
        },
        count_parser=parse_flint_counts,
    ),
    Suite(
        evidence_id="character-lattice",
        script=FrozenFile(
            "verification/checks/verify_character_lattice.py",
            "b91d2c7b0f11a5470fd1bf41964b579973ae6b15cb3cc18e6e5b4854225bd91a",
        ),
        baselines=(
            FrozenFile(
                "verification/receipts/baseline/stage1/character_lattice_receipt.txt",
                "5efd7944b92cb8e9422d3ea33b17545a6e0b386489ce01c9578dc02e8997df51",
            ),
            FrozenFile(
                "verification/receipts/baseline/stage1/character_lattice_receipt_optimized.txt",
                "5efd7944b92cb8e9422d3ea33b17545a6e0b386489ce01c9578dc02e8997df51",
            ),
        ),
        normal_receipt="verification/receipts/regenerated/character-lattice.normal.json",
        optimized_receipt="verification/receipts/regenerated/character-lattice.optimized.json",
        normal_environment="verification/receipts/environment/character-lattice.normal.json",
        optimized_environment="verification/receipts/environment/character-lattice.optimized.json",
        expected_result_lines=(
            "character-lattice exact verification",
            "bounds=max_vertices:5,max_degree:3",
            "PASS tree determinant formula checks=31761",
            "PASS general maximal-minor graph formula checks=52741",
            "PASS Smith structure and bad-prime checks=351",
            "PASS NC1 total sum substituted for bipartite balance detected",
            "PASS NC2 odd-cycle factor 2 omitted detected",
            "PASS NC3 common gcd omitted from Smith form detected",
            "PASS NC4 rank-one equal-degree collapse extrapolated to k=3 detected",
        ),
        expected_environment_lines=1,
        negative_controls=(
            (
                "nc1-total-sum-for-bipartite-balance",
                "PASS NC1 total sum substituted for bipartite balance detected",
            ),
            ("nc2-odd-cycle-factor-two-omitted", "PASS NC2 odd-cycle factor 2 omitted detected"),
            ("nc3-common-gcd-omitted", "PASS NC3 common gcd omitted from Smith form detected"),
            (
                "nc4-rank-one-collapse-extrapolated",
                "PASS NC4 rank-one equal-degree collapse extrapolated to k=3 detected",
            ),
        ),
        summary={
            "general_graph_minors": 52741,
            "positive_comparisons": 84853,
            "smith_and_bad_prime_checks": 351,
            "tree_determinants": 31761,
        },
        count_parser=parse_character_counts,
    ),
    Suite(
        evidence_id="local-smith",
        script=FrozenFile(
            "verification/checks/verify_local_smith.py",
            "09ce5ad767d89dd03c29718da7f6b1c2dbce1b8aac9f9eb4566fdebb22a2906a",
        ),
        baselines=(
            FrozenFile(
                "verification/receipts/baseline/stage4/local_smith_receipt.txt",
                "4d437bf2a6c885cc71f69f365d966ccce055cc05ee505dedc4678618401f40c4",
            ),
            FrozenFile(
                "verification/receipts/baseline/stage4/local_smith_receipt_optimized.txt",
                "4d437bf2a6c885cc71f69f365d966ccce055cc05ee505dedc4678618401f40c4",
            ),
        ),
        normal_receipt="verification/receipts/regenerated/local-smith.normal.json",
        optimized_receipt="verification/receipts/regenerated/local-smith.optimized.json",
        normal_environment="verification/receipts/environment/local-smith.normal.json",
        optimized_environment="verification/receipts/environment/local-smith.optimized.json",
        expected_result_lines=(
            "local Smith exact verification",
            "PASS local/global Smith checks=42727",
            "PASS tree-gcd checks=1485",
            "PASS displayed examples=8",
            "PASS NC1 factor-two omission detected",
            "PASS NC2 odd support substituted for valuation detected",
            "PASS NC3 two-adic support substituted for valuation detected",
            "PASS NC4 full-list gcd replaced by edge basis detected",
            "PASS NC5 nonprimitive content omitted detected",
            "PASS deliberate negative controls detected=5",
            "PASS summary positive=44220 negative_controls=5",
        ),
        expected_environment_lines=1,
        negative_controls=(
            ("nc1-factor-two-omitted", "PASS NC1 factor-two omission detected"),
            (
                "nc2-odd-support-for-valuation",
                "PASS NC2 odd support substituted for valuation detected",
            ),
            (
                "nc3-two-adic-support-for-valuation",
                "PASS NC3 two-adic support substituted for valuation detected",
            ),
            (
                "nc4-full-list-gcd-replaced-by-edge-basis",
                "PASS NC4 full-list gcd replaced by edge basis detected",
            ),
            (
                "nc5-nonprimitive-content-omitted",
                "PASS NC5 nonprimitive content omitted detected",
            ),
        ),
        summary={
            "displayed_examples": 8,
            "local_global_smith": 42727,
            "positive_comparisons": 44220,
            "tree_gcd": 1485,
        },
        count_parser=parse_local_smith_counts,
    ),
)


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
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


def verify_frozen_file(root: Path, frozen: FrozenFile) -> bytes:
    path = root / frozen.path
    try:
        data = path.read_bytes()
    except OSError as exc:
        raise VerificationError(f"cannot read frozen file {frozen.path}: {exc}") from exc
    observed = sha256_bytes(data)
    if observed != frozen.sha256:
        raise VerificationError(
            f"frozen file hash drift for {frozen.path}: expected {frozen.sha256}, observed {observed}"
        )
    return data


def verify_frozen_inputs(root: Path) -> None:
    for suite in SUITES:
        verify_frozen_file(root, suite.script)
        baseline_data = [verify_frozen_file(root, item) for item in suite.baselines]
        if baseline_data[0] != baseline_data[1]:
            raise VerificationError(
                f"Stage-1 normal/optimized baseline mismatch for {suite.evidence_id}"
            )


def result_receipt(suite: Suite) -> dict[str, Any]:
    return {
        "evidence_set": suite.evidence_id,
        "negative_control_count": len(suite.negative_controls),
        "negative_controls": [
            {"detected": True, "id": identifier, "line": line}
            for identifier, line in suite.negative_controls
        ],
        "pass": True,
        "result_lines": list(suite.expected_result_lines),
        "schema_version": SCHEMA_VERSION,
        "script_sha256": suite.script.sha256,
        "summary": dict(suite.summary),
    }


def command_for(root: Path, suite: Suite, mode: str) -> tuple[list[str], list[str]]:
    executable = sys.executable
    logical = ["python3"]
    actual = [executable]
    if mode == "optimized":
        logical.append("-O")
        actual.append("-O")
    logical.append(suite.script.path)
    actual.append(str(root / suite.script.path))
    return actual, logical


def split_runtime_lines(
    suite: Suite, stdout: bytes
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    try:
        text = stdout.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise VerificationError(f"{suite.evidence_id}: stdout is not UTF-8") from exc
    lines = tuple(text.splitlines())
    environment = tuple(line for line in lines if line.startswith("python="))
    results = tuple(line for line in lines if not line.startswith("python="))
    if len(environment) != suite.expected_environment_lines:
        raise VerificationError(
            f"{suite.evidence_id}: expected {suite.expected_environment_lines} runtime lines, "
            f"observed {len(environment)}"
        )
    return results, environment


def validate_result_lines(suite: Suite, lines: tuple[str, ...]) -> None:
    if lines != suite.expected_result_lines:
        missing = [line for line in suite.expected_result_lines if line not in lines]
        unexpected = [line for line in lines if line not in suite.expected_result_lines]
        raise VerificationError(
            f"{suite.evidence_id}: result-line contract failed; "
            f"missing={missing}, unexpected={unexpected}, order_or_duplicates_may_differ=True"
        )
    observed_negative = tuple(line for line in lines if " NC" in line)
    expected_negative = tuple(line for _, line in suite.negative_controls)
    if observed_negative != expected_negative:
        raise VerificationError(
            f"{suite.evidence_id}: negative-control lines differ from contract"
        )
    parsed = suite.count_parser(lines)
    if parsed != suite.summary:
        raise VerificationError(
            f"{suite.evidence_id}: parsed summary {parsed} differs from expected {suite.summary}"
        )


def environment_receipt(
    suite: Suite,
    mode: str,
    logical_command: list[str],
    environment_lines: tuple[str, ...],
    stdout: bytes,
    stderr: bytes,
) -> dict[str, Any]:
    return {
        "command": logical_command,
        "evidence_set": suite.evidence_id,
        "interpreter": {
            "executable": sys.executable,
            "implementation": platform.python_implementation(),
            "version": platform.python_version(),
        },
        "mode": mode,
        "platform": {
            "machine": platform.machine(),
            "platform": platform.platform(),
            "release": platform.release(),
            "system": platform.system(),
        },
        "raw_environment_lines": list(environment_lines),
        "raw_stderr_sha256": sha256_bytes(stderr),
        "raw_stdout_sha256": sha256_bytes(stdout),
        "schema_version": SCHEMA_VERSION,
        "script_sha256": suite.script.sha256,
    }


def run_mode(
    root: Path, suite: Suite, mode: str, timeout_seconds: int
) -> tuple[bytes, bytes]:
    actual_command, logical_command = command_for(root, suite, mode)
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    print(f"RUN evidence={suite.evidence_id} mode={mode}", flush=True)
    try:
        completed = subprocess.run(
            actual_command,
            cwd=root,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        raise VerificationError(
            f"{suite.evidence_id} {mode}: timeout after {timeout_seconds} seconds"
        ) from exc
    if completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace")
        raise VerificationError(
            f"{suite.evidence_id} {mode}: exit={completed.returncode}; stderr={stderr!r}"
        )
    if completed.stderr:
        stderr = completed.stderr.decode("utf-8", errors="replace")
        raise VerificationError(
            f"{suite.evidence_id} {mode}: unexpected stderr={stderr!r}"
        )
    result_lines, environment_lines = split_runtime_lines(suite, completed.stdout)
    validate_result_lines(suite, result_lines)
    canonical = canonical_json_bytes(result_receipt(suite))
    environment_bytes = canonical_json_bytes(
        environment_receipt(
            suite,
            mode,
            logical_command,
            environment_lines,
            completed.stdout,
            completed.stderr,
        )
    )
    print(
        f"PASS evidence={suite.evidence_id} mode={mode} "
        f"positive={suite.summary['positive_comparisons']} "
        f"negative={len(suite.negative_controls)}",
        flush=True,
    )
    return canonical, environment_bytes


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


def receipt_path(suite: Suite, mode: str) -> str:
    return suite.normal_receipt if mode == "normal" else suite.optimized_receipt


def environment_path(suite: Suite, mode: str) -> str:
    return suite.normal_environment if mode == "normal" else suite.optimized_environment


def verify_existing_receipt(root: Path, suite: Suite, mode: str) -> bytes:
    relative = receipt_path(suite, mode)
    path = root / relative
    try:
        observed = path.read_bytes()
    except OSError as exc:
        raise VerificationError(f"cannot read canonical receipt {relative}: {exc}") from exc
    expected = canonical_json_bytes(result_receipt(suite))
    if observed != expected:
        raise VerificationError(f"canonical receipt content drift: {relative}")
    return observed


def compare_existing(root: Path) -> None:
    for suite in SUITES:
        normal = verify_existing_receipt(root, suite, "normal")
        optimized = verify_existing_receipt(root, suite, "optimized")
        if normal != optimized:
            raise VerificationError(
                f"normal/optimized canonical receipt mismatch: {suite.evidence_id}"
            )
        print(
            f"PASS compare evidence={suite.evidence_id} sha256={sha256_bytes(normal)}",
            flush=True,
        )


def execute(root: Path, mode: str, timeout_seconds: int) -> None:
    modes = ("normal", "optimized") if mode == "both" else (mode,)
    pending: list[tuple[Path, bytes]] = []
    results: dict[tuple[str, str], bytes] = {}
    for suite in SUITES:
        for current_mode in modes:
            canonical, environment = run_mode(root, suite, current_mode, timeout_seconds)
            results[(suite.evidence_id, current_mode)] = canonical
            pending.append((root / receipt_path(suite, current_mode), canonical))
            pending.append((root / environment_path(suite, current_mode), environment))

        if mode == "both":
            normal = results[(suite.evidence_id, "normal")]
            optimized = results[(suite.evidence_id, "optimized")]
            if normal != optimized:
                raise VerificationError(
                    f"normal/optimized canonical output mismatch: {suite.evidence_id}"
                )
        elif mode == "optimized":
            normal = verify_existing_receipt(root, suite, "normal")
            if normal != results[(suite.evidence_id, "optimized")]:
                raise VerificationError(
                    f"optimized result differs from existing normal receipt: {suite.evidence_id}"
                )

    for path, data in pending:
        atomic_write(path, data)

    if mode in {"both", "optimized"}:
        compare_existing(root)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument(
        "--mode",
        choices=("both", "normal", "optimized"),
        default="both",
        help="checker modes to execute; default runs and compares both",
    )
    parser.add_argument(
        "--compare-only",
        action="store_true",
        help="validate and compare existing canonical receipts without execution",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=900,
        help="per-checker subprocess timeout",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.timeout_seconds <= 0:
            raise VerificationError("timeout must be positive")
        root = args.root.resolve(strict=True)
        verify_frozen_inputs(root)
        if args.compare_only:
            compare_existing(root)
        else:
            execute(root, args.mode, args.timeout_seconds)
        total_positive = sum(suite.summary["positive_comparisons"] for suite in SUITES)
        total_negative = sum(len(suite.negative_controls) for suite in SUITES)
        print(
            f"PASS verification total_positive={total_positive} "
            f"total_negative_controls={total_negative}",
            flush=True,
        )
        return 0
    except (VerificationError, OSError, ValueError) as exc:
        print(f"FAIL verification: {exc}", file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
