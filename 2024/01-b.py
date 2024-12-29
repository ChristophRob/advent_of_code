#!/usr/bin/env python3

# TEST_RESULT = 31
# REAL_RESULT = 25358365


X = []
Y = []
with open("./data/01-real.txt") as file:
    for line in file.readlines():
        x, y = [int(i) for i in line.strip().split(" ") if i]
        X.append(x)
        Y.append(y)


COUNTS = {}
for y in Y:
    if y not in COUNTS:
        COUNTS[y] = 0
    COUNTS[y] += 1

print(sum([x * COUNTS.get(x, 0) for x in X]))
