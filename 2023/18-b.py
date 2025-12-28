#!/usr/bin/env python3

# TEST_RESULT = 952408144115
# REAL_RESULT = 42708339569950

# To Calculate the area of a polygon including the
# border we can make use of the Shoelace formula.
# The Shoelace Formula + half border + 1

y1, x1 = 0, 0
area = 0
border = 0

with open("./data/18-real.txt") as file:
    for line in file.readlines():
        _, hex = line.split("#")
        n = int(hex[:5], 16)
        border += n
        d = hex[5]
        # 0 means R, 1 means D, 2 means L, and 3 means U
        if d in "23":
            n *= -1
        x2 = x1 if d in "13" else x1 + n
        y2 = y1 if d in "02" else y1 + n
        area += (y1 + y2) * (x1 - x2)
        y1, x1 = y2, x2

result = int((abs(area) + border) / 2 + 1)
print(result)
