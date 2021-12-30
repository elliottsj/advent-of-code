#!/usr/bin/env python

# 
# https://adventofcode.com/2021/day/1
# 

from pathlib import Path

path = Path(__file__).parent / "day01input.txt"

with path.open() as f:
    depths = [int(num.strip()) for num in f.readlines()]
    print(depths)
