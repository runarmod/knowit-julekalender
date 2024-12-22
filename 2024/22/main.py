import heapq
from collections import deque

from tqdm import tqdm

with open("stekebrett.txt", encoding="utf-8") as f:
    data = [
        [list(line) for line in section.split("\n")]
        for section in f.read().strip().split("\n\n")
    ]


def get_optimal_group(board: list[list[str]]):
    W, H = len(board[0]), len(board)
    for by, row in enumerate(board):
        for bx, group_type in enumerate(row):
            if group_type == " ":
                continue

            group = get_group(board, bx, by)

            if not all(
                y == 0 or board[y - 1][x] in (board[y][x], " ") for x, y in group
            ):
                continue  # Annen type funnet over gruppen

            left_edge = min(x for x, y in group)
            right_edge = max(x for x, y in group)
            optimal = True

            for y in range(H):
                for x in range(max(0, left_edge - 1), min(W, right_edge + 2)):
                    if (x, y) in group:
                        continue
                    if board[y][x] == group_type:
                        optimal = False
                        break
                if not optimal:
                    break
            if optimal:
                return group
    return None


def get_group(board: list[list[str]], x: int, y: int):
    group_type = board[y][x]
    q = deque([(x, y)])
    removable = set()

    while q:
        x, y = q.popleft()
        removable.add((x, y))

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_x, new_y = x + dx, y + dy

            if (
                new_x in range(len(board[0]))
                and new_y in range(len(board))
                and board[new_y][new_x] == group_type
                and (new_x, new_y) not in removable
            ):
                q.append((new_x, new_y))
    return removable


def remove_group(board: list[list[str]], group: set[tuple[int, int]]):
    # Remove group
    new_board = list(map(list, board))
    for x, y in group:
        new_board[y][x] = " "

    # Apply gravity
    for x in range(len(new_board[0])):
        for y in range(len(new_board) - 1, -1, -1):
            if new_board[y][x] == " ":
                for new_y in range(y - 1, -1, -1):
                    if new_board[new_y][x] != " ":
                        new_board[y][x] = new_board[new_y][x]
                        new_board[new_y][x] = " "
                        break
    return new_board


def heuristic(grid: list[list[str]]):
    return sum(1 for row in grid for c in row if c != " ") / 4


def Astar(grid: list[list[str]]):
    q = []
    heapq.heappush(q, (0, 0, grid))  # (steps + heuristic, steps, state)
    visited = set()

    while q:
        _, steps, state = heapq.heappop(q)
        if all(all(c == " " for c in row) for row in state):
            return steps
        t_state = tuple(map(tuple, state))
        if t_state in visited:
            continue
        visited.add(t_state)
        optimal_group = get_optimal_group(state)
        if optimal_group is not None:
            new_state = remove_group(state, optimal_group)
            heapq.heappush(q, (steps + 1 + heuristic(new_state), steps + 1, new_state))
            continue

        removed = set()
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x] == " " or (x, y) in removed:
                    continue
                group = get_group(state, x, y)
                removed.update(group)
                new_state = remove_group(state, group)
                heapq.heappush(
                    q, (steps + 1 + heuristic(new_state), steps + 1, new_state)
                )
    assert False, "No solution found"


print(sum(map(Astar, tqdm(data, leave=False))))
