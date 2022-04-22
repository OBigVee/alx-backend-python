#!/usr/bin/env python3
""" micmic wait-random """
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ new Task is created """
    return asyncio.create_task(wait_random(max_delay))