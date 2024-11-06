"""EX06 dictionary utility fns"""

__author__ = "730648923"


def invert(userdict: dict[str, str]) -> dict[str, str]:
    """Inverts key for value and value for key"""
    dict_inverted: dict[str, str] = {}
    for elem in userdict:
        if userdict[elem] in dict_inverted:
            raise KeyError(f"duplicate {elem} found when inverting dictionary")
        dict_inverted[userdict[elem]] = elem
    return dict_inverted


def favorite_color(usercolor: dict[str, str]) -> str:
    """takes user's name and fav color, and sees which one is seen most frequently"""
    color_count: dict[str, int] = {}
    max_count: str = ""
    order_of_appearance: list[str] = []
    for name in usercolor:
        color = usercolor[name]
        if color not in color_count:
            color_count[color] = 0
            order_of_appearance.append(color)
        color_count[color] += 1
    high_count: int = -1
    for color in order_of_appearance:
        if color_count[color] > high_count:
            max_count = color
            high_count = color_count[color]
    return max_count


def count(values: list[str]) -> dict[str, int]:
    """Create a dict that has number of times value appeared in input list and
    associates a unique key"""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """creates dictionary from list that alphabetizes the list by first letter"""
    result: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]
    return result


def update_attendance(
    days_of_week: dict[str, list[str]], day: str, student: str
) -> None:
    """makes attendance dictionary of who was there in class that day"""
    if day in days_of_week:
        if student not in days_of_week[day]:
            days_of_week[day].append(student)
    else:
        days_of_week[day] = [student]
