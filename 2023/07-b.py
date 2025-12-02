#!/usr/bin/env python3
from collections import defaultdict

# TEST_RESULT =
# REAL_RESULT =

FIVE = "9"
FOUR = "8"
FULL = "7"
THREE = "6"
TWO_PAIR = "5"
PAIR = "4"
HIGH = "3"

STRENGTHS = {
    "T": "10",
    "J": "01",  # JOKER Value
    "Q": "12",
    "K": "13",
    "A": "14",
}
for i in range(2, 10):
    STRENGTHS[str(i)] = "0" + str(i)


def evaluate_value(cards):
    val = ""
    occs = defaultdict(int)
    for i in cards:
        occs[i] += 1
    jokers = occs.get("J", 0)
    occs["J"] = 0
    c = sorted(occs.values(), key=int, reverse=True)
    c[0] += jokers

    if c[0] == 5:
        val += FIVE
    elif c[0] == 4:
        val += FOUR
    elif c[0] == 3 and c[1] == 2:
        val += FULL
    elif c[0] == 3:
        val += THREE
    elif c[0] == 2 and c[1] == 2:
        val += TWO_PAIR
    elif c[0] == 2:
        val += PAIR
    elif len(c) in [5, 6]:
        val += HIGH
    else:
        raise ValueError(c)
    for i in cards:
        val += STRENGTHS[i]
    return val


bids = []
with open("./data/07-real.txt") as file:
    for line in file.readlines():
        cards, bid = line.strip().split(" ")
        val = evaluate_value(cards)
        bids.append((int(bid), val))

res = 0
for idx, b in enumerate(sorted(bids, key=lambda x: x[1])):
    res += (idx + 1) * b[0]

print(res)
