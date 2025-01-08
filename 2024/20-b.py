#!/usr/bin/env python3

# TEST_RESULT = 0
# REAL_RESULT = 1020244
from collections import deque

grid = []
costs = []
with open("./data/20-real.txt") as file:
    for line in file.readlines():
        grid.append(list(line.strip()))
        costs.append([None for _ in line.strip()])

for y, line in enumerate(grid):
    for x, v in enumerate(line):
        if v == "S":
            start = (y, x)

walls = []
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        if grid[y][x] == "#":
            walls.append((y, x))


queue = deque([(0, start[0], start[1])])
seen = []


while queue:
    cost, y, x = queue.popleft()
    costs[y][x] = cost
    seen.append((y, x))
    if grid[y][x] == "E":
        max_path = cost
        break
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = y + dy, x + dx
        if grid[ny][nx] == "#" and (ny, nx):
            continue
        if (ny, nx) in seen:
            continue
        seen.append((ny, nx))
        queue.append((cost + 1, ny, nx))

wins = {}
cheats = []
over_hundred = 0

RANGE = 20
other_wins = {}
for y_start, line in enumerate(grid):
    for x_start, v_start in enumerate(line):
        S = (y_start, x_start)
        if v_start not in [".", "S"]:
            continue
        for y_end, line_end in enumerate(grid):
            for x_end, v_end in enumerate(line_end):
                if v_end not in [".", "E"]:
                    continue
                diff = abs(y_start - y_end) + abs(x_start - x_end)
                cheat_value = costs[y_end][x_end] - costs[y_start][x_start] - diff
                if 0 < diff <= RANGE and cheat_value > 0:
                    if cheat_value not in other_wins:
                        other_wins[cheat_value] = 0
                    other_wins[cheat_value] += 1


counter = 0
new_other_wins = {}
for k, v in other_wins.items():
    if k >= 100:
        new_other_wins[k] = v
        counter += v
print(counter)
