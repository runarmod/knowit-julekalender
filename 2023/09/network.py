print(
    sum(
        (
            path := __import__("networkx").algorithms.shortest_path(
                g := __import__("networkx").Graph(eval(open("rekke.txt").read())),
                *[n for n, d in g.degree if d == 1],
            )
        )[len(path) // 2 - 1 : len(path) // 2 + 1]
    )
)
