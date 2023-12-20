import sympy
from tqdm import trange

s = 0
for i in trange(1, 100_000_000 + 1):
    n = sum(map(int, list(str(i))))
    if i / n == i // n:
        if sympy.isprime(i // n):
            s += 1
print(s)
# print(
#     sum(
#         i
#         if (abc :=  and sympy.isprime(i // abc))))
#     )
# )
