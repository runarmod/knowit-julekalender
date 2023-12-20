import itertools
import re

d = {
    i: itertools.cycle(map(int, re.findall(r"\d+", open(f"d{i}.txt").read())))
    for i in (4, 6, 8, 10, 20)
}

minimum_sleiphet = 18


def knivstikk():
    return (
        sum(sorted([next(d[6]), next(d[6])])[-1:]) + 2 + next(d[4])
        if next(d[20]) + 8 >= minimum_sleiphet
        else 0
    )


def sverdslag():
    return next(d[8]) + 5 if next(d[20]) + 6 >= minimum_sleiphet else 0


def okseslag():
    return (
        min([next(d[10]), next(d[10])]) + 6
        if next(d[20]) + 3 >= minimum_sleiphet
        else 0
    )


angrep = itertools.cycle((knivstikk, sverdslag, okseslag))

i = 0
helse = 10_000_000
while helse > 0:
    helse -= next(angrep)()
    i += 1
print("Antall angrep:", i)
