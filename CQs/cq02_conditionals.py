"""CQ00"""

__author__ = "730648923"


def guess_a_number() -> None:
    """Number guessing game!"""
    secret: int = 7
    x: int = int(input("Guess a number: "))
    print("Your guess was", x)
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is 7")
    elif x > secret:
        print("Your guess was too high! The secret number is 7")


if __name__ == "__main__":
    guess_a_number()
