"""EX03 Wordle"""

__author__ = "730648923"
secret_word: str = ""


def input_guess(correct_length: int):
    while True:
        guess = input(f"Enter a guess with {correct_length} characters: ")
        if len(guess) == correct_length:
            return guess
        else:
            print(
                f"Your guess must be exactly {correct_length} characters long. Try again: ",
                guess,
            )


def contains_char(user_word: str, one_char: str) -> bool:
    """parces through user's word and searches to see if a character is present in the word"""
    assert len(one_char) == 1
    index: int = 0
    while index < len(user_word):
        if user_word[index] == one_char:
            return True
        else:
            index += 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Will give emojis based on if user guess matches secret word"""
    assert len(user_guess) == len(secret_word)
    index: int = 0
    result: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(user_guess):
        if user_guess[index] == secret_word[index]:
            result += GREEN_BOX
        elif contains_char(secret_word, user_guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    secret = secret
    len_secret: int = len(secret)
    num_turns: int = 1
    win: bool = False
    guess: str = ""
    while num_turns <= len_secret and win == False:
        print("=== Turn", num_turns, "/", len_secret, " ===")
        guess = emojified(input_guess(len(secret)), secret)
        print(guess)
        num_turns += 1
    if guess == secret:
        win == True
        print("You won in ", num_turns, "/", len_secret)
        return win
    if guess != secret and num_turns > len_secret:
        print("X/", len_secret, " - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
