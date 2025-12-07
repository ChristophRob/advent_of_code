#!/usr/bin/env python3

# TEST_RESULT = 40
# REAL_RESULT = 13418215871354
result = 0

N = []

with open("./data/07-real.txt") as file:
    for line in file.readlines():
        N.append(list(line.strip().replace("S", "|")))

queue = []
COUNT = {}
for x, c in enumerate(N[0]):
    if c == "|":
        queue.append((0, x))
        COUNT[f"0,{x}"] = 1


def add_queue(y, x, c):
    key = f"{y},{x}"
    if key in COUNT:
        COUNT[key] += c
    else:
        COUNT[key] = c
        queue.append((y, x))


while queue:
    y, x = queue.pop(0)
    c = COUNT[f"{y},{x}"]
    if y >= len(N) - 1:
        result += c
        continue
    if N[y + 1][x] == ".":
        add_queue(y + 1, x, c)
    if N[y + 1][x] == "^":
        add_queue(y + 1, x - 1, c)
        add_queue(y + 1, x + 1, c)


print(result)
