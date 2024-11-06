"""EX05 utils"""

__author__ = "730648923"


def only_evens(list1: list[int]) -> list:
    """from list of integers, returns only even ones"""
    list_evens: list[int] = []
    for elem in list1:
        if elem % 2 == 0:
            list_evens.append(elem)
    return list_evens


def sub(userlist: list[int], start: int, end: int) -> list:
    """returns values in given list that are between two given indicies"""
    list_mutated: list[int] = []
    if start < 0:
        start = 0
    if end > len(userlist):
        end = len(userlist)
    if len(userlist) == 0 or start >= len(userlist) or end <= 0:
        return list_mutated
    for i in range(start, end):
        list_mutated.append(userlist[i])
    return list_mutated


def add_at_index(userlist: list[int], added: int, index: int) -> None:
    """Adds something at index of user choosing"""
    if index > len(userlist) or index < 0:
        raise IndexError("Index is out of bounds for the input list")
    userlist.append(0)
    for i in range(len(userlist) - 1, index, -1):
        """shifts all elements to right"""
        userlist[i] = userlist[i - 1]
    userlist[index] = added
