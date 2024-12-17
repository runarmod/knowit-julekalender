import re
from functools import partial, reduce
from itertools import product
from operator import mul

from more_itertools import distinct_permutations, islice_extended, set_partitions


def godkjent_splitts(splits: list[str], tall: int) -> bool:
    for permutations in product(*(distinct_permutations(sl) for sl in splits)):
        if reduce(mul, map(int, map("".join, permutations))) == tall:
            return True
    return False


def pseudo_vampyr(tall: int):
    return any(
        map(
            partial(godkjent_splitts, tall=tall),
            islice_extended(set_partitions(str(tall)))[1:],
        )
    )


print(sum(filter(pseudo_vampyr, map(int, re.findall(r"\d+", open("tall.txt").read())))))
