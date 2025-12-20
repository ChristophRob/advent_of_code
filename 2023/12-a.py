#!/usr/bin/env python3

# TEST_RESULT = 21
# REAL_RESULT = 6852

import time

result = 0
P = []
start = time.time()
with open("./data/12-real.txt") as file:
    for line in file.readlines():
        s, ns = line.strip().split()
        ns = [int(n) for n in ns.split(",")]
        P.append((s, ns))


for s, ns in P:
    counts = {
        "?": 0,
        "#": 0,
        ".": 0,
    }
    for c in s:
        counts[c] += 1
    counts["g#"] = sum(ns)
    counts["g."] = len(s) - counts["g#"]
    queue = [(s, counts["g."] - counts["."], counts["g#"] - counts["#"])]
    while queue:
        ps, dots_left, hash_left = queue.pop(0)
        try:
            i = ps.index("?")
            sg = ps[:i].replace(".", " ").split()
            if sg and (
                not [len(c) for c in sg[:-1]] == ns[: len(sg) - 1]
                or len(sg) > len(ns)
                or len(sg[-1]) > ns[len(sg) - 1]
                or counts["g#"] > len(ps.replace(".", ""))
            ):
                continue
            if dots_left:
                ds = ps[:i] + "." + ps[i + 1 :]
                queue.append((ds, dots_left - 1, hash_left))
            if hash_left:
                ds = ps[:i] + "#" + ps[i + 1 :]
                queue.append((ds, dots_left, hash_left - 1))
        except ValueError:
            sg = ps.replace(".", " ").split()
            if ns == [len(c) for c in sg]:
                result += 1

print(result)
end = time.time()
print(end - start)
