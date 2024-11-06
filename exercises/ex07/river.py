"""File to define River class."""

__author__ = "730648923"

from ex07.fish import Fish
from ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """making sure ages align with given ages that survive"""
        surviving_bears = []
        surviving_fish = []

        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)

        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)

        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def check_hunger(self):
        """removes bears with hunger score < 0"""
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        return None

    def remove_fish(self, num: int):
        """Remove given amount of Fish from the River starting from  front"""
        for _ in range(num):
            if self.fish:
                self.fish.pop(0)

    def bears_eating(self):
        """each Bear eats fish from the river if enough are available."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

        return None

    def repopulate_fish(self):
        """Add new fish to  river based on the current fish population"""
        num_fish = len(self.fish)
        new_fish = (num_fish // 2) * 4

        while new_fish > 0:
            self.fish.append(Fish())
            new_fish -= 1
        return None

    def repopulate_bears(self):
        """Add new bears to river based on the current bear population"""
        num_bears = len(self.bears)
        new_bears = num_bears // 2

        while new_bears > 0:
            self.bears.append(Bear())
            new_bears -= 1
        return None

    def view_river(self):
        """Print day and population of bears and fish"""
        print(f"~~~ Day{self.day}: ~~~")
        print(f"Fish population:{len(self.fish)}")
        print(f"Bear population:{len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        # simulate 7 days of life in river
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
