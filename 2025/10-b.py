#!/usr/bin/env python3
import re
import pulp

# TEST_RESULT = 33
# REAL_RESULT = 18771

result = 0

G = []
B = []

with open("./data/10-real.txt") as file:
    for line in file.readlines():
        line = re.sub(r"[\{\}\(\)]", "", line)
        parts = line.split()
        G.append([int(i) for i in parts[-1].split(",")])
        bs = []
        for b in parts[1:-1]:
            bs.append(tuple([int(i) for i in b.split(",")]))
        B.append(bs)

for buttons, goal in zip(B, G):
    prob = pulp.LpProblem("Summen_Minimierung", pulp.LpMinimize)
    vars = [
        pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(buttons))
    ]
    prob += pulp.lpSum(vars)

    gleichungen = []
    for idx, n in enumerate(goal):
        vs = []
        for ib, b in enumerate(buttons):
            if idx in b:
                vs.append(vars[ib])
        prob += sum(vs) == n

    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    result += int(pulp.value(prob.objective))

print(result)
