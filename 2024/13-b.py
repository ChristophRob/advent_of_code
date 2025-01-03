#!/usr/bin/env python3
from fractions import Fraction

# TEST_RESULT = 875318608908
# REAL_RESULT = 104140871044942

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
        X = int(xx[1].split(",")[0]) + 10000000000000
        Y = int(xx[2]) + 10000000000000
        machine.append((X, Y))
        machines.append(machine)
        machine = []


tokens = 0
for machine in machines:
    (Ax, Ay), (Bx, By), (Px, Py) = machine
    b = (Px - Fraction(Ax * Py, Ay)) / (Bx - Ax * Fraction(By, Ay))
    if not b.is_integer():
        continue
    a = (Px - Bx * b) / Ax
    tokens += int(a * 3 + b * 1)
print(tokens)
