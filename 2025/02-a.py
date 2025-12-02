#!/usr/bin/env python3

# TEST_RESULT = 1227775554
# REAL_RESULT = 32976912643
res = 0

with open("./data/02-real.txt") as file:
    for line in file.readlines():
        for _range in line.split(","):
            a, b = _range.split("-")
            for i in range(int(a), int(b) + 1):
                n = str(i)
                h = len(n) // 2
                if n[:h] == n[h:]:
                    res += i

print(res)
