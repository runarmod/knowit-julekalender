import itertools
import re

from tqdm import tqdm

# The name of the displays
DISPLAY_LETTERS = "ABCDEFGHI"

# The segments that should be active for each digit (0, 1, 2, ..., 9)
DIGIT_SEGMENTS = [
    "ABCDEF",
    "BC",
    "ABDEG",
    "ABCDG",
    "BCFG",
    "ACDFG",
    "ACDEFG",
    "ABC",
    "ABCDEFG",
    "ABCDFG",
]

SWAP_INSTRUCTIONS = """
AC <-> IB
BD <-> EG
GF <-> DE
BA <-> BB"""


# Dictionary with entries {"AC": "IB", "IB": "AC", ...}
swap_map = {}
swap_map.update(
    itertools.chain(
        *(
            [(section1, section2), (section2, section1)]
            for section1, section2 in re.findall(r"(\w+) <-> (\w+)", SWAP_INSTRUCTIONS)
        )
    )
)

# Dictionary with a list of the sections that should be active for each digit on each display
displays = {
    display: [
        set(
            [
                swap_map.get(display + segment, display + segment)
                for segment in DIGIT_SEGMENTS[digit]
            ]
        )
        for digit in range(10)
    ]
    for display in DISPLAY_LETTERS
}


changed_letters = {
    letter
    for letter in DISPLAY_LETTERS
    if any(letter == double[0] for double in swap_map)
}

s = 0
for values in tqdm(
    itertools.product(range(10), repeat=len(changed_letters)),
    total=10 ** len(changed_letters),
    leave=False,
):
    # Find which sections should be active
    sections_should_be_active = set()
    for display_letter, digit_value in zip(changed_letters, values):
        sections_should_be_active.update(
            (
                display_letter + section_letter
                for section_letter in DIGIT_SEGMENTS[digit_value]
            )
        )

    # Find out if every place is correct
    for display_letter, digit_value in zip(changed_letters, values):
        sections = displays[display_letter][digit_value]
        if not all(section in sections_should_be_active for section in sections):
            break
    else:
        s += 1

print(s * 10 ** (len(DISPLAY_LETTERS) - len(changed_letters)))
