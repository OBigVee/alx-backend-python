#!/usr/bin/env python3
"""Measure the runtime"""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n:int, max_delay:int)->float:
    """n:param
    max_delay:"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n