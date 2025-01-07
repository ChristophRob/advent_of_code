#!/usr/bin/env python3

# TEST_RESULT = 64
# REAL_RESULT = 520

import sys

sys.setrecursionlimit(10000)

with open("./data/16-real.txt") as file:
    GRID = [list(line.strip()) for line in file.readlines()]

CLOCKWISE_ORDER = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Position(object):
    def __init__(self, x, y, value, orientation, goal=None):
        self.x = x
        self.y = y
        self.value = value
        self.orientation = orientation
        if best_values[y][x] is None or best_values[y][x].value >= value:
            best_values[y][x] = self
        self.goal = goal
        self.relevant = False

    def go(self):
        result = []
        if self.goal and self.value > self.goal:
            return result
        straight = self.go_straight()
        left = self.go_left()
        right = self.go_right()

        for value in straight + left + right:
            if value:
                result.append(value)
        if self.goal and self.goal in result:
            self.relevant = True
        return result

    def go_straight(self):
        new_value = self.value + 1
        return self.create_new_position(new_value, self.orientation)

    def go_left(self):
        orientation = CLOCKWISE_ORDER[CLOCKWISE_ORDER.index(self.orientation) - 1]
        new_value = self.value + 1001
        return self.create_new_position(new_value, orientation)

    def go_right(self):
        orientation = CLOCKWISE_ORDER[
            (CLOCKWISE_ORDER.index(self.orientation) + 1) % len(CLOCKWISE_ORDER)
        ]
        new_value = self.value + 1001
        return self.create_new_position(new_value, orientation)

    def create_new_position(self, new_value, orientation):
        new_x = self.x + orientation[0]
        new_y = self.y + orientation[1]
        pos_value = GRID[new_y][new_x]
        if pos_value == ".":
            existing_pos = best_values[new_y][new_x]
            if existing_pos is None or existing_pos.value >= new_value - 1000:
                new_pos = Position(new_x, new_y, new_value, orientation, self.goal)
                return new_pos.go()
            return []
        elif pos_value == "#":
            return []
        elif pos_value == "E":
            return [new_value]


def init_best_values():
    global best_values
    best_values = []
    for y, line in enumerate(GRID):
        best_line = []
        for x, v in enumerate(line):
            best_line.append(None)
        best_values.append(best_line)


best_values = []
for y, line in enumerate(GRID):
    best_line = []
    for x, v in enumerate(line):
        best_line.append(None)
        if v == "S":
            y_start, x_start = y, x
    best_values.append(best_line)
values = Position(x_start, y_start, 0, (1, 0)).go()
goal = min(values)
init_best_values()
Position(x_start, y_start, 0, (1, 0), goal).go()
result = 1
for y, line in enumerate(best_values):
    for x, pos in enumerate(line):
        if pos and pos.relevant:
            result += 1
print(result)