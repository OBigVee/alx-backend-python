#!/usr/bin/env python3

""" Measure time: Run time for four parallel comprehensions """
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ execution time """
    sTime = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    elapsed = time.perf_counter() - sTime
    return elapsed
