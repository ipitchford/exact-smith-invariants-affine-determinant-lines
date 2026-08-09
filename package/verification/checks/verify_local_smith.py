#!/usr/bin/env python3
"""Exact regression checks for the Stage-4 local Smith theorem.

This program is producer-side falsification evidence.  It checks finite
instances of the proved integer-lattice theorem; it is not a proof,
independent reproduction, or novelty evidence.
"""

from __future__ import annotations

import itertools
import math
import platform
from functools import reduce
from typing import Iterable, Sequence

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


Edge = tuple[int, int]


def fail(label: str, *payload: object) -> None:
    raise RuntimeError((label, *payload))


def integer_gcd(values: Iterable[int]) -> int:
    return reduce(math.gcd, (abs(int(value)) for value in values), 0)


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return math.inf
    result = 0
    value = abs(value)
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def complete_edges(vertex_count: int) -> tuple[Edge, ...]:
    return tuple(itertools.combinations(range(vertex_count), 2))


def character_row(edge: Edge, degrees: Sequence[int]) -> list[int]:
    left, right = edge
    row = [0] * (len(degrees) - 1)
    for vertex, weight in ((left, degrees[right]), (right, degrees[left])):
        if vertex < len(degrees) - 1:
            row[vertex] += weight
        else:
            for column in range(len(degrees) - 1):
                row[column] -= weight
    return row


def character_matrix(
    degrees: Sequence[int], edges: Sequence[Edge] | None = None
) -> sp.Matrix:
    chosen = complete_edges(len(degrees)) if edges is None else tuple(edges)
    return sp.Matrix([character_row(edge, degrees) for edge in chosen])


def smith_diagonal(degrees: Sequence[int]) -> tuple[int, ...]:
    matrix = character_matrix(degrees)
    smith = smith_normal_form(matrix, domain=sp.ZZ)
    return tuple(
        abs(int(smith[index, index]))
        for index in range(len(degrees) - 1)
    )


def local_exponent(degrees: Sequence[int], prime: int, pivot: int) -> int:
    if degrees[pivot] % prime == 0:
        fail("nonunit pivot", degrees, prime, pivot)
    diagonal = degrees[pivot] - sum(
        degree for index, degree in enumerate(degrees) if index != pivot
    )
    candidates: list[int] = [valuation(diagonal, prime)]
    outside = [index for index in range(len(degrees)) if index != pivot]
    for left, right in itertools.combinations(outside, 2):
        candidates.append(
            valuation(2, prime)
            + valuation(degrees[left], prime)
            + valuation(degrees[right], prime)
        )
    return int(min(candidates))


def global_index_formula(degrees: Sequence[int]) -> int:
    odd_count = sum(degree % 2 for degree in degrees)
    if odd_count % 2 == 1:
        eta_two = 0
    elif odd_count >= 4:
        eta_two = 1
    elif odd_count == 2:
        odd = [index for index, degree in enumerate(degrees) if degree % 2]
        left, right = odd
        outside = [
            degree
            for index, degree in enumerate(degrees)
            if index not in (left, right)
        ]
        outside_gcd = integer_gcd(outside)
        diagonal = degrees[left] - degrees[right] - sum(outside)
        eta_two = min(valuation(diagonal, 2), 1 + valuation(outside_gcd, 2))
    else:
        fail("primitive vector has no odd entry", degrees)

    odd_product = 1
    for left, right in itertools.combinations(range(len(degrees)), 2):
        outside = [
            degree
            for index, degree in enumerate(degrees)
            if index not in (left, right)
        ]
        pair_gcd = math.gcd(abs(degrees[left] - degrees[right]), integer_gcd(outside))
        while pair_gcd % 2 == 0:
            pair_gcd //= 2
        odd_product *= pair_gcd
    return (2**eta_two) * odd_product


def prufer_tree(sequence: Sequence[int], vertex_count: int) -> tuple[Edge, ...]:
    valences = [1] * vertex_count
    for vertex in sequence:
        valences[vertex] += 1
    edges: list[Edge] = []
    for vertex in sequence:
        leaf = next(index for index, valence in enumerate(valences) if valence == 1)
        edges.append(tuple(sorted((leaf, vertex))))
        valences[leaf] -= 1
        valences[vertex] -= 1
    remaining = [index for index, valence in enumerate(valences) if valence == 1]
    edges.append(tuple(sorted(remaining)))
    return tuple(edges)


def tree_gcd(degrees: Sequence[int]) -> int:
    vertex_count = len(degrees)
    values = []
    for sequence in itertools.product(
        range(vertex_count), repeat=max(0, vertex_count - 2)
    ):
        edges = (
            prufer_tree(sequence, vertex_count)
            if vertex_count > 2
            else ((0, 1),)
        )
        values.append(abs(int(character_matrix(degrees, edges).det(method="domain-ge"))))
    return integer_gcd(values)


def primes_for(degrees: Sequence[int], index: int) -> tuple[int, ...]:
    support = {2}
    for value in (*degrees, index):
        support.update(int(prime) for prime in sp.factorint(value))
    support.update(int(prime) for prime in sp.primerange(2, max(degrees) + 2))
    return tuple(sorted(support))


def primitive_vectors(vertex_count: int, bound: int) -> Iterable[tuple[int, ...]]:
    for degrees in itertools.product(range(1, bound + 1), repeat=vertex_count):
        if integer_gcd(degrees) == 1:
            yield degrees


def verify_smith_local_and_global() -> int:
    checks = 0
    bounds = ((3, 10), (4, 6), (5, 4), (6, 3))
    for vertex_count, bound in bounds:
        for degrees in primitive_vectors(vertex_count, bound):
            diagonal = smith_diagonal(degrees)
            if diagonal[:-1] != (1,) * (vertex_count - 2):
                fail("primitive cyclicity", degrees, diagonal)
            observed = diagonal[-1]
            predicted = global_index_formula(degrees)
            if observed != predicted:
                fail("global formula", degrees, observed, predicted)
            checks += 2

            for prime in primes_for(degrees, observed):
                expected = valuation(observed, prime)
                pivot_values = []
                for pivot, degree in enumerate(degrees):
                    if degree % prime:
                        pivot_values.append(local_exponent(degrees, prime, pivot))
                if not pivot_values or any(value != expected for value in pivot_values):
                    fail("local formula", degrees, prime, expected, pivot_values)
                checks += len(pivot_values)
    print(f"PASS local/global Smith checks={checks}")
    return checks


def verify_tree_gcd() -> int:
    checks = 0
    bounds = ((3, 9), (4, 5), (5, 3))
    for vertex_count, bound in bounds:
        for degrees in primitive_vectors(vertex_count, bound):
            observed = smith_diagonal(degrees)[-1]
            predicted = tree_gcd(degrees)
            if observed != predicted:
                fail("tree gcd", degrees, observed, predicted)
            checks += 1
    print(f"PASS tree-gcd checks={checks}")
    return checks


def verify_displayed_examples() -> int:
    examples = {
        (1, 1, 1): (1, 1),
        (1, 1, 3): (1, 3),
        (1, 1, 9): (1, 9),
        (1, 1, 4): (1, 4),
        (1, 5, 4): (1, 8),
        (1, 2, 2): (1, 1),
        (1, 1, 1, 1): (1, 1, 2),
        (2, 2, 18): (2, 18),
    }
    for degrees, expected in examples.items():
        observed = smith_diagonal(degrees)
        if observed != expected:
            fail("displayed example", degrees, observed, expected)
    print(f"PASS displayed examples={len(examples)}")
    return len(examples)


def verify_negative_controls() -> int:
    detected = 0

    # NC1: deleting the coefficient 2 misses the four-odd obstruction.
    if global_index_formula((1, 1, 1, 1)) == 1:
        fail("NC1 not detected")
    detected += 1
    print("PASS NC1 factor-two omission detected")

    # NC2: support-only arithmetic misses higher odd valuation.
    if smith_diagonal((1, 1, 9))[-1] == 3:
        fail("NC2 not detected")
    detected += 1
    print("PASS NC2 odd support substituted for valuation detected")

    # NC3: support-only arithmetic misses higher 2-adic valuation.
    if smith_diagonal((1, 5, 4))[-1] == 2:
        fail("NC3 not detected")
    detected += 1
    print("PASS NC3 two-adic support substituted for valuation detected")

    # NC4: full-list saturation need not be attained by an edge basis.
    matrix = character_matrix((1, 2, 2))
    minors = {
        abs(int(matrix[list(rows), :].det(method="domain-ge")))
        for rows in itertools.combinations(range(matrix.rows), 2)
    }
    if 1 in minors or integer_gcd(minors) != 1:
        fail("NC4 not detected", minors)
    detected += 1
    print("PASS NC4 full-list gcd replaced by edge basis detected")

    # NC5: omitting common content gives the wrong nonprimitive Smith form.
    if smith_diagonal((2, 2, 18)) == (1, 9):
        fail("NC5 not detected")
    detected += 1
    print("PASS NC5 nonprimitive content omitted detected")

    print(f"PASS deliberate negative controls detected={detected}")
    return detected


def main() -> None:
    print("local Smith exact verification")
    print(f"python={platform.python_version()} sympy={sp.__version__}")
    positive = 0
    positive += verify_smith_local_and_global()
    positive += verify_tree_gcd()
    positive += verify_displayed_examples()
    negative = verify_negative_controls()
    print(f"PASS summary positive={positive} negative_controls={negative}")


if __name__ == "__main__":
    main()
