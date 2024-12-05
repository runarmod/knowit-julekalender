import re


kandidater = {
    nr: {"navn": navn, "parti": parti, "valg_nisser": 0}
    for nr, navn, parti in re.findall(
        r"(k\d+) - (.*) - (.*)", open("kandidater.txt", encoding="utf-8").read()
    )
}


stater = {
    nr: {
        "navn": navn,
        "valg_nisser": int(valg_nisser),
        "test": valg_nisser,
        "kandidat_stemmer": {
            kandidat_nr: int(stemmer)
            for kandidat_nr, stemmer in re.findall(r"(k\d+): (\d+)", kandidat_stemmer)
        },
    }
    for nr, navn, valg_nisser, kandidat_stemmer in re.findall(
        r"(s\d+) - (.*) - (\d+) - (.*)", open("stater.txt", encoding="utf-8").read()
    )
}

for state_nr, state in stater.items():
    valg_nisser = state["valg_nisser"]
    tot_stemmer_stat = sum(state["kandidat_stemmer"].values())
    kandidat_valgnisser = {
        kandidat: stemmer / tot_stemmer_stat * valg_nisser
        for kandidat, stemmer in state["kandidat_stemmer"].items()
    }
    for kandidat, andel in kandidat_valgnisser.items():
        kandidater[kandidat]["valg_nisser"] += int(andel)
        kandidat_valgnisser[kandidat] = andel % 1
        valg_nisser -= int(andel)

    for kandidat in sorted(
        kandidat_valgnisser, key=lambda x: kandidat_valgnisser[x], reverse=True
    )[:valg_nisser]:
        kandidater[kandidat]["valg_nisser"] += 1

vinner = max(kandidater, key=lambda x: kandidater[x]["valg_nisser"])
print(f"{kandidater[vinner]['navn']} - {kandidater[vinner]['valg_nisser']}")
