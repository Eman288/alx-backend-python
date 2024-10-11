#!/usr/bin/env python3
from typing import List
"""
5. Complex types - list of floats
"""


def sum_list(input_list: List[float]) -> float:
    """
    a function to return the sum of a list of floats
    """
    s: float = 0.0
    for i in input_list:
        s += i
    return s
