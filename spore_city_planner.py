from itertools import product
from typing import TypeVar

T = TypeVar("T")


def flatten_tuple(tup: tuple[tuple[T, ...] | list[T] | T, ...] | list, typ: type[T]) -> list[T]:
    stack = [(tup, 0)]
    flattened = []

    while stack:
        current, state = stack.pop()

        if state == 0:
            current = iter(current)
        try:
            elem = next(current)
            stack.append((current, 1))

            if isinstance(elem, typ):
                flattened.append(elem)
            else:
                stack.append((elem, 0))
        except StopIteration:
            continue

    return flattened


def evaluator(graph: tuple[tuple[int, int], ...], variant: tuple[str, ...]) -> tuple[int, int, int, int]:
    n_h, n_e, n_f = variant.count("H"), variant.count("E"), variant.count("F")

    production = 0
    happiness = n_e - n_f
    population = n_h * 15 + 15
    cost = n_h * 1600 + n_e * 800 + n_f * 1200

    dct = dict(enumerate(variant, start=1))
    dct[0] = "C"
    for v, u in graph:
        if dct[v] == "C" and dct[u] == "E" or dct[v] == "E" and dct[u] == "C":  # city hall & entertainment
            happiness += 1
        elif dct[v] == "H" and dct[u] == "E" or dct[v] == "E" and dct[u] == "H":  # house & entertainment
            happiness += 1
        elif dct[v] == "F" and dct[u] == "E" or dct[v] == "E" and dct[u] == "F":  # factory & entertainment
            happiness -= 1
        elif dct[v] == "C" and dct[u] == "F" or dct[v] == "F" and dct[u] == "C":  # city hall & factory
            production += 1
        elif dct[v] == "H" and dct[u] == "F" or dct[v] == "F" and dct[u] == "H":  # house and factory
            production += 1

    return production, happiness, population, cost


def main() -> None:
    allow_sad = True

    colony = (
        (0, 2),
        (0, 4),
        (0, 9),
        (0, 10),
        (0, 11),
        (5, 11),
        (6, 11),
        (5, 6),
        (6, 7),
        (7, 10),
        (8, 10),
        (7, 8),
        (4, 5),
        (8, 9),
        (3, 4),
        (2, 3),
        (2, 9),
        (1, 2),
    )
    homeworld_1 = (
        (1, 10),
        (2, 3),
        (0, 10),
        (0, 3),
        (10, 11),
        (0, 11),
        (0, 5),
        (0, 7),
        (3, 4),
        (4, 5),
        (9, 10),
        (8, 9),
        (3, 5),
        (8, 11),
        (7, 11),
        (7, 8),
        (5, 7),
        (6, 7),
        (5, 6),
    )
    homeworld_2 = (
        (1, 10),
        (2, 3),
        (3, 4),
        (9, 10),
        (0, 10),
        (0, 3),
        (3, 5),
        (0, 5),
        (0, 11),
        (8, 10),
        (8, 9),
        (8, 11),
        (5, 11),
        (7, 8),
        (6, 7),
        (5, 6),
    )
    homeworld_3 = (
        (0, 1),
        (0, 3),
        (0, 4),
        (0, 5),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
    )
    homeworld_4 = (
        (0, 3),
        (0, 4),
        (0, 5),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
    )
    homeworld_5 = (
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
    )

    city = homeworld_2

    permutations = product(("F", "H", "E"), repeat=max(flatten_tuple(city, int)))
    configs: list[tuple[str, int, int, int, int]] = []
    for perm in permutations:
        prod, happy, pop, cost = evaluator(city, perm)
        if allow_sad or not allow_sad and happy >= 0:
            configs.append(("".join(list(perm)), prod, happy, pop, cost))

    #configs.sort(key=lambda x: (-x[1], x[4], -x[2], -x[3]))  # prod desc, cost asc, happy desc, pop desc
    configs.sort(key=lambda x: (-x[1], x[4], -x[2], -x[3]))
    print(*configs[:100])

    #print(evaluator(colony, ("H", "F", "H", "F", "H", "H", "E", "H", "F", "E", "F")))


if __name__ == "__main__":
    main()
