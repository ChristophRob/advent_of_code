#!/usr/bin/env python3

# TEST_RESULT = 9021
# REAL_RESULT = 1468005

WIDER_GRID = {
    "@": "@.",
    "#": "##",
    ".": "..",
    "O": "[]",
}


with open("./data/15-real.txt") as file:
    raw = [line.strip() for line in file.readlines() if line.strip()]
    GRID = []
    INPUTS = ""
    for line in raw:
        if "#" in line:
            GRID.append(list("".join([WIDER_GRID[c] for c in line])))
        else:
            INPUTS += line


DIRECTION = {
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
    "^": (0, -1),
}


class CantMoveBox(Exception):
    pass


class Box(object):
    def __init__(self, id, xl, y):
        self.xl = xl
        self.xr = xl + 1
        self.y = y
        self.id = id
        GRID[y][xl] = id
        GRID[y][self.xr] = id

    def check_move(self, dx, dy):
        next_vs = []
        if self.xl + dx != self.xr:
            next_vs.append(GRID[self.y + dy][self.xl + dx])
        if self.xr + dx != self.xl:
            next_vs.append(GRID[self.y + dy][self.xr + dx])
        for next_v in next_vs:
            if next_v == ".":
                pass
            elif next_v == "#":
                raise CantMoveBox()
            else:
                box = boxes[next_v]
                box.check_move(dx, dy)

    def move(self, dx, dy):
        if dx == 0:
            self.move_vertical(dx, dy)
        else:
            self.move_horizontal(dx, dy)
        self.xl += dx
        self.xr += dx
        self.y += dy
        GRID[self.y - dy][self.xl - dx] = "."
        GRID[self.y - dy][self.xr - dx] = "."
        GRID[self.y][self.xl] = self.id
        GRID[self.y][self.xr] = self.id

    def move_vertical(self, dx, dy):
        for x in [self.xl + dx, self.xr + dx]:
            next_v = GRID[self.y + dy][x]
            if next_v != ".":
                box = boxes[next_v]
                box.move(dx, dy)

    def move_horizontal(self, dx, dy):
        x = self.xr if dx > 0 else self.xl
        next_v = GRID[self.y + dy][x + dx]
        if next_v != ".":
            box = boxes[next_v]
            box.move(dx, dy)

    def calc_value(self):
        return 100 * self.y + self.xl


boxes = {}
i = 1
for y, line in enumerate(GRID):
    for x, v in enumerate(line):
        if v == "[":
            boxes[str(i)] = Box(str(i), x, y)
            i += 1


for y, line in enumerate(GRID):
    for x, v in enumerate(line):
        if v == "@":
            break
    else:
        continue
    break

for n in INPUTS:
    dx, dy = DIRECTION[n]
    if GRID[y + dy][x + dx] == "#":
        continue
    if GRID[y + dy][x + dx] == ".":
        pass
    else:
        box = boxes[GRID[y + dy][x + dx]]
        try:
            box.check_move(dx, dy)
            box.move(dx, dy)
        except CantMoveBox:
            continue
    GRID[y + dy][x + dx] = "@"
    GRID[y][x] = "."
    x, y = x + dx, y + dy

result = sum([box.calc_value() for box in boxes.values()])
print(result)
