"""CQ03 While Loops"""

__author__ = "730648923"


def num_instances(phrase: str, search_char: str) -> int:
    index: int = 0
    count: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    print(count)
    return count
