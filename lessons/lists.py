"""How to do lists"""

# creating empty lists
numbers: list[float] = []  # literal
letters: list[str] = list()  # constructor

numbers.append(1.5)
numbers.append(3.0)
"print(numbers)"

# create already populated list
game_pts: list[int] = [102, 93, 132]
"print(game_pts)"
"print(game_pts[1])"

# lists can be changed (mutable)
"""game_pts[2] = 20"""

# get length
"""print(len(game_pts))"""

# remove something from list
game_pts.pop(1)
print(game_pts)
"""Note that your index moves as you remove/add things to your list"""


def display(number_list: list[int]) -> None:
    print(number_list)


display(game_pts)
