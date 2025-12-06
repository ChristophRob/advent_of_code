#!/usr/bin/env python3

# TEST_RESULT = 8
# REAL_RESULT = 6860

M = []

N, W, S, E = "N", "W", "S", "E"

D = {
    N: (-1, 0),
    W: (0, -1),
    S: (1, 0),
    E: (0, 1),
}


VALID = {
    "-": (W, E),
    "|": (N, S),
    "F": (S, E),
    "7": (S, W),
    "J": (N, W),
    "L": (N, E),
}

D_VALID = {
    N: "|F7S",
    E: "-7JS",
    W: "-LFS",
    S: "|JLS",
}

OPPOSITE = {
    N: S,
    S: N,
    W: E,
    E: W,
}

S = None

# Set up grid
with open("./data/10-real.txt") as file:
    for line in file.readlines():
        M.append([p for p in line.strip()])

# Get Start Position
for y, row in enumerate(M):
    for x, p in enumerate(row):
        if p == "S":
            S = (y, x)
            break

# Get first direction
for d, (yd, xd) in D.items():
    ys, xs = S
    if M[ys + yd][xs + xd] in D_VALID[d]:
        old_d = d
        break

# Pathfinding
p = (S[0] + D[old_d][0], S[1] + D[old_d][1])
seen = [S, p]
while True:
    y, x = p
    od = OPPOSITE[old_d]

    d = [d for d in VALID[M[y][x]] if d != od][0]
    old_d = d
    yd, xd = D[d]
    p = (y + yd, x + xd)
    seen.append(p)
    if p == S:
        break


print(len(seen) // 2)
