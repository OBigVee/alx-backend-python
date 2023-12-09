#!/usr/bin/env python3
"""type-annotation function"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """returns a tuple"""
    return (k, v ** 2)
