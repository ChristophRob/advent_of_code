#!/usr/bin/env python3

# TEST_RESULT = 357
# REAL_RESULT = 16927
result = 0


with open("./data/03-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        fn = fi = ln = li = 0
        for idx, c in enumerate(line[:-1]):
            n = int(c)
            if n > fn:
                fn, fi = n, idx
            if n == 9:
                break
        for idx, c in enumerate(line[fi + 1 :]):
            n = int(c)
            if n > ln:
                ln, li = n, idx
            if n == 9:
                break
        result += fn * 10 + ln


print(result)
