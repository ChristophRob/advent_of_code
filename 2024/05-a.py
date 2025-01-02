#!/usr/bin/env python3

# TEST_RESULT = 143
# REAL_RESULT = 4185

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


def check_valid_string(testString, rules):
    for i in range(len(testString)):
        if testString[i] in rules:
            if collections.Counter(rules[testString[i]]) & collections.Counter(
                testString[:i]
            ):
                return 0
    return testString[int((len(testString) - 1) / 2)]


result = 0
rules = {}
for key, param in RULES:
    if key not in rules:
        rules[key] = []
    rules[key].append(param)

for testString in INPUT:
    result += check_valid_string(testString, rules)
print(result)
