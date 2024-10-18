#!/usr/bin/env python3
"""a module to execute multiple coroutines at the same time with async"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ a function to execute wait_random n times"""
    l = []
    while n != 0:
        b = asyncio.gather(wait_random(max_delay))
        l.append(await b)
        n -= 1
    return l
