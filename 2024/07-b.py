#!/usr/bin/env python3

# TEST_RESULT = 11387
# REAL_RESULT = 472290821152397

INPUT = []
with open("./data/07-real.txt") as file:
    for line in file.readlines():
        INPUT.append([int(i) for i in line.strip().replace(":", "").split()])


def concatentate(amount, n):
    return int(str(amount) + str(n))


result = 0
for statement in INPUT:
    expected = statement[0]
    amounts = [statement[1]]
    for n in statement[2:]:
        new_amounts = []
        for amount in amounts:
            new_amounts.append(amount + n)
            new_amounts.append(amount * n)
            new_amounts.append(concatentate(amount, n))
        amounts = new_amounts
    if expected in amounts:
        result += expected
print(result)
