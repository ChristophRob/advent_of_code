#!/usr/bin/env python3

# TEST_RESULT = 34
# REAL_RESULT = 912

with open("./data/08-real.txt") as file:
    INPUT = [line.strip() for line in file.readlines()]


def node_in_boundaries(node, max_index):
    if node[0] < 0 or node[0] > max_index:
        return False
    if node[1] < 0 or node[1] > max_index:
        return False
    return True


def check_node(loc, pair, max_index):
    result = [loc, pair]
    diff = (pair[0] - loc[0], pair[1] - loc[1])
    loc1 = pair[0] + diff[0], pair[1] + diff[1]
    while True:
        if node_in_boundaries(loc1, max_index):
            result.append(loc1)
        else:
            break
        loc1 = loc1[0] + diff[0], loc1[1] + diff[1]
    loc2 = loc[0] - diff[0], loc[1] - diff[1]
    while True:
        if node_in_boundaries(loc2, max_index):
            result.append(loc2)
        else:
            break
        loc2 = loc2[0] - diff[0], loc2[1] - diff[1]
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
result = list(set(result))

result_matrix = []
for i in INPUT:
    result_matrix.append(list(i))

for i in result:
    result_matrix[i[0]][i[1]] = "#"

print(len(result))
