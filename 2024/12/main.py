import datetime
from collections import deque


def is_advent_sunday(date: datetime.date) -> bool:
    advent_sundays = []
    current_date = datetime.date(date.year, 12, 24)
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)
    for _ in range(4):
        advent_sundays.append(current_date)
        current_date -= datetime.timedelta(days=7)
    return date in advent_sundays


def sundays_since_known_bad_update(date: datetime.date) -> int:
    # Vi vet at vi har en dårlig update om det er advent/juli/19. april
    sundays_since_bad_update = 0
    current_date = date
    while (
        current_date.month != 7
        and current_date > datetime.date(2020, 4, 19)
        and not is_advent_sunday(current_date)
    ):
        if current_date.weekday() == 6:
            sundays_since_bad_update += 1
        current_date -= datetime.timedelta(days=7)
    return sundays_since_bad_update


def bad_update(date: datetime.date) -> bool:
    if date.weekday() != 6 or date < datetime.date(2020, 4, 19):
        return False
    if date.month == 7 or is_advent_sunday(date):
        return True

    sundays = sundays_since_known_bad_update(date)
    # Hvis det er (et tall delelig på 3) søndager siden sist, så er det en dårlig update
    return sundays % 3 == 0


start = datetime.date(2020, 4, 1)
total_bookmarks = 0
recent_bookmarks = deque([1], maxlen=2)
yesterday_bad = False

current_date = start
while current_date <= datetime.date(2024, 12, 12):
    if bad_update(current_date):
        recent_bookmarks.append(0)
        yesterday_bad = True
    elif yesterday_bad:
        recent_bookmarks.append(1)
        yesterday_bad = False
    elif current_date != start:
        recent_bookmarks.append(sum(recent_bookmarks))
    total_bookmarks += recent_bookmarks[-1]
    current_date += datetime.timedelta(days=1)
print(total_bookmarks)
