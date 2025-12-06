#!/usr/bin/env python3
from itertools import cycle
import math

# TEST_RESULT = 6
# REAL_RESULT = 13289612809129

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

pos = []
for c in M.keys():
    if c[-1] == "A":
        pos.append(c)

intervalls = []
for cs in pos:
    c = cs
    for idx, d in enumerate(cycle(dirs)):
        i = 0 if d == "L" else 1
        c = M[c][i]
        if c[-1] == "Z":
            break
    intervalls.append(idx + 1)

print(math.lcm(*intervalls))
