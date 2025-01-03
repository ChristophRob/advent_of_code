#!/usr/bin/env python3

# TEST_RESULT = 1206
# REAL_RESULT = 855082


with open("./data/12-real.txt") as file:
    INPUT = [list(line.strip()) for line in file.readlines()]

max_x = 0
max_y = 0
region_ids = [[0 for x in line] for line in INPUT]
REGION_ID = 1


def get_neighbours(x, y, plant, discount):
    neighbours = []
    # left fence
    if x > 0 and INPUT[y][x - 1] == plant:
        neighbours.append((x - 1, y))
    elif (
        discount
        and y > 0
        and INPUT[y - 1][x] == plant
        and (x == 0 or INPUT[y - 1][x - 1] != plant)
    ):
        neighbours.append((x - 1, y))
    # top fence
    if y > 0 and INPUT[y - 1][x] == plant:
        neighbours.append((x, y - 1))
    elif (
        discount
        and x > 0
        and INPUT[y][x - 1] == plant
        and (y == 0 or INPUT[y - 1][x - 1] != plant)
    ):
        neighbours.append((x, y - 1))
    # right fence
    if x < max_x and INPUT[y][x + 1] == plant:
        neighbours.append((x + 1, y))
    elif (
        discount
        and y > 0
        and INPUT[y - 1][x] == plant
        and (x == max_x or INPUT[y - 1][x + 1] != plant)
    ):
        neighbours.append((x + 1, y))
    # bottom fence
    if y < max_y and INPUT[y + 1][x] == plant:
        neighbours.append((x, y + 1))
    elif (
        discount
        and x > 0
        and INPUT[y][x - 1] == plant
        and (y == max_y or INPUT[y + 1][x - 1] != plant)
    ):
        neighbours.append((x, y + 1))
    return neighbours


def set_region(x, y, plant, region_id):
    global region_ids
    region_ids[y][x] = region_id
    for pos in get_neighbours(x, y, plant, False):
        if not region_ids[pos[1]][pos[0]]:
            set_region(pos[0], pos[1], plant, region_id)


max_y = len(INPUT) - 1
max_x = len(INPUT[0]) - 1
perimeters = []
for y, line in enumerate(INPUT):
    for x, plant in enumerate(line):
        perimeters.append((x, y, 4 - len(get_neighbours(x, y, plant, True))))
        if region_ids[y][x]:
            continue
        region_id = REGION_ID
        REGION_ID += 1
        set_region(x, y, plant, region_id)

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
