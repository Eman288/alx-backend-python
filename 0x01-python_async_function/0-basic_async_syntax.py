#!/usr/bin/env python3
"""a module to Write an asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """a function that waits for a random
    delay between 0 and max_delay"""
    y = random.uniform(0, max_delay)
    await asyncio.sleep(y)
    return y
