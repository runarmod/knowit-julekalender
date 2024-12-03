from itertools import count


refill = {
    "ris": [0, 0, 1, 0, 0, 2],
    "erter": [0, 3, 0, 0],
    "gulrøtter": [0, 1, 0, 0, 0, 8],
    "reinsdyrkjøtt": [100, 80, 40, 20, 10],
    "julekringle": [0],
}

current = {food: 100 for food in refill}

reinsdyr_tomt = None

for t in count():
    eatable = []
    if current["ris"] > 0:
        eatable.append(["ris", min(5, current["ris"])])
    if current["erter"] > 0:
        eatable.append(["erter", min(5, current["erter"])])
    if current["gulrøtter"] > 0:
        eatable.append(["gulrøtter", min(5, current["gulrøtter"])])
    if current["reinsdyrkjøtt"] > 0:
        eatable.append(["reinsdyrkjøtt", min(2, current["reinsdyrkjøtt"])])
    if current["julekringle"] > 0:
        eatable.append(["julekringle", min(1, current["julekringle"])])
    eat = eatable[:2]
    if len(eat) == 0:
        break
    if (
        "reinsdyrkjøtt" in eat[0]
        or "julekringle" in eat[0]
        or eat[1]
        and ("julekringle" in eat[1] or "reinsdyrkjøtt" in eat[1])
    ):
        eat = eat[:1]

    if len(eat) == 2:
        eat[1][1] = min(3, eat[1][1])
    for food, amount in eat:
        current[food] -= amount
        if food == "reinsdyrkjøtt" and current[food] == 0:
            reinsdyr_tomt = t

    # Fill
    for food, amount in refill.items():
        if food == "gulrøtter" and t <= 30:
            continue
        if food == "reinsdyrkjøtt" and (
            reinsdyr_tomt is None or reinsdyr_tomt + 50 < t
        ):
            continue
        current[food] += amount[t % len(amount)]
        if food == "reinsdyrkjøtt":
            refill[food][t % len(amount)] = 0

print(t)
