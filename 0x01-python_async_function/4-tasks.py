#!/usr/bin/env python3
"""Tasks 4"""

import asyncio
from typing import List

wait_n = __import__("1-concurrent_coroutines").wait_n
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """alter wait_n into task_wait_n"""
    delay_task_list = []
    spawn_task = []
    for spawn in range(n):
        spawn_task.append(task_wait_random(max_delay))
    spawn_task = asyncio.as_completed(spawn_task)
    for spawn in spawn_task:
        delay_task_list.append(await spawn)
    return delay_task_list
