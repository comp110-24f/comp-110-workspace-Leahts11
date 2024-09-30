"""EX02 Chardle"""

__author__ = "730648923"


def input_word() -> str:
    """Takes user input of word and says if word is acceptable"""
    word: str = str(input("Enter a 5-character word: "))
    if len(word) == 5:
        return word
    elif len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """takes user letter"""
    letter: str = str(input("Enter a single character: "))
    if len(letter) == 1:
        return letter
    elif len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    """Checks to see if letter is in word"""
    count: int = 0
    print("Searching for", letter, "in", word)
    if word[0] == letter:
        print(letter, "found at index 0")
        count = count + 1
    if letter == word[1]:
        print(letter, "found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter, "found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter, "found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter, "found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of", letter, "found in", word)
    if count == 1:
        print(count, "instance of", letter, "found in", word)
    if count >= 1:
        print(count, "instances of", letter, "found in", word)
    print(str(count), "instances of", str(letter), "found in", str(word))


def main() -> None:
    """runs program"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
