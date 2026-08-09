#!/usr/bin/env python3
"""Exploratory exact checks for multifactor binary-form multiplication.

This is a research-stage program, not a release verifier.  It constructs the
multiplication differential, pairwise Sylvester resultants, and the torus
kernel matrix by separate formulas and compares every Pluecker coordinate.

Coordinate convention:

    A_h = sum_{i=0}^{d_h} a_{h,i} X^(d_h-i) Y^i.

For a deleted set I of t=k-1 source columns, the signed maximal minor is

    p_I = (-1)^sum(I) det(M on the complementary columns).

For k=2 this is exactly the cofactor convention in the parent candidate.
"""

from __future__ import annotations

import argparse
import itertools
from dataclasses import dataclass
from typing import Iterable, Sequence

import sympy as sp


@dataclass(frozen=True)
class FactorisationData:
    degrees: tuple[int, ...]
    blocks: tuple[tuple[sp.Symbol, ...], ...]
    variables: tuple[sp.Symbol, ...]
    product_coefficients: tuple[sp.Expr, ...]
    differential: sp.Matrix
    torus_kernel: sp.Matrix
    pairwise_resultants: tuple[sp.Expr, ...]
    collision_product: sp.Expr


def sylvester_resultant(left: Sequence[sp.Expr], right: Sequence[sp.Expr]) -> sp.Expr:
    """Return the parent bundle's ascending-coefficient Sylvester resultant."""
    r = len(left) - 1
    s = len(right) - 1
    sylvester = sp.zeros(r + s, r + s)
    for shift in range(s):
        for index, coefficient in enumerate(left):
            sylvester[shift, shift + index] = coefficient
    for shift in range(r):
        for index, coefficient in enumerate(right):
            sylvester[s + shift, shift + index] = coefficient
    return sp.expand(sylvester.det(method="berkowitz"))


def convolution(factors: Sequence[Sequence[sp.Expr]]) -> tuple[sp.Expr, ...]:
    coefficients: tuple[sp.Expr, ...] = (sp.Integer(1),)
    for factor in factors:
        next_coefficients = [sp.Integer(0)] * (len(coefficients) + len(factor) - 1)
        for i, left in enumerate(coefficients):
            for j, right in enumerate(factor):
                next_coefficients[i + j] += left * right
        coefficients = tuple(map(sp.expand, next_coefficients))
    return coefficients


def other_factor_product(
    blocks: Sequence[Sequence[sp.Expr]], omitted: int
) -> tuple[sp.Expr, ...]:
    return convolution([block for index, block in enumerate(blocks) if index != omitted])


def build_data(degrees: Sequence[int]) -> FactorisationData:
    degrees = tuple(degrees)
    if len(degrees) < 2 or any(degree < 1 for degree in degrees):
        raise ValueError("need at least two positive degrees")

    blocks = tuple(
        tuple(sp.symbols(f"a{block}_0:{degree + 1}"))
        for block, degree in enumerate(degrees)
    )
    variables = tuple(variable for block in blocks for variable in block)
    product_coefficients = convolution(blocks)

    # Construct Dm directly.  The derivative with respect to a coefficient in
    # block h is the coefficient vector of the product of all other factors,
    # shifted by that coefficient's index.
    row_count = sum(degrees) + 1
    columns: list[list[sp.Expr]] = []
    for block_index, block in enumerate(blocks):
        complement = other_factor_product(blocks, block_index)
        for coefficient_index in range(len(block)):
            column = [sp.Integer(0)] * row_count
            for degree_index, value in enumerate(complement):
                column[coefficient_index + degree_index] = value
            columns.append(column)
    differential = sp.Matrix(row_count, len(variables), lambda i, j: columns[j][i])

    # Basis e_b-e_last for the product-one scaling torus.
    torus_rows: list[list[sp.Expr]] = []
    offsets = []
    offset = 0
    for block in blocks:
        offsets.append(offset)
        offset += len(block)
    for basis_index in range(len(blocks) - 1):
        row = [sp.Integer(0)] * len(variables)
        own_offset = offsets[basis_index]
        last_offset = offsets[-1]
        for index, value in enumerate(blocks[basis_index]):
            row[own_offset + index] = value
        for index, value in enumerate(blocks[-1]):
            row[last_offset + index] = -value
        torus_rows.append(row)
    torus_kernel = sp.Matrix(torus_rows)

    pairwise = tuple(
        sylvester_resultant(blocks[left], blocks[right])
        for left, right in itertools.combinations(range(len(blocks)), 2)
    )
    collision_product = sp.prod(pairwise)

    return FactorisationData(
        degrees=degrees,
        blocks=blocks,
        variables=variables,
        product_coefficients=product_coefficients,
        differential=differential,
        torus_kernel=torus_kernel,
        pairwise_resultants=pairwise,
        collision_product=sp.expand(collision_product),
    )


def signed_maximal_minor(matrix: sp.Matrix, deleted: Sequence[int]) -> sp.Expr:
    deleted_set = set(deleted)
    kept = [column for column in range(matrix.cols) if column not in deleted_set]
    return (-1) ** sum(deleted) * matrix[:, kept].det(method="berkowitz")


def kernel_minor(kernel: sp.Matrix, deleted: Sequence[int]) -> sp.Expr:
    return kernel[:, list(deleted)].det(method="berkowitz")


def exact_zero(expression: sp.Expr) -> bool:
    expanded = sp.expand(expression)
    if expanded == 0:
        return True
    return sp.Poly(expanded).is_zero


def candidate_orientation_sign(degrees: Sequence[int]) -> int:
    """Orientation predicted by the recursive determinant-line lemma."""
    factor_count = len(degrees)
    exponent = sum(
        degrees[left] * (degrees[right] + 1)
        for left in range(factor_count)
        for right in range(left + 1, factor_count)
    )
    exponent += factor_count * (factor_count + 1) // 2 + 1
    return (-1) ** exponent


def identity_holds(
    data: FactorisationData,
    *,
    differential: sp.Matrix | None = None,
    kernel: sp.Matrix | None = None,
    collision_product: sp.Expr | None = None,
    orientation: int | None = None,
) -> bool:
    """Compare every Pluecker coordinate for a supplied or mutated encoding."""
    differential = data.differential if differential is None else differential
    kernel = data.torus_kernel if kernel is None else kernel
    collision_product = (
        data.collision_product if collision_product is None else collision_product
    )
    orientation = (
        candidate_orientation_sign(data.degrees) if orientation is None else orientation
    )
    deleted_size = len(data.degrees) - 1
    for deleted in itertools.combinations(range(len(data.variables)), deleted_size):
        left = signed_maximal_minor(differential, deleted)
        right = orientation * collision_product * kernel_minor(kernel, deleted)
        if not exact_zero(left - right):
            return False
    return True


def negative_controls() -> None:
    """Confirm that five structural mutations are detected in the (1,1,1) case."""
    data = build_data((1, 1, 1))
    expected_orientation = candidate_orientation_sign(data.degrees)

    missing_resultant = sp.prod(data.pairwise_resultants[1:])
    squared_collision_product = data.collision_product**2

    flipped_kernel = data.torus_kernel.copy()
    for column in range(flipped_kernel.cols):
        flipped_kernel[0, column] = -flipped_kernel[0, column]

    perturbed_differential = data.differential.copy()
    perturbed_differential[0, 0] += 1

    controls = (
        (
            "NC1 missing pairwise resultant",
            identity_holds(data, collision_product=missing_resultant),
        ),
        (
            "NC2 squared collision product",
            identity_holds(data, collision_product=squared_collision_product),
        ),
        (
            "NC3 reversed torus basis vector",
            identity_holds(data, kernel=flipped_kernel),
        ),
        (
            "NC4 omitted recursive orientation constant",
            identity_holds(data, orientation=-expected_orientation),
        ),
        (
            "NC5 perturbed convolution differential",
            identity_holds(data, differential=perturbed_differential),
        ),
    )
    for label, mutation_survived in controls:
        if mutation_survived:
            raise AssertionError(f"negative control survived: {label}")
        print(f"PASS {label} detected")


def verify_pluecker_identity(degrees: Sequence[int], verbose: bool = False) -> int:
    data = build_data(degrees)
    deleted_size = len(data.degrees) - 1
    all_deleted = list(itertools.combinations(range(len(data.variables)), deleted_size))
    inferred_sign: int | None = None
    checked = 0

    for deleted in all_deleted:
        left = sp.expand(signed_maximal_minor(data.differential, deleted))
        kernel_coordinate = sp.expand(kernel_minor(data.torus_kernel, deleted))
        if exact_zero(kernel_coordinate):
            if not exact_zero(left):
                raise AssertionError(
                    f"forbidden nonzero Pluecker coordinate for degrees={tuple(degrees)}, I={deleted}"
                )
            checked += 1
            continue

        positive_rhs = sp.expand(data.collision_product * kernel_coordinate)
        if exact_zero(left - positive_rhs):
            sign = 1
        elif exact_zero(left + positive_rhs):
            sign = -1
        else:
            difference = sp.factor(left - positive_rhs)
            raise AssertionError(
                f"non-sign discrepancy for degrees={tuple(degrees)}, I={deleted}: {difference}"
            )

        if inferred_sign is None:
            inferred_sign = sign
        elif sign != inferred_sign:
            raise AssertionError(
                f"I-dependent sign for degrees={tuple(degrees)}: "
                f"expected {inferred_sign:+d}, got {sign:+d} at I={deleted}"
            )
        checked += 1
        if verbose:
            print(f"  I={deleted}: sign={sign:+d}")

    if inferred_sign is None:
        raise AssertionError(f"all kernel coordinates vanished for degrees={tuple(degrees)}")

    expected = candidate_orientation_sign(degrees)
    if inferred_sign != expected:
        raise AssertionError(
            f"orientation formula mismatch for degrees={tuple(degrees)}: "
            f"expected {expected:+d}, observed {inferred_sign:+d}"
        )

    print(
        f"PASS degrees={tuple(degrees)} factors={len(degrees)} "
        f"coordinates={checked} orientation={inferred_sign:+d}"
    )
    return inferred_sign


def parse_degree_vector(text: str) -> tuple[int, ...]:
    return tuple(int(part) for part in text.split(",") if part)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "degrees",
        nargs="*",
        default=["1,1", "1,2", "1,1,1", "1,1,2", "1,2,1", "2,1,1", "1,1,1,1"],
        help="comma-separated degree vectors",
    )
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--skip-negative-controls", action="store_true")
    args = parser.parse_args()
    for text in args.degrees:
        verify_pluecker_identity(parse_degree_vector(text), verbose=args.verbose)
    if not args.skip_negative_controls:
        negative_controls()


if __name__ == "__main__":
    main()
