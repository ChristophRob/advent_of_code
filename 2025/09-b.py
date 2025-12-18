#!/usr/bin/env python3

# TEST_RESULT = 50
# REAL_RESULT = 1550760868

N = []
A = []
max_x, max_y = 0, 0


with open("./data/09-real.txt") as file:
    for line in file.readlines():
        x1, y1 = [int(i) for i in line.split(",")]
        max_x, max_y = max(x1, max_x), max(y1, max_y)
        for x2, y2 in N:
            A.append(((abs(x2 - x1) + 1) * (abs(y2 - y1) + 1), (x1, y1), (x2, y2)))
        N.append((x1, y1))

A = sorted(A, key=lambda tup: tup[0], reverse=True)

G = []

for (px, py), (qx, qy) in zip(N, N[1:] + N[:1]):
    if px == qx:
        for y in range(min(py, qy) + 1, max(py, qy), 1):
            G.append((px, y))
    if py == qy:
        for x in range(min(px, qx) + 1, max(px, qx), 1):
            G.append((x, py))


for res, (x1, y1), (x2, y2) in A:
    print(res)
    xs, ys, xl, yl = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    for xn, yn in N:
        if xs + 1 < xn and xn < xl - 1 and ys + 1 < yn and yn < yl - 1:
            break
    else:
        for xn, yn in G:
            if xs + 1 < xn and xn < xl - 1 and ys + 1 < yn and yn < yl - 1:
                break
        else:
            print((x1, y1), (x2, y2))
            print(f"Found it {res}")
            break


GRID = []
for y in range(9):
    row = []
    for x in range(14):
        if (x, y) in [(x1, y1), (x2, y2)]:
            row.append("O")
        elif (x, y) in N:
            row.append("X")
        elif (x, y) in G:
            row.append("Z")
        else:
            row.append(".")

    GRID.append(row)

for row in GRID:
    print("".join(str(i) for i in row))
