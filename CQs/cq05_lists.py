"""Mutating functions."""

__author__ = "730648923"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(lst: list[int], num: int) -> None:
    lst.append(num)


def double(lst: list[int]) -> None:
    idx: int = 0
    while idx < len(lst):
        lst[idx] = lst[idx] * 2
        idx += 1


double(list_2)
print(list_2)
print(list_1)
