#!/usr/bin/env python3

# TEST_RESULT = 35
# REAL_RESULT = 910845529


seeds = None
M = []
cur = None
with open("./data/05-real.txt") as file:
    for line in file.readlines():
        line = line.strip()

        if "seeds" in line:
            seeds = [int(i) for i in line.split()[1:]]
        elif "map" in line:
            cur = []
            M.append(cur)
        elif line:
            cur.append([int(i) for i in line.split()])

places = []
for seed in seeds:
    place = seed
    for m in M:
        for to, fro, le in m:
            if fro <= place < fro + le:
                place = (place - fro) + to
                break
    places.append(place)

print(min(places))
