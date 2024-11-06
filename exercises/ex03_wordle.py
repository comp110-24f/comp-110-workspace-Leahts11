"""EX03 Wordle"""

__author__ = "730648923"
secret_word: str = ""


def input_guess(secret_word_length: int) -> str:
    """Takes the user input secret word"""
    word: str = input(f"Enter a {secret_word_length} character word: ")
    while len(word) != secret_word_length:
        word = input(f"That wasn't {secret_word_length} chars! Try again:")
    return word


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
    turn: int = 1
    while turn <= 6:
        print(f"===Turn {turn}/6===")
        word_guess: str = input_guess(len(secret))
        print(emojified(word_guess, secret))
        if word_guess == secret:
            print(f"You won in {turn}/6 turns!")
            return None
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main("codes")
