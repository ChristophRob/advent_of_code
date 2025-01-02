#!/usr/bin/env python3

# TEST_RESULT = 123
# REAL_RESULT = 4480

import collections


with open("./data/05-real.txt") as file:
    RULES = []
    INPUT = []
    for line in file.readlines():
        line = line.strip()
        if "|" in line:
            RULES.append([int(i) for i in line.split("|")])
        if "," in line:
            INPUT.append([int(i) for i in line.split(",")])


def check_new_order_valid(testString, rules):
    for i in range(len(testString)):
        if testString[i] in rules:
            if collections.Counter(rules[testString[i]]) & collections.Counter(
                testString[:i]
            ):
                return False
    return True


def correct_order(testString, rules):
    newOrder = []
    for n in testString:
        increment = 0
        while True:
            newOrderTry = newOrder.copy()
            newOrderTry.insert(increment, n)
            if check_new_order_valid(newOrderTry, rules):
                newOrder = newOrderTry
                break

            increment += 1

    return newOrder[int((len(newOrder) - 1) / 2)]


def check_valid_string(testString, rules):
    for i in range(len(testString)):
        if testString[i] in rules:
            if collections.Counter(rules[testString[i]]) & collections.Counter(
                testString[:i]
            ):
                return correct_order(testString, rules)
    return 0


result = 0
rules = {}
for key, param in RULES:
    if key not in rules:
        rules[key] = []
    rules[key].append(param)

for testString in INPUT:
    result += check_valid_string(testString, rules)
print(result)
