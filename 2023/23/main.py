COORDS = [
    tuple(map(lambda x: int(x.replace(".", "").ljust(8, "0")), line.split()))
    for line in open("gateadresser_oslo_koordinater_liten.txt")
    .read()
    .strip()
    .split("\n")
]


class Direction:
    NORTH, EAST, SOUTH, WEST = range(4)


def always_north(coords, time, prev_dir):
    return get_north(coords), Direction.NORTH


def outwards(coords, time, prev_dir):
    match time % 4:
        case 0:
            return get_north(coords), Direction.NORTH
        case 1:
            return get_east(coords), Direction.EAST
        case 2:
            return get_south(coords), Direction.SOUTH
        case 3:
            return get_west(coords), Direction.WEST


def complicated(coords, time, prev_dir):
    if len(coords) % 5 == 0:
        match prev_dir:
            case Direction.NORTH:
                return get_north(coords), Direction.NORTH
            case Direction.EAST:
                return get_east(coords), Direction.EAST
            case Direction.SOUTH:
                return get_south(coords), Direction.SOUTH
            case Direction.WEST:
                return get_west(coords), Direction.WEST
        assert False
    if len(coords) % 2 == 0:
        match prev_dir:
            case Direction.NORTH:
                return get_west(coords), Direction.WEST
            case Direction.WEST:
                return get_south(coords), Direction.SOUTH
            case Direction.SOUTH:
                return get_east(coords), Direction.EAST
            case Direction.EAST:
                return get_north(coords), Direction.NORTH
        assert False

    match prev_dir:
        case Direction.NORTH:
            return get_east(coords), Direction.EAST
        case Direction.EAST:
            return get_south(coords), Direction.SOUTH
        case Direction.SOUTH:
            return get_west(coords), Direction.WEST
        case Direction.WEST:
            return get_north(coords), Direction.NORTH
    assert False


def get_west(coords):
    return min(coords, key=lambda coord: (coord.east, -coord.north))


def get_south(coords):
    return min(coords, key=lambda coord: (coord.north, coord.east))


def get_east(coords):
    return min(coords, key=lambda coord: (-coord.east, coord.north))


def get_north(coords):
    return min(coords, key=lambda coord: (-coord.north, -coord.east))


class Coord:
    def __init__(self, north, east):
        self.north = north
        self.east = east

    def distance(self, other):
        return (
            ((self.east - other.east) ** 2 + (self.north - other.north) ** 2) ** 0.5
            * 55_500
            / 10**6
        )

    def __repr__(self):
        return f"N{str(self.north)[:2]}.{str(self.north)[2:]} E{str(self.east)[:2]}.{str(self.east)[2:]}"


best = float("inf")
for base_r, reload_time, koefficient in [
    (2_000, 62, 0.10),
    (1_000, 22, 0.05),
    (500, 16, 0.002),
]:
    less_each_time = base_r * koefficient
    print(f"{base_r=}, {reload_time=}, {koefficient=}")
    radiuses = set()
    for get_coord_fun in (always_north, outwards, complicated):
        radius = base_r
        time = 0
        coords = {Coord(north, east) for north, east in COORDS}
        current_direction = Direction.NORTH
        print("\t" + get_coord_fun.__name__)
        i = 0
        while coords:
            i += 1
            coord, current_direction = get_coord_fun(coords, i, current_direction)
            removable = set()
            for coord2 in coords:
                if coord.distance(coord2) <= radius:
                    removable.add(coord2)
            for coord2 in removable:
                coords.remove(coord2)
            time += reload_time
            radius = round(max(base_r * 0.2, base_r - less_each_time * i))
        time -= reload_time
        print("\t\tTime:", time)
        best = min(best, time)

assert best == 21312, f"{best} is wrong"

print("Best:", best)
