#!/usr/bin/env python3

import re

# TEST_RESULT = 4361
# REAL_RESULT = 528819


result = 0
s = ""
with open("./data/03-real.txt") as file:
    for line in file.readlines():
        w = len(line)
        s += line.strip()

n = ""
for i, c in enumerate(s):
    if c.isnumeric():
        n += c
    elif n:
        check = (
            s[i - len(n) - w - 1 : i + 1 - w]
            + s[i - len(n) - 1 : i + 1]
            + s[i - len(n) + w - 1 : i + 1 + w]
        )
        if re.sub(r"[.0-9]+", "", check):
            result += int(n)
        n = ""

print(result)
