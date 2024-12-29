#!/usr/bin/env python3

# TEST_RESULT = 11
# REAL_RESULT = 2580760

X = []
Y = []
with open("./data/01-real.txt") as file:
    for line in file.readlines():
        x, y = [int(i) for i in line.strip().split(" ") if i]
        X.append(x)
        Y.append(y)

X.sort()
Y.sort()

result = sum([abs(x - y) for x, y in list(zip(X, Y))])
print(result)
