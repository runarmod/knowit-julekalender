import os
import re
from itertools import count


def _primes_from_list(file_nr: int):
    filename = f"primes.{str(file_nr).zfill(4)}"
    if not os.path.exists(filename):
        os.system(
            f"curl -s https://raw.githubusercontent.com/srmalins/primelists/refs/heads/master/100000primes/primes.{str(file_nr).zfill(4)} > {filename}"
        )
    yield from map(int, re.findall(r"\d+", open(filename).read()))


def primes():
    for i in count():
        yield from _primes_from_list(i)


def tverrsum(n: int):
    return sum(map(int, str(n)))


s = 0
c = 0
for i, prime in enumerate(primes(), start=1):
    if tverrsum(prime) == tverrsum(i):
        s += prime
        c += 1
        if c == 10_000:
            break
print(s)
