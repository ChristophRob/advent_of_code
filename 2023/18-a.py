#!/usr/bin/env python3

# TEST_RESULT = 62
# REAL_RESULT = 53844

# This code is fairly inefficient. It uses a slow BFS approach
# to find everything outside the polygon. On top it also creates
# a GRID to make it display it in an Image for future reference.

from PIL import Image


DIRECTIONS = {
    "L": complex(0, -1),
    "R": complex(0, 1),
    "D": complex(1, 0),
    "U": complex(-1, 0),
}

point = complex(0, 0)
BORDER = []

with open("./data/18-real.txt") as file:
    for line in file.readlines():
        direction, length, _ = line.split()
        length = int(length)
        while length:
            length -= 1
            point += DIRECTIONS[direction]
            BORDER.append(point)


min_y = int(min(p.real for p in BORDER))
min_x = int(min(p.imag for p in BORDER))

BORDER = [p - complex(min_y, min_x) for p in BORDER]

height = int(max(p.real for p in BORDER)) + 1
width = int(max(p.imag for p in BORDER)) + 1


EMPTY = set()
GRID = []
for y in range(height):
    row = []
    for x in range(width):
        if complex(y, x) in BORDER:
            row.append("#")
        else:
            if y in (0, height - 1) or x in (0, width - 1):
                EMPTY.add(complex(y, x))
                row.append("x")
            else:
                row.append(".")
    GRID.append(row)


directions = [
    complex(1, 0),
    complex(0, 1),
    complex(-1, 0),
    complex(0, -1),
]

queue = list(EMPTY)
while queue:
    p = queue.pop(0)
    for d in DIRECTIONS.values():
        np = p + d
        if np in EMPTY or np in BORDER:
            continue
        elif not (0 <= np.real < height and 0 <= np.imag < width):
            continue
        EMPTY.add(np)
        queue.append(np)
        GRID[int(np.real)][int(np.imag)] = "x"


img = Image.new("RGB", (width, height), "black")
pixels = img.load()

for y, row in enumerate(GRID):
    for x in range(width):
        if GRID[y][x] == "x":
            pixels[x, y] = (255, 0, 255)  # Lila für außen
        if GRID[y][x] == "#":
            pixels[x, y] = (255, 255, 255)  # Weiß für Wände

img.show()

print(width * height - len(EMPTY))
