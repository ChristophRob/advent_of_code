#!/usr/bin/env python3

# TEST_RESULT = 55312
# REAL_RESULT = 175006


with open("./data/11-real.txt") as file:
    INPUT = [line.strip() for line in file.readlines()][0].split(" ")


for i in range(25):
    result = []
    for n in INPUT:
        if n == "0":
            result.append("1")
        elif len(n) % 2 == 0:
            middle = len(n) // 2
            result.extend([n[:middle], str(int(n[middle:]))])
        else:
            result.append(str(int(n) * 2024))
    INPUT = result

print(len(INPUT))
