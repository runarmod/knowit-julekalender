import networkx as nx

kart = open("kart.txt").read().strip().split("\n")

G = nx.Graph()
for y, line in enumerate(kart):
    for x, c in enumerate(line):
        if c != "X":
            continue
        G.add_node((x, y))
        for dx, dy in ((1, -1), (1, 0), (1, 1), (0, 1)):
            # Sjekker bare til høyre og ned siden G er en undirected graph
            if (
                not dx == dy == 0
                and 0 <= x + dx < len(line)
                and 0 <= y + dy < len(kart)
                and kart[y + dy][x + dx] == "X"
            ):
                G.add_edge((x, y), (x + dx, y + dy))
print(sum(1 for _ in nx.connected_components(G)))
