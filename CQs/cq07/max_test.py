"""CQ07 Max Test"""

__author__ = "730648923"

from find_max import find_and_remove_max


def test_return_FAR() -> None:
    """Tests to make sure function returns the right max"""
    assert find_and_remove_max([1, 2, 2, 1, 3, 3, 4, 4]) == 4


def test_mutate_FAR() -> None:
    """Tests to make sure function removes the the max in every instance"""
    test_list: list[int] = [1, 2, 4, 2, 2, 2, 4, 4, 3, 1]
    find_and_remove_max(test_list)
    assert 4 not in test_list


def test_inbounds_FAR() -> None:
    """Makes sure function returns the right output if input value is not in range"""
    list1: list[int] = []
    assert find_and_remove_max(list1) == -1
