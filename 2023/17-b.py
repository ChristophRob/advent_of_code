#!/usr/bin/env python3

# TEST_RESULT = 94
# REAL_RESULT = 748

from heapq import heappush, heappop
from itertools import count
from time import time

start_time = time()


def solve():
    _push = heappush
    _pop = heappop
    G = []
    with open("./data/17-real.txt") as file:
        for line in file.readlines():
            row = [int(i) for i in line.strip()]
            G.append(row)

    LEN_Y = len(G)
    LEN_X = len(G[0])

    SEEN = set()

    UP, RIGHT, LEFT, DOWN = (-1, 0), (0, 1), (0, -1), (1, 0)
    ORIS_ALL = {
        UP: [UP, RIGHT, LEFT],
        DOWN: [DOWN, RIGHT, LEFT],
        RIGHT: [RIGHT, UP, DOWN],
        LEFT: [LEFT, UP, DOWN],
    }
    ORIS_STRAIGHT = {
        UP: [UP],
        DOWN: [DOWN],
        RIGHT: [RIGHT],
        LEFT: [LEFT],
    }

    goal = (LEN_Y - 1, LEN_X - 1)
    counter = count()
    queue = []
    _push(queue, (0, -2, 0, (0, 0), DOWN))
    _push(queue, (0, -1, 0, (0, 0), RIGHT))
    while queue:
        value, _, cons, point, orient = _pop(queue)
        if point == goal:
            result = value
            break
        oris = ORIS_STRAIGHT if cons < 4 else ORIS_ALL
        for new_orient in oris[orient]:
            new_point = (point[0] + new_orient[0], point[1] + new_orient[1])
            if not (0 <= new_point[0] < LEN_Y and 0 <= new_point[1] < LEN_X):
                continue
            new_consecutive = cons + 1 if new_orient == orient else 1
            if new_consecutive > 10:
                continue
            new_value = value + G[new_point[0]][new_point[1]]
            if (new_consecutive, new_point, new_orient) in SEEN:
                continue
            SEEN.add((new_consecutive, new_point, new_orient))
            state = (
                new_value,
                next(counter),
                new_consecutive,
                new_point,
                new_orient,
            )
            _push(queue, state)

    print(f"Result: {result}")
    print(f"End time {time() - start_time}")


solve()
