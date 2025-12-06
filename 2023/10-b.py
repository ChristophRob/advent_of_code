#!/usr/bin/env python3

# TEST_RESULT = 8
# REAL_RESULT = 343

M = []

N, W, S, E = "N", "W", "S", "E"

D = {
    W: (0, -1),
    N: (-1, 0),
    E: (0, 1),
    S: (1, 0),
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

BIG_M = {
    "-": ["...", "---", "..."],
    "|": [".|.", ".|.", ".|."],
    "F": ["...", ".F-", ".|."],
    "7": ["...", "-7.", ".|."],
    "J": [".|.", "-J.", "..."],
    "L": [".|.", ".L-", "..."],
    ".": ["...", "...", "..."],
    " ": ["   ", "   ", "   "],
    "S": [".|.", "-S-", ".|."],
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

# Remove everything not on the path
for y, row in enumerate(M):
    for x, p in enumerate(row):
        if (y, x) not in seen:
            M[y][x] = "."


# Create bigger Grid to see gaps
bM = []
for y, row in enumerate(M):
    a, b, c = [], [], []
    for x, p in enumerate(row):
        ad, bd, cd = BIG_M[p]
        a.extend(ad)
        b.extend(bd)
        c.extend(cd)
    bM.extend([a, b, c])

# Remove outer ring to get starting points
for y in [0, -1]:
    for x, p in enumerate(bM[y]):
        if p == ".":
            bM[y][x] = " "
for y, row in enumerate(bM):
    for x in [0, -1]:
        if row[x] == ".":
            row[x] = " "

# Remove all dots adjacent to spaces
changed = True
while changed:
    changed = False
    for y, row in enumerate(bM):
        for x, p in enumerate(row):
            if p == ".":
                for dy, dx in D.values():
                    if bM[y + dy][x + dx] == " ":
                        bM[y][x] = " "
                        changed = True
                        break

# Count only dots at original positions
result = 0
for y in range(1, len(bM), 3):
    old_y = []
    for x in range(1, len(bM[y]), 3):
        if bM[y][x] == ".":
            result += 1
        old_y.append(bM[y][x])


print(result)
