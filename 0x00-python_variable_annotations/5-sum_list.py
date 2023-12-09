#!/usr/bin/env python3
"""annotate function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum as float"""
    sum = 0.0
    for i in input_list:
        sum += i
    return sum
