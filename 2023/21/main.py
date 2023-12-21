print(
    sum(
        1
        for line in open("kredittkort.txt").read().strip().split("\n")
        if not (
            lambda card: (
                24
                - (
                    sum(
                        [
                            c * 2 if not i % 2 else c
                            for i, c in enumerate(map(int, list(card[:-2])))
                        ]
                    )
                    % 24
                )
            )
            % 24
            == int(card[-2:])
        )(line)
    )
)
