#!/usr/bin/env python3

# TEST_RESULT = 3
# REAL_RESULT = 2854

LOCKS = []
KEYS = []

raster = None
new_schematic = True
schema = None
with open("./data/25-real.txt") as file:
    for line in file.readlines():
        line = line.strip()

        if new_schematic:
            if raster:
                if schema == "lock":
                    LOCKS.append(raster)
                else:
                    reverse_raster = []
                    for c in raster:
                        reverse_raster.append(5 - c)
                    KEYS.append(reverse_raster)
            schema = "lock" if line[0] == "#" else "key"
            new_schematic = False
            first_run = False
            raster = [-1, -1, -1, -1, -1]
        if not line:
            new_schematic = True
        for i, c in enumerate(line):
            lookup = "#" if schema == "lock" else "."
            if c == lookup:
                raster[i] += 1
    if schema == "lock":
        LOCKS.append(raster)
    else:
        reverse_raster = []
        for c in raster:
            reverse_raster.append(5 - c)
        KEYS.append(reverse_raster)

win = 0

for key in KEYS:
    for lock in LOCKS:
        for k, l in list(zip(key, lock)):
            if k + l > 5:
                break
        else:
            win += 1

print(win)
