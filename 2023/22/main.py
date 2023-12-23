from collections import deque
import itertools


looking_coords_corners = [
    tuple(map(int, line.split(",")))
    for line in open("path.txt").read().strip().split("\n")
]

lines = open("stars.txt").read().strip().split("\n")
stars = [deque([1 if c == "*" else 0 for c in line]) for line in lines]
WIDTH, HEIGHT = len(lines[0]), len(lines)


def get_looking_coords(original_x, original_y):
    for x, y in itertools.product(
        range(original_x - 4, original_x + 4 + 1),
        range(original_y - 1, original_y + 1 + 1),
    ):
        yield (x, y)

    for x, y in itertools.product(
        range(original_x - 2, original_x + 2 + 1),
        (original_y - 2, original_y + 2),  # It is corrent not being range...
    ):
        yield (x, y)

    yield ((original_x - 5), original_y)
    yield ((original_x + 5), original_y)


seen_count = 0

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
        curr = set()
        for look_x, look_y in get_looking_coords(x, y):
            curr.add((look_x, look_y))
            assert 0 <= look_x < WIDTH and 0 <= look_y < HEIGHT
            if stars[look_y][look_x]:
                stars[look_y][look_x] = 0
                seen_count += 1

        x += dx
        y += dy

        assert 0 <= x < WIDTH and 0 <= y < HEIGHT

        for i in range(HEIGHT):
            stars[i].rotate(-1)


print(f"Unique stars: {seen_count}")
