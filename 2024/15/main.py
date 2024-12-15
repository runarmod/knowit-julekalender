tall_mapping = {
    "J": 10_000,
    "U": 5_000,
    "L": 1_000,
    "E": 500,
    "T": 100,
    "R": 50,
    "3": 10,
    "V": 5,
    "I": 1,
}


def getValueGruppe(rekke: list[str] | str, avsluttendeTall: str) -> int:
    s = 0
    finishers = []
    for i in range(len(rekke)):
        if tall_mapping[rekke[i]] >= tall_mapping[avsluttendeTall]:
            finishers.append(tall_mapping[rekke[i]])
            s += tall_mapping[rekke[i]]
        else:
            s -= tall_mapping[rekke[i]]
    s += tall_mapping[avsluttendeTall]
    return s, finishers


def getValue(alvetall: str) -> int:
    v = 0
    finishers = []
    rekke = []
    for c in alvetall:
        if not len(rekke):
            rekke = [c]
            continue
        if tall_mapping[rekke[-1]] < tall_mapping[c]:
            group_value, gruppe_finishers = getValueGruppe(rekke, c)
            finishers.extend(gruppe_finishers)
            finishers.append(tall_mapping[c])
            v += group_value
            rekke = []
        else:
            rekke.append(c)
    if len(rekke):
        finishers.extend(map(tall_mapping.get, rekke))
        v += sum(map(tall_mapping.get, rekke))

    if any(
        finisher1 < finisher2 for finisher1, finisher2 in zip(finishers, finishers[1:])
    ):
        return -1
    return v


# Testing
for alvetall, tall in (
    line.split(" = ") for line in open("eksempler.txt").read().strip().split("\n")
):
    tall = int(tall)
    value = getValue(alvetall)
    assert value == tall, f"Expected {tall}, but got {value} from {alvetall}"


print(max(map(getValue, open("transaksjoner.txt").read().strip().split("\n"))))
