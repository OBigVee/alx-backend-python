#!/usr/bin/env python3
"""Async comprehensions list"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """collect async generated list"""
    # collector = []
    # async for i in async_generator():
    #     collector.append(i)
    # return collector

    return [i async for i in async_generator()]
