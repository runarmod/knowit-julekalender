from collections import Counter


def partition(number: list[int]):
    example = [
        [[0, 0], [0, 0], [1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0]],
        [[0, 0], [0, 0, 1, 1, 0, 1], [0, 1], [1, 0, 1, 0, 0, 0]],
        [[0, 0], [0, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 0], [0, 0]],
        [[0, 0, 0, 0, 1, 1], [0, 1], [0, 1], [1, 0, 1, 0, 0, 0]],
        [[0, 0, 0, 0, 1, 1], [0, 1], [0, 1, 1, 0, 1, 0], [0, 0]],
        [[0, 0, 0, 0, 1, 1], [0, 1, 0, 1, 1, 0], [1, 0], [0, 0]],
        [[0, 0, 0], [0, 1, 1], [0, 1, 0, 1, 1], [0, 1, 0, 0, 0]],
        [[0, 0, 0], [0, 1, 1, 0, 1], [0, 1, 1], [0, 1, 0, 0, 0]],
        [[0, 0, 0], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 0, 0]],
        [[0, 0, 0, 0, 1], [1, 0, 1], [0, 1, 1], [0, 1, 0, 0, 0]],
        [[0, 0, 0, 0, 1], [1, 0, 1], [0, 1, 1, 0, 1], [0, 0, 0]],
        [[0, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1], [0, 0, 0]],
        [[0, 0, 0, 0], [1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 0]],
    ]
    for line in example:
        out = []
        for section in line:
            a = sum(map(len, out))
            out.append(tuple(number[a : a + len(section)]))
        yield out


def valid_partion(part: tuple[tuple[int]]):
    c = Counter(part)
    assert sum(c.values()) == 4
    return all(value in (2, 4) for value in c.values())


def isDombjelletall(num):
    bits = list(map(int, bin(num)[2:].zfill(16)))
    return any(map(valid_partion, partition(bits)))


assert isDombjelletall(3432)
print(sum(map(isDombjelletall, range(2**16))))
