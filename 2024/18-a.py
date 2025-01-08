#!/usr/bin/env python3

# TEST_RESULT = 22
# REAL_RESULT = 354

from collections import deque

INPUT = []
with open("./data/18-real.txt") as file:
    for line in file.readlines():
        INPUT.append(tuple([int(i) for i in line.strip().split(",") if i]))

max_xy, max_walls = (70, 1024) if len(INPUT) > 30 else (6, 12)

CLOCKWISE_ORDER = [(1, 0), (0, 1), (-1, 0), (0, -1)]
WALLS = set(INPUT[:max_walls])
BEST = [[None for _ in range(max_xy + 1)] for y in range(max_xy + 1)]

RESULTS = []
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
            RESULTS.append(new_value)

        existing_pos = BEST[ny][nx]
        if existing_pos is None or existing_pos > new_value:
            BEST[ny][nx] = new_value
            POSITIONS.append((nx, ny, new_value))
print(min(RESULTS))
