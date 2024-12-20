import re
from collections import Counter

# with open("eksempel.txt") as f:
with open("usorterte_alver.txt") as f:
    alver = [
        (line[0], int(line[1])) for line in re.findall(r"(.+) (\d+)", f.read().strip())
    ]

fest_count = Counter()


def sort(alver: list[tuple[str, int]]):
    i = 0
    moved = 0
    while i < len(alver) - 1:
        i = max(0, i)
        if alver[i + 1][1] < alver[i][1]:
            alver[i], alver[i + 1] = alver[i + 1], alver[i]
            moved += 1
            if moved % 7 == 0:
                fest_count.update(map(lambda x: x[0], alver[i + 1 : i + 6]))
                alver[i + 1 : i + 6] = alver[i + 1 : i + 6][::-1]
            i -= 1
        else:
            i += 1


sort(alver)
print(",".join(map(str, fest_count.most_common(1)[0])))
