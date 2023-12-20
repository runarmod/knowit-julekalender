rekke = eval(open("rekke.txt").read())
mynter = [1 for _ in range(len(rekke))]

updated = True
while updated:
    updated = False
    for curr in range(len(mynter)):
        for other in range(max(0, curr - 2), min(len(mynter), curr + 3)):
            if rekke[curr] > rekke[other] and mynter[curr] < mynter[other] + 1:
                updated = mynter[curr] = mynter[other] + 1
            elif rekke[curr] == rekke[other] and mynter[curr] != mynter[other]:
                updated = mynter[other] = mynter[curr] = max(
                    mynter[curr], mynter[other]
                )
print("Gullmynter:", sum(mynter))
