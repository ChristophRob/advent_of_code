#!/usr/bin/env python3

from collections import Counter

# TEST_RESULT = NA
# REAL_RESULT = 271397390297138


codes = []
with open("./data/21-real.txt") as file:
    for line in file.readlines():
        codes.append(line.strip())

MAPPING = {
    "965A": Counter({"^^^A": 1, "vA": 1, "<A": 1, "vv>A": 1}),
    "^^^A": Counter({"A": 2, "<A": 1, ">A": 1}),
    "vA": Counter({"<vA": 1, "^>A": 1}),
    "<A": Counter({"v<<A": 1, ">>^A": 1}),
    "vv>A": Counter({"<vA": 1, "A": 1, ">A": 1, "^A": 1}),
    "A": Counter({"A": 1}),
    ">A": Counter({"vA": 1, "^A": 1}),
    "<vA": Counter({"v<<A": 1, ">A": 1, "^>A": 1}),
    "^>A": Counter({"<A": 1, "v>A": 1, "^A": 1}),
    "v<<A": Counter({"<vA": 1, "<A": 1, "A": 1, ">>^A": 1}),
    ">>^A": Counter({"vA": 1, "A": 1, "<^A": 1, ">A": 1}),
    "^A": Counter({"<A": 1, ">A": 1}),
    "v>A": Counter({"<vA": 1, ">A": 1, "^A": 1}),
    "<^A": Counter({"v<<A": 1, ">^A": 1, ">A": 1}),
    ">^A": Counter({"vA": 1, "<^A": 1, ">A": 1}),
    "143A": Counter({"^<<A": 1, "^A": 1, "v>>A": 1, "vA": 1}),
    "^<<A": Counter({"<A": 1, "v<A": 1, "A": 1, ">>^A": 1}),
    "v>>A": Counter({"<vA": 1, ">A": 1, "A": 1, "^A": 1}),
    "v<A": Counter({"<vA": 1, "<A": 1, ">>^A": 1}),
    "528A": Counter({"<^^A": 1, "vA": 1, "^^A": 1, "vvv>A": 1}),
    "<^^A": Counter({"v<<A": 1, ">^A": 1, "A": 1, ">A": 1}),
    "^^A": Counter({"<A": 1, "A": 1, ">A": 1}),
    "vvv>A": Counter({"A": 2, "<vA": 1, ">A": 1, "^A": 1}),
    "670A": Counter({"^^A": 1, "<<^A": 1, ">vvvA": 1, ">A": 1}),
    "<<^A": Counter({"v<<A": 1, "A": 1, ">^A": 1, ">A": 1}),
    ">vvvA": Counter({"A": 2, "vA": 1, "<A": 1, "^>A": 1}),
    "973A": Counter({"^^^A": 1, "<<A": 1, "vv>>A": 1, "vA": 1}),
    "<<A": Counter({"v<<A": 1, "A": 1, ">>^A": 1}),
    "vv>>A": Counter({"A": 2, "<vA": 1, ">A": 1, "^A": 1}),
}


result = 0
for code in codes:
    fractions = MAPPING[code]
    for i in range(25):
        new_fractions = Counter()
        for fraction, count in fractions.items():
            f = MAPPING[fraction]
            for k, v in f.items():
                if k not in new_fractions:
                    new_fractions[k] = 0
                new_fractions[k] += v * count
        fractions = new_fractions
    length = sum([v * len(k) for k, v in fractions.items()])
    result += int(code[:-1]) * length

print(result)
