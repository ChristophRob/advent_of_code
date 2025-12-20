#!/usr/bin/env python3
from collections import defaultdict

# TEST_RESULT = 525152
# REAL_RESULT = 8475948826693

result = 0
P = []

with open("./data/12-real.txt") as file:
    for line in file.readlines():
        s, ns = line.strip().split()
        ns = [int(n) for n in ns.split(",")] * 5
        s = "?".join([s for _ in range(5)])
        P.append((s, ns))


for s, ns in P:
    s += "."
    counts = {(0, 0): 1}
    for c in s:
        n_counts = defaultdict(int)
        for (hgi, hl), count in counts.items():
            if c in ".?":
                if hl == 0:
                    n_counts[(hgi, hl)] += count
                elif hgi < len(ns) and hl == ns[hgi]:
                    n_counts[(hgi + 1, 0)] = count

            if c in "#?":
                if hgi < len(ns) and hl < ns[hgi]:
                    n_counts[(hgi, hl + 1)] = count
        counts = n_counts
    result += counts[(len(ns), 0)]

print(result)
