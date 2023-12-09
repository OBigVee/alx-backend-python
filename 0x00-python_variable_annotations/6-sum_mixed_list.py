#!/usr/bin/env python
"""type-annotation"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns sum as float"""
    sum: float = 0.0
    for i in mxd_list:
        sum += i
    return sum
