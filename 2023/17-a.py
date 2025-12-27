#!/usr/bin/env python3

# TEST_RESULT = 102
# REAL_RESULT = 638
import heapq
from typing import NamedTuple
from itertools import count

G = []
total = 0
with open("./data/17-real.txt") as file:
    for line in file.readlines():
        row = [int(i) for i in line.strip()]
        total += sum(row)
        G.append(row)

LEN_Y = len(G)
LEN_X = len(G[0])
avg_hl = total // (LEN_Y * LEN_X) + 1
print("AVG", avg_hl)

SEEN = {(0, complex(0, 0), complex(1, 0)): 0}


class State(NamedTuple):
    priority: int
    tiebreaker: int
    value: int
    consecutive: int
    point: complex
    orientation: complex


start = State((LEN_Y + LEN_X) * avg_hl, 0, 0, 0, complex(0, 0), complex(1, 0))


def possible_orients(ori: complex):
    return [ori, ori * 1j, ori * -1j]


def calc_priority(point: complex, value: int):
    return int((value + (LEN_Y - point.real + LEN_X - point.imag) * avg_hl).real)


goal = complex(LEN_Y - 1, LEN_X - 1)
counter = count()

queue = []
heapq.heappush(queue, start)
result = None

while queue:
    priority, _, value, cons, point, orient = heapq.heappop(queue)
    for new_orient in possible_orients(orient):
        new_point = point + new_orient
        if not (0 <= new_point.real < LEN_Y and 0 <= new_point.imag < LEN_X):
            continue
        new_consecutive = cons + 1 if new_orient == orient else 1
        if new_consecutive > 3:
            continue
        new_value = value + G[int(new_point.real)][int(new_point.imag)]
        if result and result <= new_value:
            continue
        if new_point == goal:
            print(new_value)
            result = new_value
        if (new_consecutive, new_point, new_orient) in SEEN and SEEN[
            (new_consecutive, new_point, new_orient)
        ] <= new_value:
            continue
        SEEN[(new_consecutive, new_point, new_orient)] = new_value
        new_priority = calc_priority(new_point, new_value)
        state = State(
            new_priority,
            next(counter),
            new_value,
            new_consecutive,
            new_point,
            new_orient,
        )
        heapq.heappush(queue, state)

print(result)
