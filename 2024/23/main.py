import matplotlib.pyplot as plt

plt.scatter(*zip(*map(lambda s: map(float, s.split()), open("lekescan.txt").readlines())))
plt.savefig("solution.png")
print("SYKKEL")
