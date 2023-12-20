import re


inn = [eval(line) for line in open("input.txt", encoding="utf-8").readlines()]
alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

translations = []
for tran in inn:
    translation = {}
    for i, key in enumerate(alphabet):
        translation[key] = alphabet[tran[i]]
    for s in ",.\n ":
        translation[s] = s
    translations.append({v: k for k, v in translation.items()})

data = open("cypher.txt", encoding="utf-8").read()

d = list(re.findall(r"\w+,? ?\n?", data))

output = ""
for i, translation in enumerate(translations):
    output += "".join([translation[c] for c in d[i]])
print(output)
print("".join(line[0] for line in output.strip().split("\n")))
