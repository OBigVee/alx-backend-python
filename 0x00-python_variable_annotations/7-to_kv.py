#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""


from typing import List, Union


def to_kv(k: str, v: List[Union[int, float]]) -> tuple:
    """return tuple"""
    return (k, v ** 2)
