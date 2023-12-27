from itertools import pairwise
from math import ceil

print(
    ceil(
        sum(
            ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5
            for coord1, coord2 in pairwise(
                tuple(map(int, line.split(",")))
                for line in open("rute.txt").read().strip().split("\n")
            )
        )
        * 9
        / 1000
    )
)
