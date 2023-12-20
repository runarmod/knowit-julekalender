a = 0
s = ""
for i in range(100_000):
    if str(i) not in s:
        s += str(i)
        a += 1
print(a)
