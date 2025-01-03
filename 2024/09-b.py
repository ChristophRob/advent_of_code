#!/usr/bin/env python3

# TEST_RESULT = 2858
# REAL_RESULT = 6363268339304

with open("./data/09-real.txt") as file:
    INPUT = [int(i) for i in [line.strip() for line in file.readlines()][0]]


extra_space = [0 for i in INPUT]
result = []

original_index = 0
for original_index, v in enumerate(INPUT):
    result += [0] * extra_space[original_index]
    if original_index % 2 == 0:
        result += [original_index // 2] * v
    else:
        increment = 0
        while INPUT[original_index] != 0:
            if (
                INPUT[-1 - increment] != 0
                and INPUT[-1 - increment] <= INPUT[original_index]
            ):
                value = INPUT[-1 - increment]
                result += [(len(INPUT) - increment) // 2] * value
                INPUT[original_index] -= value
                extra_space[-1 - increment] += INPUT[-1 - increment]
                INPUT[-1 - increment] = 0
            increment += 2
            if len(INPUT) - 1 - increment <= original_index:
                result += [0] * INPUT[original_index]
                INPUT[original_index] = 0

    original_index += 1

print(sum([i * r for i, r in enumerate(result)]))
