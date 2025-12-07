#!/usr/bin/env python3

# TEST_RESULT = 1030
# REAL_RESULT = 857986849428

M = []
G = []

er = []
ec = []

expand = 1000000

# Set up grid
with open("./data/11-real.txt") as file:
    for line in file.readlines():
        line = list(line.strip())
        M.append(line)


# Find galaxies and empty rows/ columns
for y, row in enumerate(M):
    if "#" not in row:
        er.append(y)
    else:
        for x, c in enumerate(row):
            if c == "#":
                G.append((y, x))

for x in range(len(M[0])):
    for row in M:
        if row[x] == "#":
            break
    else:
        ec.append(x)

result = 0
for idx, g1 in enumerate(G):
    for g2 in G[idx + 1 :]:
        y1, x1 = g1
        y2, x2 = g2
        # Add diff without expansion
        result += abs(y1 - y2) + abs(x1 - x2)
        # Add expansion
        for ye in er:
            if min(y1, y2) < ye and max(y1, y2) > ye:
                result += expand - 1
        for xe in ec:
            if min(x1, x2) < xe and max(x1, x2) > xe:
                result += expand - 1

print(result)
