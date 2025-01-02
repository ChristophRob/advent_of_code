#!/usr/bin/env python3

# TEST_RESULT = 3749
# REAL_RESULT = 5540634308362

INPUT = []
with open("./data/07-test.txt") as file:
    for line in file.readlines():
        INPUT.append([int(i) for i in line.strip().replace(":", "").split()])


result = 0
for statement in INPUT:
    expected = statement[0]
    amounts = [statement[1]]
    for n in statement[2:]:
        new_amounts = []
        for amount in amounts:
            new_amounts.append(amount + n)
            new_amounts.append(amount * n)
        amounts = new_amounts
    if expected in amounts:
        result += expected
print(result)
