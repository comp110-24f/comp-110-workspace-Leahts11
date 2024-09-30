"""EX01 Tea Party"""

__author__ = "730648923"


def main_planner(guests: int) -> None:
    """prints info about the details of the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """tells you how many tea bags you will need for the tea party depending on the
    number of people attending!"""
    return people * 2


def treats(people: int) -> int:
    """tells you how many treats you will need depending on the number of people
    attending the tea party"""
    return int((tea_bags(people=people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """finds cost of tea + treats total"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
