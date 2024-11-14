"""File to define Fish class."""

__author__ = "730648923"


class Fish:
    """Class defining fish!"""

    age: int

    def __init__(self):
        """Initializing age for fish."""
        self.age = 0
        return None

    def one_day(self):
        """Describing what happens to fish after a day."""
        self.age += 1
        return None
