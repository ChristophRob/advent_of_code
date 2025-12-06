#!/usr/bin/env python3

# TEST_RESULT = 6
# REAL_RESULT = 1637452029

result = 0

with open("./data/09-real.txt") as file:
    for line in file.readlines():
        ns = [int(i) for i in line.strip().split()]
        result += ns[-1]
        while True:
            diffs = []
            for i, n in enumerate(ns[:-1]):
                diffs.append(ns[i + 1] - ns[i])
            result += diffs[-1]
            if sum(diffs) == 0:
                break
            ns = diffs
print(result)
