#!/usr/bin/env python3

# TEST_RESULT = NA
# REAL_RESULT = hf,hz,lb,lm,ls,my,ps,qu,ra,uc,vi,xz,yv

connections = []
with open("./data/23-real.txt") as file:
    for line in file.readlines():
        connections.append(line.strip().split("-"))


MAP = {}
for x, y in connections:
    if x not in MAP:
        MAP[x] = []
    MAP[x].append(y)
    if y not in MAP:
        MAP[y] = []
    MAP[y].append(x)

ALL = set([])
for k, conns in MAP.items():
    inter = set(conns + [k])
    for conn in conns:
        new_inter = inter & set(MAP[conn] + [conn])
        if len(new_inter) >= len(inter) - 1:
            inter = new_inter
        else:
            try:
                inter.remove(conn)
            except KeyError:
                pass
    if len(inter) >= 13:
        ALL.add(frozenset(inter))

for a in ALL:
    res = list(a)
    res.sort()
    print(",".join(res))
