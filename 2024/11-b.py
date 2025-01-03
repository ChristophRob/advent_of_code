#!/usr/bin/env python3

# TEST_RESULT = 65601038650482
# REAL_RESULT = 207961583799296

with open("./data/11-test.txt") as file:
    INPUT = [line.strip() for line in file.readlines()][0].split(" ")


def addN(n, k, v):
    if k not in n:
        n[k] = 0
    n[k] += v
    return n


def increment(numbers):
    new_numbers = {}
    if numbers.get("0"):
        addN(new_numbers, "1", numbers["0"])
        del numbers["0"]

    for k, v in numbers.items():
        if len(k) % 2 == 0:
            middle = len(k) // 2
            addN(new_numbers, k[:middle], v)
            addN(new_numbers, str(int(k[middle:])), v)
        else:
            addN(new_numbers, str(int(k) * 2024), v)
    return new_numbers


TOTAL_RANGE = 75
new_input = INPUT
numbers = {}
for i in new_input:
    addN(numbers, i, 1)
for i in range(TOTAL_RANGE):
    numbers = increment(numbers)

print(sum(numbers.values()))
