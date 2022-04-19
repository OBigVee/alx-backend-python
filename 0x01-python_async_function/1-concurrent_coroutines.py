#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """n: numbers of time to spin wait_random(max_delay)
    max_delay: max number of delay"""
    delay_list = []
    spawn_list = []
    for spawn in range(n):
        spawn_list.append(wait_random(max_delay))
    spawn_list = asyncio.as_completed(spawn_list)
    for spawn in spawn_list:
        delay_list.append(await spawn)
    return delay_list
