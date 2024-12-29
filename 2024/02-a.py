#!/usr/bin/env python3

# TEST_RESULT = 2
# REAL_RESULT = 383

DATA = []
with open("./data/02-real.txt") as file:
    for line in file.readlines():
        DATA.append(tuple([int(i) for i in line.strip().split(" ") if i]))


safe_amount = 0
for x in DATA:
    minimum, maximum = (1, 3) if x[0] - x[1] < 0 else (-3, -1)
    for i in range(1, len(x)):
        if not maximum >= x[i] - x[i - 1] >= minimum:
            break
    else:
        safe_amount += 1

print(safe_amount)
