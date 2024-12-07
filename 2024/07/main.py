from itertools import chain
from more_itertools import triplewise


def lystig(tall: int):
    seen: set[int] = set()

    while tall not in (0, 1):
        if tall in seen:
            return False
        seen.add(tall)
        tall = sum(int(num) ** 2 for num in str(tall))
    return True


def jule3tall(tall: int):
    if tall < 10:
        return lystig(tall)
    s = str(tall)
    length = len(s)
    half_length = length // 2
    first_half, last_half = s[:half_length], s[half_length:]
    if length % 2 == 1:
        last_half = last_half[1:]

    first_half, last_half = int(first_half), int(last_half)
    return all(
        map(
            lystig,
            chain(
                (
                    tall,
                    first_half,
                    last_half,
                ),
                map(lambda num: int("".join(num)), triplewise(str(tall))),
            ),
        )
    )


assert jule3tall(1)
assert jule3tall(7)
assert jule3tall(70)
assert jule3tall(3100)
assert jule3tall(13023)


print(next(num for num in range(10_000_000 - 1, -1, -1) if jule3tall(num)))
