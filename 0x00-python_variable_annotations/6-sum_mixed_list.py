#!/usr/bin/env python3
"""
6. Complex types - mixed list
"""
from typing import List, Optional, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a function to sum the values in a list
    """
    s: float = 0.0
    for i in mxd_lst:
        s += i
    return s
