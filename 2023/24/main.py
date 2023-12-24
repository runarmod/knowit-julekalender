print(
    "".join(
        [
            tittel[0]
            for tittel, pris, hash in (
                line.split(";")
                for line in open("transaksjoner.txt", encoding="utf-8")
                .read()
                .strip()
                .split("\n")
            )
            if int(hash)
            != (
                sum(
                    bokstaver.index(c) + 1
                    for c in tittel.lower()
                    if c in (bokstaver := "abcdefghijklmnopqrstuvwxyzæøå")
                )
                * int(pris)
            )
            % 0xBEEF
        ]
    )
)
