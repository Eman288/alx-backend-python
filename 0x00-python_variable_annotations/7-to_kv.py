#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    a function to create a tuple of the k and v
    """
    s: float = v * v
    return (k, s)
