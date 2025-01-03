#!/usr/bin/env python3

# TEST_RESULT = 36
# REAL_RESULT = 822


with open("./data/10-real.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    INPUT = []
    for line in lines:
        INPUT.append([int(i) for i in line])


def go_step(i, y, x):
    results = []
    if INPUT[y][x] == i:
        if i == 9:
            results.append((y, x))
        else:
            next_pos = [
                (y + dy, x + dx)
                for dy, dx in [(0, -1), (1, 0), (0, 1), (-1, 0)]
                if all([0 <= y + dy <= max_y, 0 <= x + dx <= max_x])
            ]
            for next_y, next_x in next_pos:
                results.extend(go_step(i + 1, next_y, next_x))

        if i == 0:
            results = list(set(results))
    return results


max_y = len(INPUT) - 1
max_x = len(INPUT[0]) - 1
results = []
for y, line in enumerate(INPUT):
    for x, v in enumerate(line):
        results.extend(go_step(0, y, x))

print(len(results))
