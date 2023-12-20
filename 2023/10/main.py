import itertools
import networkx as nx
from tqdm import tqdm

with open("sjokkis.txt") as f:
    content = f.read().strip()

lines = [list(itertools.batched(map(int, line), n=8)) for line in content.split("\n")]


def get_graphs():
    for line in lines:
        G = nx.Graph()
        for x, y in itertools.product(range(8), range(8)):
            if line[y][x] == 0:
                continue
            for dx, dy in ((1, 0), (0, 1)):
                if 0 <= x + dx < 8 and 0 <= y + dy < 8:
                    if line[y + dy][x + dx] == 1:
                        G.add_edge((x, y), (x + dx, y + dy))
        yield G


def possible_to_cut(G):
    if G.number_of_nodes() % 2:
        return 0
    for x, y in itertools.product(range(7), range(7)):
        for direction in ((1, 0), (0, 1)):
            for length in range(8 - (direction[0] * x + direction[1] * y)):
                H = G.copy()
                for i in range(length + 1):
                    if direction == (1, 0):
                        start, end = (x + i, y), (x + i, y + 1)
                    else:
                        start, end = (x, y + i), (x + 1, y + i)
                    if (start, end) in H.edges or (end, start) in H.edges:
                        H.remove_edge(start, end)
                connected_components = list(nx.connected_components(H))
                if len(connected_components) != 2:
                    continue
                if len(connected_components[0]) == len(connected_components[1]):
                    return 1
    return 0


s = 0
for G in tqdm(get_graphs(), total=len(lines)):
    s += possible_to_cut(G)
print(f"Antall godkjente sjokoladeplater: {s}")
