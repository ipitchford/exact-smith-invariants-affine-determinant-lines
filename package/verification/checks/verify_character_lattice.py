#!/usr/bin/env python3
"""Exact research checks for the resultant-character lattice.

For positive degrees d_i, the edge ij has torus character

    chi_ij(u) = d_j u_i + d_i u_j,  sum_i u_i = 0.

Coordinates use u_0,...,u_{k-2}, with u_{k-1}=-sum_{b<k-1} u_b.
The program checks tree and general maximal-minor formulas, Smith-form
structure, bad-prime criteria, and deliberate negative controls.
"""

from __future__ import annotations

import argparse
import itertools
import math
import platform
from fractions import Fraction
from functools import reduce
from typing import Iterable, Sequence

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


Edge = tuple[int, int]


def complete_edges(vertex_count: int) -> tuple[Edge, ...]:
    return tuple(itertools.combinations(range(vertex_count), 2))


def character_row(edge: Edge, degrees: Sequence[int]) -> list[int]:
    left, right = edge
    vertex_count = len(degrees)
    row = [0] * (vertex_count - 1)
    for vertex, weight in ((left, degrees[right]), (right, degrees[left])):
        if vertex < vertex_count - 1:
            row[vertex] += weight
        else:
            for column in range(vertex_count - 1):
                row[column] -= weight
    return row


def character_matrix(degrees: Sequence[int], edges: Sequence[Edge] | None = None) -> sp.Matrix:
    edges = complete_edges(len(degrees)) if edges is None else tuple(edges)
    return sp.Matrix([character_row(edge, degrees) for edge in edges])


def prufer_tree(sequence: Sequence[int], vertex_count: int) -> tuple[Edge, ...]:
    degrees = [1] * vertex_count
    for vertex in sequence:
        degrees[vertex] += 1
    edges: list[Edge] = []
    for vertex in sequence:
        leaf = next(index for index, degree in enumerate(degrees) if degree == 1)
        edges.append(tuple(sorted((leaf, vertex))))
        degrees[leaf] -= 1
        degrees[vertex] -= 1
    remaining = [index for index, degree in enumerate(degrees) if degree == 1]
    edges.append(tuple(sorted(remaining)))
    return tuple(edges)


def graph_components(vertex_count: int, edges: Sequence[Edge]) -> list[list[int]]:
    adjacency = [[] for _ in range(vertex_count)]
    for left, right in edges:
        adjacency[left].append(right)
        adjacency[right].append(left)
    components: list[list[int]] = []
    unseen = set(range(vertex_count))
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        stack = [root]
        component = []
        while stack:
            vertex = stack.pop()
            component.append(vertex)
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
        components.append(sorted(component))
    return components


def component_edges(component: Sequence[int], edges: Sequence[Edge]) -> list[Edge]:
    vertices = set(component)
    return [edge for edge in edges if edge[0] in vertices and edge[1] in vertices]


def bipartition(component: Sequence[int], edges: Sequence[Edge]) -> tuple[list[int], list[int]] | None:
    vertices = set(component)
    adjacency = {vertex: [] for vertex in component}
    for left, right in edges:
        if left in vertices and right in vertices:
            adjacency[left].append(right)
            adjacency[right].append(left)
    color: dict[int, int] = {}
    for root in component:
        if root in color:
            continue
        color[root] = 0
        stack = [root]
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[vertex]
                    stack.append(neighbor)
                elif color[neighbor] == color[vertex]:
                    return None
    return (
        [vertex for vertex in component if color[vertex] == 0],
        [vertex for vertex in component if color[vertex] == 1],
    )


def vertex_degrees(vertex_count: int, edges: Sequence[Edge]) -> list[int]:
    result = [0] * vertex_count
    for left, right in edges:
        result[left] += 1
        result[right] += 1
    return result


def predicted_maximal_minor(degrees: Sequence[int], edges: Sequence[Edge]) -> int:
    """Absolute determinant from the tree/odd-unicyclic component formula."""
    vertex_count = len(degrees)
    if len(edges) != vertex_count - 1:
        raise ValueError("a maximal edge minor needs k-1 edges")

    components = graph_components(vertex_count, edges)
    tree_components: list[tuple[list[int], tuple[list[int], list[int]]]] = []
    odd_unicyclic_count = 0

    for component in components:
        internal_edges = component_edges(component, edges)
        coloring = bipartition(component, internal_edges)
        if len(internal_edges) == len(component) - 1 and coloring is not None:
            tree_components.append((component, coloring))
        elif len(internal_edges) == len(component) and coloring is None:
            odd_unicyclic_count += 1
        else:
            return 0

    if len(tree_components) != 1 or odd_unicyclic_count != len(components) - 1:
        return 0

    _, (positive, negative) = tree_components[0]
    balance = sum(degrees[vertex] for vertex in positive) - sum(
        degrees[vertex] for vertex in negative
    )
    graph_degrees = vertex_degrees(vertex_count, edges)
    product = Fraction(2 ** odd_unicyclic_count * abs(balance), 1)
    for degree, valence in zip(degrees, graph_degrees):
        product *= Fraction(degree) ** (valence - 1)
    if product.denominator != 1:
        raise AssertionError((degrees, edges, product))
    return product.numerator


def tree_formula(degrees: Sequence[int], edges: Sequence[Edge]) -> int:
    coloring = bipartition(range(len(degrees)), edges)
    if coloring is None:
        raise ValueError("tree unexpectedly non-bipartite")
    positive, negative = coloring
    balance = abs(
        sum(degrees[vertex] for vertex in positive)
        - sum(degrees[vertex] for vertex in negative)
    )
    graph_degrees = vertex_degrees(len(degrees), edges)
    return balance * math.prod(
        degree ** (valence - 1)
        for degree, valence in zip(degrees, graph_degrees)
    )


def exact_smith_diagonal(matrix: sp.Matrix) -> tuple[int, ...]:
    smith = smith_normal_form(matrix, domain=sp.ZZ)
    return tuple(
        abs(int(smith[index, index]))
        for index in range(min(smith.rows, smith.cols))
        if smith[index, index]
    )


def integer_gcd(values: Iterable[int]) -> int:
    return reduce(math.gcd, (abs(value) for value in values), 0)


def primitive_index(degrees: Sequence[int]) -> int:
    common = integer_gcd(degrees)
    primitive = tuple(degree // common for degree in degrees)
    matrix = character_matrix(primitive)
    rank = len(degrees) - 1
    minors = (
        int(matrix[list(rows), :].det(method="domain-ge"))
        for rows in itertools.combinations(range(matrix.rows), rank)
    )
    return integer_gcd(minors)


def predicted_bad_primes(primitive_degrees: Sequence[int]) -> set[int]:
    # Generate candidates independently of the observed index.  For an odd
    # prime larger than every primitive degree, all k >= 3 residues are
    # nonzero, so the exceptional "exactly two equal residues" condition is
    # impossible.  The prime 2 is included separately.
    candidate_bound = max(2, max(primitive_degrees))
    candidates = set(sp.primerange(2, candidate_bound + 1))
    predicted = set()
    for prime in candidates:
        nonzero = [degree % prime for degree in primitive_degrees if degree % prime]
        if prime == 2:
            if len(nonzero) % 2 == 0:
                predicted.add(prime)
        elif len(nonzero) == 2 and nonzero[0] == nonzero[1]:
            predicted.add(prime)
    return predicted


def verify_tree_formulas(max_vertices: int, max_degree: int) -> int:
    checks = 0
    for vertex_count in range(2, max_vertices + 1):
        sequences = itertools.product(range(vertex_count), repeat=max(0, vertex_count - 2))
        for sequence in sequences:
            edges = prufer_tree(sequence, vertex_count) if vertex_count > 2 else ((0, 1),)
            for degrees in itertools.product(range(1, max_degree + 1), repeat=vertex_count):
                observed = abs(int(character_matrix(degrees, edges).det(method="domain-ge")))
                expected = tree_formula(degrees, edges)
                if observed != expected:
                    raise AssertionError(("tree", degrees, edges, observed, expected))
                checks += 1
    print(f"PASS tree determinant formula checks={checks}")
    return checks


def verify_general_minor_formulas(max_vertices: int, max_degree: int) -> int:
    checks = 0
    for vertex_count in range(2, max_vertices + 1):
        all_edges = complete_edges(vertex_count)
        for edges in itertools.combinations(all_edges, vertex_count - 1):
            for degrees in itertools.product(range(1, max_degree + 1), repeat=vertex_count):
                observed = abs(int(character_matrix(degrees, edges).det(method="domain-ge")))
                expected = predicted_maximal_minor(degrees, edges)
                if observed != expected:
                    raise AssertionError(("graph", degrees, edges, observed, expected))
                checks += 1

    # First case with two odd-unicyclic components plus one tree component.
    degrees = (1, 2, 3, 4, 5, 6, 7)
    edges = ((0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5))
    observed = abs(int(character_matrix(degrees, edges).det(method="domain-ge")))
    expected = predicted_maximal_minor(degrees, edges)
    if observed != expected:
        raise AssertionError(("two odd components", observed, expected))
    checks += 1

    print(f"PASS general maximal-minor graph formula checks={checks}")
    return checks


def verify_smith_structure(max_vertices: int, max_degree: int) -> int:
    checks = 0
    for vertex_count in range(3, max_vertices + 1):
        for degrees in itertools.product(range(1, max_degree + 1), repeat=vertex_count):
            common = integer_gcd(degrees)
            primitive = tuple(degree // common for degree in degrees)
            index = primitive_index(primitive)
            expected = (common,) * (vertex_count - 2) + (common * index,)
            observed = exact_smith_diagonal(character_matrix(degrees))
            if observed != expected:
                raise AssertionError(("smith", degrees, observed, expected))

            actual_primes = set(sp.factorint(index))
            if predicted_bad_primes(primitive) != actual_primes:
                raise AssertionError(
                    ("bad primes", degrees, predicted_bad_primes(primitive), actual_primes)
                )
            checks += 1
    print(f"PASS Smith structure and bad-prime checks={checks}")
    return checks


def negative_controls() -> None:
    degrees = (1, 2, 3, 4)
    tree = ((0, 1), (0, 2), (0, 3))
    observed_tree = abs(int(character_matrix(degrees, tree).det(method="domain-ge")))
    correct_tree = tree_formula(degrees, tree)
    if observed_tree != correct_tree:
        raise AssertionError("control fixture is invalid")

    triangle_and_isolate = ((0, 1), (1, 2), (0, 2))
    observed_cycle = abs(
        int(character_matrix(degrees, triangle_and_isolate).det(method="domain-ge"))
    )
    correct_cycle = predicted_maximal_minor(degrees, triangle_and_isolate)
    if observed_cycle != correct_cycle:
        raise AssertionError("cycle control fixture is invalid")

    wrong_total_sum = sum(degrees) * math.prod(
        degree ** (valence - 1)
        for degree, valence in zip(degrees, vertex_degrees(4, tree))
    )
    controls = (
        ("NC1 total sum substituted for bipartite balance", wrong_total_sum == observed_tree),
        ("NC2 odd-cycle factor 2 omitted", correct_cycle // 2 == observed_cycle),
        (
            "NC3 common gcd omitted from Smith form",
            exact_smith_diagonal(character_matrix((2, 2, 2, 2))) == (1, 1, 2),
        ),
        (
            "NC4 rank-one equal-degree collapse extrapolated to k=3",
            character_matrix((1, 1, 1)).rank() < 2,
        ),
    )
    for label, mutation_survived in controls:
        if mutation_survived:
            raise AssertionError(f"negative control survived: {label}")
        print(f"PASS {label} detected")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-vertices", type=int, default=5)
    parser.add_argument("--max-degree", type=int, default=3)
    args = parser.parse_args()
    print("character-lattice exact verification")
    print(f"python={platform.python_version()} sympy={sp.__version__}")
    print(
        f"bounds=max_vertices:{args.max_vertices},max_degree:{args.max_degree}"
    )
    verify_tree_formulas(args.max_vertices, args.max_degree)
    verify_general_minor_formulas(args.max_vertices, args.max_degree)
    verify_smith_structure(args.max_vertices, args.max_degree)
    negative_controls()


if __name__ == "__main__":
    main()
