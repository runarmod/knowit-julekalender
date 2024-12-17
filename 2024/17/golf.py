import re
from functools import reduce
from itertools import product
from operator import mul

from more_itertools import distinct_permutations, islice_extended, set_partitions

print(
    sum(
        filter(
            lambda tall: any(
                map(
                    lambda splits: any(
                        reduce(mul, map(int, map("".join, permutations))) == tall
                        for permutations in product(
                            *(distinct_permutations(sl) for sl in splits)
                        )
                    ),
                    islice_extended(set_partitions(str(tall)))[1:],
                )
            ),
            map(int, re.findall(r"\d+", open("tall.txt").read())),
        )
    )
)
