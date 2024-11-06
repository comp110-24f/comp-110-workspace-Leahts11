"""CQ07 Find Max"""

__author__ = "730648923"


def find_and_remove_max(list1: list[int]) -> int:
    """Finds the largest number in list and deletes all duplicates"""
    max_nums: int = 0
    i: int = 0
    if list1 == []:
        return -1
    for elem in list1:
        if elem > max_nums:
            max_nums = elem
    while i < len(list1):
        if list1[i] == max_nums:
            list1.pop(i)
        else:
            i += 1
    return max_nums
