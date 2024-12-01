teppe = """ xxx
xxxxx
xxxxx
xxxxx
xxxxx
  x
xxxxx
xxxxx
xxxxx
xxxxx
 xxx""".split(
    "\n"
)

with open("joe.txt") as f:
    joe = f.read().rstrip().split("\n")

joe = [line.ljust(max(len(line) for line in joe)) for line in joe]
teppe = [line.ljust(max(len(line) for line in teppe)) for line in teppe]

joe = [tuple(map(int, line.replace(" ", "0"))) for line in joe]
teppe = [tuple(map(int, line.replace(" ", "0").replace("x", "1"))) for line in teppe]

m = 0
for offset_x in range(0, len(joe[0]) - len(teppe[0])):
    for offset_y in range(0, len(joe) - len(teppe)):
        m = max(
            m,
            sum(
                joe[teppe_y + offset_y][teppe_x + offset_x] * teppe[teppe_y][teppe_x]
                for teppe_y in range(len(teppe))
                for teppe_x in range(len(teppe[0]))
            ),
        )
print(m)
