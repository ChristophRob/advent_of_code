#!/usr/bin/env python3

# TEST_RESULT = 6
# REAL_RESULT = 1523
from itertools import cycle
import json

with open("./data/06-real.txt") as file:
    INPUT = [list(line.strip()) for line in file.readlines()]


def find_starting_position(input):
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == "^":
                return (x, y)


def check_input(input, x, y):
    orientations = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])

    dx, dy = next(orientations)
    seen = set([])
    while True:
        xNew, yNew = x + dx, y + dy
        if (xNew, yNew, dx, dy) in seen:
            return True
        seen.add((xNew, yNew, dx, dy))
        if yNew < 0 or yNew > len(input) - 1:
            return False
        if xNew < 0 or xNew > len(input[0]) - 1:
            return False
        if input[yNew][xNew] in [".", "X", "^"]:
            x, y = xNew, yNew
            input[yNew][xNew] = "X"
        elif input[yNew][xNew] == "#":
            dx, dy = next(orientations)


(xs, ys) = find_starting_position(INPUT)
result = 0
for y in range(len(INPUT)):
    for x in range(len(INPUT[0])):
        if INPUT[y][x] == ".":
            new_input = json.loads(json.dumps(INPUT))
            new_input[y][x] = "#"
            if check_input(new_input, xs, ys):
                result += 1
print(result)
