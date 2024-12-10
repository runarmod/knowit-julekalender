import numpy as np
from scipy.signal import convolve2d


def parse(filename):
    with open(filename) as f:
        lines = f.read().split("\n")
        longest = max(len(line) for line in lines)
        return np.array(
            [
                [
                    int(-2 if c == "x" else 0 if c == " " else c)
                    for c in line.ljust(longest)
                ]
                for line in lines
            ]
        )


joe = parse("joe.txt")
teppe = parse("teppe.txt")

m = 0
for _ in range(2):
    for _ in range(4):
        m = max(m, convolve2d(joe, teppe).max())
        teppe = np.rot90(teppe)
    teppe = np.flip(teppe, 1)

print(m)
