"""File to define Bear class."""

__author__ = "730648923"


class Bear:
    """class defining bear!"""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing age and hunger score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Says what happens to age and hunger score per day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increase hunger score by number of fish eaten."""
        self.hunger_score += num_fish
