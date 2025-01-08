#!/usr/bin/env python3

# TEST_RESULT = 6
# REAL_RESULT = 206


PATTERNS = []
with open("./data/19-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if not line:
            continue
        if "," in line:
            TOWELS = line.split(", ")
        else:
            PATTERNS.append(line)

KNOWN_PATTERNS = {}


def step(i, pattern):
    result = 0
    if pattern[i:] in KNOWN_PATTERNS:
        return KNOWN_PATTERNS[pattern[i:]]
    for towel in TOWELS:
        if pattern[i:].startswith(towel):
            if i + len(towel) == len(pattern):
                return 1
            else:
                n = step(i + len(towel), pattern)
                if n:
                    return n
    KNOWN_PATTERNS[pattern[i:]] = result
    return result


print(sum([step(0, p) for p in PATTERNS]))
