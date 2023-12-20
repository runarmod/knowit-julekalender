from sympy import isprime
from tqdm import tqdm


def get_primes():
    yield 2
    yield 3
    i = 6
    while True:
        a = i - 1
        b = i + 1
        if isprime(a):
            yield a
        if isprime(b):
            yield b
        i += 6


def save_primes(n):
    with open("primes.txt", "w") as f:
        for i, p in tqdm(enumerate(get_primes()), total=n):
            f.write(str(p) + "\n")
            if i > n:
                break


working = set(map(int, open("input/alver_på_jobb.txt").read().strip().split("\n")))
not_working = set(
    map(int, open("input/alver_ikke_på_jobb.txt").read().strip().split("\n"))
)
grinchen = set(map(int, open("input/grinchen.txt").read().strip().split("\n")))
windows = 400_009
# save_primes(max(working + not_working))

# Test case
# working = [0, 6]
# not_working = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13]
# grinchen = [5]
# windows = 7


primes = list(map(int, open("primes.txt").readlines()))
hashes = {lambda x: (x * 2) % windows, lambda x: (x + primes[x]) % windows}

windows_lit = {h(elf) for elf in working for h in hashes}
slipper_unna = sum((all(h(elf) in windows_lit for h in hashes) for elf in not_working))

new_windows_lit = windows_lit - grinchen
slipper_unna_igjen = sum(
    all(h(elf) in new_windows_lit for h in hashes) for elf in not_working
)

print("Antall ferska:", slipper_unna - slipper_unna_igjen)
