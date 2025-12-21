#!/usr/bin/env python3

# TEST_RESULT = 405
# REAL_RESULT = 33735

result = 0

PUZZLES = []

with open("./data/13-real.txt") as file:
    P = []
    PUZZLES.append(P)
    for line in file.readlines():
        line = line.strip()
        if line:
            P.append(line)
        else:
            P = []
            PUZZLES.append(P)


for P in PUZZLES:
    configs = [
        (len(P[0]), len(P), True),
        (len(P), len(P[0]), False),
    ]
    for cand_len, check_len, vertical in configs:
        candidates = [i for i in range(cand_len - 1)]
        for check in range(check_len):
            new_candidates = []
            for i in candidates:
                for xi in range(cand_len):
                    if i - xi < 0 or i + xi + 1 >= cand_len:
                        continue
                    if vertical and P[check][i - xi] != P[check][i + 1 + xi]:
                        break
                    if not vertical and P[i - xi][check] != P[i + 1 + xi][check]:
                        break
                else:
                    new_candidates.append(i)
            candidates = new_candidates
        if len(candidates) == 1:
            result += (candidates[0] + 1) * (1 if vertical else 100)
            break

print(result)
