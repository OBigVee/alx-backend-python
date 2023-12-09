#!/usr/bin/env python3
"""type-annotate function"""
from typing import Callable, Union


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier"""

    def function(multiple: float) -> float:
        """callable function"""
        return float(multiplier * multiple)

    return function
