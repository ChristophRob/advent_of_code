#!/usr/bin/env python3

# TEST_RESULT = 3
# REAL_RESULT = 992

n = 50
res = 0
with open("./data/01-real.txt") as file:
    for line in file.readlines():
        d, i = line[0], int(line[1:]) % 100
        if d == "L":
            i = 100 - i
        n += i
        if n % 100 == 0:
            res += 1
        print(res, line.strip(), d, i, n)


print(res)
