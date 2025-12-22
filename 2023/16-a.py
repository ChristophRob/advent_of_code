#!/usr/bin/env python3

# TEST_RESULT = 46
# REAL_RESULT = 7434

result = 0

left, right, up, down = (0, -1), (0, 1), (-1, 0), (1, 0)

SEEN_P = set([(0, 0)])
SEEN_M = set([(0, 0, right)])

G = []

with open("./data/16-real.txt") as file:
    for line in file.readlines():
        G.append(list(line.strip()))

queue = [(0, 0, right)]
max_x = len(G[0]) - 1
max_y = len(G) - 1


def move(y, x, d):
    y, x = y + d[0], x + d[1]
    if y < 0 or x < 0 or y > max_y or x > max_x or (y, x, d) in SEEN_M:
        return
    SEEN_M.add((y, x, d))
    SEEN_P.add((y, x))
    queue.append((y, x, d))


turn = {
    up: [right, left],
    down: [left, right],
    left: [down, up],
    right: [up, down],
}

while queue:
    y, x, d = queue.pop(0)
    p = G[y][x]
    match p:
        case ".":
            move(y, x, d)
        case "|":
            if d in (right, left):
                move(y, x, up)
                move(y, x, down)
            else:
                move(y, x, d)
        case "-":
            if d in (up, down):
                move(y, x, left)
                move(y, x, right)
            else:
                move(y, x, d)
        case "/":
            move(y, x, turn[d][0])
        case "\\":
            move(y, x, turn[d][1])

print(len(SEEN_P))
