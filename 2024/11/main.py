import heapq
import math

reach = """Venstre          Høyre
       xxx           xxx
     xxxxxxx       xxxxxxx
    xxxxxxxxx     xxxxxxxxx
   xxxxxxxxxxx   xxxxxxxxxxx
  xxxxxxxxxxxx   xxxxxxxxxxxx
 xxxxxxxxxxxxx   xxxxxxxxxxxxx
 xxxxxxxxxxxxx   xxxxxxxxxxxxx
xxxxxxxxxxxxx     xxxxxxxxxxxxx
xxxxxxxxxxxx       xxxxxxxxxxxx
         o           o""".split(
    "\n"
)

# Parse reach
starts = (
    (x, y) for y, line in enumerate(reach) for x, c in enumerate(line) if c == "o"
)
reaches = []
for start_x, start_y in starts:
    reach_from_here = set()
    prev_y = start_y
    for y in range(start_y, 0, -1):
        for dx in (-1, 1):
            x, y = start_x, prev_y - 1
            while x in range(len(reach[y])) and reach[y][x] == "x":
                reach_from_here.add((start_y - y, x - start_x))
                x += dx
        prev_y = y
    reaches.append(reach_from_here)

assert len(reaches) == 2

# Parse grep
with open("grep.txt") as f:
    grep = set()
    for line in f.read().strip().split("\n"):
        grep.add(tuple(map(int, line.split(" "))))

# Dijkstra
start_coords, end_coords = (0, 250), (999, 749)
q = [
    (0, start_coords, False, False),
    (0, start_coords, True, True),
]  # (dist, coords, current_hand, start_hand) (hand: False=venstre, True=høyre)
heapq.heapify(q)

visited = set()
while q:
    dist, coords, current_hand, start_hand = heapq.heappop(q)
    if (coords, current_hand) in visited:
        continue
    visited.add((coords, current_hand))
    if coords == end_coords:
        print(
            math.floor(10 * dist),
            ["venstre", "høyre"][start_hand],
            ["venstre", "høyre"][current_hand],
            sep=",",
        )
        break
    next_hand = not current_hand
    for dy, dx in reaches[next_hand]:
        new_coords = (coords[0] + dy, coords[1] + dx)
        if new_coords not in grep:
            continue
        extra_dist = (dx**2 + dy**2) ** 0.5
        heapq.heappush(q, (dist + extra_dist, new_coords, next_hand, start_hand))
