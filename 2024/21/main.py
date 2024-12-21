import json
import math
import re
from itertools import pairwise, permutations

import shapely
from haversine import haversine
from more_itertools import collapse, first
from tqdm import tqdm

with open("butikker.csv") as f:
    butikker = map(
        lambda x: (
            float(x[1]),
            float(x[0]),
            int(x[2]),
        ),  # Denne filen og geojson har byttet om på rekkefølgen av koordinater
        re.findall(r"(-?\d+\.\d+), (-?\d+\.\d+)\),(\d+)", f.read()),
    )


regions = []

min_x, min_y, max_x, max_y = float("inf"), float("inf"), -float("inf"), -float("inf")

with open("norge.geojson") as f:
    for region in json.load(f)["features"][0]["geometry"]["coordinates"]:
        poly = shapely.Polygon(collapse(region, levels=1))
        regions.append(poly)
        minx, miny, maxx, maxy = poly.bounds
        min_x = min(min_x, minx)
        min_y = min(min_y, miny)
        max_x = max(max_x, maxx)
        max_y = max(max_y, maxy)

butikker = filter(lambda x: x[2] > 0, butikker)  # Fjern butikker uten grøt
butikker = map(lambda x: x[:2], butikker)  # Trenger ikke bry oss om antall grøt lengre
butikker = filter(
    lambda x: min_x < x[0] < max_x and min_y < x[1] < max_y, butikker
)  # Fjern butikker (garantert) utenfor Norge


def is_inside_norway(point: tuple[float, float]):
    p = shapely.Point(point)
    return any(region.contains(p) for region in regions)


butikker = filter(is_inside_norway, butikker)  # Fjern butikker utenfor Norge
butikker = list(
    map(lambda x: x[::-1], butikker)
)  # Bytt tilbake til "riktig" rekkefølge av koordinater

start_node = (90.000, 0.000)


def find_distances(nodes):
    return {(a, b): haversine(a, b) for a in nodes for b in nodes if a != b}


def calculate_optimal_route(butikker, start_node):
    distances = find_distances(butikker + [start_node])

    best = {"distance": float("inf"), "orders": []}
    for butikk_rekkefolge in tqdm(
        permutations(butikker),
        total=math.factorial(len(butikker)),
        leave=False,
    ):
        butikk_rekkefolge = [start_node] + list(butikk_rekkefolge) + [start_node]
        total_distance = sum(map(distances.get, pairwise(butikk_rekkefolge)))
        if total_distance < best["distance"]:
            best["distance"] = total_distance
            best["orders"] = [butikk_rekkefolge]
        elif total_distance == best["distance"]:
            best["orders"].append(butikk_rekkefolge)
    return best


best = calculate_optimal_route(butikker, start_node)

# The best order is the order that first visits a latitiude with value < 0 (Jan Mayen)
best_order = first(
    sorted(
        best["orders"],
        key=lambda x: next(i for i, (_, v) in enumerate(x) if v < 0),
    )
)


def float_to_3_decimals(s):
    before, after = str(s).split(".")
    return f"{before}.{after[:3]:<03}"


print(
    ",".join(
        map(
            lambda x: f"({','.join(map(float_to_3_decimals, x))})",
            best_order,
        )
    )
)
