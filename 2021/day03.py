#!/usr/bin/env python

# 
# https://adventofcode.com/2021/day/3
# 

from collections import deque
from pathlib import Path

path = Path(__file__).parent / "day03input.txt"

gamma_rate = {}
# 10110
# {
#   0: 3
#   1: -1
#   2: 2
#   3: 1
#   4: -2
# }

with path.open() as f:
    nums = [num.strip() for num in f.readlines()]

for num in nums:
    for i, bit in enumerate(num):
        if bit == '1':
            gamma_rate[i] = gamma_rate.get(i, 0) + 1
        else:
            gamma_rate[i] = gamma_rate.get(i, 0) - 1    

gamma_rate_str = ''.join(('1' if gamma_rate[i] > 0 else '0') for i in gamma_rate)
epsilon_rate_str = ''.join(('1' if gamma_rate[i] < 0 else '0') for i in gamma_rate)

def to_decimal(binary_str):
    result = 0
    for bit in binary_str:
        result *= 2
        result += int(bit)
    return result

print("Part 1")
print("gamma_rate", gamma_rate)
print("gamma_rate_str", gamma_rate_str)
print("epsilon_rate_str", epsilon_rate_str)
print("power", to_decimal(gamma_rate_str) * to_decimal(epsilon_rate_str))

def find_oxygen_generator_rating(indices_matching_bit_criteria, bit_pos):
    if len(indices_matching_bit_criteria) == 1:
        return nums[next(iter(indices_matching_bit_criteria))]
    
    keep_indices = set()
    most_common_bit_scale = 0
    for index in indices_matching_bit_criteria:
        if nums[index][bit_pos] == '1':
            most_common_bit_scale += 1
        else:
            most_common_bit_scale -= 1
    
    most_common_bit = '1' if most_common_bit_scale >= 0 else '0'
    for index in indices_matching_bit_criteria:
        if nums[index][bit_pos] == most_common_bit:
            keep_indices.add(index)

    return find_oxygen_generator_rating(keep_indices, bit_pos + 1)

def find_co2_scrubber_rating(indices_matching_bit_criteria, bit_pos):
    if len(indices_matching_bit_criteria) == 1:
        return nums[next(iter(indices_matching_bit_criteria))]
    
    keep_indices = set()
    most_common_bit_scale = 0
    for index in indices_matching_bit_criteria:
        if nums[index][bit_pos] == '1':
            most_common_bit_scale += 1
        else:
            most_common_bit_scale -= 1
    
    least_common_bit = '0' if most_common_bit_scale >= 0 else '1'
    for index in indices_matching_bit_criteria:
        if nums[index][bit_pos] == least_common_bit:
            keep_indices.add(index)

    return find_co2_scrubber_rating(keep_indices, bit_pos + 1)


oxygen_generator_rating = find_oxygen_generator_rating(
    indices_matching_bit_criteria=set(range(len(nums))),
    bit_pos=0
)
co2_scrubber_rating = find_co2_scrubber_rating(
    indices_matching_bit_criteria=set(range(len(nums))),
    bit_pos=0
)

print("Part 2")
print("oxygen_generator_rating", to_decimal(oxygen_generator_rating))
print("co2_scrubber_rating", to_decimal(co2_scrubber_rating))
print("life_support_rating", to_decimal(oxygen_generator_rating) * to_decimal(co2_scrubber_rating))
