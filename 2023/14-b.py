#!/usr/bin/env python3

import numpy

# TEST_RESULT = 64
# REAL_RESULT = 91286

result = 0
G = []

with open("./data/14-real.txt") as file:
    for line in file.readlines():
        G.append(list(line.strip()))

G = numpy.transpose(G)
prev_keys = []
si = 1000000000
i = si
while i:
    i -= 1

    # Check reoccurance
    new_key = "".join(["".join(row) for row in G])
    try:
        prev_i = prev_keys.index(new_key)
        difference = (si - i - 1) - prev_i
        i = i % difference
    except ValueError:
        prev_keys.append(new_key)

    # One Cycle
    for _ in range(4):
        for row in G:
            current_index = 0
            for y, p in enumerate(row):
                if p == "O":
                    if current_index != y:
                        row[current_index] = "O"
                        row[y] = "."
                    current_index += 1
                    pass
                elif p == ".":
                    pass
                elif p == "#":
                    current_index = y + 1
        G = numpy.rot90(G)

max_value = len(G[0])
for row in G:
    for y, p in enumerate(row):
        if p == "O":
            result += max_value - y

G = numpy.transpose(G)

print(result)
