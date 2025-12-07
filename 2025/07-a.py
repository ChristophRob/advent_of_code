#!/usr/bin/env python3

# TEST_RESULT = 21
# REAL_RESULT = 1579
result = 0

N = []

with open("./data/07-real.txt") as file:
    for line in file.readlines():
        N.append(list(line.strip().replace("S", "|")))

for y, row in enumerate(N):
    for x, c in enumerate(row):
        if N[y - 1][x] == "|":
            if c == ".":
                N[y][x] = "|"
            if c == "^":
                result += 1
                N[y][x - 1] = "|"
                N[y][x + 1] = "|"


for row in N:
    print("".join(row))

print(result)
