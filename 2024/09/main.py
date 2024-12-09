import sys

sys.setrecursionlimit(10**6)

m = {
    "nittiseks": 96,
    "nitti": 90,
    "åttifire": 84,
    "syttiåtte": 78,
    "syttito": 72,
    "sekstiseks": 66,
    "seksti": 60,
    "femtifire": 54,
    "førtiåtte": 48,
    "førtito": 42,
    "trettiseks": 36,
    "tretti": 30,
    "tjuefire": 24,
    "atten": 18,
    "tolv": 12,
    "seks": 6,
}

file = open("tall.txt", "r", encoding="utf-8").read().strip()
for key in m:
    assert key in file, key


def dfs(i, s):
    if i >= len(file):
        return s

    for key, val in m.items():
        if file[i : i + len(key)] != key:
            continue
        d = dfs(i + len(key), s + val)
        if d is not None:
            return d


print(dfs(0, 0) // 6)
