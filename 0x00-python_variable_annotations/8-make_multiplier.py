#!/usr/bin/env python3
"""Complex types - functions"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier"""

    def function(multiple: float) -> float:
        """callable function"""
        return float(multiplier * multiple)

    return function
