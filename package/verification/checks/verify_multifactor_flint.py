#!/usr/bin/env python3
"""Independent exact FLINT checks for the multifactor Pluecker identity.

This research-stage backend uses ``fmpz_mpoly`` and fraction-free Bareiss
determinants.  It intentionally does not import the SymPy implementation.

For deleted source columns I of size k-1, the convention is

    (-1)^sum(I) det(Dm without I) = epsilon(d) Delta det(K_I),

where K has rows (0,...,A_b,...,0,-A_k), and Delta is the product of all
pairwise Sylvester resultants in ascending-coefficient convention.
"""

from __future__ import annotations

import argparse
import itertools
import math
import platform
from dataclasses import dataclass
from typing import Sequence

import flint
from flint import Ordering, fmpz_mpoly_ctx


@dataclass(frozen=True)
class Data:
    degrees: tuple[int, ...]
    context: object
    blocks: tuple[tuple[object, ...], ...]
    differential: tuple[tuple[object, ...], ...]
    kernel: tuple[tuple[object, ...], ...]
    resultants: tuple[object, ...]
    collision_product: object


def zero(context):
    return context.from_dict({})


def one(context):
    return context.from_dict({(0,) * context.nvars(): 1})


def bareiss_det(matrix: Sequence[Sequence[object]]):
    """Fraction-free determinant over an fmpz_mpoly context."""
    work = [list(row) for row in matrix]
    size = len(work)
    if size == 0:
        raise ValueError("empty determinant is not needed by this verifier")
    context = work[0][0].context()
    previous = one(context)
    sign = 1
    for pivot in range(size - 1):
        if not work[pivot][pivot]:
            replacement = next(
                (row for row in range(pivot + 1, size) if work[row][pivot]),
                None,
            )
            if replacement is None:
                return zero(context)
            work[pivot], work[replacement] = work[replacement], work[pivot]
            sign = -sign
        for row in range(pivot + 1, size):
            for column in range(pivot + 1, size):
                numerator = (
                    work[pivot][pivot] * work[row][column]
                    - work[row][pivot] * work[pivot][column]
                )
                work[row][column] = numerator // previous
        previous = work[pivot][pivot]
    determinant = work[-1][-1]
    return determinant if sign == 1 else -determinant


def convolution(context, factors: Sequence[Sequence[object]]) -> tuple[object, ...]:
    coefficients = [one(context)]
    for factor in factors:
        next_coefficients = [zero(context) for _ in range(len(coefficients) + len(factor) - 1)]
        for left_index, left in enumerate(coefficients):
            for right_index, right in enumerate(factor):
                next_coefficients[left_index + right_index] += left * right
        coefficients = next_coefficients
    return tuple(coefficients)


def sylvester_resultant(context, left: Sequence[object], right: Sequence[object]):
    left_degree = len(left) - 1
    right_degree = len(right) - 1
    size = left_degree + right_degree
    matrix = [[zero(context) for _ in range(size)] for _ in range(size)]
    for shift in range(right_degree):
        for index, coefficient in enumerate(left):
            matrix[shift][shift + index] = coefficient
    for shift in range(left_degree):
        for index, coefficient in enumerate(right):
            matrix[right_degree + shift][shift + index] = coefficient
    return bareiss_det(matrix)


def build_data(degrees: Sequence[int]) -> Data:
    degrees = tuple(degrees)
    if len(degrees) < 2 or any(degree < 1 for degree in degrees):
        raise ValueError("need at least two positive degrees")
    names = tuple(
        f"a{block}_{coefficient}"
        for block, degree in enumerate(degrees)
        for coefficient in range(degree + 1)
    )
    context = fmpz_mpoly_ctx.get(names, Ordering.lex)
    generators = context.gens()
    blocks = []
    offset = 0
    for degree in degrees:
        blocks.append(tuple(generators[offset : offset + degree + 1]))
        offset += degree + 1
    blocks = tuple(blocks)

    row_count = sum(degrees) + 1
    columns = []
    for omitted, block in enumerate(blocks):
        complement = convolution(
            context, [other for index, other in enumerate(blocks) if index != omitted]
        )
        for coefficient_index in range(len(block)):
            column = [zero(context) for _ in range(row_count)]
            for degree_index, value in enumerate(complement):
                column[coefficient_index + degree_index] = value
            columns.append(column)
    differential = tuple(
        tuple(columns[column][row] for column in range(len(columns)))
        for row in range(row_count)
    )

    offsets = []
    offset = 0
    for block in blocks:
        offsets.append(offset)
        offset += len(block)
    kernel_rows = []
    for basis in range(len(blocks) - 1):
        row = [zero(context) for _ in range(len(names))]
        for index, value in enumerate(blocks[basis]):
            row[offsets[basis] + index] = value
        for index, value in enumerate(blocks[-1]):
            row[offsets[-1] + index] = -value
        kernel_rows.append(tuple(row))

    resultants = tuple(
        sylvester_resultant(context, blocks[left], blocks[right])
        for left, right in itertools.combinations(range(len(blocks)), 2)
    )
    collision_product = one(context)
    for resultant in resultants:
        collision_product *= resultant

    return Data(
        degrees=degrees,
        context=context,
        blocks=blocks,
        differential=differential,
        kernel=tuple(kernel_rows),
        resultants=resultants,
        collision_product=collision_product,
    )


def orientation(degrees: Sequence[int]) -> int:
    factor_count = len(degrees)
    exponent = sum(
        degrees[left] * (degrees[right] + 1)
        for left in range(factor_count)
        for right in range(left + 1, factor_count)
    )
    exponent += factor_count * (factor_count + 1) // 2 + 1
    return -1 if exponent % 2 else 1


def integer_bareiss_det(matrix: Sequence[Sequence[int]]) -> int:
    """Small exact integer determinant, independent of symbolic matrices."""
    work = [list(row) for row in matrix]
    size = len(work)
    previous = 1
    sign = 1
    for pivot in range(size - 1):
        if work[pivot][pivot] == 0:
            replacement = next(
                (row for row in range(pivot + 1, size) if work[row][pivot]),
                None,
            )
            if replacement is None:
                return 0
            work[pivot], work[replacement] = work[replacement], work[pivot]
            sign = -sign
        for row in range(pivot + 1, size):
            for column in range(pivot + 1, size):
                numerator = (
                    work[pivot][pivot] * work[row][column]
                    - work[row][pivot] * work[pivot][column]
                )
                work[row][column] = numerator // previous
        previous = work[pivot][pivot]
    return sign * work[-1][-1]


def character_row(degrees: Sequence[int], edge: tuple[int, int]) -> list[int]:
    """Coordinates of a resultant character after eliminating u_last."""
    left, right = edge
    factor_count = len(degrees)
    row = [0] * (factor_count - 1)
    for vertex, weight in ((left, degrees[right]), (right, degrees[left])):
        if vertex < factor_count - 1:
            row[vertex] += weight
        else:
            for column in range(factor_count - 1):
                row[column] -= weight
    return row


def verify_multiborder(
    degrees: Sequence[int], normalizer_edges: Sequence[tuple[int, int]]
) -> None:
    """Check the square Jacobian bordered by pairwise resultants."""
    data = build_data(degrees)
    factor_count = len(degrees)
    if len(normalizer_edges) != factor_count - 1:
        raise ValueError("need one normalizer edge per torus dimension")
    resultant_by_edge = dict(
        zip(itertools.combinations(range(factor_count), 2), data.resultants)
    )
    normalizers = [resultant_by_edge[edge] for edge in normalizer_edges]
    source_dimension = sum(len(block) for block in data.blocks)
    gradients = [
        [normalizer.derivative(variable) for variable in range(source_dimension)]
        for normalizer in normalizers
    ]
    observed = bareiss_det([list(row) for row in data.differential] + gradients)

    weight_matrix = [character_row(degrees, edge) for edge in normalizer_edges]
    weight_det = integer_bareiss_det(weight_matrix)
    target_dimension = sum(degrees) + 1
    torus_dimension = factor_count - 1
    exponent = (
        target_dimension * torus_dimension
        + torus_dimension * (torus_dimension - 1) // 2
    )
    prefactor = (-1 if exponent % 2 else 1) * orientation(degrees) * weight_det
    expected = prefactor * data.collision_product
    for normalizer in normalizers:
        expected *= normalizer
    if observed != expected:
        raise AssertionError(
            f"FLINT multiborder failed for degrees={tuple(degrees)}, "
            f"edges={tuple(normalizer_edges)}"
        )
    print(
        f"PASS FLINT multiborder degrees={tuple(degrees)} "
        f"edges={tuple(normalizer_edges)} detW={weight_det:+d}"
    )


def identity_holds(
    data: Data,
    *,
    differential: Sequence[Sequence[object]] | None = None,
    kernel: Sequence[Sequence[object]] | None = None,
    collision_product=None,
    expected_orientation: int | None = None,
) -> bool:
    differential = data.differential if differential is None else differential
    kernel = data.kernel if kernel is None else kernel
    collision_product = (
        data.collision_product if collision_product is None else collision_product
    )
    expected_orientation = (
        orientation(data.degrees)
        if expected_orientation is None
        else expected_orientation
    )
    source_dimension = sum(len(block) for block in data.blocks)
    deleted_size = len(data.degrees) - 1
    for deleted in itertools.combinations(range(source_dimension), deleted_size):
        deleted_set = set(deleted)
        kept = [column for column in range(source_dimension) if column not in deleted_set]
        source_minor = bareiss_det(
            [[row[column] for column in kept] for row in differential]
        )
        if sum(deleted) % 2:
            source_minor = -source_minor
        kernel_minor = bareiss_det(
            [[row[column] for column in deleted] for row in kernel]
        )
        if source_minor != expected_orientation * collision_product * kernel_minor:
            return False
    return True


def verify_case(degrees: Sequence[int]) -> int:
    data = build_data(degrees)
    if not identity_holds(data):
        raise AssertionError(f"FLINT identity failed for degrees={tuple(degrees)}")
    coordinate_count = math.comb(
        sum(degree + 1 for degree in degrees), len(degrees) - 1
    )
    print(
        f"PASS FLINT degrees={tuple(degrees)} coordinates={coordinate_count} "
        f"orientation={orientation(degrees):+d}"
    )
    return coordinate_count


def negative_controls() -> None:
    data = build_data((1, 1, 1))
    flipped_kernel = [list(row) for row in data.kernel]
    flipped_kernel[0] = [-value for value in flipped_kernel[0]]
    perturbed_differential = [list(row) for row in data.differential]
    perturbed_differential[0][0] += one(data.context)
    controls = (
        (
            "NC1 missing pairwise resultant",
            identity_holds(data, collision_product=data.resultants[1] * data.resultants[2]),
        ),
        (
            "NC2 reversed torus basis vector",
            identity_holds(data, kernel=flipped_kernel),
        ),
        (
            "NC3 wrong orientation",
            identity_holds(data, expected_orientation=-orientation(data.degrees)),
        ),
        (
            "NC4 perturbed differential",
            identity_holds(data, differential=perturbed_differential),
        ),
    )
    for label, mutation_survived in controls:
        if mutation_survived:
            raise AssertionError(f"negative control survived: {label}")
        print(f"PASS FLINT {label} detected")


def parse_degrees(text: str) -> tuple[int, ...]:
    return tuple(int(part) for part in text.split(",") if part)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "degrees",
        nargs="*",
        default=["1,1,1", "1,1,2", "1,2,1", "2,1,1", "1,1,1,1"],
    )
    parser.add_argument("--skip-negative-controls", action="store_true")
    args = parser.parse_args()
    print("multifactor Pluecker exact FLINT verification")
    print(f"python={platform.python_version()} python-flint={flint.__version__}")
    total = 0
    for text in args.degrees:
        total += verify_case(parse_degrees(text))
    verify_multiborder((1, 1, 1), ((0, 1), (1, 2)))
    verify_multiborder((1, 1, 2), ((0, 1), (1, 2)))
    if not args.skip_negative_controls:
        negative_controls()
    print(f"PASS total symbolic Pluecker coordinates={total}")


if __name__ == "__main__":
    main()
