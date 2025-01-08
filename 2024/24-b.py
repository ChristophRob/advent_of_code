#!/usr/bin/env python3

# TEST_RESULT = NA
# REAL_RESULT = gfv,hcm,kfs,tqm,vwr,z06,z11,z16

ROOT_MAP = {}

ROOT_OPERATIONS = []

SWAPS = {
    "z06": "vwr",
    "vwr": "z06",
    "tqm": "z11",
    "z11": "tqm",
    "z16": "kfs",
    "kfs": "z16",
    "gfv": "hcm",
    "hcm": "gfv",
}

connections = []
with open("./data/24-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if ":" in line:
            k, v = line.split(": ")
            ROOT_MAP[k] = int(v)
        if "->" in line:
            a, op, b, _, res = line.split(" ")
            if res in SWAPS:
                res = SWAPS[res]
            ROOT_OPERATIONS.append((a, b, op, res))


def set_var(var, new_value):
    for k in MAP:
        if k.startswith(var):
            MAP[k] = 0
    new_bin = format(new_value, "b")
    for i in range(len(new_bin)):
        key = var + "{:02d}".format(i)
        MAP[key] = int(new_bin[-i - 1])


class NotValid(Exception):
    pass


def sum(operations, map):
    while operations:
        new_operations = []
        for ops in operations:
            (a, b, op, res) = ops
            if a in map and b in map:
                if op == "AND":
                    MAP[res] = MAP[a] and MAP[b]
                elif op == "OR":
                    MAP[res] = MAP[a] or MAP[b]
                elif op == "XOR":
                    MAP[res] = MAP[a] ^ MAP[b]
            else:
                new_operations.append(ops)
        operations = new_operations

    zs = []
    for k, v in map.items():
        if k.startswith("z"):
            zs.append((int(k[1:]), v))

    sorted_zs = sorted(zs, key=lambda tup: tup[0], reverse=True)

    result = ""
    for z in sorted_zs:
        result += str(z[1])

    return int(result, 2)


def go_func(operations, x, y):
    global MAP
    OPERATIONS = list(operations)
    MAP = ROOT_MAP.copy()
    set_var("x", x)
    set_var("y", y)
    res = sum(OPERATIONS, MAP)
    assert x + y == res


"""
Increasing the test range to find the issues one by one.
"""
TEST_RANGE = 2**40 + 1
TEST_START = 2**40 - 1

for x in range(TEST_START, TEST_RANGE, 1):
    for y in range(TEST_START, TEST_RANGE, 1):
        go_func(ROOT_OPERATIONS, x, y)

x = [s for s in SWAPS]
x.sort()
print(",".join(x))
