#!/usr/bin/env python3

# TEST_RESULT = 126384
# REAL_RESULT = 222670


codes = []
with open("./data/21-real.txt") as file:
    for line in file.readlines():
        codes.append(line.strip())


NAV = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

NUMBERS = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}


D = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
    "A": (0, 0),
}


class XException(Exception):
    pass


def move(cy, cx, char, pad):
    dy, dx = D[char]
    new_cursor = (cy + dy, cx + dx)
    if new_cursor not in pad.values():
        raise XException(f"cursor {new_cursor} out of bounds")
    return new_cursor


def backwards(code, pad):
    cy, cx = pad["A"]
    inputs = [""]
    for char in code:
        new_inputs = ["", ""]
        y, x = pad[char]
        cy_backup, cx_backup = cy, cx
        try:
            while cy != y:
                i = "^" if cy > y else "v"
                new_inputs[0] += i
                (cy, cx) = move(cy, cx, i, pad)
            while cx != x:
                i = "<" if cx > x else ">"
                new_inputs[0] += i
                (cy, cx) = move(cy, cx, i, pad)
        except XException:
            del new_inputs[0]
        cy, cx = cy_backup, cx_backup
        try:
            while cx != x:
                i = "<" if cx > x else ">"
                new_inputs[-1] += i
                (cy, cx) = move(cy, cx, i, pad)
            while cy != y:
                i = "^" if cy > y else "v"
                new_inputs[-1] += i
                (cy, cx) = move(cy, cx, i, pad)
        except XException:
            del new_inputs[-1]
            cy, cx = cy_backup, cx_backup
            for m in new_inputs[0]:
                (cy, cx) = move(cy, cx, m, pad)
        update_inputs = []
        for i in inputs:
            for j in list(set(new_inputs)):
                update_inputs.append(i + j + "A")
        inputs = update_inputs
    return inputs


result = 0
for code in codes:
    A = backwards(code, NUMBERS)
    for i in range(2):
        B = []
        for a in A:
            B += backwards(a, NAV)
        A = B
    result += int(code[:-1]) * min([len(i) for i in A])

print(result)
