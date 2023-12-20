from pprint import pprint
from PIL import Image


files = [
    (name, eval(dirs))
    for name, dirs in [
        line.split(", ", 1) for line in open("puzzle.txt").read().strip().split("\n")
    ]
]

all_edges = [edge for _, edges in files for edge in edges if edge != -1]
assert len(all_edges) == len(set(all_edges)), "Duplikate kanter :("

edge_pair_sum = sum(all_edges) // (
    len(all_edges) // 2
)  # Verdien alle kant-par skal summe til (7 i eksempelet)


class CustomImage:
    def __init__(self, name: str):
        self.name = name
        self.rotation: int = 0
        self.neighbors: list[str] = [None for _ in range(4)]

    def rotate_right(self):
        self.rotation += 1
        self.neighbors = [self.neighbors[(i + 1) % 4] for i in range(4)]

    @property
    def top(self) -> str:
        return self.neighbors[0]

    @property
    def right(self) -> str:
        return self.neighbors[1]

    @property
    def bottom(self) -> str:
        return self.neighbors[2]

    @property
    def left(self) -> str:
        return self.neighbors[3]

    def __repr__(self):
        return f"{self.name}"


images: dict[str, CustomImage] = dict()
for name, dirs in files:
    images[name] = CustomImage(name)
    for i in range(4):
        for name2, dirs2 in files:
            if edge_pair_sum - dirs[i] in dirs2:
                images[name].neighbors[i] = name2

# Velger en tilfeldig brikke som top_left
top_left = next(
    filter(
        lambda img: len([x for x in img.neighbors if x != None]) == 2, images.values()
    )
)

while not (top_left.top is None and top_left.left is None):
    top_left.rotate_right()

final_image: list[list[CustomImage]] = [[None for _ in range(15)] for _ in range(15)]
final_image[0][0] = top_left

for y in range(15):
    for x in range(15):
        if x == 0 and y == 0:
            continue
        elif x == 0:
            next_image = images[final_image[y - 1][x].bottom]
            while next_image.top != final_image[y - 1][x].name:
                next_image.rotate_right()
            final_image[y][x] = next_image
        else:
            next_image = images[final_image[y][x - 1].right]
            while next_image.left != final_image[y][x - 1].name:
                next_image.rotate_right()
            final_image[y][x] = next_image

# pprint(final_image, compact=True, width=200)

frame_width = Image.open("pieces/" + final_image[0][0].name).size[0]
out_image = Image.new("RGB", (15 * frame_width, 15 * frame_width), color="red")

for y in range(15):
    for x in range(15):
        name = final_image[y][x].name
        img = Image.open("pieces/" + name).rotate(90 * final_image[y][x].rotation)
        out_image.paste(img, (x * frame_width, y * frame_width))

# Ser i etterkant at top_left ble valgt feil, men roterer bare hele bildet, så er det fikset
out_image.rotate(90).save("out.png")
