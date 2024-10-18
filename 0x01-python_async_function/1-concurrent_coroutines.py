#!/usr/bin/env python3
"""a module to execute multiple coroutines at the same time with async"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ a function to execute wait_random n times"""
    l: List = []
    while n != 0:
        b = await asyncio.gather(wait_random(max_delay))
        d = b[0]
        
        for i, val in enumerate(l):
            if d < val:
                l.insert(i, d)
                break
            else:
                l.append(d)
        n -= 1
    return l
