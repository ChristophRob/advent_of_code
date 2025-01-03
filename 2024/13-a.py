#!/usr/bin/env python3

# TEST_RESULT = 480
# REAL_RESULT = 29201

from fractions import Fraction

"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

I  94a + 22b = 8400
II 34a + 67b = 5400

II a = (5400 - 67b) / 34
II in I:
94 * (5400 - 67b) / 34 + 22b = 8400

8400 - 94 * 5400 / 34 = (22 - 94 * 67 / 34) * b
b = (8400 - 94 * 5400 / 34) / (22 - 94 * 67 / 34)

a = (8400 - 22b) / 94
"""


with open("./data/13-real.txt") as file:
    INPUT = [line.strip() for line in file.readlines() if line.strip()]

machines = []
machine = []
for line in INPUT:
    if "Button" in line:
        xx = line.split("+")
        X = int(xx[1].split(",")[0])
        Y = int(xx[2])
        machine.append((X, Y))
    else:
        xx = line.split("=")
        X = int(xx[1].split(",")[0])
        Y = int(xx[2])
        machine.append((X, Y))
        machines.append(machine)
        machine = []


tokens = 0
for machine in machines:
    (Ax, Ay), (Bx, By), (Px, Py) = machine
    # [(94, 34), (22, 67), (8400, 5400)]

    b = (Px - Fraction(Ax * Py, Ay)) / (Bx - Ax * Fraction(By, Ay))

    if not b.is_integer():
        continue
    a = (Px - Bx * b) / Ax
    tokens += int(a * 3 + b * 1)
print(tokens)
