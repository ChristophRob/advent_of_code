#!/usr/bin/env python3
import math
import numpy

# TEST_RESULT = 4277556
# REAL_RESULT = 4405895212738
result = 0

N = []

with open("./data/06-real.txt") as file:
    for line in file.readlines():
        N.append(line.strip().split())

N = numpy.transpose(N)

for ns in N:
    op = math.prod if ns[-1] == "*" else sum
    result += op([int(i) for i in ns[:-1]])

print(result)
