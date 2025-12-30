#!/usr/bin/env python3

# TEST_RESULT = 13
# REAL_RESULT = 26426

result = 0
with open("./data/04-real.txt") as file:
    for line in file.readlines():
        left, right = [
            [int(i) for i in s.split()] for s in line.strip().split(":")[1].split("|")
        ]
        if intersection := len(set(left).intersection(set(right))):
            result += 2 ** (intersection - 1)
print(result)
