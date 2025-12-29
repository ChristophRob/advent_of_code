#!/usr/bin/env python3

# TEST_RESULT = 288
# REAL_RESULT = 771628

lines = []
with open("./data/06-real.txt") as file:
    for line in file.readlines():
        lines.append([int(i) for i in line.split()[1:]])

result = 1
for idx, time in enumerate(lines[0]):
    ways = sum([1 for t in range(time) if t * (time - t) > lines[1][idx]])
    result *= ways

print(result)
