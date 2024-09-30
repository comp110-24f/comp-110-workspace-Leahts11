"""Coordinates CQ4"""

__author__ = "730648923"


def get_coords(xs: str, ys: str) -> None:
    """Mix and match each index of one var with another"""
    index: int = 0
    index2: int = 0
    while index < len(xs):
        while index2 < len(ys):
            print("(" + xs[index] + "," + ys[index2] + ")")
            index2 += 1
        index += 1
        index2 = 0
