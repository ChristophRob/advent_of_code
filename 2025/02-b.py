#!/usr/bin/env python3

# TEST_RESULT = 4174379265
# REAL_RESULT = 54446379122
result = 0


def check_n(number):
    t = str(number)
    le = len(t)

    steps = [i for i in range(1, le) if le % i == 0]

    for s in steps:
        parts = []
        for i in range(0, le, s):
            parts.append(t[i : i + s])
        if len(set(parts)) == 1:
            return number
    return 0


with open("./data/02-real.txt") as file:
    for line in file.readlines():
        for _range in line.split(","):
            a, b = _range.split("-")
            for n in range(int(a), int(b) + 1):
                result += check_n(n)


print(result)
