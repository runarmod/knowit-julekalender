nums = eval(open("rekke.txt").read())
# nums = [(1, 2), (4, 3), (2, 3)]
nums = set(nums)


class Node:
    def __init__(self, index: int):
        self.index = index
        self.neighbors = set()

    def get_index(self):
        return self.index

    def get_neighbors(self):
        return self.neighbors

    def add_neighbor(self, neighbor: "Node"):
        self.neighbors.add(neighbor)

    def __repr__(self):
        return f"Node({self.index}, {set(node.get_index() for node in self.neighbors)})"


nodes = set()
for index, neighbor_int in nums:
    node: "Node" = None
    neighbor: "Node" = None
    if any(map(lambda x: x.index == index, nodes)):
        node = next(filter(lambda x: x.index == index, nodes))
    else:
        node = Node(index)
        nodes.add(node)
    if any(map(lambda x: x.index == neighbor_int, nodes)):
        neighbor = next(filter(lambda x: x.index == neighbor_int, nodes))
    else:
        neighbor = Node(neighbor_int)
        nodes.add(neighbor)
    node.add_neighbor(neighbor)
    neighbor.add_neighbor(node)

ends = list(filter(lambda x: len(x.neighbors) == 1, nodes))


def get_neighbors(node: Node, prev: Node):
    return next(iter(node.neighbors - {prev}))


l = [None, ends.pop()]
nodes -= {l[0]}
while True:
    l.append(get_neighbors(l[-1], l[-2]))
    if l[-1] in ends:
        break
l = l[1:]
print(sum(node.get_index() for node in l[len(l) // 2 - 1 : len(l) // 2 + 1]))
