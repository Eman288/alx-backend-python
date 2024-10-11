#!/usr/bin/env python3
"""
8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a function to return another function
    """
    def mul(n: float) -> float:
        """
        a function that return the multiplie of n * multiplier
        """
        return n * multiplier

    return mul
