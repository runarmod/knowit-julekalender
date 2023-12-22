import itertools
from tqdm import tqdm


looking_coords_corners = [
    tuple(map(int, line.split(",")))
    for line in open("path.txt").read().strip().split("\n")
]

lines = open("stars.txt").read().strip().split("\n")
WIDTH, HEIGHT = len(lines[0]), len(lines)

stars = {(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "*"}


def get_looking_coords(original_x, original_y):
    for y in range(original_y - 1, original_y + 1 + 1):
        for x in range(original_x - 4, original_x + 4 + 1):
            yield (x % WIDTH, y % HEIGHT)

    for y in (original_y - 2, original_y + 2):
        for x in range(original_x - 2, original_x + 2 + 1):
            yield (x % WIDTH, y % HEIGHT)
    yield ((original_x - 5) % WIDTH, original_y % HEIGHT)
    yield ((original_y + 5) % WIDTH, original_y % HEIGHT)


seen: set[tuple[int, int]] = set()

for (start_x, start_y), (end_x, end_y) in zip(
    looking_coords_corners, looking_coords_corners[1:]
):
    direction = (
        (end_x - start_x) // max(1, abs(end_x - start_x)),
        (end_y - start_y) // max(1, abs(end_y - start_y)),
    )

    if direction == (1, 0):
        direction = (2, 0)
    elif direction == (-1, 0):
        direction = (0, 0)
    elif direction == (0, 1):
        direction = (1, 1)
    elif direction == (0, -1):
        direction = (1, -1)

    x, y = start_x, start_y
    length = max(abs(end_x - start_x), abs(end_y - start_y))
    dx, dy = direction
    for _ in range(length):
        for look_x, look_y in get_looking_coords(x, y):
            if (look_x, look_y) in stars:
                seen.add((look_x, look_y))
        x += dx
        y += dy
        x %= WIDTH
        y %= HEIGHT
    for look_x, look_y in get_looking_coords(x, y):
        if (look_x, look_y) in stars:
            seen.add((look_x, look_y))

assert len(seen) != 2641
assert len(seen) != 4044
assert len(seen) != 4058
assert len(seen) != 4059
assert len(seen) != 4193
assert len(seen) != 4624
assert len(seen) != 4653
assert len(seen) != 4869
assert len(seen) != 4885

print(f"{len(seen)=}")
