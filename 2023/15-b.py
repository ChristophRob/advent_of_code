#!/usr/bin/env python3

from collections import OrderedDict

# TEST_RESULT = 145
# REAL_RESULT = 241094

SEQ = []
result = 0

with open("./data/15-real.txt") as file:
    for line in file.readlines():
        SEQ = line.strip().split(",")

MAP = {}

BOXES = [OrderedDict() for _ in range(256)]
for s in SEQ:
    if "-" in s:
        label = s.split("-")[0]
        if label in MAP:
            box = BOXES[MAP[label]]
            if label in box:
                del box[label]
    elif "=" in s:
        label, v = s.split("=")
        if label not in MAP:
            current_value = 0
            for c in label:
                current_value += ord(c)
                current_value = (current_value * 17) % 256
            MAP[label] = current_value
        box = BOXES[MAP[label]]
        box[label] = int(v)


for idx, box in enumerate(BOXES):
    for li, (lens, v) in enumerate(box.items()):
        result += (idx + 1) * (li + 1) * v

print(result)
