counter = [100_000] * 10

order = []
iteration = 0
while any(count > 0 for count in counter):
    iteration += 1
    for i in range(9, -1, -1):
        count = counter[i]
        counter[i] = max(0, counter[i] - 1)
        for c in map(int, str(count)):
            counter[c] = max(0, counter[c] - 1)
            if counter[c] == 0 and c not in order:
                order.append(c)

print(iteration, ",".join(map(str, order)))
