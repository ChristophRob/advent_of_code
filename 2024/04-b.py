#!/usr/bin/env python3

# TEST_RESULT = 9
# REAL_RESULT = 1945

with open("./data/04-real.txt") as file:
    INPUT = [line.strip() for line in file.readlines()]

result = 0

for i in range(1, len(INPUT) - 1):
    line = INPUT[i]
    for j in range(1, len(INPUT) - 1):
        if line[j] == "A":
            lu = INPUT[i - 1][j - 1]
            ld = INPUT[i - 1][j + 1]
            rd = INPUT[i + 1][j + 1]
            ru = INPUT[i + 1][j - 1]
            if (lu + rd in ["SM", "MS"]) and (ru + ld in ["SM", "MS"]):
                result += 1

print(result)
