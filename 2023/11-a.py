#!/usr/bin/env python3
import numpy

# TEST_RESULT = 374
# REAL_RESULT = 9565386

M = []

# Set up grid
with open("./data/11-real.txt") as file:
    for line in file.readlines():
        line = list(line.strip())
        M.append(line)
        # Expand universe 1.st time
        if "#" not in line:
            M.append(line)

# Expand universe further
M = numpy.transpose(M)
nM = []
for row in M:
    nM.append(row)
    if "#" not in row:
        nM.append(row)
M = numpy.transpose(nM)

# Find galaxies
G = []
for y, row in enumerate(M):
    for x, c in enumerate(row):
        if c == "#":
            G.append((y, x))

# Get distance between all galaxies
result = 0
for idx, g1 in enumerate(G):
    for g2 in G[idx + 1 :]:
        result += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

print(result)
