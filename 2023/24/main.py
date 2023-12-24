import string


lines = [
    line.split(";")
    for line in open("transaksjoner.txt", encoding="utf-8").read().strip().split("\n")
]
lines = [(line[0], int(line[1]), int(line[2])) for line in lines]


def _hash(tittel, pris):
    s = 0
    bokstaver = string.ascii_lowercase + "æøå"
    for c in tittel.lower():
        if c in bokstaver:
            s += bokstaver.index(c) + 1
    s *= pris
    return s % 0xBEEF


out = ""
for tittel, pris, hash in lines:
    h = _hash(tittel, pris)
    if h != hash:
        out += tittel[0]


print(out)
