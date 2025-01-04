#!/usr/bin/env python3

# TEST_RESULT = NA
# REAL_RESULT = 7138


with open("./data/14-real.txt") as file:
    INPUT = [line.strip() for line in file.readlines()]

WIDE = 101
TALL = 103
MIN_IN_LINE = 7

robots = []
for line in INPUT:
    px, py = [int(i) for i in line.split("=")[1].split(" ")[0].split(",")]
    vx, vy = [int(i) for i in line.split("=")[2].split(",")]
    robots.append((px, py, vx, vy))


for seconds in range(WIDE * TALL):
    positions = []
    for px, py, vx, vy in robots:
        x = (px + seconds * vx) % WIDE
        y = (py + seconds * vy) % TALL
        positions.append((x, y))

    ordered = sorted(list(set(positions)), key=lambda x: (x[1], x[0]))
    for i, (x, y) in enumerate(ordered[:-MIN_IN_LINE]):
        cx, cy = ordered[i + MIN_IN_LINE]
        if x + MIN_IN_LINE == cx and y == cy:
            print(seconds)
            break
