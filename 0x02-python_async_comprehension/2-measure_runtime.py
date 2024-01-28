#!/usr/bn/python3
"""run time for four parallel comprehensions"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """corountine measures"""
    start_time = time.perf_counter()
    futures = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    done, _ = await asyncio.wait(futures)
    end_time = time.perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
