from itertools import cycle


mapping = {
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

streng = open("tall.txt", "r", encoding="utf-8").read().strip()

i = len(streng)
s = 0
for tall_str, tall in cycle(mapping.items()):
    if streng.endswith(tall_str, 0, i):
        s += tall
        i -= len(tall_str)
        if i <= 0:
            break
print(s // 6)
