#!/usr/bin/env python3

# TEST_RESULT = 6,1
# REAL_RESULT = 36,17

from collections import deque

INPUT = []

with open("./data/18-test.txt") as file:
    for line in file.readlines():
        INPUT.append(tuple([int(i) for i in line.strip().split(",") if i]))

CLOCKWISE_ORDER = [(1, 0), (0, 1), (-1, 0), (0, -1)]
max_xy = 70 if len(INPUT) > 30 else 6


def calc(max_walls):
    WALLS = set(INPUT[:max_walls])
    BEST = [[None for _ in range(max_xy + 1)] for y in range(max_xy + 1)]

    POSITIONS = deque([(0, 0, 0)])
    while POSITIONS:
        x, y, value = POSITIONS.popleft()
        for dx, dy in CLOCKWISE_ORDER:
            new_value = value + 1
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > max_xy or ny < 0 or ny > max_xy:
                continue
            elif (nx, ny) in WALLS:
                continue
            elif (nx, ny) == (max_xy, max_xy):
                return True
            existing_pos = BEST[ny][nx]
            if existing_pos is None or existing_pos > new_value:
                BEST[ny][nx] = new_value
                POSITIONS.append((nx, ny, new_value))


max_value = len(INPUT)
min_value = 1
while min_value + 1 < max_value:
    middle = (max_value + min_value) // 2
    result = calc(middle)
    if result:
        min_value = middle
    else:
        max_value = middle
print(",".join([str(i) for i in list(INPUT[min_value])]))
