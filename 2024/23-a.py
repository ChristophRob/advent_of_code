#!/usr/bin/env python3

# TEST_RESULT = 7
# REAL_RESULT = 1184

connections = []
with open("./data/23-real.txt") as file:
    for line in file.readlines():
        connections.append(line.strip().split("-"))


MAP = {}
for x, y in connections:
    if x not in MAP:
        MAP[x] = []
    MAP[x].append(y)
    if y not in MAP:
        MAP[y] = []
    MAP[y].append(x)


THREES = set([])
for key, conns in MAP.items():
    for conn in conns:
        inter = set(MAP[conn]) & set(MAP[key])
        for i in inter:
            if i == conn or key == conn or key == i:
                raise Exception(f"Oh no {key}, {conn}, {i}")
            for c in [key, conn, i]:
                if c[0] == "t":
                    frozen = frozenset([key, conn, i])
                    THREES.add(frozen)
                    break

print(len(THREES))
