import re


reps = map(int, re.findall(r"\d+", open("reps.txt").read()))


class Streak:
    def __init__(self, rep=None):
        if rep:
            self.reps = [rep]
            self.length = 1
        else:
            self.reps = []
            self.length = 0

    def add(self, rep):
        self.reps.append(rep)
        self.length += 1

    def better(self, rep):
        return len(self.reps) == 0 or rep > self.reps[-1]


record = Streak()
current = Streak()
for rep in reps:
    if not current.better(rep):
        current = Streak(rep)
        continue
    current.add(rep)
    if current.length > record.length:
        record = current

print(sum(record.reps))
