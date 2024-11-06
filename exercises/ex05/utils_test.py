"""EX05 utils test"""

__author__ = "730648923"

from utils import only_evens
from utils import sub
from utils import add_at_index


# tests for only_evens
def test_only_evens_return() -> None:
    """makes sure fn returns evens from list"""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_mutates() -> None:
    """Checks to see if the inputted list is different than the outputted list"""
    list1: list[int] = [1, 2, 3, 4]
    list_expected: list[int] = [2, 4]
    assert only_evens(list1) == list_expected


def test_only_evens_edge() -> None:
    """Checks to see that if an empty list is given, it will just output that empty list"""
    assert only_evens([]) == []


# Tests for sub
def test_sub_return() -> None:
    """makes sure fn returns correct values from given indicies"""
    userlist: list[int] = [2, 3, 4, 5, 6]
    assert sub(userlist, 0, 2) == [2, 3, 4]


def test_sub_mutates() -> None:
    """Checks to see if the inputted list is different than the outputted list"""
    userlist: list[int] = [2, 3, 4, 5, 6]
    list_expected: list[int] = [2, 3, 4]
    assert sub(userlist, 0, 2) == list_expected


def test_sub_edge() -> None:
    """Checks to see if we give indecies that are out of range, will the
    code function as planned"""
    userlist: list[int] = [2, 3, 4, 5, 6]
    assert sub(userlist, -4, 10) == [2, 3, 4, 5, 6]


# tests for add_at_index
def test_add_at_index_return() -> None:
    """sees if fn returns nothing, as expected"""
    assert add_at_index([1, 2, 3], 2, 2) == None


def test_add_at_index_mutates() -> None:
    """sees if list is mutated when fn is called"""
    OG_list: list[int] = [1, 2, 3]
    OG_list_copy: list[int] = [1, 2, 3]
    assert add_at_index(OG_list, 99, 1) != OG_list_copy


def test_add_at_index_edge() -> None:
    """sees if the function returns index error if index is out of range"""
    OG_list: list[int] = [1, 2, 3]
    assert add_at_index(OG_list, 99, 100) == IndexError
