#!/usr/bin/env python3
"""a module for task 4"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ a function to execute wait_random n times"""
    l: List = []
    while n != 0:
        b = await asyncio.gather(task_wait_random(max_delay))
        d = b[0]

        for i, val in enumerate(l):
            if d < val:
                l.insert(i, d)
                break
            else:
                l.append(d)
        n -= 1
    return l
