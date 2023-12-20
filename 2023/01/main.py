bets = []
with open("bets.txt") as f_bets:
    bets = eval(f_bets.read().strip())

goals = []
with open("goals.txt") as f_goals:
    goals = eval(f_goals.read().strip())

bet_percent = 17.5 / 100

sukkerstenger = 50_000

for goal, (min_goal, odds) in zip(goals, bets):
    bet = round(sukkerstenger * bet_percent)
    if goal >= min_goal:
        sukkerstenger += round(bet * odds)
    else:
        sukkerstenger -= bet

print(50_000 - sukkerstenger)
