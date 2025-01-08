#!/usr/bin/env python3

# TEST_RESULT = 2024
# REAL_RESULT = 50411513338638

MAP = {}

OPERATIONS = []


connections = []
with open("./data/24-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if ":" in line:
            k, v = line.split(": ")
            MAP[k] = int(v)
        if "->" in line:
            a, op, b, _, res = line.split(" ")
            OPERATIONS.append((a, b, op, res))


while OPERATIONS:
    new_operations = []
    for ops in OPERATIONS:
        (a, b, op, res) = ops
        if a in MAP and b in MAP:
            if op == "AND":
                MAP[res] = MAP[a] and MAP[b]
            elif op == "OR":
                MAP[res] = MAP[a] or MAP[b]
            elif op == "XOR":
                MAP[res] = MAP[a] ^ MAP[b]
        else:
            new_operations.append(ops)
    OPERATIONS = new_operations


zs = []
for k, v in MAP.items():
    if k.startswith("z"):
        zs.append((int(k[1:]), v))

sorted_zs = sorted(zs, key=lambda tup: tup[0], reverse=True)

result = ""
for z in sorted_zs:
    result += str(z[1])

print(int(result, 2))
