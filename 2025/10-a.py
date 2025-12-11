#!/usr/bin/env python3
import re

# TEST_RESULT = 7
# REAL_RESULT = 488

result = 0

G = []
B = []

with open("./data/10-real.txt") as file:
    for line in file.readlines():
        line = re.sub(r"[\[\]\(\)]", "", line)
        parts = line.split()
        G.append(parts[0])
        bs = []
        for b in parts[1:-1]:
            bs.append(tuple([int(i) for i in b.split(",")]))
        B.append(bs)


for idx, g in enumerate(G):
    start = "." * len(g)
    seen = set([start])
    queue = [("." * len(g), 0)]
    while queue:
        p, i = queue.pop(0)
        for b in B[idx]:
            np = list(p)
            for n in b:
                np[n] = "." if np[n] == "#" else "#"
            np = "".join(np)
            if np in seen:
                continue
            if np == g:
                result += i + 1
                print(g, i + 1)
                queue = []
                break
            seen.add(np)
            queue.append((np, i + 1))

print(result)
