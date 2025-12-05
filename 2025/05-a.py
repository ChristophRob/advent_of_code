#!/usr/bin/env python3

# TEST_RESULT = 3
# REAL_RESULT = 664
result = 0

RANGES = []
N = []

with open("./data/05-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if "-" in line:
            a, b = line.split("-")
            RANGES.append((int(a), int(b)))
        elif line:
            N.append(int(line))


for n in N:
    for ra, rb in RANGES:
        if n >= ra and n <= rb:
            result += 1
            break

print(result)
