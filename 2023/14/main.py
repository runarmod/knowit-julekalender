import re


pushups = list(map(int, re.findall(r"\d+", open("push.txt").read())))
# pushups = [16, 3, 1, 2, 9, 8, 12, 14, 19, 21, 20, 11, 2, 4, 3, 1, 7, 9]

record = 0
record_sum = 0

for i in range(len(pushups)):
    if i == len(pushups) - 1 or pushups[i] > pushups[i + 1]:
        continue
    stig = True
    curr_streak = 1
    curr_streak_sum = pushups[i]
    for j in range(i + 1, len(pushups)):
        if not stig and not pushups[j] < pushups[j - 1]:
            break
        if stig and not pushups[j] > pushups[j - 1]:
            stig = False
        curr_streak += 1
        curr_streak_sum += pushups[j]

    if curr_streak > record:
        record = curr_streak
        record_sum = curr_streak_sum
print(f"{record=} {record_sum=}")
