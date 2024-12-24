import string

with open("kryptert.txt", "rb") as f:
    kryptert = f.read()

passord = "Da-"

for s in string.printable:
    ukryptert = s
    for i in range(len(kryptert) - 1):
        ukryptert += chr(ord(ukryptert[-1]) ^ kryptert[i + 1])
    if "Da-" in ukryptert:
        print(
            next(word for word in ukryptert.split() if word.startswith("Da-")),
        )
        with open("dekryptert.txt", "w", encoding="utf-8") as f:
            f.write(ukryptert)
        break
