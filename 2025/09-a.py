#!/usr/bin/env python3

# TEST_RESULT = 50
# REAL_RESULT = 4748985168


N = []
A = []

with open("./data/09-real.txt") as file:
    for line in file.readlines():
        x1, y1 = [int(i) for i in line.split(",")]
        for x2, y2 in N:
            A.append(abs((x2 - x1 + 1) * (y2 - y1 + 1)))
        N.append((x1, y1))

print(max(A))
