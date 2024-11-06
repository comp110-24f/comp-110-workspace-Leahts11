"""EX04"""

__author__ = "730648923"

hi: list[int] = [3, 3, 3]


def all(input_list: list[int], num: int) -> bool:
    """checks to see if numbers in list are the same as the given number"""
    if len(input_list) == 0:
        return False
    for elem in input_list:
        if elem != num:
            return False
    return True


def max(input_list: list[int]) -> int:
    """find max in list"""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty list")
    largest = input_list[0]
    for elem in input_list:
        if elem > largest:
            largest = elem
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """see if every element in list equal"""
    if len(list1) != len(list2):
        return False
    for index in range(0, len(list1)):
        if list1[index] != list2[index]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Extend the list"""
    for elem in list2:
        list1.append(elem)
