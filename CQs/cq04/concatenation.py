"""Concatenation CQ4"""

__author__ = "730648923"

word1: str = "happy"
word2: str = "tuesday"


def concat(p1: str, p2: str) -> str:
    """Concatenates two strings"""
    print(p1 + p2)
    return p1 + p2


if __name__ == "__main__":
    concat(word1, word2)
