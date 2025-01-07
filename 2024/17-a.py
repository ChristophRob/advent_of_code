#!/usr/bin/env python3

# TEST_RESULT = 4,6,3,5,6,3,5,2,1,0
# REAL_RESULT = 2,7,6,5,6,0,2,3,1

R = {}

with open("./data/17-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if "Register" in line:
            _, key, value = line.replace(":", "").split()
            R[key] = int(value)
        if "Program" in line:
            key, value = line.replace(":", "").split()
            PROGRAM = [int(v) for v in value.split(",")]

A, B, C = R["A"], R["B"], R["C"]
p = 0


result = []
while p < len(PROGRAM):
    next, lit_op = PROGRAM[p: p + 2]
    combo_operand = {4: A, 5: B, 6: C}.get(lit_op, lit_op)
    match next:
        case 0:
            A = A // (2**combo_operand)
        case 1:
            B = B ^ lit_op
        case 2:
            B = combo_operand % 8
        case 3:
            if A != 0:
                p = lit_op
                continue
        case 4:
            B = B ^ C
        case 5:
            result.append(str(combo_operand % 8))
        case 6:
            B = A // (2**combo_operand)
        case 7:
            C = A // (2**combo_operand)
    p += 2

print(",".join(result))
