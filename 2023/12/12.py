from itertools import count


with open("primes.txt") as f:
    primes = [int(x) for x in f.read().split() if int(x) <= 6**6 + 666]


twin_primes = [
    (primes[i], primes[i + 1])
    for i in range(len(primes) - 1)
    if primes[i + 1] - primes[i] == 2
]


def get_even_1s():
    for j in count():
        if bin(j).count("1") % 2 == 0:
            yield j


def get_ith_even_1s(i):
    for j in get_even_1s():
        if i == 0:
            return j
        i -= 1


def rot_alpha(*symbols):
    def _rot(n):
        encoded = "".join(sy[n:] + sy[:n] for sy in symbols)
        lookup = str.maketrans("".join(symbols), encoded)
        return lambda s: s.translate(lookup)

    return _rot


def rot(c, n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc

    return rot_alpha(lc + uc)(n)(c)


cipher = "Ojfkyezkz bvclae zisj a guomiwly qr tmuematbcqxqv sa zmcgloz."

for i, c in enumerate(cipher):
    n = (len(twin_primes) * get_ith_even_1s(i)) % (26 * 2)
    if c.isalpha():
        print(rot(c, -n), end="")
    else:
        print(c, end="")
print()
print("Ondskapen trives best i skyggene av likegyldighet og taushet.")
