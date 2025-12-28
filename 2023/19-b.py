#!/usr/bin/env python3

from collections import deque

# TEST_RESULT = 167409079868000
# REAL_RESULT = 136661579897555
RULES = {}


with open("./data/19-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if line and line[0] != "{":
            key, values = line.replace("}", "").split("{")
            RULES[key] = [
                (
                    {
                        "to": (s := v.split(":"))[1],  # Walrus operator
                        "part": s[0][0],
                        "compare": s[0][1],
                        "with": int(s[0][2:]),
                    }
                    if ":" in v
                    else {"to": v}
                )
                for v in values.split(",")
            ]

opposite = {">": "<", "<": ">"}
possible_ways = []
queue = deque([("in", [])])


while queue:
    key, conditions = queue.popleft()
    for rule in RULES[key]:
        if "compare" in rule:
            these_conditions = [j for j in conditions] + [
                {
                    "part": rule["part"],
                    "operator": rule["compare"],
                    "with": rule["with"],
                }
            ]
            conditions.append(
                {
                    "part": rule["part"],
                    "operator": opposite[rule["compare"]],
                    "with": rule["with"] + (1 if rule["compare"] == ">" else -1),
                }
            )
            if rule["to"] == "A":
                possible_ways.append(these_conditions)
            elif rule["to"] == "R":
                pass
            else:
                queue.append((rule["to"], these_conditions))
        else:
            if rule["to"] == "R":
                pass
            elif rule["to"] == "A":
                possible_ways.append([j for j in conditions])
            else:
                queue.append((rule["to"], [j for j in conditions]))


RANGES = []

for conditions in possible_ways:
    assigned = {"x": [], "m": [], "a": [], "s": []}
    for c in conditions:
        assigned[c["part"]].append((c["operator"], c["with"]))

    ranges = {}
    for key, conditions in assigned.items():
        range_low, range_high = 1, 4000
        for op, v in conditions:
            if op == ">":
                range_low = max(range_low, v + 1)
            if op == "<":
                range_high = min(range_high, v - 1)
        ranges[key] = (range_low, range_high)
    RANGES.append(ranges)

result = 0
for ranges in RANGES:
    combinations = 1
    for low, high in ranges.values():
        combinations *= high - low + 1
    result += combinations
print(result)
