from collections import deque
import itertools
from pprint import pprint
from tqdm import tqdm


class Star:
    def __init__(self):
        self.seen = False


looking_coords_corners = [
    tuple(map(int, line.split(",")))
    for line in open("path.txt").read().strip().split("\n")
]

lines = open("stars.txt").read().strip().split("\n")
WIDTH, HEIGHT = len(lines[0]), len(lines)

stars = [deque([Star() if c == "*" else 0 for c in line]) for line in lines]


def cap(value, min, max):
    return max if value > max else min if value < min else value


def get_looking_coords(original_x, original_y):
    for y in range(original_y - 1, original_y + 1 + 1):
        for x in range(original_x - 4, original_x + 4 + 1):
            yield cap(x, 0, WIDTH - 1), cap(y, 0, HEIGHT - 1)

    for y in (original_y - 2, original_y + 2):
        for x in range(original_x - 2, original_x + 2 + 1):
            yield cap(x, 0, WIDTH - 1), cap(y, 0, HEIGHT - 1)
    yield cap(original_x - 5, 0, WIDTH - 1), cap(original_y, 0, HEIGHT - 1)
    yield cap(original_x + 5, 0, WIDTH - 1), cap(original_y, 0, HEIGHT - 1)


seen: set[Star] = set()

time = -1
for (start_x, start_y), (end_x, end_y) in zip(
    looking_coords_corners, looking_coords_corners[1:]
):
    direction = (
        (end_x - start_x) // max(1, abs(end_x - start_x)),
        (end_y - start_y) // max(1, abs(end_y - start_y)),
    )

    x, y = start_x, start_y
    length = max(abs(end_x - start_x), abs(end_y - start_y))
    dx, dy = direction
    for _ in range(length):
        time += 1
        for i in range(HEIGHT):
            stars[i].rotate(-1)
        real_end_x = (end_x + (-1 * time)) % WIDTH
        real_y = y
        print()
        for look_x, look_y in get_looking_coords(real_end_x, real_y):
            print(look_x, look_y)
            if isinstance(stars[look_y][look_x], Star):
                stars[look_y][look_x].seen = True
                seen.add(stars[look_y][look_x])

        x += dx
        y += dy

        # TURN AROUND
        if x < 0:
            direction = (1, 0)
            dx, dy = direction
            x = 1
        if x >= WIDTH:
            direction = (-1, 0)
            dx, dy = direction
            x = WIDTH - 2
        # if y < 0:
        #     direction = (0, 1)
        #     dx, dy = direction
        #     y = 1
        # if y >= HEIGHT:
        #     direction = (0, -1)
        #     dx, dy = direction
        #     y = HEIGHT - 2
    # print(time)
    #     for look_x, look_y in get_looking_coords(x, y):
    #         if (look_x, look_y) in stars:
    #             seen.add((look_x, look_y))
    #     x += dx
    #     y += dy
    #     x %= WIDTH
    #     y %= HEIGHT
    # for look_x, look_y in get_looking_coords(x, y):
    #     if (look_x, look_y) in stars:
    #         seen.add((look_x, look_y))

assert len(seen) != 2641
assert len(seen) != 4044
assert len(seen) != 4058
assert len(seen) != 4059
assert len(seen) != 4193
assert len(seen) != 4483
assert len(seen) != 4624
assert len(seen) != 4653
assert len(seen) != 4869
assert len(seen) != 4885

print(f"{len(seen)=}")
