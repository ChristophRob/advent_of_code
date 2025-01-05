#!/usr/bin/env python3

# TEST_RESULT = 10092
# REAL_RESULT = 1476771

with open("./data/15-real.txt") as file:
    raw = [line.strip() for line in file.readlines() if line.strip()]
    GRID = []
    INPUTS = ""
    for line in raw:
        if "#" in line:
            GRID.append(list(line))
        else:
            INPUTS += line


DIRECTION = {
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
    "^": (0, -1),
}


for y, line in enumerate(GRID):
    for x, v in enumerate(line):
        if v == "@":
            break
    else:
        continue
    break

for n in INPUTS:
    dx, dy = DIRECTION[n]
    move = False
    if GRID[y + dy][x + dx] == ".":
        move = True
    if GRID[y + dy][x + dx] == "O":
        i = 2
        while GRID[y + i * dy][x + i * dx] != "#":
            if GRID[y + i * dy][x + i * dx] == ".":
                GRID[y + i * dy][x + i * dx] = "O"
                move = True
                break
            i += 1
    if move:
        GRID[y + dy][x + dx] = "@"
        GRID[y][x] = "."
        x, y = x + dx, y + dy

result = 0
for y, line in enumerate(GRID):
    for x, v in enumerate(line):
        if v == "O":
            result += 100 * y + x
print(result)
