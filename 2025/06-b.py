#!/usr/bin/env python3
import math
import numpy

# TEST_RESULT = 3263827
# REAL_RESULT = 7450962489289
result = 0

N = []

with open("./data/06-real.txt") as file:
    for line in file.readlines():
        N.append([c for c in line if c != "\n"])

N = numpy.transpose(N)
op = None
ns = []

for line in N:
    if line[-1] != " ":
        if line[-1] == "*":
            op = math.prod
        elif line[-1] == "+":
            op = sum
        else:
            raise KeyError()
    n = "".join(line[:-1])
    if n.split():
        ns.append(int(n))
    else:
        result += op(ns)
        ns = []
result += op(ns)

print(result)
