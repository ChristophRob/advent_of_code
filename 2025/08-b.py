#!/usr/bin/env python3
import math

# TEST_RESULT = 40
# REAL_RESULT = 42315


N = []
D = []
FIRST_PAIRS = 1000

with open("./data/08-real.txt") as file:
    for line in file.readlines():
        N.append(tuple([int(i) for i in line.split(",")]))


for idx, p in enumerate(N):
    for q in N[idx + 1 :]:
        D.append((p, q, math.dist(p, q)))

D.sort(key=lambda d: d[2])

for d in range(FIRST_PAIRS, 10000):
    C = []
    for p, q, _ in D[:d]:
        C.append(set([str(p), str(q)]))

    changed = True
    while changed:
        changed = False
        for idx, c1 in enumerate(C):
            for c2 in C[idx + 1 :]:
                if c2.intersection(c1):
                    c1.update(c2)
                    del C[C.index(c2)]
                    changed = True

    if len(C) == 1 and len(C[0]) == len(N):
        print(d, len(C), len(C[0]))
        print(p, q)
        print(p[0] * q[0])
        break
    else:
        print(d, len(C), len(C[0]))
