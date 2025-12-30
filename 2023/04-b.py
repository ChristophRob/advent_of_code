#!/usr/bin/env python3

from collections import defaultdict

# TEST_RESULT = 30
# REAL_RESULT = 6227972


result = 0

copies = defaultdict(int)

with open("./data/04-real.txt") as file:
    for idx, line in enumerate(file.readlines()):
        left, right = [
            [int(i) for i in s.split()] for s in line.strip().split(":")[1].split("|")
        ]
        if intersection := len(set(left).intersection(set(right))):
            for i in range(intersection):
                copies[i + idx + 1] += copies[idx] + 1
        result += copies[idx] + 1
print(result)
