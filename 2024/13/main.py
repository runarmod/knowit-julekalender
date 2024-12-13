from typing import Counter


def parse_line(line):
    line = line.split("/")
    assert len(line) == 5
    return (
        line[0],
        int(line[1]),
        line[2] == "B",
        tuple(map(int, line[3].split("-"))),
        Counter(line[4]),
    )


clubs = {
    "FCB": 1,
    "J": 2,
    "NT": 1,
    "NF": 1,
    "RC": 3,
    "SP": 2,
    "VM": 3,
}


def main():
    with open("salary.txt") as f:
        data = f.read()
        lines = map(parse_line, data.strip().split(",\n"))

    salary = 0
    loss_streak = 0
    for opponent, minutes, away, (home_goals, away_goals), extras in lines:
        base_salary = 100 * minutes
        our_goals, their_goals = (
            (away_goals, home_goals) if away else (home_goals, away_goals)
        )
        won = our_goals > their_goals
        lost = our_goals < their_goals

        salary_percentage = 100
        salary_percentage += 5 * (our_goals - their_goals)
        for type, count in extras.items():
            match type:
                case "A":
                    salary_percentage += 1 * count
                case "S":
                    salary_percentage += 2 * count
                case "B":
                    salary_percentage += 2 * count
                case _:
                    raise ValueError(f"Unknown extra type: {type}")
        salary_percentage += clubs[opponent] * (1 if won else -1 if lost else 0)

        if won:
            salary_percentage += loss_streak
            loss_streak = 0
        elif lost:
            if loss_streak == 0:
                loss_streak = 3
            else:
                loss_streak += 1
        salary += base_salary * salary_percentage // 100

    print(salary)


if __name__ == "__main__":
    main()
