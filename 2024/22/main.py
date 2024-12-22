from collections import deque
from copy import deepcopy

from tqdm import tqdm


def custom_cache(func):
    cache = {}

    def wrapper(board):
        tuple_board = tuple("".join(row) for row in board)
        if tuple_board not in cache:
            cache[tuple_board] = func(board)
        return cache[tuple_board]

    return wrapper


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
    new_board = deepcopy(board)
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


def non_empty_coords(board: list[list[str]]):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell != " ":
                yield x, y


@custom_cache
def remaining_moves(board: list[list[str]]) -> int:
    if next(non_empty_coords(board), None) is None:  # Empty board
        return 0

    optimal_group = get_optimal_group(board)
    if optimal_group is not None:
        return 1 + remaining_moves(remove_group(board, optimal_group))

    removed = set()
    best = float("inf")
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if (x, y) in removed or cell == " ":
                continue
            group = get_group(board, x, y)
            removed.update(group)
            best = min(best, 1 + remaining_moves(remove_group(board, group)))
    return best


print(sum(remaining_moves(board) for board in tqdm(data)))
