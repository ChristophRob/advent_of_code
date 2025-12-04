#!/usr/bin/env python3

# TEST_RESULT = 13
# REAL_RESULT = 1395
result = 0

G = []
DIRECTIONS = []
for y in [-1, 0, 1]:
    for x in [-1, 0, 1]:
        if (y, x) != (0, 0):
            DIRECTIONS.append((y, x))

with open("./data/04-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        L = []
        G.append(L)
        for c in line.strip():
            L.append(1 if c == "@" else 0)
    for y, L in enumerate(G):
        for x, p in enumerate(L):
            if p:
                papers_around = 0
                for dy, dx in DIRECTIONS:
                    iy, ix = (y + dy, x + dx)
                    if iy >= 0 and ix >= 0 and iy < len(G) and ix < len(L):
                        papers_around += G[iy][ix]
                if papers_around < 4:
                    result += 1

print(result)
