import math
import re
import sys

sys.setrecursionlimit(10**6)


def cache(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n) % (10**20)
        return cache[n]

    return wrapper


rekker = {}


@cache
def alvonacci(n):
    if n <= 1:
        return n

    log = round(math.log(n, 5))
    if 5**log == n:
        rekker[5**log] = 0

    s = alvonacci(n - 1) + alvonacci(n - 2)

    if n % 5 == 0:
        for i in sorted(rekker.keys(), reverse=True):
            if n % i == 0:
                rekker[i] += 1
                return alvonacci(rekker[i] - 1)
    elif n % 5 == 1:
        return s + alvonacci(n - 3)
    return s


# Testing
for n, fasit in map(
    lambda line: map(int, line),
    re.findall(r"(\d+): (\d+)", open("eksempler.txt").read()),
):
    calc = alvonacci(n)
    assert calc == fasit, f"{n}: {calc=}, {fasit=}"

print(alvonacci(5**8 - 1))
