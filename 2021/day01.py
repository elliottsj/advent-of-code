#!/usr/bin/env python

# 
# https://adventofcode.com/2021/day/1
# 

from pathlib import Path

path = Path(__file__).parent / "day01input.txt"

with path.open() as f:
    depths = [int(num.strip()) for num in f.readlines()]

increases = 0
last = 0
for depth in depths:
    if last == 0:
        last = depth
    elif depth > last:
        increases += 1
    last = depth

print(increases)
