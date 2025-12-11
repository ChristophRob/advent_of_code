#!/usr/bin/env python3

# TEST_RESULT = 5
# REAL_RESULT = 749

result = 0

D = {}

with open("./data/11-real.txt") as file:
    for line in file.readlines():
        a, b = line.strip().split(":")
        D[a] = b.strip().split()


queue = ["you"]

while queue:
    a = queue.pop(0)
    for b in D[a]:
        if b == "out":
            result += 1
            continue
        queue.append(b)


print(result)
