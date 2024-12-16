sviller = set()
jord = set()
grus = set()
sand = set()

with open("el-paso_santa-cruz.txt") as f:
    ss, us = f.read().strip("\n").split("\n")


length = len(ss)
assert len(ss) == len(us)

for i, (s, u) in enumerate(zip(ss, us)):
    if s == "*":
        sviller.add(i)
    match u:
        case "j":
            jord.add(i)
        case "g":
            grus.add(i)
        case "s":
            sand.add(i)
        case _:
            raise ValueError("Unknown soil type")

offsets = {
    "ben": range(0, 10),
    "rumpe": range(10, 13),
    "overkropp": range(13, 22),
    "nakke": range(22, 24),
    "hode": range(24, 29),
}
alv_size = offsets["hode"].stop


def valid(leg_i):
    # Dersom hele underlaget er jord og det ikke er noen sviller kan han fint sove der også.
    if all(leg_i + i in jord and leg_i + i not in sviller for i in range(alv_size)):
        return True

    # Han vil ha minst én sville som pute under hodet.
    if not any(leg_i + i in sviller for i in offsets["hode"]):
        return False

    # Han liker ikke å ha noe trykkende på nakken, ingen sviller der.
    if any(leg_i + i in sviller for i in offsets["nakke"]):
        return False

    # Selvfølgelig liker han heller ikke sand i nakken!
    if any(leg_i + i in sand for i in offsets["nakke"]):
        return False

    # Han kan ha opp til én sville under bena som støtte.
    if sum(leg_i + i in sviller for i in offsets["ben"]) > 1:
        return False

    # Han liker ikke grus! Det kan ikke være grus på noen del av underlaget, også under sviller.
    if any(leg_i + i in grus for i in range(alv_size)):
        return False

    return True


print(sum(map(valid, range(length - alv_size))))
