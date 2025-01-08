#!/usr/bin/env python3

# TEST_RESULT = 0
# REAL_RESULT = 1402
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
    if grid[y][x] == "E":
        max_path = cost
        break
    seen.append((y, x))
    costs[y][x] = cost
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
for y, x in walls:
    for (y1, x1), (y2, x2) in [((1, 0), (-1, 0)), ((0, 1), (0, -1))]:
        if costs[y + y1][x + x1] is not None and costs[y + y2][x + x2] is not None:
            cheats.append((y, x))
            diff = abs(costs[y + y1][x + x1] - costs[y + y2][x + x2]) - 2
            if diff not in wins:
                wins[diff] = 0
            wins[diff] += 1
            if diff >= 100:
                over_hundred += 1

new_wins = {key: wins[key] for key in sorted(wins.keys())}

print(over_hundred)
