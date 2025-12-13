#!/usr/bin/env python3
import math

# TEST_RESULT = 2
# REAL_RESULT = 420257875695750

result = 0

D = {}

with open("./data/11-real.txt") as file:
    for line in file.readlines():
        a, b = line.strip().split(":")
        D[a] = b.strip().split()

# Only one WAY can work otherwise there would be
# an endless loop. So we just tried out both ways
# and took the one that worked
WAY1 = ("svr", "dac", "fft", "out")
WAY2 = ("svr", "fft", "dac", "out")
WAYA = ("you", "out")  # first part still works

w = WAY2
w_result = []
for idx, s in enumerate(w[:-1]):
    g = w[idx + 1]
    p_result = 0
    queue = [[s, 1]]
    while queue:
        a, count = queue.pop(0)
        for b in D[a]:
            if b == g:
                p_result += count
                continue
            elif b == "out":
                continue
            for p in queue:
                if p[0] == b:
                    p[1] += count
                    break
            else:
                queue.append([b, count])
    w_result.append(p_result)

print(w_result)
result += math.prod(w_result)

print(result)
