#!/usr/bin/env python3

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random
"""import wait random module"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """n: numbers of time to spin wait_random(max_delay)
    max_delay: max number of delay"""
    # list of all delays
    delay_list = []
    spawn_list = []
    for spawn in range(n):
        spawn_list.append(wait_random(max_delay))
    spawn_list = asyncio.as_completed(spawn_list)
    for spawn in spawn_list:
        delay_list.append(await spawn)
    return delay_list
