#!/usr/bin/env python3

# TEST_RESULT = 41
# REAL_RESULT = 5145

from itertools import cycle

with open("./data/06-real.txt") as file:
    INPUT = [list(line.strip()) for line in file.readlines()]


def find_starting_position():
    for y in range(len(INPUT)):
        for x in range(len(INPUT[0])):
            if INPUT[y][x] == "^":
                return (x, y)


(x, y) = find_starting_position()

orientations = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])

dx, dy = next(orientations)
while True:
    xNew, yNew = x + dx, y + dy
    if yNew < 0 or yNew > len(INPUT) - 1:
        break
    if xNew < 0 or xNew > len(INPUT[0]) - 1:
        break
    if INPUT[yNew][xNew] in [".", "X", "^"]:
        x, y = xNew, yNew
        INPUT[yNew][xNew] = "X"
    elif INPUT[yNew][xNew] == "#":
        dx, dy = next(orientations)

result = 0
for i in INPUT:
    for j in i:
        if j in ["X", "^"]:
            result += 1
print(result)
