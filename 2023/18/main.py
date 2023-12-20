import re


def find_start(lines):
    for y in range(len(lines)):
        if lines[y][0] != " ":
            return y


def calculate_profit(filename):
    lines = open(filename).read().rstrip().split("\n")
    amount = map(int, re.findall(r"\d+", lines[-1]))
    y = find_start(lines)
    total = 0

    for x in range(len(lines[0])):
        price = len(lines) - y - 1 - 1
        if lines[y][x] != "#":
            total += price * next(amount) * (-1 if lines[y][x] == "K" else 1)
        for dy in (-1, 0, 1):
            if (
                x < len(lines[0]) - 1
                and 0 <= y + dy < len(lines)
                and lines[y + dy][x + 1] != " "
            ):
                y += dy
                break
    return total


print(sum(map(calculate_profit, [f"graphs/graph_{i}.txt" for i in range(1, 11)])))
