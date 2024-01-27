#!/bin/usr/env python3
"""Tasks 4"""
import asyncio
from typing import List

wait_n = __import__("1-concurrent_coroutines").wait_n
task_wait_random = __import__("3-tasks").task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ """
    return task_wait_random(n, max_delay)
