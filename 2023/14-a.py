#!/usr/bin/env python3

import numpy

# TEST_RESULT = 136
# REAL_RESULT = 105784

result = 0
G = []

with open("./data/14-test.txt") as file:
    for line in file.readlines():
        G.append(list(line.strip()))


G = numpy.transpose(G)

max_value = len(G[0])
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

    for y, p in enumerate(row):
        if p == "O":
            result += max_value - y

print(result)
print(len(G), len(G[0]))
