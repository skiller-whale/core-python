"""
These fortunes are based on the old English rhyme, Monday's child:
https://en.wikipedia.org/wiki/Monday's_Child

Monday's child is fair of face
Tuesday's child is full of grace,
Wednesday's child is full of woe,
Thursday's child has far to go,
Friday's child is loving and giving,
Saturday's child works hard for a living,
But the child who is born on the Sabbath Day
Is bonny and blithe and good and gay.
"""

import datetime


FORTUNES = {
    0: "are fair of face",
    1: "are full of grace",
    2: "are full of woe",
    3: "have far to go",
    4: "are loving and giving",
    5: "work hard for a living",
    6: "are bonny and blithe and good and gay",
}

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def input_number(prompt):
    """Asks the user for an input and converts it to a number"""
    response = input(prompt + " ")
    value = float(response)  # Convert response from a string into a float
    if int(value) == value:  # If number is a whole number, convert to an int
        value = int(value)
    return value


def ask_for_birthday():
    """Asks the user for their birthday, and returns a date"""
    year = input_number("In what year were you born?")
    month = input_number("In what month were you born?")
    day = input_number("On what day of the month were you born?")
    return datetime.date(year=year, month=month, day=day)


def tell_fortune(date):
    """Expects a datetime.date input"""
    if date.year < 1000:
        raise ValueError("Millenium Bug! Fortunes only available after 1000AD")
    day_of_the_week = date.weekday()
    print("You were born on a", DAY_NAMES[day_of_the_week])
    print("You", FORTUNES[day_of_the_week])
