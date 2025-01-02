#!/usr/bin/env python3

# TEST_RESULT = 14
# REAL_RESULT = 244

with open("./data/08-real.txt") as file:
    INPUT = [line.strip() for line in file.readlines()]


def node_in_boundaries(node, max_index):
    if node[0] < 0 or node[0] > max_index:
        return False
    if node[1] < 0 or node[1] > max_index:
        return False
    return True


def check_node(loc, pair, max_index):
    result = []
    diff = (pair[0] - loc[0], pair[1] - loc[1])
    loc1 = pair[0] + diff[0], pair[1] + diff[1]
    loc2 = loc[0] - diff[0], loc[1] - diff[1]
    if node_in_boundaries(loc1, max_index):
        result.append(loc1)
    if node_in_boundaries(loc2, max_index):
        result.append(loc2)
    return result


locs = {}
for y in range(len(INPUT)):
    for x in range(len(INPUT[0])):
        val = INPUT[y][x]
        if val != ".":
            if val not in locs:
                locs[val] = []
            locs[val].append((y, x))

result = []
max_index = len(INPUT) - 1
for sequence in locs.values():
    for loc in sequence:
        for pair in sequence:
            if loc == pair:
                continue
            result.extend(check_node(loc, pair, max_index))

print(len(list(set(result))))
