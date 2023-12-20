from PIL import Image
from pprint import pprint
from scipy.integrate import quad
from scipy.optimize import fsolve
import io
import itertools
import matplotlib.pyplot as plt
import numpy as np
import re

from tqdm import tqdm

lines = [
    (
        list(map(float, line.split(": ")[0][1:-1].split(" "))),
        list(
            itertools.batched(
                map(float, re.findall(r"(\d+\.\d+)", line.split(": ")[1])), n=3
            )
        ),
    )
    for line in open("input.txt").read().strip().split("\n")[1:]
]


def integrand(x):
    global a, b, c
    # Bue lengde er integralet fra 0 til x av sqrt(1 + f'(x)^2) dx
    # For en andregradsfunksjon er f'(x) = 2ax + b
    return np.sqrt(1 + (2 * a * x + b) ** 2)


def func(x):
    y, *_ = quad(integrand, 0, x)
    return y


def optimize_for_x(pos, start=0):
    return fsolve(lambda x: func(x) - pos, start)[0]


for line in tqdm(lines):
    a, b, c = line[0]
    for pos, intensity, radius in line[1]:
        x = optimize_for_x(pos, start=1)
        y = a * x**2 + b * x + c
        plt.scatter([x], [y], s=[radius], color=[intensity] * 3)

# plt.show()


def fig2img(fig):
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img


img = fig2img(plt.gcf())
img.save("output.png")
