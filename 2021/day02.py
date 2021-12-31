#!/usr/bin/env python

# 
# https://adventofcode.com/2021/day/1
# 

from collections import deque
from pathlib import Path

path = Path(__file__).parent / "day02input.txt"

x_position = 0
depth = 0
with path.open() as f:
    for command in f.readlines():
        direction, amount = command.strip().split()
        if direction == 'forward':
            x_position += int(amount)
        elif direction == 'down':
            depth += int(amount)
        else:
            depth -= int(amount)

print("Part 1")
print("x_position", x_position)
print("depth", depth)
print("x_position * depth", x_position * depth)

x_position = 0
depth = 0
aim = 0
with path.open() as f:
    for command in f.readlines():
        direction, amount = command.strip().split()
        if direction == 'forward':
            x_position += int(amount)
            depth += aim * int(amount)
        elif direction == 'down':
            aim += int(amount)
        else:
            aim -= int(amount)

print("Part 2")
print("x_position", x_position)
print("depth", depth)
print("aim", aim)
print("x_position * depth", x_position * depth)
