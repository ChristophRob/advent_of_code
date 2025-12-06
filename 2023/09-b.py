#!/usr/bin/env python3

# TEST_RESULT = 6
# REAL_RESULT = 908

result = 0

with open("./data/09-real.txt") as file:
    for line in file.readlines():
        ns = [int(i) for i in line.strip().split()]
        N = [ns[0]]
        while True:
            diffs = []
            for i, n in enumerate(ns[:-1]):
                diffs.append(ns[i + 1] - ns[i])
            N.append(diffs[0])
            if sum(diffs) == 0:
                break
            ns = diffs

        x = 0
        for i in N[::-1]:
            x = i - x
        result += x

print(result)
