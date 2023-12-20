import re


test = False

filename = None if test else "log.txt"

with open(filename, encoding="utf8") as f:
    matches = re.findall(r"(kl[ai]kk) på (\d+)", f.read().strip())

state = {}


def reset_state():
    global state
    state = {str(i): "klakk" for i in range(1, 8)}


reset_state()
done = 0
for sound, num in matches:
    state[num] = sound
    if all(v == "klikk" for v in state.values()):
        done += 1
        reset_state()
print(f"Answer: {done}")
