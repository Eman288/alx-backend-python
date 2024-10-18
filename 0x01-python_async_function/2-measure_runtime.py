#!/usr/bin/env python3
"""a module to measure the runtime"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """a function to return the total_time / n"""
    startTime = time.time()
    asyncio.run(wait_n(n, max_delay))
    endTime = time.time()
    return (endTime - startTime) / n
