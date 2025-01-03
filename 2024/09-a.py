#!/usr/bin/env python3

# TEST_RESULT = 1928
# REAL_RESULT = 6331212425418


with open("./data/09-real.txt") as file:
    INPUT = [line.strip() for line in file.readlines()][0]


odd = True
increment = 0
disk_map = []
for i in INPUT:
    if odd:
        for j in range(int(i)):
            disk_map.append(increment)
        increment += 1
    else:
        for j in range(int(i)):
            disk_map.append(".")
    odd = not odd

result = 0
try:
    for i in range(len(disk_map)):
        if disk_map[i] == ".":
            last = disk_map.pop()
            while last == ".":
                last = disk_map.pop()
            result += i * last
        else:
            result += i * disk_map[i]
except IndexError:
    print(result)
