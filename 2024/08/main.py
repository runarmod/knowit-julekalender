import os
import re
from itertools import count, takewhile

import sympy


def primes():
    def _primes_from_list(file_nr: int):
        filename = f"primes.{str(file_nr).zfill(4)}"
        if not os.path.exists(filename):
            os.system(
                f"curl -s https://raw.githubusercontent.com/srmalins/primelists/refs/heads/master/100000primes/primes.{str(file_nr).zfill(4)} > {filename}"
            )
        yield from map(int, re.findall(r"\d+", open(filename).read()))

    for i in count():
        yield from _primes_from_list(i)


def primtalvs():
    s = 0
    for prime in primes():
        for i, d_prime in enumerate(str(prime)):
            s += int(d_prime) * 10**i
        yield s


def perfekt_primtalvs():
    yield from filter(sympy.isprime, primtalvs())


def perfekt_primtalvs_under(n):
    yield from takewhile(lambda p: p < n, perfekt_primtalvs())


print(sum(1 for _ in perfekt_primtalvs_under(10_000_000)))
