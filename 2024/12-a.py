#!/usr/bin/env python3

# TEST_RESULT = 1930
# REAL_RESULT = 1433460


with open("./data/12-real.txt") as file:
    INPUT = [list(line.strip()) for line in file.readlines()]

region_ids = [[0 for x in line] for line in INPUT]
max_x = 0
max_y = 0
REGION_ID = 1


def get_neighbours(x, y, plant):
    new_neighbours = []
    for dy, dx in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        ny, nx = (y + dy, x + dx)
        if 0 <= ny <= max_y and 0 <= nx <= max_x and INPUT[ny][nx] == plant:
            new_neighbours.append((nx, ny))
    return new_neighbours


def set_region(x, y, plant, region_id):
    global region_ids
    region_ids[y][x] = region_id
    for px, py in get_neighbours(x, y, plant):
        if not region_ids[py][px]:
            set_region(px, py, plant, region_id)


max_y = len(INPUT) - 1
max_x = len(INPUT[0]) - 1
perimeters = []
for y, line in enumerate(INPUT):
    for x, plant in enumerate(line):
        perimeters.append((x, y, 4 - len(get_neighbours(x, y, plant))))
        if region_ids[y][x]:
            continue
        set_region(x, y, plant, REGION_ID)
        REGION_ID += 1

area_numbers = {}
for line in region_ids:
    for pos in line:
        if pos not in area_numbers:
            area_numbers[pos] = 0
        area_numbers[pos] += 1

result = 0
for x, y, perimeter in perimeters:
    region_id = region_ids[y][x]
    result += area_numbers[region_id] * perimeter

print(result)
