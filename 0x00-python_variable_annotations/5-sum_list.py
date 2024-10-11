#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    a function to return the sum of a list of floats
    """
    s: float = 0.0
    for i in input_list:
        s += i
    return s
