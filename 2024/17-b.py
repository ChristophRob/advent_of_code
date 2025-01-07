#!/usr/bin/env python3

# TEST_RESULT = NA
# REAL_RESULT = 107416870455451

with open("./data/17-real.txt") as file:
    for line in file.readlines():
        if "Program" in line:
            PROGRAM = [
                int(v) for v in line.strip().replace(":", "").split()[1].split(",")
            ]


def calc(A):
    p = B = C = 0
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
                result.append(combo_operand % 8)
            case 6:
                B = A // (2**combo_operand)
            case 7:
                C = A // (2**combo_operand)
        p += 2
    return result


class FoundIt(Exception):
    pass


FINAL_A = None

"""
Went through the Program steps one by one. Found the following hints:
- We only have to look at Register A, since B and C are set by A during the Program
- A is basically floor dividing itself by 8 with every program
- If we go backwards and start with the last number "0" only one number for Register A can have that output "3".
- If A must be 3 and the output must be 3 (2nd last digit of Program) then Register A must be one of 24,25,29 or 31.
- So we have to check further starting with the lowest number.
"""


def calc_backwards(A, step):
    for next_a in range(8 * A, 8 * (A + 1)):
        result = calc(next_a)
        if result == PROGRAM[step:]:
            if step == 0:
                global FINAL_A
                FINAL_A = next_a
                raise FoundIt(next_a)
            calc_backwards(next_a, step - 1)


try:
    calc_backwards(0, len(PROGRAM) - 1)
except FoundIt:
    print(FINAL_A)
