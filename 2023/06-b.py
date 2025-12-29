#!/usr/bin/env python3

# TEST_RESULT = 71503
# REAL_RESULT = 27363861

lines = []
with open("./data/06-real.txt") as file:
    for line in file.readlines():
        lines.append(int(line.replace(" ", "").split(":")[1]))

time = lines[0]
quick_start = 0
for t in range(1, time, 1000):
    if t * (time - t) > lines[1]:
        quick_start = t - 1000
        break

for t in range(quick_start, time):
    if t * (time - t) > lines[1]:
        break

result = (time // 2 - t) * 2 + 1
print(result)
