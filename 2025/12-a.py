#!/usr/bin/env python3

# TEST_RESULT = 2
# REAL_RESULT = 528

parts = []
p = 0
easy_fit = 0
no_fit = 0
total = 0

with open("./data/12-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if "#" in line:
            for c in line:
                if c == "#":
                    p += 1
        elif "x" in line:
            total += 1
            grid, counts = line.split(":")
            x, y = [int(i) for i in grid.split("x")]
            ns = [int(i) for i in counts.split()]
            space = x * y
            full = sum(ns) * 9
            minimum = sum([n * p for n, p in zip(ns, parts)])
            if space > full:
                easy_fit += 1
            elif minimum > space:
                no_fit += 1
        elif p:
            parts.append(p)
            p = 0


print(easy_fit)
print(no_fit)
print(f"Should fit: {total-no_fit}")
