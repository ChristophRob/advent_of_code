#!/usr/bin/env python3

# TEST_RESULT = 6
# REAL_RESULT = 6133

n = 50
res = 0
with open("./data/01-real.txt") as file:
    for line in file.readlines():
        d = 1 if line[0] == "R" else -1
        i = int(line[1:])

        n_old = n
        res += i // 100
        i = i % 100
        n += i * d
        if n >= 100 or (n <= 0 and n_old != 0):
            res += 1
        n = n % 100

print(res)
