"""Summing the elements of a list using different loops"""

__author__ = "730648923"


def w_sum(vals: list[float]) -> float:
    """adds up the values"""
    total: float = 0.0
    i = 0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total


def f_sum(vals: list[float]) -> float:
    """using the for in loop"""
    total: float = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """using the range for in"""
    total: float = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total
