#!/usr/bin/env python3
"""a module for task0"""
import random
import asyncio
from typing import Generator

async def async_generator() -> Generator[int, None, None]:
    """a function to yield a random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield int(random.uniform(0, 10))
