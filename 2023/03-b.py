#!/usr/bin/env python3

# TEST_RESULT = 467835
# REAL_RESULT = 80403602


result = 0
s = ""
with open("./data/03-real.txt") as file:
    for line in file.readlines():
        w = len(line)
        s += line.strip()

N = {}
n = ""
stars = []
for i, c in enumerate(s):
    if c.isnumeric():
        n += c
    elif n:
        for ix in range(1, len(n) + 1):
            N[i - ix] = (int(n), i)
        n = ""
    if c == "*":
        stars.append(i)

for st in stars:
    ns = [
        N[st + i] for i in [-1, 1, -w, -1 - w, +1 - w, w, -1 + w, 1 + w] if st + i in N
    ]
    if len(ns := list(set(ns))) == 2:
        result += ns[0][0] * ns[1][0]


print(result)
