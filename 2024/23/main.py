import matplotlib.pyplot as plt


plt.scatter(
    *zip(
        *[
            list(map(float, line.split(" ")))
            for line in open("lekescan.txt").read().splitlines()
        ]
    )
)
plt.show()
