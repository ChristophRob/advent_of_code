#!/usr/bin/env python3
from itertools import cycle

# TEST_RESULT = 6
# REAL_RESULT = 20777

M = {}

dirs = None
with open("./data/08-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if not line:
            continue
        if not dirs:
            dirs = line
            continue
        a, r = line.split("=")
        b, c = r.replace(" ", "").split(",")
        M[a.strip()] = (b.replace("(", ""), c.replace(")", ""))

c = "AAA"
for idx, d in enumerate(cycle(dirs)):
    i = 0 if d == "L" else 1
    c = M[c][i]
    if c == "ZZZ":
        break


print(idx + 1)
