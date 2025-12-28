#!/usr/bin/env python3

# TEST_RESULT = 19114
# REAL_RESULT = 332145

import operator

INPUTS = []
RULES = {}


with open("./data/19-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if not line:
            continue
        if line[0] == "{":
            INPUTS.append(
                {
                    k: int(v)
                    for item in line[1:-1].split(",")
                    for k, v in [item.split("=")]
                }
            )

        else:
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

result = 0

ops = {">": operator.gt, "<": operator.lt}

for i in INPUTS:
    rule_key = "in"
    run = True
    while run:
        for rule in RULES[rule_key]:
            if "compare" in rule and not ops[rule["compare"]](
                i[rule["part"]], rule["with"]
            ):
                continue
            if rule["to"] == "A":
                result += sum(i.values())
            if rule["to"] in "AR":
                run = False
                break
            rule_key = rule["to"]
            break

print(result)
