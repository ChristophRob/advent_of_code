#!/usr/bin/env python3

# TEST_RESULT = 12
# REAL_RESULT = 229839456

with open("./data/14-real.txt") as file:
    INPUT = [line.strip() for line in file.readlines()]

WIDE = 11 if len(INPUT) < 20 else 101
TALL = 7 if len(INPUT) < 20 else 103

end_positions = []
for line in INPUT:
    _, p, v = line.split("=")
    px, py = [int(i) for i in p.split(" ")[0].split(",")]
    vx, vy = [int(i) for i in v.split(",")]
    x = (px + 100 * vx) % WIDE
    y = (py + 100 * vy) % TALL
    end_positions.append((x, y))


lu = ld = ru = rd = 0
for x, y in end_positions:
    rd += 1 if x > WIDE // 2 and y > TALL // 2 else 0
    ld += 1 if x < WIDE // 2 and y > TALL // 2 else 0
    ru += 1 if x > WIDE // 2 and y < TALL // 2 else 0
    lu += 1 if x < WIDE // 2 and y < TALL // 2 else 0

print(lu * ld * ru * rd)
