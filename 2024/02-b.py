#!/usr/bin/env python3

# TEST_RESULT = 4
# REAL_RESULT = 436


DATA = []
with open("./data/02-real.txt") as file:
    for line in file.readlines():
        DATA.append(tuple([int(i) for i in line.strip().split(" ") if i]))


def test_if_safe(levels):
    minimum, maximum = (1, 3) if levels[0] - levels[1] < 0 else (-3, -1)
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if diff < minimum or diff > maximum:
            return False
    return True


safe_amount = 0
for x in DATA:
    if test_if_safe(x):
        safe_amount += 1
    else:
        for i in range(len(x)):
            n = i + 1
            if test_if_safe(x[:i] + x[n:]):
                safe_amount += 1
                break

print(safe_amount)
