#!/usr/bin/env python3

# TEST_RESULT = 18
# REAL_RESULT = 2458


def make_diagonal_lines(input, change):
    diagonal = []
    length = len(input[0])
    increment = 0
    for i in range(length * length):
        diagonal.append("")
    for i in range(length):
        for j in range(length):
            first = i
            if change:
                first = i * (-1) - 1
            diagonal[j + increment] += input[first][j]
        increment += 1

    new_diagonal = []
    for x in diagonal:
        if x:
            new_diagonal.append(x)
    return new_diagonal


def calc(input, variation):
    result = 0
    for line in input:
        result += len(line.split(variation)) - 1
    return result


with open("./data/04-real.txt") as file:
    INPUT = [line.strip() for line in file.readlines()]

result = 0

result += calc(INPUT, "XMAS")
result += calc(INPUT, "SAMX")

transposed = []
length = len(INPUT[0])
for i in range(length):
    transposed.append("")
for i in range(length):
    for j in range(length):
        transposed[j] += INPUT[i][j]
result += calc(transposed, "XMAS")
result += calc(transposed, "SAMX")

d1 = make_diagonal_lines(INPUT, False)
result += calc(d1, "XMAS")
result += calc(d1, "SAMX")

d2 = make_diagonal_lines(INPUT, True)
result += calc(d2, "XMAS")
result += calc(d2, "SAMX")

print(result)
