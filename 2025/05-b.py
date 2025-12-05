#!/usr/bin/env python3

# TEST_RESULT = 14
# REAL_RESULT = 350780324308385

RANGES = []

with open("./data/05-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if "-" in line:
            a, b = line.split("-")
            RANGES.append((int(a), int(b)))

while True:
    RANGES_WO = []  # RANGES_WITHOUT_OVERLAP
    for ra, rb in RANGES:
        for idx, (wa, wb) in enumerate(RANGES_WO):
            if ra >= wa and ra <= wb:  # expand to the right
                RANGES_WO[idx] = (wa, max(wb, rb))
                break
            if rb >= wa and rb <= wb:  # expand to the left
                RANGES_WO[idx] = (min(wa, ra), wb)
                break
            if ra <= wa and rb >= wb:  # expand to both sides
                RANGES_WO[idx] = (ra, rb)
                break
        else:
            RANGES_WO.append((ra, rb))
    if len(RANGES) == len(RANGES_WO):
        break
    RANGES = [i for i in RANGES_WO]

result = sum([(b - a + 1) for (a, b) in RANGES])
print(result)
