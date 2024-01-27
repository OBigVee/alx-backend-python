#!/usr/bin/env python3
"""Tasks 4"""

import asyncio
from typing import List

wait_n = __import__("1-concurrent_coroutines").wait_n
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ """
    delay_list = []
    spawn_list = []
    for spawn in range(n):
        spawn_list.append(task_wait_random(max_delay))
    spawn_list = asyncio.as_completed(spawn_list)
    for spawn in spawn_list:
        delay_list.append(await spawn)
    return delay_list
