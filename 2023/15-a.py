#!/usr/bin/env python3

# TEST_RESULT = 1320
# REAL_RESULT = 501680

SEQ = []
result = 0

with open("./data/15-real.txt") as file:
    for line in file.readlines():
        SEQ = line.strip().split(",")


for s in SEQ:
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value = (current_value * 17) % 256
    result += current_value

print(result)
