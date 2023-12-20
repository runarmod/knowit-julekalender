test = False

filename = "example.txt" if test else "input.txt"
money = 1_000 if test else 200_000

lines = None
with open(filename) as f:
    lines = [list(map(int, line.split(","))) for line in f.read().strip().split("\n")]


for line in lines:
    best = money
    for i, buy_price in enumerate(line):
        for j, sell_price in enumerate(line[i:], start=i):
            stocks = money // buy_price
            rest = money - stocks * buy_price
            new_money = stocks * sell_price + rest
            best = max(best, new_money)
    money = best

print(f"Answer: {money}")
