#!/usr/bin/env python

# 
# https://adventofcode.com/2021/day/1
# 

from collections import deque
from pathlib import Path

path = Path(__file__).parent / "day01input.txt"

with path.open() as f:
    depths = [int(num.strip()) for num in f.readlines()]

# Part 1
increases = 0
last = 0
for depth in depths:
    if last == 0:
        last = depth
    elif depth > last:
        increases += 1
    last = depth

print("Part 1:", increases)

# Part 2
window = deque()

increases = 0
last_sum = 0
for depth in depths:
    if len(window) < 3:
        window.append(depth)
        last_sum = sum(window)
        continue
    
    if last_sum == 0:
        last_sum = sum(window)
        continue

    window.popleft()
    window.append(depth)
    this_sum = sum(window)
    print("this_sum", this_sum)
    
    if this_sum > last_sum:
        increases += 1
    
    last_sum = this_sum

print("Part 2:", increases)
