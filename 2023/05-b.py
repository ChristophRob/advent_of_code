#!/usr/bin/env python3

# TEST_RESULT = 46
# REAL_RESULT = 77435348


seeds = None
M = []
cur = None
with open("./data/05-real.txt") as file:
    for line in file.readlines():
        line = line.strip()

        if "seeds" in line:
            seeds = [int(i) for i in line.split()[1:]]
            seeds = [
                (seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)
            ]

        elif "map" in line:
            cur = []
            M.append(cur)
        elif line:
            cur.append([int(i) for i in line.split()])


for m in M:
    new_seeds = []
    while len(seeds) > 0:
        seed_start, seed_end = seeds.pop()

        for to, fro, le in m:
            overlap_start = max(seed_start, fro)
            overlap_end = min(seed_end, fro + le)

            if overlap_start < overlap_end:
                new_seeds.append((overlap_start - fro + to, overlap_end - fro + to))
                if overlap_start > seed_start:
                    seeds.append((seed_start, overlap_start))
                if seed_end > overlap_end:
                    seeds.append((overlap_end, seed_end))
                break
        else:
            new_seeds.append((seed_start, seed_end))

    seeds = new_seeds

print(min(r[0] for r in seeds))
